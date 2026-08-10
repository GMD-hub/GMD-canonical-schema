# Dashboard / work-queue module (Golem mod_ convention).
#
# Encapsulates the work-queue table, its data-driven module/state/assignment
# filters, and the refresh action.  The parent server passes a shared
# `refresh_counter` reactiveVal so that other modules (e.g. mod_detail after a
# successful action) can trigger a queue reload without tight coupling.

#' Dashboard module UI
#'
#' @param id module namespace ID.
#' @return bslib::card containing filters and the DT output.
#' @export
mod_dashboard_ui <- function(id) {
  ns <- shiny::NS(id)
  bslib::card(
    bslib::card_header(
      "Work Queue",
      shiny::actionButton(ns("refresh_queue"), "Refresh", class = "btn-sm")
    ),
    bslib::layout_columns(
      col_widths = c(6, 6, 6),
      shiny::uiOutput(ns("filter_module_ui")),
      shiny::selectInput(
        ns("filter_state"),
        "State",
        choices = c(
          "All" = "",
          "draft",
          "in-review",
          "needs-revision",
          "approved"
        ),
        selected = ""
      ),
      shiny::textInput(ns("filter_assigned"), "Assigned to (identity contains)")
    ),
    DT::DTOutput(ns("queue_table"))
  )
}

#' Dashboard module server
#'
#' @param id module namespace ID (handled automatically by Shiny).
#' @param adapter reactive returning the GitHub adapter handle (or NULL).
#' @param refresh_counter shared [shiny::reactiveVal]; increment to trigger a
#'   queue reload from another module.
#' @return A named list:
#'   - `selected_artifact`: reactive returning the selected row as a one-row
#'     data.frame, or NULL when nothing is selected.
#'   - `queue_index`: the reactiveVal holding the current index data.frame.
#' @export
mod_dashboard_server <- function(id, adapter, refresh_counter) {
  shiny::moduleServer(id, function(input, output, session) {

    queue_index <- shiny::reactiveVal(data.frame())

    load_queue <- function() {
      ad <- adapter()
      if (!is.null(ad)) {
        queue_index(adapter_index_review(ad)$index)
      } else {
        queue_index(data.frame())
      }
    }

    # Refresh on button click or when another module increments the counter
    shiny::observeEvent(input$refresh_queue, {
      load_queue()
    })
    shiny::observeEvent(refresh_counter(), {
      load_queue()
    }, ignoreInit = TRUE)

    # Data-driven module filter (R10): dead modules never appear.
    output$filter_module_ui <- shiny::renderUI({
      shiny::selectInput(
        session$ns("filter_module"),
        "Module",
        choices = module_filter_choices(queue_index()),
        selected = ""
      )
    })

    output$queue_table <- DT::renderDT({
      index <- queue_index()
      if (nrow(index) == 0L) return(NULL)

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

    # --- return values for the parent server --------------------------------
    list(
      selected_artifact = shiny::reactive({
        sel <- input$queue_table_rows_selected
        idx <- queue_index()
        if (is.null(sel) || nrow(idx) == 0L) return(NULL)
        idx[sel, , drop = FALSE]
      }),
      queue_index = queue_index
    )
  })
}
