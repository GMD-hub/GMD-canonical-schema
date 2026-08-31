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

read_source_snapshot <- function(adapter, source_commit, source_artifact_path,
                                 artifact_id) {
  if (!.is_sha1(source_commit)) {
    stop("source revision must be an explicit lowercase Git commit SHA-1")
  }
  if (!is_valid_source_artifact_path(source_artifact_path, artifact_id)) {
    stop("source revision must keep the same artifact ID and source path")
  }
  token <- adapter$get_token()
  commit <- adapter_fetch_commit(
    adapter$owner,
    adapter$repo,
    source_commit,
    token,
    adapter$http
  )
  if (!identical(commit$sha, source_commit)) {
    stop("source revision did not resolve to the requested immutable commit")
  }
  tree <- adapter_fetch_tree_at(
    adapter$owner,
    adapter$repo,
    source_commit,
    token,
    adapter$http
  )
  blob_sha <- tree$blobs[[source_artifact_path]] %||% NULL
  if (!.is_sha1(blob_sha)) {
    stop(sprintf(
      "source path '%s' is absent from candidate commit '%s'",
      source_artifact_path,
      source_commit
    ))
  }
  blob <- adapter_fetch_blob_by_sha(
    adapter$owner,
    adapter$repo,
    blob_sha,
    token,
    adapter$http
  )
  if (!identical(git_blob_sha_raw(blob$raw), blob_sha)) {
    stop("source bytes do not match the candidate Git blob SHA")
  }
  split <- split_frontmatter_exact(blob$content)
  metadata <- .source_frontmatter(split, artifact_id)
  body_raw <- split$body_raw %||% charToRaw(enc2utf8(split$body %||% ""))
  content_hash <- hash_raw(blob$raw)
  list(
    artifact_id = artifact_id,
    source_artifact_path = source_artifact_path,
    source_commit = source_commit,
    source_artifact_blob_sha = blob_sha,
    sha = blob_sha,
    source_content_sha256 = content_hash,
    content_sha256 = content_hash,
    enrolled_body_sha256 = hash_raw(body_raw),
    content = blob$content,
    raw = blob$raw,
    front = split$front,
    body = split$body %||% "",
    body_raw = body_raw,
    line_ending = split$line_ending %||% "\n",
    metadata = metadata
  )
}

verify_enrolled_source <- function(adapter, record) {
  validate_review_record_v2(record)
  source <- read_source_snapshot(
    adapter,
    record$source_commit,
    record$source_artifact_path,
    record$artifact_id
  )
  fields <- c(
    "source_artifact_blob_sha", "source_content_sha256",
    "enrolled_body_sha256"
  )
  for (field in fields) {
    if (!identical(source[[field]], record[[field]])) {
      stop(source_binding_error(sprintf(
        "enrolled source %s does not match record for '%s'",
        field,
        record$artifact_id
      )))
    }
  }
  source
}

read_source_revision_candidate <- function(adapter, record, candidate_commit) {
  validate_review_record_v2(record)
  read_source_snapshot(
    adapter,
    candidate_commit,
    record$source_artifact_path,
    record$artifact_id
  )
}

read_enrolled_source <- function(adapter, record) {
  validate_review_record_v2(record)
  enrolled <- tryCatch(
    verify_enrolled_source(adapter, record),
    error = function(error) {
      stop(source_binding_error(sprintf(
        "enrolled source snapshot '%s:%s' could not be read or verified: %s",
        record$source_commit,
        record$source_artifact_path,
        conditionMessage(error)
      )))
    }
  )
  enrolled
}

validate_record_source_snapshots <- function(adapter, records) {
  if (!is.list(records)) stop("source records must be a list")
  revisions <- unique(vapply(
    records,
    function(record) record$source_commit,
    character(1)
  ))
  token <- adapter$get_token()
  for (revision in revisions) {
    selected <- Filter(function(record) {
      identical(record$source_commit, revision)
    }, records)
    paths <- vapply(
      selected,
      function(record) record$source_artifact_path,
      character(1)
    )
    adapter_fetch_commit(
      adapter$owner,
      adapter$repo,
      revision,
      token,
      adapter$http
    )
    source_tree <- adapter_fetch_tree_at(
      adapter$owner,
      adapter$repo,
      revision,
      token,
      adapter$http
    )
    source_blobs <- adapter_fetch_blobs_graphql(adapter, revision, paths)
    for (record in selected) {
      path <- record$source_artifact_path
      source <- source_blobs[[path]] %||% NULL
      if (is.null(source) ||
          !identical(source_tree$blobs[[path]], record$source_artifact_blob_sha) ||
          !identical(source$sha, record$source_artifact_blob_sha)) {
        stop(source_binding_error(sprintf(
          "record '%s' source Git identity is not present at its source revision",
          record$artifact_id
        )))
      }
      source_raw <- source$raw %||% charToRaw(enc2utf8(source$content))
      split <- split_frontmatter_exact(source$content)
      .source_frontmatter(split, record$artifact_id)
      body_raw <- split$body_raw %||%
        charToRaw(enc2utf8(split$body %||% ""))
      if (!identical(
        git_blob_sha_raw(source_raw),
        record$source_artifact_blob_sha
      ) || !identical(hash_raw(source_raw), record$source_content_sha256) ||
          !identical(hash_raw(body_raw), record$enrolled_body_sha256)) {
        stop(source_binding_error(sprintf(
          "record '%s' source bytes do not match enrollment",
          record$artifact_id
        )))
      }
    }
  }
  invisible(TRUE)
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

source_pre_publish_check <- function(adapter, record, require_current = FALSE) {
  force(adapter)
  force(record)
  force(require_current)
  function() {
    if (isTRUE(require_current)) {
      assert_source_binding_current(adapter, record)
    } else {
      tryCatch(
        verify_enrolled_source(adapter, record),
        error = function(error) {
          stop(source_drift_error(sprintf(
            "enrolled source changed or became unverifiable: %s",
            conditionMessage(error)
          )))
        }
      )
    }
    invisible(TRUE)
  }
}

source_revision_pre_publish_check <- function(adapter, record, candidate) {
  force(adapter)
  force(record)
  force(candidate)
  function() {
    latest <- tryCatch(
      read_source_revision_candidate(
        adapter,
        record,
        candidate$source_commit
      ),
      error = function(error) {
        stop(source_drift_error(sprintf(
          "candidate source became unverifiable: %s",
          conditionMessage(error)
        )))
      }
    )
    fields <- c(
      "source_commit", "source_artifact_blob_sha", "source_content_sha256",
      "enrolled_body_sha256"
    )
    if (any(!vapply(fields, function(field) {
      identical(latest[[field]], candidate[[field]])
    }, logical(1)))) {
      stop(source_drift_error(
        "candidate source identity changed before publication"
      ))
    }
    invisible(TRUE)
  }
}
