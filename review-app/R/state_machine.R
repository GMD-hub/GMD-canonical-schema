# State-transition engine, enforcing exactly the plan's Data Schemas
# state-transition table. Pure function: takes a record, action, actor, role
# and returns a NEW record with the transition applied and an event appended.
# Every illegal (from_state, action) pair raises an explicit error.

TRANSITIONS <- list(
  "draft" = list(submitted = c("reviewer", "in-review")),
  "in-review" = list(
    "request-revision" = c("approver", "needs-revision"),
    "approved" = c("approver", "approved")
  ),
  "needs-revision" = list(submitted = c("reviewer", "in-review")),
  "approved" = list(reopened = c("administrator", "needs-revision"))
)

#' Enforce the state-transition table.
#'
#' @param rec review record (see new_review_record)
#' @param action one of submitted / request-revision / approved / reopened
#' @param actor Connect identity string
#' @param role current actor role (reviewer / approver / administrator)
#' @return a NEW record with the transition applied and one event appended
transition <- function(rec, action, actor, role) {
  validate_review_record(rec)
  from_state <- rec$state

  valid <- TRANSITIONS[[from_state]][[action]]
  if (is.null(valid)) {
    stop(sprintf(
      "illegal transition: action '%s' not allowed from state '%s'",
      action, from_state
    ))
  }
  required_role <- valid[[1L]]
  to_state <- valid[[2L]]
  if (!identical(role, required_role)) {
    stop(sprintf(
      "unauthorized: action '%s' from state '%s' requires role '%s', got '%s'",
      action, from_state, required_role, role
    ))
  }

  sequence <- length(rec$events)
  ev <- new_event(
    action = action,
    from_state = from_state,
    to_state = to_state,
    actor = actor,
    actor_role = role,
    sequence = sequence,
    source_blob_sha = rec$source_commit,
    body_sha256 = rec$current_content_sha256
  )

  new_rec <- rec
  new_rec$state <- to_state
  new_rec$events <- c(rec$events, list(ev))
  if (from_state == "needs-revision" && to_state == "in-review" && action == "submitted") {
    new_rec$review_round <- as.integer(rec$review_round + 1L)
  }
  validate_review_record(new_rec)
  new_rec
}

#' A record-replacement event for assignments / saves that are not transitions.
record_action <- function(rec, action, actor, role, note = NULL) {
  stopifnot(action %in% c("assigned", "saved"))
  if (!is.null(role) && !role %in% ROLES) stop("invalid role")
  sequence <- length(rec$events)
  ev <- new_event(
    action = action,
    from_state = NULL,
    to_state = NULL,
    actor = actor,
    actor_role = role,
    sequence = sequence,
    source_blob_sha = rec$source_commit,
    body_sha256 = rec$current_content_sha256,
    note = note
  )
  new_rec <- rec
  new_rec$events <- c(rec$events, list(ev))
  validate_review_record(new_rec)
  new_rec
}
