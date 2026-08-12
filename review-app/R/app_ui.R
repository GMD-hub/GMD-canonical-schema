# Shiny UI for the Human Review Application (Golem structure).
#
# The top-level page layout composes module UIs.  Navigation and authentication
# status remain at the app level; the dashboard and detail views are provided by
# mod_dashboard and mod_detail respectively.

#' Top-level UI for the review application.
#'
#' @return A fillable bslib page with a compact header and module panels.
#' @export
app_ui <- function() {
  bslib::page_fillable(
    theme = review_app_theme(),
    padding = 0,
    golem_add_external_resources(),
    shiny::div(
      class = "review-app",
      shiny::tags$header(
        class = "app-header",
        shiny::div(
          class = "app-header-inner",
          shiny::div(
            class = "product-identity",
            shiny::span(class = "product-mark", "GMD"),
            shiny::div(
              shiny::div(class = "product-title", "Human Review"),
              shiny::div(class = "product-subtitle", "Canonical Variable Schema")
            )
          ),
          shiny::div(
            class = "header-actions",
            shiny::uiOutput("auth_status"),
            shiny::actionButton(
              "show_help",
              shiny::tagList(
                shiny::icon("circle-question", `aria-hidden` = "true"),
                "How to Use"
              ),
              class = "btn btn-outline-primary help-trigger"
            )
          )
        )
      ),
      shiny::tags$main(
        class = "app-main",
        bslib::navset_hidden(
          id = "main_nav",
          bslib::nav_panel("dashboard", mod_dashboard_ui("dashboard")),
          bslib::nav_panel("detail", mod_detail_ui("detail"))
        )
      )
    )
  )
}
