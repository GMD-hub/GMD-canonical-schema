#!/usr/bin/env Rscript

parse_args <- function(args) {
  bootstrap <- "--expect-bootstrap-state" %in% args
  args <- args[args != "--expect-bootstrap-state"]
  required <- c(
    "--repo", "--expected-source", "--expected-count",
    "--expected-path-digest"
  )
  if (length(args) != 2L * length(required)) {
    stop(paste(
      "usage: validate-production-queue.R --repo <repository>",
      "--expected-source <sha1> --expected-count <n>",
      "--expected-path-digest <sha256>"
    ))
  }
  flags <- args[seq(1L, length(args), by = 2L)]
  if (anyDuplicated(flags) || !setequal(flags, required)) {
    stop("validator arguments are missing, duplicated, or unsupported")
  }
  values <- stats::setNames(args[seq(2L, length(args), by = 2L)], flags)
  count <- suppressWarnings(as.integer(values[["--expected-count"]]))
  if (is.na(count) || count < 1L) stop("--expected-count must be positive")
  list(
    repo = normalizePath(values[["--repo"]], mustWork = TRUE),
    expected_source = values[["--expected-source"]],
    expected_count = count,
    expected_path_digest = values[["--expected-path-digest"]],
    bootstrap = bootstrap
  )
}

tool_app_dir <- function(command_args = commandArgs(trailingOnly = FALSE)) {
  file_args <- grep("^--file=", command_args, value = TRUE)
  if (length(file_args) != 1L) {
    stop("cannot resolve validator script path")
  }
  script_path <- normalizePath(
    sub("^--file=", "", file_args[[1L]]),
    mustWork = TRUE
  )
  app_dir <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
  if (!file.exists(file.path(app_dir, "DESCRIPTION"))) {
    stop("validator script is not inside the review-app package")
  }
  app_dir
}

git_blob_raw <- function(repo, commit, path) {
  destination <- tempfile()
  errors <- tempfile()
  on.exit(unlink(c(destination, errors)), add = TRUE)
  status <- system2(
    "git", c("-C", repo, "show", paste0(commit, ":", path)),
    stdout = destination, stderr = errors,
    env = "GIT_NO_REPLACE_OBJECTS=1"
  )
  if (!identical(status, 0L)) {
    stop(sprintf("cannot read enrolled source '%s'", path))
  }
  readBin(destination, "raw", n = file.info(destination)$size)
}

git_commit_sha <- function(repo, revision) {
  errors <- tempfile()
  on.exit(unlink(errors), add = TRUE)
  output <- system2(
    "git",
    c("-C", repo, "rev-parse", "--verify", paste0(revision, "^{commit}")),
    stdout = TRUE,
    stderr = errors,
    env = "GIT_NO_REPLACE_OBJECTS=1"
  )
  if (!is.null(attr(output, "status")) || length(output) != 1L ||
      !identical(output[[1L]], revision)) {
    stop("--expected-source must identify an exact commit object")
  }
  output[[1L]]
}

git_tree_paths <- function(repo, commit, prefix) {
  output <- system2(
    "git",
    c("-C", repo, "ls-tree", "-r", "--name-only", commit, "--", prefix),
    stdout = TRUE,
    stderr = TRUE,
    env = "GIT_NO_REPLACE_OBJECTS=1"
  )
  if (!is.null(attr(output, "status"))) {
    stop(sprintf("cannot inspect governed tree '%s'", prefix))
  }
  output
}

git_regular_blob_raw <- function(repo, commit, path) {
  entry <- system2(
    "git",
    c("-C", repo, "ls-tree", commit, "--", path),
    stdout = TRUE,
    stderr = TRUE,
    env = "GIT_NO_REPLACE_OBJECTS=1"
  )
  if (!is.null(attr(entry, "status")) || length(entry) != 1L ||
      !grepl("^100644 blob [0-9a-f]{40}\\t", entry)) {
    stop(sprintf("governed path '%s' is not one regular Git blob", path))
  }
  git_blob_raw(repo, commit, path)
}

record_matches_source_bytes <- function(record, source_raw) {
  if (!is.raw(source_raw)) stop("source content must be raw bytes")
  source_text <- rawToChar(source_raw)
  split <- reviewapp:::split_frontmatter_exact(source_text)
  reviewapp:::.source_frontmatter(split, record$artifact_id)
  body_raw <- split$body_raw %||% charToRaw(enc2utf8(split$body %||% ""))
  identical(
    reviewapp:::git_blob_sha_raw(source_raw),
    record$source_artifact_blob_sha
  ) && identical(
    reviewapp:::hash_raw(source_raw),
    record$source_content_sha256
  ) && identical(
    reviewapp:::hash_raw(body_raw),
    record$enrolled_body_sha256
  )
}

read_raw_file <- function(path) {
  readBin(path, "raw", n = file.info(path)$size)
}

validate_bootstrap_state <- function(
  records,
  descriptor,
  body_paths,
  approved_paths
) {
  invalid <- vapply(records, function(record) {
    !identical(record$state, "draft") ||
      !identical(record$review_round, 1L) ||
      length(record$assigned_to) > 0L ||
      length(record$events) > 0L ||
      length(record$blocker_refs) > 0L ||
      !identical(record$source_commit, descriptor$source_revision) ||
      !identical(
        record$current_content_sha256,
        record$enrolled_body_sha256
      )
  }, logical(1))
  if (any(invalid) || length(body_paths) || length(approved_paths) ||
      isTRUE(descriptor$approvals_enabled %||% FALSE)) {
    stop(paste(
      "queue does not match bootstrap state:",
      "records must be draft, round 1, unassigned, event-free,",
      "blocker-free, body-unchanged, approval-disabled, and without",
      "reviewed bodies or approved outputs"
    ))
  }
  invisible(TRUE)
}

main <- function(
  args = commandArgs(trailingOnly = TRUE),
  app_dir = tool_app_dir()
) {
  opts <- parse_args(args)
  pkgload::load_all(app_dir, quiet = TRUE)
  queue_commit <- git_commit_sha(
    opts$repo,
    system2(
      "git", c("-C", opts$repo, "rev-parse", "HEAD"),
      stdout = TRUE,
      env = "GIT_NO_REPLACE_OBJECTS=1"
    )[[1L]]
  )
  queue_prefix <- "extraction/30_review"
  paths <- sub(
    paste0("^", queue_prefix, "/"),
    "",
    git_tree_paths(opts$repo, queue_commit, queue_prefix)
  )
  controls <- intersect(
    c("queue-descriptor.yml", "queue-manifest.yml"),
    paths
  )
  if (length(controls) != 1L) {
    stop("queue must contain exactly one simplified or production-v2 control")
  }
  control_path <- if (identical(controls, "queue-descriptor.yml")) {
    reviewapp:::QUEUE_DESCRIPTOR_PATH
  } else {
    reviewapp:::LEGACY_QUEUE_MANIFEST_PATH
  }
  control_raw <- git_regular_blob_raw(
    opts$repo,
    queue_commit,
    file.path(queue_prefix, controls)
  )
  descriptor <- if (identical(control_path, reviewapp:::LEGACY_QUEUE_MANIFEST_PATH) &&
                    isTRUE(opts$bootstrap)) {
    reviewapp:::parse_legacy_queue_manifest(
      rawToChar(control_raw),
      require_approval_disabled = TRUE
    )
  } else {
    reviewapp:::parse_queue_control(rawToChar(control_raw), control_path)
  }
  if (!reviewapp:::.is_sha1(opts$expected_source) ||
      !identical(descriptor$source_revision, opts$expected_source)) {
    stop("queue source revision does not match --expected-source")
  }
  git_commit_sha(opts$repo, opts$expected_source)
  if (!reviewapp:::.is_sha256(opts$expected_path_digest)) {
    stop("--expected-path-digest must be a lowercase SHA-256")
  }
  record_paths <- sort(grep("^[^/]+[.]review[.]yml$", paths, value = TRUE))
  body_paths <- grep("^[^/]+[.]body[.]md$", paths, value = TRUE)
  allowed <- c(
    ".gitkeep", controls, record_paths, body_paths,
    if (identical(controls, "queue-manifest.yml") &&
        "queue-index.yml" %in% paths) {
      "queue-index.yml"
    }
  )
  extras <- setdiff(paths, allowed)
  if (length(extras)) {
    stop("unexpected queue paths: ", paste(extras, collapse = ", "))
  }

  records <- lapply(record_paths, function(path) {
    raw <- git_regular_blob_raw(
      opts$repo,
      queue_commit,
      file.path(queue_prefix, path)
    )
    record <- reviewapp:::parse_review_record(rawToChar(raw))
    reviewapp:::validate_review_record_v2(record)
    if (!identical(path, sprintf("%s.review.yml", record$artifact_id))) {
      stop("review record filename is not canonical")
    }
    git_commit_sha(opts$repo, record$source_commit)
    source_raw <- git_blob_raw(
      opts$repo,
      record$source_commit,
      record$source_artifact_path
    )
    if (!record_matches_source_bytes(record, source_raw)) {
      stop(sprintf(
        "record '%s' does not match enrolled source bytes",
        record$artifact_id
      ))
    }
    body_path <- sprintf("%s.body.md", record$artifact_id)
    current_hash <- if (body_path %in% body_paths) {
      reviewapp:::hash_raw(git_regular_blob_raw(
        opts$repo,
        queue_commit,
        file.path(queue_prefix, body_path)
      ))
    } else {
      record$enrolled_body_sha256
    }
    if (!identical(current_hash, record$current_content_sha256)) {
      stop(sprintf(
        "record '%s' reviewed-body hash does not match persisted content",
        record$artifact_id
      ))
    }
    record
  })
  if (length(records) != opts$expected_count) {
    stop(sprintf(
      "queue record count mismatch: expected %d, found %d",
      opts$expected_count,
      length(records)
    ))
  }
  source_paths <- vapply(
    records,
    function(record) record$source_artifact_path,
    character(1)
  )
  if (!identical(
    reviewapp:::queue_path_set_digest(source_paths),
    opts$expected_path_digest
  )) {
    stop("queue source path set does not match --expected-path-digest")
  }
  reviewapp:::validate_queue_record_set(records, descriptor)
  approved_prefix <- "extraction/40_approved"
  approved_paths <- sub(
    paste0("^", approved_prefix, "/"),
    "",
    git_tree_paths(opts$repo, queue_commit, approved_prefix)
  )
  approved_paths <- setdiff(approved_paths, ".gitkeep")
  if (isTRUE(opts$bootstrap)) {
    validate_bootstrap_state(
      records,
      descriptor,
      body_paths,
      approved_paths
    )
  }
  if (!identical(
    git_commit_sha(
      opts$repo,
      system2(
        "git", c("-C", opts$repo, "rev-parse", "HEAD"),
        stdout = TRUE,
        env = "GIT_NO_REPLACE_OBJECTS=1"
      )[[1L]]
    ),
    queue_commit
  )) {
    stop("queue commit moved during validation")
  }
  cat(sprintf(
    "validated review queue: %d records; source %s\n",
    length(records),
    descriptor$source_revision
  ))
  invisible(TRUE)
}

`%||%` <- function(a, b) if (is.null(a)) b else a

if (!identical(Sys.getenv("REVIEWAPP_TOOL_TESTING"), "1")) {
  tryCatch(main(), error = function(error) {
    message("review queue validation failed: ", conditionMessage(error))
    quit(status = 1L)
  })
}
