test_that("same-record stale writes fail before publication", {
  record <- .queue_record_fixture()
  descriptor <- .queue_descriptor_fixture(list(record))
  control_content <- canonical_yaml(descriptor)
  control_sha <- git_blob_sha(control_content)
  adapter <- list(read_only = FALSE)
  local_mocked_bindings(
    adapter_read_queue_descriptor = function(...) list(
      descriptor = descriptor,
      content = control_content,
      sha = control_sha,
      path = QUEUE_DESCRIPTOR_PATH
    ),
    adapter_read_review = function(...) list(
      content = record_to_yaml(record),
      sha = paste(rep("c", 40L), collapse = "")
    ),
    .package = "reviewapp"
  )
  expect_error(
    reviewapp:::.read_v2_controls(
      adapter,
      record,
      record_blob_sha = .sha1_fixture_2,
      expected_descriptor_blob_sha = control_sha,
      descriptor_path = QUEUE_DESCRIPTOR_PATH
    ),
    class = "stale_write"
  )
})

test_that("versioned actions lock only the selected record and descriptor", {
  record <- .queue_record_fixture()
  descriptor <- .queue_descriptor_fixture(list(record))
  descriptor_sha <- git_blob_sha(canonical_yaml(descriptor))
  captured <- NULL
  adapter <- list(
    owner = "o", repo = "r", review_branch = "fixture-review",
    read_only = FALSE, get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
    assert_source_binding_current = function(...) list(
      status = "current",
      code = "current",
      enrolled = list(content = "---\na: b\n---\nbody")
    ),
    .read_v2_controls = function(...) list(
      descriptor = descriptor,
      descriptor_blob_sha = descriptor_sha,
      descriptor_path = QUEUE_DESCRIPTOR_PATH,
      record = record,
      record_blob_sha = .sha1_fixture_2
    ),
    .read_v2_review_body = function(...) list(content = "body", sha = NA_character_),
    adapter_write_with_recovery = function(
      adapter, changes, expected_ref_sha, expected_blob_shas, message,
      reject_unrelated_head
    ) {
      captured <<- list(
        changes = changes,
        locks = expected_blob_shas,
        reject_unrelated_head = reject_unrelated_head
      )
      list(ok = TRUE, commit_sha = paste(rep("d", 40L), collapse = ""))
    },
    .package = "reviewapp"
  )
  caller_record <- record
  caller_record$assigned_to <- list("caller-supplied@example.org")
  result <- perform_action(
    adapter,
    caller_record,
    body_sha256 = record$current_content_sha256,
    blob_sha = .sha1_fixture_2,
    branch_head_sha = paste(rep("e", 40L), collapse = ""),
    action = "submitted",
    actor = "reviewer@example.org",
    role = "reviewer",
    expected_descriptor_blob_sha = descriptor_sha,
    descriptor_path = QUEUE_DESCRIPTOR_PATH
  )
  expect_true(result$report$ok)
  expect_identical(result$record$assigned_to, list())
  expect_setequal(names(captured$changes), ACTION_PATH(record$artifact_id))
  expect_setequal(
    names(captured$locks),
    c(
      ACTION_PATH(record$artifact_id),
      QUEUE_DESCRIPTOR_PATH,
      BODY_PATH(record$artifact_id)
    )
  )
  expect_false(captured$reject_unrelated_head)
  expect_false(LEGACY_QUEUE_INDEX_PATH %in% names(captured$locks))
})

test_that("production-v2 compatibility rejects writes until migration", {
  record <- .queue_record_fixture()
  descriptor <- .queue_descriptor_fixture(list(record))
  attr(descriptor, "compatibility_format") <- "production_v2"
  adapter <- list(read_only = FALSE)
  local_mocked_bindings(
    .read_v2_controls = function(...) list(
      descriptor = descriptor,
      descriptor_blob_sha = .sha1_fixture,
      descriptor_path = LEGACY_QUEUE_MANIFEST_PATH,
      record = record,
      record_blob_sha = .sha1_fixture_2
    ),
    .package = "reviewapp"
  )
  expect_error(
    perform_action(
      adapter,
      record,
      body_sha256 = record$current_content_sha256,
      blob_sha = .sha1_fixture_2,
      branch_head_sha = .sha1_fixture,
      action = "submitted",
      actor = "reviewer@example.org",
      role = "reviewer"
    ),
    "read-only until queue migration"
  )
})

test_that("v2 reopen stays unavailable until Task E", {
  record <- .queue_record_fixture()
  record$state <- "approved"
  descriptor <- .queue_descriptor_fixture(list(record))
  adapter <- list(read_only = FALSE)
  local_mocked_bindings(
    .read_v2_controls = function(...) list(
      descriptor = descriptor,
      descriptor_blob_sha = .sha1_fixture,
      descriptor_path = QUEUE_DESCRIPTOR_PATH,
      record = record,
      record_blob_sha = .sha1_fixture_2
    ),
    .package = "reviewapp"
  )
  expect_error(
    perform_action(
      adapter,
      record,
      body_sha256 = record$current_content_sha256,
      blob_sha = .sha1_fixture_2,
      branch_head_sha = .sha1_fixture,
      action = "reopened",
      actor = "admin@example.org",
      role = "administrator"
    ),
    "source-revision lifecycle"
  )
})

test_that("unrelated record changes do not create a global stale conflict", {
  selected_path <- "extraction/30_review/VAR-one.review.yml"
  other_path <- "extraction/30_review/VAR-two.review.yml"
  current_head <- paste(rep("c", 40L), collapse = "")
  adapter <- list(
    owner = "o", repo = "r", review_branch = "fixture-review",
    get_token = function() "secret", http = function(method, url, token, body = NULL) {
      if (grepl("git/ref/heads/", url)) {
        return(list(object = list(sha = current_head)))
      }
      list(
        tree = list(
          list(path = selected_path, type = "blob", sha = .sha1_fixture),
          list(path = other_path, type = "blob", sha = .sha1_fixture_2)
        ),
        truncated = FALSE
      )
    }
  )
  tree <- adapter_check_stale(
    adapter,
    expected_ref_sha = paste(rep("d", 40L), collapse = ""),
    expected_blob_shas = stats::setNames(list(.sha1_fixture), selected_path),
    reject_unrelated_head = FALSE
  )
  expect_identical(tree$blobs[[selected_path]], .sha1_fixture)
  expect_identical(tree$blobs[[other_path]], .sha1_fixture_2)
})

test_that("legacy review rejects server-side writes", {
  adapter <- list(read_only = TRUE)
  record <- new_review_record(
    "VAR-male",
    "extraction/20_drafts/dem/VAR-male.md",
    current_content_sha256 = paste(rep("a", 64L), collapse = ""),
    source_commit = "legacy"
  )
  expect_error(
    perform_action(
      adapter,
      record,
      body_sha256 = record$current_content_sha256,
      blob_sha = "legacy",
      branch_head_sha = "legacy-head",
      action = "saved",
      actor = "reviewer@example.org",
      role = "reviewer"
    ),
    "read-only"
  )
})

test_that("caller-controlled schema downgrade cannot bypass v2 gates", {
  adapter <- list(
    review_branch = "fixture-review",
    read_only = FALSE
  )
  forged <- new_review_record(
    "VAR-male",
    "extraction/20_drafts/dem/VAR-male.md",
    state = "in-review",
    current_content_sha256 = paste(rep("a", 64L), collapse = ""),
    source_commit = "legacy"
  )
  expect_error(
    perform_action(
      adapter,
      forged,
      body_sha256 = forged$current_content_sha256,
      blob_sha = .sha1_fixture,
      branch_head_sha = .sha1_fixture_2,
      action = "approved",
      actor = "approver@example.org",
      role = "approver",
      approved_content = "---\na: b\n---\nforged"
    ),
    "legacy review records are read-only"
  )
})
