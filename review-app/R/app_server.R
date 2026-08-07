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
  # Built from Connect secrets at session start (R3); in local/dev an adapter
  # is injected via `options(reviewapp.adapter)` or `REVIEW_APP_OFFLINE=1`.
  # The UI layer talks only through `perform_action` and the index functions,
  # so the storage interface (R20) can be swapped. Absent env vars fail loudly.
  adapter <- reactiveValues(handle = review_app_adapter())

  # ---- dashboard / work queue (Step 9) -------------------------------------
  queue_index <- reactiveVal(data.frame())

  load_queue <- function() {
    if (!is.null(adapter$handle)) {
      queue_index(adapter_index_review(adapter$handle)$index)
    } else {
      # Offline/injected mode (REVIEW_APP_OFFLINE=1 or injected adapter absent):
      # queue stays empty. Preserves the local/dev smoke test; production always
      # provides a handle (review_app_adapter() fails loudly otherwise).
      queue_index(data.frame())
    }
  }

  observeEvent(input$refresh_queue, {
    load_queue()
  })

  # R10: the module filter is data-driven -- derived from the indexed modules,
  # so dead modules (e.g. empty edu/welfare) never appear and module_id dirs
  # like geo do.
  output$filter_module_ui <- renderUI({
    selectInput(
      "filter_module",
      "Module",
      choices = module_filter_choices(queue_index()),
      selected = ""
    )
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
    # Load via the adapter (R4): draft from the default branch (canonical read-only
    # context), review record + companion body from the review branch.
    if (is.null(adapter$handle)) {
      stop("no adapter configured; cannot load artifact detail")
    }
    draft <- adapter_read_draft(adapter$handle, row$source_artifact_path)
    sp <- split_frontmatter(draft$content)

    record_path <- ACTION_PATH(artifact_id)
    record_blob <- adapter_read_review(adapter$handle, record_path)
    rec <- parse_review_record(record_blob$content)

    # P1.2: the editable body is loaded from the companion file on the review
    # branch when one exists (after a save); otherwise from the source draft.
    body_text <- sp$body
    companion_path <- BODY_PATH(artifact_id)
    companion <- tryCatch(
      adapter_read_review(adapter$handle, companion_path),
      error = function(e) NULL
    )
    if (!is.null(companion)) {
      body_text <- companion$content
    }

    head_sha <- adapter_branch_head(
      adapter$handle$owner, adapter$handle$repo, adapter$handle$review_branch,
      adapter$handle$get_token(), adapter$handle$http
    )

    detail_state$front <- sp$front
    detail_state$body <- body_text
    detail_state$record <- rec
    detail_state$blob_sha <- record_blob$sha
    detail_state$branch_head_sha <- head_sha
    detail_state$body_sha256 <- hash_body(body_text %||% "")
    input_ok <- !is.null(input$editor_body)
    editor_value <- if (input_ok) input$editor_body else body_text

    bslib::layout_columns(
      col_widths = c(7, 5),
      bslib::card(
        bslib::card_header(paste("Artifact:", artifact_id)),
        textAreaInput(
          "editor_body",
          "Markdown body",
          value = editor_value,
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

  run_action <- function(action, note = NULL, body = NULL) {
    req(detail_state$record)
    tryCatch(
      {
        res <- perform_action(
          adapter$handle,
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
            detail_state$front %+% "\n" %+% input$editor_body
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
    # then persist the edited body as a companion file + record a `saved` event.
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
}
