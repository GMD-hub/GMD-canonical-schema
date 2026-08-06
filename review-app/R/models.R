# Review-record, event, assignment, and role-map models.
#
# Implements the per-artifact review record, the audit event (including the
# `sequence` field), and the role map exactly per the plan's Data Schemas
# section. Models are plain validated R lists.

STATES <- c("draft", "in-review", "needs-revision", "approved")
ACTIONS <- c("submitted", "request-revision", "approved", "assigned", "reopened", "saved")
ROLES <- c("reviewer", "approver", "administrator")

#' Create a validated audit event element (list).
new_event <- function(action, from_state = NULL, to_state = NULL, actor,
                      actor_role, sequence, source_blob_sha, body_sha256,
                      note = NULL, occurred_at = NULL) {
  if (!action %in% ACTIONS) {
    stop(sprintf("invalid action '%s'; must be one of %s", action, paste(ACTIONS, collapse = ", ")))
  }
  if (!actor_role %in% ROLES) {
    stop(sprintf("invalid actor_role '%s'; must be one of %s", actor_role, paste(ROLES, collapse = ", ")))
  }
  if (is.null(occurred_at)) {
    occurred_at <- format(Sys.time(), tz = "UTC", usetz = TRUE, format = "%Y-%m-%dT%H:%M:%SZ")
  }
  event_id <- as.character(uuid::UUIDgenerate())
  ev <- list(
    event_id = event_id,
    sequence = as.integer(sequence),
    action = action,
    from_state = from_state,
    to_state = to_state,
    actor = actor,
    actor_role = actor_role,
    occurred_at = occurred_at,
    source_blob_sha = source_blob_sha,
    body_sha256 = body_sha256,
    note = note
  )
  class(ev) <- "reviewapp_event"
  ev
}

#' Create a validated review-record element (list).
new_review_record <- function(artifact_id, source_artifact_path, state = "draft",
                              review_round = 1L, assigned_to = list(),
                              current_content_sha256, source_commit,
                              events = list()) {
  if (!is.character(artifact_id) || nchar(artifact_id) == 0L) {
    stop("artifact_id must be a non-empty string")
  }
  if (!state %in% STATES) {
    stop(sprintf("invalid state '%s'; must be one of %s", state, paste(STATES, collapse = ", ")))
  }
  if (!is.integer(review_round) || review_round < 1L) {
    stop("review_round must be an integer >= 1")
  }
  if (!grepl("^[0-9a-f]{64}$", current_content_sha256)) {
    stop("current_content_sha256 must be a 64-character lowercase hex SHA-256")
  }
  rec <- list(
    artifact_id = artifact_id,
    source_artifact_path = source_artifact_path,
    state = state,
    review_round = review_round,
    assigned_to = assigned_to,
    current_content_sha256 = current_content_sha256,
    source_commit = source_commit,
    events = events
  )
  class(rec) <- "reviewapp_review_record"
  validate_review_record(rec)
  rec
}

#' Validate a review-record element; errors on any missing/required field issue.
validate_review_record <- function(rec) {
  required <- c("artifact_id", "source_artifact_path", "state", "review_round",
                "assigned_to", "current_content_sha256", "source_commit", "events")
  missing <- required[!required %in% names(rec)]
  if (length(missing) > 0L) {
    stop(sprintf("review record missing required fields: %s", paste(missing, collapse = ", ")))
  }
  if (!rec$state %in% STATES) {
    stop(sprintf("invalid state '%s'", rec$state))
  }
  if (!is.integer(rec$review_round) || rec$review_round < 1L) {
    stop("review_round must be an integer >= 1")
  }
  if (is.null(rec$assigned_to)) rec$assigned_to <- list()
  if (!grepl("^[0-9a-f]{64}$", rec$current_content_sha256)) {
    stop("current_content_sha256 must be a 64-character lowercase hex SHA-256")
  }
  invisible(rec)
}

#' Append an event to a review record (returns a new record; original is unchanged).
add_event <- function(rec, event) {
  validate_review_record(rec)
  new_events <- c(rec$events, list(event))
  rec$events <- new_events
  validate_review_record(rec)
  rec
}

#' Return the current state of a record.
record_state <- function(rec) rec$state

#' Return the current review round.
review_round <- function(rec) rec$review_round

#' Return (a copy of) the assigned-to identities.
assigned_to <- function(rec) rec$assigned_to

#' Set assigned-to identities (returns a new record).
set_assigned_to <- function(rec, identities) {
  rec$assigned_to <- as.list(identities)
  validate_review_record(rec)
  rec
}

#' Parse a review record from a YAML string (tolerant of ordering/formatting).
parse_review_record <- function(yaml_string) {
  rec <- yaml::read_yaml(text = yaml_string)
  rec$events <- lapply(rec$events, function(e) { class(e) <- "reviewapp_event"; e })
  class(rec) <- "reviewapp_review_record"
  validate_review_record(rec)
  rec
}

#' Create a validated role map from a list of {identity, role} entries.
new_role_map <- function(entries) {
  entries <- lapply(entries, function(e) {
    if (is.null(e$identity) || is.null(e$role)) {
      stop("each role-map entry must have identity and role")
    }
    if (!e$role %in% ROLES) {
      stop(sprintf("invalid role '%s'; must be one of %s", e$role, paste(ROLES, collapse = ", ")))
    }
    list(identity = e$identity, role = e$role)
  })
  map <- list(roles = entries)
  class(map) <- "reviewapp_role_map"
  map
}

#' Load a role map from a YAML file (top-level `roles` key).
load_role_map <- function(path) {
  if (!file.exists(path)) {
    stop(sprintf("role map file not found: %s", path))
  }
  raw <- tryCatch(yaml::read_yaml(path), error = function(e) {
    stop(sprintf("failed to parse role map %s: %s", path, conditionMessage(e)))
  })
  if (is.null(raw$roles)) {
    stop(sprintf("role map %s is missing top-level `roles` key", path))
  }
  new_role_map(raw$roles)
}

#' Resolve a Connect identity to a role; NULL when unmapped.
resolve_role <- function(role_map, identity) {
  if (is.null(identity) || nchar(identity) == 0L) return(NULL)
  hit <- Filter(function(e) identical(e$identity, identity), role_map$roles)
  if (length(hit) == 0L) return(NULL)
  hit[[1L]]$role
}
