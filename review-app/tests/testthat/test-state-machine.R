# State-transition tests (V2). One test per transition-table row plus illegal
# transition coverage per state.

.sample_hash <- "a01d65a9a0e22dbe6735c4f9ca36ae3d42d8d8b50b1ee0062c8ca300925f8e24"

mk <- function(state = "draft", round = 1L, events_n = 0L) {
  evs <- lapply(seq_len(events_n), function(i) {
    reviewapp::new_event(
      action = "saved", actor = "a@b.org", actor_role = "reviewer",
      sequence = i - 1L, source_blob_sha = "abc123",
      body_sha256 = .sample_hash
    )
  })
  reviewapp::new_review_record(
    artifact_id = "VAR-male",
    source_artifact_path = "extraction/20_drafts/dem/VAR-male.md",
    state = state,
    review_round = round,
    assigned_to = list(),
    current_content_sha256 = .sample_hash,
    source_commit = "abc123",
    events = evs
  )
}

test_that("draft -> in-review via submitted (reviewer) succeeds", {
  rec <- reviewapp::transition(mk("draft"), "submitted", "reviewer@example.org", "reviewer")
  expect_identical(reviewapp::record_state(rec), "in-review")
  expect_length(rec$events, 1L)
  expect_identical(rec$events[[1L]]$action, "submitted")
  expect_identical(rec$events[[1L]]$sequence, 0L)
  expect_identical(rec$events[[1L]]$from_state, "draft")
  expect_identical(rec$events[[1L]]$to_state, "in-review")
})

test_that("in-review -> needs-revision via request-revision (approver) succeeds", {
  rec <- reviewapp::transition(mk("in-review"), "request-revision", "approver@example.org", "approver")
  expect_identical(reviewapp::record_state(rec), "needs-revision")
  expect_identical(rec$events[[1L]]$action, "request-revision")
})

test_that("in-review -> approved via approved (approver) succeeds", {
  rec <- reviewapp::transition(mk("in-review"), "approved", "approver@example.org", "approver")
  expect_identical(reviewapp::record_state(rec), "approved")
  expect_identical(rec$events[[1L]]$action, "approved")
})

test_that("needs-revision -> in-review via submitted (reviewer) increments round", {
  rec <- reviewapp::transition(mk("needs-revision", round = 2L), "submitted", "reviewer@example.org", "reviewer")
  expect_identical(reviewapp::record_state(rec), "in-review")
  expect_identical(reviewapp::review_round(rec), 3L)
})

test_that("approved -> needs-revision via reopened (administrator) succeeds and emits event", {
  rec <- reviewapp::transition(mk("approved"), "reopened", "admin@example.org", "administrator")
  expect_identical(reviewapp::record_state(rec), "needs-revision")
  expect_identical(rec$events[[1L]]$action, "reopened")
  expect_identical(rec$events[[1L]]$actor_role, "administrator")
})

test_that("sequence increments monotonically across applied transitions", {
  r1 <- reviewapp::transition(mk("draft", events_n = 2L), "submitted", "a@b.org", "reviewer")
  expect_identical(r1$events[[3L]]$sequence, 2L)
  r2 <- reviewapp::transition(r1, "request-revision", "ap@b.org", "approver")
  expect_identical(r2$events[[4L]]$sequence, 3L)
})

# ---- illegal transitions ----

test_that("wrong role for an otherwise legal action is rejected", {
  expect_error(reviewapp::transition(mk("in-review"), "approved", "reviewer@example.org", "reviewer"),
               "requires role 'approver'")
  expect_error(reviewapp::transition(mk("draft"), "submitted", "approver@example.org", "approver"),
               "requires role 'reviewer'")
  expect_error(reviewapp::transition(mk("in-review"), "request-revision", "administrator@example.org", "administrator"),
               "requires role 'approver'")
})

test_that("reopen requires administrator role", {
  expect_error(reviewapp::transition(mk("approved"), "reopened", "reviewer@example.org", "reviewer"),
               "requires role 'administrator'")
})

test_that("illegal actions from each state are rejected", {
  # reviewer cannot approve
  expect_error(reviewapp::transition(mk("in-review"), "approved", "reviewer@example.org", "reviewer"))
  # cannot submit from in-review
  expect_error(reviewapp::transition(mk("in-review"), "submitted", "reviewer@example.org", "reviewer"),
               "not allowed from state 'in-review'")
  # cannot request-revision from draft
  expect_error(reviewapp::transition(mk("draft"), "request-revision", "approver@example.org", "approver"),
               "not allowed from state 'draft'")
  # cannot approve from needs-revision
  expect_error(reviewapp::transition(mk("needs-revision"), "approved", "approver@example.org", "approver"),
               "not allowed from state 'needs-revision'")
  # cannot reopen from non-approved
  expect_error(reviewapp::transition(mk("draft"), "reopened", "admin@example.org", "administrator"),
               "not allowed from state 'draft'")
})

test_that("transition never silently no-ops", {
  expect_error(reviewapp::transition(mk("draft"), "approved", "approver@example.org", "approver"))
})
