# Shared presentation helpers for the review workspace.

state_label <- function(state) {
  switch(state,
    "draft" = "Draft",
    "in-review" = "In review",
    "needs-revision" = "Needs revision",
    "approved" = "Approved",
    "ERROR" = "Record error",
    state %||% "Unknown"
  )
}

state_icon <- function(state) {
  switch(state,
    "draft" = "pencil",
    "in-review" = "magnifying-glass",
    "needs-revision" = "triangle-exclamation",
    "approved" = "circle-check",
    "ERROR" = "circle-exclamation",
    "circle-question"
  )
}

state_badge <- function(state) {
  shiny::span(
    class = paste("review-badge state-badge", paste0("state-", state)),
    shiny::icon(state_icon(state), `aria-hidden` = "true"),
    state_label(state)
  )
}

role_label <- function(role) {
  switch(role %||% "",
    "reviewer" = "Reviewer",
    "approver" = "Approver",
    "administrator" = "Administrator",
    "Read only"
  )
}

role_badge <- function(role) {
  shiny::span(
    class = paste("review-badge role-badge", paste0("role-", role %||% "none")),
    role_label(role)
  )
}

detail_is_editable <- function(role, state) {
  authorize(role, "saved") && state %in% c("draft", "needs-revision")
}

approved_artifact_content <- function(front, persisted_body) {
  join_body(front, persisted_body %||% "")
}

next_step_text <- function(role, state) {
  if (is.null(role)) {
    return("You have read-only access. A repository role mapping is required to act.")
  }
  if (role == "reviewer" && state %in% c("draft", "needs-revision")) {
    return("Edit and save the Markdown, then submit it for approval.")
  }
  if (role == "approver" && state == "in-review") {
    return("Compare the persisted content with its source references, then decide.")
  }
  if (role == "administrator" && state == "approved") {
    return("Inspect the decision history and reopen only when correction is required.")
  }
  if (state == "in-review") {
    return("This artifact is awaiting an approver decision.")
  }
  if (state == "approved") {
    return("This artifact is approved and its review decision is complete.")
  }
  if (state == "needs-revision") {
    return("This artifact is waiting for reviewer revisions.")
  }
  "This artifact is waiting for reviewer submission."
}

permission_text <- function(role, state, dirty = FALSE) {
  if (detail_is_editable(role, state)) {
    if (dirty) {
      return("Save the draft before submitting it for review.")
    }
    return("Save updates without changing status, or submit the saved draft.")
  }
  if (identical(role, "approver") && identical(state, "in-review")) {
    return("Decisions use the persisted reviewed content shown here.")
  }
  if (identical(role, "administrator") && identical(state, "approved")) {
    return("Reopening requires a reason and returns the artifact for revision.")
  }
  "No action is available for your role in this state."
}

parse_frontmatter_summary <- function(front) {
  if (is.null(front) || !nzchar(front)) {
    return(list())
  }
  lines <- strsplit(front, "\n", fixed = TRUE)[[1L]]
  if (length(lines) >= 2L && identical(lines[[1L]], "---")) {
    lines <- lines[-1L]
  }
  if (length(lines) && identical(lines[[length(lines)]], "---")) {
    lines <- lines[-length(lines)]
  }
  tryCatch(
    yaml::read_yaml(text = paste(lines, collapse = "\n")) %||% list(),
    error = function(e) list()
  )
}

display_value <- function(value, empty = "Not specified") {
  if (is.null(value) || length(value) == 0L || all(is.na(value))) {
    return(empty)
  }
  text <- paste(unlist(value, use.names = FALSE), collapse = ", ")
  if (nzchar(text)) text else empty
}

escape_html_text <- function(value) {
  value <- gsub("&", "&amp;", value, fixed = TRUE)
  value <- gsub("<", "&lt;", value, fixed = TRUE)
  value <- gsub(">", "&gt;", value, fixed = TRUE)
  value <- gsub('"', "&quot;", value, fixed = TRUE)
  gsub("'", "&#39;", value, fixed = TRUE)
}

metadata_item <- function(label, value) {
  shiny::div(
    class = "metadata-item",
    shiny::tags$dt(label),
    shiny::tags$dd(display_value(value))
  )
}

context_group <- function(title, ..., open = FALSE, class = NULL) {
  shiny::tags$details(
    class = paste("context-group", class),
    open = if (open) NA else NULL,
    shiny::tags$summary(title),
    shiny::div(class = "context-group-body", ...)
  )
}

action_label <- function(action) {
  switch(action,
    "submitted" = "Submitted for review",
    "request-revision" = "Requested revision",
    "approved" = "Approved artifact",
    "reopened" = "Reopened artifact",
    "saved" = "Saved draft",
    "assigned" = "Updated assignment",
    action
  )
}

activity_timeline <- function(events) {
  if (length(events) == 0L) {
    return(shiny::p(class = "empty-note", "No activity has been recorded yet."))
  }
  newest_first <- rev(events)
  shiny::tags$ol(
    class = "activity-timeline",
    lapply(newest_first, function(event) {
      transition_text <- if (!is.null(event$from_state) &&
                             !is.null(event$to_state)) {
        paste(state_label(event$from_state), "to", state_label(event$to_state))
      } else {
        "Status unchanged"
      }
      shiny::tags$li(
        shiny::div(class = "activity-title", action_label(event$action)),
        shiny::div(class = "activity-transition", transition_text),
        shiny::div(
          class = "activity-meta",
          paste(display_value(event$actor), "as", role_label(event$actor_role)),
          shiny::tags$time(
            datetime = event$occurred_at,
            display_value(event$occurred_at)
          )
        ),
        if (!is.null(event$note) && nzchar(event$note)) {
          shiny::tags$blockquote(event$note)
        }
      )
    })
  )
}

help_workflow <- function(role) {
  switch(role %||% "",
    reviewer = c(
      "Find and filter the item you need.",
      "Read its source references and review history.",
      "Edit the Markdown and compare the preview.",
      "Save the draft, then submit the saved version."
    ),
    approver = c(
      "Filter the queue to In review.",
      "Compare the saved content with its source references.",
      "Request revision with a reason, or approve the artifact.",
      "Verify the updated status and recorded activity."
    ),
    administrator = c(
      "Inspect queue status and artifact history.",
      "Open an approved artifact that requires correction.",
      "Reopen it with a clear reason.",
      "Verify that it returns to Needs revision."
    ),
    c(
      "Browse the queue and open artifacts read only.",
      "Inspect saved content, source references, and activity.",
      "A repository role mapping is required to take action."
    )
  )
}

help_role_summary <- function(role) {
  switch(role %||% "",
    reviewer = "You can edit drafts, save work, and submit saved content for approval.",
    approver = "You can review persisted content, request revisions, or approve it.",
    administrator = "You can inspect all records and reopen approved artifacts for correction.",
    "You can browse saved review information, but you cannot change it."
  )
}

how_to_use_modal <- function(auth) {
  role <- auth$role
  steps <- help_workflow(role)
  shiny::modalDialog(
    title = shiny::div(
      class = "help-modal-title",
      shiny::span("How to use this review workspace"),
      role_badge(role)
    ),
    easyClose = TRUE,
    size = "m",
    footer = shiny::modalButton("Close"),
    shiny::div(
      class = "help-modal-body",
      shiny::p(class = "role-summary", help_role_summary(role)),
      shiny::h3("Your workflow"),
      shiny::tags$ol(lapply(steps, shiny::tags$li)),
      shiny::h3("Status guide"),
      shiny::div(
        class = "status-guide",
        shiny::div(state_badge("draft"), shiny::span("Being prepared by a reviewer.")),
        shiny::div(state_badge("in-review"), shiny::span("Awaiting an approver decision.")),
        shiny::div(state_badge("needs-revision"), shiny::span("Returned for reviewer changes.")),
        shiny::div(state_badge("approved"), shiny::span("Decision complete and recorded."))
      ),
      shiny::h3("Important"),
      shiny::tags$ul(
        shiny::tags$li("YAML metadata is read only."),
        shiny::tags$li("Save does not submit an artifact."),
        shiny::tags$li("Decisions and notes are recorded in activity history."),
        shiny::tags$li("Stale writes never overwrite newer work.")
      ),
      shiny::tags$details(
        class = "other-roles",
        shiny::tags$summary("Other roles"),
        shiny::p("Reviewers edit and submit. Approvers decide. Administrators may reopen approved artifacts. Unmapped identities are read only.")
      )
    )
  )
}
