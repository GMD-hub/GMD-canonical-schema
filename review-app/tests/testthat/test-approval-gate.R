.approval_unit_fixture <- function(
  approvals_enabled = TRUE,
  state = "in-review",
  submitted_by = "reviewer@example.org",
  blocker_refs = character(0),
  binding_status = "current",
  assessment = new_empty_assessment()
) {
  source_content <- "---\nvariable_id: VAR-one\n---\nsource body"
  reviewed_body <- "persisted reviewed body"
  record <- new_review_record_v2(
    artifact_id = "VAR-one",
    queue_id = "approval-queue",
    source_artifact_path = "extraction/20_drafts/alpha/VAR-one.md",
    source_commit = paste(rep("a", 40L), collapse = ""),
    source_artifact_blob_sha = git_blob_sha(source_content),
    source_content_sha256 = hash_body(source_content),
    enrolled_body_sha256 = hash_body("source body"),
    current_content_sha256 = hash_body(reviewed_body),
    enrolled_at = "2026-08-24T13:25:07Z",
    enrolled_by = "admin@example.org",
    state = "draft",
    assessment = assessment,
    blocker_refs = blocker_refs
  )
  record <- record_action(
    record,
    "saved",
    submitted_by,
    "reviewer",
    body_sha256 = hash_body(reviewed_body),
    blob_sha = paste(rep("b", 40L), collapse = "")
  )
  record <- transition(
    record,
    "submitted",
    submitted_by,
    "reviewer",
    body_sha256 = hash_body(reviewed_body),
    blob_sha = paste(rep("c", 40L), collapse = "")
  )
  record$state <- state
  validate_review_record_v2(record)
  descriptor <- .queue_descriptor_fixture(
    list(record),
    approvals_enabled = approvals_enabled
  )
  binding <- list(
    status = binding_status,
    enrolled = list(
      content = source_content,
      sha = record$source_artifact_blob_sha,
      content_sha256 = record$source_content_sha256
    ),
    current = list(
      content = source_content,
      sha = record$source_artifact_blob_sha,
      content_sha256 = record$source_content_sha256
    )
  )
  list(
    descriptor = descriptor,
    record = record,
    binding = binding,
    body = reviewed_body,
    proposed = paste0(
      "---\nvariable_id: VAR-one\n---\n",
      "client body is not approval authority"
    ),
    destination = list(content = NULL, sha = NA_character_)
  )
}

.validate_unit_approval <- function(fixture, ...) {
  arguments <- utils::modifyList(list(
    descriptor = fixture$descriptor,
    record = fixture$record,
    binding = fixture$binding,
    persisted_body = fixture$body,
    actor = "approver@example.org",
    role = "approver",
    rationale = "The persisted revision is correct.",
    proposed_content = fixture$proposed,
    approved_destination = fixture$destination
  ), list(...), keep.null = TRUE)
  do.call(validate_approval_gate, arguments)
}

.perform_stateful_approval <- function(
  fixture,
  actor = "approver@example.org",
  role = "approver",
  rationale = "The persisted revision is correct.",
  proposed_body = "unsaved browser recovery text",
  record_blob_sha = NULL,
  descriptor_blob_sha = NULL,
  body_sha256 = NULL
) {
  tree <- fixture$tree()
  record_blob_sha <- record_blob_sha %||% tree[[fixture$record_path]]
  descriptor_blob_sha <- descriptor_blob_sha %||%
    tree[[QUEUE_DESCRIPTOR_PATH]]
  record <- parse_review_record(fixture$blob_text(tree[[fixture$record_path]]))
  source <- split_frontmatter_exact(fixture$source_content)
  perform_action(
    fixture$adapter,
    record,
    body_sha256 = body_sha256 %||% record$current_content_sha256,
    blob_sha = record_blob_sha,
    branch_head_sha = fixture$env$review_head,
    action = "approved",
    actor = actor,
    role = role,
    approved_content = join_enrolled_body(
      source$front,
      proposed_body,
      separator = source$line_ending
    ),
    note = rationale,
    expected_descriptor_blob_sha = descriptor_blob_sha,
    descriptor_path = QUEUE_DESCRIPTOR_PATH
  )
}

test_that("descriptor approval control remains fail closed by default", {
  disabled <- .approval_unit_fixture(approvals_enabled = FALSE)
  enabled <- .approval_unit_fixture(approvals_enabled = TRUE)

  expect_false(queue_approval_eligible(
    disabled$record,
    disabled$binding,
    disabled$descriptor,
    actor = "approver@example.org",
    role = "approver"
  ))
  expect_error(.validate_unit_approval(disabled), "approvals are disabled")
  expect_true(queue_approval_eligible(
    enabled$record,
    enabled$binding,
    enabled$descriptor,
    actor = "approver@example.org",
    role = "approver"
  ))
  expect_no_error(.validate_unit_approval(enabled))
})

test_that("roles and submitter separation are enforced by the approval gate", {
  fixture <- .approval_unit_fixture()

  expect_error(
    .validate_unit_approval(fixture, role = "reviewer"),
    "not approver"
  )
  expect_error(
    .validate_unit_approval(fixture, role = "administrator"),
    "not approver"
  )
  expect_error(
    .validate_unit_approval(fixture, actor = "reviewer@example.org"),
    "own submitted revision"
  )
})

test_that("approval requires in-review state, rationale, and no blockers", {
  expect_error(
    .validate_unit_approval(.approval_unit_fixture(state = "draft")),
    "not in-review"
  )
  expect_error(
    .validate_unit_approval(.approval_unit_fixture(), rationale = "  "),
    "non-empty rationale"
  )
  expect_error(
    .validate_unit_approval(
      .approval_unit_fixture(blocker_refs = "BLOCK-1")
    ),
    "record blockers"
  )
})

test_that("source, body, front matter, and destination must remain current", {
  expect_error(
    .validate_unit_approval(
      .approval_unit_fixture(binding_status = "drifted")
    ),
    "drifted or unverifiable"
  )
  expect_error(
    .validate_unit_approval(
      .approval_unit_fixture(binding_status = "unverifiable")
    ),
    "drifted or unverifiable"
  )
  fixture <- .approval_unit_fixture()
  expect_error(
    .validate_unit_approval(fixture, persisted_body = "stale body"),
    "body hash is not current"
  )
  expect_error(
    .validate_unit_approval(
      fixture,
      proposed_content = "---\nvariable_id: VAR-other\n---\nbody"
    ),
    "front matter was not preserved byte-exactly"
  )
  expect_error(
    .validate_unit_approval(
      fixture,
      proposed_content = gsub("\n", "\r\n", fixture$proposed, fixed = TRUE)
    ),
    "front matter was not preserved byte-exactly"
  )
  expect_error(
    .validate_unit_approval(
      fixture,
      approved_destination = list(
        content = fixture$proposed,
        sha = git_blob_sha(fixture$proposed)
      )
    ),
    "approved destination already exists"
  )
  no_separator <- "---\nvariable_id: VAR-one\n---"
  fixture$binding$enrolled$content <- no_separator
  expect_error(
    .validate_unit_approval(
      fixture,
      proposed_content = paste0(no_separator, "\nclient body")
    ),
    "has no body separator"
  )
})

test_that("legacy assessment content is irrelevant to approval eligibility", {
  assessments <- list(
    new_empty_assessment(),
    list(
      layer1 = list(status = "pass", evidence_ref = "layer1.yml"),
      layer2 = list(list(
        section = "Definition",
        rating = "pass",
        notes = NULL
      )),
      content_errors = list(),
      agent_review = list(status = "pass", evidence_ref = "agent.yml")
    ),
    list(
      layer1 = list(status = "fail", evidence_ref = "layer1.yml"),
      layer2 = list(list(
        section = "Definition",
        rating = "revise",
        notes = "Legacy revision note"
      )),
      content_errors = list(list(
        id = "LEGACY-1",
        severity = "block",
        status = "open"
      )),
      agent_review = list(status = "fail", evidence_ref = "agent.yml")
    )
  )
  expect_false(assessment_approval_complete(assessments[[1L]]))
  expect_true(assessment_approval_complete(assessments[[2L]]))
  expect_false(assessment_approval_complete(assessments[[3L]]))
  for (assessment in assessments) {
    fixture <- .approval_unit_fixture(assessment = assessment)
    expect_true(queue_approval_eligible(
      fixture$record,
      fixture$binding,
      fixture$descriptor,
      actor = "approver@example.org",
      role = "approver"
    ))
    expect_no_error(.validate_unit_approval(fixture))
  }
})

test_that("server attestation records fixed approval evidence", {
  fixture <- .approval_unit_fixture()
  approval <- .validate_unit_approval(fixture)
  occurred_at <- "2026-09-01T00:00:00Z"
  previous <- paste(rep("d", 40L), collapse = "")
  note <- approval_attestation_note(
    approval,
    fixture$descriptor,
    fixture$record,
    "approver@example.org",
    "approver",
    occurred_at,
    previous
  )

  for (value in c(
    APPROVAL_ATTESTATION_PREFIX,
    fixture$record$artifact_id,
    fixture$descriptor$source_revision,
    fixture$record$source_commit,
    fixture$record$source_artifact_path,
    fixture$record$source_artifact_blob_sha,
    fixture$record$source_content_sha256,
    fixture$record$current_content_sha256,
    approval$approved_content_sha256,
    approval$approved_content_blob_sha,
    "approver@example.org",
    "approver_role: approver",
    occurred_at,
    previous,
    "from_state: in-review",
    "to_state: approved",
    approval$rationale
  )) {
    expect_match(note, value, fixed = TRUE)
  }
})

test_that("unauthorized approval causes no token or write call", {
  fixture <- .approval_unit_fixture()
  calls <- new.env(parent = emptyenv())
  calls$token <- 0L
  calls$http <- 0L
  adapter <- new_github_adapter(
    "GMD-hub",
    "fixture",
    "main",
    "fixture-review",
    get_token = function() {
      calls$token <- calls$token + 1L
      "secret"
    },
    http = function(...) {
      calls$http <- calls$http + 1L
      stop("HTTP must not be called")
    }
  )
  for (role in list(NULL, "reviewer", "administrator")) {
    expect_error(
      perform_action(
        adapter,
        fixture$record,
        body_sha256 = fixture$record$current_content_sha256,
        blob_sha = paste(rep("e", 40L), collapse = ""),
        branch_head_sha = paste(rep("f", 40L), collapse = ""),
        action = "approved",
        actor = "identity@example.org",
        role = role,
        approved_content = fixture$proposed,
        note = "Reason"
      ),
      "unauthorized"
    )
  }
  expect_identical(calls$token, 0L)
  expect_identical(calls$http, 0L)
})

test_that("approval writes persisted bytes and record atomically", {
  fixture <- .stateful_git_fixture(
    state = "in-review",
    approvals_enabled = TRUE,
    blocker_refs = character(0),
    approval_ready = TRUE
  )
  old_head <- fixture$env$review_head
  result <- .perform_stateful_approval(fixture)

  expect_true(result$report$ok)
  expect_identical(fixture$env$patches, 1L)
  expect_identical(fixture$env$patch_attempts, 1L)
  expect_identical(
    fixture$env$commits[[result$report$commit_sha]]$parent,
    old_head
  )
  tree <- fixture$tree(result$report$commit_sha)
  persisted <- parse_review_record(fixture$blob_text(tree[[fixture$record_path]]))
  approved <- fixture$blob_text(tree[[fixture$approved_path]])
  expect_identical(persisted$state, "approved")
  expect_identical(
    approved,
    "---\nvariable_id: VAR-one\n---\nreviewed body"
  )
  expect_false(grepl("unsaved browser recovery text", approved, fixed = TRUE))
  event <- persisted$events[[length(persisted$events)]]
  expect_identical(event$action, "approved")
  expect_match(event$note, APPROVAL_ATTESTATION_PREFIX, fixed = TRUE)
  expect_match(event$note, "The persisted revision is correct.", fixed = TRUE)
  expect_match(event$note, hash_body(approved), fixed = TRUE)
  expect_match(event$note, git_blob_sha(approved), fixed = TRUE)
})

test_that("disabled descriptor denies the server action without publication", {
  fixture <- .stateful_git_fixture(
    state = "in-review",
    approvals_enabled = FALSE,
    blocker_refs = character(0),
    approval_ready = TRUE
  )
  old_head <- fixture$env$review_head
  expect_error(.perform_stateful_approval(fixture), "approvals are disabled")
  expect_identical(fixture$env$review_head, old_head)
  expect_identical(fixture$env$patch_attempts, 0L)
  expect_identical(fixture$env$patches, 0L)
  tree <- fixture$tree()
  record <- parse_review_record(fixture$blob_text(tree[[fixture$record_path]]))
  expect_identical(record$state, "in-review")
  expect_false(fixture$approved_path %in% names(tree))
})

test_that("approval preserves CRLF front matter and Unicode body bytes", {
  source_content <- paste0(
    "---\r\nvariable_id: VAR-one\r\n---\r\n",
    "source body"
  )
  reviewed_body <- "Unicode: caf\u00e9 and \U0001f30d\r\nSecond line\r\n"
  fixture <- .stateful_git_fixture(
    state = "in-review",
    approvals_enabled = TRUE,
    blocker_refs = character(0),
    approval_ready = TRUE,
    source_content = source_content,
    reviewed_body = reviewed_body
  )
  result <- .perform_stateful_approval(fixture)
  tree <- fixture$tree(result$report$commit_sha)
  actual <- fixture$blob_text(tree[[fixture$approved_path]])
  expected <- paste0(
    "---\r\nvariable_id: VAR-one\r\n---\r\n",
    reviewed_body
  )

  expect_identical(charToRaw(actual), charToRaw(expected))
  expect_identical(tree[[fixture$approved_path]], git_blob_sha(expected))
})

test_that("stale descriptor, record, and body deny approval before publication", {
  fixture <- .stateful_git_fixture(
    state = "in-review",
    approvals_enabled = TRUE,
    blocker_refs = character(0),
    approval_ready = TRUE
  )
  stale <- paste(rep("9", 40L), collapse = "")
  expect_error(
    .perform_stateful_approval(fixture, descriptor_blob_sha = stale),
    "descriptor changed"
  )
  expect_error(
    .perform_stateful_approval(fixture, record_blob_sha = stale),
    "record changed"
  )
  expect_error(
    .perform_stateful_approval(fixture, body_sha256 = hash_body("stale")),
    "supplied body hash"
  )
  expect_identical(fixture$env$patch_attempts, 0L)
  expect_identical(fixture$env$patches, 0L)
})

test_that("concurrent descriptor, record, and body changes are terminal", {
  for (kind in c("descriptor", "record", "body")) {
    fixture <- .stateful_git_fixture(
      state = "in-review",
      approvals_enabled = TRUE,
      blocker_refs = character(0),
      approval_ready = TRUE
    )
    tree <- fixture$tree()
    race <- switch(kind,
      descriptor = {
        descriptor <- parse_queue_descriptor(
          fixture$blob_text(tree[[QUEUE_DESCRIPTOR_PATH]])
        )
        descriptor$approvals_enabled <- FALSE
        list(
          path = QUEUE_DESCRIPTOR_PATH,
          content = canonical_yaml(descriptor),
          error = "descriptor changed"
        )
      },
      record = {
        record <- parse_review_record(
          fixture$blob_text(tree[[fixture$record_path]])
        )
        record$assigned_to <- list("concurrent@example.org")
        list(
          path = fixture$record_path,
          content = record_to_yaml(record),
          error = "record changed"
        )
      },
      body = list(
        path = fixture$body_path,
        content = "concurrent reviewed body",
        error = "persisted review body hash"
      )
    )
    fixture$schedule_path_race(race$path, race$content)
    expect_error(
      .perform_stateful_approval(fixture),
      race$error,
      info = kind
    )
    expect_identical(fixture$env$patch_attempts, 1L, info = kind)
    expect_identical(fixture$env$patches, 0L, info = kind)
    expect_false(
      fixture$approved_path %in% names(fixture$tree()),
      info = kind
    )
  }
})

test_that("pre-publication source race leaves approval commit unreachable", {
  fixture <- .stateful_git_fixture(
    state = "in-review",
    approvals_enabled = TRUE,
    blocker_refs = character(0),
    approval_ready = TRUE
  )
  old_head <- fixture$env$review_head
  fixture$env$corrupt_source_after_commit <- TRUE
  result <- .perform_stateful_approval(fixture)

  expect_false(result$report$ok)
  expect_identical(result$report$error$kind, "source-drift")
  expect_identical(fixture$env$review_head, old_head)
  expect_identical(fixture$env$patches, 0L)
  expect_true("commit-creation" %in% result$report$steps_completed)
  expect_false(fixture$approved_path %in% names(fixture$tree()))
})

test_that("approved destination race is terminal and preserves competitor", {
  fixture <- .stateful_git_fixture(
    state = "in-review",
    approvals_enabled = TRUE,
    blocker_refs = character(0),
    approval_ready = TRUE
  )
  fixture$env$race_destination_on_patch <- TRUE
  result <- tryCatch(.perform_stateful_approval(fixture), error = identity)

  expect_s3_class(result, "error")
  expect_match(conditionMessage(result), "approved destination changed")
  expect_identical(fixture$env$patches, 0L)
  tree <- fixture$tree()
  record <- parse_review_record(fixture$blob_text(tree[[fixture$record_path]]))
  expect_identical(record$state, "in-review")
  expect_match(
    fixture$blob_text(tree[[fixture$approved_path]]),
    "concurrent approved body",
    fixed = TRUE
  )
})

test_that("one unrelated ref race uses the existing safe retry", {
  fixture <- .stateful_git_fixture(
    state = "in-review",
    approvals_enabled = TRUE,
    blocker_refs = character(0),
    approval_ready = TRUE
  )
  fixture$env$ref_races_remaining <- 1L
  result <- .perform_stateful_approval(fixture)

  expect_true(result$report$ok)
  expect_identical(fixture$env$patch_attempts, 2L)
  expect_identical(fixture$env$patches, 1L)
  expect_identical(
    fixture$env$commits[[result$report$commit_sha]]$parent,
    fixture$env$last_competing_commit
  )
  tree <- fixture$tree()
  record <- parse_review_record(fixture$blob_text(tree[[fixture$record_path]]))
  expect_identical(record$state, "approved")
  expect_true(any(grepl("^unrelated/", names(tree))))
})
