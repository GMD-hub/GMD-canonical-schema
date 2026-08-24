# Dashboard / work-queue index.

REVIEW_DIR <- "extraction/30_review"

empty_review_index <- function() {
  data.frame(
    artifact_id = character(0),
    state = character(0),
    review_round = integer(0),
    assigned_to = character(0),
    module = character(0),
    source_artifact_path = character(0),
    current_content_sha256 = character(0),
    source_commit = character(0),
    record_path = character(0),
    record_blob_sha = character(0),
    governance_blocked = logical(0),
    source_drift = logical(0),
    queue_id = character(0),
    record_schema_version = character(0),
    approval_eligible = logical(0),
    parse_error = character(0),
    stringsAsFactors = FALSE
  )
}

.index_module <- function(path) {
  sub("^extraction/20_drafts/([^/]+)/VAR-[a-z0-9]+\\.md$", "\\1", path)
}

.index_error_row <- function(
  id,
  message,
  record_path = NA_character_,
  record_blob_sha = NA_character_
) {
  data.frame(
    artifact_id = id,
    state = "ERROR",
    review_round = NA_integer_,
    assigned_to = NA_character_,
    module = NA_character_,
    source_artifact_path = NA_character_,
    current_content_sha256 = NA_character_,
    source_commit = NA_character_,
    record_path = record_path,
    record_blob_sha = record_blob_sha,
    governance_blocked = NA,
    source_drift = NA,
    queue_id = NA_character_,
    record_schema_version = NA_character_,
    approval_eligible = FALSE,
    parse_error = message,
    stringsAsFactors = FALSE
  )
}

review_record_index_row <- function(
  artifact_id,
  parsed,
  record_blob_sha = NA_character_,
  manifest = NULL,
  source_drift = FALSE,
  record_path = NULL
) {
  record_path <- record_path %||% sprintf(
    "extraction/30_review/%s.review.yml",
    artifact_id
  )
  blocked <- if (is.null(manifest)) {
    FALSE
  } else {
    length(queue_open_blockers(manifest, artifact_id)) > 0L
  }
  data.frame(
    artifact_id = artifact_id,
    state = parsed$state,
    review_round = as.integer(parsed$review_round),
    assigned_to = paste(parsed$assigned_to, collapse = ", "),
    module = .index_module(parsed$source_artifact_path),
    source_artifact_path = parsed$source_artifact_path,
    current_content_sha256 = parsed$current_content_sha256,
    source_commit = parsed$source_commit,
    record_path = record_path,
    record_blob_sha = record_blob_sha,
    governance_blocked = isTRUE(blocked),
    source_drift = isTRUE(source_drift),
    queue_id = parsed$queue_id %||% NA_character_,
    record_schema_version = parsed$record_schema_version %||% NA_character_,
    approval_eligible = FALSE,
    parse_error = NA_character_,
    stringsAsFactors = FALSE
  )
}

#' Build a dashboard data frame from review-record blobs.
index_review_records <- function(records, manifest = NULL) {
  rows <- lapply(records, function(record) {
    path <- record$record_path %||% NULL
    id <- record$id %||% sub(
      "\\.review\\.yml$",
      "",
      basename(path %||% "")
    )
    parsed <- tryCatch(
      parse_review_record(record$yaml_string),
      error = function(error) error
    )
    record_path <- path %||% sprintf(
      "extraction/30_review/%s.review.yml",
      id
    )
    record_sha <- record$blob_sha %||% NA_character_
    if (inherits(parsed, "condition")) {
      return(.index_error_row(id, conditionMessage(parsed), record_path, record_sha))
    }
    if (!identical(parsed$artifact_id, id)) {
      return(.index_error_row(
        id,
        "record filename ID does not match artifact_id",
        record_path,
        record_sha
      ))
    }
    if (!is.null(manifest) && is_v2_review_record(parsed) &&
        !identical(parsed$queue_id, manifest$queue_id)) {
      return(.index_error_row(
        id,
        "record queue_id does not match queue manifest",
        record_path,
        record_sha
      ))
    }
    review_record_index_row(
      id,
      parsed,
      record_blob_sha = record_sha,
      manifest = manifest,
      source_drift = record$source_drift %||% FALSE,
      record_path = record_path
    )
  })
  if (!length(rows)) return(empty_review_index())
  output <- do.call(rbind, rows)
  row.names(output) <- NULL
  output
}

queue_index_row_from_record <- function(
  record,
  record_blob_sha,
  manifest,
  source_drift = FALSE
) {
  validate_review_record_v2(record)
  blockers <- queue_open_blockers(manifest, record$artifact_id)
  new_queue_index_row(
    artifact_id = record$artifact_id,
    source_artifact_path = record$source_artifact_path,
    module = .index_module(record$source_artifact_path),
    state = record$state,
    review_round = record$review_round,
    assigned_to = record$assigned_to,
    record_path = sprintf(
      "extraction/30_review/%s.review.yml",
      record$artifact_id
    ),
    record_blob_sha = record_blob_sha,
    governance_blocked = length(blockers) > 0L,
    source_drift = source_drift
  )
}

queue_index_from_record_items <- function(records, manifest) {
  validate_queue_manifest(manifest)
  if (!is.list(records)) stop("records must be a list")
  rows <- lapply(records, function(item) {
    if (!is.list(item) || is.null(item$record) || is.null(item$blob_sha)) {
      stop("each record item requires record and blob_sha")
    }
    queue_index_row_from_record(item$record, item$blob_sha, manifest)
  })
  rows <- rows[order(vapply(rows, function(row) row$artifact_id, character(1)))]
  validate_queue_index(rows, manifest)
  rows
}

queue_index_from_records <- function(records, manifest) {
  validate_queue_manifest(manifest)
  rows <- lapply(records, function(record) {
    parsed <- if (!is.null(record$record)) record$record else record
    queue_index_row_from_record(
      parsed,
      record$blob_sha %||% record$record_blob_sha,
      manifest,
      record$source_drift %||% FALSE
    )
  })
  rows <- rows[order(vapply(rows, function(row) row$artifact_id, character(1)))]
  validate_queue_index(rows, manifest)
  rows
}

new_queue_index <- function(queue_id, rows, manifest = NULL) {
  .require_queue_scalar(queue_id, "queue_id")
  rows <- queue_index_rows_to_list(rows)
  if (!is.null(manifest)) validate_queue_index(rows, manifest)
  structure(
    list(
      schema_version = QUEUE_SCHEMA_VERSION,
      queue_id = queue_id,
      rows = rows
    ),
    class = c("reviewapp_queue_index", "list")
  )
}

queue_index_to_data_frame <- function(index, manifest = NULL) {
  rows <- if (is.list(index) && !is.null(index$rows)) {
    index$rows
  } else {
    index
  }
  rows <- queue_index_rows_to_list(rows)
  if (!length(rows)) return(empty_review_index())
  output <- do.call(rbind, lapply(rows, function(row) {
    data.frame(
      artifact_id = row$artifact_id,
      state = row$state,
      review_round = as.integer(row$review_round),
      assigned_to = paste(row$assigned_to, collapse = ", "),
      module = row$module,
      source_artifact_path = row$source_artifact_path,
      current_content_sha256 = NA_character_,
      source_commit = NA_character_,
      record_path = row$record_path,
      record_blob_sha = row$record_blob_sha,
      governance_blocked = row$governance_blocked,
      source_drift = row$source_drift,
      queue_id = manifest$queue_id %||% QUEUE_ID,
      record_schema_version = REVIEW_RECORD_SCHEMA_VERSION,
      approval_eligible = FALSE,
      parse_error = NA_character_,
      stringsAsFactors = FALSE
    )
  }))
  row.names(output) <- NULL
  output
}

serialize_queue_index <- function(index) {
  queue <- if (is.list(index) && !is.null(index$rows)) {
    index
  } else {
    new_queue_index(
      queue_id = attr(index, "queue_id") %||% QUEUE_ID,
      rows = index
    )
  }
  queue$rows <- queue_index_rows_to_list(queue$rows)
  queue$rows <- queue$rows[
    order(vapply(queue$rows, function(row) row$artifact_id, character(1)))
  ]
  queue$schema_version <- QUEUE_SCHEMA_VERSION
  canonical_yaml(queue)
}

rebuild_queue_index <- function(records, manifest) {
  serialize_queue_index(new_queue_index(
    manifest$queue_id,
    queue_index_from_records(records, manifest),
    manifest = manifest
  ))
}

parse_queue_index_blob <- function(yaml_string, manifest = NULL) {
  parse_queue_index(yaml_string, manifest = manifest)
}

adapter_index_review <- function(adapter) {
  token <- adapter$get_token()
  if (identical(adapter$review_branch, "review")) {
    tree <- adapter_fetch_tree(
      adapter$owner,
      adapter$repo,
      adapter$review_branch,
      token,
      adapter$http
    )
    paths <- grep(
      paste0("^", REVIEW_DIR, "/[^/]+\\.review\\.yml$"),
      names(tree$blobs),
      value = TRUE
    )
    records <- lapply(paths, function(path) {
      blob <- adapter_fetch_blob(
        adapter$owner,
        adapter$repo,
        path,
        adapter$review_branch,
        token,
        adapter$http
      )
      list(
        id = sub("\\.review\\.yml$", "", basename(path)),
        record_path = path,
        yaml_string = blob$content,
        blob_sha = blob$sha
      )
    })
    return(list(
      mode = "legacy_read_only",
      queue_mode = "legacy_read_only",
      index = index_review_records(records),
      blobs = tree$blobs,
      branch_head_sha = tree$commit,
      manifest = NULL,
      manifest_blob_sha = NULL,
      index_blob_sha = NULL,
      error = NULL
    ))
  }
  if (!identical(adapter$review_branch, "review/production")) {
    return(list(
      mode = "queue_error",
      queue_mode = "queue_error",
      index = empty_review_index(),
      blobs = list(),
      branch_head_sha = NULL,
      manifest = NULL,
      manifest_blob_sha = NULL,
      index_blob_sha = NULL,
      error = "unsupported production review branch; expected review/production"
    ))
  }
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
  manifest_sha <- tree$blobs[[QUEUE_MANIFEST_PATH]] %||% NULL
  if (is.null(manifest_sha)) {
    return(list(
      mode = "bootstrap_required",
      queue_mode = "bootstrap_required",
      index = empty_review_index(),
      blobs = tree$blobs,
      branch_head_sha = head,
      manifest = NULL,
      manifest_blob_sha = NULL,
      index_blob_sha = NULL,
      error = "production review branch has no queue manifest; administrator bootstrap is required"
    ))
  }
  manifest_blob <- adapter_fetch_blob_by_sha(
    adapter$owner,
    adapter$repo,
    manifest_sha,
    token,
    adapter$http
  )
  manifest <- parse_queue_manifest(manifest_blob$content)
  index_sha <- tree$blobs[[QUEUE_INDEX_PATH]] %||% NULL
  if (is.null(index_sha)) {
    return(list(
      mode = "queue_error",
      queue_mode = "queue_error",
      index = empty_review_index(),
      blobs = tree$blobs,
      branch_head_sha = head,
      manifest = manifest,
      manifest_blob_sha = manifest_sha,
      index_blob_sha = NULL,
      error = "production queue manifest exists but queue-index.yml is missing"
    ))
  }
  index_blob <- adapter_fetch_blob_by_sha(
    adapter$owner,
    adapter$repo,
    index_sha,
    token,
    adapter$http
  )
  queue_index <- parse_queue_index_blob(index_blob$content, manifest)
  list(
    mode = "production",
    queue_mode = "production",
    index = queue_index_to_data_frame(queue_index, manifest),
    blobs = tree$blobs,
    branch_head_sha = head,
    manifest = manifest,
    manifest_blob_sha = manifest_sha,
    index_blob_sha = index_sha,
    queue_index = queue_index,
    error = NULL
  )
}

filter_review_index <- function(index, artifact_id = NULL, module = NULL,
                                 state = NULL, assigned_to = NULL,
                                 next_step = NULL) {
  out <- index
  if (!is.null(artifact_id) && nzchar(artifact_id)) {
    out <- out[
      grepl(tolower(artifact_id), tolower(out$artifact_id), fixed = TRUE),
      ,
      drop = FALSE
    ]
  }
  if (!is.null(module) && nzchar(module)) {
    out <- out[grepl(module, out$module, fixed = TRUE), , drop = FALSE]
  }
  if (!is.null(state) && nzchar(state)) {
    out <- out[out$state == state, , drop = FALSE]
  }
  if (!is.null(assigned_to) && nzchar(assigned_to)) {
    assigned <- out$assigned_to
    assigned[is.na(assigned)] <- ""
    out <- out[
      grepl(tolower(assigned_to), tolower(assigned), fixed = TRUE),
      ,
      drop = FALSE
    ]
  }
  if (!is.null(next_step) && nzchar(next_step)) {
    steps <- vapply(out$state, action_required, character(1))
    out <- out[steps == next_step, , drop = FALSE]
  }
  row.names(out) <- NULL
  out
}

action_required <- function(state) {
  switch(state,
    "draft" = "Submit",
    "in-review" = "Review",
    "needs-revision" = "Revise",
    "approved" = "Approved",
    "ERROR" = "Repair",
    NA_character_
  )
}

selected_review_artifact <- function(displayed_index, selected_row) {
  if (is.null(selected_row) || length(selected_row) != 1L ||
      nrow(displayed_index) == 0L || selected_row < 1L ||
      selected_row > nrow(displayed_index)) {
    return(NULL)
  }
  displayed_index[selected_row, , drop = FALSE]
}

queue_table_options <- function() {
  list(
    pageLength = 25,
    lengthChange = FALSE,
    dom = "tip",
    responsive = list(details = list(type = "column", target = 0)),
    columnDefs = list(
      list(className = "control", orderable = FALSE, targets = 0),
      list(responsivePriority = 1, targets = 1),
      list(responsivePriority = 2, targets = 2),
      list(responsivePriority = 3, targets = 5)
    ),
    language = list(
      info = "Showing _START_ to _END_ of _TOTAL_ items",
      infoEmpty = "No items",
      paginate = list(previous = "Previous", `next` = "Next")
    )
  )
}

module_filter_choices <- function(index) {
  modules <- unique(index$module[!is.na(index$module)])
  modules <- modules[nzchar(modules)]
  stats::setNames(c("", modules), c("All", modules))
}
