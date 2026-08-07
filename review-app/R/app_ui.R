# Shiny UI definitions for the Human Review Application.
#
# Phase 1+3 provide the dashboard/work queue (Step 9) and the artifact detail
# view with read-only YAML/evidence panels and a Markdown editor (Step 10),
# plus role-gated action wiring and the audit timeline (Step 11).

#' Top-level UI for the review application.
app_ui <- function() {
  bslib::page_sidebar(
    title = "GMD Human Review Application",
    sidebar = bslib::sidebar(
      title = "Navigation",
      div(id = "auth_panel", uiOutput("auth_status")),
      hr(),
      actionButton("nav_dashboard", "Dashboard / Work Queue", width = "100%"),
      br(),
      br(),
      conditionalPanel(
        condition = "output.show_detail",
        actionButton("nav_detail", "Back to Dashboard", width = "100%")
      )
    ),
    bslib::navset_hidden(
      id = "main_nav",
      bslib::nav_panel(
        "dashboard",
        bslib::card(
          bslib::card_header(
            "Work Queue",
            actionButton("refresh_queue", "Refresh", class = "btn-sm")
          ),
          bslib::layout_columns(
            col_widths = c(6, 6, 6),
            uiOutput("filter_module_ui"),
            selectInput(
              "filter_state",
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
            textInput("filter_assigned", "Assigned to (identity contains)")
          ),
          DT::DTOutput("queue_table")
        )
      ),
      bslib::nav_panel("detail", uiOutput("detail_dynamic"))
    )
  )
}
