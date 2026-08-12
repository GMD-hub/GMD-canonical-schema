# App-level smoke test (Phase 3 + Golem module structure), using shinytest2.
#
# V7 requires app-level checks in addition to unit tests.  This smoke test
# confirms the app boots and renders the dashboard/work-queue surface in a
# local/offline mode.  Module-level adapter wiring is verified in-process via
# shiny::testServer() on the dashboard module with an injected adapter double.

library(testthat)

# Resolve the role-map YAML without hard-failing on missing/installed-package
# layouts: use the package helper first, then the source-tree candidate, and
# return NULL (tests skip) rather than erroring via normalizePath(mustWork).
.smoke_roles_path <- function() {
  roles <- reviewapp::reviewapp_role_map_path()
  if (!is.null(roles)) return(roles)
  cand <- testthat::test_path("..", "..", "config", "roles.yml")
  if (file.exists(cand)) return(cand)
  NULL
}

test_that("dashboard UI renders and the server boots without error", {
  skip_if_not_installed("shinytest2")
  requireNamespace("shinytest2", quietly = TRUE)

  roles <- .smoke_roles_path()
  if (is.null(roles)) {
    skip("role map not found; smoke tests require config/roles.yml")
  }
  withr::local_envvar(
    REVIEW_APP_ROLES = roles,
    REVIEW_APP_OFFLINE = "1"
  )

  app <- shinytest2::AppDriver$new(reviewapp::run_app(), name = "dashboard-smoke")
  app$wait_for_idle()

  page_html <- app$get_html("body")
  expect_true(grepl("Human Review", page_html, fixed = TRUE))
  expect_true(grepl("Review work queue", page_html, fixed = TRUE))
  expect_true(grepl("How to Use", page_html, fixed = TRUE))

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
      entries <- lapply(names(blobs), function(p) list(path = p, type = "blob", sha = paste0("blob-", basename(p))))
      return(list(tree = entries, truncated = FALSE))
    }
    if (grepl("/contents/", url) && method == "GET") {
      path <- sub(".*/contents/(.*)\\?ref=.*", "\\1", url)
      return(list(
        content = base64enc::base64encode(charToRaw(enc2utf8(blobs[[path]]))),
        sha = paste0("blob-", basename(path))
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
  roles <- .smoke_roles_path()
  if (is.null(roles)) {
    skip("role map not found; smoke tests require config/roles.yml")
  }
  withr::local_envvar(REVIEW_APP_ROLES = roles)

  adapter_reactive <- shiny::reactiveVal(fake)
  refresh_counter <- shiny::reactiveVal(0L)

  # Golem modules return their observable state (queue_index, selected_artifact)
  # in a list; testServer does not bind module return values into the test
  # environment, so wrap the module to capture the return list and drive
  # namespaced inputs deterministically.
  dashboard_out <- NULL
  wrapped_dashboard <- function(id, adapter, refresh_counter) {
    shiny::moduleServer(id, function(input, output, session) {
      dashboard_out <<- reviewapp::mod_dashboard_server(
        "dashboard", adapter, refresh_counter
      )
    })
  }

  shiny::testServer(
    wrapped_dashboard,
    args = list(adapter = adapter_reactive, refresh_counter = refresh_counter),
    {
      session$setInputs("dashboard-refresh_queue" = 1L)
      q <- dashboard_out$queue_index()
      expect_true("VAR-male" %in% q$artifact_id)
      expect_identical(q$state[q$artifact_id == "VAR-male"], "draft")

      # Select the row and verify selected_artifact returns it.
      session$setInputs("dashboard-queue_table_rows_selected" = 1L)
      sel <- dashboard_out$selected_artifact()
      expect_false(is.null(sel))
      expect_identical(sel$artifact_id, "VAR-male")
    }
  )
})
