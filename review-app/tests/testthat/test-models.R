# Model validation tests (V1). Verifies the review-record, event, and role-map
# models against the plan's Data Schemas section.

.sample_hash <- "a01d65a9a0e22dbe6735c4f9ca36ae3d42d8d8b50b1ee0062c8ca300925f8e24"

new_draft <- function() {
  reviewapp::new_review_record(
    artifact_id = "VAR-male",
    source_artifact_path = "extraction/20_drafts/dem/VAR-male.md",
    state = "draft",
    review_round = 1L,
    assigned_to = list(),
    current_content_sha256 = .sample_hash,
    source_commit = "abc123",
    events = list()
  )
}

test_that("a valid draft record parses and validates", {
  rec <- new_draft()
  expect_s3_class(rec, "reviewapp_review_record")
  expect_identical(reviewapp::record_state(rec), "draft")
  expect_identical(reviewapp::review_round(rec), 1L)
  expect_length(reviewapp::assigned_to(rec), 0L)
})

test_that("a missing required field is rejected", {
  rec <- new_draft()
  rec_bad <- rec
  rec_bad$current_content_sha256 <- NULL  # required
  expect_error(reviewapp::validate_review_record(rec_bad), "current_content_sha256")
})

test_that("an invalid state is rejected", {
  rec <- new_draft()
  rec_bad <- rec
  rec_bad$state <- "bogus"
  expect_error(reviewapp::new_review_record(
    artifact_id = "VAR-male",
    source_artifact_path = "x",
    state = "bogus",
    current_content_sha256 = .sample_hash,
    source_commit = "abc"
  ), "invalid state")
})

test_that("a non-64-hex content sha is rejected", {
  expect_error(reviewapp::new_review_record(
    artifact_id = "VAR-male",
    source_artifact_path = "x",
    state = "draft",
    current_content_sha256 = "tooshort",
    source_commit = "abc"
  ), "current_content_sha256")
})

test_that("an invalid review_round is rejected", {
  expect_error(reviewapp::new_review_record(
    artifact_id = "VAR-male",
    source_artifact_path = "x",
    state = "draft",
    review_round = 0L,
    current_content_sha256 = .sample_hash,
    source_commit = "abc"
  ), "review_round")
})

test_that("new_event validates action and role and assigns a sequence/UUID", {
  ev <- reviewapp::new_event(
    action = "submitted", from_state = "draft", to_state = "in-review",
    actor = "reviewer@example.org", actor_role = "reviewer", sequence = 0L,
    source_blob_sha = "abc123", body_sha256 = .sample_hash
  )
  expect_s3_class(ev, "reviewapp_event")
  expect_identical(ev$sequence, 0L)
  expect_match(ev$event_id, "^[0-9a-f-]{36}$")
  expect_error(reviewapp::new_event(
    action = "not-an-action", actor = "a", actor_role = "reviewer",
    sequence = 0L, source_blob_sha = "x", body_sha256 = .sample_hash
  ), "invalid action")
  expect_error(reviewapp::new_event(
    action = "saved", actor = "a", actor_role = "superuser",
    sequence = 0L, source_blob_sha = "x", body_sha256 = .sample_hash
  ), "invalid actor_role")
})

test_that("add_event appends and preserves the record immutably", {
  rec <- new_draft()
  ev <- reviewapp::new_event(
    action = "saved", actor = "a@b.org", actor_role = "reviewer",
    sequence = 0L, source_blob_sha = "abc123", body_sha256 = .sample_hash
  )
  original <- rec
  rec2 <- reviewapp::add_event(rec, ev)
  expect_length(rec2$events, 1L)
  expect_length(rec$events, 0L)  # original unchanged
})

test_that("parse_review_record loads a YAML string into a valid record", {
  yaml_text <- sprintf(
    "artifact_id: VAR-male\nsource_artifact_path: extraction/20_drafts/dem/VAR-male.md\nstate: draft\nreview_round: 1\nassigned_to: []\ncurrent_content_sha256: %s\nsource_commit: abc123\nevents: []\n",
    .sample_hash
  )
  rec <- reviewapp::parse_review_record(yaml_text)
  expect_s3_class(rec, "reviewapp_review_record")
  expect_identical(reviewapp::record_state(rec), "draft")
})

# ---- role map ----

test_that("role map validates entries and roles", {
  rm <- reviewapp::new_role_map(list(
    list(identity = "reviewer@example.org", role = "reviewer"),
    list(identity = "approver@example.org", role = "approver"),
    list(identity = "admin@example.org", role = "administrator")
  ))
  expect_s3_class(rm, "reviewapp_role_map")
  expect_error(reviewapp::new_role_map(list(list(identity = "x", role = "superuser"))),
               "invalid role")
  expect_error(reviewapp::new_role_map(list(list(identity = "x"))),
               "identity and role")
})

test_that("resolve_role maps identity and denies unmapped identities", {
  rm <- reviewapp::new_role_map(list(
    list(identity = "reviewer@example.org", role = "reviewer"),
    list(identity = "admin@example.org", role = "administrator")
  ))
  expect_identical(reviewapp::resolve_role(rm, "reviewer@example.org"), "reviewer")
  expect_identical(reviewapp::resolve_role(rm, "admin@example.org"), "administrator")
  expect_null(reviewapp::resolve_role(rm, "nobody@example.org"))
  expect_null(reviewapp::resolve_role(rm, NULL))
})

test_that("load_role_map fails loudly on missing or malformed files", {
  skip_if_not(file.exists(system.file(package = "reviewapp")))
  expect_error(reviewapp::load_role_map("definitely/not/here.yml"), "not found")
})
