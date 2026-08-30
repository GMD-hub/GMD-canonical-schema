test_that("production and legacy branch contracts coexist", {
  expect_identical(PRODUCTION_REVIEW_BRANCH, "review-production")
  expect_true(production_branch_name(list(review_branch = "review-production")))
  expect_false(production_branch_name(list(review_branch = "review")))
  expect_false(production_branch_name(list(review_branch = "review/production")))
})

test_that("expected source commit is required and validated", {
  withr::local_envvar(REVIEW_APP_EXPECTED_SOURCE_COMMIT = NA_character_)
  expect_error(expected_source_commit(), "REVIEW_APP_EXPECTED_SOURCE_COMMIT")

  withr::local_envvar(REVIEW_APP_EXPECTED_SOURCE_COMMIT = "ABC")
  expect_error(expected_source_commit(), "lowercase Git SHA-1")

  sha <- paste(rep("a", 40L), collapse = "")
  withr::local_envvar(REVIEW_APP_EXPECTED_SOURCE_COMMIT = sha)
  expect_identical(expected_source_commit(), sha)
})

test_that("production index performs four reads and no record reads", {
  modules <- rep(names(QUEUE_EXPECTED_MODULE_COUNTS), QUEUE_EXPECTED_MODULE_COUNTS)
  source_paths <- vapply(seq_len(QUEUE_EXPECTED_TOTAL), function(i) {
    sprintf("extraction/20_drafts/%s/VAR-fixture%03d.md", modules[[i]], i)
  }, character(1))
  manifest <- new_queue_manifest(
    created_at = "2026-08-24T13:25:07Z",
    created_by = "admin@example.org",
    source_commit = paste(rep("a", 40L), collapse = ""),
    expected_path_set_sha256 = queue_path_set_digest(source_paths)
  )
  rows <- lapply(seq_len(QUEUE_EXPECTED_TOTAL), function(i) {
    module <- modules[[i]]
    new_queue_index_row(
      artifact_id = sprintf("VAR-fixture%03d", i),
      module = module,
      source_artifact_path = source_paths[[i]],
      record_blob_sha = paste(rep(sprintf("%x", i %% 16L), 40L), collapse = ""),
      governance_blocked = TRUE,
      source_drift = FALSE
    )
  })
  index <- new_queue_index(QUEUE_ID, rows, manifest)
  manifest_raw <- charToRaw(canonical_yaml(manifest))
  index_raw <- charToRaw(serialize_queue_index(index))
  manifest_sha <- git_blob_sha_raw(manifest_raw)
  index_sha <- git_blob_sha_raw(index_raw)
  calls <- character()
  http <- function(method, url, token, body = NULL) {
    calls <<- c(calls, url)
    if (grepl("git/ref/heads/", url)) {
      return(list(object = list(sha = paste(rep("d", 40L), collapse = ""))))
    }
    if (grepl("git/trees/", url)) {
      return(list(tree = list(
        list(path = QUEUE_MANIFEST_PATH, type = "blob", sha = manifest_sha),
        list(path = QUEUE_INDEX_PATH, type = "blob", sha = index_sha)
      ), truncated = FALSE))
    }
    raw <- if (grepl(manifest_sha, url, fixed = TRUE)) manifest_raw else index_raw
    list(
      sha = if (identical(raw, manifest_raw)) manifest_sha else index_sha,
      encoding = "base64",
      content = base64enc::base64encode(raw)
    )
  }
  telemetry <- new_repository_read_telemetry()
  adapter <- new_github_adapter(
    "GMD-hub", "fixture", "main", PRODUCTION_REVIEW_BRANCH,
    get_token = function() "secret", http = http, telemetry = telemetry,
    expected_source_commit = paste(rep("a", 40L), collapse = "")
  )

  result <- adapter_index_review(adapter)

  expect_identical(result$mode, "production")
  expect_identical(result$request_telemetry$logical_reads, 4L)
  expect_identical(result$request_telemetry$actual_attempts, 4L)
  expect_identical(result$request_telemetry$per_record_reads, 0L)
  expect_gte(result$request_telemetry$duration_ms, 0L)
  expect_length(calls, 4L)
})

test_that("session telemetry does not share mutable counters", {
  adapter <- new_github_adapter(
    "GMD-hub", "fixture", "main", PRODUCTION_REVIEW_BRANCH,
    get_token = function() "secret",
    http = function(method, url, token, body = NULL) list(),
    telemetry = new_repository_read_telemetry()
  )
  first <- repository_telemetry_operation(adapter)
  second <- repository_telemetry_operation(adapter)
  first$adapter$http("GET", "https://api.github.com/repos/o/r/git/trees/a", "secret")
  expect_identical(first$snapshot()$logical_reads, 1L)
  expect_identical(second$snapshot()$logical_reads, 0L)
})

test_that("malformed production manifest returns a controlled queue error", {
  manifest_raw <- charToRaw("not: [valid")
  manifest_sha <- git_blob_sha_raw(manifest_raw)
  http <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/", url)) {
      return(list(object = list(sha = paste(rep("d", 40L), collapse = ""))))
    }
    if (grepl("git/trees/", url)) {
      return(list(tree = list(list(
        path = QUEUE_MANIFEST_PATH, type = "blob", sha = manifest_sha
      )), truncated = FALSE))
    }
    list(
      sha = manifest_sha, encoding = "base64",
      content = base64enc::base64encode(manifest_raw)
    )
  }
  adapter <- new_github_adapter(
    "GMD-hub", "fixture", "main", PRODUCTION_REVIEW_BRANCH,
    get_token = function() "secret", http = http
  )
  result <- adapter_index_review(adapter)
  expect_identical(result$mode, "queue_error")
  expect_equal(nrow(result$index), 0L)
  expect_match(result$error, "production queue is invalid")
})

test_that("bootstrap source mismatch aborts before any write", {
  wrote <- FALSE
  heads <- c(paste(rep("d", 40L), collapse = ""))
  local_mocked_bindings(
    adapter_branch_head = function(...) heads[[1L]],
    adapter_fetch_tree_at = function(...) list(blobs = list()),
    adapter_write_with_recovery = function(...) {
      wrote <<- TRUE
      stop("unexpected write")
    },
    .package = "reviewapp"
  )
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    review_branch = PRODUCTION_REVIEW_BRANCH,
    get_token = function() "secret", http = function(...) list()
  )
  expect_error(
    bootstrap_production_queue(
      adapter, "admin@example.org", "administrator",
      expected_source_commit = paste(rep("a", 40L), collapse = "")
    ),
    "does not match"
  )
  expect_false(wrote)
})

test_that("bootstrap rejects source movement before writing", {
  expected <- paste(rep("a", 40L), collapse = "")
  heads <- c(paste(rep("b", 40L), collapse = ""), expected,
             paste(rep("c", 40L), collapse = ""))
  calls <- 0L
  wrote <- FALSE
  local_mocked_bindings(
    adapter_branch_head = function(...) {
      calls <<- calls + 1L
      heads[[calls]]
    },
    adapter_fetch_tree_at = function(...) list(blobs = list()),
    release_a_draft_paths = function(...) "extraction/20_drafts/dem/VAR-male.md",
    adapter_fetch_blobs_graphql = function(...) list(),
    generate_production_enrollment = function(...) list(
      payload_bytes = 1L, changes = list()
    ),
    adapter_write_with_recovery = function(...) {
      wrote <<- TRUE
      list(ok = TRUE)
    },
    .package = "reviewapp"
  )
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    review_branch = PRODUCTION_REVIEW_BRANCH,
    get_token = function() "secret", http = function(...) list()
  )
  expect_error(
    bootstrap_production_queue(
      adapter, "admin@example.org", "administrator",
      expected_source_commit = expected
    ),
    "moved"
  )
  expect_false(wrote)
})

test_that("bootstrap reports failed publication and returns successful evidence", {
  expected <- paste(rep("a", 40L), collapse = "")
  review_head <- paste(rep("b", 40L), collapse = "")
  publish_ok <- FALSE
  local_mocked_bindings(
    adapter_branch_head = local({
      calls <- 0L
      function(...) {
        calls <<- calls + 1L
        c(review_head, expected, expected)[[(calls - 1L) %% 3L + 1L]]
      }
    }),
    adapter_fetch_tree_at = function(...) list(blobs = list()),
    release_a_draft_paths = function(...) "extraction/20_drafts/dem/VAR-male.md",
    adapter_fetch_blobs_graphql = function(...) list(),
    generate_production_enrollment = function(...) list(
      payload_bytes = 1L, changes = list("record" = "body"),
      manifest = list(queue_id = QUEUE_ID), index = list(rows = list()),
      records = list(one = list())
    ),
    adapter_write_with_recovery = function(...) {
      if (publish_ok) list(ok = TRUE, commit_sha = expected) else list(
        ok = FALSE, recovery = list(status = "not_published")
      )
    },
    recovery_report_text = function(...) "not published",
    .package = "reviewapp"
  )
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    review_branch = PRODUCTION_REVIEW_BRANCH,
    get_token = function() "secret", http = function(...) list()
  )
  expect_error(
    bootstrap_production_queue(
      adapter, "admin@example.org", "administrator",
      expected_source_commit = expected
    ),
    "not published"
  )
  publish_ok <- TRUE
  result <- bootstrap_production_queue(
    adapter, "admin@example.org", "administrator",
    expected_source_commit = expected
  )
  expect_true(result$ok)
  expect_identical(result$commit_sha, expected)
  expect_identical(result$record_count, 1L)
})
