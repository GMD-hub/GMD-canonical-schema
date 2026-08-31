# Artifact detail / editor module.

#' Detail module UI
#'
#' @param id module namespace ID.
#' @return Artifact review workspace UI.
#' @export
mod_detail_ui <- function(id) {
  ns <- shiny::NS(id)
  shiny::div(
    class = "detail-page page-container",
    shiny::actionButton(
      ns("back_queue"),
      shiny::tagList(
        shiny::icon("arrow-left", `aria-hidden` = "true"),
        "Back to work queue"
      ),
      class = "btn btn-link back-link dirty-navigation-guard"
    ),
    shiny::uiOutput(ns("detail_status")),
    shiny::uiOutput(ns("detail_header")),
    shiny::div(
      class = "detail-layout",
      shiny::tags$aside(
        class = "context-rail",
        `aria-label` = "Artifact context",
        shiny::uiOutput(ns("context_content"))
      ),
      shiny::tags$section(
        class = "content-workspace",
        shiny::div(
          class = "phone-editing-advisory",
          shiny::icon("desktop", `aria-hidden` = "true"),
          "Editing is best on a larger screen."
        ),
        shiny::div(
          class = "workspace-tabs",
          role = "tablist",
          `aria-label` = "Artifact content views",
          shiny::tags$button(
            type = "button",
            class = "workspace-tab active",
            role = "tab",
            `aria-selected` = "true",
            `aria-controls` = ns("editor_panel"),
            `data-review-tab` = "editor",
            "Edit"
          ),
          shiny::tags$button(
            type = "button",
            class = "workspace-tab",
            role = "tab",
            `aria-selected` = "false",
            `aria-controls` = ns("preview_panel"),
            `data-review-tab` = "preview",
            "Preview"
          )
        ),
        shiny::div(
          class = "editor-preview-grid",
          shiny::tags$section(
            id = ns("editor_panel"),
            class = "workspace-panel editor-panel active",
            role = "tabpanel",
            shiny::div(
              class = "panel-heading",
              shiny::div(
                shiny::h2("Markdown content"),
                shiny::p(
                  "YAML metadata is read only and is preserved automatically."
                )
              ),
              shiny::uiOutput(ns("save_indicator"))
            ),
            shiny::uiOutput(ns("draft_recovery")),
            shiny::uiOutput(ns("editor_surface"))
          ),
          shiny::tags$section(
            id = ns("preview_panel"),
            class = "workspace-panel preview-panel",
            role = "tabpanel",
            shiny::div(
              class = "panel-heading",
              shiny::div(
                shiny::h2("Preview"),
                shiny::p("Rendered from the content currently shown in the editor.")
              )
            ),
            shiny::htmlOutput(ns("preview"))
          )
        ),
        shiny::uiOutput(ns("action_feedback")),
        shiny::uiOutput(ns("action_bar"))
      )
    )
  )
}

#' Detail module server
#'
#' @param id module namespace ID.
#' @param adapter reactive returning the GitHub adapter handle.
#' @param auth reactive returning the session auth list.
#' @param role reactive returning the current role string.
#' @param selected_artifact reactive returning the selected queue row.
#' @param refresh_counter shared [shiny::reactiveVal] incremented after writes.
#' @param queue_mode reactive queue routing mode.
#' @param queue_descriptor reactive current queue descriptor.
#' @param queue_descriptor_path reactive descriptor compatibility path.
#' @param queue_descriptor_blob_sha reactive descriptor blob SHA.
#' @return A list containing the back-navigation event reactive.
#' @export
mod_detail_server <- function(id, adapter, auth, role, selected_artifact,
                               refresh_counter,
                               queue_mode = shiny::reactive("legacy_read_only"),
                               queue_descriptor = shiny::reactive(NULL),
                               queue_descriptor_path = shiny::reactive(NULL),
                               queue_descriptor_blob_sha = shiny::reactive(NULL)) {
  shiny::moduleServer(id, function(input, output, session) {
    detail_state <- shiny::reactiveValues(
      phase = "idle",
      error = NULL,
      action_error = NULL,
      action_success = NULL,
      report = NULL,
      selected_row = NULL,
      artifact_id = NULL,
      front = NULL,
      metadata = list(),
      body = NULL,
      blob_sha = NULL,
      branch_head_sha = NULL,
      body_sha256 = NULL,
      record = NULL,
      source_binding = NULL,
      source_drift = FALSE,
      source_drift_status = "unchecked",
      source_drift_code = NULL,
      source_drift_reason = NULL,
      enrolled_source = NULL,
      descriptor_path = NULL,
      descriptor_blob_sha = NULL
    )

    load_detail <- function(row = detail_state$selected_row) {
      if (is.null(row)) return(invisible(NULL))
      detail_state$phase <- "loading"
      detail_state$error <- NULL
      detail_state$action_error <- NULL
      detail_state$action_success <- NULL
      session$sendCustomMessage("review-dirty-state", list(dirty = FALSE))

      tryCatch(
        {
          ad <- shiny::isolate(adapter())
          if (is.null(ad)) {
            stop("No repository adapter is configured.")
          }
           artifact_id <- row$artifact_id[[1L]]
            record_path <- row$record_path[[1L]] %||% ACTION_PATH(artifact_id)
          record_blob <- adapter_read_review(ad, record_path)
           record <- parse_review_record(record_blob$content)
           source_binding <- NULL
            if (is_v2_review_record(record)) {
              source_binding <- check_source_binding(ad, record)
              if (is.null(source_binding$enrolled$content)) {
                stop(sprintf(
                  "enrolled source is unavailable: %s",
                  source_binding$message %||% source_binding$code
                ))
              }
              snapshot <- source_binding$enrolled$content
             split <- split_frontmatter_exact(snapshot)
             body_text <- split$body
           } else {
             draft <- adapter_read_draft(ad, row$source_artifact_path[[1L]])
             split <- split_frontmatter(draft$content)
             body_text <- split$body
           }
           companion <- tryCatch(
            adapter_read_review(ad, BODY_PATH(artifact_id)),
            error = function(e) NULL
          )
          if (!is.null(companion)) body_text <- companion$content
           head_sha <- adapter_branch_head(
            ad$owner,
            ad$repo,
            ad$review_branch,
            ad$get_token(),
            ad$http
          )

          detail_state$artifact_id <- artifact_id
          detail_state$front <- split$front
          detail_state$metadata <- parse_frontmatter_summary(split$front)
          detail_state$body <- body_text
          detail_state$record <- record
          detail_state$blob_sha <- record_blob$sha
          detail_state$branch_head_sha <- head_sha
           detail_state$body_sha256 <- hash_body(body_text %||% "")
           detail_state$source_binding <- source_binding
            detail_state$source_drift <- !is.null(source_binding) &&
              !source_binding_is_current(source_binding)
            detail_state$source_drift_status <- source_binding$status %||% "unchecked"
            detail_state$source_drift_code <- source_binding$code %||% NULL
            detail_state$source_drift_reason <- source_binding$message %||% NULL
            detail_state$enrolled_source <- source_binding$enrolled %||% NULL
            detail_state$descriptor_path <- queue_descriptor_path() %||% NULL
            detail_state$descriptor_blob_sha <-
              queue_descriptor_blob_sha() %||% NULL
            if (is_v2_review_record(record) &&
                is.null(detail_state$descriptor_blob_sha)) {
              control <- adapter_read_queue_descriptor(ad)
              detail_state$descriptor_path <- control$path
              detail_state$descriptor_blob_sha <- control$sha
            }
           detail_state$phase <- "loaded"
        },
        error = function(e) {
          detail_state$error <- conditionMessage(e)
          detail_state$phase <- "error"
        }
      )
      invisible(NULL)
    }

    shiny::observeEvent(selected_artifact(), {
      row <- selected_artifact()
      if (is.null(row)) return()
      detail_state$selected_row <- row
      load_detail(row)
    }, ignoreNULL = TRUE)
    shiny::observeEvent(input$retry_detail, load_detail(), ignoreInit = TRUE)

    current_state <- shiny::reactive({
      if (is.null(detail_state$record)) "draft" else detail_state$record$state
    })
    queue_read_only <- shiny::reactive({
      queue_mode() %in% c(
        "legacy_read_only",
        "production_v2_read_only",
        "descriptor_v1_0_read_only"
      )
    })
    editable <- shiny::reactive({
      detail_is_editable(role(), current_state()) &&
        !queue_read_only()
    })
    dirty <- shiny::reactive({
      if (!editable() || !identical(detail_state$phase, "loaded")) {
        return(FALSE)
      }
      !identical(input$editor_body %||% "", detail_state$body %||% "")
    })
    dirty_debounced <- shiny::debounce(dirty, 500)

    shiny::observe({
      session$sendCustomMessage(
        "review-dirty-state",
        list(dirty = isTRUE(dirty_debounced()))
      )
    })

    current_draft_recovery_context <- function(ad = adapter()) {
      actor <- auth()$identity
      if (!is_v2_review_record(detail_state$record) ||
          !.is_scalar_character(actor)) {
        return(NULL)
      }
      draft_recovery_context(
        adapter = ad,
        record = detail_state$record,
        actor = actor,
        base_body_sha256 = detail_state$body_sha256,
        base_record_blob_sha = detail_state$blob_sha
      )
    }

    output$detail_status <- shiny::renderUI({
      if (identical(detail_state$phase, "loading")) {
        return(shiny::div(
          class = "detail-loading",
          role = "status",
          `aria-live` = "polite",
          shiny::span(class = "loading-dot", `aria-hidden` = "true"),
          "Loading artifact context and review history."
        ))
      }
      if (identical(detail_state$phase, "error")) {
        return(shiny::div(
          class = "app-alert alert-error detail-error",
          role = "alert",
          shiny::icon("circle-exclamation", `aria-hidden` = "true"),
          shiny::div(
            shiny::strong("This artifact could not be loaded"),
            shiny::span("Retry the read or return to the work queue."),
            shiny::tags$details(
              shiny::tags$summary("Technical details"),
              shiny::code(detail_state$error)
            )
          ),
          shiny::actionButton(
            session$ns("retry_detail"),
            "Retry",
            class = "btn btn-outline-danger btn-sm"
          )
        ))
      }
      if (identical(detail_state$phase, "loaded") &&
          isTRUE(detail_state$source_drift)) {
        return(shiny::div(
          class = "app-alert alert-warning detail-error",
          role = "alert",
          shiny::icon("triangle-exclamation", `aria-hidden` = "true"),
          shiny::div(
            shiny::strong("Source drift detected"),
            shiny::span(
              paste(
                "This view uses the enrolled source snapshot.",
                "Reviewers can save and submit it, but approval stays blocked.",
                "An administrator can explicitly re-enroll a verified source."
              )
            ),
            shiny::tags$details(
              shiny::tags$summary("Technical details"),
              shiny::code(sprintf(
                "%s: %s",
                detail_state$source_drift_code %||% "unresolved",
                detail_state$source_drift_reason %||%
                  "source changed or could not be verified"
              ))
            )
          )
        ))
      }
      NULL
    })

    output$detail_header <- shiny::renderUI({
      if (!identical(detail_state$phase, "loaded")) return(NULL)
      record <- detail_state$record
      module <- detail_state$metadata$module_id %||%
        detail_state$selected_row$module[[1L]]
      assignment <- display_value(record$assigned_to, "Unassigned")
      shiny::tags$header(
        class = "detail-header",
        shiny::div(
          class = "detail-title-row",
          shiny::h1(detail_state$artifact_id),
          state_badge(record$state)
        ),
        shiny::div(
          class = "detail-facts",
          shiny::span(shiny::strong("Module"), module),
          shiny::span(shiny::strong("Review round"), record$review_round),
          shiny::span(shiny::strong("Assigned to"), assignment)
        ),
        shiny::p(
          class = "next-step-sentence",
          shiny::icon("arrow-right", `aria-hidden` = "true"),
          next_step_text(role(), record$state)
        )
      )
    })

    output$context_content <- shiny::renderUI({
      if (!identical(detail_state$phase, "loaded")) return(NULL)
      meta <- detail_state$metadata
      record <- detail_state$record
      provenance <- meta$provenance %||% list()
      source_items <- list(
        metadata_item("Source document", provenance$source_document),
        metadata_item("Source section", provenance$source_section),
        metadata_item("Rules", meta$rules),
        metadata_item("Exceptions", meta$exceptions)
      )
      shiny::div(
        class = "context-groups",
        context_group(
          "Overview",
          shiny::tags$dl(
            class = "metadata-list",
            metadata_item(
              "Canonical label",
              meta$canonical_label %||% meta$label
            ),
            metadata_item(
              "Variable name",
              meta$variable_name %||% meta$name
            ),
            metadata_item("Module", meta$module_id %||% meta$module),
            metadata_item("Tier", meta$tier),
            metadata_item("Data type", meta$data_type),
            metadata_item("Unit", meta$unit %||% meta$unit_of_analysis),
            metadata_item("Current state", state_label(record$state)),
            metadata_item("Review round", record$review_round),
            metadata_item(
              "Assigned to",
              display_value(record$assigned_to, "Unassigned")
            )
          ),
          open = TRUE
        ),
        context_group(
          "Source and evidence",
          shiny::p(
            class = "context-note",
            "References available in the artifact metadata. No source excerpt is stored here."
          ),
          shiny::tags$dl(class = "metadata-list", source_items),
          open = TRUE
        ),
        context_group(
          "Raw YAML",
          shiny::span(class = "read-only-label", "Read only"),
          shiny::tags$pre(
            class = "raw-yaml",
            shiny::code(detail_state$front %||% "No YAML front matter")
          )
        ),
        context_group(
          "Activity",
          activity_timeline(record$events),
          open = length(record$events) > 0L
        )
      )
    })

    output$editor_surface <- shiny::renderUI({
      if (!identical(detail_state$phase, "loaded")) return(NULL)
      if (editable()) {
        return(shiny::textAreaInput(
          session$ns("editor_body"),
          label = NULL,
          value = detail_state$body %||% "",
          width = "100%",
          height = "60vh",
          placeholder = "Enter Markdown content"
        ))
      }
      shiny::div(
        class = "read-only-markdown",
        `aria-label` = "Persisted Markdown content, read only",
        shiny::tags$pre(shiny::code(detail_state$body %||% ""))
      )
    })

    output$draft_recovery <- shiny::renderUI({
      if (!identical(detail_state$phase, "loaded")) return(NULL)
      context <- current_draft_recovery_context()
      if (is.null(context)) return(NULL)
      draft_recovery_controls(
        context,
        session$ns("editor_body"),
        editable = editable()
      )
    })

    preview_source <- shiny::reactive({
      if (editable()) input$editor_body %||% "" else detail_state$body %||% ""
    })
    preview_debounced <- shiny::debounce(preview_source, 300)
    output$preview <- shiny::renderUI({
      if (!identical(detail_state$phase, "loaded")) return(NULL)
      shiny::HTML(render_markdown_preview(preview_debounced()))
    })

    output$save_indicator <- shiny::renderUI({
      if (!identical(detail_state$phase, "loaded")) return(NULL)
      if (!editable()) {
        return(shiny::span(
          class = "save-indicator read-only",
          shiny::icon("lock", `aria-hidden` = "true"),
          "Persisted, read only"
        ))
      }
      if (dirty()) {
        return(shiny::span(
          class = "save-indicator unsaved",
          shiny::icon("circle", `aria-hidden` = "true"),
          "Unsaved changes"
        ))
      }
      shiny::span(
        class = "save-indicator saved",
        shiny::icon("circle-check", `aria-hidden` = "true"),
        "Saved"
      )
    })

    refresh_write_metadata <- function(ad) {
      record_blob <- adapter_read_review(
        ad,
        ACTION_PATH(detail_state$artifact_id)
      )
         detail_state$record <- parse_review_record(record_blob$content)
      detail_state$blob_sha <- record_blob$sha
         detail_state$branch_head_sha <- adapter_branch_head(
        ad$owner,
        ad$repo,
        ad$review_branch,
        ad$get_token(),
        ad$http
         )
          if (is_v2_review_record(detail_state$record)) {
            detail_state$source_binding <- check_source_binding(ad, detail_state$record)
            detail_state$source_drift <-
              !source_binding_is_current(detail_state$source_binding)
            detail_state$source_drift_status <-
              detail_state$source_binding$status %||% "unverifiable"
            detail_state$source_drift_code <-
              detail_state$source_binding$code %||% NULL
            detail_state$source_drift_reason <-
              detail_state$source_binding$message %||% NULL
            control <- adapter_read_queue_descriptor(
              ad,
              detail_state$descriptor_path
            )
            detail_state$descriptor_path <- control$path
            detail_state$descriptor_blob_sha <- control$sha
          }
    }

      run_action <- function(action, note = NULL, body = NULL,
                             candidate_source_commit = NULL) {
      shiny::req(detail_state$record)
      detail_state$action_error <- NULL
      detail_state$action_success <- NULL
      detail_state$report <- NULL
      ad <- adapter()
      recovery_ack <- if (identical(action, "saved")) {
        context <- current_draft_recovery_context(ad)
        if (is.null(context)) NULL else draft_recovery_save_ack(
          context,
          body %||% ""
        )
      } else {
        NULL
      }
      tryCatch(
        {
          approved_content <- if (identical(action, "approved")) {
            approved_artifact_content(
              detail_state$front,
              detail_state$body
            )
          } else {
            NULL
          }
          result <- perform_action(
            ad,
            detail_state$record,
            body_sha256 = if (identical(action, "saved")) {
              hash_body(body %||% "")
            } else {
              detail_state$body_sha256
            },
            blob_sha = detail_state$blob_sha,
            branch_head_sha = detail_state$branch_head_sha,
            action = action,
            actor = auth()$identity,
            role = role(),
            approved_content = approved_content,
            body = if (identical(action, "saved")) body else NULL,
            note = note,
            expected_descriptor_blob_sha = detail_state$descriptor_blob_sha,
            descriptor_path = detail_state$descriptor_path,
            legacy_read_only = queue_read_only(),
            candidate_source_commit = candidate_source_commit
          )
          detail_state$report <- result$report
          if (!result$report$ok) {
            detail_state$action_error <- recovery_report_text(result$report)
            indeterminate <- identical(
              result$report$error$kind,
              "indeterminate"
            )
            shiny::showNotification(
              if (indeterminate) {
                "Publication could not be confirmed. Do not retry until an operator reconciles the branch."
              } else {
                "The change was not applied. Review the recovery message below."
              },
              type = "error",
              duration = 8
            )
            return(invisible(FALSE))
          }

          if (identical(action, "saved")) {
            detail_state$body <- body %||% ""
            detail_state$body_sha256 <- hash_body(detail_state$body)
          }
          refresh_error <- tryCatch(
            {
              if (identical(action, "source-revision")) {
                load_detail()
                if (identical(detail_state$phase, "error")) {
                  stop(detail_state$error %||% "detail refresh failed")
                }
              } else {
                refresh_write_metadata(ad)
              }
              NULL
            },
            error = function(error) conditionMessage(error)
          )
          if (!is.null(recovery_ack)) {
            session$sendCustomMessage("review-draft-saved", recovery_ack)
          }
          success_message <- switch(action,
            saved = "Draft saved. Its status did not change.",
            submitted = "Artifact submitted for approval.",
            `request-revision` = "Revision requested and reason recorded.",
            approved = "Artifact approved from the persisted reviewed content.",
            reopened = paste(
              "Artifact reopened and returned for revision.",
              "The active approved output was retired."
            ),
            `source-revision` = if (isTRUE(result$replay)) {
              "The selected source revision is already enrolled. No new event was added."
            } else {
              "The verified source revision was enrolled and prior assessment data was reset."
            },
            "Change recorded."
          )
          detail_state$action_success <- if (is.null(refresh_error)) {
            success_message
          } else {
            paste(
              success_message,
              "The change was applied, but the refreshed repository state could not be loaded.",
              refresh_error
            )
          }
          session$sendCustomMessage("review-dirty-state", list(dirty = FALSE))
          refresh_counter(refresh_counter() + 1L)
          shiny::showNotification(
            detail_state$action_success,
            type = if (is.null(refresh_error)) "message" else "warning",
            duration = 6
          )
          invisible(TRUE)
        },
        error = function(e) {
          detail_state$action_error <- conditionMessage(e)
          shiny::showNotification(
            "The change was not applied. Your local content is still available.",
            type = "error",
            duration = 8
          )
          invisible(FALSE)
        }
      )
    }

    output$action_feedback <- shiny::renderUI({
      if (!is.null(detail_state$action_success)) {
        return(shiny::div(
          class = "app-alert alert-success action-feedback",
          role = "status",
          `aria-live` = "polite",
          shiny::icon("circle-check", `aria-hidden` = "true"),
          shiny::div(
            shiny::strong("Change recorded"),
            shiny::span(detail_state$action_success)
          )
        ))
      }
      if (!is.null(detail_state$action_error)) {
        report <- detail_state$report
        stale <- !is.null(report) && !is.null(report$error) &&
          identical(report$error$kind, "stale")
        indeterminate <- !is.null(report) && !is.null(report$error) &&
          identical(report$error$kind, "indeterminate")
        return(shiny::div(
          class = "app-alert alert-error action-feedback",
          role = "alert",
          shiny::icon("circle-exclamation", `aria-hidden` = "true"),
          shiny::div(
            shiny::strong(if (indeterminate) {
              "Publication could not be confirmed"
            } else {
              "The change was not applied"
            }),
            shiny::span(detail_state$action_error),
            if (!is.null(report) && !is.null(report$error$detail)) {
              shiny::tags$details(
                shiny::tags$summary("Technical details"),
                shiny::code(report$error$detail)
              )
            }
          ),
          if (stale) {
            shiny::actionButton(
              session$ns("reload_latest"),
              "Reload latest",
              class = "btn btn-outline-danger btn-sm"
            )
          }
        ))
      }
      NULL
    })

    output$action_bar <- shiny::renderUI({
      if (!identical(detail_state$phase, "loaded")) return(NULL)
      state <- current_state()
      current_role <- role()
      actions <- list()
      if (detail_is_editable(current_role, state) && !queue_read_only()) {
        actions[[length(actions) + 1L]] <- shiny::actionButton(
          session$ns("save_draft"),
          "Save Draft",
          class = "btn btn-outline-primary",
          disabled = !dirty()
        )
        actions[[length(actions) + 1L]] <- shiny::actionButton(
          session$ns("act_submit"),
          "Submit for review",
          class = "btn btn-primary",
          disabled = dirty(),
          title = if (dirty()) "Save draft before submitting." else NULL
        )
      }
      if (authorize(current_role, "request-revision") &&
          state == "in-review" && !queue_read_only()) {
        actions[[length(actions) + 1L]] <- shiny::actionButton(
          session$ns("act_reqrev"),
          "Request revision",
          class = "btn btn-outline-secondary"
        )
      }
      approval_eligible <- if (is.null(queue_descriptor())) {
        FALSE
      } else {
        isTRUE(tryCatch(
          queue_approval_eligible(
            detail_state$record,
            detail_state$source_binding,
            queue_descriptor()
          ),
          error = function(error) FALSE
        ))
      }
      if (authorize(current_role, "approved") && state == "in-review" &&
          !isTRUE(detail_state$source_drift) && !queue_read_only() &&
          approval_eligible) {
        actions[[length(actions) + 1L]] <- shiny::actionButton(
          session$ns("act_approve"),
          "Approve",
          class = "btn btn-success"
        )
      }
      if (authorize(current_role, "source-revision") &&
          !identical(state, "approved") && !queue_read_only()) {
        actions[[length(actions) + 1L]] <- shiny::actionButton(
          session$ns("act_source_revision"),
          "Re-enroll source",
          class = "btn btn-outline-secondary"
        )
      }
      if (authorize(current_role, "reopened") &&
          identical(state, "approved") && !queue_read_only()) {
        actions[[length(actions) + 1L]] <- shiny::actionButton(
          session$ns("act_reopen"),
          "Reopen and retire output",
          class = "btn btn-danger"
        )
      }
      shiny::div(
        class = "action-bar",
        shiny::div(
          class = "action-explanation",
          shiny::strong(if (editable()) {
            if (dirty()) "Unsaved changes" else "Saved"
          } else {
            "Permissions"
          }),
          shiny::span(permission_text(current_role, state, dirty()))
        ),
        shiny::div(class = "action-buttons", actions)
      )
    })

    show_confirmation <- function(kind) {
      artifact_id <- detail_state$artifact_id
      state <- state_label(current_state())
      modal <- switch(kind,
        submit = shiny::modalDialog(
          title = "Submit for review",
          easyClose = TRUE,
          shiny::p(
            shiny::strong(artifact_id),
            sprintf("will move from %s to In review.", state)
          ),
          shiny::p("Only the saved Markdown content will be submitted."),
          footer = shiny::tagList(
            shiny::modalButton("Cancel"),
            shiny::actionButton(
              session$ns("confirm_submit"),
              "Submit for review",
              class = "btn btn-primary"
            )
          )
        ),
        approve = shiny::modalDialog(
          title = "Approve artifact",
          easyClose = TRUE,
          shiny::p(
            shiny::strong(artifact_id),
            "will be written to",
            shiny::code(approved_path_for(detail_state$record$source_artifact_path)),
            "using the persisted reviewed body."
          ),
          shiny::textAreaInput(
            session$ns("approval_note"),
            "Approval note (optional)",
            rows = 3
          ),
          footer = shiny::tagList(
            shiny::modalButton("Cancel"),
            shiny::actionButton(
              session$ns("confirm_approve"),
              "Approve artifact",
              class = "btn btn-success"
            )
          )
        ),
        revision = shiny::modalDialog(
          title = "Request revision",
          easyClose = TRUE,
          shiny::p(
            shiny::strong(artifact_id),
            "will move to Needs revision. Explain what must change."
          ),
          shiny::textAreaInput(
            session$ns("revision_note"),
            "Reason for revision",
            rows = 4
          ),
          shiny::uiOutput(session$ns("revision_note_error")),
          footer = shiny::tagList(
            shiny::modalButton("Cancel"),
            shiny::actionButton(
              session$ns("confirm_revision"),
              "Request revision",
              class = "btn btn-primary"
            )
          )
        ),
        reopen = shiny::modalDialog(
          title = "Reopen approved artifact",
          easyClose = TRUE,
          shiny::p(
            shiny::strong(artifact_id),
            "will move to Needs revision. Its active approved output will be deleted in the same Git commit."
          ),
          shiny::textAreaInput(
            session$ns("reopen_note"),
            "Reason for reopen",
            rows = 4
          ),
          shiny::uiOutput(session$ns("reopen_note_error")),
          footer = shiny::tagList(
            shiny::modalButton("Cancel"),
            shiny::actionButton(
              session$ns("confirm_reopen"),
              "Reopen and retire output",
              class = "btn btn-danger"
            )
          )
        ),
        source_revision = shiny::modalDialog(
          title = "Re-enroll source revision",
          easyClose = TRUE,
          shiny::p(
            shiny::strong(artifact_id),
            "will keep its queue membership and use the same source path. Enter an immutable commit SHA."
          ),
          shiny::textInput(
            session$ns("source_revision_commit"),
            "Candidate source commit"
          ),
          shiny::textAreaInput(
            session$ns("source_revision_note"),
            "Reason for source revision",
            rows = 4
          ),
          shiny::uiOutput(session$ns("source_revision_error")),
          footer = shiny::tagList(
            shiny::modalButton("Cancel"),
            shiny::actionButton(
              session$ns("confirm_source_revision"),
              "Verify and re-enroll",
              class = "btn btn-primary"
            )
          )
        )
      )
      shiny::showModal(modal)
    }

    shiny::observeEvent(input$save_draft, {
      if (!editable() || !dirty()) return()
      body <- input$editor_body %||% ""
      full <- join_body(detail_state$front, body)
      if (!frontmatter_unchanged(detail_state$front, full)) {
        detail_state$action_error <-
          "YAML front matter must be preserved exactly. No write occurred."
        return()
      }
      run_action("saved", body = body)
    }, ignoreInit = TRUE)
    shiny::observeEvent(input$act_submit, {
      if (editable() && !dirty()) show_confirmation("submit")
    }, ignoreInit = TRUE)
    shiny::observeEvent(input$act_reqrev, show_confirmation("revision"), ignoreInit = TRUE)
    shiny::observeEvent(input$act_approve, show_confirmation("approve"), ignoreInit = TRUE)
    shiny::observeEvent(input$act_reopen, show_confirmation("reopen"), ignoreInit = TRUE)
    shiny::observeEvent(
      input$act_source_revision,
      show_confirmation("source_revision"),
      ignoreInit = TRUE
    )

    output$revision_note_error <- shiny::renderUI({
      clicks <- input$confirm_revision %||% 0L
      if (clicks < 1L ||
          nzchar(trimws(input$revision_note %||% ""))) return(NULL)
      shiny::p(class = "field-error", role = "alert", "Enter a reason before requesting revision.")
    })
    output$reopen_note_error <- shiny::renderUI({
      clicks <- input$confirm_reopen %||% 0L
      if (clicks < 1L || nzchar(trimws(input$reopen_note %||% ""))) {
        return(NULL)
      }
      shiny::p(
        class = "field-error",
        role = "alert",
        "Enter a reason before reopening the artifact."
      )
    })
    output$source_revision_error <- shiny::renderUI({
      clicks <- input$confirm_source_revision %||% 0L
      if (clicks < 1L) return(NULL)
      commit <- trimws(input$source_revision_commit %||% "")
      reason <- trimws(input$source_revision_note %||% "")
      messages <- c(
        if (!.is_sha1(commit)) "Enter a lowercase 40-character commit SHA.",
        if (!nzchar(reason)) "Enter a reason for the source revision."
      )
      if (!length(messages)) return(NULL)
      shiny::p(class = "field-error", role = "alert", paste(messages, collapse = " "))
    })

    shiny::observeEvent(input$confirm_submit, {
      shiny::removeModal()
      run_action("submitted")
    }, ignoreInit = TRUE)
    shiny::observeEvent(input$confirm_approve, {
      note <- trimws(input$approval_note %||% "")
      shiny::removeModal()
      run_action("approved", note = if (nzchar(note)) note else NULL)
    }, ignoreInit = TRUE)
    shiny::observeEvent(input$confirm_revision, {
      note <- trimws(input$revision_note %||% "")
      if (!nzchar(note)) return()
      shiny::removeModal()
      run_action("request-revision", note = note)
    }, ignoreInit = TRUE)
    shiny::observeEvent(input$confirm_reopen, {
      note <- trimws(input$reopen_note %||% "")
      if (!nzchar(note)) return()
      shiny::removeModal()
      run_action("reopened", note = note)
    }, ignoreInit = TRUE)
    shiny::observeEvent(input$confirm_source_revision, {
      commit <- trimws(input$source_revision_commit %||% "")
      note <- trimws(input$source_revision_note %||% "")
      if (!.is_sha1(commit) || !nzchar(note)) return()
      shiny::removeModal()
      run_action(
        "source-revision",
        note = note,
        candidate_source_commit = commit
      )
    }, ignoreInit = TRUE)
    shiny::observeEvent(input$reload_latest, {
      shiny::showModal(shiny::modalDialog(
        title = "Reload latest content?",
        easyClose = TRUE,
        shiny::p(
          "Reloading replaces this local view with the latest saved repository version."
        ),
        footer = shiny::tagList(
          shiny::modalButton("Keep local view"),
          shiny::actionButton(
            session$ns("confirm_reload"),
            "Reload latest",
            class = "btn btn-danger"
          )
        )
      ))
    }, ignoreInit = TRUE)
    shiny::observeEvent(input$confirm_reload, {
      shiny::removeModal()
      load_detail()
    }, ignoreInit = TRUE)

    list(
      back_requested = shiny::reactive(input$back_queue)
    )
  })
}
