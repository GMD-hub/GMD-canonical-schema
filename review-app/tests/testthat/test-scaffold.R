# Step 1 -- Scaffold verification: the package namespace loads without error
# and the app skeleton boots.  Updated for Golem module structure.

test_that("package namespace loads without error", {
  expect_true(requireNamespace("reviewapp", quietly = TRUE))
  expect_true(is.function(reviewapp::app_ui))
  expect_true(is.function(reviewapp::app_server))
  expect_true(is.function(reviewapp::run_app))
})

test_that("golem exports are present", {
  expect_true(is.function(reviewapp::app_sys))
  expect_true(is.function(reviewapp::mod_dashboard_ui))
  expect_true(is.function(reviewapp::mod_dashboard_server))
  expect_true(is.function(reviewapp::mod_detail_ui))
  expect_true(is.function(reviewapp::mod_detail_server))
})

test_that("backward-compatible entry points still work", {
  expect_identical(reviewapp::shiny_review_app, reviewapp::run_app)
  expect_identical(reviewapp::run_review_app, reviewapp::run_app)
})

test_that("core dependencies are resolvable", {
  for (pkg in c("shiny", "bslib", "yaml", "commonmark", "openssl", "testthat")) {
    expect_true(requireNamespace(pkg, quietly = TRUE), info = pkg)
  }
})

test_that("the app skeleton boots to a shiny.appobj", {
  app <- shiny::shinyApp(ui = reviewapp::app_ui(), server = reviewapp::app_server)
  expect_s3_class(app, "shiny.appobj")
})

test_that("app_sys resolves the golem config", {
  cfg_path <- reviewapp::app_sys("golem-config.yml")
  expect_true(file.exists(cfg_path))
})
