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
    source_drift_status = character(0),
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
    source_drift_status = NA_character_,
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
  source_drift_status = "unchecked",
  record_path = NULL
) {
  record_path <- record_path %||% sprintf(
    "extraction/30_review/%s.review.yml",
    artifact_id
  )
  blocked <- is_v2_review_record(parsed) && length(parsed$blocker_refs) > 0L
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
    governance_blocked = blocked,
    source_drift = identical(source_drift_status, "drifted"),
    source_drift_status = source_drift_status,
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
      source_drift_status = record$source_drift_status %||% "unchecked",
      record_path = record_path
    )
  })
  if (!length(rows)) return(empty_review_index())
  output <- do.call(rbind, rows)
  row.names(output) <- NULL
  output
}

.review_record_paths <- function(tree_blobs) {
  sort(grep(
    paste0("^", REVIEW_DIR, "/VAR-[a-z0-9]+[.]review[.]yml$"),
    names(tree_blobs),
    value = TRUE
  ))
}

.queue_control_path <- function(tree_blobs) {
  present <- intersect(
    c(QUEUE_DESCRIPTOR_PATH, LEGACY_QUEUE_MANIFEST_PATH),
    names(tree_blobs)
  )
  if (!length(present)) {
    stop(.queue_error(
      "queue descriptor is missing; initialize the queue outside the application"
    ))
  }
  if (length(present) != 1L) {
    stop(.queue_error("queue contains both simplified and legacy controls"))
  }
  if (identical(present[[1L]], QUEUE_DESCRIPTOR_PATH) &&
      LEGACY_QUEUE_INDEX_PATH %in% names(tree_blobs)) {
    stop(.queue_error(
      "simplified queue contains the obsolete production-v2 index"
    ))
  }
  present[[1L]]
}

.legacy_review_index <- function(adapter, token) {
  tree <- adapter_fetch_tree(
    adapter$owner,
    adapter$repo,
    adapter$review_branch,
    token,
    adapter$http
  )
  paths <- .review_record_paths(tree$blobs)
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
      id = sub("[.]review[.]yml$", "", basename(path)),
      record_path = path,
      yaml_string = blob$content,
      blob_sha = blob$sha
    )
  })
  list(
    mode = "legacy_read_only",
    queue_mode = "legacy_read_only",
    index = index_review_records(records),
    blobs = tree$blobs,
    branch_head_sha = tree$commit,
    descriptor = NULL,
    descriptor_path = NULL,
    descriptor_blob_sha = NULL,
    error = NULL
  )
}

.versioned_review_index <- function(adapter, token) {
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
  descriptor_path <- .queue_control_path(tree$blobs)
  descriptor_sha <- tree$blobs[[descriptor_path]]
  descriptor_blob <- adapter_fetch_blob_by_sha(
    adapter$owner,
    adapter$repo,
    descriptor_sha,
    token,
    adapter$http
  )
  descriptor <- parse_queue_control(descriptor_blob$content, descriptor_path)
  paths <- .review_record_paths(tree$blobs)
  blobs <- adapter_fetch_review_records_graphql(adapter, head, paths)
  items <- lapply(paths, function(path) {
    blob <- blobs[[path]] %||% NULL
    expected_sha <- tree$blobs[[path]]
    if (is.null(blob) || !identical(blob$sha, expected_sha) ||
        !identical(git_blob_sha(blob$content), expected_sha)) {
      stop(.queue_error(sprintf(
        "review record '%s' does not match the queue tree",
        path
      )))
    }
    id <- sub("[.]review[.]yml$", "", basename(path))
    record <- parse_review_record(blob$content)
    if (!is_v2_review_record(record)) {
      stop(.queue_error(sprintf("versioned queue record '%s' is not v2", id)))
    }
    if (!identical(record$artifact_id, id)) {
      stop(.queue_error(sprintf(
        "review record filename '%s' does not match artifact_id",
        path
      )))
    }
    list(
      id = id,
      record_path = path,
      yaml_string = blob$content,
      blob_sha = blob$sha,
      record = record,
      source_drift_status = "unchecked"
    )
  })
  records <- lapply(items, function(item) item$record)
  validate_queue_record_set(records, descriptor)
  validate_record_source_snapshots(adapter, records)
  mode <- switch(queue_descriptor_format(descriptor),
    production_v2 = "production_v2_read_only",
    descriptor_1_0 = "descriptor_v1_0_read_only",
    descriptor_1_1 = "versioned"
  )
  list(
    mode = mode,
    queue_mode = mode,
    index = index_review_records(items, descriptor),
    blobs = tree$blobs,
    branch_head_sha = head,
    descriptor = descriptor,
    descriptor_path = descriptor_path,
    descriptor_blob_sha = descriptor_sha,
    error = NULL
  )
}

.adapter_index_review <- function(adapter) {
  token <- adapter$get_token()
  if (isTRUE(adapter$read_only) || identical(adapter$review_branch, "review")) {
    return(.legacy_review_index(adapter, token))
  }
  .versioned_review_index(adapter, token)
}

adapter_index_review <- function(adapter) {
  telemetry <- repository_telemetry_operation(adapter)
  result <- tryCatch(
    .adapter_index_review(telemetry$adapter),
    error = function(error) {
      list(
        mode = "queue_error",
        queue_mode = "queue_error",
        index = empty_review_index(),
        blobs = list(),
        branch_head_sha = NULL,
        descriptor = NULL,
        descriptor_path = NULL,
        descriptor_blob_sha = NULL,
        error = sprintf("review queue is invalid: %s", conditionMessage(error))
      )
    }
  )
  result$request_telemetry <- telemetry$snapshot()
  result
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
