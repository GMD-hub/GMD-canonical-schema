#!/usr/bin/env Rscript

MIGRATION_REQUIRED_ARGUMENTS <- c(
  "--target-branch", "--expected-head", "--actor"
)
MIGRATION_PRODUCTION_AUTHORIZATION <- "--authorize-production"

migration_usage <- function() {
  paste(
    "usage: migrate-review-queue.R --target-branch <branch>",
    "--expected-head <sha1> --actor <identity>",
    "[--authorize-production]"
  )
}

is_safe_branch_name <- function(branch) {
  is.character(branch) && length(branch) == 1L && !is.na(branch) &&
    nchar(branch, type = "bytes") <= 244L &&
    grepl("^[A-Za-z0-9][A-Za-z0-9._/-]*$", branch) &&
    !grepl("[.][.]|//|@[{]|[.]lock(/|$)", branch) &&
    !grepl("(^|/)[.]|[./]$", branch)
}

parse_args <- function(args) {
  production_count <- sum(args == MIGRATION_PRODUCTION_AUTHORIZATION)
  production_authorized <- identical(production_count, 1L)
  pair_args <- args[args != MIGRATION_PRODUCTION_AUTHORIZATION]
  malformed <- production_count > 1L ||
    length(pair_args) != 2L * length(MIGRATION_REQUIRED_ARGUMENTS)
  if (!malformed) {
    flags <- pair_args[seq(1L, length(pair_args), by = 2L)]
    values <- pair_args[seq(2L, length(pair_args), by = 2L)]
    malformed <- anyDuplicated(flags) ||
      !setequal(flags, MIGRATION_REQUIRED_ARGUMENTS) ||
      any(startsWith(values, "--")) ||
      any(!nzchar(values))
  }
  if (malformed) {
    stop(paste(
      migration_usage(),
      "arguments are missing, duplicated, malformed, or unsupported"
    ))
  }
  values <- stats::setNames(values, flags)
  target_branch <- values[["--target-branch"]]
  expected_head <- values[["--expected-head"]]
  actor <- values[["--actor"]]
  if (!is_safe_branch_name(target_branch)) {
    stop("--target-branch is not a safe Git branch name")
  }
  if (!grepl("^[0-9a-f]{40}$", expected_head)) {
    stop("--expected-head must be a lowercase Git SHA-1")
  }
  if (!grepl("^[A-Za-z0-9][A-Za-z0-9._@+-]*$", actor)) {
    stop("--actor must be one repository role-map identity")
  }
  list(
    target_branch = target_branch,
    expected_head = expected_head,
    actor = actor,
    production_authorized = production_authorized
  )
}

tool_app_dir <- function(command_args = commandArgs(trailingOnly = FALSE)) {
  file_args <- grep("^--file=", command_args, value = TRUE)
  if (length(file_args) != 1L) {
    stop("cannot resolve migration script path")
  }
  script_path <- normalizePath(
    sub("^--file=", "", file_args[[1L]]),
    mustWork = TRUE
  )
  app_dir <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
  if (!file.exists(file.path(app_dir, "DESCRIPTION"))) {
    stop("migration script is not inside the review-app package")
  }
  app_dir
}

load_reviewapp <- function(app_dir) {
  pkgload::load_all(app_dir, quiet = TRUE)
}

required_environment <- function(names, label) {
  values <- stats::setNames(vapply(
    names,
    Sys.getenv,
    character(1),
    unset = ""
  ), names)
  missing <- names[!nzchar(values)]
  if (length(missing)) {
    stop(sprintf(
      "%s environment variables are required: %s",
      label,
      paste(missing, collapse = ", ")
    ))
  }
  values
}

migration_repository_config <- function() {
  values <- required_environment(
    c(
      "REVIEW_APP_GH_OWNER",
      "REVIEW_APP_GH_REPO",
      "REVIEW_APP_GH_DEFAULT_BRANCH"
    ),
    "repository"
  )
  if (any(!grepl("^[A-Za-z0-9_.-]+$", values[1:2])) ||
      !is_safe_branch_name(values[["REVIEW_APP_GH_DEFAULT_BRANCH"]])) {
    stop("repository environment configuration is malformed")
  }
  list(
    owner = values[["REVIEW_APP_GH_OWNER"]],
    repo = values[["REVIEW_APP_GH_REPO"]],
    default_branch = values[["REVIEW_APP_GH_DEFAULT_BRANCH"]]
  )
}

migration_github_app_credentials <- function() {
  values <- required_environment(
    c(
      "GITHUB_APP_ID",
      "GITHUB_APP_INSTALLATION_ID",
      "GITHUB_APP_PRIVATE_KEY"
    ),
    "GitHub App credential"
  )
  as.list(values)
}

assert_migration_target <- function(opts, default_branch) {
  target <- tolower(opts$target_branch)
  if (identical(opts$target_branch, default_branch) || identical(target, "main")) {
    stop("migration target must not be main or the configured default branch")
  }
  if (identical(target, "review")) {
    stop("the preserved review branch is not a migration target")
  }
  if (identical(target, "review-production") &&
      !isTRUE(opts$production_authorized)) {
    stop(paste(
      "review-production requires the separate",
      MIGRATION_PRODUCTION_AUTHORIZATION,
      "argument"
    ))
  }
  invisible(TRUE)
}

build_migration_adapter <- function(opts, repository) {
  credentials <- migration_github_app_credentials()
  token_cache <- reviewapp::new_token_cache()
  reviewapp::new_github_adapter(
    owner = repository$owner,
    repo = repository$repo,
    default_branch = repository$default_branch,
    review_branch = opts$target_branch,
    read_only = FALSE,
    get_token = function() {
      reviewapp::installation_token(
        get_token = function() reviewapp::gh_exchange_installation_token(
          app_id = credentials$GITHUB_APP_ID,
          private_key_pem = credentials$GITHUB_APP_PRIVATE_KEY,
          installation_id = credentials$GITHUB_APP_INSTALLATION_ID
        ),
        cache = token_cache
      )
    }
  )
}

assert_adapter_identity <- function(adapter, opts, repository) {
  if (!inherits(adapter, "reviewapp_github_adapter") ||
      !identical(adapter$owner, repository$owner) ||
      !identical(adapter$repo, repository$repo) ||
      !identical(adapter$default_branch, repository$default_branch) ||
      !identical(adapter$review_branch, opts$target_branch) ||
      isTRUE(adapter$read_only)) {
    stop("migration adapter does not match the explicit repository target")
  }
  invisible(TRUE)
}

preserved_record_blob_digest <- function(blobs) {
  valid <- is.character(blobs) && length(blobs) > 0L &&
    !is.null(names(blobs)) && !anyNA(names(blobs)) &&
    all(nzchar(names(blobs))) && !anyDuplicated(names(blobs)) &&
    all(grepl(
      "^extraction/30_review/VAR-[a-z0-9]+[.]review[.]yml$",
      names(blobs)
    )) && all(grepl("^[0-9a-f]{40}$", blobs))
  if (!valid) {
    stop("migration result contains invalid preserved record blob identities")
  }
  paths <- sort(names(blobs))
  lines <- vapply(paths, function(path) {
    sha <- blobs[[path]]
    paste0(
      nchar(path, type = "bytes"), ":", path,
      nchar(sha, type = "bytes"), ":", sha
    )
  }, character(1))
  reviewapp:::hash_body(paste0(paste(lines, collapse = "\n"), "\n"))
}

build_migration_evidence <- function(result, adapter, opts) {
  descriptor <- result$descriptor %||% NULL
  if (!isTRUE(result$ok) || !is.list(descriptor)) {
    stop("migration did not return successful evidence inputs")
  }
  reviewapp::validate_queue_descriptor(descriptor)
  if (!identical(result$old_head, opts$expected_head) ||
      !grepl("^[0-9a-f]{40}$", result$commit_sha %||% "") ||
      identical(result$commit_sha, result$old_head) ||
      !is.character(result$source_format) ||
      length(result$source_format) != 1L ||
      !result$source_format %in% c("production_v2", "descriptor_1_0") ||
      !identical(result$record_count, descriptor$expected_record_count) ||
      !identical(descriptor$approvals_enabled, FALSE)) {
    stop("migration result failed evidence validation")
  }
  preserved_digest <- preserved_record_blob_digest(
    result$preserved_record_blobs
  )
  if (length(result$preserved_record_blobs) != result$record_count) {
    stop("migration result preserved-record count is inconsistent")
  }
  list(
    repository = paste(adapter$owner, adapter$repo, sep = "/"),
    target_branch = opts$target_branch,
    expected_old_head = result$old_head,
    migration_commit = result$commit_sha,
    queue_id = descriptor$queue_id,
    source_revision = descriptor$source_revision,
    source_format = result$source_format,
    record_count = result$record_count,
    record_set_sha256 = descriptor$record_set_sha256,
    preserved_record_blob_sha256 = preserved_digest,
    approvals_enabled = FALSE
  )
}

main <- function(
  args = commandArgs(trailingOnly = TRUE),
  app_dir = tool_app_dir(),
  package_loader = load_reviewapp,
  adapter_factory = build_migration_adapter,
  migrate_queue = NULL
) {
  opts <- parse_args(args)
  package_loader(app_dir)
  repository <- migration_repository_config()
  assert_migration_target(opts, repository$default_branch)
  adapter <- adapter_factory(opts, repository)
  assert_adapter_identity(adapter, opts, repository)
  if (is.null(migrate_queue)) {
    migrate_queue <- getExportedValue("reviewapp", "migrate_review_queue")
  }
  result <- migrate_queue(
    adapter = adapter,
    actor = opts$actor,
    expected_head = opts$expected_head
  )
  evidence <- build_migration_evidence(result, adapter, opts)
  cat(jsonlite::toJSON(
    evidence,
    auto_unbox = TRUE,
    pretty = TRUE,
    null = "null"
  ), "\n")
  invisible(evidence)
}

`%||%` <- function(a, b) if (is.null(a)) b else a

if (!identical(Sys.getenv("REVIEWAPP_TOOL_TESTING"), "1") &&
    sys.nframe() == 0L) {
  tryCatch(main(), error = function(error) {
    message("review queue migration failed")
    quit(status = 1L)
  })
}
