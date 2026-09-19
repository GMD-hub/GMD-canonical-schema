# UI for the country input review app.

app_ui <- function() {
  shiny::fluidPage(
    shiny::titlePanel("Country Input Review App"),
    shiny::fluidRow(
      shiny::column(
        width = 4,
        shiny::checkboxInput("include_benchmarks", "Include benchmark references", TRUE),
        shiny::selectInput("filter_type", "Artifact type", choices = c("all", ARTIFACT_TYPES), selected = "all"),
        shiny::textInput("filter_iso3", "ISO3 filter", value = ""),
        shiny::selectInput("actor_role", "Role", choices = ROLES, selected = "reviewer"),
        shiny::textInput("actor_id", "Actor", value = "reviewer@example.org"),
        shiny::selectInput("selected_artifact", "Artifact", choices = character(0)),
        shiny::actionButton("refresh", "Refresh queue")
      ),
      shiny::column(
        width = 8,
        shiny::verbatimTextOutput("queue_summary"),
        shiny::tableOutput("queue_table"),
        shiny::tags$hr(),
        shiny::verbatimTextOutput("detail_meta"),
        shiny::textAreaInput("editor_body", "Artifact content", value = "", rows = 18),
        shiny::textInput("action_note", "Action note", value = ""),
        shiny::fluidRow(
          shiny::column(2, shiny::actionButton("act_save", "Save")),
          shiny::column(2, shiny::actionButton("act_submit", "Submit")),
          shiny::column(2, shiny::actionButton("act_revision", "Needs revision")),
          shiny::column(2, shiny::actionButton("act_approve", "Approve")),
          shiny::column(2, shiny::actionButton("act_reopen", "Reopen"))
        ),
        shiny::verbatimTextOutput("action_result")
      )
    )
  )
}
