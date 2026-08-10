# Artifact detail / editor module (Golem mod_ convention).
#
# Renders the detail view for a single CVS draft artifact: read-only YAML
# front-matter, an editable Markdown body with a debounced live preview, and
# role-gated action buttons (submit, request-revision, approve, reopen, save
# draft).  After every successful action the module increments the shared
# `refresh_counter` so the dashboard module reloads the work queue.

#' Detail module UI
#'
#' @param id module namespace ID.
#' @return A dynamic UI placeholder rendered by the server.
#' @export
mod_detail_ui <- function(id) {
  ns <- shiny::NS(id)
  shiny::uiOutput(ns("detail_dynamic"))
}

#' Detail module server
#'
#' @param id module namespace ID (handled automatically by Shiny).
#' @param adapter reactive returning the GitHub adapter handle.
#' @param auth reactive returning the session auth list.
#' @param reactive returning the current role string.
#' @param selected_artifact reactive returning the selected row (one-row
#'   data.frame) from the dashboard module, or NULL.
#' @param refresh_counter shared [shiny::reactiveVal]; incremented after every
#'   successful action to trigger a dashboard reload.
#' @export
mod_detail_server <- function(id, adapter, auth, role, selected_artifact,
                              refresh_counter) {
  shiny::moduleServer(id, function(input, output, session) {

    detail_state <- shiny::reactiveValues(
      artifact_id = NULL,
      front = NULL,
      body = NULL,
      blob_sha = NULL,
      branch_head_sha = NULL,
      body_sha256 = NULL,
      record = NULL
    )

    # ---- detail view render ------------------------------------------------
    output$detail_dynamic <- shiny::renderUI({
      row <- selected_artifact()
      if (is.null(row)) {
        return(shiny::h4("Select an artifact from the work queue."))
      }
      ad <- adapter()
      if (is.null(ad)) {
        stop("no adapter configured; cannot load artifact detail")
      }

      artifact_id <- row$artifact_id
      detail_state$artifact_id <- artifact_id

      draft <- adapter_read_draft(ad, row$source_artifact_path)
      sp <- split_frontmatter(draft$content)

      record_path <- ACTION_PATH(artifact_id)
      record_blob <- adapter_read_review(ad, record_path)
      rec <- parse_review_record(record_blob$content)

      body_text <- sp$body
      companion_path <- BODY_PATH(artifact_id)
      companion <- tryCatch(
        adapter_read_review(ad, companion_path),
        error = function(e) NULL
      )
      if (!is.null(companion)) {
        body_text <- companion$content
      }

      head_sha <- adapter_branch_head(
        ad$owner, ad$repo, ad$review_branch,
        ad$get_token(), ad$http
      )

      detail_state$front <- sp$front
      detail_state$body <- body_text
      detail_state$record <- rec
      detail_state$blob_sha <- record_blob$sha
      detail_state$branch_head_sha <- head_sha
      detail_state$body_sha256 <- hash_body(body_text %||% "")

      input_ok <- !is.null(input$editor_body)
      editor_value <- if (input_ok) input$editor_body else body_text

      ns <- session$ns
      bslib::layout_columns(
        col_widths = c(7, 5),
        bslib::card(
          bslib::card_header(paste("Artifact:", artifact_id)),
          shiny::textAreaInput(
            ns("editor_body"),
            "Markdown body",
            value = editor_value,
            height = "320px"
          ),
          shiny::actionButton(ns("save_draft"), "Save Draft"),
          shiny::div(
            id = ns("action_buttons"),
            shiny::uiOutput(ns("action_buttons"))
          )
        ),
        bslib::card(
          bslib::card_header("Preview"),
          shiny::htmlOutput(ns("preview"))
        )
      )
    })

    # ---- debounced preview (performance: avoids re-render on every keystroke)
    editor_body_reactive <- shiny::reactive({
      input$editor_body %||% ""
    })
    editor_debounced <- shiny::debounce(editor_body_reactive, 300)

    output$preview <- shiny::renderUI({
      shiny::HTML(render_markdown_preview(editor_debounced()))
    })

    # ---- role-gated action buttons -----------------------------------------
    output$action_buttons <- shiny::renderUI({
      r <- role()
      st <- if (!is.null(detail_state$record)) {
        detail_state$record$state
      } else {
        "draft"
      }
      tags <- list()
      if (authorize(r, "submitted") && st %in% c("draft", "needs-revision")) {
        tags[[length(tags) + 1L]] <- shiny::actionButton(
          session$ns("act_submit"),
          "Submit for Review",
          class = "btn-primary"
        )
      }
      if (authorize(r, "request-revision") && st == "in-review") {
        tags[[length(tags) + 1L]] <- shiny::actionButton(
          session$ns("act_reqrev"),
          "Request Revision"
        )
      }
      if (authorize(r, "approved") && st == "in-review") {
        tags[[length(tags) + 1L]] <- shiny::actionButton(
          session$ns("act_approve"),
          "Approve",
          class = "btn-success"
        )
      }
      if (authorize(r, "reopened") && st == "approved") {
        tags[[length(tags) + 1L]] <- shiny::actionButton(
          session$ns("act_reopen"),
          "Reopen (Admin)",
          class = "btn-warning"
        )
      }
      if (length(tags) == 0L) {
        tags[[1L]] <- shiny::p(
          class = "text-muted",
          "No authorized actions for your role in this state."
        )
      }
      shiny::div(tags)
    })

    # ---- action execution --------------------------------------------------
    run_action <- function(action, note = NULL, body = NULL) {
      shiny::req(detail_state$record)
      ad <- adapter()
      tryCatch(
        {
          res <- perform_action(
            ad,
            detail_state$record,
            body_sha256 = if (action == "saved") {
              hash_body(body %||% "")
            } else {
              detail_state$body_sha256
            },
            blob_sha = detail_state$blob_sha,
            branch_head_sha = detail_state$branch_head_sha,
            action = action,
            actor = auth()$identity,
            role = role(),
            approved_content = if (action == "approved") {
              paste0(detail_state$front, "\n", input$editor_body)
            } else {
              NULL
            },
            body = if (action == "saved") body else NULL,
            note = note
          )
          detail_state$record <- res$record
          detail_state$body_sha256 <- hash_body(body %||% detail_state$body %||% "")
          shiny::showNotification(
            recovery_report_text(res$report),
            type = if (res$report$ok) "message" else "error"
          )
          # Signal the dashboard to refresh
          if (res$report$ok) {
            refresh_counter(refresh_counter() + 1L)
          }
        },
        error = function(e) {
          shiny::showNotification(conditionMessage(e), type = "error")
        }
      )
    }

    shiny::observeEvent(input$act_submit, run_action("submitted"))
    shiny::observeEvent(input$act_reqrev, run_action("request-revision"))
    shiny::observeEvent(input$act_approve, run_action("approved"))
    shiny::observeEvent(input$act_reopen, run_action("reopened"))
    shiny::observeEvent(input$save_draft, {
      full <- join_body(detail_state$front %||% "", input$editor_body %||% "")
      if (!frontmatter_unchanged(detail_state$front, full)) {
        shiny::showNotification(
          "YAML front matter must be preserved exactly -- edit rejected.",
          type = "error"
        )
        return()
      }
      run_action("saved", body = input$editor_body %||% "")
    })
  })
}
