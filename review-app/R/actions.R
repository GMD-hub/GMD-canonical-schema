# Role-gated actions (Step 11 / R8, R9, R10, R14).
#
# Combines the Phase 1 state machine + authorization with the Phase 2 adapter.
# Each action is a pure orchestration function: it authorizes the actor via
# `authorize()`, applies the transition via `transition()` (pure), serializes
# the resulting record, and writes it (plus the approved artifact on approval)
# through `adapter_write_with_recovery` so a partial failure never claims a
# transition (R18). The recoverable report is returned so the UI can render
# success/failure accurately and never claim a transition that did not
# complete.

ACTION_PATH <- function(artifact_id) {
  sprintf("extraction/30_review/%s.review.yml", artifact_id)
}

# P1.2 companion-body convention: the editable working copy of a draft's body is
# persisted beside the review record so the editor reflects the last saved body
# across loads (the review branch is the only authoritative write target).
BODY_PATH <- function(artifact_id) {
  sprintf("extraction/30_review/%s.body.md", artifact_id)
}

#' Serialize a review record to YAML for writing.
#'
#' @param rec review record.
#' @return character(1) YAML string.
record_to_yaml <- function(rec) {
  yaml::as.yaml(rec, indent = 2)
}

#' Path of the approved artifact on the review branch for an artifact.
#'
#' Mirrors R14: a draft at `extraction/20_drafts/dem/VAR-male.md` is written to
#' `extraction/40_approved/dem/VAR-male.md`.
#'
#' @param source_artifact_path draft path under extraction/20_drafts/.
#' @return review-branch approved path.
approved_path_for <- function(source_artifact_path) {
  sub("^extraction/20_drafts/", "extraction/40_approved/", source_artifact_path)
}

#' Perform a role-gated state-transition action and persist it (with recovery).
#'
#' This is the single entry point the UI server calls for state-changing
#' actions (submitted, request-revision, approved, reopened, saved, assigned).
#'
#' @param adapter github adapter.
#' @param rec the loaded (current) review record.
#' @param body_sha256 SHA-256 of the current Markdown body (for the event).
#' @param blob_sha review-record blob SHA loaded at read time (optimistic lock).
#' @param branch_head_sha the review-branch commit SHA loaded at read time.
#' @param action one of the state-changing actions.
#' @param actor Connect identity.
#' @param role actor role.
#' @param approved_body_sha256 approved artifact full-merge SHA (used on approve).
#' @param approved_content full approved artifact content (used on approve; NULL otherwise).
#' @param body optional working-copy Markdown body to persist as a companion file
#'   (`extraction/30_review/<id>.body.md`) on `saved` (P1.2); NULL otherwise.
#' @param note optional note for the event.
#' @return recovery report from `adapter_write_with_recovery` plus the applied
#'   record; `transition_applied` is only TRUE on a fully successful atomic
#'   write.
perform_action <- function(
  adapter,
  rec,
  body_sha256,
  blob_sha,
  branch_head_sha,
  action,
  actor,
  role,
  approved_content = NULL,
  body = NULL,
  note = NULL
) {
  if (!authorize(role, action)) {
    stop(sprintf(
      "unauthorized: role '%s' cannot perform action '%s'",
      role %||% "(none)",
      action
    ))
  }
  # `saved`/`assigned` are record-replacement (non-transition) actions: route
  # them through record_action, never transition (which rejects them as illegal).
  # body_sha256/blob_sha flow through to the event AND the record hash (R7).
  if (action %in% c("saved", "assigned")) {
    updated <- record_action(
      rec, action, actor, role,
      note = note,
      body_sha256 = body_sha256,
      blob_sha = blob_sha
    )
  } else {
    updated <- transition(
      rec, action, actor, role,
      note = note,
      body_sha256 = body_sha256,
      blob_sha = blob_sha
    )
  }

  change_paths <- ACTION_PATH(rec$artifact_id)
  changes <- list()
  changes[[change_paths]] <- record_to_yaml(updated)

  if (action == "approved") {
    if (is.null(approved_content)) {
      stop("performing 'approved' requires approved_content")
    }
    # P2.5: the approved artifact must carry a YAML front-matter block; the
    # byte-for-byte match against the loaded draft's front matter is enforced by
    # the caller (server assembly uses the loaded front matter), so this is a
    # structural invariant / defense-in-depth gate.
    approved_front <- split_frontmatter(approved_content)$front
    if (is.null(approved_front)) {
      stop("approved content must carry YAML front matter (structural gate, P2.5)")
    }
    changes[[approved_path_for(rec$source_artifact_path)]] <- approved_content
  }
  if (action == "saved" && !is.null(body)) {
    # P1.2: the working copy is persisted atomically with the review record.
    changes[[BODY_PATH(rec$artifact_id)]] <- body
  }

  report <- adapter_write_with_recovery(
    adapter,
    changes = changes,
    expected_ref_sha = branch_head_sha,
    expected_blob_shas = stats::setNames(list(blob_sha), change_paths),
    message = sprintf(
      "review action '%s' by %s on %s",
      action,
      actor,
      rec$artifact_id
    )
  )

  list(report = report, record = updated)
}
