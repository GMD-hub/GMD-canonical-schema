# Shiny server logic for the Human Review Application.
#
# Phase 1+3: resolves Connect identity to a role (Step 8), builds the
# dashboard/work-queue index (Step 9), renders the artifact detail view with
# read-only YAML/evidence + Markdown editor + preview (Step 10), and wires
# role-gated actions + the audit timeline (Step 11).

#' Server function for the review application.
app_server <- function(input, output, session) {
  # ---- identity / authorization (Step 8) -----------------------------------
  roles_path <- Sys.getenv("REVIEW_APP_ROLES", unset = "")
  if (!nzchar(roles_path)) {
    roles_path <- reviewapp_role_map_path()
  }
  if (is.null(roles_path) || !file.exists(roles_path)) {
    stop("review application requires a role map; set REVIEW_APP_ROLES or ensure a role map is installed")
  }
  auth <- reactiveVal(session_auth(
    connect_identity(session),
    roles_path
  ))
  role <- reactive(auth()$role)

  output$auth_status <- renderText(auth_text(auth()))

  # ---- adapter --------------------------------------------------------------
  # In a real deployment this is built from Connect secrets; for local/dev it
  # is injected. The UI layer talks only through `perform_action` and the
  # index functions, so the storage interface (R20) can be swapped.
  adapter <- reactiveValues()
  # adapter is supplied via a package option / environment in production; the
  # placeholder value here is replaced at deploy time.

  # ---- dashboard / work queue (Step 9) -------------------------------------
  queue_index <- reactiveVal(data.frame())

  load_queue <- function() {
    # TODO(phase3-deploy): wire adapter_index_review to the injected adapter.
    # For local/offline dev (no network) the queue is left empty; the Deployed
    # integration path populates it. See operator guide.
    if (!is.null(adapter$handle)) {
      queue_index(adapter_index_review(adapter$handle)$index)
    } else {
      queue_index(data.frame())
    }
  }

  observeEvent(input$refresh_queue, {
    load_queue()
  })

  output$queue_table <- DT::renderDT({
    index <- queue_index()
    if (nrow(index) == 0L) {
      return(NULL)
    }
    filtered <- filter_review_index(
      index,
      module = input$filter_module,
      state = input$filter_state,
      assigned_to = input$filter_assigned
    )
    filtered$action_required <- vapply(
      filtered$state,
      action_required,
      character(1)
    )
    DT::datatable(
      filtered[, c(
        "artifact_id",
        "state",
        "module",
        "assigned_to",
        "action_required"
      )],
      selection = "single",
      rownames = FALSE,
      options = list(pageLength = 10, dom = "t")
    )
  })

  # ---- navigation --------------------------------------------------------
  output$show_detail <- reactive({
    !is.null(input$queue_table_rows_selected) &&
      nrow(queue_index()) > 0L
  })
  outputOptions(output, "show_detail", suspendWhenHidden = FALSE)

  observeEvent(input$queue_table_rows_selected, {
    shiny::updateTabsetPanel(session, "main_nav", selected = "detail")
  })
  observeEvent(input$nav_detail, {
    shiny::updateTabsetPanel(session, "main_nav", selected = "dashboard")
  })

  # ---- artifact detail view (Step 10) --------------------------------------
  detail_state <- reactiveValues(
    artifact_id = NULL,
    front = NULL,
    body = NULL,
    blob_sha = NULL,
    branch_head_sha = NULL,
    body_sha256 = NULL,
    record = NULL
  )

  output$detail_dynamic <- renderUI({
    sel <- input$queue_table_rows_selected
    idx <- queue_index()
    if (is.null(sel) || nrow(idx) == 0L) {
      return(h4("Select an artifact from the work queue."))
    }
    row <- idx[sel, , drop = FALSE]
    artifact_id <- row$artifact_id
    detail_state$artifact_id <- artifact_id
    # In production, the detail is loaded via the adapter (read-only draft +
    # review record). For local/offline dev the body is a placeholder; the
    # deployed integration populates it. See operator guide.
    detail_state$front <- "---\nartifact_id: " %+%
      artifact_id %+%
      "\nstate: " %+%
      row$state %+%
      "\n---"
    detail_state$body <- "# " %+%
      artifact_id %+%
      "\n\n(Reviewer body -- loaded from the review branch in deployment.)"

    bslib::layout_columns(
      col_widths = c(7, 5),
      bslib::card(
        bslib::card_header(paste("Artifact:", artifact_id)),
        textAreaInput(
          "editor_body",
          "Markdown body",
          value = detail_state$body,
          height = "320px"
        ),
        actionButton("save_draft", "Save Draft"),
        div(id = "action_buttons", uiOutput("action_buttons"))
      ),
      bslib::card(
        bslib::card_header("Preview"),
        htmlOutput("preview")
      )
    )
  })

  output$preview <- renderUI({
    shiny::HTML(render_markdown_preview(input$editor_body %||% ""))
  })

  # ---- role-gated action buttons (Step 11) ---------------------------------
  output$action_buttons <- renderUI({
    r <- role()
    st <- if (!is.null(detail_state$record)) {
      detail_state$record$state
    } else {
      "draft"
    }
    tags <- list()
    if (authorize(r, "submitted") && st %in% c("draft", "needs-revision")) {
      tags[[length(tags) + 1L]] <- actionButton(
        "act_submit",
        "Submit for Review",
        class = "btn-primary"
      )
    }
    if (authorize(r, "request-revision") && st == "in-review") {
      tags[[length(tags) + 1L]] <- actionButton(
        "act_reqrev",
        "Request Revision"
      )
    }
    if (authorize(r, "approved") && st == "in-review") {
      tags[[length(tags) + 1L]] <- actionButton(
        "act_approve",
        "Approve",
        class = "btn-success"
      )
    }
    if (authorize(r, "reopened") && st == "approved") {
      tags[[length(tags) + 1L]] <- actionButton(
        "act_reopen",
        "Reopen (Admin)",
        class = "btn-warning"
      )
    }
    if (length(tags) == 0L) {
      tags[[1L]] <- p(
        class = "text-muted",
        "No authorized actions for your role in this state."
      )
    }
    div(tags)
  })

  run_action <- function(action, note = NULL) {
    req(detail_state$record)
    tryCatch(
      {
        res <- perform_action(
          adapter$handle,
          detail_state$record,
          body_sha256 = detail_state$body_sha256,
          blob_sha = detail_state$blob_sha,
          branch_head_sha = detail_state$branch_head_sha,
          action = action,
          actor = auth()$identity,
          role = role(),
          approved_content = if (action == "approved") {
            detail_state$front %+% "\n" %+% input$editor_body
          } else {
            NULL
          },
          note = note
        )
        detail_state$record <- res$record
        shiny::showNotification(
          recovery_report_text(res$report),
          type = if (res$report$ok) "message" else "error"
        )
        load_queue()
      },
      error = function(e) {
        shiny::showNotification(conditionMessage(e), type = "error")
      }
    )
  }

  observeEvent(input$act_submit, run_action("submitted"))
  observeEvent(input$act_reqrev, run_action("request-revision"))
  observeEvent(input$act_approve, run_action("approved"))
  observeEvent(input$act_reopen, run_action("reopened"))
  observeEvent(input$save_draft, {
    # save-draft is a bookkeeping action (non-transition): reject YAML tampering,
    # then persist the body SHA via the review record.
    full <- join_body(detail_state$front, input$editor_body)
    if (!frontmatter_unchanged(detail_state$front, full)) {
      shiny::showNotification(
        "YAML front matter must be preserved exactly -- edit rejected.",
        type = "error"
      )
      return()
    }
    # In deployment this writes the body via the adapter; local/dev logs only.
    shiny::showNotification("Draft saved (local/dev mode: no write performed).")
  })
}
