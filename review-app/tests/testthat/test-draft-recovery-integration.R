library(testthat)

.run_detail_recovery_save <- function(outcome) {
  source_content <- paste0(
    "---\nartifact_id: VAR-male\nmodule_id: MOD-DEM\n---\n",
    "body"
  )
  record <- .queue_record_fixture(source_content = source_content)
  record_content <- record_to_yaml(record)
  record_blob_sha <- git_blob_sha(record_content)
  descriptor <- .queue_descriptor_fixture(list(record))
  descriptor_blob_sha <- git_blob_sha(canonical_yaml(descriptor))
  binding <- list(
    status = "current",
    code = "current",
    message = NULL,
    enrolled = list(
      content = source_content,
      sha = record$source_artifact_blob_sha
    )
  )
  adapter <- new_github_adapter(
    owner = "GMD-hub",
    repo = "fixture-repo",
    default_branch = "main",
    review_branch = "fixture-review",
    get_token = function() "unused",
    http = function(...) NULL,
    read_only = FALSE
  )
  local_mocked_bindings(
    adapter_branch_head = function(...) .sha1_fixture_2,
    adapter_read_queue_descriptor = function(...) list(
      descriptor = descriptor,
      content = canonical_yaml(descriptor),
      path = QUEUE_DESCRIPTOR_PATH,
      sha = descriptor_blob_sha
    ),
    adapter_read_review = function(adapter, path) {
      if (identical(path, ACTION_PATH(record$artifact_id))) {
        return(list(content = record_content, sha = record_blob_sha))
      }
      stop("reviewed body does not exist")
    },
    check_source_binding = function(...) binding,
    perform_action = function(...) {
      if (identical(outcome, "exception")) stop("simulated network failure")
      if (identical(outcome, "report-failure")) {
        return(list(report = list(
          ok = FALSE,
          transition_applied = FALSE,
          commit_sha = NULL,
          steps_completed = character(0),
          error = list(
            kind = "stale",
            message = "simulated stale write",
            detail = NULL
          )
        )))
      }
      list(report = list(
        ok = TRUE,
        transition_applied = FALSE,
        commit_sha = .sha1_fixture_2,
        steps_completed = c("staleness-check", "ref-update"),
        error = NULL
      ))
    }
  )

  selected <- shiny::reactiveVal(NULL)
  root_session <- shiny::MockShinySession$new()
  messages <- list()
  root_session$sendCustomMessage <- function(type, message) {
    messages[[length(messages) + 1L]] <<- list(type = type, message = message)
    invisible(NULL)
  }
  shiny::testServer(
    mod_detail_server,
    args = list(
      adapter = shiny::reactiveVal(adapter),
      auth = shiny::reactiveVal(list(identity = "reviewer@example.org")),
      role = shiny::reactiveVal("reviewer"),
      selected_artifact = selected,
      refresh_counter = shiny::reactiveVal(0L),
      queue_mode = shiny::reactiveVal("versioned"),
      queue_descriptor = shiny::reactiveVal(descriptor),
      queue_descriptor_path = shiny::reactiveVal(QUEUE_DESCRIPTOR_PATH),
      queue_descriptor_blob_sha = shiny::reactiveVal(descriptor_blob_sha)
    ),
    session = root_session,
    {
      selected(data.frame(
        artifact_id = record$artifact_id,
        module = "dem",
        source_artifact_path = record$source_artifact_path,
        record_path = ACTION_PATH(record$artifact_id),
        stringsAsFactors = FALSE
      ))
      session$flushReact()
      session$setInputs(editor_body = "changed body")
      session$flushReact()
      session$setInputs(save_draft = 1L)
      session$flushReact()
    }
  )
  Filter(
    function(message) identical(message$type, "review-draft-saved"),
    messages
  )
}

test_that("detail server acknowledges only a successful matching save", {
  messages <- .run_detail_recovery_save("success")
  expect_length(messages, 1L)
  expect_match(messages[[1L]]$message$context_key, "^[0-9a-f]{64}$")
  expect_identical(
    messages[[1L]]$message$saved_body_sha256,
    hash_body("changed body")
  )
})

test_that("detail server preserves recovery after save report failure", {
  expect_length(.run_detail_recovery_save("report-failure"), 0L)
})

test_that("detail server preserves recovery after save exception", {
  expect_length(.run_detail_recovery_save("exception"), 0L)
})
