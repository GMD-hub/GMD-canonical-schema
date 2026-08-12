# Connect identity resolution (Step 8 / R2, R3).
#
# Connect authentication is the ONLY identity source (R2); there is no second
# login layer. This module extracts the authenticated Connect user from the
# session and resolves it against the repository-managed role map (management
# is via direct repository edit -- there is no in-app role-management UI in the
# MVP). The role map is read once at session start and resolved through the
# Phase 1 `resolve_role()` helper, which returns NULL for any unmapped identity
# (never a default role).


#' Extract the Connect-provided authenticated user identity.
#'
#' Connect exposes the authenticated user via `session$user`. For local
#' development without Connect, an explicit override via the
#' `REVIEW_APP_USER` environment variable is honoured; when neither is present
#' the identity is NULL (treated as unauthenticated / no role).
#'
#' @param session the Shiny session object.
#' @return character(1) identity string, or NULL when no identity is available.
connect_identity <- function(session = NULL) {
  if (!is.null(session) && !is.null(session$user) && nzchar(session$user)) {
    return(session$user)
  }
  env_user <- Sys.getenv("REVIEW_APP_USER", unset = "")
  if (nzchar(env_user)) {
    return(env_user)
  }
  NULL
}


#' Build an authorization state for the current session identity.
#'
#' Resolves `identity` against the role map returned by `role_map_source`.
#' `role_map_source` is either an already-loaded role-map object (the result of
#' `new_role_map()` / `load_role_map()`) or a path to a YAML role-map file
#' (which is loaded via `load_role_map()`). A missing/malformed role map fails
#' loudly. An unmapped identity yields `role = NULL` /
#' `authorized = FALSE` -- never a default role (R3).
#'
#' @param identity character(1) or NULL Connect identity.
#' @param role_map_source role-map object or path to a role-map YAML file.
#' @return list(identity, role, authorized) -- authorized is TRUE only when a
#'   role was resolved.
session_auth <- function(identity, role_map_source) {
  role_map <- if (is.character(role_map_source)) {
    load_role_map(role_map_source)
  } else {
    role_map_source
  }
  if (!inherits(role_map, "reviewapp_role_map")) {
    # a raw list was passed -- re-validate it so a malformed map fails loudly
    role_map <- new_role_map(role_map$roles %||% list())
  }
  role <- resolve_role(role_map, identity)
  list(
    identity = identity,
    role = role,
    authorized = !is.null(role)
  )
}


#' Human-readable authentication status line for the UI.
#'
#' @param auth list() as returned by `session_auth()`.
#' @return character(1) status message.
auth_text <- function(auth) {
  if (is.null(auth$identity)) {
    return("Not authenticated (no Connect identity).")
  }
  if (!auth$authorized) {
    return(sprintf(
      "Authenticated as %s -- **not authorized** (no role mapped).",
      auth$identity
    ))
  }
  sprintf("Authenticated as %s (role: %s).", auth$identity, auth$role)
}

#' Semantic identity treatment for the application header.
#'
#' @param auth list() as returned by `session_auth()`.
#' @return HTML tags describing the current identity and role.
auth_identity_ui <- function(auth) {
  identity <- auth$identity %||% "No Connect identity"
  shiny::div(
    class = "identity-block",
    role_badge(auth$role),
    shiny::div(
      class = "identity-copy",
      shiny::span(class = "identity-label", "Signed in as"),
      shiny::span(class = "identity-name", identity)
    )
  )
}


#' Resolve the path to the role-map YAML file independently of the working dir.
#'
#' The Shiny server sub-process does not run from the package root, so relying
#' on a relative path like `config/roles.yml` fails (V7 app smoke test). This
#' helper returns a path by checking, in order:
#'   1. the `REVIEW_APP_ROLES` environment variable override;
#'   2. the installed-package config directory (`system.file`);
#'   3. source candidates discovered from the current directory upward (works
#'      under `devtools::load_all()` and when running tests from the workspace
#'      root).
#'
#' When no candidate exists it returns `NULL`; `session_auth()` will then
#' fail loudly on the missing role map rather than silently running without one.
#'
#' @return character(1) absolute path to a role-map YAML file, or NULL.
#' @export
reviewapp_role_map_path <- function() {
  env_path <- Sys.getenv("REVIEW_APP_ROLES", unset = "")
  if (nzchar(env_path) && file.exists(env_path)) {
    return(normalizePath(env_path))
  }

  candidates <- character(0)

  inst_cfg <- system.file("config", "roles.yml", package = "reviewapp")
  if (nzchar(inst_cfg)) {
    candidates <- c(candidates, inst_cfg)
  }

  tryCatch({
    down <- rprojroot::find_root(
      criterion = rprojroot::has_file("DESCRIPTION"),
      path = getwd()
    )
    candidates <- c(candidates, file.path(down, "config", "roles.yml"))
  }, error = function(e) NULL)

  candidates <- c(candidates,
                  "config/roles.yml", "review-app/config/roles.yml")

  for (cand in unique(candidates)) {
    if (file.exists(cand)) {
      return(normalizePath(cand))
    }
  }

  NULL
}
