source(file.path("R", "models.R"), local = TRUE)
source(file.path("R", "country_queue.R"), local = TRUE)

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
