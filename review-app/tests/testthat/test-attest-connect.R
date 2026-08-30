attestor_path <- file.path("tools", "attest-connect.R")
if (!file.exists(attestor_path)) {
  attestor_path <- file.path("..", "..", "tools", "attest-connect.R")
}
attestor <- new.env(parent = globalenv())
attestor_available <- file.exists(attestor_path)
if (attestor_available) sys.source(attestor_path, envir = attestor)

valid_attestor_args <- function() c(
  "--server", "https://connect.example.org",
  "--guid", "content-1234",
  "--expected-repository", "https://github.com/GMD-hub/repo.git",
  "--expected-branch", "main",
  "--expected-directory", "review-app",
  "--expected-commit", paste(rep("a", 40L), collapse = "")
)

test_that("Connect attestor keeps API keys environment-only", {
  if (!attestor_available) skip("repository tool is unavailable in the built package")
  withr::local_envvar(CONNECT_API_KEY = "environment-secret")
  expect_error(
    attestor$parse_args(c(valid_attestor_args(), "--api-key", "command-line-secret")),
    "exactly the documented arguments"
  )
})

test_that("Connect attestor requires its non-secret arguments", {
  if (!attestor_available) skip("repository tool is unavailable in the built package")
  withr::local_envvar(
    CONNECT_SERVER = NA_character_, CONNECT_CONTENT_GUID = NA_character_
  )
  expect_error(attestor$parse_args(character()), "exactly the documented arguments")
})

test_that("Connect attestor rejects unsafe endpoints before requests", {
  if (!attestor_available) skip("repository tool is unavailable in the built package")
  withr::local_envvar(CONNECT_API_KEY = "environment-secret")
  expect_error(
    attestor$parse_args(replace(
      valid_attestor_args(), 2L, "http://connect.example.org"
    )),
    "HTTPS origin"
  )
})

test_that("Connect attestor collects arrays without pagination", {
  if (!attestor_available) skip("repository tool is unavailable in the built package")
  base <- paste0(
    "https://connect.example.org/__api__/v1/content/",
    "content-1234"
  )
  calls <- character()
  request <- function(url, api_key) {
    calls <<- c(calls, url)
    expect_identical(api_key, "environment-secret")
    list(list(id = "2"), list(id = "1"))
  }

  result <- attestor$collect_pages(
    paste0(base, "/bundles"), base, "environment-secret", request
  )

  expect_identical(vapply(result, `[[`, character(1), "id"), c("2", "1"))
  expect_length(calls, 1L)
})

test_that("Connect attestor preserves enveloped pagination", {
  if (!attestor_available) skip("repository tool is unavailable in the built package")
  base <- paste0(
    "https://connect.example.org/__api__/v1/content/",
    "content-1234"
  )
  page_two <- paste0(base, "/jobs?page=2")
  request <- function(url, api_key) {
    expect_identical(api_key, "environment-secret")
    if (identical(url, page_two)) {
      return(list(results = list(list(id = "2"))))
    }
    list(results = list(list(id = "1")), `next` = page_two)
  }

  result <- attestor$collect_pages(
    paste0(base, "/jobs"), base, "environment-secret", request
  )

  expect_identical(vapply(result, `[[`, character(1), "id"), c("1", "2"))
})

test_that("Connect attestor rejects malformed collection objects", {
  if (!attestor_available) skip("repository tool is unavailable in the built package")
  base <- paste0(
    "https://connect.example.org/__api__/v1/content/",
    "content-1234"
  )

  expect_error(
    attestor$collect_pages(
      paste0(base, "/jobs"), base, "environment-secret",
      function(...) list(unexpected = list())
    ),
    "malformed"
  )
  empty_object <- structure(list(), names = character())
  expect_error(
    attestor$collect_pages(
      paste0(base, "/jobs"), base, "environment-secret",
      function(...) list(results = empty_object)
    ),
    "malformed"
  )
})
