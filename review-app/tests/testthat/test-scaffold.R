# Step 1 -- Scaffold verification: the package namespace loads without error
# and the app skeleton boots.

test_that("package namespace loads without error", {
  expect_true(requireNamespace("reviewapp", quietly = TRUE))
  expect_true(is.function(reviewapp::app_ui))
  expect_true(is.function(reviewapp::app_server))
  expect_true(is.function(reviewapp::run_review_app))
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
