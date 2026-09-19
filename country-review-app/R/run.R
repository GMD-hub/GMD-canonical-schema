# Runtime entrypoint helpers.

source(file.path("R", "models.R"), local = TRUE)
source(file.path("R", "country_queue.R"), local = TRUE)
source(file.path("R", "authorization.R"), local = TRUE)
source(file.path("R", "state_machine.R"), local = TRUE)
source(file.path("R", "actions.R"), local = TRUE)
source(file.path("R", "app_ui.R"), local = TRUE)
source(file.path("R", "app_server.R"), local = TRUE)

run_app <- function() {
  shiny::shinyApp(ui = app_ui(), server = app_server)
}
