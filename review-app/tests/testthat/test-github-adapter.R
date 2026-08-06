# Step 5 & 6 -- GitHub adapter tests (R13, R16, R11, R14, R18).
#
# Covers authenticated reads (content + blob SHA), hash verification, atomic
# multi-file writes, and optimistic-locking staleness rejection. These run
# against an in-memory test double of the GitHub API so the atomicity,
# staleness, and "no lost update" guarantees are proven deterministically and
# without network. A real-disposable-repo integration check is a documented
# manual step in the operator guide.

.fake_adapter <- function(http_fun) {
  reviewapp::new_github_adapter(
    owner = "GMD-hub", repo = "fixture-repo",
    default_branch = "main", review_branch = "review",
    get_token = function() "ghu_testtoken",
    http = http_fun
  )
}

# --- Step 5: reads + hash verification --------------------------------------

test_that("adapter_read_draft returns content and blob SHA from the default branch", {
  http_fun <- function(method, url, token, body = NULL) {
    list(content = base64enc::base64encode(charToRaw("## Title\nbody")), sha = "blob-a")
  }
  ad <- .fake_adapter(http_fun)
  out <- reviewapp::adapter_read_draft(ad, "extraction/20_drafts/dem/VAR-male.md")
  expect_match(out$content, "## Title")
  expect_identical(out$sha, "blob-a")
})

test_that("adapter_read_review / adapter_read_approved read from the review branch", {
  called <- character(0)
  http_fun <- function(method, url, token, body = NULL) {
    called <<- c(called, url)
    list(content = base64enc::base64encode(charToRaw("rev")), sha = "blob-r")
  }
  ad <- .fake_adapter(http_fun)
  r1 <- reviewapp::adapter_read_review(ad, "extraction/30_review/VAR-male.review.yml")
  r2 <- reviewapp::adapter_read_approved(ad, "extraction/40_approved/dem/VAR-male.md")
  expect_identical(r1$sha, "blob-r")
  expect_identical(r2$sha, "blob-r")
  expect_true(any(grepl("review", called)))
})

test_that("verify_body_hash succeeds/fails on matching/mismatching content", {
  body <- "reviewer body"
  expect_true(reviewapp::verify_body_hash(body, reviewapp::hash_body(body)))
  expect_false(reviewapp::verify_body_hash(body, reviewapp::hash_body("other")))
})

# --- Step 6: atomic writes with optimistic locking --------------------------

test_that("atomic write succeeds with multiple files and rolls the branch forward", {
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-1"
  counter <- 0L
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      return(list(tree = list(
        list(path = "a.md", type = "blob", sha = "blob-a"),
        list(path = "b.review.yml", type = "blob", sha = "blob-b")
      )))
    }
    if (grepl("git/blobs$", url) && method == "POST") {
      counter <<- counter + 1L
      return(list(sha = paste0("blob-new-", counter)))
    }
    if (grepl("git/trees$", url) && method == "POST") {
      return(list(sha = "new-tree"))
    }
    if (grepl("git/commits$", url) && method == "POST") {
      return(list(sha = "new-commit"))
    }
    if (grepl("git/refs/heads/review", url) && method == "PATCH") {
      state$commit <- "new-commit"
      return(list(object = list(sha = "new-commit")))
    }
    list(object = list())
  }
  ad <- .fake_adapter(http_fun)
  res <- reviewapp::adapter_write_atomic(
    ad,
    changes = list("a.md" = "updated body", "b.review.yml" = "state: in-review"),
    expected_ref_sha = "commit-1",
    expected_blob_shas = list("a.md" = "blob-a", "b.review.yml" = "blob-b"),
    message = "save draft"
  )
  expect_true(res$ok)
  expect_identical(res$commit_sha, "new-commit")
  expect_identical(state$commit, "new-commit")
})

test_that("stale write (touched blob SHA changed since load) is rejected without overwrite", {
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-1"
  state$blobs <- list("a.md" = "blob-a-CHANGED")
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      return(list(tree = list(
        list(path = "a.md", type = "blob", sha = state$blobs[["a.md"]]),
        list(path = "b.review.yml", type = "blob", sha = "blob-b")
      )))
    }
    list(object = list())
  }
  ad <- .fake_adapter(http_fun)
  expect_error(
    reviewapp::adapter_write_atomic(
      ad,
      changes = list("a.md" = "edit"),
      expected_ref_sha = "commit-1",
      expected_blob_shas = list("a.md" = "blob-a-OLD"),
      message = "m"
    ),
    "stale, please reload"
  )
  expect_identical(state$commit, "commit-1")
})

test_that("stale write where only the branch ref moved (unrelated file) is also rejected", {
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-2"
  state$blobs <- list("a.md" = "blob-a")
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      return(list(tree = list(list(path = "a.md", type = "blob", sha = state$blobs[["a.md"]]))))
    }
    list(object = list())
  }
  ad <- .fake_adapter(http_fun)
  expect_error(
    reviewapp::adapter_write_atomic(
      ad,
      changes = list("a.md" = "edit"),
      expected_ref_sha = "commit-1",
      expected_blob_shas = list("a.md" = "blob-a"),
      message = "m"
    ),
    "stale, please reload"
  )
  expect_identical(state$commit, "commit-2")
})

test_that("concurrent-writer simulation rejects the lost update", {
  # Writer 2 already advanced the branch ref to commit-writer2; writer 1 holds a
  # stale loaded ref (commit-1) and must be rejected -- no lost update.
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-writer2"
  state$blobs <- list("a.md" = "blob-a")
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      return(list(tree = list(list(path = "a.md", type = "blob", sha = state$blobs[["a.md"]]))))
    }
    list(object = list())
  }
  ad <- .fake_adapter(http_fun)
  expect_error(
    reviewapp::adapter_write_atomic(
      ad,
      changes = list("a.md" = "w1"),
      expected_ref_sha = "commit-1",
      expected_blob_shas = list("a.md" = "blob-a"),
      message = "w1"
    ),
    "stale, please reload"
  )
  expect_identical(state$commit, "commit-writer2")
})
