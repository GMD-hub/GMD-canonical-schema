# Entry point to launch the review application (Golem convention).

#' Run the GMD Human Review Application
#'
#' Builds the Shiny app object with [app_ui()] and [app_server] and returns it.
#' This is the standard Golem entry point; Posit Connect deploys via `app.R`
#' which calls this function.
#'
#' @param ... additional options passed to [shiny::shinyApp()].
#' @return A Shiny app object.
#' @export
run_app <- function(...) {
  shiny::shinyApp(ui = app_ui(), server = app_server, options = list(...))
}

#' @export
#' @rdname run_app
shiny_review_app <- run_app

#' Run the review app locally (development helper).
#' @export
#' @rdname run_app
run_review_app <- run_app
