source(file.path("R", "models.R"), local = TRUE)
source(file.path("R", "authorization.R"), local = TRUE)
source(file.path("R", "state_machine.R"), local = TRUE)

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