# Shiny UI definitions for the Human Review Application.
#
# Phase 1 provides a minimal skeleton that boots locally. Dashboard and
# artifact-detail views are built out in Phase 3 (Steps 9-11).

#' Top-level UI for the review application.
app_ui <- function() {
  bslib::page_sidebar(
    title = "GMD Human Review Application",
    sidebar = bslib::sidebar(
      title = "Navigation",
      "Review workflow placeholder (dashboard arrives in Phase 3)."
    ),
    bslib::card(
      bslib::card_header("Status"),
      "Shiny for R app skeleton. Boots successfully."
    )
  )
}
