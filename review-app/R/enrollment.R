# Administrator-controlled production queue enrollment.

bootstrap_authorized <- function(role) identical(role, "administrator")

production_branch_name <- function(adapter) {
  identical(adapter$review_branch, PRODUCTION_REVIEW_BRANCH)
}

release_a_draft_paths <- function(tree_blobs) {
  if (!is.list(tree_blobs) || is.null(names(tree_blobs))) {
    stop("source tree blobs must be a named list")
  }
  paths <- names(tree_blobs)
  module_paths <- paths[grepl(
    "^extraction/20_drafts/(idn|geo|dem|lbr|utl|dwl)/",
    paths
  )]
  all_var_paths <- paths[grepl(
    "^extraction/20_drafts/[^/]+/VAR-[a-z0-9]+[.]md$",
    paths
  )]
  draft_paths <- module_paths[grepl(
    "^extraction/20_drafts/(idn|geo|dem|lbr|utl|dwl)/VAR-[a-z0-9]+[.]md$",
    module_paths
  )]
  if (length(module_paths) != length(draft_paths)) {
    extras <- setdiff(module_paths, draft_paths)
    stop(sprintf(
      "source tree contains malformed or extra draft paths: %s",
      paste(extras, collapse = ", ")
    ))
  }
  if (!setequal(all_var_paths, draft_paths)) {
    extras <- setdiff(all_var_paths, draft_paths)
    stop(sprintf(
      "source tree contains VAR draft paths outside the reviewed modules: %s",
      paste(extras, collapse = ", ")
    ))
  }
  draft_paths <- sort(draft_paths)
  if (length(draft_paths) != QUEUE_EXPECTED_TOTAL) {
    stop(sprintf(
      "source draft count mismatch: expected %d, found %d",
      QUEUE_EXPECTED_TOTAL,
      length(draft_paths)
    ))
  }
  modules <- sub("^extraction/20_drafts/([^/]+)/.*$", "\\1", draft_paths)
  counts <- table(factor(modules, levels = names(QUEUE_EXPECTED_MODULE_COUNTS)))
  if (!identical(as.integer(counts), as.integer(QUEUE_EXPECTED_MODULE_COUNTS))) {
    stop("source draft module counts do not match the Release A set")
  }
  if (!identical(queue_path_set_digest(draft_paths), QUEUE_EXPECTED_PATH_SET_SHA256)) {
    stop("source draft path set does not match the reviewed Release A set")
  }
  ids <- sub("^.*[?/]", "", sub("[.]md$", "", draft_paths))
  if (anyDuplicated(ids)) stop("source draft set contains duplicate artifact IDs")
  draft_paths
}

enrollment_timestamp <- function(now = Sys.time()) {
  format(now, tz = "UTC", usetz = FALSE, format = "%Y-%m-%dT%H:%M:%SZ")
}

generate_production_enrollment <- function(
  source_commit,
  source_tree,
  source_blobs,
  actor,
  queue_id = QUEUE_ID,
  created_at = enrollment_timestamp(),
  progress = NULL
) {
  if (!.is_sha1(source_commit)) stop("enrollment requires a Git commit SHA-1")
  if (!.is_scalar_character(actor)) stop("enrollment requires an administrator identity")
  if (!is.list(source_blobs) || is.null(names(source_blobs))) {
    stop("source blobs must be a named list")
  }
  paths <- release_a_draft_paths(source_tree$blobs)
  missing <- setdiff(paths, names(source_blobs))
  if (length(missing)) {
    stop(sprintf("source blob batch omitted paths: %s", paste(missing, collapse = ", ")))
  }
  records <- list()
  for (i in seq_along(paths)) {
    path <- paths[[i]]
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
    body_sha <- hash_raw(split$body_raw %||% charToRaw(enc2utf8(split$body %||% "")))
    full_sha <- hash_raw(source_raw)
    artifact_id <- sub("^.*[/]([^/]+)[.]md$", "\\1", path)
    record <- new_review_record_v2(
      artifact_id = artifact_id,
      queue_id = queue_id,
      source_artifact_path = path,
      source_commit = source_commit,
      source_artifact_blob_sha = source$sha,
      source_content_sha256 = full_sha,
      enrolled_body_sha256 = body_sha,
      current_content_sha256 = body_sha,
      enrolled_at = created_at,
      enrolled_by = actor
    )
    yaml_text <- record_to_yaml(record)
    record_path <- ACTION_PATH(artifact_id)
    records[[record_path]] <- list(
      artifact_id = artifact_id,
      record = record,
      content = yaml_text,
      blob_sha = git_blob_sha(yaml_text)
    )
    if (!is.null(progress)) progress(i, length(paths))
  }
  record_list <- unname(records)
  manifest <- new_queue_manifest(
    queue_id = queue_id,
    created_at = created_at,
    created_by = actor,
    source_commit = source_commit
  )
  index_rows <- queue_index_from_record_items(record_list, manifest)
  index <- new_queue_index(queue_id, index_rows, manifest = manifest)
  index_yaml <- serialize_queue_index(index)
  manifest_yaml <- canonical_yaml(manifest)
  changes <- list()
  for (path in names(records)) changes[[path]] <- records[[path]]$content
  changes[[QUEUE_INDEX_PATH]] <- index_yaml
  changes[[QUEUE_MANIFEST_PATH]] <- manifest_yaml
  validate_generated_enrollment(
    records = records,
    manifest = manifest,
    index = index,
    source_paths = paths
  )
  list(
    records = records,
    manifest = manifest,
    manifest_yaml = manifest_yaml,
    index = index,
    index_yaml = index_yaml,
    changes = changes,
    payload_bytes = nchar(
      jsonlite::toJSON(
        lapply(names(changes), function(path) {
          list(path = path, mode = "100644", type = "blob", content = changes[[path]])
        }),
        auto_unbox = TRUE
      ),
      type = "bytes"
    )
  )
}

validate_generated_enrollment <- function(records, manifest, index, source_paths) {
  validate_queue_manifest(manifest)
  if (length(records) != QUEUE_EXPECTED_TOTAL) {
    stop("generated record count does not match the Release A set")
  }
  validate_queue_index(index$rows, manifest)
  record_paths <- sort(vapply(unname(records), function(item) {
    item$record$source_artifact_path
  }, character(1)))
  if (!identical(record_paths, sort(source_paths))) {
    stop("generated record source paths do not match the source draft set")
  }
  invisible(TRUE)
}

bootstrap_production_queue <- function(
  adapter,
  actor,
  role = NULL,
  expected_source_commit,
  queue_id = QUEUE_ID,
  progress = NULL,
  max_payload_bytes = QUEUE_BOOTSTRAP_MAX_PAYLOAD_BYTES
) {
  if (!production_branch_name(adapter)) {
    stop(sprintf(
      "production bootstrap is only allowed on %s",
      PRODUCTION_REVIEW_BRANCH
    ))
  }
  if (!bootstrap_authorized(role)) {
    stop("only an authenticated administrator may bootstrap the production queue")
  }
  if (!.is_scalar_character(actor)) stop("bootstrap requires an authenticated actor")
  if (!.is_sha1(expected_source_commit)) {
    stop("bootstrap expected source commit must be a lowercase Git SHA-1")
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
  if (!is.null(review_tree$blobs[[QUEUE_MANIFEST_PATH]])) {
    stop("production queue bootstrap has already been completed")
  }
  if (!is.null(review_tree$blobs[[QUEUE_INDEX_PATH]])) {
    stop("production queue has an index but no manifest; refusing implicit repair")
  }
  source_head <- adapter_branch_head(
    adapter$owner,
    adapter$repo,
    adapter$default_branch,
    token,
    adapter$http
  )
  if (!identical(source_head, expected_source_commit)) {
    stop("default source branch does not match the configured expected source commit")
  }
  source_tree <- adapter_fetch_tree_at(
    adapter$owner,
    adapter$repo,
    source_head,
    token,
    adapter$http
  )
  paths <- release_a_draft_paths(source_tree$blobs)
  source_blobs <- adapter_fetch_blobs_graphql(
    adapter,
    source_head,
    paths,
    batch_size = 50L,
    progress = progress
  )
  generated <- generate_production_enrollment(
    source_commit = source_head,
    source_tree = source_tree,
    source_blobs = source_blobs,
    actor = actor,
    queue_id = queue_id,
    progress = NULL
  )
  if (generated$payload_bytes > max_payload_bytes) {
    stop(sprintf(
      "bootstrap payload exceeds configured limit of %d bytes",
      max_payload_bytes
    ))
  }
  if (generated$payload_bytes > QUEUE_BOOTSTRAP_MAX_PAYLOAD_BYTES) {
    stop("bootstrap payload exceeds the documented maximum payload budget")
  }
  source_head_after <- adapter_branch_head(
    adapter$owner,
    adapter$repo,
    adapter$default_branch,
    token,
    adapter$http
  )
  if (!identical(source_head_after, expected_source_commit)) {
    stop("default source branch moved or no longer matches the expected source commit")
  }
  result <- adapter_write_with_recovery(
    adapter,
    changes = generated$changes,
    expected_ref_sha = review_head,
    expected_blob_shas = list(),
    message = sprintf(
      "bootstrap production review queue (%d artifacts) by %s",
      QUEUE_EXPECTED_TOTAL,
      actor
    ),
    inline_changes = generated$changes,
    max_payload_bytes = max_payload_bytes,
    preflight_tree = review_tree,
    reject_unrelated_head = TRUE
  )
  if (!result$ok) {
    stop(sprintf("production bootstrap was not published: %s", recovery_report_text(result)))
  }
  list(
    ok = TRUE,
    commit_sha = result$commit_sha,
    manifest = generated$manifest,
    index = generated$index,
    record_count = length(generated$records),
    payload_bytes = generated$payload_bytes
  )
}
