# Authenticated non-UI queue initialization and migration.

QUEUE_WRITE_MAX_PAYLOAD_BYTES <- 8000000L

queue_administration_authorized <- function(actor, action) {
  role_map_path <- reviewapp_role_map_path()
  if (is.null(role_map_path)) {
    stop("queue administration requires the configured repository role map")
  }
  auth <- session_auth(actor, role_map_path)
  isTRUE(auth$authorized) && authorize(auth$role, action)
}

queue_source_paths <- function(tree_blobs) {
  if (!is.list(tree_blobs) || is.null(names(tree_blobs))) {
    stop("source tree blobs must be a named list")
  }
  paths <- sort(grep(
    paste0(
      "^extraction/20_drafts/",
      "[a-z0-9][a-z0-9_-]*/VAR-[a-z0-9]+[.]md$"
    ),
    names(tree_blobs),
    value = TRUE
  ))
  if (!length(paths)) stop("source tree contains no reviewable draft records")
  ids <- sub("^.*[/]([^/]+)[.]md$", "\\1", paths)
  if (anyDuplicated(ids)) stop("source draft set contains duplicate artifact IDs")
  paths
}

enrollment_timestamp <- function(now = Sys.time()) {
  format(now, tz = "UTC", usetz = FALSE, format = "%Y-%m-%dT%H:%M:%SZ")
}

assert_queue_namespace_empty <- function(tree) {
  paths <- names(tree$blobs %||% list())
  governed <- paths[grepl(
    "^extraction/(30_review|40_approved)/",
    paths
  )]
  allowed <- c(
    "extraction/30_review/.gitkeep",
    "extraction/40_approved/.gitkeep"
  )
  occupied <- setdiff(governed, allowed)
  if (length(occupied)) {
    stop(sprintf(
      paste(
        "queue initialization requires an empty review and approved namespace;",
        "found: %s"
      ),
      paste(sort(occupied), collapse = ", ")
    ))
  }
  invisible(TRUE)
}

generate_queue_enrollment <- function(
  source_revision,
  source_tree,
  source_blobs,
  actor,
  queue_id,
  created_at = enrollment_timestamp(),
  source_paths = queue_source_paths(source_tree$blobs),
  progress = NULL
) {
  if (!.is_sha1(source_revision)) {
    stop("enrollment requires a lowercase Git SHA-1 source revision")
  }
  if (!.is_scalar_character(actor)) {
    stop("enrollment requires an authenticated administrator identity")
  }
  .require_queue_scalar(queue_id, "queue_id")
  if (!is.list(source_blobs) || is.null(names(source_blobs))) {
    stop("source blobs must be a named list")
  }
  source_paths <- sort(as.character(source_paths))
  if (!length(source_paths) || anyDuplicated(source_paths)) {
    stop("enrollment source paths must be non-empty and unique")
  }
  missing <- setdiff(source_paths, names(source_blobs))
  if (length(missing)) {
    stop(sprintf(
      "source blob batch omitted paths: %s",
      paste(missing, collapse = ", ")
    ))
  }
  records <- list()
  for (i in seq_along(source_paths)) {
    path <- source_paths[[i]]
    source <- source_blobs[[path]]
    if (!is.list(source) || !.is_scalar_character(source$content) ||
        !.is_sha1(source$sha)) {
      stop(sprintf("source blob for '%s' is incomplete", path))
    }
    if (!identical(source$sha, source_tree$blobs[[path]])) {
      stop(sprintf("source blob identity mismatch for '%s'", path))
    }
    source_raw <- source$raw %||% charToRaw(enc2utf8(source$content))
    if (!identical(git_blob_sha_raw(source_raw), source$sha)) {
      stop(sprintf("source blob bytes do not verify for '%s'", path))
    }
    split <- split_frontmatter_exact(source$content)
    body_sha <- hash_raw(
      split$body_raw %||% charToRaw(enc2utf8(split$body %||% ""))
    )
    artifact_id <- sub("^.*[/]([^/]+)[.]md$", "\\1", path)
    record <- new_review_record_v2(
      artifact_id = artifact_id,
      queue_id = queue_id,
      source_artifact_path = path,
      source_commit = source_revision,
      source_artifact_blob_sha = source$sha,
      source_content_sha256 = hash_raw(source_raw),
      enrolled_body_sha256 = body_sha,
      current_content_sha256 = body_sha,
      enrolled_at = created_at,
      enrolled_by = actor
    )
    record_path <- ACTION_PATH(artifact_id)
    content <- record_to_yaml(record)
    records[[record_path]] <- list(
      artifact_id = artifact_id,
      record = record,
      content = content,
      blob_sha = git_blob_sha(content)
    )
    if (!is.null(progress)) progress(i, length(source_paths))
  }
  record_values <- lapply(unname(records), function(item) item$record)
  descriptor <- new_queue_descriptor(
    queue_id = queue_id,
    source_revision = source_revision,
    created_at = created_at,
    created_by = actor,
    expected_record_count = length(records),
    record_set_sha256 = queue_record_set_digest(record_values)
  )
  validate_queue_record_set(record_values, descriptor)
  changes <- lapply(records, function(item) item$content)
  changes[[QUEUE_DESCRIPTOR_PATH]] <- canonical_yaml(descriptor)
  payload_bytes <- nchar(
    jsonlite::toJSON(
      lapply(names(changes), function(path) {
        list(
          path = path,
          mode = "100644",
          type = "blob",
          content = changes[[path]]
        )
      }),
      auto_unbox = TRUE
    ),
    type = "bytes"
  )
  list(
    records = records,
    descriptor = descriptor,
    descriptor_yaml = changes[[QUEUE_DESCRIPTOR_PATH]],
    changes = changes,
    payload_bytes = payload_bytes
  )
}

validate_generated_enrollment <- function(generated) {
  if (!is.list(generated) || is.null(generated$records) ||
      is.null(generated$descriptor)) {
    stop("generated enrollment is incomplete")
  }
  records <- lapply(unname(generated$records), function(item) item$record)
  validate_queue_record_set(records, generated$descriptor)
  invisible(TRUE)
}

initialize_review_queue <- function(
  adapter,
  actor,
  source_revision,
  queue_id,
  expected_record_count,
  expected_path_set_sha256,
  source_paths = NULL,
  progress = NULL,
  max_payload_bytes = QUEUE_WRITE_MAX_PAYLOAD_BYTES
) {
  .assert_writable_adapter(adapter)
  if (!queue_administration_authorized(
    actor,
    "initialize"
  )) {
    stop("only an authenticated administrator may initialize a review queue")
  }
  if (!.is_scalar_character(actor)) {
    stop("queue initialization requires an authenticated actor")
  }
  if (!.is_sha1(source_revision)) {
    stop("queue initialization requires a lowercase Git SHA-1 source revision")
  }
  token <- adapter$get_token()
  review_head <- adapter_branch_head(
    adapter$owner,
    adapter$repo,
    adapter$review_branch,
    token,
    adapter$http
  )
  review_tree <- adapter_fetch_tree_at(
    adapter$owner,
    adapter$repo,
    review_head,
    token,
    adapter$http
  )
  assert_queue_namespace_empty(review_tree)
  adapter_fetch_commit(
    adapter$owner,
    adapter$repo,
    source_revision,
    token,
    adapter$http
  )
  source_tree <- adapter_fetch_tree_at(
    adapter$owner,
    adapter$repo,
    source_revision,
    token,
    adapter$http
  )
  paths <- source_paths %||% queue_source_paths(source_tree$blobs)
  if (!is.numeric(expected_record_count) ||
      length(expected_record_count) != 1L ||
      is.na(expected_record_count) ||
      as.integer(expected_record_count) < 1L ||
      expected_record_count != as.integer(expected_record_count)) {
    stop("expected_record_count must be a positive integer")
  }
  if (!.is_sha256(expected_path_set_sha256)) {
    stop("expected_path_set_sha256 must be a SHA-256")
  }
  if (length(paths) != as.integer(expected_record_count)) {
    stop(sprintf(
      "source record count mismatch: expected %d, found %d",
      as.integer(expected_record_count),
      length(paths)
    ))
  }
  if (!identical(queue_path_set_digest(paths), expected_path_set_sha256)) {
    stop("source path set does not match the independent expected digest")
  }
  source_blobs <- adapter_fetch_blobs_graphql(
    adapter,
    source_revision,
    paths,
    batch_size = 50L,
    progress = progress
  )
  generated <- generate_queue_enrollment(
    source_revision = source_revision,
    source_tree = source_tree,
    source_blobs = source_blobs,
    actor = actor,
    queue_id = queue_id,
    source_paths = paths
  )
  validate_generated_enrollment(generated)
  if (generated$payload_bytes > max_payload_bytes) {
    stop(sprintf(
      "queue initialization payload exceeds %d bytes",
      max_payload_bytes
    ))
  }
  report <- adapter_write_with_recovery(
    adapter,
    changes = generated$changes,
    expected_ref_sha = review_head,
    expected_blob_shas = list(),
    message = sprintf(
      "initialize review queue %s (%d records) by %s",
      queue_id,
      length(generated$records),
      actor
    ),
    inline_changes = generated$changes,
    max_payload_bytes = max_payload_bytes,
    preflight_tree = review_tree,
    reject_unrelated_head = TRUE
  )
  if (!report$ok) {
    stop(sprintf(
      "review queue was not initialized: %s",
      recovery_report_text(report)
    ))
  }
  list(
    ok = TRUE,
    commit_sha = report$commit_sha,
    descriptor = generated$descriptor,
    record_count = length(generated$records),
    payload_bytes = generated$payload_bytes
  )
}
