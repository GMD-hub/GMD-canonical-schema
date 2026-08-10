# Shiny server logic for the Human Review Application (Golem structure).
#
# The server resolves Connect identity, builds the GitHub adapter, and
# delegates to Golem modules for the dashboard (mod_dashboard) and detail view
# (mod_detail).  Navigation between panels is handled here since it references
# top-level UI elements.

#' Server function for the review application.
#'
#' @param input Shiny input object.
#' @param output Shiny output object.
#' @param session Shiny session object.
#' @export
app_server <- function(input, output, session) {

  # ---- identity / authorization --------------------------------------------
  roles_path <- Sys.getenv("REVIEW_APP_ROLES", unset = "")
  if (!nzchar(roles_path)) {
    roles_path <- reviewapp_role_map_path()
  }
  if (is.null(roles_path) || !file.exists(roles_path)) {
    stop("review application requires a role map; set REVIEW_APP_ROLES or ensure a role map is installed")
  }
  auth <- shiny::reactiveVal(session_auth(
    connect_identity(session),
    roles_path
  ))
  role <- shiny::reactive(auth()$role)

  output$auth_status <- shiny::renderText(auth_text(auth()))

  # ---- GitHub adapter ------------------------------------------------------
  adapter <- shiny::reactiveVal(review_app_adapter())

  # ---- shared refresh counter (detail module increments after actions) -----
  refresh_counter <- shiny::reactiveVal(0L)

  # ---- dashboard module ----------------------------------------------------
  dashboard <- mod_dashboard_server("dashboard", adapter, refresh_counter)

  # ---- detail module -------------------------------------------------------
  mod_detail_server("detail", adapter, auth, role,
                    dashboard$selected_artifact, refresh_counter)

  # ---- navigation (app-level, controls navset_hidden) ----------------------
  output$show_detail <- shiny::reactive({
    !is.null(dashboard$selected_artifact()) &&
      nrow(dashboard$queue_index()) > 0L
  })
  shiny::outputOptions(output, "show_detail", suspendWhenHidden = FALSE)

  shiny::observeEvent(dashboard$selected_artifact(), {
    if (!is.null(dashboard$selected_artifact())) {
      shiny::updateTabsetPanel(session, "main_nav", selected = "detail")
    }
  })
  shiny::observeEvent(input$nav_detail, {
    shiny::updateTabsetPanel(session, "main_nav", selected = "dashboard")
  })
}
