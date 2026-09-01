# Browser-local Markdown draft recovery contract.

DRAFT_RECOVERY_SCHEMA_VERSION <- 1L

.draft_recovery_digest <- function(fields) {
  if (!is.list(fields) || is.null(names(fields)) ||
      any(!nzchar(names(fields))) || anyDuplicated(names(fields))) {
    stop("draft recovery digest fields must be a named list")
  }
  valid <- vapply(
    fields,
    function(value) {
      is.character(value) && length(value) == 1L &&
        !is.na(value) && nzchar(value)
    },
    logical(1)
  )
  if (!all(valid)) {
    stop("draft recovery digest fields must be non-empty strings")
  }
  canonical <- jsonlite::toJSON(
    fields,
    auto_unbox = TRUE,
    null = "null",
    digits = NA,
    pretty = FALSE
  )
  hash_body(canonical)
}

draft_recovery_context <- function(
  adapter,
  record,
  actor,
  base_body_sha256,
  base_record_blob_sha
) {
  validate_review_record_v2(record)
  if (!inherits(adapter, "reviewapp_github_adapter")) {
    stop("draft recovery requires a GitHub adapter")
  }
  if (!.is_sha256(base_body_sha256) || !.is_sha1(base_record_blob_sha)) {
    stop("draft recovery requires valid persisted body and record identities")
  }
  lookup_fields <- list(
    recovery_schema_version = as.character(DRAFT_RECOVERY_SCHEMA_VERSION),
    repository_owner = adapter$owner,
    repository_name = adapter$repo,
    review_branch = adapter$review_branch,
    queue_id = record$queue_id,
    artifact_id = record$artifact_id,
    actor = actor
  )
  context_fields <- c(
    lookup_fields,
    list(
      source_commit = record$source_commit,
      source_blob_sha = record$source_artifact_blob_sha,
      enrolled_at = record$enrolled_at,
      base_body_sha256 = base_body_sha256,
      base_record_blob_sha = base_record_blob_sha
    )
  )
  list(
    recovery_schema_version = DRAFT_RECOVERY_SCHEMA_VERSION,
    lookup_key = .draft_recovery_digest(lookup_fields),
    context_key = .draft_recovery_digest(context_fields),
    source_commit = record$source_commit,
    source_blob_sha = record$source_artifact_blob_sha,
    base_body_sha256 = base_body_sha256,
    base_record_blob_sha = base_record_blob_sha
  )
}

draft_recovery_controls <- function(context, editor_id, editable = TRUE) {
  shiny::div(
    class = "draft-recovery-panel",
    hidden = "hidden",
    `data-recovery-editable` = if (isTRUE(editable)) "true" else "false",
    `data-recovery-schema-version` = context$recovery_schema_version,
    `data-recovery-lookup-key` = context$lookup_key,
    `data-recovery-context-key` = context$context_key,
    `data-recovery-source-commit` = context$source_commit,
    `data-recovery-source-blob-sha` = context$source_blob_sha,
    `data-recovery-base-body-sha256` = context$base_body_sha256,
    `data-recovery-base-record-blob-sha` = context$base_record_blob_sha,
    `data-recovery-editor-id` = editor_id,
    shiny::div(
      class = "draft-recovery-copy",
      shiny::strong("Browser recovery"),
      shiny::span(
        class = "draft-recovery-status",
        role = "status",
        `aria-live` = "polite"
      )
    ),
    shiny::div(
      class = "draft-recovery-actions",
      shiny::tags$label(
        class = "visually-hidden",
        `for` = paste0(editor_id, "_recovery_entry"),
        "Recovery entry"
      ),
      shiny::tags$select(
        id = paste0(editor_id, "_recovery_entry"),
        class = "draft-recovery-select form-select form-select-sm",
        `aria-label` = "Recovery entry"
      ),
      shiny::tags$button(
        type = "button",
        class = "btn btn-sm btn-primary draft-recovery-restore",
        "Restore"
      ),
      shiny::tags$button(
        type = "button",
        class = "btn btn-sm btn-outline-danger draft-recovery-discard",
        "Discard"
      ),
      shiny::tags$button(
        type = "button",
        class = "btn btn-sm btn-outline-secondary draft-recovery-copy-button",
        "Copy"
      ),
      shiny::tags$button(
        type = "button",
        class = "btn btn-sm btn-outline-secondary draft-recovery-export",
        "Export"
      )
    )
  )
}

draft_recovery_save_ack <- function(context, saved_body) {
  list(
    context_key = context$context_key,
    saved_body_sha256 = hash_body(saved_body)
  )
}
