# Release A production queue contracts and fail-closed controls.

.sha1_fixture <- paste(rep("a", 40L), collapse = "")
.sha1_fixture_2 <- paste(rep("b", 40L), collapse = "")
.sha256_fixture <- paste(rep("c", 64L), collapse = "")

.production_manifest <- function(...) {
  new_queue_manifest(
    created_at = "2026-08-24T13:25:07Z",
    created_by = "admin@example.org",
    source_commit = .sha1_fixture,
    ...
  )
}

.production_record <- function(
  state = "draft", assigned_to = list(), source_content = "---\na: b\n---\nbody"
) {
  new_review_record_v2(
    artifact_id = "VAR-male",
    queue_id = QUEUE_ID,
    source_artifact_path = "extraction/20_drafts/dem/VAR-male.md",
    source_commit = .sha1_fixture,
    source_artifact_blob_sha = git_blob_sha(source_content),
    source_content_sha256 = hash_body(source_content),
    enrolled_body_sha256 = hash_body("body"),
    current_content_sha256 = hash_body("body"),
    enrolled_at = "2026-08-24T13:25:07Z",
    enrolled_by = "admin@example.org",
    state = state,
    assigned_to = assigned_to
  )
}

.production_index <- function(manifest, record = .production_record()) {
  new_queue_index(
    QUEUE_ID,
    list(queue_index_row_from_record(record, .sha1_fixture_2, manifest))
  )
}

test_that("v2 records require immutable source identity and structured assessment", {
  record <- .production_record(assigned_to = list("reviewer@example.org"))
  round_trip <- parse_review_record(record_to_yaml(record))
  expect_true(is_v2_review_record(round_trip))
  expect_identical(round_trip$assigned_to, list("reviewer@example.org"))
  expect_true(all(c(
    "source_commit", "source_artifact_blob_sha", "source_content_sha256",
    "enrolled_body_sha256", "current_content_sha256", "assessment"
  ) %in% names(round_trip)))
  broken <- record
  broken$source_artifact_blob_sha <- NULL
  expect_error(validate_review_record_v2(broken), "source_artifact_blob_sha")
  unsupported <- record
  unsupported$record_schema_version <- "3.0"
  expect_error(validate_review_record(unsupported), "unsupported")
})

test_that("manifest and index serialize deterministically and enforce the full set", {
  manifest <- .production_manifest()
  expect_identical(manifest$approval_mode, "disabled")
  expect_setequal(
    vapply(manifest$global_blockers, function(blocker) blocker$id, character(1)),
    QUEUE_GLOBAL_BLOCKER_IDS
  )
  index <- .production_index(manifest)
  expect_error(validate_queue_index(index$rows, manifest), "total")
  expect_error(parse_queue_manifest(sub("267", "266", canonical_yaml(manifest))), "267")
  expect_identical(
    serialize_queue_index(index),
    serialize_queue_index(index)
  )
})

test_that("legacy calibration records are explicitly read-only", {
  expect_error(
    perform_action(
      adapter = NULL,
      rec = new_review_record(
        "VAR-male",
        "extraction/20_drafts/dem/VAR-male.md",
        current_content_sha256 = .sha256_fixture,
        source_commit = "abc"
      ),
      body_sha256 = .sha256_fixture,
      blob_sha = "legacy",
      branch_head_sha = "legacy-head",
      action = "saved",
      actor = "reviewer@example.org",
      role = "reviewer",
      legacy_read_only = TRUE
    ),
    "read-only"
  )
})

test_that("approval stays denied while Release A controls are pending", {
  manifest <- .production_manifest()
  record <- .production_record(state = "in-review")
  expect_false(queue_approval_eligible(manifest, record))
  enabled <- manifest
  enabled$approval_mode <- "enabled"
  enabled$approval_enablement <- list(
    enabled_at = "2026-08-24T13:25:07Z",
    enabled_by = "admin@example.org",
    readiness_command = "readiness",
    audit_event_id = "event-1"
  )
  expect_error(queue_approval_eligible(enabled, record), "global blockers")
})

test_that("Release A draft enumeration rejects incomplete or malformed sets", {
  repo_root <- tryCatch(
    rprojroot::find_root(rprojroot::has_file("AGENTS.md"), path = getwd()),
    error = function(error) NULL
  )
  if (is.null(repo_root)) {
    skip("repository draft inventory is unavailable in the built package")
  }
  paths <- list.files(
    file.path(
      repo_root,
      "extraction",
      "20_drafts"
    ),
    recursive = TRUE,
    full.names = FALSE
  )
  paths <- file.path("extraction/20_drafts", paths)
  tree <- stats::setNames(as.list(seq_along(paths)), paths)
  expect_equal(length(release_a_draft_paths(tree)), QUEUE_EXPECTED_TOTAL)
  missing <- tree[-1L]
  expect_error(release_a_draft_paths(missing), "267")
  extra <- tree
  extra[["extraction/20_drafts/dem/VAR-evil.md.bak"]] <- "blob"
  expect_error(release_a_draft_paths(extra), "malformed")
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
  queue_commit <- git("rev-parse", "HEAD")
  expect_false(identical(queue_commit, source_commit))

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
