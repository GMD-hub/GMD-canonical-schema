# Step 11 -- role-gated actions + approved-artifact write (R8, R9, R10, R14).

library(testthat)

.build_rec <- function(artifact_id = "VAR-male", state = "draft",
                       source = "extraction/20_drafts/dem/VAR-male.md",
                       assignees = list()) {
  new_review_record(
    artifact_id = artifact_id,
    source_artifact_path = source,
    state = state,
    review_round = 1L,
    assigned_to = assignees,
    current_content_sha256 = hash_body("body"),
    source_commit = "abc123"
  )
}

# A minimal adapter whose http layer honours a happy-path atomic write.
.happy_write_adapter <- function() {
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-1"
  state$blobs <- list(
    "extraction/30_review/VAR-male.review.yml" = "blob-rec",
    "extraction/30_review/VAR-urban.review.yml" = "blob-urban"
  )
  counter <- 0L
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/fixture-review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      entries <- lapply(names(state$blobs), function(p) list(path = p, type = "blob", sha = state$blobs[[p]]))
      return(list(tree = entries, truncated = FALSE))
    }
    if (grepl("git/blobs$", url) && method == "POST") {
      counter <<- counter + 1L
      return(list(sha = paste0("blob-new-", counter)))
    }
    if (grepl("git/trees$", url) && method == "POST") return(list(sha = "new-tree"))
    if (grepl("git/commits$", url) && method == "POST") return(list(sha = "new-commit"))
    if (grepl("git/refs/heads/fixture-review", url) && method == "PATCH") {
      state$commit <- "new-commit"
      return(list(object = list(sha = "new-commit")))
    }
    list(object = list())
  }
  reviewapp::new_github_adapter(
    owner = "GMD-hub", repo = "fixture-repo",
    default_branch = "main", review_branch = "fixture-review",
    get_token = function() "tok", http = http_fun
  )
}

test_that("perform_action submits a draft and applies the transition atomically", {
  ad <- .happy_write_adapter()
  rec <- .build_rec()  # draft
  res <- .perform_legacy_test_action(
    ad, rec,
    body_sha256 = rec$current_content_sha256,
    blob_sha = "blob-rec", branch_head_sha = "commit-1",
    action = "submitted", actor = "r@example.org", role = "reviewer"
  )
  expect_true(res$report$ok)
  expect_true(res$report$transition_applied)
  expect_identical(record_state(res$record), "in-review")
  # exactly one new event appended
  expect_length(res$record$events, 1L)
  expect_identical(res$record$events[[1L]]$action, "submitted")
})

test_that("perform_action rejects a role that is not authorized for the action", {
  ad <- .happy_write_adapter()
  rec <- .build_rec()
  expect_error(
    .perform_legacy_test_action(ad, rec, rec$current_content_sha256, "blob-rec", "commit-1",
                   action = "approved", actor = "r@example.org", role = "reviewer"),
    "unauthorized"
  )
})

test_that("approval requires an approver role and writes the approved artifact path (R14)", {
  ad <- .happy_write_adapter()
  rec <- .build_rec(state = "in-review")
  res <- .perform_legacy_test_action(
    ad, rec,
    body_sha256 = rec$current_content_sha256,
    blob_sha = "blob-rec", branch_head_sha = "commit-1",
    action = "approved", actor = "a@example.org", role = "approver",
    approved_content = "---\nartifact_id: VAR-male\n---\nApproved body."
  )
  expect_true(res$report$ok)
  expect_true(res$report$transition_applied)
  expect_identical(record_state(res$record), "approved")
  # approved_path_for mirrors R14
  expect_identical(
    approved_path_for("extraction/20_drafts/dem/VAR-male.md"),
    "extraction/40_approved/dem/VAR-male.md"
  )
})

test_that("approve without approved_content fails loudly", {
  ad <- .happy_write_adapter()
  rec <- .build_rec(state = "in-review")
  expect_error(
    .perform_legacy_test_action(ad, rec, rec$current_content_sha256, "blob-rec", "commit-1",
                   action = "approved", actor = "a@example.org", role = "approver"),
    "requires approved_content"
  )
})

test_that("request-revision moves in-review to needs-revision (approver)", {
  ad <- .happy_write_adapter()
  rec <- .build_rec(state = "in-review")
  res <- .perform_legacy_test_action(
    ad, rec, rec$current_content_sha256, "blob-rec", "commit-1",
    action = "request-revision", actor = "a@example.org", role = "approver",
    note = "please fix"
  )
  expect_true(res$report$transition_applied)
  expect_identical(record_state(res$record), "needs-revision")
  expect_identical(res$record$events[[1L]]$note, "please fix")
})

test_that("a stale write on an action is reported without claiming a transition", {
  # branch head moved since load -> stale
  state <- new.env(parent = emptyenv())
  state$commit <- "moved-commit"
  state$blobs <- list("extraction/30_review/VAR-male.review.yml" = "blob-rec")
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/fixture-review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    list(object = list())
  }
  ad <- reviewapp::new_github_adapter(
    owner = "GMD-hub", repo = "fixture-repo",
    default_branch = "main", review_branch = "fixture-review",
    get_token = function() "tok", http = http_fun
  )
  rec <- .build_rec()
  res <- .perform_legacy_test_action(
    ad, rec, rec$current_content_sha256, "blob-rec", branch_head_sha = "OLD-HEAD",
    action = "submitted", actor = "r@example.org", role = "reviewer"
  )
  expect_false(res$report$ok)
  expect_false(res$report$transition_applied)
  expect_match(recovery_report_text(res$report), "Stale write rejected")
})

test_that("reopen is administrator-only and emits an explicit event", {
  ad <- .happy_write_adapter()
  rec <- .build_rec(state = "approved")
  # reviewer cannot reopen
  expect_error(
    .perform_legacy_test_action(ad, rec, rec$current_content_sha256, "blob-rec", "commit-1",
                   action = "reopened", actor = "r@example.org", role = "reviewer"),
    "unauthorized"
  )
  res <- .perform_legacy_test_action(
    ad, rec, rec$current_content_sha256, "blob-rec", "commit-1",
    action = "reopened", actor = "admin@example.org", role = "administrator"
  )
  expect_true(res$report$transition_applied)
  expect_identical(record_state(res$record), "needs-revision")
  expect_identical(res$record$events[[1L]]$action, "reopened")
})

test_that("reopen persists the administrator reason", {
  ad <- .happy_write_adapter()
  rec <- .build_rec(state = "approved")
  res <- .perform_legacy_test_action(
    ad, rec, rec$current_content_sha256, "blob-rec", "commit-1",
    action = "reopened", actor = "admin@example.org", role = "administrator",
    note = "The approved artifact needs a source correction."
  )
  expect_identical(
    res$record$events[[1L]]$note,
    "The approved artifact needs a source correction."
  )
})

test_that("saved maps to reviewer in the action-role map (P1.1)", {
  # Step 2 adds saved = "reviewer" so Step 4's fail-closed change does not
  # reject save_draft for the reviewer who performs it.
  expect_identical(action_requires_role[["saved"]], "reviewer")
  expect_true(authorize("reviewer", "saved"))
  expect_false(authorize("approver", "saved"))
  expect_false(authorize(NULL, "saved"))
})

test_that("perform_action('saved') persists a companion body file and appends a saved event (P1.2)", {
  ad <- .happy_write_adapter()
  rec <- .build_rec()  # draft
  # a happy adapter whose blob map seeds the review record path
  state <- new.env(parent = emptyenv())
  state$commit <- "commit-1"
  state$blobs <- list(
    "extraction/30_review/VAR-male.review.yml" = "blob-rec"
  )
  counter <- 0L
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/fixture-review", url) && method == "GET") {
      return(list(object = list(sha = state$commit)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      entries <- lapply(names(state$blobs), function(p) list(path = p, type = "blob", sha = state$blobs[[p]]))
      return(list(tree = entries, truncated = FALSE))
    }
    if (grepl("git/blobs$", url) && method == "POST") {
      counter <<- counter + 1L
      return(list(sha = paste0("blob-new-", counter)))
    }
    if (grepl("git/trees$", url) && method == "POST") return(list(sha = "new-tree"))
    if (grepl("git/commits$", url) && method == "POST") return(list(sha = "new-commit"))
    if (grepl("git/refs/heads/fixture-review", url) && method == "PATCH") {
      state$commit <- "new-commit"
      return(list(object = list(sha = "new-commit")))
    }
    list(object = list())
  }
  ad2 <- reviewapp::new_github_adapter(
    owner = "GMD-hub", repo = "fixture-repo",
    default_branch = "main", review_branch = "fixture-review",
    get_token = function() "tok", http = http_fun
  )

  res <- .perform_legacy_test_action(
    ad2, rec,
    body_sha256 = hash_body("edited body"),
    blob_sha = "blob-rec", branch_head_sha = "commit-1",
    action = "saved", actor = "r@example.org", role = "reviewer",
    body = "edited body"
  )
  expect_true(res$report$ok)
  expect_true(res$report$transition_applied)
  # no state transition occurs
  expect_identical(record_state(res$record), "draft")
  # a saved event is appended
  expect_identical(res$record$events[[1L]]$action, "saved")
})

test_that("perform_action('assigned') appends an assigned event without a transition", {
  ad <- .happy_write_adapter()
  rec <- .build_rec()
  res <- .perform_legacy_test_action(
    ad, rec,
    body_sha256 = rec$current_content_sha256,
    blob_sha = "blob-rec", branch_head_sha = "commit-1",
    action = "assigned", actor = "admin@example.org", role = "administrator"
  )
  expect_true(res$report$transition_applied)
  expect_identical(record_state(res$record), "draft")
  expect_identical(res$record$events[[1L]]$action, "assigned")
})
