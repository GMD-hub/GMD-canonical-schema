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
