helper_candidates <- c(
  file.path("country-review-app", "tests", "testthat", "helper-load.R"),
  file.path("tests", "testthat", "helper-load.R"),
  "helper-load.R"
)
helper_path <- helper_candidates[file.exists(helper_candidates)][1]
if (is.na(helper_path)) {
  stop(sprintf("Unable to locate helper-load.R from current directory: %s", getwd()))
}
source(helper_path, local = TRUE)
app_source(file.path("R", "models.R"))
app_source(file.path("R", "country_queue.R"))

testthat::test_that("queue digest is stable for equal sets", {
  a <- data.frame(
    artifact_id = c("A", "B"),
    source_artifact_path = c("p/1", "p/2"),
    stringsAsFactors = FALSE
  )
  b <- data.frame(
    artifact_id = c("B", "A"),
    source_artifact_path = c("p/2", "p/1"),
    stringsAsFactors = FALSE
  )
  testthat::expect_identical(queue_membership_digest(a), queue_membership_digest(b))
})
