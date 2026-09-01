# Step 7 -- partial-failure detection and operator recovery (R18).
#
# If a multi-step Git operation fails partway, the recovery surface reports
# exactly which steps succeeded/failed and never marks the review-record
# transition as applied unless the full atomic operation completed.

.fake_recovery_adapter <- function(http_fun) {
  reviewapp::new_github_adapter(
    owner = "GMD-hub", repo = "fixture-repo",
    default_branch = "main", review_branch = "fixture-review",
    get_token = function() "ghu_testtoken",
    http = http_fun
  )
}

# happy path through the recovery wrapper
test_that("recovery wrapper reports success and applies the transition on a full atomic write", {
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-1"
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/fixture-review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      return(list(tree = list(list(path = "a.md", type = "blob", sha = "blob-a"))))
    }
    if (grepl("git/blobs$", url) && method == "POST") return(list(sha = "nb1"))
    if (grepl("git/trees$", url) && method == "POST") return(list(sha = "tree1"))
    if (grepl("git/commits$", url) && method == "POST") return(list(sha = "c1"))
    if (grepl("git/refs/heads/fixture-review", url) && method == "PATCH") {
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
    if (grepl("git/ref/heads/fixture-review", url) && method == "GET") {
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
    if (grepl("git/ref/heads/fixture-review", url) && method == "GET") {
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

test_that("atomic writes support forward-only control-file deletion", {
  captured_tree <- NULL
  captured_ref <- NULL
  head <- paste(rep("a", 40L), collapse = "")
  http_fun <- function(method, url, token, body = NULL) {
    if (identical(method, "GET") && grepl("git/ref/heads/fixture-review", url)) {
      return(list(object = list(sha = head)))
    }
    if (identical(method, "GET") && grepl("git/trees/", url)) {
      return(list(
        tree = list(
          list(
            path = LEGACY_QUEUE_MANIFEST_PATH,
            type = "blob",
            sha = paste(rep("b", 40L), collapse = "")
          ),
          list(
            path = LEGACY_QUEUE_INDEX_PATH,
            type = "blob",
            sha = paste(rep("c", 40L), collapse = "")
          )
        ),
        sha = paste(rep("d", 40L), collapse = ""),
        truncated = FALSE
      ))
    }
    if (identical(method, "POST") && grepl("git/blobs$", url)) {
      return(list(sha = paste(rep("e", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/trees$", url)) {
      captured_tree <<- body
      return(list(sha = paste(rep("f", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/commits$", url)) {
      return(list(sha = paste(rep("1", 40L), collapse = "")))
    }
    if (identical(method, "PATCH")) {
      captured_ref <<- body
      return(list(object = list(sha = body$sha)))
    }
    stop("unexpected request")
  }
  adapter <- .fake_recovery_adapter(http_fun)
  changes <- list()
  changes[QUEUE_DESCRIPTOR_PATH] <- list("schema_version: '1.0'\n")
  changes[LEGACY_QUEUE_MANIFEST_PATH] <- list(NULL)
  changes[LEGACY_QUEUE_INDEX_PATH] <- list(NULL)
  result <- adapter_write_atomic(
    adapter,
    changes = changes,
    expected_ref_sha = head,
    message = "migrate queue"
  )
  entries <- stats::setNames(captured_tree$tree, vapply(
    captured_tree$tree,
    function(entry) entry$path,
    character(1)
  ))
  expect_null(entries[[LEGACY_QUEUE_MANIFEST_PATH]]$sha)
  expect_null(entries[[LEGACY_QUEUE_INDEX_PATH]]$sha)
  expect_identical(captured_ref$force, FALSE)
  expect_identical(result$commit_sha, paste(rep("1", 40L), collapse = ""))
})

test_that("pre-publication source failure leaves the new commit unreachable", {
  head <- paste(rep("a", 40L), collapse = "")
  calls <- character()
  http_fun <- function(method, url, token, body = NULL) {
    calls <<- c(calls, paste(method, url))
    if (identical(method, "GET") && grepl("git/ref/heads/", url)) {
      return(list(object = list(sha = head)))
    }
    if (identical(method, "GET") && grepl("git/trees/", url)) {
      return(list(
        tree = list(list(path = "a.md", type = "blob", sha = .sha1_fixture)),
        sha = .sha1_fixture_2,
        truncated = FALSE
      ))
    }
    if (identical(method, "POST") && grepl("git/blobs$", url)) {
      return(list(sha = paste(rep("c", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/trees$", url)) {
      return(list(sha = paste(rep("d", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/commits$", url)) {
      return(list(sha = paste(rep("e", 40L), collapse = "")))
    }
    if (identical(method, "PATCH")) stop("ref update must not occur")
    stop("unexpected request")
  }
  adapter <- .fake_recovery_adapter(http_fun)
  report <- adapter_write_with_recovery(
    adapter,
    changes = list("a.md" = "changed"),
    expected_ref_sha = head,
    expected_blob_shas = list("a.md" = .sha1_fixture),
    message = "source-sensitive write",
    pre_publish_check = function() {
      stop(source_drift_error("selected source path changed"))
    }
  )
  expect_false(report$ok)
  expect_identical(report$error$kind, "source-drift")
  expect_false(report$transition_applied)
  expect_true("commit-creation" %in% report$steps_completed)
  expect_false(any(grepl("^PATCH ", calls)))
  expect_identical(head, paste(rep("a", 40L), collapse = ""))
})

test_that("pre-publication check runs between commit creation and ref update", {
  head <- paste(rep("a", 40L), collapse = "")
  order <- character()
  http_fun <- function(method, url, token, body = NULL) {
    if (identical(method, "GET") && grepl("git/ref/heads/", url)) {
      return(list(object = list(sha = head)))
    }
    if (identical(method, "GET") && grepl("git/trees/", url)) {
      return(list(
        tree = list(list(path = "a.md", type = "blob", sha = .sha1_fixture)),
        sha = .sha1_fixture_2,
        truncated = FALSE
      ))
    }
    if (identical(method, "POST") && grepl("git/blobs$", url)) {
      return(list(sha = paste(rep("c", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/trees$", url)) {
      return(list(sha = paste(rep("d", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/commits$", url)) {
      order <<- c(order, "commit")
      return(list(sha = paste(rep("e", 40L), collapse = "")))
    }
    if (identical(method, "PATCH")) {
      order <<- c(order, "patch")
      return(list(object = list(sha = body$sha)))
    }
    stop("unexpected request")
  }
  result <- adapter_write_atomic(
    .fake_recovery_adapter(http_fun),
    changes = list("a.md" = "changed"),
    expected_ref_sha = head,
    expected_blob_shas = list("a.md" = .sha1_fixture),
    message = "ordered source check",
    pre_publish_check = function() {
      order <<- c(order, "check")
      invisible(TRUE)
    }
  )
  expect_identical(order, c("commit", "check", "patch"))
  expect_true("pre-publication-check" %in% result$steps_completed)
})

test_that("approved-output deletion emits a Git tree sha NULL entry", {
  captured_tree <- NULL
  approved_path <- "extraction/40_approved/dem/VAR-male.md"
  head <- paste(rep("a", 40L), collapse = "")
  approved_sha <- paste(rep("b", 40L), collapse = "")
  http_fun <- function(method, url, token, body = NULL) {
    if (identical(method, "GET") && grepl("git/ref/heads/", url)) {
      return(list(object = list(sha = head)))
    }
    if (identical(method, "GET") && grepl("git/trees/", url)) {
      return(list(
        tree = list(list(path = approved_path, type = "blob", sha = approved_sha)),
        sha = .sha1_fixture,
        truncated = FALSE
      ))
    }
    if (identical(method, "POST") && grepl("git/trees$", url)) {
      captured_tree <<- body
      return(list(sha = .sha1_fixture_2))
    }
    if (identical(method, "POST") && grepl("git/commits$", url)) {
      return(list(sha = paste(rep("c", 40L), collapse = "")))
    }
    if (identical(method, "PATCH")) {
      return(list(object = list(sha = body$sha)))
    }
    stop("unexpected request")
  }
  adapter <- .fake_recovery_adapter(http_fun)
  changes <- list()
  changes[approved_path] <- list(NULL)
  adapter_write_atomic(
    adapter,
    changes = changes,
    expected_ref_sha = head,
    expected_blob_shas = stats::setNames(list(approved_sha), approved_path),
    message = "retire approved output"
  )
  entry <- captured_tree$tree[[1L]]
  expect_identical(entry$path, approved_path)
  expect_true("sha" %in% names(entry))
  expect_null(entry$sha)
})

test_that("absent destination locks reject trees and descendants", {
  destination <- "extraction/40_approved/dem/VAR-male.md"
  head <- paste(rep("a", 40L), collapse = "")
  tree_sha <- paste(rep("b", 40L), collapse = "")
  for (entries in list(
    list(list(
      path = destination,
      type = "tree",
      sha = paste(rep("c", 40L), collapse = "")
    )),
    list(list(
      path = paste0(destination, "/keep.txt"),
      type = "blob",
      sha = paste(rep("d", 40L), collapse = "")
    ))
  )) {
    http_fun <- function(method, url, token, body = NULL) {
      if (identical(method, "GET") && grepl("git/ref/heads/", url)) {
        return(list(object = list(sha = head)))
      }
      if (identical(method, "GET") && grepl("/git/trees/", url)) {
        return(list(sha = tree_sha, truncated = FALSE, tree = entries))
      }
      stop("unexpected request")
    }
    expect_error(
      adapter_check_stale(
        .fake_recovery_adapter(http_fun),
        expected_blob_shas = stats::setNames(
          list(NA_character_),
          destination
        )
      ),
      "is no longer absent"
    )
  }
})

test_that("a lost PATCH response is reconciled when the ref moved", {
  old_head <- paste(rep("a", 40L), collapse = "")
  new_commit <- paste(rep("e", 40L), collapse = "")
  state <- new.env(parent = emptyenv())
  state$head <- old_head
  http_fun <- function(method, url, token, body = NULL) {
    if (identical(method, "GET") && grepl("git/ref/heads/", url)) {
      return(list(object = list(sha = state$head)))
    }
    if (identical(method, "GET") && grepl("git/trees/", url)) {
      return(list(
        tree = list(list(path = "a.md", type = "blob", sha = .sha1_fixture)),
        sha = .sha1_fixture_2,
        truncated = FALSE
      ))
    }
    if (identical(method, "POST") && grepl("git/blobs$", url)) {
      return(list(sha = paste(rep("c", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/trees$", url)) {
      return(list(sha = paste(rep("d", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/commits$", url)) {
      return(list(sha = new_commit))
    }
    if (identical(method, "PATCH")) {
      state$head <- body$sha
      stop("connection reset after ref update")
    }
    stop("unexpected request")
  }
  report <- adapter_write_with_recovery(
    .fake_recovery_adapter(http_fun),
    changes = list("a.md" = "changed"),
    expected_ref_sha = old_head,
    expected_blob_shas = list("a.md" = .sha1_fixture),
    message = "reconcile applied ref"
  )
  expect_true(report$ok)
  expect_true(report$transition_applied)
  expect_identical(report$commit_sha, new_commit)
  expect_identical(state$head, new_commit)
})

test_that("an unreconciled PATCH response is reported as indeterminate", {
  old_head <- paste(rep("a", 40L), collapse = "")
  new_commit <- paste(rep("e", 40L), collapse = "")
  concurrent_head <- paste(rep("f", 40L), collapse = "")
  state <- new.env(parent = emptyenv())
  state$head <- old_head
  http_fun <- function(method, url, token, body = NULL) {
    if (identical(method, "GET") && grepl("git/ref/heads/", url)) {
      return(list(object = list(sha = state$head)))
    }
    if (identical(method, "GET") && grepl("git/trees/", url)) {
      return(list(
        tree = list(list(path = "a.md", type = "blob", sha = .sha1_fixture)),
        sha = .sha1_fixture_2,
        truncated = FALSE
      ))
    }
    if (identical(method, "POST") && grepl("git/blobs$", url)) {
      return(list(sha = paste(rep("c", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/trees$", url)) {
      return(list(sha = paste(rep("d", 40L), collapse = "")))
    }
    if (identical(method, "POST") && grepl("git/commits$", url)) {
      return(list(sha = new_commit))
    }
    if (identical(method, "PATCH")) {
      state$head <- concurrent_head
      stop("connection reset with concurrent publication")
    }
    stop("unexpected request")
  }
  report <- adapter_write_with_recovery(
    .fake_recovery_adapter(http_fun),
    changes = list("a.md" = "changed"),
    expected_ref_sha = old_head,
    expected_blob_shas = list("a.md" = .sha1_fixture),
    message = "indeterminate ref"
  )
  expect_false(report$ok)
  expect_true(is.na(report$transition_applied))
  expect_identical(report$error$kind, "indeterminate")
  expect_identical(report$commit_sha, new_commit)
  expect_match(recovery_report_text(report), "Do not retry")
})

test_that("no-op reports have explicit recovery text", {
  expect_match(recovery_report_text(.no_op_report()), "No write was needed")
})
