# Golem application configuration helpers.

#' Resolve a path within the installed package's inst/ directory.
#'
#' @param ... path components passed to [system.file()].
#' @return character(1) absolute path.
#' @export
app_sys <- function(...) {
  system.file(..., package = "reviewapp")
}

#' Read a value from the golem configuration file.
#'
#' The configuration lives at `inst/golem-config.yml` and is read once per
#' session.  The active profile is selected by the `GOLEM_CONFIG_ACTIVE`
#' environment variable (defaults to `"default"`).
#'
#' @param value scalar character key.
#' @param config profile name (default: `Sys.getenv("GOLEM_CONFIG_ACTIVE", "default")`).
#' @return the configuration value, or NULL if absent.
get_golem_config <- function(value,
                             config = Sys.getenv("GOLEM_CONFIG_ACTIVE", "default")) {
  cfg_path <- app_sys("golem-config.yml")
  if (!file.exists(cfg_path)) return(NULL)
  cfg <- yaml::read_yaml(cfg_path)
  if (!is.null(cfg[[config]][[value]])) {
    return(cfg[[config]][[value]])
  }
  cfg[["default"]][[value]]
}

#' Attach external resources (CSS, JS) to the application UI.
#'
#' Called once from [app_ui()] to register the `inst/app/www` asset path and
#' inject the custom stylesheet and local interaction script into the page head.
#'
#' @return An HTML tag list for inclusion in the UI head section.
#' @keywords internal
golem_add_external_resources <- function() {
  shiny::addResourcePath("www", app_sys("app/www"))
  shiny::tags$head(
    shiny::tags$link(
      rel = "stylesheet",
      type = "text/css",
      href = "www/custom.css"
    ),
    shiny::tags$script(
      type = "text/javascript",
      src = "www/review-ui.js"
    )
  )
}

#' Bootstrap theme for the review workspace.
#'
#' @return A Bootstrap 5 bslib theme.
review_app_theme <- function() {
  bslib::bs_theme(
    version = 5,
    bg = "#F4F7FA",
    fg = "#172B3A",
    primary = "#0067B1",
    secondary = "#526675",
    success = "#1F7A4D",
    warning = "#8A5A00",
    danger = "#B42318",
    base_font = bslib::font_collection(
      "Segoe UI", "Helvetica Neue", "Arial", "sans-serif"
    ),
    code_font = bslib::font_collection(
      "ui-monospace", "SFMono-Regular", "Consolas", "monospace"
    ),
    `border-radius` = "0.5rem",
    `border-color` = "#CCD8E1"
  )
}
