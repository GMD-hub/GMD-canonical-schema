# Runtime entrypoint helpers.

resolve_app_root <- function() {
  cwd <- normalizePath(getwd(), winslash = "/", mustWork = TRUE)
  candidates <- c(
    cwd,
    file.path(cwd, "country-review-app"),
    dirname(cwd)
  )
  candidates <- unique(candidates)
  for (root in candidates) {
    if (file.exists(file.path(root, "R", "models.R")) &&
        file.exists(file.path(root, "R", "app_server.R"))) {
      return(root)
    }
    if (file.exists(file.path(root, "country-review-app", "R", "models.R")) &&
        file.exists(file.path(root, "country-review-app", "R", "app_server.R"))) {
      return(file.path(root, "country-review-app"))
    }
  }
  stop(sprintf(
    "Unable to locate country-review-app root from working directory: %s",
    cwd
  ))
}

app_source <- function(relative_path) {
  source(file.path(resolve_app_root(), relative_path), local = parent.frame())
}

app_source(file.path("R", "models.R"))
app_source(file.path("R", "country_queue.R"))
app_source(file.path("R", "authorization.R"))
app_source(file.path("R", "state_machine.R"))
app_source(file.path("R", "actions.R"))
app_source(file.path("R", "app_ui.R"))
app_source(file.path("R", "app_server.R"))

run_app <- function() {
  if (!requireNamespace("shiny", quietly = TRUE)) {
    stop(
      paste(
        "Package 'shiny' is required.",
        "Install it with:",
        "install.packages('shiny', repos='https://cloud.r-project.org')"
      )
    )
  }
  shiny::shinyApp(ui = app_ui(), server = app_server)
}
