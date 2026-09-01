APPROVAL_ATTESTATION_PREFIX <- "APPROVAL_ATTESTATION_V1"

.approval_rationale <- function(rationale) {
  if (!is.character(rationale) || length(rationale) != 1L ||
      is.na(rationale) || !nzchar(trimws(rationale))) {
    stop("approval requires a non-empty rationale")
  }
  trimws(rationale)
}

.current_submission_event <- function(record) {
  transitions <- Filter(function(event) {
    !is.null(event$to_state)
  }, record$events)
  if (!length(transitions)) return(NULL)
  event <- transitions[[length(transitions)]]
  if (!identical(event$action, "submitted") ||
      !identical(event$actor_role, "reviewer") ||
      !(event$from_state %in% c("draft", "needs-revision")) ||
      !identical(event$to_state, "in-review") ||
      !identical(event$body_sha256, record$current_content_sha256)) {
    return(NULL)
  }
  event
}

queue_approval_eligible <- function(
  record,
  source_binding = NULL,
  descriptor = NULL,
  actor = NULL,
  role = NULL
) {
  validate_review_record_v2(record)
  if (is.null(descriptor) ||
      !identical(
        as.character(descriptor$schema_version %||% ""),
        QUEUE_DESCRIPTOR_SCHEMA_VERSION
      ) ||
      !isTRUE(descriptor$approvals_enabled) ||
      !identical(record$state, "in-review") ||
      !source_binding_is_current(source_binding) ||
      length(record$blocker_refs) > 0L) {
    return(FALSE)
  }
  submission <- .current_submission_event(record)
  if (is.null(submission)) return(FALSE)
  if (!identical(role, "approver") || !.is_scalar_character(actor) ||
      identical(actor, submission$actor)) {
    return(FALSE)
  }
  TRUE
}

.approval_frontmatter_matches <- function(enrolled_content, proposed_content) {
  if (!is.character(proposed_content) || length(proposed_content) != 1L ||
      is.na(proposed_content)) {
    return(FALSE)
  }
  enrolled <- split_frontmatter_exact(enrolled_content)
  proposed <- split_frontmatter_exact(proposed_content)
  !is.null(enrolled$front_raw) &&
    !is.null(proposed$front_raw) &&
    identical(enrolled$front_raw, proposed$front_raw)
}

validate_approval_gate <- function(
  descriptor,
  record,
  binding,
  persisted_body,
  actor,
  role,
  rationale,
  proposed_content,
  approved_destination
) {
  rationale <- .approval_rationale(rationale)
  reasons <- c(
    if (is.null(descriptor) ||
        !identical(
          as.character(descriptor$schema_version %||% ""),
          QUEUE_DESCRIPTOR_SCHEMA_VERSION
        )) {
      "a persisted descriptor 1.1 record is required"
    },
    if (!isTRUE(descriptor$approvals_enabled %||% FALSE)) {
      "queue approvals are disabled"
    },
    if (!identical(role, "approver")) {
      "the authenticated role is not approver"
    },
    if (!.is_scalar_character(actor)) {
      "an authenticated approver identity is required"
    },
    if (!identical(record$state, "in-review")) {
      "the review record is not in-review"
    },
    if (!source_binding_is_current(binding)) {
      "the current source binding is drifted or unverifiable"
    },
    if (length(record$blocker_refs) > 0L) {
      paste0("record blockers: ", paste(record$blocker_refs, collapse = ", "))
    },
    if (!identical(hash_body(persisted_body), record$current_content_sha256)) {
      "the persisted reviewed body hash is not current"
    }
  )
  submission <- .current_submission_event(record)
  if (is.null(submission)) {
    reasons <- c(reasons, "the current revision has no matching submitted event")
  } else if (identical(actor, submission$actor)) {
    reasons <- c(reasons, "an approver cannot approve their own submitted revision")
  }
  if (!.approval_frontmatter_matches(
    binding$enrolled$content %||% "",
    proposed_content
  )) {
    reasons <- c(
      reasons,
      "the enrolled YAML front matter was not preserved byte-exactly"
    )
  }
  enrolled <- split_frontmatter_exact(binding$enrolled$content %||% "")
  if (!is.null(enrolled$front_raw) &&
      !nzchar(enrolled$line_ending %||% "") && nzchar(persisted_body)) {
    reasons <- c(
      reasons,
      paste(
        "the enrolled YAML front matter has no body separator;",
        "source correction and re-enrollment are required"
      )
    )
  }
  if (!is.null(approved_destination$content) ||
      !is.na(approved_destination$sha %||% NA_character_)) {
    reasons <- c(reasons, "the approved destination already exists")
  }
  if (length(reasons)) {
    stop(sprintf("approval denied: %s", paste(reasons, collapse = "; ")))
  }
  approved_content <- join_enrolled_body(
    enrolled$front,
    persisted_body,
    separator = enrolled$line_ending
  )
  approved <- split_frontmatter_exact(approved_content)
  if (is.null(approved$front_raw) ||
      !identical(approved$front_raw, enrolled$front_raw)) {
    stop("approval denied: generated output did not preserve YAML front matter")
  }
  list(
    rationale = rationale,
    submission = submission,
    approved_content = approved_content,
    approved_content_sha256 = hash_body(approved_content),
    approved_content_blob_sha = git_blob_sha(approved_content)
  )
}

approval_attestation_note <- function(
  approval,
  descriptor,
  record,
  actor,
  role,
  occurred_at,
  previous_record_blob_sha
) {
  prefix <- paste(
    APPROVAL_ATTESTATION_PREFIX,
    sprintf("artifact_id: %s", record$artifact_id),
    sprintf("source_revision: %s", descriptor$source_revision),
    sprintf("source_commit: %s", record$source_commit),
    sprintf("source_path: %s", record$source_artifact_path),
    sprintf("source_blob_sha: %s", record$source_artifact_blob_sha),
    sprintf("source_content_sha256: %s", record$source_content_sha256),
    sprintf("reviewed_body_sha256: %s", record$current_content_sha256),
    sprintf(
      "approved_content_sha256: %s",
      approval$approved_content_sha256
    ),
    sprintf(
      "approved_content_blob_sha: %s",
      approval$approved_content_blob_sha
    ),
    sprintf("approver: %s", actor),
    sprintf("approver_role: %s", role),
    sprintf("occurred_at: %s", occurred_at),
    sprintf(
      "review_record_blob_sha_before: %s",
      previous_record_blob_sha
    ),
    sprintf("from_state: %s", record$state),
    "to_state: approved",
    "rationale:",
    sep = "\n"
  )
  paste0(prefix, " ", approval$rationale)
}
