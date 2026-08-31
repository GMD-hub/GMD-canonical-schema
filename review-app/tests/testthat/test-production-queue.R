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
  expect_error(
    validate_queue_record_set(wrong, descriptor),
    "source revision"
  )
  rewritten_provenance <- records
  rewritten_provenance[[1L]]$enrolled_by <- "other-admin@example.org"
  expect_error(
    validate_queue_record_set(rewritten_provenance, descriptor),
    "record-set digest"
  )
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

test_that("approval stays fail-closed until Task D installs the rubric gate", {
  record <- .queue_record_fixture()
  record$assessment <- list(
    layer1 = list(status = "pass", evidence_ref = "evidence/layer1.yml"),
    layer2 = list(list(
      section = "Definition", rating = "pass", notes = NULL
    )),
    content_errors = list(),
    agent_review = list(status = "pass", evidence_ref = "evidence/agent.yml")
  )
  current <- list(status = "current")
  drifted <- list(status = "drifted")
  expect_true(assessment_approval_complete(record$assessment))
  expect_false(queue_approval_eligible(record, current))
  expect_false(queue_approval_eligible(record, drifted))
  record$blocker_refs <- "record-blocker"
  expect_false(queue_approval_eligible(record, current))
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

  source_raw <- charToRaw("---\r\na: b\r\n---\r\nbody\r\n")
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
