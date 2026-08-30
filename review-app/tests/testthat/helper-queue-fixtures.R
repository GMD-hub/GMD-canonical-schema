.sha1_fixture <- paste(rep("a", 40L), collapse = "")
.sha1_fixture_2 <- paste(rep("b", 40L), collapse = "")

.queue_record_fixture <- function(
  id = "VAR-male",
  module = "dem",
  queue_id = "fixture-queue",
  source_revision = .sha1_fixture,
  source_content = "---\na: b\n---\nbody"
) {
  new_review_record_v2(
    artifact_id = id,
    queue_id = queue_id,
    source_artifact_path = sprintf(
      "extraction/20_drafts/%s/%s.md",
      module,
      id
    ),
    source_commit = source_revision,
    source_artifact_blob_sha = git_blob_sha(source_content),
    source_content_sha256 = hash_body(source_content),
    enrolled_body_sha256 = hash_body("body"),
    current_content_sha256 = hash_body("body"),
    enrolled_at = "2026-08-24T13:25:07Z",
    enrolled_by = "admin@example.org"
  )
}

.queue_descriptor_fixture <- function(records) {
  new_queue_descriptor(
    queue_id = records[[1L]]$queue_id,
    source_revision = records[[1L]]$source_commit,
    created_at = "2026-08-24T13:25:07Z",
    created_by = "admin@example.org",
    expected_record_count = length(records),
    record_set_sha256 = queue_record_set_digest(records)
  )
}

.local_queue_role_map <- function() {
  caller <- parent.frame()
  path <- withr::local_tempfile(
    lines = c(
      "roles:",
      "  - identity: acastanedaa",
      "    role: administrator",
      "  - identity: bbrunckhorst",
      "    role: reviewer"
    ),
    .local_envir = caller
  )
  withr::local_envvar(
    REVIEW_APP_ROLES = path,
    .local_envir = caller
  )
  invisible(path)
}
