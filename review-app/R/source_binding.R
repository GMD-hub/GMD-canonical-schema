# Immutable source enrollment and current-source drift checks.

source_drift_error <- function(message) {
  structure(
    list(message = message, call = NULL),
    class = c("source_drift", "error", "condition")
  )
}

source_binding_error <- function(message) {
  structure(
    list(message = message, call = NULL),
    class = c("source_binding_error", "error", "condition")
  )
}

new_source_binding_state <- function(
  status,
  code,
  message = NULL,
  record,
  enrolled = NULL,
  current = NULL
) {
  allowed <- c("current", "drifted", "unverifiable")
  if (!status %in% allowed) stop("invalid source binding status")
  list(
    status = status,
    code = code,
    message = message,
    expected = list(
      source_revision = record$source_commit,
      source_artifact_path = record$source_artifact_path,
      source_artifact_blob_sha = record$source_artifact_blob_sha,
      source_content_sha256 = record$source_content_sha256
    ),
    actual = list(
      source_artifact_blob_sha = current$sha %||% NULL,
      source_content_sha256 = current$content_sha256 %||% NULL,
      error = current$error %||% NULL
    ),
    enrolled = enrolled,
    current = current,
    ok = identical(status, "current"),
    drift = !identical(status, "current"),
    reason = message
  )
}

source_binding_is_current <- function(binding) {
  is.list(binding) && identical(binding$status, "current")
}

hash_raw <- function(raw) {
  if (!is.raw(raw)) stop("hash_raw() requires a raw vector")
  digest <- as.character(openssl::sha256(raw))
  attributes(digest) <- NULL
  digest
}

source_content_hash <- function(content) {
  if (!is.character(content) || length(content) != 1L || is.na(content)) {
    stop("source_content_hash() requires one non-NA text value")
  }
  hash_raw(charToRaw(enc2utf8(content)))
}

read_enrolled_source <- function(adapter, record) {
  validate_review_record_v2(record)
  enrolled <- tryCatch(
    adapter_fetch_blob_by_sha(
      adapter$owner,
      adapter$repo,
      record$source_artifact_blob_sha,
      adapter$get_token(),
      adapter$http
    ),
    error = function(error) {
      stop(source_binding_error(sprintf(
        "enrolled source blob '%s' could not be read or verified: %s",
        record$source_artifact_blob_sha,
        conditionMessage(error)
      )))
    }
  )
  actual_hash <- hash_raw(enrolled$raw)
  if (!identical(actual_hash, record$source_content_sha256)) {
    stop(source_binding_error(sprintf(
      "enrolled source content hash does not match record for '%s'",
      record$artifact_id
    )))
  }
  list(
    content = enrolled$content,
    raw = enrolled$raw,
    sha = enrolled$sha,
    content_sha256 = actual_hash
  )
}

check_source_binding <- function(adapter, record) {
  validate_review_record_v2(record)
  enrolled <- tryCatch(
    read_enrolled_source(adapter, record),
    error = function(error) error
  )
  if (inherits(enrolled, "condition")) {
    return(new_source_binding_state(
      status = "unverifiable",
      code = "enrolled_source_unverifiable",
      message = conditionMessage(enrolled),
      record = record,
      current = list(error = conditionMessage(enrolled))
    ))
  }
  current <- tryCatch(
    adapter_read_draft(adapter, record$source_artifact_path),
    error = function(error) {
      list(
        error = conditionMessage(error),
        content = NULL,
        raw = NULL,
        sha = NULL,
        content_sha256 = NULL
      )
    }
  )
  if (!is.null(current$error)) {
    return(new_source_binding_state(
      status = "unverifiable",
      code = "current_source_unreadable",
      message = sprintf("current source could not be read: %s", current$error),
      record = record,
      enrolled = enrolled,
      current = current
    ))
  }
  current_hash <- tryCatch(hash_raw(current$raw), error = function(error) NULL)
  current_git_sha <- tryCatch(
    git_blob_sha_raw(current$raw),
    error = function(error) NULL
  )
  current$content_sha256 <- current_hash
  if (is.null(current_hash) || is.null(current_git_sha) ||
      !.is_sha1(current$sha) || !identical(current_git_sha, current$sha)) {
    return(new_source_binding_state(
      status = "unverifiable",
      code = "current_source_invalid",
      message = "current source bytes do not verify against their Git identity",
      record = record,
      enrolled = enrolled,
      current = current
    ))
  }
  if (!identical(current$sha, record$source_artifact_blob_sha) ||
      !identical(current_hash, record$source_content_sha256)) {
    return(new_source_binding_state(
      status = "drifted",
      code = "source_identity_mismatch",
      message = "current source content or Git blob identity differs from enrollment",
      record = record,
      enrolled = enrolled,
      current = current
    ))
  }
  new_source_binding_state(
    status = "current",
    code = "current",
    record = record,
    enrolled = enrolled,
    current = current
  )
}

assert_source_binding_current <- function(adapter, record) {
  binding <- check_source_binding(adapter, record)
  if (!source_binding_is_current(binding)) {
    error <- source_drift_error(sprintf(
      "source drift detected for %s: %s",
      record$artifact_id,
      binding$message %||% binding$code
    ))
    error$binding <- binding
    stop(error)
  }
  binding
}
