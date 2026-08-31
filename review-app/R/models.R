# Review records, events, assessments, and role-map models.

STATES <- c("draft", "in-review", "needs-revision", "approved")
ACTIONS <- c(
  "submitted", "request-revision", "approved", "assigned", "reopened",
  "saved", "source-revision"
)
ROLES <- c("reviewer", "approver", "administrator")
REVIEW_RECORD_SCHEMA_VERSION <- "2.0"
ASSESSMENT_SECTIONS <- c(
  "Definition", "Conceptual intent", "Construction notes",
  "Consistency checks", "Escalation triggers", "Common mistakes", "Change log"
)

.is_scalar_character <- function(value) {
  is.character(value) && length(value) == 1L && !is.na(value) && nzchar(value)
}

.is_sha256 <- function(value) {
  .is_scalar_character(value) && grepl("^[0-9a-f]{64}$", value)
}

.is_sha1 <- function(value) {
  .is_scalar_character(value) && grepl("^[0-9a-f]{40}$", value)
}

.is_timestamp <- function(value) {
  .is_scalar_character(value) && grepl(
    "^20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$",
    value
  )
}

is_valid_artifact_id <- function(artifact_id) {
  .is_scalar_character(artifact_id) && grepl("^VAR-[a-z0-9]+$", artifact_id)
}

is_safe_artifact_id <- function(artifact_id) {
  .is_scalar_character(artifact_id) && grepl("^VAR-[A-Za-z0-9_-]+$", artifact_id)
}

is_valid_source_artifact_path <- function(path, artifact_id = NULL) {
  valid <- .is_scalar_character(path) && grepl(
    paste0(
      "^extraction/20_drafts/",
      "[a-z0-9][a-z0-9_-]*/VAR-[a-z0-9]+[.]md$"
    ),
    path
  )
  if (!valid) return(FALSE)
  path_id <- sub("^.*[/](VAR-[a-z0-9]+)[.]md$", "\\1", path)
  is.null(artifact_id) || identical(path_id, artifact_id)
}

.normalize_assignments <- function(value) {
  if (is.null(value)) return(list())
  if (is.character(value)) value <- as.list(value)
  if (!is.list(value) || any(!vapply(value, .is_scalar_character, logical(1)))) {
    stop("assignments must be a sequence of non-empty identities")
  }
  value
}

new_empty_assessment <- function() {
  list(
    layer1 = list(status = "pending", evidence_ref = NULL),
    layer2 = list(),
    content_errors = list(),
    agent_review = list(status = "pending", evidence_ref = NULL)
  )
}

validate_assessment <- function(assessment) {
  required <- c("layer1", "layer2", "content_errors", "agent_review")
  if (!is.list(assessment)) stop("assessment must be a mapping")
  missing <- required[!required %in% names(assessment)]
  extra <- setdiff(names(assessment), required)
  if (length(missing)) {
    stop(sprintf("assessment missing required fields: %s", paste(missing, collapse = ", ")))
  }
  if (length(extra)) {
    stop(sprintf("assessment contains unsupported fields: %s", paste(extra, collapse = ", ")))
  }
  for (field in c("layer1", "agent_review")) {
    value <- assessment[[field]]
    if (!is.list(value) || any(!c("status", "evidence_ref") %in% names(value)) ||
        length(setdiff(names(value), c("status", "evidence_ref"))) > 0L ||
        !(value$status %in% c("pending", "pass", "fail"))) {
      stop(sprintf("assessment.%s is invalid", field))
    }
    if (value$status == "pending" && !is.null(value$evidence_ref)) {
      stop(sprintf("pending assessment.%s must not contain evidence", field))
    }
    if (value$status != "pending" &&
        !.is_scalar_character(value$evidence_ref %||% NULL)) {
      stop(sprintf("assessment.%s evidence_ref is required once assessed", field))
    }
  }
  if (!is.list(assessment$layer2) || !is.list(assessment$content_errors)) {
    stop("assessment.layer2 and assessment.content_errors must be lists")
  }
  for (rating in assessment$layer2) {
    if (!is.list(rating) ||
        any(!c("section", "rating", "notes") %in% names(rating)) ||
        length(setdiff(names(rating), c("section", "rating", "notes"))) > 0L ||
        !.is_scalar_character(rating$section) ||
        !(rating$section %in% ASSESSMENT_SECTIONS) ||
        !(rating$rating %in% c("pass", "revise", "fail"))) {
      stop("each assessment.layer2 entry is invalid")
    }
    if (!is.null(rating$notes) && !is.character(rating$notes)) {
      stop("assessment.layer2 notes must be a string or null")
    }
    if (rating$rating == "revise" && !.is_scalar_character(rating$notes %||% NULL)) {
      stop("assessment notes are required for every revise rating")
    }
  }
  if (length(assessment$layer2)) {
    sections <- vapply(assessment$layer2, function(rating) rating$section, character(1))
    if (anyDuplicated(sections)) stop("assessment.layer2 sections must be unique")
  }
  for (error in assessment$content_errors) {
    if (!is.list(error) ||
        any(!c("id", "severity", "status") %in% names(error)) ||
        length(setdiff(names(error), c("id", "severity", "status", "notes", "evidence_ref"))) > 0L ||
        !.is_scalar_character(error$id) ||
        !(error$severity %in% c("block", "major", "minor")) ||
        !(error$status %in% c("open", "closed"))) {
      stop("each assessment.content_errors entry is invalid")
    }
  }
  invisible(assessment)
}

validate_review_event_v2 <- function(event) {
  required <- c(
    "event_id", "sequence", "action", "from_state", "to_state", "actor",
    "actor_role", "occurred_at", "review_record_blob_sha_before", "body_sha256",
    "note"
  )
  if (!is.list(event)) stop("v2 event must be a mapping")
  missing <- required[!required %in% names(event)]
  extra <- setdiff(names(event), required)
  if (length(missing)) {
    stop(sprintf("v2 event missing required fields: %s", paste(missing, collapse = ", ")))
  }
  if (length(extra)) {
    stop(sprintf("v2 event contains unsupported fields: %s", paste(extra, collapse = ", ")))
  }
  if (!.is_scalar_character(event$event_id) ||
      !grepl("^[0-9a-f-]{36}$", event$event_id) ||
      !is.integer(event$sequence) || event$sequence < 0L ||
      !(event$action %in% ACTIONS) || !(event$actor_role %in% ROLES) ||
      !.is_scalar_character(event$actor) || !.is_timestamp(event$occurred_at) ||
      !.is_sha1(event$review_record_blob_sha_before) ||
      !.is_sha256(event$body_sha256)) {
    stop("v2 event identity, action, actor, or digest is invalid")
  }
  if (!is.null(event$from_state) && !(event$from_state %in% STATES)) {
    stop("v2 event from_state is invalid")
  }
  if (!is.null(event$to_state) && !(event$to_state %in% STATES)) {
    stop("v2 event to_state is invalid")
  }
  if (!is.null(event$note) && !.is_scalar_character(event$note)) {
    stop("v2 event note must be a non-empty string or null")
  }
  if (identical(event$action, "source-revision")) {
    allowed <- list(
      c("draft", "draft"),
      c("in-review", "needs-revision"),
      c("needs-revision", "needs-revision")
    )
    transition_valid <- any(vapply(allowed, function(states) {
      identical(event$from_state, states[[1L]]) &&
        identical(event$to_state, states[[2L]])
    }, logical(1)))
    if (!identical(event$actor_role, "administrator") ||
        !.is_scalar_character(event$note %||% NULL) ||
        !transition_valid) {
      stop("source-revision event role, reason, or state transition is invalid")
    }
  }
  if (identical(event$action, "reopened") &&
      (!identical(event$actor_role, "administrator") ||
       !.is_scalar_character(event$note %||% NULL) ||
       !identical(event$from_state, "approved") ||
       !identical(event$to_state, "needs-revision"))) {
    stop("reopened event role, reason, or state transition is invalid")
  }
  invisible(event)
}

#' Create a legacy audit event.
new_event <- function(action, from_state = NULL, to_state = NULL, actor,
                      actor_role, sequence, source_blob_sha = NULL,
                      body_sha256, note = NULL, occurred_at = NULL) {
  if (!(action %in% ACTIONS)) stop(sprintf("invalid action '%s'", action))
  if (!(actor_role %in% ROLES)) stop(sprintf("invalid actor_role '%s'", actor_role))
  occurred_at <- occurred_at %||% format(
    Sys.time(), tz = "UTC", usetz = FALSE, format = "%Y-%m-%dT%H:%M:%SZ"
  )
  structure(list(
    event_id = as.character(uuid::UUIDgenerate()),
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
  ), class = "reviewapp_event")
}

new_event_v2 <- function(action, from_state = NULL, to_state = NULL, actor,
                         actor_role, sequence, review_record_blob_sha_before,
                         body_sha256, note = NULL, occurred_at = NULL) {
  occurred_at <- occurred_at %||% format(
    Sys.time(), tz = "UTC", usetz = FALSE, format = "%Y-%m-%dT%H:%M:%SZ"
  )
  event <- structure(list(
    event_id = as.character(uuid::UUIDgenerate()),
    sequence = as.integer(sequence),
    action = action,
    from_state = from_state,
    to_state = to_state,
    actor = actor,
    actor_role = actor_role,
    occurred_at = occurred_at,
    review_record_blob_sha_before = review_record_blob_sha_before,
    body_sha256 = body_sha256,
    note = note
  ), class = c("reviewapp_event_v2", "reviewapp_event"))
  validate_review_event_v2(event)
  event
}

#' Create a legacy review record.
new_review_record <- function(artifact_id, source_artifact_path, state = "draft",
                              review_round = 1L, assigned_to = list(),
                              current_content_sha256, source_commit,
                              events = list()) {
  record <- structure(list(
    artifact_id = artifact_id,
    source_artifact_path = source_artifact_path,
    state = state,
    review_round = as.integer(review_round),
    assigned_to = .normalize_assignments(assigned_to),
    current_content_sha256 = current_content_sha256,
    source_commit = source_commit,
    events = events
  ), class = "reviewapp_review_record")
  validate_review_record(record)
  record
}

new_review_record_v2 <- function(
  artifact_id, queue_id, source_artifact_path, source_commit,
  source_artifact_blob_sha, source_content_sha256, enrolled_body_sha256,
  enrolled_at, enrolled_by, current_content_sha256 = enrolled_body_sha256,
  state = "draft", review_round = 1L, assigned_to = list(),
  assessment = new_empty_assessment(), blocker_refs = character(0), events = list()
) {
  record <- structure(list(
    record_schema_version = REVIEW_RECORD_SCHEMA_VERSION,
    queue_id = queue_id,
    artifact_id = artifact_id,
    source_artifact_path = source_artifact_path,
    state = state,
    review_round = as.integer(review_round),
    assigned_to = .normalize_assignments(assigned_to),
    source_commit = source_commit,
    source_artifact_blob_sha = source_artifact_blob_sha,
    source_content_sha256 = source_content_sha256,
    enrolled_body_sha256 = enrolled_body_sha256,
    current_content_sha256 = current_content_sha256,
    enrolled_at = enrolled_at,
    enrolled_by = enrolled_by,
    assessment = assessment,
    blocker_refs = as.character(blocker_refs),
    events = events
  ), class = c("reviewapp_review_record_v2", "reviewapp_review_record"))
  validate_review_record_v2(record)
  record
}

validate_review_record_v2 <- function(record) {
  required <- c(
    "record_schema_version", "queue_id", "artifact_id", "source_artifact_path",
    "state", "review_round", "assigned_to", "source_commit",
    "source_artifact_blob_sha", "source_content_sha256", "enrolled_body_sha256",
    "current_content_sha256", "enrolled_at", "enrolled_by", "assessment",
    "blocker_refs", "events"
  )
  if (!is.list(record)) stop("v2 review record must be a mapping")
  missing <- required[!required %in% names(record)]
  extra <- setdiff(names(record), required)
  if (length(missing)) {
    stop(sprintf("v2 review record missing required fields: %s", paste(missing, collapse = ", ")))
  }
  if (length(extra)) {
    stop(sprintf("v2 review record contains unsupported fields: %s", paste(extra, collapse = ", ")))
  }
  if (!identical(as.character(record$record_schema_version), REVIEW_RECORD_SCHEMA_VERSION) ||
      !.is_scalar_character(record$queue_id) ||
      !is_valid_artifact_id(record$artifact_id) ||
      !is_valid_source_artifact_path(record$source_artifact_path, record$artifact_id) ||
      !(record$state %in% STATES) ||
      !is.integer(record$review_round) || record$review_round < 1L ||
      !.is_sha1(record$source_commit) || !.is_sha1(record$source_artifact_blob_sha) ||
      !.is_sha256(record$source_content_sha256) ||
      !.is_sha256(record$enrolled_body_sha256) ||
      !.is_sha256(record$current_content_sha256) ||
      !.is_timestamp(record$enrolled_at) || !.is_scalar_character(record$enrolled_by)) {
    stop("v2 review record identity, state, or digest is invalid")
  }
  if (is.null(record$assigned_to)) stop("v2 assigned_to must be a sequence")
  .normalize_assignments(record$assigned_to)
  if (!is.character(record$blocker_refs) ||
      (length(record$blocker_refs) > 0L &&
       any(!vapply(record$blocker_refs, .is_scalar_character, logical(1))))) {
    stop("v2 blocker_refs must be a character vector of IDs")
  }
  validate_assessment(record$assessment)
  if (!is.list(record$events)) stop("v2 events must be a list")
  if (length(record$events)) {
    for (event in record$events) validate_review_event_v2(event)
    event_ids <- vapply(record$events, function(event) event$event_id, character(1))
    sequences <- vapply(record$events, function(event) event$sequence, integer(1))
    if (anyDuplicated(event_ids) ||
        !identical(sequences, seq_len(length(sequences)) - 1L)) {
      stop("v2 event IDs must be unique and sequences contiguous")
    }
  }
  invisible(record)
}

is_v2_review_record <- function(record) {
  is.list(record) && identical(
    as.character(record$record_schema_version %||% ""),
    REVIEW_RECORD_SCHEMA_VERSION
  )
}

is_legacy_review_record <- function(record) !is_v2_review_record(record)

#' Validate a legacy or v2 review record.
validate_review_record <- function(record) {
  if ("record_schema_version" %in% names(record) &&
      !identical(as.character(record$record_schema_version), REVIEW_RECORD_SCHEMA_VERSION)) {
    stop(sprintf("unsupported review record schema version '%s'", record$record_schema_version))
  }
  if (is_v2_review_record(record)) return(validate_review_record_v2(record))
  required <- c(
    "artifact_id", "source_artifact_path", "state", "review_round", "assigned_to",
    "current_content_sha256", "source_commit", "events"
  )
  if (!is.list(record)) stop("review record must be a mapping")
  missing <- required[!required %in% names(record)]
  if (length(missing)) {
    stop(sprintf("review record missing required fields: %s", paste(missing, collapse = ", ")))
  }
  if (!(record$state %in% STATES)) stop(sprintf("invalid state '%s'", record$state))
  if (!is.integer(record$review_round) || record$review_round < 1L) {
    stop("review_round must be an integer >= 1")
  }
  if (!grepl("^[0-9a-f]{64}$", record$current_content_sha256)) {
    stop("current_content_sha256 must be a 64-character lowercase hex SHA-256")
  }
  invisible(record)
}

add_event <- function(record, event) {
  validate_review_record(record)
  if (is_v2_review_record(record)) validate_review_event_v2(event)
  record$events <- c(record$events, list(event))
  validate_review_record(record)
  record
}

record_state <- function(record) record$state
review_round <- function(record) record$review_round
assigned_to <- function(record) record$assigned_to

set_assigned_to <- function(record, identities) {
  record$assigned_to <- .normalize_assignments(identities)
  validate_review_record(record)
  record
}

#' Parse a legacy or v2 YAML review record.
parse_review_record <- function(yaml_string) {
  record <- yaml::read_yaml(text = yaml_string)
  if (!is.list(record)) stop("review record YAML must decode to a mapping")
  if ("record_schema_version" %in% names(record)) {
    if (!identical(as.character(record$record_schema_version), REVIEW_RECORD_SCHEMA_VERSION)) {
      stop(sprintf("unsupported review record schema version '%s'", record$record_schema_version))
    }
    required <- c(
      "record_schema_version", "queue_id", "artifact_id", "source_artifact_path",
      "state", "review_round", "assigned_to", "source_commit",
      "source_artifact_blob_sha", "source_content_sha256", "enrolled_body_sha256",
      "current_content_sha256", "enrolled_at", "enrolled_by", "assessment",
      "blocker_refs", "events"
    )
    missing <- required[!required %in% names(record)]
    if (length(missing)) {
      stop(sprintf(
        "v2 review record missing required fields: %s",
        paste(missing, collapse = ", ")
      ))
    }
    record$review_round <- as.integer(record$review_round)
    record$assigned_to <- .normalize_assignments(record$assigned_to)
    record$blocker_refs <- as.character(unlist(record$blocker_refs %||% list()))
    record$events <- lapply(record$events, function(event) {
      event_required <- c(
        "event_id", "sequence", "action", "from_state", "to_state", "actor",
        "actor_role", "occurred_at", "review_record_blob_sha_before",
        "body_sha256", "note"
      )
      missing_event <- event_required[!event_required %in% names(event)]
      if (length(missing_event)) {
        stop(sprintf(
          "v2 event missing required fields: %s",
          paste(missing_event, collapse = ", ")
        ))
      }
      event$sequence <- as.integer(event$sequence)
      class(event) <- c("reviewapp_event_v2", "reviewapp_event")
      event
    })
    class(record) <- c("reviewapp_review_record_v2", "reviewapp_review_record")
    validate_review_record_v2(record)
    return(record)
  }
  required <- c(
    "artifact_id", "source_artifact_path", "state", "review_round", "assigned_to",
    "current_content_sha256", "source_commit", "events"
  )
  missing <- required[!required %in% names(record)]
  if (length(missing)) {
    stop(sprintf(
      "review record missing required fields: %s",
      paste(missing, collapse = ", ")
    ))
  }
  record$review_round <- as.integer(record$review_round)
  record$assigned_to <- .normalize_assignments(record$assigned_to)
  record$events <- lapply(record$events, function(event) {
    class(event) <- "reviewapp_event"
    event
  })
  class(record) <- "reviewapp_review_record"
  validate_review_record(record)
  record
}

new_role_map <- function(entries) {
  entries <- lapply(entries, function(entry) {
    if (is.null(entry$identity) || is.null(entry$role)) {
      stop("each role-map entry must have identity and role")
    }
    if (!(entry$role %in% ROLES)) stop(sprintf("invalid role '%s'", entry$role))
    list(identity = entry$identity, role = entry$role)
  })
  structure(list(roles = entries), class = "reviewapp_role_map")
}

load_role_map <- function(path) {
  if (!file.exists(path)) stop(sprintf("role map file not found: %s", path))
  raw <- tryCatch(yaml::read_yaml(path), error = function(error) {
    stop(sprintf("failed to parse role map %s: %s", path, conditionMessage(error)))
  })
  if (is.null(raw$roles)) stop(sprintf("role map %s is missing top-level `roles` key", path))
  new_role_map(raw$roles)
}

resolve_role <- function(role_map, identity) {
  if (is.null(identity) || !nzchar(identity)) return(NULL)
  hit <- Filter(function(entry) identical(entry$identity, identity), role_map$roles)
  if (!length(hit)) return(NULL)
  hit[[1L]]$role
}
