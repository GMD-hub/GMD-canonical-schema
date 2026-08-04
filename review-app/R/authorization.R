# Authorization gate. Single source of truth consulted by both the state
# engine and UI action-availability logic. UI hiding is not a security
# boundary; authorize() is the authoritative check.

action_requires_role <- list(
  submitted = "reviewer",
  "request-revision" = "approver",
  approved = "approver",
  reopened = "administrator",
  assigned = "administrator"
)

#' Return TRUE if the given role may perform the given action.
#' @param role character(1) or NULL -- one of reviewer/approver/administrator.
#' @param action character(1) -- an action name from the action set.
#' @return logical(1)
authorize <- function(role, action) {
  required <- action_requires_role[[action]]
  if (is.null(required)) {
    # non-gated bookkeeping actions (e.g. saved) require a mapped role
    return(!is.null(role))
  }
  !is.null(role) && identical(role, required)
}
