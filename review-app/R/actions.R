# Role-gated actions and production queue writes.

ACTION_PATH <- function(artifact_id) {
  if (!is_safe_artifact_id(artifact_id)) {
    stop("invalid artifact ID")
  }
  sprintf("extraction/30_review/%s.review.yml", artifact_id)
}

BODY_PATH <- function(artifact_id) {
  if (!is_safe_artifact_id(artifact_id)) {
    stop("invalid artifact ID")
  }
  sprintf("extraction/30_review/%s.body.md", artifact_id)
}

record_to_yaml <- function(rec) {
  validate_review_record(rec)
  canonical_yaml(rec)
}

approved_path_for <- function(source_artifact_path) {
  if (!is_valid_source_artifact_path(source_artifact_path)) {
    stop("invalid source artifact path")
  }
  sub(
    "^extraction/20_drafts/",
    "extraction/40_approved/",
    source_artifact_path
  )
}

adapter_read_queue_manifest <- function(adapter) {
  adapter_read_review(adapter, QUEUE_MANIFEST_PATH)
}

adapter_read_queue_index <- function(adapter) {
  adapter_read_review(adapter, QUEUE_INDEX_PATH)
}

.queue_row_for <- function(index, artifact_id) {
  rows <- index$rows %||% index
  matches <- which(vapply(rows, function(row) {
    identical(row$artifact_id, artifact_id)
  }, logical(1)))
  if (length(matches) != 1L) {
    stop(sprintf("queue index must contain exactly one row for '%s'", artifact_id))
  }
  rows[[matches[[1L]]]]
}

.replace_queue_row <- function(index, row) {
  rows <- index$rows %||% index
  matches <- which(vapply(rows, function(candidate) {
    identical(candidate$artifact_id, row$artifact_id)
  }, logical(1)))
  if (length(matches) != 1L) {
    stop(sprintf("queue index must contain exactly one row for '%s'", row$artifact_id))
  }
  rows[[matches[[1L]]]] <- row
  if (!is.null(index$rows)) {
    index$rows <- rows
    return(index)
  }
  rows
}

.index_row_with_update <- function(index, artifact_id, updated, blob_sha, manifest) {
  rows <- index$rows
  hit <- which(vapply(rows, function(candidate) {
    identical(candidate$artifact_id, artifact_id)
  }, logical(1)))
  if (length(hit) != 1L) stop("queue index selected row is missing or duplicated")
  current <- rows[[hit[[1L]]]]
  current$state <- updated$state
  current$review_round <- as.integer(updated$review_round)
  current$assigned_to <- updated$assigned_to
  current$record_blob_sha <- blob_sha
  current$governance_blocked <- length(queue_open_blockers(manifest, artifact_id)) > 0L
  current$source_drift <- FALSE
  validate_queue_index_row(current)
  rows[[hit[[1L]]]] <- current
  index$rows <- rows
  index
}

.read_v2_controls <- function(
  adapter, rec, record_blob_sha, expected_manifest_blob_sha = NULL,
  expected_index_blob_sha = NULL
) {
  manifest_blob <- adapter_read_queue_manifest(adapter)
  if (!is.null(expected_manifest_blob_sha) &&
      !identical(manifest_blob$sha, expected_manifest_blob_sha)) {
    stop(stale_write_error(
      "queue manifest changed since load; reload before applying the action"
    ))
  }
  manifest <- parse_queue_manifest(manifest_blob$content)
  if (!identical(manifest$queue_id, rec$queue_id)) {
    stop(.queue_error("review record queue_id does not match the current queue manifest"))
  }
  index_blob <- adapter_read_queue_index(adapter)
  index_changed_since_load <- !is.null(expected_index_blob_sha) &&
    !identical(index_blob$sha, expected_index_blob_sha)
  if (index_changed_since_load) {
    stop(stale_write_error(
      "queue index changed since load; reload before applying the action"
    ))
  }
  index <- parse_queue_index_blob(index_blob$content, manifest)
  row <- .queue_row_for(index, rec$artifact_id)
  if (!identical(row$record_blob_sha, record_blob_sha) ||
      !identical(row$source_artifact_path, rec$source_artifact_path)) {
    stop(stale_write_error(
      "queue row changed since load; reload before applying the action"
    ))
  }
  current_record <- adapter_read_review(adapter, ACTION_PATH(rec$artifact_id))
  if (!identical(current_record$sha, record_blob_sha)) {
    stop(stale_write_error(
      "review record changed since load; reload before applying the action"
    ))
  }
  list(
    manifest = manifest,
    manifest_blob_sha = manifest_blob$sha,
    index = index,
    index_blob_sha = index_blob$sha,
    row = row,
    index_changed_since_load = index_changed_since_load,
    record = parse_review_record(current_record$content),
    record_blob_sha = current_record$sha
  )
}

.read_v2_review_body <- function(adapter, record, enrolled_content) {
  body_blob <- tryCatch(
    adapter_read_review(adapter, BODY_PATH(record$artifact_id)),
    error = function(error) {
      if (grepl("404|not found|blob not found", conditionMessage(error), ignore.case = TRUE)) {
        return(list(
          content = split_frontmatter_exact(enrolled_content)$body,
          sha = NA_character_
        ))
      }
      stop(error)
    }
  )
  body <- body_blob$content
  if (!identical(hash_body(body), record$current_content_sha256)) {
    stop(stale_write_error(
      "persisted review body hash does not match the loaded record"
    ))
  }
  list(content = body, sha = body_blob$sha %||% NA_character_)
}

.optional_review_blob <- function(adapter, path) {
  tryCatch(
    adapter_read_review(adapter, path),
    error = function(error) {
      if (grepl("404|not found|blob not found", conditionMessage(error), ignore.case = TRUE)) {
        return(list(content = NULL, sha = NA_character_))
      }
      stop(error)
    }
  )
}

.updated_v2_queue_row <- function(
  row, updated, new_record_blob_sha, manifest
) {
  row$state <- updated$state
  row$review_round <- as.integer(updated$review_round)
  row$assigned_to <- updated$assigned_to
  row$record_blob_sha <- new_record_blob_sha
  row$governance_blocked <- length(queue_open_blockers(
    manifest,
    updated$artifact_id
  )) > 0L
  row$source_drift <- FALSE
  validate_queue_index_row(row)
  row
}

.v2_approval_check <- function(manifest, record, binding) {
  if (!queue_approval_eligible(manifest, record)) {
    blockers <- queue_open_blockers(manifest, record$artifact_id)
    reasons <- c(
      if (!identical(manifest$approval_mode, "enabled")) {
        "approval_mode is disabled"
      },
      if (length(blockers)) {
        paste0("open blockers: ", paste(
          vapply(blockers, function(blocker) blocker$id, character(1)),
          collapse = ", "
        ))
      },
      if (!assessment_approval_complete(record$assessment)) {
        "assessment is incomplete"
      }
    )
    stop(sprintf("approval denied: %s", paste(reasons, collapse = "; ")))
  }
  if (isTRUE(binding$drift)) {
    stop(source_drift_error("approval denied because the source has drifted"))
  }
  invisible(TRUE)
}

.perform_v2_action <- function(
  adapter, rec, body_sha256, blob_sha, branch_head_sha, action, actor, role,
  approved_content, body, note, assigned_identities = NULL,
  assessment_payload = NULL,
  expected_manifest_blob_sha = NULL, expected_index_blob_sha = NULL,
  max_retries = 1L
) {
  validate_review_record_v2(rec)
  if (!is_valid_artifact_id(rec$artifact_id)) stop("invalid artifact ID")
  if (!.is_sha1(blob_sha)) stop("v2 actions require a Git SHA-1 record blob")
  if (!.is_sha1(expected_manifest_blob_sha) ||
      !.is_sha1(expected_index_blob_sha)) {
    stop("v2 actions require loaded manifest and index blob identities")
  }
  if (!authorize(role, action)) {
    stop(sprintf(
      "unauthorized: role '%s' cannot perform action '%s'",
      role %||% "(none)",
      action
    ))
  }
  if (action == "approved" && is.null(approved_content)) {
    stop("performing 'approved' requires approved_content")
  }
  if (!is.null(body) && !identical(hash_body(body), body_sha256)) {
    stop("body_sha256 does not match the body supplied for the action")
  }

  expected_manifest <- expected_manifest_blob_sha
  expected_index <- expected_index_blob_sha
  for (attempt in seq_len(as.integer(max_retries) + 1L)) {
    controls <- .read_v2_controls(
      adapter,
      rec,
      blob_sha,
      expected_manifest_blob_sha = expected_manifest,
      expected_index_blob_sha = expected_index
    )
    persisted <- controls$record
    if (!identical(record_to_yaml(rec), record_to_yaml(persisted))) {
      stop(stale_write_error("caller record differs from persisted review record"))
    }
    default_head <- adapter_branch_head(
      adapter$owner, adapter$repo, adapter$default_branch,
      adapter$get_token(), adapter$http
    )
    binding <- assert_source_binding_current(adapter, persisted, default_head)
    if (isTRUE(controls$index_changed_since_load) && attempt > 1L) {
      stop(stale_write_error(
        "queue index changed during the action; reload before applying the action"
      ))
    }
    persisted_body <- .read_v2_review_body(
      adapter, persisted, binding$enrolled$content
    )
    if (action != "saved" &&
        !identical(hash_body(persisted_body$content), body_sha256)) {
      stop(stale_write_error(
        "the supplied body hash does not match the persisted reviewed body"
      ))
    }
    approved_blob <- NULL
    if (action == "approved") {
      machine <- build_machine_assessment(
        adapter, persisted, persisted_body$content, binding,
        evidence_commit = persisted$assessment$binding$evidence_commit,
        agent_review_authority = controls$manifest$agent_review
      )
      layer1_identity <- c("result", "validator_id", "evidence_generated_at")
      if (!identical(persisted$assessment$binding, machine$binding) ||
          !identical(
            persisted$assessment$layer1[layer1_identity],
            machine$layer1[layer1_identity]
          ) || !identical(persisted$assessment$agent_review, machine$agent_review)) {
        stop("approval denied: persisted assessment binding or evidence is stale")
      }
      .v2_approval_check(controls$manifest, persisted, binding)
      approved_blob <- .optional_review_blob(
        adapter, approved_path_for(persisted$source_artifact_path)
      )
    }
    updated <- if (action %in% c("saved", "assigned", "assessed")) {
      replaced <- record_action(
        persisted, action, actor, role, note = note,
        body_sha256 = body_sha256, blob_sha = blob_sha
      )
      if (action == "assigned" && !is.null(assigned_identities)) {
        replaced <- set_assigned_to(replaced, assigned_identities)
      }
      if (action == "assessed") {
        if (is.null(assessment_payload)) stop("assessed action requires assessment_payload")
        machine <- build_machine_assessment(
          adapter, persisted, persisted_body$content, binding,
          evidence_commit = default_head,
          agent_review_authority = controls$manifest$agent_review
        )
        if (!identical(machine$layer1$result, "pass")) {
          stop("assessment denied because current Layer 1 does not pass")
        }
        replaced$assessment <- stamp_human_assessment(
          machine, assessment_payload, actor,
          replaced$events[[length(replaced$events)]]$occurred_at
        )
      }
      replaced
    } else {
      transition(
        persisted, action, actor, role, note = note,
        body_sha256 = body_sha256, blob_sha = blob_sha
      )
    }
    if (action == "submitted") {
      updated$assessment <- build_machine_assessment(
        adapter, persisted, persisted_body$content, binding,
        evidence_commit = default_head,
        agent_review_authority = controls$manifest$agent_review
      )
      if (!identical(updated$assessment$layer1$result, "pass")) {
        stop("submission denied: current Layer 1 structural gate failed")
      }
    }
    validate_review_record_v2(updated)
    updated_yaml <- record_to_yaml(updated)
    new_record_sha <- tryCatch(
      git_blob_sha(updated_yaml),
      error = function(error) stop(sprintf(
        "could not compute the updated record identity: %s",
        conditionMessage(error)
      ))
    )
    updated_index <- .index_row_with_update(
      controls$index,
      persisted$artifact_id,
      updated,
      new_record_sha,
      controls$manifest
    )
    changes <- list()
    changes[[ACTION_PATH(persisted$artifact_id)]] <- updated_yaml
    changes[[QUEUE_INDEX_PATH]] <- serialize_queue_index(updated_index)
    if (action == "approved") {
      enrolled_split <- split_frontmatter_exact(binding$enrolled$content)
      enrolled_front <- enrolled_split$front
      if (is.null(enrolled_front) ||
          !frontmatter_unchanged(enrolled_front, approved_content)) {
        stop("approved content must preserve the enrolled YAML front matter")
      }
      approved_content <- join_enrolled_body(
        enrolled_front,
        persisted_body$content,
        separator = enrolled_split$line_ending
      )
      changes[[approved_path_for(persisted$source_artifact_path)]] <- approved_content
    }
    if (action == "saved" && !is.null(body)) {
      changes[[BODY_PATH(persisted$artifact_id)]] <- body
    }
    expected_blobs <- c(
      setNames(list(blob_sha), ACTION_PATH(persisted$artifact_id)),
      setNames(list(controls$index_blob_sha), QUEUE_INDEX_PATH),
      setNames(list(controls$manifest_blob_sha), QUEUE_MANIFEST_PATH),
      setNames(list(persisted_body$sha), BODY_PATH(persisted$artifact_id))
    )
    if (action == "approved") {
      expected_blobs <- c(
        expected_blobs,
        setNames(
          list(approved_blob$sha),
          approved_path_for(persisted$source_artifact_path)
        )
      )
    }
    source_head <- if (action == "approved") default_head else NULL
    pre_publish_check <- if (action == "approved") function() {
      current_head <- adapter_branch_head(
        adapter$owner, adapter$repo, adapter$default_branch,
        adapter$get_token(), adapter$http
      )
      current <- adapter_fetch_blob(
        adapter$owner, adapter$repo, persisted$source_artifact_path,
        current_head, adapter$get_token(), adapter$http
      )
      if (!identical(current_head, source_head) ||
          !identical(current$sha, persisted$source_artifact_blob_sha) ||
          !identical(source_content_hash(current$content), persisted$source_content_sha256)) {
        stop(source_drift_error("source changed before approval publication"))
      }
      invisible(TRUE)
    } else NULL
    report <- adapter_write_with_recovery(
      adapter,
      changes = changes,
      expected_ref_sha = branch_head_sha,
      expected_blob_shas = expected_blobs,
      message = sprintf(
        "review action '%s' by %s on %s",
        action,
        actor,
        persisted$artifact_id
      ),
      pre_publish_check = pre_publish_check
    )
    if (report$ok ||
        !identical(report$error$kind, "ref-race") ||
        attempt > as.integer(max_retries)) {
      return(list(report = report, record = updated, binding = binding))
    }
    # Only a proven review-ref publication race is retryable. All selected-path
    # staleness is terminal inside adapter_write_with_recovery().
    latest <- .read_v2_controls(adapter, rec, blob_sha)
    same_row <- identical(latest$row, controls$row)
    same_manifest <- identical(latest$manifest_blob_sha, controls$manifest_blob_sha)
    same_index <- identical(latest$index_blob_sha, controls$index_blob_sha)
    latest_body <- .read_v2_review_body(adapter, latest$record, binding$enrolled$content)
    same_body <- identical(latest_body$sha, persisted_body$sha)
    latest_destination <- if (action == "approved") .optional_review_blob(
      adapter, approved_path_for(persisted$source_artifact_path)
    ) else NULL
    same_destination <- action != "approved" ||
      identical(latest_destination$sha, approved_blob$sha)
    if (!same_row || !same_manifest || !same_index || !same_body ||
        !same_destination) {
      return(list(report = report, record = updated, binding = binding))
    }
    expected_manifest <- latest$manifest_blob_sha
    expected_index <- latest$index_blob_sha
    branch_head_sha <- adapter_branch_head(
      adapter$owner,
      adapter$repo,
      adapter$review_branch,
      adapter$get_token(),
      adapter$http
    )
  }
  stop("action retry loop exhausted")
}

#' Serialize a review record to YAML and persist a role-gated action.
perform_action <- function(
  adapter, rec, body_sha256, blob_sha, branch_head_sha, action, actor, role,
  approved_content = NULL, body = NULL, note = NULL,
  assigned_identities = NULL, assessment_payload = NULL,
  expected_manifest_blob_sha = NULL, expected_index_blob_sha = NULL
) {
  if (is_v2_review_record(rec)) {
    return(.perform_v2_action(
      adapter,
      rec,
      body_sha256,
      blob_sha,
      branch_head_sha,
      action,
      actor,
      role,
      approved_content,
      body,
      note,
      assigned_identities = assigned_identities,
      assessment_payload = assessment_payload,
      expected_manifest_blob_sha = expected_manifest_blob_sha,
      expected_index_blob_sha = expected_index_blob_sha
    ))
  }
  stop("legacy calibration records are read-only")
}
