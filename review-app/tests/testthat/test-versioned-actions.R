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
    .write_binding = function(...) list(
      status = "drifted",
      code = "source_identity_mismatch",
      enrolled = list(
        content = "---\nvariable_id: VAR-male\n---\nbody",
        front = "---\nvariable_id: VAR-male\n---",
        line_ending = "\n"
      )
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
      reject_unrelated_head, pre_publish_check
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
  expect_identical(result$binding$status, "drifted")
})

test_that("save remains available against a drifted enrolled snapshot", {
  record <- .queue_record_fixture()
  descriptor <- .queue_descriptor_fixture(list(record))
  new_body <- "reviewed body while source is drifted"
  captured <- NULL
  adapter <- list(read_only = FALSE)
  local_mocked_bindings(
    .read_v2_controls = function(...) list(
      descriptor = descriptor,
      descriptor_blob_sha = .sha1_fixture,
      descriptor_path = QUEUE_DESCRIPTOR_PATH,
      record = record,
      record_blob_sha = .sha1_fixture_2
    ),
    .write_binding = function(...) list(
      status = "drifted",
      code = "source_identity_mismatch",
      enrolled = list(content = "---\nvariable_id: VAR-male\n---\nbody")
    ),
    .read_v2_review_body = function(...) list(content = "body", sha = NA_character_),
    adapter_write_with_recovery = function(adapter, changes, ...) {
      captured <<- changes
      list(
        ok = TRUE,
        transition_applied = TRUE,
        commit_sha = paste(rep("c", 40L), collapse = ""),
        error = NULL
      )
    },
    .package = "reviewapp"
  )
  result <- perform_action(
    adapter,
    record,
    body_sha256 = hash_body(new_body),
    blob_sha = .sha1_fixture_2,
    branch_head_sha = .sha1_fixture,
    action = "saved",
    actor = "reviewer@example.org",
    role = "reviewer",
    body = new_body
  )
  expect_true(result$report$ok)
  expect_identical(result$binding$status, "drifted")
  expect_identical(captured[[BODY_PATH(record$artifact_id)]], new_body)
})

test_that("approval remains blocked while source drift is unresolved", {
  record <- .queue_record_fixture()
  record <- transition(
    record,
    "submitted",
    "reviewer@example.org",
    "reviewer",
    body_sha256 = record$current_content_sha256,
    blob_sha = .sha1_fixture_2
  )
  descriptor <- .queue_descriptor_fixture(
    list(record),
    approvals_enabled = TRUE
  )
  expect_error(
    reviewapp:::.v2_approval_check(
      descriptor,
      record,
      list(
        status = "drifted",
        enrolled = list(content = "---\nvariable_id: VAR-male\n---\nbody")
      ),
      "body",
      "approver@example.org",
      "approver",
      "The source must be current.",
      "---\nvariable_id: VAR-male\n---\nbody",
      list(content = NULL, sha = NA_character_)
    ),
    "drifted or unverifiable"
  )
})

test_that("production-v2 compatibility rejects writes until migration", {
  record <- .queue_record_fixture()
  descriptor <- .queue_descriptor_fixture(list(record), schema_version = "1.0")
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

test_that("stateful production-v2 queue remains byte-exactly read-only", {
  fixture <- .stateful_git_fixture(
    control = "production_v2",
    state = "draft"
  )
  old_head <- fixture$env$review_head
  old_tree <- fixture$tree(old_head)
  old_bytes <- lapply(old_tree, fixture$blob_text)
  record <- parse_review_record(
    fixture$blob_text(old_tree[[fixture$record_path]])
  )

  expect_error(
    perform_action(
      fixture$adapter,
      record,
      body_sha256 = record$current_content_sha256,
      blob_sha = old_tree[[fixture$record_path]],
      branch_head_sha = old_head,
      action = "saved",
      actor = "reviewer@example.org",
      role = "reviewer",
      body = fixture$reviewed_body
    ),
    "compatibility mode is read-only"
  )
  expect_identical(fixture$env$review_head, old_head)
  expect_identical(fixture$tree(), old_tree)
  expect_identical(lapply(fixture$tree(), fixture$blob_text), old_bytes)
  expect_identical(fixture$env$patch_attempts, 0L)
  expect_identical(fixture$env$patches, 0L)
})

test_that("literal review branch rejects v2 approval before token access", {
  fixture <- .stateful_git_fixture(
    state = "in-review",
    approvals_enabled = TRUE,
    blocker_refs = character(0),
    approval_ready = TRUE
  )
  adapter <- fixture$adapter
  adapter$review_branch <- "review"
  old_head <- fixture$env$review_head
  old_tree <- fixture$tree(old_head)

  expect_error(
    perform_action(
      adapter,
      fixture$record,
      body_sha256 = fixture$record$current_content_sha256,
      blob_sha = old_tree[[fixture$record_path]],
      branch_head_sha = old_head,
      action = "approved",
      actor = "approver@example.org",
      role = "approver",
      approved_content = fixture$source_content,
      note = "The persisted revision is correct."
    ),
    "legacy review records are read-only"
  )
  expect_identical(fixture$env$token_calls, 0L)
  expect_identical(fixture$env$review_head, old_head)
  expect_identical(fixture$tree(), old_tree)
  expect_identical(fixture$env$patch_attempts, 0L)
  expect_identical(fixture$env$patches, 0L)
})

test_that("drifted approved records reopen and retire output atomically", {
  record <- .queue_record_fixture()
  record$state <- "approved"
  descriptor <- .queue_descriptor_fixture(list(record))
  enrolled <- "---\nvariable_id: VAR-male\n---\nbody"
  approved_path <- approved_path_for(record$source_artifact_path)
  approved_sha <- git_blob_sha(enrolled)
  captured <- NULL
  adapter <- list(
    owner = "o", repo = "r", review_branch = "fixture-review",
    read_only = FALSE, get_token = function() "secret", http = function(...) list()
  )
  local_mocked_bindings(
    .read_v2_controls = function(...) list(
      descriptor = descriptor,
      descriptor_blob_sha = .sha1_fixture,
      descriptor_path = QUEUE_DESCRIPTOR_PATH,
      record = record,
      record_blob_sha = .sha1_fixture_2
    ),
    .write_binding = function(...) list(
      status = "drifted",
      code = "source_identity_mismatch",
      enrolled = list(
        content = enrolled,
        front = "---\nvariable_id: VAR-male\n---",
        line_ending = "\n"
      )
    ),
    .read_v2_review_body = function(...) list(content = "body", sha = NA_character_),
    .optional_review_blob = function(...) list(
      content = enrolled,
      raw = charToRaw(enrolled),
      sha = approved_sha
    ),
    adapter_write_with_recovery = function(
      adapter, changes, expected_blob_shas, ...
    ) {
      captured <<- list(changes = changes, locks = expected_blob_shas)
      list(
        ok = TRUE,
        transition_applied = TRUE,
        commit_sha = paste(rep("d", 40L), collapse = ""),
        error = NULL
      )
    },
    .package = "reviewapp"
  )
  result <- perform_action(
    adapter,
    record,
    body_sha256 = record$current_content_sha256,
    blob_sha = .sha1_fixture_2,
    branch_head_sha = .sha1_fixture,
    action = "reopened",
    actor = "admin@example.org",
    role = "administrator",
    note = "The approved artifact needs correction."
  )
  expect_true(result$report$ok)
  expect_identical(result$record$state, "needs-revision")
  expect_identical(result$record$events[[1L]]$action, "reopened")
  expect_identical(
    result$record$events[[1L]]$review_record_blob_sha_before,
    .sha1_fixture_2
  )
  expect_true(approved_path %in% names(captured$changes))
  expect_null(captured$changes[[approved_path]])
  expect_identical(captured$locks[[approved_path]], approved_sha)
  expect_false(BODY_PATH(record$artifact_id) %in% names(captured$changes))
  expect_identical(
    result$record$current_content_sha256,
    record$current_content_sha256
  )
})

test_that("reopen fails closed when approved output is missing", {
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
    .write_binding = function(...) list(
      status = "unverifiable",
      code = "current_source_unreadable",
      enrolled = list(
        content = "---\nvariable_id: VAR-male\n---\nbody",
        front = "---\nvariable_id: VAR-male\n---",
        line_ending = "\n"
      )
    ),
    .read_v2_review_body = function(...) list(content = "body", sha = NA_character_),
    .optional_review_blob = function(...) list(content = NULL, sha = NA_character_),
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
      role = "administrator",
      note = "Correct the approved artifact."
    ),
    "approved output is missing"
  )
})

test_that("stateful approved-output race publishes no reopen", {
  fixture <- .stateful_git_fixture(
    control = "descriptor_1_1",
    state = "approved"
  )
  old_head <- fixture$env$review_head
  fixture$env$race_approved <- TRUE
  result <- tryCatch(
    perform_action(
      fixture$adapter,
      fixture$record,
      body_sha256 = fixture$record$current_content_sha256,
      blob_sha = fixture$tree(old_head)[[fixture$record_path]],
      branch_head_sha = old_head,
      action = "reopened",
      actor = "admin@example.org",
      role = "administrator",
      note = "Race the selected approved output."
    ),
    error = identity
  )
  expect_s3_class(result, "error")
  expect_match(conditionMessage(result), "approved output is inconsistent")
  expect_identical(fixture$env$patches, 0L)
  expect_false(identical(fixture$env$review_head, old_head))
  current_tree <- fixture$tree()
  current_record <- parse_review_record(
    fixture$blob_text(current_tree[[fixture$record_path]])
  )
  expect_identical(current_record$state, "approved")
  expect_length(current_record$events, length(fixture$record$events))
  expect_true(fixture$approved_path %in% names(current_tree))
})

test_that("reopen rejects an inconsistent approved output before writing", {
  record <- .queue_record_fixture()
  record$state <- "approved"
  descriptor <- .queue_descriptor_fixture(list(record))
  enrolled <- "---\nvariable_id: VAR-male\n---\nbody"
  inconsistent <- "---\nvariable_id: VAR-male\n---\nother body"
  writes <- 0L
  adapter <- list(read_only = FALSE)
  local_mocked_bindings(
    .read_v2_controls = function(...) list(
      descriptor = descriptor,
      descriptor_blob_sha = .sha1_fixture,
      descriptor_path = QUEUE_DESCRIPTOR_PATH,
      record = record,
      record_blob_sha = .sha1_fixture_2
    ),
    .write_binding = function(...) list(
      status = "current",
      code = "current",
      enrolled = list(
        content = enrolled,
        front = "---\nvariable_id: VAR-male\n---",
        line_ending = "\n"
      )
    ),
    .read_v2_review_body = function(...) list(content = "body", sha = NA_character_),
    .optional_review_blob = function(...) list(
      content = inconsistent,
      raw = charToRaw(inconsistent),
      sha = git_blob_sha(inconsistent)
    ),
    adapter_write_with_recovery = function(...) {
      writes <<- writes + 1L
      stop("writer must not run")
    },
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
      role = "administrator",
      note = "Correct the inconsistent output."
    ),
    "approved output is inconsistent"
  )
  expect_identical(writes, 0L)
})

test_that("source re-enrollment resets review data and removes stale body", {
  record <- .queue_record_fixture()
  record$state <- "in-review"
  record$assigned_to <- list("reviewer@example.org")
  record$blocker_refs <- "BLOCK-1"
  record$assessment$layer1 <- list(status = "pass", evidence_ref = "old.yml")
  descriptor <- .queue_descriptor_fixture(list(record))
  descriptor_sha <- git_blob_sha(canonical_yaml(descriptor))
  companion_sha <- paste(rep("c", 40L), collapse = "")
  candidate <- list(
    artifact_id = record$artifact_id,
    source_artifact_path = record$source_artifact_path,
    source_commit = .sha1_fixture_2,
    source_artifact_blob_sha = paste(rep("d", 40L), collapse = ""),
    source_content_sha256 = paste(rep("e", 64L), collapse = ""),
    enrolled_body_sha256 = paste(rep("f", 64L), collapse = ""),
    content = "---\nvariable_id: VAR-male\n---\nnew body"
  )
  captured <- NULL
  adapter <- list(
    owner = "o", repo = "r", review_branch = "fixture-review",
    read_only = FALSE, get_token = function() "secret", http = function(...) list()
  )
  before_digest <- queue_record_set_digest(list(record))
  local_mocked_bindings(
    .read_v2_controls = function(...) list(
      descriptor = descriptor,
      descriptor_blob_sha = descriptor_sha,
      descriptor_path = QUEUE_DESCRIPTOR_PATH,
      record = record,
      record_blob_sha = .sha1_fixture
    ),
    verify_enrolled_source = function(...) list(
      content = "---\nvariable_id: VAR-male\n---\nbody"
    ),
    .read_v2_review_body = function(...) list(
      content = "reviewed body",
      sha = companion_sha
    ),
    read_source_revision_candidate = function(...) candidate,
    adapter_write_with_recovery = function(
      adapter, changes, expected_blob_shas, ...
    ) {
      captured <<- list(changes = changes, locks = expected_blob_shas)
      list(
        ok = TRUE,
        transition_applied = TRUE,
        commit_sha = paste(rep("1", 40L), collapse = ""),
        error = NULL
      )
    },
    .package = "reviewapp"
  )
  result <- perform_action(
    adapter,
    record,
    body_sha256 = record$current_content_sha256,
    blob_sha = .sha1_fixture,
    branch_head_sha = paste(rep("2", 40L), collapse = ""),
    action = "source-revision",
    actor = "admin@example.org",
    role = "administrator",
    note = "Enroll the corrected source snapshot.",
    candidate_source_commit = .sha1_fixture_2,
    expected_descriptor_blob_sha = descriptor_sha
  )
  expect_true(result$report$ok)
  expect_identical(result$record$state, "needs-revision")
  expect_identical(result$record$assigned_to, record$assigned_to)
  expect_identical(result$record$blocker_refs, record$blocker_refs)
  expect_identical(result$record$assessment, new_empty_assessment())
  expect_identical(queue_record_set_digest(list(result$record)), before_digest)
  expect_true(BODY_PATH(record$artifact_id) %in% names(captured$changes))
  expect_null(captured$changes[[BODY_PATH(record$artifact_id)]])
  expect_identical(captured$locks[[BODY_PATH(record$artifact_id)]], companion_sha)
})

test_that("duplicate source re-enrollment creates no write or event", {
  record <- .queue_record_fixture()
  descriptor <- .queue_descriptor_fixture(list(record))
  candidate <- c(
    list(
      artifact_id = record$artifact_id,
      source_artifact_path = record$source_artifact_path,
      content = "---\nvariable_id: VAR-male\n---\nbody"
    ),
    record[c(
      "source_commit", "source_artifact_blob_sha", "source_content_sha256",
      "enrolled_body_sha256"
    )]
  )
  writes <- 0L
  adapter <- list(read_only = FALSE)
  local_mocked_bindings(
    .read_v2_controls = function(...) list(
      descriptor = descriptor,
      descriptor_blob_sha = .sha1_fixture_2,
      descriptor_path = QUEUE_DESCRIPTOR_PATH,
      record = record,
      record_blob_sha = .sha1_fixture
    ),
    verify_enrolled_source = function(...) list(content = candidate$content),
    .read_v2_review_body = function(...) list(content = "body", sha = NA_character_),
    read_source_revision_candidate = function(...) candidate,
    adapter_write_with_recovery = function(...) {
      writes <<- writes + 1L
      stop("duplicate replay must not write")
    },
    .package = "reviewapp"
  )
  result <- perform_action(
    adapter,
    record,
    body_sha256 = record$current_content_sha256,
    blob_sha = .sha1_fixture,
    branch_head_sha = .sha1_fixture_2,
    action = "source-revision",
    actor = "admin@example.org",
    role = "administrator",
    note = "Replay the same source request.",
    candidate_source_commit = record$source_commit
  )
  expect_true(result$report$ok)
  expect_false(result$report$transition_applied)
  expect_true(result$replay)
  expect_identical(writes, 0L)
  expect_length(result$record$events, 0L)
})

test_that("real source pre-publication failure leaves action commit unreachable", {
  fixture <- .stateful_git_fixture(
    control = "descriptor_1_1",
    state = "draft"
  )
  old_head <- fixture$env$review_head
  old_commit_count <- length(fixture$env$commits)
  fixture$env$corrupt_source_after_commit <- TRUE
  new_body <- "local save before source publication failure"
  result <- perform_action(
    fixture$adapter,
    fixture$record,
    body_sha256 = hash_body(new_body),
    blob_sha = fixture$tree(old_head)[[fixture$record_path]],
    branch_head_sha = old_head,
    action = "saved",
    actor = "reviewer@example.org",
    role = "reviewer",
    body = new_body
  )
  expect_false(result$report$ok)
  expect_identical(result$report$error$kind, "source-drift")
  expect_true("commit-creation" %in% result$report$steps_completed)
  expect_identical(fixture$env$review_head, old_head)
  expect_identical(fixture$env$patches, 0L)
  expect_gt(length(fixture$env$commits), old_commit_count)
  persisted <- parse_review_record(
    fixture$blob_text(fixture$tree(old_head)[[fixture$record_path]])
  )
  expect_identical(persisted$current_content_sha256, fixture$record$current_content_sha256)
})

test_that("candidate source pre-publication failure leaves revision unreachable", {
  fixture <- .stateful_git_fixture(
    control = "descriptor_1_1",
    state = "in-review"
  )
  candidate <- fixture$add_source_revision(
    "---\nvariable_id: VAR-one\n---\nnew source body",
    commit_sha = paste(rep("d", 40L), collapse = "")
  )
  old_head <- fixture$env$review_head
  old_commit_count <- length(fixture$env$commits)
  fixture$env$corrupt_source_after_commit <- TRUE
  fixture$env$corrupt_blob_sha <- candidate$blob_sha
  result <- perform_action(
    fixture$adapter,
    fixture$record,
    body_sha256 = fixture$record$current_content_sha256,
    blob_sha = fixture$tree(old_head)[[fixture$record_path]],
    branch_head_sha = old_head,
    action = "source-revision",
    actor = "admin@example.org",
    role = "administrator",
    note = "Exercise candidate pre-publication verification.",
    candidate_source_commit = candidate$commit
  )
  expect_false(result$report$ok)
  expect_identical(result$report$error$kind, "source-drift")
  expect_true("commit-creation" %in% result$report$steps_completed)
  expect_identical(fixture$env$review_head, old_head)
  expect_identical(fixture$env$patches, 0L)
  expect_gt(length(fixture$env$commits), old_commit_count)
  persisted <- parse_review_record(
    fixture$blob_text(fixture$tree(old_head)[[fixture$record_path]])
  )
  expect_identical(persisted$state, "in-review")
  expect_identical(persisted$source_commit, fixture$record$source_commit)
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
