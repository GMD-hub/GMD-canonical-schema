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

adapter_read_queue_descriptor <- function(adapter, descriptor_path = NULL) {
  paths <- if (is.null(descriptor_path)) {
    c(QUEUE_DESCRIPTOR_PATH, LEGACY_QUEUE_MANIFEST_PATH)
  } else {
    descriptor_path
  }
  for (path in paths) {
    blob <- tryCatch(
      adapter_read_review(adapter, path),
      error = function(error) error
    )
    if (!inherits(blob, "condition")) {
      return(list(
        descriptor = parse_queue_control(blob$content, path),
        content = blob$content,
        sha = blob$sha,
        path = path
      ))
    }
    if (!grepl(
      "404|not found|blob not found",
      conditionMessage(blob),
      ignore.case = TRUE
    )) {
      stop(blob)
    }
  }
  stop(.queue_error("queue descriptor could not be read"))
}

.read_v2_controls <- function(
  adapter, rec, record_blob_sha, expected_descriptor_blob_sha = NULL,
  descriptor_path = NULL
) {
  control <- adapter_read_queue_descriptor(adapter, descriptor_path)
  if (!is.null(expected_descriptor_blob_sha) &&
      !identical(control$sha, expected_descriptor_blob_sha)) {
    stop(stale_write_error(
      "queue descriptor changed since load; reload before applying the action"
    ))
  }
  descriptor <- control$descriptor
  if (!identical(descriptor$queue_id, rec$queue_id) ||
      !identical(descriptor$source_revision, rec$source_commit)) {
    stop(.queue_error(
      "review record identity does not match the current queue descriptor"
    ))
  }
  current_record <- adapter_read_review(adapter, ACTION_PATH(rec$artifact_id))
  if (!identical(current_record$sha, record_blob_sha)) {
    stop(stale_write_error(
      "review record changed since load; reload before applying the action"
    ))
  }
  parsed <- parse_review_record(current_record$content)
  validate_review_record_v2(parsed)
  if (!identical(queue_record_identity(parsed), queue_record_identity(rec))) {
    stop(stale_write_error(
      "review record enrollment identity changed; reload before applying the action"
    ))
  }
  list(
    descriptor = descriptor,
    descriptor_blob_sha = control$sha,
    descriptor_path = control$path,
    record = parsed,
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

.v2_approval_check <- function(record, binding) {
  if (!queue_approval_eligible(record, binding)) {
    reasons <- c(
      "approval rubric gate is not installed",
      if (!source_binding_is_current(binding)) {
        "source binding is unresolved"
      },
      if (length(record$blocker_refs)) {
        paste0("record blockers: ", paste(record$blocker_refs, collapse = ", "))
      },
      if (!assessment_approval_complete(record$assessment)) {
        "assessment is incomplete"
      }
    )
    stop(sprintf("approval denied: %s", paste(reasons, collapse = "; ")))
  }
  invisible(TRUE)
}

.perform_v2_action <- function(
  adapter, rec, body_sha256, blob_sha, branch_head_sha, action, actor, role,
  approved_content, body, note, assigned_identities = NULL,
  expected_descriptor_blob_sha = NULL, descriptor_path = NULL,
  max_retries = 1L
) {
  validate_review_record_v2(rec)
  if (!is_valid_artifact_id(rec$artifact_id)) stop("invalid artifact ID")
  if (!.is_sha1(blob_sha)) stop("v2 actions require a Git SHA-1 record blob")
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

  expected_descriptor <- expected_descriptor_blob_sha
  updated <- NULL
  updated_yaml <- NULL
  controls <- NULL
  binding <- NULL
  authoritative <- NULL
  persisted_body <- NULL
  approved_blob <- NULL
  for (attempt in seq_len(as.integer(max_retries) + 1L)) {
    controls <- .read_v2_controls(
      adapter,
      rec,
      blob_sha,
      expected_descriptor_blob_sha = expected_descriptor,
      descriptor_path = descriptor_path
    )
    if (queue_descriptor_is_legacy(controls$descriptor)) {
      stop("production-v2 compatibility is read-only until queue migration")
    }
    if (identical(action, "reopened")) {
      stop("v2 reopen is unavailable until the source-revision lifecycle is installed")
    }
    authoritative <- controls$record
    binding <- assert_source_binding_current(adapter, authoritative)
    if (is.null(updated)) {
      persisted_body <- .read_v2_review_body(
        adapter,
        authoritative,
        binding$enrolled$content
      )
      if (action != "saved" &&
          !identical(hash_body(persisted_body$content), body_sha256)) {
        stop(stale_write_error(
          "the supplied body hash does not match the persisted reviewed body"
        ))
      }
      if (action == "approved") {
        .v2_approval_check(authoritative, binding)
        approved_blob <- .optional_review_blob(
          adapter,
          approved_path_for(authoritative$source_artifact_path)
        )
      }
      updated <- if (action %in% c("saved", "assigned")) {
        replaced <- record_action(
          authoritative,
          action,
          actor,
          role,
          note = note,
          body_sha256 = body_sha256,
          blob_sha = blob_sha
        )
        if (action == "assigned" && !is.null(assigned_identities)) {
          set_assigned_to(replaced, assigned_identities)
        } else {
          replaced
        }
      } else {
        transition(
          authoritative,
          action,
          actor,
          role,
          note = note,
          body_sha256 = body_sha256,
          blob_sha = blob_sha
        )
      }
      updated_yaml <- record_to_yaml(updated)
    } else if (!identical(controls$record_blob_sha, blob_sha)) {
      stop(stale_write_error(
        "review record changed during a concurrent retry; no transition applied"
      ))
    }
    changes <- list()
    changes[[ACTION_PATH(rec$artifact_id)]] <- updated_yaml
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
      changes[[approved_path_for(authoritative$source_artifact_path)]] <-
        approved_content
    }
    if (action == "saved" && !is.null(body)) {
      changes[[BODY_PATH(rec$artifact_id)]] <- body
    }
    expected_blobs <- c(
      setNames(list(blob_sha), ACTION_PATH(rec$artifact_id)),
      setNames(
        list(controls$descriptor_blob_sha),
        controls$descriptor_path
      ),
      setNames(list(persisted_body$sha), BODY_PATH(rec$artifact_id))
    )
    if (action == "approved") {
      expected_blobs <- c(
        expected_blobs,
        setNames(
          list(approved_blob$sha),
          approved_path_for(authoritative$source_artifact_path)
        )
      )
    }
    report <- adapter_write_with_recovery(
      adapter,
      changes = changes,
      expected_ref_sha = branch_head_sha,
      expected_blob_shas = expected_blobs,
      message = sprintf(
        "review action '%s' by %s on %s",
        action,
        actor,
        rec$artifact_id
      ),
      reject_unrelated_head = FALSE
    )
    if (report$ok ||
        !report$error$kind %in% c("stale", "ref-race") ||
        attempt > as.integer(max_retries)) {
      return(list(report = report, record = updated, binding = binding))
    }
    # A retry is safe only when the selected record and descriptor did not
    # change. Unrelated record commits do not create a data-level conflict.
    latest <- .read_v2_controls(
      adapter,
      rec,
      blob_sha,
      expected_descriptor_blob_sha = controls$descriptor_blob_sha,
      descriptor_path = controls$descriptor_path
    )
    if (!identical(
      latest$descriptor_blob_sha,
      controls$descriptor_blob_sha
    )) {
      return(list(report = report, record = updated, binding = binding))
    }
    expected_descriptor <- latest$descriptor_blob_sha
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
  assigned_identities = NULL, expected_descriptor_blob_sha = NULL,
  descriptor_path = NULL, legacy_read_only = FALSE
) {
  if (isTRUE(adapter$read_only) ||
      identical(adapter$review_branch, "review") ||
      isTRUE(legacy_read_only)) {
    stop("legacy review records are read-only")
  }
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
      expected_descriptor_blob_sha = expected_descriptor_blob_sha,
      descriptor_path = descriptor_path
    ))
  }
  stop("legacy review records are read-only")
}
