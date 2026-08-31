# Authorization gate. Single source of truth consulted by both the state
# engine and UI action-availability logic. UI hiding is not a security
# boundary; authorize() is the authoritative check.

action_requires_role <- list(
  submitted = "reviewer",
  "request-revision" = "approver",
  approved = "approver",
  reopened = "administrator",
  assigned = "administrator",
  saved = "reviewer",
  "source-revision" = "administrator",
  initialize = "administrator",
  migrate = "administrator"
)

#' Return TRUE if the given role may perform the given action.
#' @param role character(1) or NULL -- one of reviewer/approver/administrator.
#' @param action character(1) -- an action name from the action set.
#' @return logical(1)
authorize <- function(role, action) {
  if (is.null(action) || length(action) != 1L || is.na(action)) {
    # no/invalid action: fail closed (R8)
    return(FALSE)
  }
  required <- action_requires_role[[action]]
  if (is.null(required)) {
    # Unknown/unlisted action: fail closed (R8). Every valid write action
    # (including saved/assigned, added in Step 2/P1.1) must be in the map.
    return(FALSE)
  }
  !is.null(role) && identical(role, required)
}
