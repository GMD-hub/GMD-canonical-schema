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
app_source(file.path("R", "actions.R"))

testthat::test_that("approved action writes staged approved output", {
  old <- getwd()
  td <- tempfile("country-review-app-test-")
  dir.create(td, recursive = TRUE)
  on.exit(setwd(old), add = TRUE)
  setwd(td)

  source_path <- file.path(
    "extraction", "20_drafts", "runs", "country-parameters", "PER",
    "PARAM-EDU-LEVEL-CROSSWALK.yaml"
  )
  dir.create(dirname(source_path), recursive = TRUE, showWarnings = FALSE)
  writeLines("schema_version: '0.2'\nstatus: draft\n", source_path, useBytes = TRUE)

  item <- list(
    artifact_id = "PARAM-EDU-LEVEL-CROSSWALK_CTY-PER",
    artifact_type = "parameter",
    iso3 = "PER",
    source_artifact_path = source_path
  )
  rec <- load_review_record(item, read_text_file(source_path), actor = "reviewer@example.org")
  rec <- perform_action(item, rec, "schema_version: '0.2'\nstatus: draft\n", "saved", "reviewer@example.org", "reviewer")
  rec <- perform_action(item, rec, "schema_version: '0.2'\nstatus: draft\n", "submitted", "reviewer@example.org", "reviewer")
  rec <- perform_action(item, rec, "schema_version: '0.2'\nstatus: draft\n", "approved", "approver@example.org", "approver")

  approved_path <- approved_path_for(item)
  testthat::expect_true(file.exists(approved_path))
  testthat::expect_identical(rec$state, "approved")
})