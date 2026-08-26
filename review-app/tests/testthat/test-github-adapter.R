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

# --- Step 1 (Phase 1): production write transport + Connect entry point ------

test_that("gh_adapter_http sends a JSON request body on POST/PATCH (R1)", {
  # Inject a mock of httr2 so no network is touched. The transport must attach
  # the body via req_body_json before performing the request.
  captured <- NULL
  mock_req <- structure(list(), class = "httr2_request")
  local_mocked_bindings(
    request = function(url, ...) mock_req,
    req_method = function(req, method, ...) req,
    req_headers = function(req, ...) req,
    req_timeout = function(req, ...) req,
    req_retry = function(req, ...) req,
    req_error = function(req, ...) req,
    req_body_json = function(req, data, ...) {
      captured <<- list(url = url_hold, data = data)
      req
    },
    req_perform = function(req, ...) structure(list(), class = "httr2_response"),
    resp_body_string = function(resp, ...) "{}",
    .package = "httr2"
  )
  url_hold <- "https://api.github.com/repos/o/r/git/blobs"
  reviewapp::gh_adapter_http("POST", url_hold, "ghu_token", body = list(content = "x"))
  expect_false(is.null(captured))
  expect_identical(captured$url, url_hold)
  expect_identical(captured$data$content, "x")
})

test_that("gh_adapter_http accepts a NULL body for GET without a request body", {
  mock_req <- structure(list(), class = "httr2_request")
  body_attached <- FALSE
  local_mocked_bindings(
    request = function(url, ...) mock_req,
    req_method = function(req, method, ...) req,
    req_headers = function(req, ...) req,
    req_timeout = function(req, ...) req,
    req_retry = function(req, ...) req,
    req_error = function(req, ...) req,
    req_body_json = function(req, data, ...) {
      body_attached <<- TRUE
      req
    },
    req_perform = function(req, ...) structure(list(), class = "httr2_response"),
    resp_body_string = function(resp, ...) "{}",
    .package = "httr2"
  )
  url_hold <- "https://api.github.com/repos/o/r/git/ref/heads/main"
  reviewapp::gh_adapter_http("GET", url_hold, "ghu_token")
  expect_false(body_attached)
})

test_that("Connect entry point resolves an exported shiny_review_app (R2)", {
  # app.R:9 calls reviewapp::shiny_review_app(); it must be in the NAMESPACE
  expect_true(
    "shiny_review_app" %in% getNamespaceExports("reviewapp"),
    info = "shiny_review_app must be exported (app.R:9 calls it with ::)"
  )
  entry <- getFromNamespace("shiny_review_app", "reviewapp")
  expect_type(entry, "closure")
  # the exported run_review_app is also present and both produce a shinyApp
  run <- getFromNamespace("run_review_app", "reviewapp")
  expect_type(run, "closure")
})

# --- Step 1/2 (Phase 1): adapter factory (R3) ---------------------------------

test_that("review_app_adapter() returns NULL in REVIEW_APP_OFFLINE mode", {
  withr::local_envvar(REVIEW_APP_OFFLINE = "1")
  expect_null(reviewapp::review_app_adapter())
})

test_that("review_app_adapter() uses an injected adapter via options", {
  fake <- structure(list(), class = "reviewapp_github_adapter")
  op <- getOption("reviewapp.adapter")
  options(reviewapp.adapter = fake)
  on.exit(options(reviewapp.adapter = op), add = TRUE)
  expect_identical(reviewapp::review_app_adapter(), fake)
})

test_that("review_app_adapter() fails loudly when required secrets are missing", {
  withr::local_envvar(
    REVIEW_APP_OFFLINE = "",
    REVIEW_APP_GH_OWNER = "",
    REVIEW_APP_GH_REPO = "",
    REVIEW_APP_GH_DEFAULT_BRANCH = "",
    REVIEW_APP_GH_REVIEW_BRANCH = "",
    REVIEW_APP_EXPECTED_SOURCE_COMMIT = paste(rep("a", 40L), collapse = ""),
    GITHUB_APP_ID = "",
    GITHUB_APP_INSTALLATION_ID = "",
    GITHUB_APP_PRIVATE_KEY = ""
  )
  op <- getOption("reviewapp.adapter")
  options(reviewapp.adapter = NULL)
  on.exit(options(reviewapp.adapter = op), add = TRUE)
  expect_error(reviewapp::review_app_adapter(), "adapter not configured")
})

test_that("review_app_adapter() builds a live adapter when secrets are present", {
  withr::local_envvar(
    REVIEW_APP_OFFLINE = "",
    REVIEW_APP_GH_OWNER = "GMD-hub",
    REVIEW_APP_GH_REPO = "fixture-repo",
    REVIEW_APP_GH_DEFAULT_BRANCH = "main",
    REVIEW_APP_GH_REVIEW_BRANCH = "review",
    REVIEW_APP_EXPECTED_SOURCE_COMMIT = paste(rep("a", 40L), collapse = ""),
    GITHUB_APP_ID = "123",
    GITHUB_APP_INSTALLATION_ID = "999",
    GITHUB_APP_PRIVATE_KEY = "not-a-real-key"
  )
  op <- getOption("reviewapp.adapter")
  options(reviewapp.adapter = NULL)
  on.exit(options(reviewapp.adapter = op), add = TRUE)
  ad <- reviewapp::review_app_adapter()
  expect_s3_class(ad, "reviewapp_github_adapter")
  expect_identical(ad$owner, "GMD-hub")
  expect_identical(ad$review_branch, "review")
  expect_identical(
    ad$expected_source_commit,
    paste(rep("a", 40L), collapse = "")
  )
})

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
