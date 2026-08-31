# Pure source-revision and reopen lifecycle logic.

.require_lifecycle_reason <- function(reason, action) {
  if (!.is_scalar_character(reason) || !nzchar(trimws(reason))) {
    stop(sprintf("%s requires a non-empty reason", action))
  }
  trimws(reason)
}

.source_frontmatter <- function(split, artifact_id) {
  if (is.null(split$front) || is.null(split$front_raw)) {
    stop("source artifact must contain YAML front matter")
  }
  front <- rawToChar(split$front_raw)
  yaml_text <- sub("^---(?:\\r?\\n|$)", "", front, perl = TRUE)
  yaml_text <- sub("(?:\\r?\\n)?---$", "", yaml_text, perl = TRUE)
  metadata <- tryCatch(
    yaml::read_yaml(text = yaml_text),
    error = function(error) {
      stop(sprintf("source front matter is invalid: %s", conditionMessage(error)))
    }
  )
  if (!is.list(metadata)) stop("source front matter must be a YAML mapping")
  declared_id <- metadata$variable_id %||% metadata$artifact_id %||% NULL
  if (!identical(declared_id, artifact_id)) {
    stop(sprintf(
      "source front matter artifact ID does not match '%s'",
      artifact_id
    ))
  }
  metadata
}

.source_revision_replay <- function(record, candidate) {
  fields <- c(
    "source_commit", "source_artifact_blob_sha", "source_content_sha256",
    "enrolled_body_sha256"
  )
  all(vapply(fields, function(field) {
    identical(record[[field]], candidate[[field]])
  }, logical(1)))
}

reenroll_review_record <- function(record, candidate, actor, role, reason,
                                   previous_blob_sha,
                                   occurred_at = enrollment_timestamp()) {
  validate_review_record_v2(record)
  reason <- .require_lifecycle_reason(reason, "source re-enrollment")
  if (!identical(role, "administrator")) {
    stop("only an administrator may re-enroll a source revision")
  }
  if (identical(record$state, "approved")) {
    stop("approved records must be reopened and retire their output first")
  }
  if (!identical(candidate$artifact_id, record$artifact_id) ||
      !identical(
        candidate$source_artifact_path,
        record$source_artifact_path
      )) {
    stop("source re-enrollment must keep the same artifact ID and source path")
  }
  if (.source_revision_replay(record, candidate)) {
    return(list(record = record, replay = TRUE))
  }
  state <- switch(record$state,
    draft = "draft",
    `in-review` = "needs-revision",
    `needs-revision` = "needs-revision",
    stop(sprintf("source re-enrollment is invalid from state '%s'", record$state))
  )
  event <- new_event_v2(
    action = "source-revision",
    from_state = record$state,
    to_state = state,
    actor = actor,
    actor_role = role,
    sequence = length(record$events),
    review_record_blob_sha_before = previous_blob_sha,
    body_sha256 = candidate$enrolled_body_sha256,
    note = reason,
    occurred_at = occurred_at
  )
  updated <- record
  updated$state <- state
  updated$source_commit <- candidate$source_commit
  updated$source_artifact_blob_sha <- candidate$source_artifact_blob_sha
  updated$source_content_sha256 <- candidate$source_content_sha256
  updated$enrolled_body_sha256 <- candidate$enrolled_body_sha256
  updated$current_content_sha256 <- candidate$enrolled_body_sha256
  updated$enrolled_at <- occurred_at
  updated$enrolled_by <- actor
  updated$assessment <- new_empty_assessment()
  updated$events <- c(record$events, list(event))
  validate_review_record_v2(updated)
  list(record = updated, replay = FALSE)
}

reopen_review_record <- function(record, actor, role, reason,
                                 previous_blob_sha, body_sha256,
                                 occurred_at = NULL) {
  reason <- .require_lifecycle_reason(reason, "reopen")
  if (!identical(record$state, "approved")) {
    stop("reopen requires an approved record")
  }
  reopened <- transition(
    record,
    "reopened",
    actor,
    role,
    note = reason,
    body_sha256 = body_sha256,
    blob_sha = previous_blob_sha
  )
  if (!is.null(occurred_at)) {
    reopened$events[[length(reopened$events)]]$occurred_at <- occurred_at
  }
  reopened$assessment <- new_empty_assessment()
  validate_review_record_v2(reopened)
  reopened
}

verify_approved_output <- function(approved_blob, enrolled_source, reviewed_body) {
  if (is.null(approved_blob$content) || !.is_sha1(approved_blob$sha %||% NULL)) {
    stop("approved output is missing for the approved record")
  }
  approved_raw <- approved_blob$raw %||%
    charToRaw(enc2utf8(approved_blob$content))
  if (!identical(git_blob_sha_raw(approved_raw), approved_blob$sha)) {
    stop("approved output bytes do not match their Git blob SHA")
  }
  expected <- join_enrolled_body(
    enrolled_source$front,
    reviewed_body,
    separator = enrolled_source$line_ending
  )
  if (!identical(approved_blob$content, expected)) {
    stop("approved output is inconsistent with the enrolled source and reviewed body")
  }
  invisible(TRUE)
}
