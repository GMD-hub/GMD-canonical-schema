#!/usr/bin/env Rscript

parse_args <- function(args) {
  allowed <- c("--repo", "--expected-source", "--expect-bootstrap-state")
  flags <- args[startsWith(args, "--")]
  if (any(!flags %in% allowed) || anyDuplicated(flags)) {
    stop("unsupported or duplicate argument")
  }
  value_after <- function(flag) {
    pos <- match(flag, args)
    if (is.na(pos) || pos == length(args) || startsWith(args[[pos + 1L]], "--")) {
      stop(sprintf("%s requires a value", flag))
    }
    args[[pos + 1L]]
  }
  consumed <- 2L * sum(c("--repo", "--expected-source") %in% args) +
    as.integer("--expect-bootstrap-state" %in% args)
  if (length(args) != consumed) stop("unexpected positional argument")
  list(
    repo = normalizePath(value_after("--repo"), mustWork = TRUE),
    expected_source = value_after("--expected-source"),
    bootstrap = "--expect-bootstrap-state" %in% args
  )
}

git_blob_raw <- function(repo, commit, path) {
  destination <- tempfile()
  errors <- tempfile()
  on.exit(unlink(c(destination, errors)), add = TRUE)
  status <- system2(
    "git", c("-C", repo, "show", paste0(commit, ":", path)),
    stdout = destination, stderr = errors
  )
  if (!identical(status, 0L)) {
    stop(sprintf("cannot read pinned source '%s'", path))
  }
  readBin(destination, "raw", n = file.info(destination)$size)
}

main <- function(args = commandArgs(trailingOnly = TRUE)) {
  opts <- parse_args(args)
  pkgload::load_all(file.path(opts$repo, "review-app"), quiet = TRUE)
  if (!reviewapp:::.is_sha1(opts$expected_source)) {
    stop("--expected-source must be a lowercase Git SHA-1")
  }
  queue_dir <- file.path(opts$repo, "extraction", "30_review")
  paths <- list.files(queue_dir, recursive = TRUE, all.files = TRUE, no.. = TRUE)
  allowed_control <- c(".gitkeep", "queue-manifest.yml", "queue-index.yml")
  record_paths <- sort(grep("^[^/]+[.]review[.]yml$", paths, value = TRUE))
  extras <- setdiff(paths, c(allowed_control, record_paths))
  if (length(extras)) stop("unexpected production queue paths: ", paste(extras, collapse = ", "))
  if (length(record_paths) != reviewapp:::QUEUE_EXPECTED_TOTAL) {
    stop(sprintf("expected 267 review records, found %d", length(record_paths)))
  }

  manifest <- reviewapp:::parse_queue_manifest(paste(
    readLines(file.path(queue_dir, "queue-manifest.yml"), warn = FALSE),
    collapse = "\n"
  ))
  if (!identical(manifest$source_commit, opts$expected_source)) {
    stop("queue manifest source commit does not match --expected-source")
  }
  if (!identical(manifest$expected_path_set_sha256,
                 reviewapp:::QUEUE_EXPECTED_PATH_SET_SHA256)) {
    stop("manifest path digest is not the canonical Release A digest")
  }

  items <- lapply(record_paths, function(path) {
    raw <- readBin(file.path(queue_dir, path), "raw", n = file.info(file.path(queue_dir, path))$size)
    record <- reviewapp:::parse_review_record(rawToChar(raw))
    reviewapp:::validate_review_record_v2(record)
    expected_name <- sprintf("%s.review.yml", record$artifact_id)
    if (!identical(path, expected_name)) stop("review record filename is not canonical")
    if (!identical(record$queue_id, manifest$queue_id) ||
        !identical(record$queue_id, reviewapp:::QUEUE_ID) ||
        !identical(record$source_commit, opts$expected_source)) {
      stop("review record queue or source identity is invalid")
    }
    source_raw <- git_blob_raw(opts$repo, opts$expected_source, record$source_artifact_path)
    source_text <- rawToChar(source_raw)
    source_blob <- reviewapp:::git_blob_sha_raw(source_raw)
    body <- reviewapp:::split_frontmatter(source_text)$body
    if (!identical(source_blob, record$source_artifact_blob_sha) ||
        !identical(reviewapp:::hash_body(source_text), record$source_content_sha256) ||
        !identical(reviewapp:::hash_body(body), record$enrolled_body_sha256) ||
        !identical(record$current_content_sha256, record$enrolled_body_sha256)) {
      stop(sprintf("record '%s' does not match pinned source bytes", record$artifact_id))
    }
    list(record = record, blob_sha = reviewapp:::git_blob_sha_raw(raw))
  })
  ids <- vapply(items, function(item) item$record$artifact_id, character(1))
  if (anyDuplicated(ids)) stop("production queue contains duplicate artifact IDs")
  source_paths <- sort(vapply(items, function(item) {
    item$record$source_artifact_path
  }, character(1)))
  computed_digest <- reviewapp:::queue_path_set_digest(source_paths)
  if (!identical(computed_digest, manifest$expected_path_set_sha256) ||
      !identical(computed_digest, reviewapp:::QUEUE_EXPECTED_PATH_SET_SHA256)) {
    stop("record source path digest is not the canonical Release A digest")
  }

  index <- reviewapp:::parse_queue_index_blob(paste(
    readLines(file.path(queue_dir, "queue-index.yml"), warn = FALSE), collapse = "\n"
  ), manifest)
  regenerated <- reviewapp:::queue_index_from_record_items(items, manifest)
  if (!identical(index$rows, regenerated)) {
    stop("queue index rows or record blob SHAs differ from exact regeneration")
  }

  if (opts$bootstrap) {
    if (!identical(manifest$approval_mode, "disabled")) stop("approval_mode must be disabled")
    blockers <- manifest$global_blockers
    if (!setequal(vapply(blockers, function(x) x$id, character(1)),
                  reviewapp:::QUEUE_GLOBAL_BLOCKER_IDS) ||
        any(vapply(blockers, function(x) !identical(x$status, "open"), logical(1)))) {
      stop("all four Release A global blockers must be open")
    }
    invalid <- vapply(items, function(item) {
      record <- item$record
      !identical(record$state, "draft") || length(record$assigned_to) != 0L ||
        length(record$events) != 0L
    }, logical(1))
    if (any(invalid)) stop("bootstrap records must be draft, unassigned, and event-free")
    approved <- list.files(
      file.path(opts$repo, "extraction", "40_approved"),
      recursive = TRUE, all.files = TRUE, no.. = TRUE
    )
    if (length(setdiff(approved, ".gitkeep"))) stop("approved output is not empty")
  }
  cat(sprintf("validated production queue: %d records; source %s\n", length(items), opts$expected_source))
  invisible(TRUE)
}

`%||%` <- function(a, b) if (is.null(a)) b else a

if (!identical(Sys.getenv("REVIEWAPP_TOOL_TESTING"), "1")) {
  tryCatch(main(), error = function(error) {
    message("production queue validation failed: ", conditionMessage(error))
    quit(status = 1L)
  })
}
