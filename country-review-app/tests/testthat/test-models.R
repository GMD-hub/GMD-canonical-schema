source(file.path("R", "models.R"), local = TRUE)

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
