# App-level smoke test (Phase 3 -- dashboard rendering), using shinytest2.
#
# V7 requires app-level checks in addition to unit tests. This smoke test
# confirms the app boots and renders the dashboard/work-queue surface in a
# local/offline mode. The Phase 5 (R3/R4/R5) adapter wiring is additionally
# verified in-process via `shiny::testServer()` with an injected adapter double
# at the bottom of this file, so it runs even where shinytest2 is absent.
#
# The Server reads the role map from the REVIEW_APP_ROLES env override, which
# we set to an absolute path here so the AppDriver sub-process is deterministic
# regardless of the working directory it starts in (it does not run from the
# package root).

library(testthat)

test_that("dashboard UI renders and the server boots without error", {
  skip_if_not_installed("shinytest2")
  requireNamespace("shinytest2", quietly = TRUE)

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
  # Offline mode: no Connect secrets in the smoke harness, so the adapter is
  # intentionally absent and the queue stays empty.
  Sys.setenv(REVIEW_APP_OFFLINE = "1")
  on.exit(Sys.unsetenv("REVIEW_APP_ROLES"), add = TRUE)
  on.exit(Sys.unsetenv("REVIEW_APP_OFFLINE"), add = TRUE)

  app <- shinytest2::AppDriver$new(reviewapp::run_review_app(), name = "dashboard-smoke")
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

# --- Phase 5 (R3/R4/R5): adapter wiring, in-process via testServer -------------

.in_mem_adapter_for_smoke <- function() {
  # minimal in-memory double: one draft + one review record on the review branch
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

test_that("server loads a real queue and detail with an injected adapter (R3/R4)", {
  skip_if_not_installed("shiny")

  fake <- .in_mem_adapter_for_smoke()
  op <- getOption("reviewapp.adapter")
  options(reviewapp.adapter = fake)
  on.exit(options(reviewapp.adapter = op), add = TRUE)
  withr::local_envvar(
    REVIEW_APP_OFFLINE = "",
    REVIEW_APP_GH_OWNER = "",
    REVIEW_APP_GH_REPO = "",
    REVIEW_APP_GH_DEFAULT_BRANCH = "",
    REVIEW_APP_GH_REVIEW_BRANCH = ""
  )
  roles <- normalizePath(testthat::test_path("..", "..", "config", "roles.yml"))
  Sys.setenv(REVIEW_APP_ROLES = roles)
  on.exit(Sys.unsetenv("REVIEW_APP_ROLES"), add = TRUE)

  withr::local_envvar(REVIEW_APP_USER = "reviewer@example.org")

  shiny::testServer(reviewapp::app_server, {
    # review_app_adapter() picks up the injected option -> non-null handle
    expect_s3_class(adapter$handle, "reviewapp_github_adapter")
    # clicking Refresh populates the queue from the review branch
    session$setInputs(refresh_queue = 1L)
    q <- queue_index()
    expect_true("VAR-male" %in% q$artifact_id)
    expect_identical(q$state[q$artifact_id == "VAR-male"], "draft")
    # selecting the row loads real front matter + body via the adapter
    session$setInputs(queue_table_rows_selected = 1L)
    expect_identical(detail_state$artifact_id, "VAR-male")
    expect_match(detail_state$front, "artifact_id: VAR-male", fixed = TRUE)
    expect_match(detail_state$body, "## Definition", fixed = TRUE)
    expect_identical(record_state(detail_state$record), "draft")
    expect_false(is.null(detail_state$blob_sha))
  })
})
