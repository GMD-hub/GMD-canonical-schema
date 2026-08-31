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

.migration_record_items <- function(adapter, head, tree) {
  paths <- .review_record_paths(tree$blobs)
  blobs <- adapter_fetch_review_records_graphql(adapter, head, paths)
  lapply(paths, function(path) {
    blob <- blobs[[path]] %||% NULL
    if (is.null(blob) || !identical(blob$sha, tree$blobs[[path]]) ||
        !identical(git_blob_sha(blob$content), blob$sha)) {
      stop(sprintf("migration record '%s' does not match the Git tree", path))
    }
    record <- parse_review_record(blob$content)
    validate_review_record_v2(record)
    if (!identical(ACTION_PATH(record$artifact_id), path)) {
      stop(sprintf("migration record path does not match '%s'", record$artifact_id))
    }
    list(path = path, blob_sha = blob$sha, record = record)
  })
}

validate_migration_source_records <- function(adapter, descriptor, records) {
  validate_queue_descriptor(descriptor)
  paths <- vapply(
    records,
    function(record) record$source_artifact_path,
    character(1)
  )
  token <- adapter$get_token()
  adapter_fetch_commit(
    adapter$owner,
    adapter$repo,
    descriptor$source_revision,
    token,
    adapter$http
  )
  source_tree <- adapter_fetch_tree_at(
    adapter$owner,
    adapter$repo,
    descriptor$source_revision,
    token,
    adapter$http
  )
  source_blobs <- adapter_fetch_blobs_graphql(
    adapter,
    descriptor$source_revision,
    paths
  )
  for (record in records) {
    path <- record$source_artifact_path
    source <- source_blobs[[path]] %||% NULL
    if (is.null(source) ||
        !identical(source_tree$blobs[[path]], record$source_artifact_blob_sha) ||
        !identical(source$sha, record$source_artifact_blob_sha)) {
      stop(sprintf(
        "record '%s' source Git identity is not present at the source revision",
        record$artifact_id
      ))
    }
    source_raw <- source$raw %||% charToRaw(enc2utf8(source$content))
    split <- split_frontmatter_exact(source$content)
    body_raw <- split$body_raw %||%
      charToRaw(enc2utf8(split$body %||% ""))
    if (!identical(git_blob_sha_raw(source_raw), record$source_artifact_blob_sha) ||
        !identical(hash_raw(source_raw), record$source_content_sha256) ||
        !identical(hash_raw(body_raw), record$enrolled_body_sha256)) {
      stop(sprintf(
        "record '%s' source bytes do not match enrollment",
        record$artifact_id
      ))
    }
  }
  invisible(TRUE)
}

validate_legacy_index_for_migration <- function(
  yaml_string,
  items,
  descriptor
) {
  index <- yaml::read_yaml(text = yaml_string)
  if (!is.list(index) || !is.list(index$rows) ||
      !identical(index$queue_id, descriptor$queue_id)) {
    stop("legacy queue index is malformed or has the wrong queue ID")
  }
  if (length(index$rows) != length(items)) {
    stop("legacy queue index record count does not match review records")
  }
  rows_by_id <- stats::setNames(
    index$rows,
    vapply(index$rows, function(row) row$artifact_id %||% "", character(1))
  )
  if (any(!nzchar(names(rows_by_id))) || anyDuplicated(names(rows_by_id))) {
    stop("legacy queue index contains missing or duplicate artifact IDs")
  }
  for (item in items) {
    record <- item$record
    row <- rows_by_id[[record$artifact_id]] %||% NULL
    if (is.null(row) ||
        !identical(row$record_path, item$path) ||
        !identical(row$record_blob_sha, item$blob_sha) ||
        !identical(row$source_artifact_path, record$source_artifact_path)) {
      stop(sprintf(
        "legacy queue index does not match record '%s'",
        record$artifact_id
      ))
    }
  }
  invisible(TRUE)
}

migrate_review_queue <- function(adapter, actor) {
  .assert_writable_adapter(adapter)
  if (!queue_administration_authorized(actor, "migrate")) {
    stop("only an authenticated administrator may migrate a review queue")
  }
  if (!.is_scalar_character(actor)) {
    stop("queue migration requires an authenticated actor")
  }
  token <- adapter$get_token()
  head <- adapter_branch_head(
    adapter$owner,
    adapter$repo,
    adapter$review_branch,
    token,
    adapter$http
  )
  tree <- adapter_fetch_tree_at(
    adapter$owner,
    adapter$repo,
    head,
    token,
    adapter$http
  )
  if (!is.null(tree$blobs[[QUEUE_DESCRIPTOR_PATH]])) {
    stop("queue already uses the simplified descriptor")
  }
  manifest_sha <- tree$blobs[[LEGACY_QUEUE_MANIFEST_PATH]] %||% NULL
  index_sha <- tree$blobs[[LEGACY_QUEUE_INDEX_PATH]] %||% NULL
  if (is.null(manifest_sha) || is.null(index_sha)) {
    stop("migration requires a complete production-v2 manifest and index")
  }
  manifest_blob <- adapter_fetch_blob_by_sha(
    adapter$owner,
    adapter$repo,
    manifest_sha,
    token,
    adapter$http
  )
  legacy_descriptor <- parse_legacy_queue_manifest(manifest_blob$content)
  items <- .migration_record_items(adapter, head, tree)
  records <- lapply(items, function(item) item$record)
  validate_queue_record_set(records, legacy_descriptor)
  validate_migration_source_records(adapter, legacy_descriptor, records)
  index_blob <- adapter_fetch_blob_by_sha(
    adapter$owner,
    adapter$repo,
    index_sha,
    token,
    adapter$http
  )
  validate_legacy_index_for_migration(
    index_blob$content,
    items,
    legacy_descriptor
  )
  descriptor <- new_queue_descriptor(
    queue_id = legacy_descriptor$queue_id,
    source_revision = legacy_descriptor$source_revision,
    created_at = legacy_descriptor$created_at,
    created_by = legacy_descriptor$created_by,
    expected_record_count = length(records),
    record_set_sha256 = queue_record_set_digest(records)
  )
  changes <- list()
  changes[QUEUE_DESCRIPTOR_PATH] <- list(canonical_yaml(descriptor))
  changes[LEGACY_QUEUE_MANIFEST_PATH] <- list(NULL)
  changes[LEGACY_QUEUE_INDEX_PATH] <- list(NULL)
  expected <- list()
  expected[QUEUE_DESCRIPTOR_PATH] <- list(NA_character_)
  expected[LEGACY_QUEUE_MANIFEST_PATH] <- list(manifest_sha)
  expected[LEGACY_QUEUE_INDEX_PATH] <- list(index_sha)
  report <- adapter_write_with_recovery(
    adapter,
    changes = changes,
    expected_ref_sha = head,
    expected_blob_shas = expected,
    message = sprintf("migrate review queue %s by %s", descriptor$queue_id, actor),
    preflight_tree = tree,
    reject_unrelated_head = TRUE
  )
  if (!report$ok) {
    stop(sprintf("review queue was not migrated: %s", recovery_report_text(report)))
  }
  list(
    ok = TRUE,
    commit_sha = report$commit_sha,
    descriptor = descriptor,
    record_count = length(records),
    preserved_record_blobs = stats::setNames(
      vapply(items, function(item) item$blob_sha, character(1)),
      vapply(items, function(item) item$path, character(1))
    )
  )
}
