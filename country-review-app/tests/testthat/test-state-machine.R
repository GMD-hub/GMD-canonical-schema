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
app_source(file.path("R", "authorization.R"))
app_source(file.path("R", "state_machine.R"))

testthat::test_that("transition enforces role and state rules", {
  item <- list(
    artifact_id = "PARAM-EDU-LEVEL-CROSSWALK_CTY-PER",
    artifact_type = "parameter",
    iso3 = "PER",
    source_artifact_path = "extraction/20_drafts/runs/country-parameters/PER/PARAM-EDU-LEVEL-CROSSWALK.yaml"
  )
  rec <- new_review_record(item, "a: 1\n")

  testthat::expect_error(
    transition(rec, "approved", "approver@example.org", "approver"),
    "illegal transition"
  )

  submitted <- transition(rec, "submitted", "reviewer@example.org", "reviewer")
  testthat::expect_identical(submitted$state, "in-review")

  approved <- transition(submitted, "approved", "approver@example.org", "approver")
  testthat::expect_identical(approved$state, "approved")
})