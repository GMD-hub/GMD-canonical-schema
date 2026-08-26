connect_attestor_root <- function() {
  tryCatch(
    rprojroot::find_root(rprojroot::has_file("AGENTS.md"), path = getwd()),
    error = function(error) NULL
  )
}

load_connect_attestor <- function() {
  root <- connect_attestor_root()
  if (is.null(root)) return(NULL)
  environment <- new.env(parent = globalenv())
  sys.source(
    file.path(root, "review-app", "tools", "attest-connect.R"),
    envir = environment
  )
  environment
}

connect_attestor_commit <- paste(rep("a", 40L), collapse = "")
connect_attestor_repository <- "https://github.com/GMD-hub/repo.git"

connect_attestor_args <- function(commit = connect_attestor_commit) {
  c(
    "--server", "https://connect.example.org",
    "--guid", "content-guid",
    "--expected-repository", connect_attestor_repository,
    "--expected-branch", "main",
    "--expected-directory", "review-app",
    "--expected-commit", commit
  )
}

connect_attestor_fixture <- function(family = c("legacy", "current")) {
  family <- match.arg(family)
  content <- list(
    guid = "content-guid",
    name = "review-app",
    bundle_id = "101",
    last_deployed_time = "2026-08-26T12:00:00Z",
    r_version = "4.4.1",
    app_mode = "shiny",
    api_key = "super-secret"
  )
  metadata <- list(
    source = if (identical(family, "legacy")) "review-app" else "git",
    source_branch = "main",
    source_commit = connect_attestor_commit,
    source_repo = connect_attestor_repository,
    api_key = "super-secret"
  )
  repository <- list(
    branch = "main",
    directory = "review-app",
    last_known_commit = connect_attestor_commit,
    last_error = NULL,
    api_key = "super-secret"
  )
  if (identical(family, "legacy")) {
    content$content_status <- "ready"
    content$runtime_status <- "running"
    repository$repository_url <- connect_attestor_repository
  } else {
    repository$repository <- connect_attestor_repository
  }
  list(
    family = family,
    content = content,
    bundles = list(
      list(
        id = "101",
        active = TRUE,
        created_time = "2026-08-26T12:00:00Z",
        r_version = "4.4.1",
        metadata = metadata
      ),
      list(id = "100", active = FALSE)
    ),
    jobs = list(
      list(
        id = "20",
        bundle_id = "101",
        status = if (identical(family, "legacy")) "finished" else 2,
        exit_code = 0,
        error = NULL,
        api_key = "super-secret"
      ),
      list(
        id = "10",
        bundle_id = "100",
        status = "succeeded",
        exit_code = 0,
        error = NULL
      )
    ),
    repository = repository
  )
}

connect_attestor_request <- function(fixture) {
  force(fixture)
  function(url, api_key) {
    expect_identical(api_key, "super-secret")
    if (grepl("/bundles[?]page=2$", url)) {
      return(list(results = fixture$bundles[2L]))
    }
    if (grepl("/bundles$", url)) {
      if (identical(fixture$family, "legacy")) {
        return(list(
          results = fixture$bundles[1L],
          `next` = paste0(url, "?page=2")
        ))
      }
      return(fixture$bundles)
    }
    if (grepl("/jobs$", url)) {
      if (identical(fixture$family, "legacy")) {
        return(list(results = fixture$jobs))
      }
      return(fixture$jobs)
    }
    if (grepl("/repository$", url)) return(fixture$repository)
    fixture$content
  }
}

attest_connect_fixture <- function(environment, fixture) {
  opts <- environment$parse_args(connect_attestor_args())
  environment$attest_connect(opts, connect_attestor_request(fixture))
}

test_that("Connect attestor accepts and redacts legacy API evidence", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")
  fixture <- connect_attestor_fixture("legacy")

  evidence <- attest_connect_fixture(environment, fixture)
  repeated <- attest_connect_fixture(environment, fixture)
  serialized <- jsonlite::toJSON(evidence, auto_unbox = TRUE, null = "null")

  expect_identical(evidence, repeated)
  expect_identical(
    vapply(evidence$bundles, `[[`, character(1), "id"),
    c("100", "101")
  )
  expect_identical(
    vapply(evidence$jobs, `[[`, character(1), "id"),
    c("10", "20")
  )
  expect_identical(
    evidence$repository$repository_url,
    connect_attestor_repository
  )
  expect_false(grepl("super-secret", serialized, fixed = TRUE))
})

test_that("Connect attestor accepts and redacts current API evidence", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")
  fixture <- connect_attestor_fixture("current")

  evidence <- attest_connect_fixture(environment, fixture)
  repeated <- attest_connect_fixture(environment, fixture)
  serialized <- jsonlite::toJSON(evidence, auto_unbox = TRUE, null = "null")

  expect_identical(evidence, repeated)
  expect_identical(evidence$repository$repository_url, connect_attestor_repository)
  expect_false("repository" %in% names(evidence$repository))
  expect_false("content_status" %in% names(evidence$content))
  expect_false("runtime_status" %in% names(evidence$content))
  expect_false(grepl("super-secret", serialized, fixed = TRUE))
})

test_that("Connect attestor requires exact content deployment identity", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")

  for (field in c("app_mode", "last_deployed_time", "r_version")) {
    fixture <- connect_attestor_fixture("current")
    fixture$content[[field]] <- NULL
    expect_error(
      attest_connect_fixture(environment, fixture),
      "content identity or deployment health",
      info = field
    )
  }
  fixture <- connect_attestor_fixture("legacy")
  fixture$content$content_status <- "failed"
  expect_error(
    attest_connect_fixture(environment, fixture),
    "content identity or deployment health"
  )
})

test_that("Connect attestor rejects missing or ambiguous active bundles", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")

  missing <- connect_attestor_fixture("current")
  missing$bundles[[1L]]$active <- FALSE
  expect_error(
    attest_connect_fixture(environment, missing),
    "active deployment bundle is missing or ambiguous"
  )

  ambiguous <- connect_attestor_fixture("current")
  ambiguous$bundles[[3L]] <- ambiguous$bundles[[1L]]
  ambiguous$bundles[[3L]]$id <- "102"
  expect_error(
    attest_connect_fixture(environment, ambiguous),
    "active deployment bundle is missing or ambiguous"
  )
})

test_that("Connect attestor rejects active bundle source mismatch", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")
  fixture <- connect_attestor_fixture("current")
  fixture$bundles[[1L]]$metadata$source <- "wrong-directory"

  expect_error(
    attest_connect_fixture(environment, fixture),
    "active bundle source identity"
  )
})

test_that("Connect attestor never partially matches response field names", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")

  partial_content <- connect_attestor_fixture("current")
  partial_content$content$guid_value <- partial_content$content$guid
  partial_content$content$guid <- NULL
  expect_error(
    attest_connect_fixture(environment, partial_content),
    "content identity"
  )

  partial_repository <- connect_attestor_fixture("current")
  partial_repository$repository$repository_value <-
    partial_repository$repository$repository
  partial_repository$repository$repository <- NULL
  expect_error(
    attest_connect_fixture(environment, partial_repository),
    "repository_url"
  )

  partial_metadata <- connect_attestor_fixture("current")
  partial_metadata$bundles[[1L]]$metadata$source_repository <-
    partial_metadata$bundles[[1L]]$metadata$source_repo
  partial_metadata$bundles[[1L]]$metadata$source_repo <- NULL
  expect_error(
    attest_connect_fixture(environment, partial_metadata),
    "active bundle source identity"
  )

  partial_job <- connect_attestor_fixture("current")
  partial_job$jobs[[1L]]$status_code <- partial_job$jobs[[1L]]$status
  partial_job$jobs[[1L]]$status <- NULL
  expect_error(
    attest_connect_fixture(environment, partial_job),
    "successful job"
  )
})

test_that("Connect attestor rejects repository errors and alias mismatches", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")

  mismatch <- connect_attestor_fixture("current")
  mismatch$repository$repository <- "https://github.com/GMD-hub/wrong.git"
  expect_error(
    attest_connect_fixture(environment, mismatch),
    "repository repository_url does not match expectation"
  )

  repository_error <- connect_attestor_fixture("current")
  repository_error$repository$last_error <- "synchronization failed"
  expect_error(
    attest_connect_fixture(environment, repository_error),
    "synchronization error"
  )
})

test_that("Connect attestor requires a successful active-bundle job", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")

  older_only <- connect_attestor_fixture("current")
  older_only$jobs[[1L]]$bundle_id <- "100"
  expect_error(
    attest_connect_fixture(environment, older_only),
    "successful job"
  )

  nonzero <- connect_attestor_fixture("current")
  nonzero$jobs[[1L]]$exit_code <- 1
  expect_error(attest_connect_fixture(environment, nonzero), "successful job")

  failed <- connect_attestor_fixture("current")
  failed$jobs[[1L]]$status <- "failed"
  expect_error(attest_connect_fixture(environment, failed), "successful job")

  errored <- connect_attestor_fixture("current")
  errored$jobs[[1L]]$error <- "deployment failed"
  expect_error(attest_connect_fixture(environment, errored), "successful job")
})

test_that("Connect attestor accepts documented successful job statuses", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")

  for (status in list(2, "finished", "success", "succeeded")) {
    fixture <- connect_attestor_fixture("current")
    fixture$jobs[[1L]]$status <- status
    expect_no_error(attest_connect_fixture(environment, fixture))
  }
})

test_that("Connect attestor rejects pagination outside its endpoint allowlist", {
  withr::local_envvar(REVIEWAPP_TOOL_TESTING = "1")
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")
  expect_error(
    environment$collect_pages(
      "https://evil.example.org/page",
      "https://connect.example.org/__api__/v1/content/content-guid",
      "secret", function(...) list()
    ),
    "allowlist"
  )
})

test_that("Connect attestor keeps API keys out of arguments and evidence", {
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- load_connect_attestor()
  if (is.null(environment)) skip("repository tool is unavailable in the built package")

  expect_error(
    environment$parse_args(c(
      connect_attestor_args(), "--api-key", "command-line-secret"
    )),
    "exactly the documented arguments"
  )
  evidence <- attest_connect_fixture(
    environment,
    connect_attestor_fixture("current")
  )
  expect_false(grepl(
    "super-secret",
    jsonlite::toJSON(evidence, auto_unbox = TRUE, null = "null"),
    fixed = TRUE
  ))

  reflected <- connect_attestor_fixture("current")
  reflected$jobs[[2L]]$status <- "super-secret"
  expect_error(
    attest_connect_fixture(environment, reflected),
    "secret material"
  )

  reflected_name <- connect_attestor_fixture("current")
  reflected_name$repository$polling <- setNames(list(TRUE), "super-secret")
  expect_error(
    attest_connect_fixture(environment, reflected_name),
    "secret material"
  )
})
