migration_cli_path <- file.path("tools", "migrate-review-queue.R")
if (!file.exists(migration_cli_path)) {
  migration_cli_path <- file.path("..", "..", "tools", "migrate-review-queue.R")
}
migration_cli <- new.env(parent = globalenv())
migration_cli_available <- file.exists(migration_cli_path)
if (migration_cli_available) {
  sys.source(migration_cli_path, envir = migration_cli)
}

valid_migration_args <- function(target = "review-staging-wave3") {
  c(
    "--target-branch", target,
    "--expected-head", paste(rep("c", 40L), collapse = ""),
    "--actor", "acastanedaa"
  )
}

migration_cli_repository_env <- function() {
  c(
    REVIEW_APP_GH_OWNER = "GMD-hub",
    REVIEW_APP_GH_REPO = "GMD-canonical-schema",
    REVIEW_APP_GH_DEFAULT_BRANCH = "main"
  )
}

migration_cli_result <- function(expected_head) {
  descriptor <- new_queue_descriptor(
    queue_id = "fixture-queue",
    source_revision = paste(rep("a", 40L), collapse = ""),
    created_at = "2026-08-24T13:25:07Z",
    created_by = "admin@example.org",
    expected_record_count = 1L,
    record_set_sha256 = hash_body("fixture record set"),
    approvals_enabled = FALSE
  )
  list(
    ok = TRUE,
    old_head = expected_head,
    commit_sha = paste(rep("d", 40L), collapse = ""),
    source_format = "production_v2",
    descriptor = descriptor,
    record_count = 1L,
    preserved_record_blobs = c(
      "extraction/30_review/VAR-one.review.yml" =
        paste(rep("e", 40L), collapse = "")
    )
  )
}

test_that("migration CLI rejects missing, duplicate, malformed, and unsupported arguments", {
  if (!migration_cli_available) {
    skip("repository migration CLI is unavailable in the built package")
  }
  valid <- valid_migration_args()
  invalid <- list(
    character(),
    c(valid, "--actor", "other-admin"),
    valid[-length(valid)],
    c(valid, "--token", "command-line-secret"),
    replace(valid, 2L, "review staging"),
    c(valid, "--authorize-production", "--authorize-production")
  )
  for (args in invalid) {
    expect_error(migration_cli$parse_args(args))
  }
})

test_that("migration CLI requires a lowercase expected-head SHA-1", {
  if (!migration_cli_available) {
    skip("repository migration CLI is unavailable in the built package")
  }
  invalid <- c(
    "abc",
    paste(rep("A", 40L), collapse = ""),
    paste(rep("a", 39L), collapse = ""),
    paste(rep("g", 40L), collapse = "")
  )
  for (sha in invalid) {
    args <- valid_migration_args()
    args[[4L]] <- sha
    expect_error(migration_cli$parse_args(args), "lowercase Git SHA-1")
  }
})

test_that("migration CLI rejects default and preserved branch targets", {
  if (!migration_cli_available) {
    skip("repository migration CLI is unavailable in the built package")
  }
  for (target in c("main", "trunk")) {
    opts <- migration_cli$parse_args(valid_migration_args(target))
    expect_error(
      migration_cli$assert_migration_target(opts, "trunk"),
      "default branch"
    )
  }
  opts <- migration_cli$parse_args(valid_migration_args("review"))
  expect_error(
    migration_cli$assert_migration_target(opts, "main"),
    "preserved review branch"
  )
})

test_that("migration CLI refuses review-production without separate authorization", {
  if (!migration_cli_available) {
    skip("repository migration CLI is unavailable in the built package")
  }
  opts <- migration_cli$parse_args(valid_migration_args("review-production"))
  expect_error(
    migration_cli$assert_migration_target(opts, "main"),
    "separate --authorize-production"
  )
})

test_that("migration CLI builds an adapter for the explicit staging target", {
  if (!migration_cli_available) {
    skip("repository migration CLI is unavailable in the built package")
  }
  withr::local_envvar(c(
    migration_cli_repository_env(),
    REVIEW_APP_GH_REVIEW_BRANCH = "review-production",
    GITHUB_APP_ID = "test-app-id",
    GITHUB_APP_INSTALLATION_ID = "test-installation-id",
    GITHUB_APP_PRIVATE_KEY = "test-private-key"
  ))
  opts <- migration_cli$parse_args(valid_migration_args())
  repository <- migration_cli$migration_repository_config()
  adapter <- migration_cli$build_migration_adapter(opts, repository)
  expect_identical(adapter$review_branch, "review-staging-wave3")
  expect_false(adapter$read_only)
})

test_that("migration CLI requires repository and GitHub App environment variables", {
  if (!migration_cli_available) {
    skip("repository migration CLI is unavailable in the built package")
  }
  withr::local_envvar(c(
    REVIEW_APP_GH_OWNER = NA_character_,
    REVIEW_APP_GH_REPO = NA_character_,
    REVIEW_APP_GH_DEFAULT_BRANCH = NA_character_
  ))
  expect_error(
    migration_cli$migration_repository_config(),
    "REVIEW_APP_GH_OWNER"
  )

  withr::local_envvar(c(
    GITHUB_APP_ID = NA_character_,
    GITHUB_APP_INSTALLATION_ID = NA_character_,
    GITHUB_APP_PRIVATE_KEY = NA_character_
  ))
  opts <- migration_cli$parse_args(valid_migration_args())
  repository <- list(
    owner = "GMD-hub",
    repo = "GMD-canonical-schema",
    default_branch = "main"
  )
  expect_error(
    migration_cli$build_migration_adapter(opts, repository),
    "GITHUB_APP_ID"
  )
})

test_that("migration CLI calls migrate_review_queue and emits redacted evidence", {
  if (!migration_cli_available) {
    skip("repository migration CLI is unavailable in the built package")
  }
  role_map <- withr::local_tempfile(lines = c(
    "roles:",
    "  - identity: role-map-secret",
    "    role: administrator"
  ))
  withr::local_envvar(c(
    migration_cli_repository_env(),
    REVIEW_APP_GH_REVIEW_BRANCH = "review-production",
    REVIEW_APP_ROLES = role_map,
    GITHUB_APP_ID = "supplied-app-secret",
    GITHUB_APP_INSTALLATION_ID = "supplied-installation-secret",
    GITHUB_APP_PRIVATE_KEY = "supplied-private-key-secret"
  ))
  called <- NULL
  adapter_factory <- function(opts, repository) {
    new_github_adapter(
      repository$owner,
      repository$repo,
      repository$default_branch,
      opts$target_branch,
      read_only = FALSE,
      get_token = function() stop("token access is not allowed"),
      http = function(...) stop("network access is not allowed")
    )
  }
  migrate_queue <- function(adapter, actor, expected_head) {
    called <<- list(
      function_name = "migrate_review_queue",
      target_branch = adapter$review_branch,
      actor = actor,
      expected_head = expected_head
    )
    migration_cli_result(expected_head)
  }
  output <- capture.output(evidence <- migration_cli$main(
    args = valid_migration_args(),
    app_dir = ".",
    package_loader = function(...) invisible(TRUE),
    adapter_factory = adapter_factory,
    migrate_queue = migrate_queue
  ))
  json <- paste(output, collapse = "\n")
  parsed <- jsonlite::fromJSON(json, simplifyVector = FALSE)

  expect_identical(called$function_name, "migrate_review_queue")
  expect_identical(called$target_branch, "review-staging-wave3")
  expect_identical(called$actor, "acastanedaa")
  expect_identical(called$expected_head, evidence$expected_old_head)
  expect_identical(parsed$repository, "GMD-hub/GMD-canonical-schema")
  expect_identical(parsed$target_branch, "review-staging-wave3")
  expect_identical(parsed$expected_old_head, evidence$expected_old_head)
  expect_identical(parsed$migration_commit, evidence$migration_commit)
  expect_identical(parsed$queue_id, "fixture-queue")
  expect_identical(parsed$source_revision, paste(rep("a", 40L), collapse = ""))
  expect_identical(parsed$source_format, "production_v2")
  expect_identical(parsed$record_count, 1L)
  expect_identical(parsed$record_set_sha256, evidence$record_set_sha256)
  expect_identical(
    parsed$preserved_record_blob_sha256,
    evidence$preserved_record_blob_sha256
  )
  expect_identical(parsed$approvals_enabled, FALSE)
  for (secret in c(
    "supplied-app-secret",
    "supplied-installation-secret",
    "supplied-private-key-secret",
    "role-map-secret"
  )) {
    expect_false(grepl(secret, json, fixed = TRUE))
  }
})

test_that("migration CLI failure returns nonzero without success evidence", {
  if (!migration_cli_available) {
    skip("repository migration CLI is unavailable in the built package")
  }
  stdout <- withr::local_tempfile()
  stderr <- withr::local_tempfile()
  status <- system2(
    file.path(R.home("bin"), "Rscript"),
    normalizePath(migration_cli_path),
    stdout = stdout,
    stderr = stderr
  )
  expect_identical(status, 1L)
  expect_length(readLines(stdout, warn = FALSE), 0L)
  expect_true(
    "review queue migration failed" %in% readLines(stderr, warn = FALSE)
  )
})
