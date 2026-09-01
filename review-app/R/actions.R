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
      (queue_descriptor_is_legacy(descriptor) &&
       !identical(descriptor$source_revision, rec$source_commit))) {
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

.v2_approval_check <- function(
  descriptor, record, binding, persisted_body, actor, role, rationale,
  proposed_content, approved_destination
) {
  validate_approval_gate(
    descriptor = descriptor,
    record = record,
    binding = binding,
    persisted_body = persisted_body,
    actor = actor,
    role = role,
    rationale = rationale,
    proposed_content = proposed_content,
    approved_destination = approved_destination
  )
}

.no_op_report <- function() {
  list(
    ok = TRUE,
    transition_applied = FALSE,
    commit_sha = NULL,
    steps_completed = character(0),
    error = NULL,
    noop = TRUE
  )
}

.write_binding <- function(adapter, record) {
  binding <- check_source_binding(adapter, record)
  if (is.null(binding$enrolled$content)) {
    stop(source_binding_error(sprintf(
      "enrolled source is unavailable for '%s': %s",
      record$artifact_id,
      binding$message %||% binding$code
    )))
  }
  binding
}

.perform_v2_source_revision <- function(
  adapter, rec, blob_sha, branch_head_sha, actor, role, note,
  candidate_source_commit, expected_descriptor_blob_sha = NULL,
  descriptor_path = NULL, max_retries = 1L
) {
  reason <- .require_lifecycle_reason(note, "source re-enrollment")
  if (!.is_sha1(candidate_source_commit)) {
    stop("source re-enrollment requires an explicit immutable candidate commit")
  }
  expected_descriptor <- expected_descriptor_blob_sha
  for (attempt in seq_len(as.integer(max_retries) + 1L)) {
    controls <- .read_v2_controls(
      adapter,
      rec,
      blob_sha,
      expected_descriptor_blob_sha = expected_descriptor,
      descriptor_path = descriptor_path
    )
    if (queue_descriptor_is_legacy(controls$descriptor)) {
      stop("queue compatibility mode is read-only until queue migration")
    }
    authoritative <- controls$record
    if (identical(authoritative$state, "approved")) {
      stop("approved records must be reopened and retire their output first")
    }
    persisted_body <- .read_v2_review_body(
      adapter,
      authoritative,
      verify_enrolled_source(adapter, authoritative)$content
    )
    candidate <- read_source_revision_candidate(
      adapter,
      authoritative,
      candidate_source_commit
    )
    revision <- reenroll_review_record(
      authoritative,
      candidate,
      actor,
      role,
      reason,
      previous_blob_sha = blob_sha
    )
    if (isTRUE(revision$replay)) {
      return(list(
        report = .no_op_report(),
        record = authoritative,
        candidate = candidate,
        replay = TRUE
      ))
    }
    if (!identical(
      queue_membership_identity(authoritative),
      queue_membership_identity(revision$record)
    )) {
      stop("source re-enrollment changed immutable queue membership")
    }
    changes <- stats::setNames(
      list(record_to_yaml(revision$record)),
      ACTION_PATH(rec$artifact_id)
    )
    if (!is.na(persisted_body$sha)) {
      changes[BODY_PATH(rec$artifact_id)] <- list(NULL)
    }
    expected_blobs <- c(
      setNames(list(blob_sha), ACTION_PATH(rec$artifact_id)),
      setNames(
        list(controls$descriptor_blob_sha),
        controls$descriptor_path
      ),
      setNames(list(persisted_body$sha), BODY_PATH(rec$artifact_id))
    )
    report <- adapter_write_with_recovery(
      adapter,
      changes = changes,
      expected_ref_sha = branch_head_sha,
      expected_blob_shas = expected_blobs,
      message = sprintf(
        "re-enroll source for %s by %s",
        rec$artifact_id,
        actor
      ),
      reject_unrelated_head = FALSE,
      pre_publish_check = source_revision_pre_publish_check(
        adapter,
        authoritative,
        candidate
      )
    )
    result <- list(
      report = report,
      record = revision$record,
      candidate = candidate,
      replay = FALSE
    )
    if (report$ok || !identical(report$error$kind, "ref-race") ||
        attempt > as.integer(max_retries)) {
      return(result)
    }
    expected_descriptor <- controls$descriptor_blob_sha
    branch_head_sha <- adapter_branch_head(
      adapter$owner,
      adapter$repo,
      adapter$review_branch,
      adapter$get_token(),
      adapter$http
    )
  }
  stop("source re-enrollment retry loop exhausted")
}

.perform_v2_action <- function(
  adapter, rec, body_sha256, blob_sha, branch_head_sha, action, actor, role,
  approved_content, body, note, assigned_identities = NULL,
  expected_descriptor_blob_sha = NULL, descriptor_path = NULL,
  candidate_source_commit = NULL, max_retries = 1L
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
  if (identical(action, "source-revision")) {
    return(.perform_v2_source_revision(
      adapter,
      rec,
      blob_sha,
      branch_head_sha,
      actor,
      role,
      note,
      candidate_source_commit,
      expected_descriptor_blob_sha,
      descriptor_path,
      max_retries
    ))
  }
  if (action == "approved" && is.null(approved_content)) {
    stop("performing 'approved' requires approved_content")
  }
  if (identical(action, "approved")) {
    note <- .approval_rationale(note)
  }
  if (identical(action, "reopened")) {
    .require_lifecycle_reason(note, "reopen")
  }
  if (!is.null(body) && !identical(hash_body(body), body_sha256)) {
    stop("body_sha256 does not match the body supplied for the action")
  }

  expected_descriptor <- expected_descriptor_blob_sha
  selected_approved_sha <- NULL
  for (attempt in seq_len(as.integer(max_retries) + 1L)) {
    controls <- .read_v2_controls(
      adapter,
      rec,
      blob_sha,
      expected_descriptor_blob_sha = expected_descriptor,
      descriptor_path = descriptor_path
    )
    if (queue_descriptor_is_legacy(controls$descriptor)) {
      stop("queue compatibility mode is read-only until queue migration")
    }
    authoritative <- controls$record
    if (identical(action, "reopened") &&
        !identical(authoritative$state, "approved")) {
      stop("reopen requires an approved record")
    }
    binding <- .write_binding(adapter, authoritative)
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
    approved_blob <- NULL
    approved_path <- NULL
    if (action == "approved") {
      approved_path <- approved_path_for(authoritative$source_artifact_path)
      approved_blob <- .optional_review_blob(adapter, approved_path)
    }
    if (action == "reopened") {
      approved_path <- approved_path_for(authoritative$source_artifact_path)
      approved_blob <- .optional_review_blob(adapter, approved_path)
      verify_approved_output(
        approved_blob,
        binding$enrolled,
        persisted_body$content
      )
    }
    if (action %in% c("approved", "reopened")) {
      if (is.null(selected_approved_sha)) {
        selected_approved_sha <- approved_blob$sha
      } else if (!identical(selected_approved_sha, approved_blob$sha)) {
        stop(stale_write_error(paste(
          "approved destination changed during a concurrent retry;",
          "the action was rejected"
        )))
      }
    }
    approval <- NULL
    occurred_at <- NULL
    event_note <- note
    if (action == "approved") {
      approval <- .v2_approval_check(
        controls$descriptor,
        authoritative,
        binding,
        persisted_body$content,
        actor,
        role,
        note,
        approved_content,
        approved_blob
      )
      occurred_at <- format(
        Sys.time(),
        tz = "UTC",
        usetz = FALSE,
        format = "%Y-%m-%dT%H:%M:%SZ"
      )
      event_note <- approval_attestation_note(
        approval,
        controls$descriptor,
        authoritative,
        actor,
        role,
        occurred_at,
        blob_sha
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
    } else if (action == "reopened") {
      reopen_review_record(
        authoritative,
        actor,
        role,
        note,
        previous_blob_sha = blob_sha,
        body_sha256 = body_sha256
      )
    } else {
      transition(
        authoritative,
        action,
        actor,
        role,
        note = event_note,
        body_sha256 = body_sha256,
        blob_sha = blob_sha,
        occurred_at = occurred_at
      )
    }
    changes <- stats::setNames(
      list(record_to_yaml(updated)),
      ACTION_PATH(authoritative$artifact_id)
    )
    if (action == "approved") {
      changes[[approved_path]] <- approval$approved_content
    }
    if (action == "reopened") {
      changes[approved_path] <- list(NULL)
    }
    if (action == "saved" && !is.null(body)) {
      changes[[BODY_PATH(authoritative$artifact_id)]] <- body
    }
    expected_blobs <- c(
      setNames(list(blob_sha), ACTION_PATH(authoritative$artifact_id)),
      setNames(
        list(controls$descriptor_blob_sha),
        controls$descriptor_path
      ),
      setNames(
        list(persisted_body$sha),
        BODY_PATH(authoritative$artifact_id)
      )
    )
    if (action %in% c("approved", "reopened")) {
      expected_blobs <- c(
        expected_blobs,
        setNames(list(approved_blob$sha), approved_path)
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
        authoritative$artifact_id
      ),
      reject_unrelated_head = FALSE,
      pre_publish_check = source_pre_publish_check(
        adapter,
        authoritative,
        require_current = identical(action, "approved")
      )
    )
    result <- list(report = report, record = updated, binding = binding)
    if (report$ok || !identical(report$error$kind, "ref-race") ||
        attempt > as.integer(max_retries)) {
      return(result)
    }
    expected_descriptor <- controls$descriptor_blob_sha
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
  descriptor_path = NULL, legacy_read_only = FALSE,
  candidate_source_commit = NULL
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
      descriptor_path = descriptor_path,
      candidate_source_commit = candidate_source_commit
    ))
  }
  stop("legacy review records are read-only")
}
