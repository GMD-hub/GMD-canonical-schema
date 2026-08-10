# App-level smoke test (Phase 3 + Golem module structure), using shinytest2.
#
# V7 requires app-level checks in addition to unit tests.  This smoke test
# confirms the app boots and renders the dashboard/work-queue surface in a
# local/offline mode.  Module-level adapter wiring is verified in-process via
# shiny::testServer() on the dashboard module with an injected adapter double.

library(testthat)

test_that("dashboard UI renders and the server boots without error", {
  skip_if_not_installed("shinytest2")
  requireNamespace("shinytest2", quietly = TRUE)

  roles <- reviewapp::reviewapp_role_map_path()
  if (is.null(roles)) {
    roles <- normalizePath(
      file.path(testthat::test_path("..", "..", "config", "roles.yml"))
    )
  }
  expect_true(file.exists(roles))
  Sys.setenv(REVIEW_APP_ROLES = roles)
  Sys.setenv(REVIEW_APP_OFFLINE = "1")
  on.exit(Sys.unsetenv("REVIEW_APP_ROLES"), add = TRUE)
  on.exit(Sys.unsetenv("REVIEW_APP_OFFLINE"), add = TRUE)

  app <- shinytest2::AppDriver$new(reviewapp::run_app(), name = "dashboard-smoke")
  app$wait_for_idle()

  page_html <- app$get_html("body")
  expect_true(grepl("GMD Human Review Application", page_html, fixed = TRUE))
  expect_true(grepl("Work Queue", page_html, fixed = TRUE))

  queue_html <- app$get_html("#dashboard-queue_table")
  expect_true(grepl("queue_table", queue_html, fixed = TRUE) ||
              grepl("datatables", queue_html, fixed = TRUE))

  auth_html <- app$get_html("#auth_status")
  expect_true(
    grepl("Not authenticated", auth_html, fixed = TRUE) ||
      grepl("not authorized", auth_html, fixed = TRUE)
  )
  app$stop()
})

# --- In-memory adapter double for module-level testing -----------------------

.in_mem_adapter_for_smoke <- function() {
  blobs <- list(
    "extraction/20_drafts/dem/VAR-male.md" =
      "---\nartifact_id: VAR-male\nstate: draft\n---\n\n## Definition\n\nReal body.",
    "extraction/30_review/VAR-male.review.yml" =
      "artifact_id: VAR-male\nsource_artifact_path: extraction/20_drafts/dem/VAR-male.md\nstate: draft\nreview_round: 1\nassigned_to: []\ncurrent_content_sha256: a01d65a9a0e22dbe6735c4f9ca36ae3d42d8d8b50b1ee0062c8ca300925f8e24\nsource_commit: source-1\nevents: []\n"
  )
  head <- "head-1"
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/", url) && method == "GET") {
      return(list(object = list(sha = head)))
    }
    if (grepl("git/trees/", url) && method == "GET") {
      entries <- lapply(names(blobs), function(p) list(path = p, type = "blob", sha = "blob-" %+% basename(p)))
      return(list(tree = entries, truncated = FALSE))
    }
    if (grepl("/contents/", url) && method == "GET") {
      path <- sub(".*/contents/(.*)\\?ref=.*", "\\1", url)
      return(list(
        content = base64enc::base64encode(charToRaw(enc2utf8(blobs[[path]]))),
        sha = "blob-" %+% basename(path)
      ))
    }
    if (grepl("git/blobs$", url) && method == "POST") return(list(sha = "new-blob"))
    if (grepl("git/trees$", url) && method == "POST") return(list(sha = "new-tree"))
    if (grepl("git/commits$", url) && method == "POST") return(list(sha = "new-commit"))
    if (grepl("git/refs/heads/", url) && method == "PATCH") return(list(object = list(sha = "new-commit")))
    list(object = list())
  }
  reviewapp::new_github_adapter(
    owner = "GMD-hub", repo = "fixture-repo",
    default_branch = "main", review_branch = "review",
    get_token = function() "tok", http = http_fun
  )
}

test_that("dashboard module loads a queue from an injected adapter", {
  skip_if_not_installed("shiny")
  skip_if_not_installed("bslib")

  fake <- .in_mem_adapter_for_smoke()
  roles <- normalizePath(testthat::test_path("..", "..", "config", "roles.yml"))
  Sys.setenv(REVIEW_APP_ROLES = roles)
  on.exit(Sys.unsetenv("REVIEW_APP_ROLES"), add = TRUE)

  adapter_reactive <- shiny::reactiveVal(fake)
  refresh_counter <- shiny::reactiveVal(0L)

  shiny::testServer(
    reviewapp::mod_dashboard_server,
    args = list(adapter = adapter_reactive, refresh_counter = refresh_counter),
    {
      session$setInputs(refresh_queue = 1L)
      q <- queue_index()
      expect_true("VAR-male" %in% q$artifact_id)
      expect_identical(q$state[q$artifact_id == "VAR-male"], "draft")

      # Select the row and verify selected_artifact returns it
      session$setInputs(queue_table_rows_selected = 1L)
      sel <- selected_artifact()
      expect_false(is.null(sel))
      expect_identical(sel$artifact_id, "VAR-male")
    }
  )
})
