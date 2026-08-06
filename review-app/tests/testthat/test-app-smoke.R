# App-level smoke test (Phase 3 -- dashboard rendering), using shinytest2.
#
# V7 requires app-level checks in addition to unit tests. This smoke test
# confirms the app boots and renders the dashboard/work-queue surface in a
# local/offline mode.
#
# The Server reads the role map from the REVIEW_APP_ROLES env override, which
# we set to an absolute path here so the AppDriver sub-process is deterministic
# regardless of the working directory it starts in (it does not run from the
# package root).

library(shinytest2)
library(testthat)

test_that("dashboard UI renders and the server boots without error", {
  skip_if_not_installed("shinytest2")

  # Resolve the role map to an absolute path (cwd-independent) and hand it to
  # the app sub-process via the documented override.
  roles <- reviewapp::reviewapp_role_map_path()
  if (is.null(roles)) {
    roles <- normalizePath(
      file.path(testthat::test_path("..", "..", "config", "roles.yml"))
    )
  }
  expect_true(file.exists(roles))
  Sys.setenv(REVIEW_APP_ROLES = roles)
  on.exit(Sys.unsetenv("REVIEW_APP_ROLES"), add = TRUE)

  app <- AppDriver$new(reviewapp::run_review_app(), name = "dashboard-smoke")
  app$wait_for_idle()

  # Dashboard / work-queue surface renders. In offline (empty-queue) mode the
  # datatable placeholder still renders, and the title / work-queue header are
  # always present.
  page_html <- app$get_html("body")
  expect_true(grepl("GMD Human Review Application", page_html, fixed = TRUE))
  expect_true(grepl("Work Queue", page_html, fixed = TRUE))
  queue_html <- app$get_html("#queue_table")
  expect_true(grepl("queue_table", queue_html, fixed = TRUE) ||
              grepl("datatables", queue_html, fixed = TRUE))

  # Server resolves the (absent) Connect identity to the unauthenticated state.
  auth_html <- app$get_html("#auth_status")
  expect_true(
    grepl("Not authenticated", auth_html, fixed = TRUE) ||
      grepl("not authorized", auth_html, fixed = TRUE)
  )
  app$stop()
})
