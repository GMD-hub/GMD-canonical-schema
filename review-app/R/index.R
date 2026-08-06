# Dashboard / work-queue index (Step 9 / R4, R15).
#
# The dashboard derives its view by scanning the per-artifact review records
# under `extraction/30_review/` via the GitHub adapter (Decision 5 / R15). This
# is a derived view, NOT a source of truth -- there is no authoritative mutable
# manifest. The scan uses the GitHub Trees API (single recursive call) for that
# directory so the MVP is one request regardless of artifact count.
#
# The pure indexing function `index_review_records()` is separated from the
# adapter I/O so it can be unit-tested deterministically without network; the
# adapter-backed `adapter_index_review()` wires the two together.

REVIEW_DIR <- "extraction/30_review"

#' Parse one review-record blob into an index row.
#'
#' @param artifact_id character(1) ID (from filename).
#' @param parsed record as returned by `parse_review_record()`.
#' @return list with the index columns for that record.
review_record_index_row <- function(artifact_id, parsed) {
  list(
    artifact_id = artifact_id,
    state = parsed$state,
    review_round = parsed$review_round,
    assigned_to = paste(parsed$assigned_to, collapse = ", "),
    module = sub("^.*\\/([^/]+)\\/[^/]+\\.md$", "\\1", parsed$source_artifact_path %||% ""),
    source_artifact_path = parsed$source_artifact_path,
    current_content_sha256 = parsed$current_content_sha256,
    source_commit = parsed$source_commit
  )
}

#' Build a dashboard index from a list of `{id, yaml_string}` records.
#'
#' Malformed YAML is NOT silently skipped: it surfaces as an explicit error row
#' so the failure is loud rather than silently dropping an artifact from the
#' queue (per the plan's dashboard test scenario).
#'
#' @param records list of `{id, yaml_string}` pairs to index.
#' @return a data.frame of index rows (or rows carrying a `parse_error`).
index_review_records <- function(records) {
  rows <- lapply(records, function(r) {
    parsed <- tryCatch(parse_review_record(r$yaml_string), error = function(e) e)
    if (inherits(parsed, "condition")) {
      return(data.frame(
        artifact_id = r$id,
        state = "ERROR",
        review_round = NA_integer_,
        assigned_to = NA_character_,
        module = NA_character_,
        source_artifact_path = NA_character_,
        current_content_sha256 = NA_character_,
        source_commit = NA_character_,
        parse_error = conditionMessage(parsed),
        stringsAsFactors = FALSE
      ))
    }
    row <- review_record_index_row(r$id, parsed)
    row$parse_error <- NA_character_
    as.data.frame(row, stringsAsFactors = FALSE)
  })
  if (length(rows) == 0L) {
    empty <- data.frame(
      artifact_id = character(0), state = character(0),
      review_round = integer(0), assigned_to = character(0),
      module = character(0), source_artifact_path = character(0),
      current_content_sha256 = character(0), source_commit = character(0),
      parse_error = character(0), stringsAsFactors = FALSE
    )
    return(empty)
  }
  do.call(rbind, rows)
}

#' Filter an index by module, state, assignment, and action-required.
#'
#' @param index data.frame from `index_review_records()`.
#' @param module character(1) or NULL exact module substring filter.
#' @param state character(1) or NULL state to keep.
#' @param assigned_to character(1) or NULL identity substring filter.
#' @return filtered data.frame.
filter_review_index <- function(index, module = NULL, state = NULL, assigned_to = NULL) {
  out <- index
  if (!is.null(module) && nzchar(module)) {
    out <- out[grepl(module, out$module, fixed = TRUE), , drop = FALSE]
  }
  if (!is.null(state) && nzchar(state)) {
    out <- out[out$state == state, , drop = FALSE]
  }
  if (!is.null(assigned_to) && nzchar(assigned_to)) {
    out <- out[grepl(assigned_to, out$assigned_to, fixed = TRUE), , drop = FALSE]
  }
  row.names(out) <- NULL
  out
}

#' Scan the review directory on a branch and build the index (adapter-backed).
#'
#' Uses a single recursive Trees API call for `extraction/30_review/`. Each
#' `.review.yml` blob is read (content + blob SHA) and indexed.
#'
#' @param adapter a github adapter (new_github_adapter / test double).
#' @return list(index = data.frame, blobs = name->sha map) where `index` is the
#'   dashboard index.
adapter_index_review <- function(adapter) {
  token <- adapter$get_token()
  tree <- adapter_fetch_tree(adapter$owner, adapter$repo, adapter$review_branch,
                             token, adapter$http)
  paths <- grep(paste0("^", REVIEW_DIR, "/[^/]+\\.review\\.yml$"),
                names(tree$blobs), value = TRUE)
  records <- lapply(paths, function(path) {
    id <- sub("\\.review\\.yml$", "", basename(path))
    blob <- adapter_fetch_blob(adapter$owner, adapter$repo, path,
                               adapter$review_branch, token, adapter$http)
    list(id = id, yaml_string = blob$content)
  })
  list(index = index_review_records(records), blobs = tree$blobs)
}

#' Map an artifact's state to the action the cur next actor must take.
#'
#' @param state character(1) review state.
#' @return character(1) short label for the "action required" column.
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
