test_that("source drift is exposed as structured state", {
  source <- "---\nvariable_id: VAR-male\n---\nbody"
  raw <- charToRaw(source)
  record <- .queue_record_fixture(source_content = source)
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
    adapter_fetch_commit = function(...) list(
      sha = record$source_commit,
      tree_sha = .sha1_fixture_2
    ),
    adapter_fetch_tree_at = function(...) list(
      commit = record$source_commit,
      blobs = stats::setNames(
        list(record$source_artifact_blob_sha),
        record$source_artifact_path
      )
    ),
    adapter_fetch_blob_by_sha = function(...) {
      list(content = source, raw = raw, sha = record$source_artifact_blob_sha)
    },
    adapter_read_draft = function(...) {
      list(content = source, raw = raw, sha = record$source_artifact_blob_sha)
    },
    .package = "reviewapp"
  )
  binding <- check_source_binding(adapter, record)
  expect_identical(binding$status, "current")
  expect_identical(binding$code, "current")
  expect_true(source_binding_is_current(binding))
  expect_identical(
    binding$expected$source_artifact_blob_sha,
    record$source_artifact_blob_sha
  )
})

test_that("unreadable current sources fail closed with a stable code", {
  source <- "---\nvariable_id: VAR-male\n---\nbody"
  raw <- charToRaw(source)
  record <- .queue_record_fixture(source_content = source)
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
    adapter_fetch_commit = function(...) list(
      sha = record$source_commit,
      tree_sha = .sha1_fixture_2
    ),
    adapter_fetch_tree_at = function(...) list(
      commit = record$source_commit,
      blobs = stats::setNames(
        list(record$source_artifact_blob_sha),
        record$source_artifact_path
      )
    ),
    adapter_fetch_blob_by_sha = function(...) {
      list(content = source, raw = raw, sha = record$source_artifact_blob_sha)
    },
    adapter_read_draft = function(...) stop("not found"),
    .package = "reviewapp"
  )
  binding <- check_source_binding(adapter, record)
  expect_identical(binding$status, "unverifiable")
  expect_identical(binding$code, "current_source_unreadable")
  expect_false(source_binding_is_current(binding))
  expect_error(
    assert_source_binding_current(adapter, record),
    class = "source_drift"
  )
})

test_that("changed source bytes are structured drift and block writes", {
  source <- "---\nvariable_id: VAR-male\n---\nbody"
  enrolled_raw <- charToRaw(source)
  current <- "---\nvariable_id: VAR-male\na: changed\n---\nbody"
  current_raw <- charToRaw(current)
  record <- .queue_record_fixture(source_content = source)
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
    adapter_fetch_commit = function(...) list(
      sha = record$source_commit,
      tree_sha = .sha1_fixture_2
    ),
    adapter_fetch_tree_at = function(...) list(
      commit = record$source_commit,
      blobs = stats::setNames(
        list(record$source_artifact_blob_sha),
        record$source_artifact_path
      )
    ),
    adapter_fetch_blob_by_sha = function(...) {
      list(
        content = source,
        raw = enrolled_raw,
        sha = record$source_artifact_blob_sha
      )
    },
    adapter_read_draft = function(...) {
      list(
        content = current,
        raw = current_raw,
        sha = git_blob_sha_raw(current_raw)
      )
    },
    .package = "reviewapp"
  )
  binding <- check_source_binding(adapter, record)
  expect_identical(binding$status, "drifted")
  expect_identical(binding$code, "source_identity_mismatch")
  expect_identical(
    binding$actual$source_content_sha256,
    hash_raw(current_raw)
  )
})

test_that("candidate source revisions verify immutable commit, path, and bytes", {
  record <- .queue_record_fixture()
  candidate_commit <- .sha1_fixture_2
  candidate_content <- "---\nvariable_id: VAR-male\n---\nnew body"
  candidate_raw <- charToRaw(candidate_content)
  candidate_blob <- git_blob_sha_raw(candidate_raw)
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
    adapter_fetch_commit = function(owner, repo, commit_sha, ...) {
      expect_identical(commit_sha, candidate_commit)
      list(sha = candidate_commit, tree_sha = .sha1_fixture)
    },
    adapter_fetch_tree_at = function(...) list(
      commit = candidate_commit,
      blobs = stats::setNames(list(candidate_blob), record$source_artifact_path)
    ),
    adapter_fetch_blob_by_sha = function(owner, repo, blob_sha, ...) {
      expect_identical(blob_sha, candidate_blob)
      list(content = candidate_content, raw = candidate_raw, sha = candidate_blob)
    },
    .package = "reviewapp"
  )
  candidate <- read_source_revision_candidate(adapter, record, candidate_commit)
  expect_identical(candidate$source_commit, candidate_commit)
  expect_identical(candidate$source_artifact_blob_sha, candidate_blob)
  expect_identical(candidate$source_content_sha256, hash_raw(candidate_raw))
  expect_identical(candidate$enrolled_body_sha256, hash_body("new body"))
})

test_that("source re-enrollment applies state rules and preserves governance", {
  record <- .queue_record_fixture()
  record$state <- "in-review"
  record$assigned_to <- list("reviewer@example.org")
  record$blocker_refs <- c("BLOCK-1", "BLOCK-2")
  record$assessment$layer1 <- list(status = "pass", evidence_ref = "old.yml")
  candidate <- list(
    artifact_id = record$artifact_id,
    source_artifact_path = record$source_artifact_path,
    source_commit = .sha1_fixture_2,
    source_artifact_blob_sha = paste(rep("c", 40L), collapse = ""),
    source_content_sha256 = paste(rep("d", 64L), collapse = ""),
    enrolled_body_sha256 = paste(rep("e", 64L), collapse = "")
  )
  result <- reenroll_review_record(
    record,
    candidate,
    "admin@example.org",
    "administrator",
    "Source draft changed.",
    previous_blob_sha = paste(rep("f", 40L), collapse = ""),
    occurred_at = "2026-08-25T13:25:07Z"
  )
  expect_false(result$replay)
  expect_identical(result$record$state, "needs-revision")
  expect_identical(result$record$assigned_to, record$assigned_to)
  expect_identical(result$record$blocker_refs, record$blocker_refs)
  expect_identical(result$record$assessment, new_empty_assessment())
  expect_identical(result$record$current_content_sha256, candidate$enrolled_body_sha256)
  expect_identical(result$record$events[[1L]]$action, "source-revision")
  expect_identical(
    result$record$events[[1L]]$review_record_blob_sha_before,
    paste(rep("f", 40L), collapse = "")
  )
  invalid_event <- result$record$events[[1L]]
  invalid_event$actor_role <- "reviewer"
  expect_error(validate_review_event_v2(invalid_event), "source-revision event")
})

test_that("source re-enrollment implements the complete state matrix", {
  expected <- c(
    draft = "draft",
    `in-review` = "needs-revision",
    `needs-revision` = "needs-revision"
  )
  for (state in names(expected)) {
    record <- .queue_record_fixture()
    record$state <- state
    candidate <- list(
      artifact_id = record$artifact_id,
      source_artifact_path = record$source_artifact_path,
      source_commit = .sha1_fixture_2,
      source_artifact_blob_sha = paste(rep("c", 40L), collapse = ""),
      source_content_sha256 = paste(rep("d", 64L), collapse = ""),
      enrolled_body_sha256 = paste(rep("e", 64L), collapse = "")
    )
    result <- reenroll_review_record(
      record,
      candidate,
      "admin@example.org",
      "administrator",
      "State matrix test.",
      previous_blob_sha = paste(rep("f", 40L), collapse = ""),
      occurred_at = "2026-08-25T13:25:07Z"
    )
    expect_identical(result$record$state, unname(expected[[state]]), info = state)
  }
})

test_that("one re-enrolled record preserves a multi-record queue denominator", {
  records <- list(
    .queue_record_fixture("VAR-one"),
    .queue_record_fixture("VAR-two")
  )
  descriptor <- .queue_descriptor_fixture(records)
  candidate <- list(
    artifact_id = records[[1L]]$artifact_id,
    source_artifact_path = records[[1L]]$source_artifact_path,
    source_commit = .sha1_fixture_2,
    source_artifact_blob_sha = paste(rep("c", 40L), collapse = ""),
    source_content_sha256 = paste(rep("d", 64L), collapse = ""),
    enrolled_body_sha256 = paste(rep("e", 64L), collapse = "")
  )
  records[[1L]] <- reenroll_review_record(
    records[[1L]],
    candidate,
    "admin@example.org",
    "administrator",
    "Update one member.",
    previous_blob_sha = paste(rep("f", 40L), collapse = ""),
    occurred_at = "2026-08-25T13:25:07Z"
  )$record
  expect_length(records, 2L)
  expect_identical(descriptor$expected_record_count, 2L)
  expect_no_error(validate_queue_record_set(records, descriptor))
})

test_that("source re-enrollment rejects approved records and duplicate replay", {
  record <- .queue_record_fixture()
  candidate <- c(
    list(
      artifact_id = record$artifact_id,
      source_artifact_path = record$source_artifact_path
    ),
    record[c(
      "source_commit", "source_artifact_blob_sha", "source_content_sha256",
      "enrolled_body_sha256"
    )]
  )
  replay <- reenroll_review_record(
    record,
    candidate,
    "admin@example.org",
    "administrator",
    "Repeat request.",
    previous_blob_sha = .sha1_fixture_2
  )
  expect_true(replay$replay)
  expect_length(replay$record$events, 0L)
  record$state <- "approved"
  expect_error(
    reenroll_review_record(
      record,
      candidate,
      "admin@example.org",
      "administrator",
      "Try approved.",
      previous_blob_sha = .sha1_fixture_2
    ),
    "must be reopened"
  )
})

test_that("candidate source verification rejects wrong bytes and artifact ID", {
  record <- .queue_record_fixture()
  candidate_commit <- .sha1_fixture_2
  candidate_content <- "---\nvariable_id: VAR-other\n---\nnew body"
  candidate_raw <- charToRaw(candidate_content)
  candidate_blob <- git_blob_sha_raw(candidate_raw)
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
    adapter_fetch_commit = function(...) list(
      sha = candidate_commit,
      tree_sha = .sha1_fixture
    ),
    adapter_fetch_tree_at = function(...) list(
      commit = candidate_commit,
      blobs = stats::setNames(list(candidate_blob), record$source_artifact_path)
    ),
    adapter_fetch_blob_by_sha = function(...) list(
      content = candidate_content,
      raw = candidate_raw,
      sha = candidate_blob
    ),
    .package = "reviewapp"
  )
  expect_error(
    read_source_revision_candidate(adapter, record, candidate_commit),
    "artifact ID"
  )
  wrong_raw <- charToRaw(sub("new body", "tampered", candidate_content))
  local_mocked_bindings(
    adapter_fetch_commit = function(...) list(
      sha = candidate_commit,
      tree_sha = .sha1_fixture
    ),
    adapter_fetch_tree_at = function(...) list(
      commit = candidate_commit,
      blobs = stats::setNames(list(candidate_blob), record$source_artifact_path)
    ),
    adapter_fetch_blob_by_sha = function(...) list(
      content = rawToChar(wrong_raw),
      raw = wrong_raw,
      sha = candidate_blob
    ),
    .package = "reviewapp"
  )
  expect_error(
    read_source_revision_candidate(adapter, record, candidate_commit),
    "bytes do not match"
  )
})
