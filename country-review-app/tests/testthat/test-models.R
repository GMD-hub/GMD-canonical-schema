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

testthat::test_that("artifact type detection recognizes parameter", {
  got <- detect_artifact_type_from_path(
    "extraction/20_drafts/runs/country-parameters/PER/PARAM-EDU-LEVEL-CROSSWALK.yaml"
  )
  testthat::expect_identical(got, "parameter")
})

testthat::test_that("artifact type detection recognizes benchmark", {
  got <- detect_artifact_type_from_path("governance/benchmarks/PER_water_benchmark_draft.yaml")
  testthat::expect_identical(got, "benchmark")
})

testthat::test_that("artifact IDs are ISO3-aware for non-benchmarks", {
  got <- build_artifact_id(
    "extraction/20_drafts/runs/country-parameters/PER/PARAM-EDU-LEVEL-CROSSWALK.yaml",
    "parameter",
    "PER"
  )
  testthat::expect_identical(got, "PARAM-EDU-LEVEL-CROSSWALK_CTY-PER")
})
