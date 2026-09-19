# State transitions for country artifact reviews.

TRANSITIONS <- list(
  "draft" = list(submitted = c("reviewer", "in-review")),
  "in-review" = list(
    "request-revision" = c("approver", "needs-revision"),
    approved = c("approver", "approved")
  ),
  "needs-revision" = list(submitted = c("reviewer", "in-review")),
  "approved" = list(reopened = c("administrator", "needs-revision"))
)

transition <- function(rec, action, actor, role, note = NULL, content_sha256 = NULL) {
  validate_review_record(rec)
  from_state <- rec$state
  valid <- TRANSITIONS[[from_state]][[action]]
  if (is.null(valid)) {
    stop(sprintf(
      "illegal transition: action '%s' not allowed from state '%s'",
      action,
      from_state
    ))
  }
  required_role <- valid[[1L]]
  to_state <- valid[[2L]]
  if (!identical(role, required_role)) {
    stop(sprintf(
      "unauthorized transition: '%s' from '%s' requires '%s'",
      action,
      from_state,
      required_role
    ))
  }

  new_rec <- rec
  new_rec$state <- to_state
  if (!is.null(content_sha256)) {
    new_rec$current_content_sha256 <- content_sha256
  }
  if (from_state == "needs-revision" && to_state == "in-review" && action == "submitted") {
    new_rec$review_round <- as.integer(new_rec$review_round + 1L)
  }
  new_rec$events <- c(
    new_rec$events,
    list(new_review_event(action, from_state, to_state, actor, role, note))
  )
  validate_review_record(new_rec)
  new_rec
}

record_action <- function(rec, action, actor, role, note = NULL, content_sha256 = NULL) {
  validate_review_record(rec)
  if (!(action %in% c("saved", "assigned"))) {
    stop("record_action only supports saved/assigned")
  }
  if (!authorize(role, action)) {
    stop(sprintf("role '%s' cannot perform '%s'", role %||% "(none)", action))
  }
  new_rec <- rec
  if (!is.null(content_sha256)) {
    new_rec$current_content_sha256 <- content_sha256
  }
  new_rec$events <- c(
    new_rec$events,
    list(new_review_event(action, new_rec$state, new_rec$state, actor, role, note))
  )
  validate_review_record(new_rec)
  new_rec
}