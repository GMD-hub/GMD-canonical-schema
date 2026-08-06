# Step 7 -- partial-failure detection and operator recovery (R18).
#
# If a multi-step Git operation fails partway, the recovery surface reports
# exactly which steps succeeded/failed and never marks the review-record
# transition as applied unless the full atomic operation completed.

.fake_recovery_adapter <- function(http_fun) {
  reviewapp::new_github_adapter(
    owner = "GMD-hub", repo = "fixture-repo",
    default_branch = "main", review_branch = "review",
    get_token = function() "ghu_testtoken",
    http = http_fun
  )
}

# happy path through the recovery wrapper
test_that("recovery wrapper reports success and applies the transition on a full atomic write", {
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-1"
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      return(list(tree = list(list(path = "a.md", type = "blob", sha = "blob-a"))))
    }
    if (grepl("git/blobs$", url) && method == "POST") return(list(sha = "nb1"))
    if (grepl("git/trees$", url) && method == "POST") return(list(sha = "tree1"))
    if (grepl("git/commits$", url) && method == "POST") return(list(sha = "c1"))
    if (grepl("git/refs/heads/review", url) && method == "PATCH") {
      state$commit <- "c1"
      return(list(object = list(sha = "c1")))
    }
    list(object = list())
  }
  ad <- .fake_recovery_adapter(http_fun)
  report <- reviewapp::adapter_write_with_recovery(
    ad,
    changes = list("a.md" = "x"),
    expected_ref_sha = "commit-1",
    expected_blob_shas = list("a.md" = "blob-a"),
    message = "apply"
  )
  expect_true(report$ok)
  expect_true(report$transition_applied)
  expect_identical(report$commit_sha, "c1")
})

# simulated failure after tree creation but before ref update -> partial failure,
# transition NOT applied
test_that("partial failure after ref update step is reported and never claims the transition", {
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-1"
  calls <- character(0)
  http_fun <- function(method, url, token, body = NULL) {
    calls <<- c(calls, url)
    if (grepl("git/ref/heads/review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      return(list(tree = list(list(path = "a.md", type = "blob", sha = "blob-a"))))
    }
    if (grepl("git/blobs$", url) && method == "POST") return(list(sha = "nb1"))
    if (grepl("git/trees$", url) && method == "POST") return(list(sha = "tree1"))
    if (grepl("git/commits$", url) && method == "POST") {
      # simulate failure returning no commit sha (tree exists, commit failed)
      stop(reviewapp::partial_failure_error("commit creation failed partway"))
    }
    list(object = list())
  }
  ad <- .fake_recovery_adapter(http_fun)
  report <- reviewapp::adapter_write_with_recovery(
    ad,
    changes = list("a.md" = "x"),
    expected_ref_sha = "commit-1",
    expected_blob_shas = list("a.md" = "blob-a"),
    message = "apply"
  )
  expect_false(report$ok)
  expect_false(report$transition_applied)
  expect_identical(report$error$kind, "partial")
  expect_null(report$commit_sha)
  # ref did not move
  expect_identical(state$commit, "commit-1")
})

# recovery wrapper returns a structured stale report (no partial-failure claim)
test_that("recovery wrapper surfaces a stale write without claiming a transition", {
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-2" # moved since load
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    list(object = list())
  }
  ad <- .fake_recovery_adapter(http_fun)
  report <- reviewapp::adapter_write_with_recovery(
    ad,
    changes = list("a.md" = "x"),
    expected_ref_sha = "commit-1",
    expected_blob_shas = list("a.md" = "blob-a"),
    message = "apply"
  )
  expect_false(report$ok)
  expect_false(report$transition_applied)
  expect_identical(report$error$kind, "stale")
})

# recovery_report_text renders a human-readable operator message
test_that("recovery_report_text renders useful operator text", {
  expect_match(
    reviewapp::recovery_report_text(list(ok = TRUE, commit_sha = "c1", error = NULL)),
    "Write succeeded"
  )
  expect_match(
    reviewapp::recovery_report_text(list(
      ok = FALSE, transition_applied = FALSE, steps_completed = c("staleness-check", "blob-creation"),
      error = list(kind = "partial", message = "tree creation failed partway")
    )),
    "PARTIAL FAILURE"
  )
})
