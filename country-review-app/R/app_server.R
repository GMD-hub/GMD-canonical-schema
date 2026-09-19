# Server logic for the country input review app.

app_server <- function(input, output, session) {
  queue_data <- shiny::reactiveVal(build_country_queue_index())
  current_record <- shiny::reactiveVal(NULL)
  current_item <- shiny::reactiveVal(NULL)
  action_status <- shiny::reactiveVal("")

  shiny::observeEvent(input$refresh, {
    queue_data(build_country_queue_index(include_benchmarks = isTRUE(input$include_benchmarks)))
  }, ignoreInit = TRUE)

  shiny::observeEvent(input$include_benchmarks, {
    queue_data(build_country_queue_index(include_benchmarks = isTRUE(input$include_benchmarks)))
  }, ignoreInit = TRUE)

  filtered <- shiny::reactive({
    df <- queue_data()
    if (!nrow(df)) return(df)

    if (!identical(input$filter_type %||% "all", "all")) {
      df <- df[df$artifact_type == input$filter_type, , drop = FALSE]
    }

    iso3_filter <- toupper(trimws(input$filter_iso3 %||% ""))
    if (nzchar(iso3_filter)) {
      df <- df[df$iso3 == iso3_filter, , drop = FALSE]
    }

    df
  })

  shiny::observe({
    df <- filtered()
    choices <- if (nrow(df)) stats::setNames(df$artifact_id, df$artifact_id) else character(0)
    selected <- if (length(choices)) choices[[1L]] else character(0)
    shiny::updateSelectInput(session, "selected_artifact", choices = choices, selected = selected)
  })

  selected_row <- shiny::reactive({
    df <- filtered()
    if (!nrow(df)) return(NULL)
    hit <- df[df$artifact_id == (input$selected_artifact %||% ""), , drop = FALSE]
    if (!nrow(hit)) return(NULL)
    hit[1L, , drop = FALSE]
  })

  shiny::observeEvent(selected_row(), {
    row <- selected_row()
    if (is.null(row)) {
      current_item(NULL)
      current_record(NULL)
      shiny::updateTextAreaInput(session, "editor_body", value = "")
      return()
    }
    item <- as.list(row)
    source_text <- read_text_file(item$source_artifact_path)
    source_text <- source_text %||% ""
    actor <- input$actor_id %||% "reviewer@example.org"

    rec <- tryCatch(
      load_review_record(item, source_text, actor = actor),
      error = function(error) {
        action_status(sprintf("Load record failed: %s", conditionMessage(error)))
        NULL
      }
    )
    current_item(item)
    current_record(rec)

    persisted <- read_text_file(review_body_path(item$artifact_id))
    shiny::updateTextAreaInput(session, "editor_body", value = persisted %||% source_text)
  }, ignoreNULL = FALSE)

  output$queue_summary <- shiny::renderText({
    df <- filtered()
    digest <- attr(df, "membership_digest")
    paste0(
      "Records: ", nrow(df), "\n",
      "Membership digest: ", ifelse(is.null(digest), "n/a", digest)
    )
  })

  output$queue_table <- shiny::renderTable({
    df <- filtered()
    if (!nrow(df)) return(df)
    df[, c("artifact_id", "artifact_type", "iso3", "status", "read_only", "human_reviewed", "parse_error")]
  })

  output$detail_meta <- shiny::renderText({
    item <- current_item()
    rec <- current_record()
    if (is.null(item) || is.null(rec)) {
      return("No artifact selected")
    }
    paste0(
      "Artifact: ", item$artifact_id, "\n",
      "Type: ", item$artifact_type, "\n",
      "ISO3: ", item$iso3, "\n",
      "State: ", rec$state, "\n",
      "Review round: ", rec$review_round, "\n",
      "Source: ", item$source_artifact_path, "\n",
      "Record file: ", review_record_path(item$artifact_id), "\n",
      "Approved path: ", approved_path_for(item)
    )
  })

  run_action <- function(action_name) {
    item <- current_item()
    rec <- current_record()
    if (is.null(item) || is.null(rec)) {
      action_status("No selected artifact")
      return()
    }
    body_text <- input$editor_body %||% ""
    actor <- input$actor_id %||% "reviewer@example.org"
    role <- input$actor_role %||% "reviewer"
    note <- input$action_note %||% NULL

    result <- tryCatch(
      perform_action(item, rec, body_text, action_name, actor, role, note = note),
      error = function(error) error
    )
    if (inherits(result, "error") || inherits(result, "condition")) {
      action_status(sprintf("Action '%s' failed: %s", action_name, conditionMessage(result)))
      return()
    }
    current_record(result)
    action_status(sprintf("Action '%s' completed; state=%s", action_name, result$state))
    queue_data(build_country_queue_index(include_benchmarks = isTRUE(input$include_benchmarks)))
  }

  shiny::observeEvent(input$act_save, run_action("saved"), ignoreInit = TRUE)
  shiny::observeEvent(input$act_submit, run_action("submitted"), ignoreInit = TRUE)
  shiny::observeEvent(input$act_revision, run_action("request-revision"), ignoreInit = TRUE)
  shiny::observeEvent(input$act_approve, run_action("approved"), ignoreInit = TRUE)
  shiny::observeEvent(input$act_reopen, run_action("reopened"), ignoreInit = TRUE)

  output$action_result <- shiny::renderText({
    action_status()
  })
}
