# Forward-only queue-control migration.

.migration_blob <- function(adapter, tree, path) {
  sha <- tree$blobs[[path]] %||% NULL
  if (!.is_sha1(sha)) stop(sprintf("migration control '%s' is missing", path))
  blob <- adapter_fetch_blob_by_sha(
    adapter$owner,
    adapter$repo,
    sha,
    adapter$get_token(),
    adapter$http
  )
  if (!identical(blob$sha, sha) ||
      !identical(git_blob_sha_raw(blob$raw), sha)) {
    stop(sprintf("migration control '%s' does not match the Git tree", path))
  }
  blob
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
  validate_record_source_snapshots(adapter, records)
}

validate_legacy_index_for_migration <- function(yaml_string, items, descriptor) {
  index <- yaml::read_yaml(text = yaml_string)
  if (!is.list(index) ||
      !identical(as.character(index$schema_version %||% ""), "1.0") ||
      !is.list(index$rows) ||
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

.migration_input <- function(adapter, tree) {
  descriptor_sha <- tree$blobs[[QUEUE_DESCRIPTOR_PATH]] %||% NULL
  manifest_sha <- tree$blobs[[LEGACY_QUEUE_MANIFEST_PATH]] %||% NULL
  index_sha <- tree$blobs[[LEGACY_QUEUE_INDEX_PATH]] %||% NULL
  if (!is.null(descriptor_sha)) {
    if (!is.null(manifest_sha) || !is.null(index_sha)) {
      stop("queue contains mixed simplified and production-v2 controls")
    }
    blob <- .migration_blob(adapter, tree, QUEUE_DESCRIPTOR_PATH)
    descriptor <- parse_queue_descriptor(blob$content)
    if (!queue_descriptor_is_legacy(descriptor)) {
      stop("queue already uses descriptor schema version 1.1")
    }
    return(list(
      kind = "descriptor_1_0",
      descriptor = descriptor,
      changes = stats::setNames(list(NULL), QUEUE_DESCRIPTOR_PATH),
      expected = stats::setNames(list(descriptor_sha), QUEUE_DESCRIPTOR_PATH)
    ))
  }
  if (is.null(manifest_sha) || is.null(index_sha)) {
    stop("migration requires a complete production-v2 manifest and index")
  }
  manifest <- .migration_blob(adapter, tree, LEGACY_QUEUE_MANIFEST_PATH)
  descriptor <- parse_legacy_queue_manifest(
    manifest$content,
    require_approval_disabled = TRUE
  )
  changes <- list()
  changes[LEGACY_QUEUE_MANIFEST_PATH] <- list(NULL)
  changes[LEGACY_QUEUE_INDEX_PATH] <- list(NULL)
  expected <- list()
  expected[QUEUE_DESCRIPTOR_PATH] <- list(NA_character_)
  expected[LEGACY_QUEUE_MANIFEST_PATH] <- list(manifest_sha)
  expected[LEGACY_QUEUE_INDEX_PATH] <- list(index_sha)
  list(
    kind = "production_v2",
    descriptor = descriptor,
    index = .migration_blob(adapter, tree, LEGACY_QUEUE_INDEX_PATH),
    changes = changes,
    expected = expected
  )
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
  input <- .migration_input(adapter, tree)
  items <- .migration_record_items(adapter, head, tree)
  records <- lapply(items, function(item) item$record)
  validate_queue_record_set(records, input$descriptor)
  validate_migration_source_records(adapter, input$descriptor, records)
  if (identical(input$kind, "production_v2")) {
    validate_legacy_index_for_migration(
      input$index$content,
      items,
      input$descriptor
    )
  }
  descriptor <- new_queue_descriptor(
    queue_id = input$descriptor$queue_id,
    source_revision = input$descriptor$source_revision,
    created_at = input$descriptor$created_at,
    created_by = input$descriptor$created_by,
    expected_record_count = length(records),
    record_set_sha256 = queue_record_set_digest(records),
    approvals_enabled = FALSE
  )
  changes <- input$changes
  changes[QUEUE_DESCRIPTOR_PATH] <- list(canonical_yaml(descriptor))
  report <- adapter_write_with_recovery(
    adapter,
    changes = changes,
    expected_ref_sha = head,
    expected_blob_shas = input$expected,
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
    source_format = input$kind,
    descriptor = descriptor,
    record_count = length(records),
    preserved_record_blobs = stats::setNames(
      vapply(items, function(item) item$blob_sha, character(1)),
      vapply(items, function(item) item$path, character(1))
    )
  )
}
