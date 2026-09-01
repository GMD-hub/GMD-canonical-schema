test_that("v2 records keep immutable source and reviewed-body identities", {
  record <- .queue_record_fixture()
  round_trip <- parse_review_record(record_to_yaml(record))
  expect_true(is_v2_review_record(round_trip))
  expect_identical(queue_record_identity(round_trip), queue_record_identity(record))
  expect_true(all(c(
    "source_commit", "source_artifact_blob_sha", "source_content_sha256",
    "enrolled_body_sha256", "current_content_sha256", "assessment", "events"
  ) %in% names(round_trip)))
})

test_that("minimal descriptors serialize deterministically for generic queue sizes", {
  records <- list(
    .queue_record_fixture("VAR-one", "alpha"),
    .queue_record_fixture("VAR-two", "beta"),
    .queue_record_fixture("VAR-three", "gamma")
  )
  descriptor <- .queue_descriptor_fixture(records)
  expect_identical(descriptor$expected_record_count, 3L)
  expect_identical(descriptor$schema_version, "1.1")
  expect_false(descriptor$approvals_enabled)
  expect_identical(
    canonical_yaml(descriptor),
    canonical_yaml(parse_queue_descriptor(canonical_yaml(descriptor)))
  )
  expect_no_error(validate_queue_record_set(records, descriptor))
  expect_false(any(c(
    "approval_mode", "global_blockers", "source_manifest", "queue_index_path"
  ) %in% names(descriptor)))
})

test_that("record-set validation rejects missing and duplicate records", {
  records <- list(
    .queue_record_fixture("VAR-one"),
    .queue_record_fixture("VAR-two")
  )
  descriptor <- .queue_descriptor_fixture(records)
  expect_error(
    validate_queue_record_set(records[1L], descriptor),
    "record count mismatch"
  )
  expect_error(
    validate_queue_record_set(list(records[[1L]], records[[1L]]), descriptor),
    "duplicate artifact IDs"
  )
  wrong <- records
  wrong[[2L]]$source_commit <- .sha1_fixture_2
  expect_no_error(validate_queue_record_set(wrong, descriptor))
  rewritten_provenance <- records
  rewritten_provenance[[1L]]$enrolled_by <- "other-admin@example.org"
  expect_no_error(validate_queue_record_set(rewritten_provenance, descriptor))
  changed_membership <- records
  changed_membership[[1L]]$source_artifact_path <-
    "extraction/20_drafts/other/VAR-one.md"
  expect_error(
    validate_queue_record_set(changed_membership, descriptor),
    "record-set digest"
  )
})

test_that("descriptor 1.0 remains strict and valid", {
  records <- list(
    .queue_record_fixture("VAR-one"),
    .queue_record_fixture("VAR-two")
  )
  descriptor <- .queue_descriptor_fixture(records, schema_version = "1.0")
  expect_identical(descriptor$schema_version, "1.0")
  expect_false("approvals_enabled" %in% names(descriptor))
  expect_no_error(validate_queue_record_set(records, descriptor))
  changed <- records
  changed[[1L]]$enrolled_by <- "other-admin@example.org"
  expect_error(validate_queue_record_set(changed, descriptor), "record-set digest")
  with_extra <- unclass(descriptor)
  attr(with_extra, "compatibility_format") <- NULL
  with_extra$approvals_enabled <- FALSE
  expect_error(validate_queue_descriptor(with_extra), "unsupported fields")
})

test_that("descriptor versions must be explicit strings", {
  record <- .queue_record_fixture()
  descriptor <- unclass(.queue_descriptor_fixture(list(record)))
  descriptor$schema_version <- 1.10
  expect_error(validate_queue_descriptor(descriptor), "must be a string")
})

test_that("descriptor 1.1 membership is stable across source revisions", {
  records <- list(
    .queue_record_fixture("VAR-one"),
    .queue_record_fixture("VAR-two")
  )
  before <- queue_record_set_digest(records)
  records[[1L]]$source_commit <- .sha1_fixture_2
  records[[1L]]$source_artifact_blob_sha <- paste(rep("c", 40L), collapse = "")
  records[[1L]]$source_content_sha256 <- paste(rep("d", 64L), collapse = "")
  records[[1L]]$enrolled_body_sha256 <- paste(rep("e", 64L), collapse = "")
  records[[1L]]$current_content_sha256 <- paste(rep("e", 64L), collapse = "")
  records[[1L]]$enrolled_at <- "2026-08-25T13:25:07Z"
  records[[1L]]$enrolled_by <- "other-admin@example.org"
  expect_identical(queue_record_set_digest(records), before)
  descriptor <- new_queue_descriptor(
    queue_id = "fixture-queue",
    source_revision = .sha1_fixture,
    created_at = "2026-08-24T13:25:07Z",
    created_by = "admin@example.org",
    expected_record_count = 2L,
    record_set_sha256 = before,
    approvals_enabled = FALSE
  )
  expect_no_error(validate_queue_record_set(records, descriptor))
})

test_that("existing production-v2 manifests adapt to the descriptor contract", {
  records <- list(
    .queue_record_fixture("VAR-one"),
    .queue_record_fixture("VAR-two")
  )
  paths <- vapply(records, function(record) {
    record$source_artifact_path
  }, character(1))
  manifest <- list(
    schema_version = "1.0",
    queue_id = "fixture-queue",
    created_at = "2026-08-24T13:25:07Z",
    created_by = "admin@example.org",
    source_commit = .sha1_fixture,
    expected_total = 2L,
    expected_path_set_sha256 = queue_path_set_digest(paths),
    approval_mode = "disabled",
    global_blockers = list()
  )
  descriptor <- parse_legacy_queue_manifest(canonical_yaml(manifest))
  expect_true(queue_descriptor_is_legacy(descriptor))
  expect_identical(descriptor$expected_record_count, 2L)
  expect_no_error(validate_queue_record_set(records, descriptor))
})

test_that("minimal approval predicate ignores legacy assessment content", {
  record <- .queue_record_fixture()
  record <- record_action(
    record,
    "saved",
    "reviewer@example.org",
    "reviewer",
    body_sha256 = record$current_content_sha256,
    blob_sha = .sha1_fixture_2
  )
  record <- transition(
    record,
    "submitted",
    "reviewer@example.org",
    "reviewer",
    body_sha256 = record$current_content_sha256,
    blob_sha = .sha1_fixture_2
  )
  current <- list(status = "current")
  drifted <- list(status = "drifted")
  descriptor <- .queue_descriptor_fixture(
    list(record),
    approvals_enabled = TRUE
  )
  expect_false(assessment_approval_complete(record$assessment))
  expect_false(queue_approval_eligible(record, current, descriptor))
  expect_false(queue_approval_eligible(
    record,
    current,
    descriptor,
    actor = "approver@example.org"
  ))
  expect_true(queue_approval_eligible(
    record,
    current,
    descriptor,
    actor = "approver@example.org",
    role = "approver"
  ))
  expect_false(queue_approval_eligible(
    record,
    drifted,
    descriptor,
    actor = "approver@example.org",
    role = "approver"
  ))
  record$blocker_refs <- "record-blocker"
  expect_false(queue_approval_eligible(
    record,
    current,
    descriptor,
    actor = "approver@example.org",
    role = "approver"
  ))
})

test_that("production queue validation resolves source from a distinct commit", {
  root <- tryCatch(
    rprojroot::find_root(rprojroot::has_file("AGENTS.md"), path = getwd()),
    error = function(error) NULL
  )
  if (is.null(root)) skip("repository tool is unavailable in the built package")
  repo <- withr::local_tempdir()
  dir.create(file.path(repo, "extraction", "20_drafts", "dem"), recursive = TRUE)
  source_path <- "extraction/20_drafts/dem/VAR-male.md"
  writeLines("source artifact", file.path(repo, source_path))
  git <- function(...) {
    result <- system2("git", c("-C", repo, ...), stdout = TRUE, stderr = TRUE)
    expect_null(attr(result, "status"), info = paste(result, collapse = "\n"))
    result
  }
  git("init", "--quiet")
  git("add", source_path)
  git(
    "-c", "user.name=Queue-Test", "-c", "user.email=queue@example.org",
    "commit", "--quiet", "-m", "source"
  )
  source_commit <- git("rev-parse", "HEAD")
  writeLines("queue state", file.path(repo, "queue.txt"))
  git("add", "queue.txt")
  git(
    "-c", "user.name=Queue-Test", "-c", "user.email=queue@example.org",
    "commit", "--quiet", "-m", "queue"
  )
  expect_false(identical(git("rev-parse", "HEAD"), source_commit))

  withr::local_envvar(REVIEWAPP_TOOL_TESTING = "1")
  environment <- new.env(parent = globalenv())
  sys.source(
    file.path(root, "review-app", "tools", "validate-production-queue.R"),
    envir = environment
  )
  expect_identical(
    rawToChar(environment$git_blob_raw(repo, source_commit, source_path)),
    "source artifact\n"
  )
})

test_that("production validator loads code from its own app checkout", {
  root <- tryCatch(
    rprojroot::find_root(rprojroot::has_file("AGENTS.md"), path = getwd()),
    error = function(error) NULL
  )
  if (is.null(root)) skip("repository tool is unavailable in the built package")
  script_path <- file.path(
    root,
    "review-app",
    "tools",
    "validate-production-queue.R"
  )
  withr::local_envvar(REVIEWAPP_TOOL_TESTING = "1")
  environment <- new.env(parent = globalenv())
  sys.source(script_path, envir = environment)
  expect_identical(
    environment$tool_app_dir(paste0("--file=", script_path)),
    normalizePath(file.path(root, "review-app"), mustWork = TRUE)
  )
})

test_that("production validator enforces explicit bootstrap state", {
  root <- tryCatch(
    rprojroot::find_root(rprojroot::has_file("AGENTS.md"), path = getwd()),
    error = function(error) NULL
  )
  if (is.null(root)) skip("repository tool is unavailable in the built package")
  withr::local_envvar(REVIEWAPP_TOOL_TESTING = "1")
  environment <- new.env(parent = globalenv())
  sys.source(
    file.path(root, "review-app", "tools", "validate-production-queue.R"),
    envir = environment
  )
  record <- .queue_record_fixture()
  descriptor <- .queue_descriptor_fixture(list(record))
  expect_no_error(environment$validate_bootstrap_state(
    list(record), descriptor, character(0), character(0)
  ))

  submitted <- transition(
    record,
    "submitted",
    "reviewer@example.org",
    "reviewer",
    blob_sha = .sha1_fixture_2
  )
  expect_error(
    environment$validate_bootstrap_state(
      list(submitted), descriptor, character(0), character(0)
    ),
    "does not match bootstrap state"
  )
  enabled <- descriptor
  enabled$approvals_enabled <- TRUE
  expect_error(
    environment$validate_bootstrap_state(
      list(record), enabled, character(0), character(0)
    ),
    "does not match bootstrap state"
  )
  wrong_source <- record
  wrong_source$source_commit <- .sha1_fixture_2
  expect_error(
    environment$validate_bootstrap_state(
      list(wrong_source), descriptor, character(0), character(0)
    ),
    "does not match bootstrap state"
  )

  paths <- record$source_artifact_path
  enabled_manifest <- list(
    schema_version = "1.0",
    queue_id = record$queue_id,
    created_at = "2026-08-24T13:25:07Z",
    created_by = "admin@example.org",
    source_commit = record$source_commit,
    expected_total = 1L,
    expected_path_set_sha256 = queue_path_set_digest(paths),
    approval_mode = "enabled"
  )
  expect_error(
    parse_legacy_queue_manifest(
      canonical_yaml(enabled_manifest),
      require_approval_disabled = TRUE
    ),
    "approval_mode to be disabled"
  )
})

test_that("production queue validation preserves exact source and body bytes", {
  root <- tryCatch(
    rprojroot::find_root(rprojroot::has_file("AGENTS.md"), path = getwd()),
    error = function(error) NULL
  )
  if (is.null(root)) skip("repository tool is unavailable in the built package")
  withr::local_envvar(REVIEWAPP_TOOL_TESTING = "1")
  environment <- new.env(parent = globalenv())
  sys.source(
    file.path(root, "review-app", "tools", "validate-production-queue.R"),
    envir = environment
  )

  source_raw <- charToRaw(
    "---\r\nvariable_id: VAR-male\r\n---\r\nbody\r\n"
  )
  exact_body <- split_frontmatter_exact(rawToChar(source_raw))$body_raw
  record <- new_review_record_v2(
    artifact_id = "VAR-male",
    queue_id = "fixture-queue",
    source_artifact_path = "extraction/20_drafts/dem/VAR-male.md",
    source_commit = .sha1_fixture,
    source_artifact_blob_sha = git_blob_sha_raw(source_raw),
    source_content_sha256 = hash_raw(source_raw),
    enrolled_body_sha256 = hash_raw(exact_body),
    current_content_sha256 = hash_raw(exact_body),
    enrolled_at = "2026-08-24T13:25:07Z",
    enrolled_by = "admin@example.org"
  )
  expect_true(environment$record_matches_source_bytes(record, source_raw))
  expect_false(environment$record_matches_source_bytes(
    record,
    c(source_raw, charToRaw("changed"))
  ))
})
