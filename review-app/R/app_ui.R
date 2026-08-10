# Shiny UI for the Human Review Application (Golem structure).
#
# The top-level page layout composes module UIs.  Navigation and authentication
# status remain at the app level; the dashboard and detail views are provided by
# mod_dashboard and mod_detail respectively.

#' Top-level UI for the review application.
#'
#' @return A bslib page with sidebar navigation and module panels.
#' @export
app_ui <- function() {
  shiny::tagList(
    golem_add_external_resources(),
    bslib::page_sidebar(
      title = "GMD Human Review Application",
      sidebar = bslib::sidebar(
        title = "Navigation",
        shiny::div(id = "auth_panel", shiny::uiOutput("auth_status")),
        shiny::hr(),
        shiny::actionButton("nav_dashboard", "Dashboard / Work Queue", width = "100%"),
        shiny::br(),
        shiny::br(),
        shiny::conditionalPanel(
          condition = "output.show_detail",
          shiny::actionButton("nav_detail", "Back to Dashboard", width = "100%")
        )
      ),
      bslib::navset_hidden(
        id = "main_nav",
        bslib::nav_panel("dashboard", mod_dashboard_ui("dashboard")),
        bslib::nav_panel("detail", mod_detail_ui("detail"))
      )
    )
  )
}
