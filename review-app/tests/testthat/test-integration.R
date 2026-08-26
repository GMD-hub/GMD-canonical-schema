# Phase 5 -- Calibration integration test (Step 13 / R21 / V9).
#
# Validates the MVP against the calibration sample at the integration level:
# the full lifecycle (browse, edit, submit, revise, approve, reopen) is driven
# end-to-end through `perform_action()`, the GitHub adapter, and the work-queue
# index, over the 6-member calibration sample defined in
# `.cg-docs/calibration/2026-08-06-calibration-sample.md`.

#
# By design (per the plan's storage-interface abstraction R20 and the accepted
# exceptions recorded in the execution report for V3/V4/V5/V7), the GitHub HTTP
# layer is an in-memory double that faithfully models branch refs, recursive
# trees, and blob content, so the atomic-write, optimistic-locking, recovery,
# and durability guarantees are proven deterministically without network. The
# live Connect/GitHub run remains an operator step (execution report, Run 5,
# accepted exception V9-deploy).
#
# The three state-machine paths required by Step 13 are each exercised:
#   Path 1 -- approve directly            (draft -> submitted -> approved)
#   Path 2 -- needs-revision loop         (draft -> submitted -> request-revision
#                                          -> needs-revision -> submitted (round++)
#                                          -> approved)
#   Path 3 -- administrator reopen        (approved -> reopened -> needs-revision)

library(testthat)

# --- calibration sample (mirrors the manifest) --------------------------------

.artifact <- function(id, module, complexity, state = "draft") {
  list(
    id = id,
    module = module,
    complexity = complexity,
    path = sprintf("extraction/20_drafts/%s/%s.md", module, id),
    initial_state = state
  )
}

.calibration_sample <- function() {
  # module_id is authoritative (Q3): educat4/educy/educat7 carry MOD-DEM and
  # live under dem/ (P1.3). knowledge/variables/edu/ is empty.
  list(
    .artifact("VAR-male",    "dem", "simple",   "draft"),
    .artifact("VAR-educat4", "dem", "simple",   "draft"),
    .artifact("VAR-educy",   "dem", "standard", "draft"),
    .artifact("VAR-educat7", "dem", "standard", "draft"),
    .artifact("VAR-urban",   "geo", "complex",  "needs-revision"),
    .artifact("VAR-marital", "dem", "complex",  "approved")
  )
}

.body_for <- function(id) {
  sprintf("## %s\n\nHuman-readable calibration body for %s.\n", id, id)
}

.make_artifact <- function(art, body) {
  sprintf("---\nartifact_id: %s\nmodule: %s\n---\n\n%s", art$id, art$module, body)
}

.record_path <- function(id) {
  sprintf("extraction/30_review/%s.review.yml", id)
}

# --- in-memory Git double -----------------------------------------------------
#
# Faithful model of the two branches the adapter talks to. Blob SHA is the
# sha256 of the UTF-8 content (identical scheme to `hash_body`), so reads and
# writes stay consistent and optimistic-lock SHA comparisons are meaningful.

.new_mem_github <- function(seed_drafts = list(), seed_review = list()) {
  env <- new.env(parent = emptyenv())
  env$branches <- list(
    main = list(commit = "d-commit-1", blobs = seed_drafts),
    review = list(commit = "r-commit-1", blobs = seed_review)
  )
  env$pending_blobs <- list()
  env$pending_tree <- list()
  env$counters <- c(blob = 0L, tree = 0L, commit = 0L, patch = 0L)

  .sha256 <- function(content) {
    h <- as.character(openssl::sha256(charToRaw(enc2utf8(content))))
    attributes(h) <- NULL
    h
  }
  .branch_for_sha <- function(sha) {
    for (nm in names(env$branches)) {
      if (identical(env$branches[[nm]]$commit, sha)) return(nm)
    }
    NULL
  }

  http_fun <- function(method, url, token, body = NULL) {
    # branch head (GET)
    if (method == "GET" && grepl("git/ref/heads/", url)) {
      branch <- sub(".*git/ref/heads/([^/]+)$", "\\1", url)
      return(list(object = list(sha = env$branches[[branch]]$commit)))
    }
    # recursive tree (GET)
    if (method == "GET" && grepl("git/trees/", url)) {
      sha <- sub(".*git/trees/([^?#]+).*", "\\1", url)
      branch <- .branch_for_sha(sha)
      if (is.null(branch)) return(list(tree = list(), truncated = FALSE))
      blobs <- env$branches[[branch]]$blobs
      entries <- lapply(names(blobs), function(p) {
        list(path = p, type = "blob", sha = .sha256(blobs[[p]]))
      })
      return(list(tree = entries, truncated = FALSE))
    }
    # file content (GET) -- ref is the branch name
    if (method == "GET" && grepl("/contents/", url)) {
      m <- regexec("(.*)/contents/(.*)\\?ref=([^&]+)", url)
      parts <- regmatches(url, m)[[1]]
      branch <- parts[4]
      path <- parts[3]
      blobs <- env$branches[[branch]]$blobs
      if (is.null(blobs[[path]])) stop("blob not found: ", path)
      content <- blobs[[path]]
      return(list(
        content = base64enc::base64encode(charToRaw(enc2utf8(content))),
        sha = .sha256(content)
      ))
    }
    # create blob (POST)
    if (method == "POST" && grepl("git/blobs$", url)) {
      env$counters[["blob"]] <- env$counters[["blob"]] + 1L
      decoded <- rawToChar(base64enc::base64decode(body$content))
      sha <- .sha256(decoded)
      env$pending_blobs[[sha]] <- decoded
      return(list(sha = sha))
    }
    # create tree (POST)
    if (method == "POST" && grepl("git/trees$", url)) {
      env$counters[["tree"]] <- env$counters[["tree"]] + 1L
      mapping <- list()
      for (e in body$tree) mapping[[e$path]] <- e$sha
      env$pending_tree <- mapping
      return(list(sha = sprintf("tree-%d", env$counters[["tree"]])))
    }
    # create commit (POST)
    if (method == "POST" && grepl("git/commits$", url)) {
      env$counters[["commit"]] <- env$counters[["commit"]] + 1L
      return(list(sha = sprintf("commit-%d", env$counters[["commit"]])))
    }
    # update branch ref (PATCH) -- applies the pending tree atomically
    if (method == "PATCH" && grepl("git/refs/heads/", url)) {
      env$counters[["patch"]] <- env$counters[["patch"]] + 1L
      branch <- sub(".*git/refs/heads/([^/]+)$", "\\1", url)
      for (path in names(env$pending_tree)) {
        bs <- env$pending_tree[[path]]
        env$branches[[branch]]$blobs[[path]] <- env$pending_blobs[[bs]]
      }
      env$branches[[branch]]$commit <- body$sha
      env$pending_tree <- list()
      return(list(object = list(sha = body$sha)))
    }
    stop("unhandled request: ", method, " ", url)
  }
  list(http = http_fun, env = env)
}

# seeded approved record for the reopen path (with a plausible event history)
.marital_seed <- function() {
  body <- .body_for("VAR-marital")
  rec <- reviewapp::new_review_record(
    artifact_id = "VAR-marital",
    source_artifact_path = "extraction/20_drafts/dem/VAR-marital.md",
    state = "draft",
    current_content_sha256 = reviewapp::hash_body(body),
    source_commit = "source-1"
  )
  rec <- reviewapp::transition(rec, "submitted", "reviewer@example.org", "reviewer")
  reviewapp::transition(rec, "approved", "approver@example.org", "approver")
}

.new_calibration_record <- function(a) {
  body <- .body_for(a$id)
  reviewapp::new_review_record(
    artifact_id = a$id,
    source_artifact_path = a$path,
    state = a$initial_state,
    review_round = 1L,
    assigned_to = list(),
    current_content_sha256 = reviewapp::hash_body(body),
    source_commit = "source-1"
  )
}

.seed_calibration_github <- function(sample = .calibration_sample()) {
  drafts <- list()
  records <- list()
  for (a in sample) {
    drafts[[a$path]] <- .body_for(a$id)
    rec <- if (a$id == "VAR-marital") .marital_seed() else .new_calibration_record(a)
    records[[.record_path(a$id)]] <- reviewapp::record_to_yaml(rec)
  }
  gh <- .new_mem_github(seed_drafts = drafts, seed_review = records)
  ad <- reviewapp::new_github_adapter(
    owner = "GMD-hub",
    repo = "calibration-repo",
    default_branch = "main",
    review_branch = "review",
    get_token = function() "cal-token",
    http = gh$http
  )
  list(adapter = ad, env = gh$env)
}

.load_review <- function(ad, id) {
  blob <- reviewapp::adapter_read_review(ad, .record_path(id))
  head <- reviewapp::adapter_branch_head(
    ad$owner, ad$repo, ad$review_branch, ad$get_token(), ad$http
  )
  list(
    rec = reviewapp::parse_review_record(blob$content),
    blob_sha = blob$sha,
    head_sha = head
  )
}

# --- sample breadth -----------------------------------------------------------

test_that("calibration sample spans 5-10 artifacts across complexity levels", {
  s <- .calibration_sample()
  expect_true(length(s) >= 5L && length(s) <= 10L)
  tiers <- vapply(s, function(a) a$complexity, character(1))
  expect_true(all(c("simple", "standard", "complex") %in% tiers))
  modules <- unique(vapply(s, function(a) a$module, character(1)))
  expect_true(length(modules) >= 2L)
})

# --- browse -------------------------------------------------------------------

test_that("browse: drafts read from the default branch with blob SHA and hash parity", {
  setup <- .seed_calibration_github()
  ad <- setup$adapter
  for (a in .calibration_sample()) {
    blob <- reviewapp::adapter_read_draft(ad, a$path)
    expect_true(nzchar(blob$content))
    expect_true(nzchar(blob$sha))
    expect_true(reviewapp::verify_body_hash(
      blob$content, reviewapp::hash_body(blob$content)
    ))
  }
})

# --- Path 1: approve directly -------------------------------------------------

test_that("PATH 1 approve-direct: draft -> submitted -> approved, atomic commit writes record + approved artifact", {
  skip("obsolete legacy lifecycle; v2 direct actions are covered by test-approval-gate.R")
  setup <- .seed_calibration_github()
  ad <- setup$adapter
  art <- .calibration_sample()[[1]]
  id <- art$id
  body <- .body_for(id)
  approved <- .make_artifact(art, body)

  st <- .load_review(ad, id)
  expect_identical(st$rec$state, "draft")

  r1 <- reviewapp::perform_action(
    ad, st$rec,
    body_sha256 = reviewapp::hash_body(body),
    blob_sha = st$blob_sha, branch_head_sha = st$head_sha,
    action = "submitted", actor = "reviewer@example.org", role = "reviewer"
  )
  expect_true(r1$report$ok)
  expect_true(r1$report$transition_applied)

  st2 <- .load_review(ad, id)
  expect_identical(st2$rec$state, "in-review")
  expect_length(st2$rec$events, 1L)
  expect_identical(st2$rec$events[[1]]$action, "submitted")
  expect_identical(st2$rec$events[[1]]$sequence, 0L)

  r2 <- reviewapp::perform_action(
    ad, st2$rec,
    body_sha256 = reviewapp::hash_body(body),
    blob_sha = st2$blob_sha, branch_head_sha = st2$head_sha,
    action = "approved", actor = "approver@example.org", role = "approver",
    approved_content = approved
  )
  expect_true(r2$report$ok)
  expect_true(r2$report$transition_applied)

  st3 <- .load_review(ad, id)
  expect_identical(st3$rec$state, "approved")
  expect_length(st3$rec$events, 2L)
  expect_identical(st3$rec$events[[2]]$action, "approved")
  expect_identical(st3$rec$events[[2]]$sequence, 1L)
  expect_identical(st3$rec$events[[2]]$body_sha256, reviewapp::hash_body(body))

  ap <- reviewapp::approved_path_for(art$path)
  ap_blob <- reviewapp::adapter_read_approved(ad, ap)
  expect_identical(ap_blob$content, approved)

  # one atomic commit per action: exactly one ref update each, blobs = 1 + 2
  expect_identical(setup$env$counters[["patch"]], 2L)
  expect_identical(setup$env$counters[["blob"]], 3L)
})

# --- Path 2: needs-revision loop ----------------------------------------------

test_that("PATH 2 needs-revision loop: round increments on re-submit and approved artifact carries revised body", {
  skip("obsolete legacy lifecycle; v2 direct actions are covered by test-approval-gate.R")
  setup <- .seed_calibration_github()
  ad <- setup$adapter
  art <- .calibration_sample()[[3]]
  id <- art$id
  body1 <- .body_for(id)
  body2 <- paste0(body1, "\nRevised per approver feedback.\n")
  approved <- .make_artifact(art, body2)

  st <- .load_review(ad, id)
  expect_identical(st$rec$state, "draft")

  # submit
  r1 <- reviewapp::perform_action(
    ad, st$rec, body_sha256 = reviewapp::hash_body(body1),
    blob_sha = st$blob_sha, branch_head_sha = st$head_sha,
    action = "submitted", actor = "reviewer@example.org", role = "reviewer"
  )
  expect_true(r1$report$transition_applied)

  # request revision
  st2 <- .load_review(ad, id)
  expect_identical(st2$rec$state, "in-review")
  r2 <- reviewapp::perform_action(
    ad, st2$rec, body_sha256 = reviewapp::hash_body(body1),
    blob_sha = st2$blob_sha, branch_head_sha = st2$head_sha,
    action = "request-revision", actor = "approver@example.org", role = "approver",
    note = "Clarify the framing"
  )
  expect_true(r2$report$transition_applied)

  # revise and re-submit
  st3 <- .load_review(ad, id)
  expect_identical(st3$rec$state, "needs-revision")
  expect_length(st3$rec$events, 2L)
  rec3 <- st3$rec
  rec3$current_content_sha256 <- reviewapp::hash_body(body2)
  reviewapp::validate_review_record(rec3)
  r3 <- reviewapp::perform_action(
    ad, rec3, body_sha256 = reviewapp::hash_body(body2),
    blob_sha = st3$blob_sha, branch_head_sha = st3$head_sha,
    action = "submitted", actor = "reviewer@example.org", role = "reviewer"
  )
  expect_true(r3$report$transition_applied)

  st4 <- .load_review(ad, id)
  expect_identical(st4$rec$state, "in-review")
  expect_identical(st4$rec$review_round, 2L)
  expect_length(st4$rec$events, 3L)
  expect_identical(st4$rec$events[[3]]$sequence, 2L)

  # approve
  r4 <- reviewapp::perform_action(
    ad, st4$rec, body_sha256 = reviewapp::hash_body(body2),
    blob_sha = st4$blob_sha, branch_head_sha = st4$head_sha,
    action = "approved", actor = "approver@example.org", role = "approver",
    approved_content = approved
  )
  expect_true(r4$report$transition_applied)

  st5 <- .load_review(ad, id)
  expect_identical(st5$rec$state, "approved")
  expect_length(st5$rec$events, 4L)
  expect_identical(
    reviewapp::adapter_read_approved(ad, reviewapp::approved_path_for(art$path))$content,
    approved
  )
})

# --- Path 3: administrator reopen ---------------------------------------------

test_that("PATH 3 admin reopen: non-admin rejected, admin reopen emits an explicit event", {
  skip("Task E owns v2 reopen lifecycle coverage")
  setup <- .seed_calibration_github()
  ad <- setup$adapter
  id <- "VAR-marital"

  st <- .load_review(ad, id)
  expect_identical(st$rec$state, "approved")
  expect_true(length(st$rec$events) >= 2L)

  # non-admin reopen is rejected and writes nothing
  expect_error(
    reviewapp::perform_action(
      ad, st$rec, body_sha256 = st$rec$current_content_sha256,
      blob_sha = st$blob_sha, branch_head_sha = st$head_sha,
      action = "reopened", actor = "approver@example.org", role = "approver"
    ),
    "unauthorized"
  )
  expect_identical(setup$env$counters[["patch"]], 0L)
  expect_identical(.load_review(ad, id)$rec$state, "approved")

  # administrator reopen applies the transition and appends the explicit event
  r <- reviewapp::perform_action(
    ad, st$rec, body_sha256 = st$rec$current_content_sha256,
    blob_sha = st$blob_sha, branch_head_sha = st$head_sha,
    action = "reopened", actor = "admin@example.org", role = "administrator",
    note = "Reopen for corrections"
  )
  expect_true(r$report$transition_applied)

  st2 <- .load_review(ad, id)
  expect_identical(st2$rec$state, "needs-revision")
  last <- st2$rec$events[[length(st2$rec$events)]]
  expect_identical(last$action, "reopened")
  expect_identical(last$actor_role, "administrator")
  expect_identical(last$note, "Reopen for corrections")
})

# --- optimistic locking at integration level ----------------------------------

test_that("stale write at integration level is rejected without overwrite", {
  skip("obsolete legacy lifecycle; v2 lock-boundary coverage is maintained separately")
  setup <- .seed_calibration_github()
  ad <- setup$adapter
  art <- .calibration_sample()[[1]]
  id <- art$id
  st <- .load_review(ad, id)

  # a concurrent writer moves the branch after the reviewer loaded it
  concurrent <- "concurrent-version-of-the-review-record"
  setup$env$branches$review$blobs[[.record_path(id)]] <- concurrent
  setup$env$branches$review$commit <- "concurrent-commit"

  res <- reviewapp::perform_action(
    ad, st$rec, body_sha256 = reviewapp::hash_body(.body_for(id)),
    blob_sha = st$blob_sha, branch_head_sha = st$head_sha,
    action = "submitted", actor = "reviewer@example.org", role = "reviewer"
  )
  expect_false(res$report$ok)
  expect_false(res$report$transition_applied)
  expect_identical(res$report$error$kind, "stale")
  # the concurrent version is preserved and no ref update occurred
  expect_identical(setup$env$branches$review$blobs[[.record_path(id)]], concurrent)
  expect_identical(setup$env$counters[["patch"]], 0L)
})

# --- dashboard index reflects durable review-branch state ---------------------

test_that("dashboard index reflects durable review-branch state after a lifecycle", {
  skip("obsolete legacy lifecycle; v2 queue integration is maintained separately")
  setup <- .seed_calibration_github()
  ad <- setup$adapter
  art <- .calibration_sample()[[1]]
  id <- art$id
  body <- .body_for(id)

  st <- .load_review(ad, id)
  reviewapp::perform_action(
    ad, st$rec, body_sha256 = reviewapp::hash_body(body),
    blob_sha = st$blob_sha, branch_head_sha = st$head_sha,
    action = "submitted", actor = "reviewer@example.org", role = "reviewer"
  )
  st2 <- .load_review(ad, id)
  reviewapp::perform_action(
    ad, st2$rec, body_sha256 = reviewapp::hash_body(body),
    blob_sha = st2$blob_sha, branch_head_sha = st2$head_sha,
    action = "approved", actor = "approver@example.org", role = "approver",
    approved_content = .make_artifact(art, body)
  )

  out <- reviewapp::adapter_index_review(ad)
  idx <- out$index
  expect_true("VAR-male" %in% idx$artifact_id)
  expect_identical(idx$state[idx$artifact_id == "VAR-male"], "approved")
  # seeded states remain visible: VAR-urban (needs-revision), VAR-marital (approved)
  expect_identical(idx$state[idx$artifact_id == "VAR-urban"], "needs-revision")
  # filters narrow correctly; after P1.3 all dem/ artifacts carry MOD-DEM (5),
  # geo/ carries VAR-urban only
  expect_equal(nrow(reviewapp::filter_review_index(idx, state = "approved")), 2L)
  expect_equal(nrow(reviewapp::filter_review_index(idx, state = "needs-revision")), 1L)
  expect_equal(nrow(reviewapp::filter_review_index(idx, module = "dem")), 5L)
  expect_equal(nrow(reviewapp::filter_review_index(idx, module = "geo")), 1L)
  # the approved artifact is on the review branch tree
  expect_true(reviewapp::approved_path_for(art$path) %in% names(out$blobs))
})
