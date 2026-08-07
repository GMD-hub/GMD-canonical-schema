# Entry point to launch the review application.

#' Build and return the Shiny app object.
#'
#' @export
shiny_review_app <- function(...) {
  shiny::shinyApp(ui = app_ui(), server = app_server, options = list(...))
}

#' Run the review app locally (development helper).
#' @export
run_review_app <- function(...) {
  shiny_review_app(...)
}
