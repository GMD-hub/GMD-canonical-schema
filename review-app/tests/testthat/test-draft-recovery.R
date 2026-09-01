library(testthat)

.draft_recovery_fixture <- function(
  owner = "GMD-hub",
  repo = "fixture-repo",
  branch = "fixture-review",
  actor = "reviewer@example.org",
  queue_id = "fixture-queue",
  artifact_id = "VAR-male",
  source_commit = .sha1_fixture,
  source_blob_sha = .sha1_fixture_2,
  enrolled_at = "2026-08-24T13:25:07Z",
  body = "Persisted body",
  record_blob_sha = paste(rep("c", 40L), collapse = "")
) {
  source_content <- "---\nartifact_id: VAR-male\n---\nPersisted body"
  record <- new_review_record_v2(
    artifact_id = artifact_id,
    queue_id = queue_id,
    source_artifact_path = sprintf(
      "extraction/20_drafts/dem/%s.md",
      artifact_id
    ),
    source_commit = source_commit,
    source_artifact_blob_sha = source_blob_sha,
    source_content_sha256 = hash_body(source_content),
    enrolled_body_sha256 = hash_body(body),
    current_content_sha256 = hash_body(body),
    enrolled_at = enrolled_at,
    enrolled_by = "admin@example.org"
  )
  adapter <- new_github_adapter(
    owner = owner,
    repo = repo,
    default_branch = "main",
    review_branch = branch,
    get_token = function() "unused",
    http = function(...) NULL,
    read_only = FALSE
  )
  draft_recovery_context(
    adapter,
    record,
    actor,
    hash_body(body),
    record_blob_sha
  )
}

test_that("draft recovery context exposes only opaque repository and actor scope", {
  context <- .draft_recovery_fixture()

  expect_match(context$lookup_key, "^[0-9a-f]{64}$")
  expect_match(context$context_key, "^[0-9a-f]{64}$")
  serialized <- jsonlite::toJSON(context, auto_unbox = TRUE)
  expect_false(grepl("reviewer@example.org", serialized, fixed = TRUE))
  expect_false(grepl("GMD-hub", serialized, fixed = TRUE))
  expect_false(grepl("fixture-repo", serialized, fixed = TRUE))
  expect_false(grepl("fixture-review", serialized, fixed = TRUE))
})

test_that("lookup scope isolates actor, repository, branch, queue, and artifact", {
  base <- .draft_recovery_fixture()
  variants <- list(
    .draft_recovery_fixture(actor = "other@example.org"),
    .draft_recovery_fixture(owner = "other-owner"),
    .draft_recovery_fixture(repo = "other-repo"),
    .draft_recovery_fixture(branch = "other-review"),
    .draft_recovery_fixture(queue_id = "other-queue"),
    .draft_recovery_fixture(artifact_id = "VAR-urban")
  )

  expect_true(all(vapply(
    variants,
    function(context) !identical(context$lookup_key, base$lookup_key),
    logical(1)
  )))
})

test_that("exact scope changes with source, enrollment, and persisted basis", {
  base <- .draft_recovery_fixture()
  variants <- list(
    .draft_recovery_fixture(source_commit = paste(rep("d", 40L), collapse = "")),
    .draft_recovery_fixture(source_blob_sha = paste(rep("e", 40L), collapse = "")),
    .draft_recovery_fixture(enrolled_at = "2026-08-25T13:25:07Z"),
    .draft_recovery_fixture(body = "Changed persisted body"),
    .draft_recovery_fixture(record_blob_sha = paste(rep("f", 40L), collapse = ""))
  )

  expect_true(all(vapply(
    variants,
    function(context) {
      identical(context$lookup_key, base$lookup_key) &&
        !identical(context$context_key, base$context_key)
    },
    logical(1)
  )))
})

test_that("recovery controls carry scope but no Markdown or raw identity", {
  context <- .draft_recovery_fixture()
  html <- as.character(draft_recovery_controls(context, "detail-editor_body"))

  expect_match(html, "draft-recovery-restore", fixed = TRUE)
  expect_match(html, "draft-recovery-discard", fixed = TRUE)
  expect_match(html, context$context_key, fixed = TRUE)
  expect_false(grepl("Persisted body", html, fixed = TRUE))
  expect_false(grepl("reviewer@example.org", html, fixed = TRUE))
})

test_that("read-only recovery controls expose stale drafts without edit access", {
  context <- .draft_recovery_fixture()
  html <- as.character(draft_recovery_controls(
    context,
    "detail-editor_body",
    editable = FALSE
  ))

  expect_match(html, 'data-recovery-editable="false"', fixed = TRUE)
  expect_match(html, "draft-recovery-copy-button", fixed = TRUE)
  expect_match(html, "draft-recovery-export", fixed = TRUE)
})

test_that("successful save acknowledgement correlates context and UTF-8 body", {
  context <- .draft_recovery_fixture()
  body <- "Unicode: cafe\u0301 \U0001f30d"

  expect_identical(
    draft_recovery_save_ack(context, body),
    list(
      context_key = context$context_key,
      saved_body_sha256 = hash_body(body)
    )
  )
})

test_that("R hashing matches the browser UTF-8 recovery vector", {
  body <- "Cafe\u0301, \u6f22\u5b57, and \U0001f30d\n"
  expect_identical(
    hash_body(body),
    "d37b78ea323749637c92f79fe0519a85f8fed187476ba8021c62f5cfc7c2c036"
  )
})

test_that("draft recovery context rejects invalid persisted identities", {
  context <- .draft_recovery_fixture()
  record <- .queue_record_fixture()
  adapter <- new_github_adapter(
    owner = "GMD-hub",
    repo = "fixture-repo",
    default_branch = "main",
    review_branch = "fixture-review",
    get_token = function() "unused",
    http = function(...) NULL,
    read_only = FALSE
  )

  expect_error(
    draft_recovery_context(
      adapter,
      record,
      "reviewer@example.org",
      "not-a-hash",
      context$base_record_blob_sha
    ),
    "valid persisted body"
  )
})
