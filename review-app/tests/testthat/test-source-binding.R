test_that("source drift is exposed as structured state", {
  source <- "---\na: b\n---\nbody"
  raw <- charToRaw(source)
  record <- .queue_record_fixture(source_content = source)
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
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
  source <- "---\na: b\n---\nbody"
  raw <- charToRaw(source)
  record <- .queue_record_fixture(source_content = source)
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
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
  source <- "---\na: b\n---\nbody"
  enrolled_raw <- charToRaw(source)
  current <- "---\na: changed\n---\nbody"
  current_raw <- charToRaw(current)
  record <- .queue_record_fixture(source_content = source)
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
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
