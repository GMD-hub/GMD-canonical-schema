# Role-based authorization for country review actions.

action_requires_role <- list(
  submitted = "reviewer",
  "request-revision" = "approver",
  approved = "approver",
  reopened = "administrator",
  assigned = "administrator",
  saved = "reviewer"
)

authorize <- function(role, action) {
  if (is.null(action) || length(action) != 1L || is.na(action)) {
    return(FALSE)
  }
  required <- action_requires_role[[action]]
  if (is.null(required)) {
    return(FALSE)
  }
  if (is.null(role)) {
    return(FALSE)
  }
  identical(role, required) || identical(role, "administrator")
}