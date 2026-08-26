# Dashboard / work-queue module.

#' Dashboard module UI
#'
#' @param id module namespace ID.
#' @return Work-queue page UI.
#' @export
mod_dashboard_ui <- function(id) {
  ns <- shiny::NS(id)
  shiny::div(
    class = "queue-page page-container",
    shiny::div(
      class = "page-heading-row",
      shiny::div(
        shiny::h1("Review work queue"),
        shiny::p(
          class = "page-lead",
          "Find an artifact and open it to review its source, content, and history."
        )
      ),
      shiny::div(
        class = "refresh-area",
        shiny::actionButton(
          ns("refresh_queue"),
          shiny::tagList(
            shiny::icon("rotate", `aria-hidden` = "true"),
            "Refresh"
          ),
          class = "btn btn-outline-primary"
        ),
        shiny::uiOutput(ns("last_refreshed"))
      )
    ),
    shiny::uiOutput(ns("queue_alert")),
    shiny::uiOutput(ns("bootstrap_panel")),
    shiny::uiOutput(ns("queue_telemetry")),
    shiny::uiOutput(ns("status_chips")),
    shiny::div(
      class = "filter-toolbar",
      shiny::textInput(
        ns("filter_artifact"),
        "Artifact ID",
        placeholder = "Search by ID"
      ),
      shiny::uiOutput(ns("filter_module_ui")),
      shiny::selectInput(
        ns("filter_state"),
        "State",
        choices = c(
          "All states" = "",
          "Draft" = "draft",
          "In review" = "in-review",
          "Needs revision" = "needs-revision",
          "Approved" = "approved",
          "Record error" = "ERROR"
        ),
        selected = ""
      ),
      shiny::textInput(
        ns("filter_assigned"),
        "Assignment",
        placeholder = "Identity contains"
      ),
      shiny::selectInput(
        ns("filter_next_step"),
        "Next step",
        choices = c(
          "All next steps" = "",
          "Submit", "Review", "Revise", "Approved", "Repair"
        ),
        selected = ""
      ),
      shiny::uiOutput(ns("clear_filters_ui"))
    ),
    shiny::div(
      class = "queue-results-heading",
      shiny::uiOutput(ns("result_count")),
      shiny::span(class = "queue-hint", "Select a row to open the artifact")
    ),
    shiny::uiOutput(ns("queue_empty")),
    shiny::div(
      class = "queue-table-card",
      role = "region",
      `aria-label` = "Review work queue",
      DT::DTOutput(ns("queue_table"))
    )
  )
}

#' Dashboard module server
#'
#' @param id module namespace ID.
#' @param adapter reactive returning the GitHub adapter handle (or NULL).
#' @param refresh_counter shared [shiny::reactiveVal] used after writes.
#' @return Selected artifact, full queue index, and displayed filtered index.
#' @export
#' @param role reactive role used to guard bootstrap.
#' @param actor_identity reactive authenticated identity.
mod_dashboard_server <- function(
  id,
  adapter,
  refresh_counter,
  role = shiny::reactive(NULL),
  actor_identity = shiny::reactive(NULL)
) {
  shiny::moduleServer(id, function(input, output, session) {
    role_value <- if (is.function(role)) role else shiny::reactive(role)
    actor_value <- if (is.function(actor_identity)) {
      actor_identity
    } else {
      shiny::reactive(actor_identity)
    }
    queue_index <- shiny::reactiveVal(data.frame())
    queue_phase <- shiny::reactiveVal("loading")
    queue_error <- shiny::reactiveVal(NULL)
    queue_mode <- shiny::reactiveVal(NULL)
    queue_manifest <- shiny::reactiveVal(NULL)
    queue_manifest_blob_sha <- shiny::reactiveVal(NULL)
    queue_index_blob_sha <- shiny::reactiveVal(NULL)
    last_refreshed_at <- shiny::reactiveVal(NULL)
    filter_generation <- shiny::reactiveVal(0L)
    queue_startup <- shiny::reactiveVal(NULL)

    clear_selection <- function() {
      proxy <- DT::dataTableProxy("queue_table", session = session)
      try(DT::selectRows(proxy, NULL), silent = TRUE)
    }

    reset_all_filters <- function() {
      shiny::updateTextInput(session, "filter_artifact", value = "")
      shiny::updateSelectInput(session, "filter_module", selected = "")
      shiny::updateSelectInput(session, "filter_state", selected = "")
      shiny::updateTextInput(session, "filter_assigned", value = "")
      shiny::updateSelectInput(session, "filter_next_step", selected = "")
    }

    load_queue <- function() {
      queue_phase("loading")
      session$sendCustomMessage(
        "review-toggle-button",
        list(id = session$ns("refresh_queue"), disabled = TRUE)
      )
      on.exit({
        session$sendCustomMessage(
          "review-toggle-button",
          list(id = session$ns("refresh_queue"), disabled = FALSE)
        )
      }, add = TRUE)

      ad <- shiny::isolate(adapter())
      if (is.null(ad)) {
        queue_index(data.frame())
        queue_error(NULL)
        queue_mode("offline")
        queue_manifest(NULL)
        queue_manifest_blob_sha(NULL)
        queue_index_blob_sha(NULL)
        queue_phase("loaded")
        last_refreshed_at(Sys.time())
        return(invisible(NULL))
      }
      tryCatch(
        {
          loaded <- adapter_index_review(ad)
          queue_index(loaded$index)
          queue_error(loaded$error %||% NULL)
          queue_mode(loaded$mode %||% NULL)
          queue_startup(loaded)
          queue_manifest(loaded$manifest %||% NULL)
          queue_manifest_blob_sha(loaded$manifest_blob_sha %||% NULL)
          queue_index_blob_sha(loaded$index_blob_sha %||% NULL)
          if (!is.null(loaded$request_telemetry)) {
            message(
              "review queue request telemetry: ",
              jsonlite::toJSON(loaded$request_telemetry, auto_unbox = TRUE)
            )
          }
          queue_phase(if (is.null(loaded$error)) "loaded" else "error")
          last_refreshed_at(Sys.time())
          clear_selection()
        },
        error = function(e) {
          queue_error(conditionMessage(e))
          queue_phase("error")
          shiny::showNotification(
            "The work queue could not be refreshed. The previous list is still shown.",
            type = "error",
            duration = 8
          )
        }
      )
      invisible(NULL)
    }

    session$onFlushed(function() load_queue(), once = TRUE)
    shiny::observeEvent(input$refresh_queue, load_queue(), ignoreInit = TRUE)
    shiny::observeEvent(input$retry_queue, load_queue(), ignoreInit = TRUE)
    shiny::observeEvent(refresh_counter(), load_queue(), ignoreInit = TRUE)

    output$last_refreshed <- shiny::renderUI({
      refreshed <- last_refreshed_at()
      if (is.null(refreshed)) {
        return(shiny::span(class = "refresh-time", "Not refreshed yet"))
      }
      shiny::tags$time(
        class = "refresh-time",
        datetime = format(refreshed, "%Y-%m-%dT%H:%M:%SZ", tz = "UTC"),
        paste("Last refreshed", format(refreshed, "%H:%M"))
      )
    })

    output$queue_telemetry <- shiny::renderUI({
      if (!identical(role_value() %||% NULL, "administrator")) return(NULL)
      telemetry <- queue_startup()$request_telemetry %||% NULL
      if (is.null(telemetry)) return(NULL)
      shiny::tags$details(
        class = "queue-telemetry",
        shiny::tags$summary("Queue refresh evidence"),
        shiny::code(sprintf(
          paste(
            "logical_reads=%d actual_attempts=%d",
            "per_record_reads=%d duration_ms=%d"
          ),
          telemetry$logical_reads,
          telemetry$actual_attempts,
          telemetry$per_record_reads,
          telemetry$duration_ms
        ))
      )
    })

    output$queue_alert <- shiny::renderUI({
      if (identical(queue_phase(), "loading")) {
        return(shiny::div(
          class = "app-alert alert-loading",
          role = "status",
          `aria-live` = "polite",
          shiny::span(class = "loading-dot", `aria-hidden` = "true"),
          shiny::div(
            shiny::strong("Loading work queue"),
            shiny::span("Retrieving the latest review records.")
          )
        ))
      }
      if (identical(queue_mode(), "bootstrap_required")) {
        return(shiny::div(
          class = "app-alert alert-warning",
          role = "status",
          shiny::icon("person-circle-exclamation", `aria-hidden` = "true"),
          shiny::div(
            shiny::strong("Production queue bootstrap required"),
            shiny::span("An authenticated administrator must enroll the reviewed source set before the queue can be used."),
            shiny::tags$details(
              shiny::tags$summary("Technical details"),
              shiny::code(queue_error())
            )
          )
        ))
      }
      if (!is.null(queue_error())) {
        stale_text <- if (nrow(queue_index()) > 0L) {
          "The last successful queue remains available and may be out of date."
        } else {
          "No queue data is currently available."
        }
        return(shiny::div(
          class = "app-alert alert-error",
          role = "alert",
          shiny::icon("circle-exclamation", `aria-hidden` = "true"),
          shiny::div(
            shiny::strong("The work queue could not be refreshed"),
            shiny::span(stale_text),
            shiny::tags$details(
              shiny::tags$summary("Technical details"),
              shiny::code(queue_error())
            )
          ),
          shiny::actionButton(
            session$ns("retry_queue"),
            "Retry",
            class = "btn btn-outline-danger btn-sm"
          )
        ))
      }
      NULL
    })

    output$bootstrap_panel <- shiny::renderUI({
      if (!identical(queue_mode(), "bootstrap_required") ||
          !identical(role_value() %||% NULL, "administrator")) {
        return(NULL)
      }
      shiny::div(
        class = "bootstrap-panel app-alert alert-warning",
        shiny::strong("Administrator bootstrap"),
        shiny::p(
          sprintf(
            "Enroll the exact Release A source set: %d artifacts (%s).",
            QUEUE_EXPECTED_TOTAL,
            paste(
              sprintf("%s/%d", names(QUEUE_EXPECTED_MODULE_COUNTS),
                      as.integer(QUEUE_EXPECTED_MODULE_COUNTS)),
              collapse = ", "
            )
          )
        ),
        shiny::actionButton(
          session$ns("bootstrap_queue"),
          "Bootstrap production queue",
          class = "btn btn-warning"
        )
      )
    })

    shiny::observeEvent(input$bootstrap_queue, {
      if (!identical(role_value() %||% NULL, "administrator")) return()
      shiny::showModal(shiny::modalDialog(
        title = "Bootstrap production queue",
        shiny::p(
          sprintf(
            "This creates %d unassigned v2 review records on %s.",
            QUEUE_EXPECTED_TOTAL,
            adapter()$review_branch
          )
        ),
        shiny::p(
          sprintf(
            "Module counts: %s.",
            paste(
              sprintf("%s=%d", names(QUEUE_EXPECTED_MODULE_COUNTS),
                      as.integer(QUEUE_EXPECTED_MODULE_COUNTS)),
              collapse = ", "
            )
          )
        ),
        shiny::p(sprintf(
          "Expected source commit: %s.",
          adapter()$expected_source_commit %||% "not configured"
        )),
        shiny::p("The operation is one atomic commit and cannot be replayed after the manifest exists."),
        footer = shiny::tagList(
          shiny::modalButton("Cancel"),
          shiny::actionButton(
            session$ns("confirm_bootstrap_queue"),
            "Confirm bootstrap",
            class = "btn btn-warning"
          )
        ),
        easyClose = TRUE
      ))
    }, ignoreInit = TRUE)

    shiny::observeEvent(input$confirm_bootstrap_queue, {
      shiny::removeModal()
      ad <- adapter()
      if (is.null(ad)) return()
      tryCatch(
        {
          shiny::withProgress(
            message = "Generating production queue",
            value = 0,
            {
              result <- bootstrap_production_queue(
                ad,
                actor = actor_value() %||% "administrator",
                role = role_value(),
                expected_source_commit = ad$expected_source_commit,
                progress = function(done, total) {
                  shiny::setProgress(value = done / total)
                }
              )
            }
          )
          shiny::showNotification(
            sprintf("Production queue bootstrapped in commit %s.", result$commit_sha),
            type = "message",
            duration = 8
          )
          load_queue()
        },
        error = function(error) {
          shiny::showNotification(
            paste("Production bootstrap was not applied:", conditionMessage(error)),
            type = "error",
            duration = 10
          )
        }
      )
    }, ignoreInit = TRUE)

    output$filter_module_ui <- shiny::renderUI({
      shiny::selectInput(
        session$ns("filter_module"),
        "Module",
        choices = module_filter_choices(queue_index()),
        selected = input$filter_module %||% ""
      )
    })

    filters_active <- shiny::reactive({
      values <- c(
        input$filter_artifact %||% "",
        input$filter_module %||% "",
        input$filter_state %||% "",
        input$filter_assigned %||% "",
        input$filter_next_step %||% ""
      )
      any(nzchar(values))
    })

    filtered_index <- shiny::reactive({
      filter_review_index(
        queue_index(),
        artifact_id = input$filter_artifact,
        module = input$filter_module,
        state = input$filter_state,
        assigned_to = input$filter_assigned,
        next_step = input$filter_next_step
      )
    })

    output$status_chips <- shiny::renderUI({
      index <- queue_index()
      counts <- c(
        all = nrow(index),
        draft = sum(index$state == "draft", na.rm = TRUE),
        `in-review` = sum(index$state == "in-review", na.rm = TRUE),
        `needs-revision` = sum(index$state == "needs-revision", na.rm = TRUE),
        approved = sum(index$state == "approved", na.rm = TRUE),
        ERROR = sum(index$state == "ERROR", na.rm = TRUE)
      )
      selected <- input$filter_state %||% ""
      chip <- function(id, label, state, count) {
        shiny::actionButton(
          session$ns(id),
          shiny::tagList(
            shiny::span(class = "chip-label", label),
            shiny::span(class = "chip-count", count)
          ),
          class = paste(
            "status-chip",
            if (identical(selected, state)) "active" else NULL
          ),
          `aria-pressed` = if (identical(selected, state)) "true" else "false"
        )
      }
      shiny::div(
        class = "status-chips",
        role = "group",
        `aria-label` = "Filter by status",
        chip("chip_all", "All", "", counts[["all"]]),
        chip("chip_draft", "Draft", "draft", counts[["draft"]]),
        chip("chip_review", "In review", "in-review", counts[["in-review"]]),
        chip("chip_revision", "Needs revision", "needs-revision", counts[["needs-revision"]]),
        chip("chip_approved", "Approved", "approved", counts[["approved"]]),
        chip("chip_error", "Errors", "ERROR", counts[["ERROR"]])
      )
    })

    set_state_filter <- function(state) {
      shiny::updateSelectInput(session, "filter_state", selected = state)
    }
    shiny::observeEvent(input$chip_all, set_state_filter(""), ignoreInit = TRUE)
    shiny::observeEvent(input$chip_draft, set_state_filter("draft"), ignoreInit = TRUE)
    shiny::observeEvent(input$chip_review, set_state_filter("in-review"), ignoreInit = TRUE)
    shiny::observeEvent(input$chip_revision, set_state_filter("needs-revision"), ignoreInit = TRUE)
    shiny::observeEvent(input$chip_approved, set_state_filter("approved"), ignoreInit = TRUE)
    shiny::observeEvent(input$chip_error, set_state_filter("ERROR"), ignoreInit = TRUE)

    output$clear_filters_ui <- shiny::renderUI({
      if (!filters_active()) return(NULL)
      shiny::actionButton(
        session$ns("clear_filters"),
        "Clear filters",
        class = "btn btn-link clear-filters"
      )
    })

    shiny::observeEvent(input$clear_filters, {
      reset_all_filters()
    }, ignoreInit = TRUE)

    shiny::observeEvent(
      list(
        input$filter_artifact,
        input$filter_module,
        input$filter_state,
        input$filter_assigned,
        input$filter_next_step
      ),
      {
        filter_generation(filter_generation() + 1L)
        clear_selection()
      },
      ignoreInit = TRUE
    )

    output$result_count <- shiny::renderUI({
      count <- nrow(filtered_index())
      shiny::strong(sprintf("%d %s", count, if (count == 1L) "item" else "items"))
    })

    output$queue_empty <- shiny::renderUI({
      if (identical(queue_phase(), "loading") || nrow(filtered_index()) > 0L) {
        return(NULL)
      }
      if (nrow(queue_index()) == 0L && is.null(queue_error())) {
        return(shiny::div(
          class = "empty-state",
          shiny::icon("inbox", `aria-hidden` = "true"),
          shiny::h2("No review records"),
          shiny::p("The queue does not currently contain any artifacts.")
        ))
      }
      shiny::div(
        class = "empty-state",
        shiny::icon("filter-circle-xmark", `aria-hidden` = "true"),
        shiny::h2("No items match these filters"),
        shiny::p("Adjust the active search, status, module, assignment, or next-step filter."),
        shiny::actionButton(
          session$ns("clear_filters_empty"),
          "Clear filters",
          class = "btn btn-outline-primary"
        )
      )
    })
    shiny::observeEvent(input$clear_filters_empty, {
      reset_all_filters()
    }, ignoreInit = TRUE)

    output$queue_table <- DT::renderDT({
      filtered <- filtered_index()
      if (nrow(filtered) == 0L) return(NULL)
      assignments <- filtered$assigned_to
      assignments[is.na(assignments) | !nzchar(assignments)] <- "Unassigned"
      steps <- vapply(filtered$state, action_required, character(1))
      state_class_map <- c(
        draft = "draft",
        `in-review` = "in-review",
        `needs-revision` = "needs-revision",
        approved = "approved",
        ERROR = "ERROR"
      )
      safe_state_class <- ifelse(
        filtered$state %in% names(state_class_map),
        state_class_map[filtered$state],
        "unknown"
      )
      display <- data.frame(
        control = "",
        Artifact = escape_html_text(filtered$artifact_id),
        Status = sprintf(
          '<span class="table-status state-%s">%s</span>',
          safe_state_class,
          escape_html_text(vapply(filtered$state, state_label, character(1)))
        ),
        Module = escape_html_text(filtered$module),
        `Assigned to` = escape_html_text(assignments),
        Flags = vapply(seq_len(nrow(filtered)), function(i) {
          flags <- character(0)
          if (isTRUE(filtered$governance_blocked[[i]])) {
            flags <- c(flags, "Governance blocked")
          }
          if (isTRUE(filtered$source_drift[[i]])) {
            flags <- c(flags, "Source drift")
          }
          escape_html_text(if (length(flags)) paste(flags, collapse = "; ") else "None")
        }, character(1)),
        `Next step` = sprintf(
          '<span class="next-step-label">%s</span>',
          steps
        ),
        check.names = FALSE,
        stringsAsFactors = FALSE
      )
      DT::datatable(
        display,
        selection = "single",
        rownames = FALSE,
        escape = FALSE,
        extensions = "Responsive",
        class = "compact hover stripe review-queue-table",
        options = queue_table_options()
      )
    })

    list(
      selected_artifact = shiny::reactive({
        req_gen <- filter_generation()
        row <- input$queue_table_rows_selected
        if (is.null(row) || length(row) != 1L) return(NULL)
        if (!identical(filter_generation(), req_gen)) return(NULL)
        selected_review_artifact(filtered_index(), row)
      }),
      queue_index = queue_index,
      filtered_index = filtered_index,
      queue_mode = queue_mode,
      queue_manifest = queue_manifest,
      queue_manifest_blob_sha = queue_manifest_blob_sha,
      queue_index_blob_sha = queue_index_blob_sha,
      queue_startup = queue_startup
    )
  })
}
