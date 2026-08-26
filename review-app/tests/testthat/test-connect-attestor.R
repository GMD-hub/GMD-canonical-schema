test_that("Connect attestor is strict, paginated, deterministic, and redacted", {
  root <- tryCatch(
    rprojroot::find_root(rprojroot::has_file("AGENTS.md"), path = getwd()),
    error = function(error) NULL
  )
  if (is.null(root)) skip("repository tool is unavailable in the built package")
  tool <- file.path(root, "review-app", "tools", "attest-connect.R")
  withr::local_envvar(
    REVIEWAPP_TOOL_TESTING = "1",
    CONNECT_API_KEY = "super-secret"
  )
  environment <- new.env(parent = globalenv())
  sys.source(tool, envir = environment)
  commit <- paste(rep("a", 40L), collapse = "")
  args <- c(
    "--server", "https://connect.example.org", "--guid", "content-guid",
    "--expected-repository", "https://github.com/GMD-hub/repo.git",
    "--expected-branch", "main", "--expected-directory", "review-app",
    "--expected-commit", commit
  )
  opts <- environment$parse_args(args)
  calls <- character()
  request <- function(url, api_key) {
    expect_identical(api_key, "super-secret")
    calls <<- c(calls, url)
    if (grepl("/bundles[?]page=2$", url)) return(list(results = list(list(
      id = "2", active = FALSE
    ))))
    if (grepl("/bundles$", url)) return(list(
      results = list(list(
        id = "1", active = TRUE,
        metadata = list(
          source = "review-app", source_branch = "main",
          source_commit = commit,
          source_repo = "https://github.com/GMD-hub/repo.git"
        )
      )),
      `next` = paste0(url, "?page=2")
    ))
    if (grepl("/jobs$", url)) return(list(results = list(
      list(id = "20", status = "finished"),
      list(id = "10", status = "finished")
    )))
    if (grepl("/repository$", url)) return(list(
      repository_url = "https://github.com/GMD-hub/repo.git",
      branch = "main", directory = "review-app", last_known_commit = commit,
      last_error = NULL
    ))
    list(
      guid = "content-guid", bundle_id = "1", content_status = "ready",
      runtime_status = "running"
    )
  }

  evidence <- environment$attest_connect(opts, request)

  expect_identical(vapply(evidence$jobs, `[[`, character(1), "id"), c("10", "20"))
  expect_false(grepl("super-secret", jsonlite::toJSON(evidence), fixed = TRUE))
  expect_length(calls, 5L)
  expect_error(environment$parse_args(c(args, "--api-key", "secret")), "exactly")
  broken <- opts
  broken$commit <- paste(rep("b", 40L), collapse = "")
  expect_error(environment$attest_connect(broken, request), "last_known_commit")
})

test_that("Connect attestor rejects pagination outside its endpoint allowlist", {
  root <- tryCatch(
    rprojroot::find_root(rprojroot::has_file("AGENTS.md"), path = getwd()),
    error = function(error) NULL
  )
  if (is.null(root)) skip("repository tool is unavailable in the built package")
  withr::local_envvar(REVIEWAPP_TOOL_TESTING = "1")
  environment <- new.env(parent = globalenv())
  sys.source(
    file.path(root, "review-app", "tools", "attest-connect.R"),
    envir = environment
  )
  expect_error(
    environment$collect_pages(
      "https://evil.example.org/page",
      "https://connect.example.org/__api__/v1/content/content-guid",
      "secret", function(...) list()
    ),
    "allowlist"
  )
})
