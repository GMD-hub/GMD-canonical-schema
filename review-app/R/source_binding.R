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

check_source_binding <- function(adapter, record, current_commit = NULL) {
  validate_review_record_v2(record)
  enrolled <- read_enrolled_source(adapter, record)
  current <- tryCatch(
    if (is.null(current_commit)) {
      adapter_read_draft(adapter, record$source_artifact_path)
    } else {
      adapter_fetch_blob(
        adapter$owner, adapter$repo, record$source_artifact_path,
        current_commit, adapter$get_token(), adapter$http
      )
    },
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
    return(list(
      ok = FALSE,
      drift = TRUE,
      reason = sprintf("current source could not be read: %s", current$error),
      enrolled = enrolled,
      current = current
    ))
  }
  current_hash <- tryCatch(hash_raw(current$raw), error = function(error) NULL)
  current_git_sha <- tryCatch(
    git_blob_sha_raw(current$raw),
    error = function(error) NULL
  )
  if (is.null(current_hash) || is.null(current_git_sha) ||
      !.is_sha1(current$sha) || !identical(current_git_sha, current$sha) ||
      !identical(current$sha, record$source_artifact_blob_sha) ||
      !identical(current_hash, record$source_content_sha256)) {
    return(list(
      ok = FALSE,
      drift = TRUE,
      reason = "current source content or Git blob identity differs from enrollment",
      enrolled = enrolled,
      current = c(current, list(content_sha256 = current_hash))
    ))
  }
  current$content_sha256 <- current_hash
  list(
    ok = identical(current$sha, record$source_artifact_blob_sha) &&
      identical(current_hash, record$source_content_sha256),
    drift = !identical(current$sha, record$source_artifact_blob_sha) ||
      !identical(current_hash, record$source_content_sha256),
    reason = if (identical(current$sha, record$source_artifact_blob_sha) &&
                identical(current_hash, record$source_content_sha256)) {
      NULL
    } else {
      "current source content or Git blob identity differs from enrollment"
    },
    enrolled = enrolled,
    current = current
  )
}

assert_source_binding_current <- function(adapter, record, current_commit = NULL) {
  binding <- check_source_binding(adapter, record, current_commit)
  if (isTRUE(binding$drift)) {
    stop(source_drift_error(sprintf(
      "source drift detected for %s: %s",
      record$artifact_id,
      binding$reason
    )))
  }
  binding
}
