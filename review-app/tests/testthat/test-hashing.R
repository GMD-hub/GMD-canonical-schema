# Cross-language SHA-256 parity test (C6).
#
# PY_REFERENCE_SHA256 was generated with:
#   python3 review-app/tests/fixtures/generate_hash_fixture.py
# which hashes review-app/tests/fixtures/hash_fixture.txt via
# extraction_pipeline/hashing.py (generated at 2026-08-04, branch
# feat/human-review-application). If extraction_pipeline/hashing.py's digest
# format ever changes, re-run the generator and update this constant in the
# same commit.

PY_REFERENCE_SHA256 <- "a01d65a9a0e22dbe6735c4f9ca36ae3d42d8d8b50b1ee0062c8ca300925f8e24"

read_fixture_bytes <- function() {
  candidates <- c(
    testthat::test_path("fixtures", "hash_fixture.txt"),
    testthat::test_path("../fixtures", "hash_fixture.txt"),
    file.path("tests", "fixtures", "hash_fixture.txt"),
    file.path("fixtures", "hash_fixture.txt")
  )
  for (p in candidates) {
    if (file.exists(p)) {
      return(readBin(p, "raw", n = file.info(p)$size))
    }
  }
  stop(paste0("hash_fixture.txt not found; looked at: ", paste(candidates, collapse = "; ")))
}

test_that("R hash over the fixture bytes matches the Python digest", {
  bytes <- read_fixture_bytes()
  r_digest <- as.character(openssl::sha256(bytes))
  attributes(r_digest) <- NULL
  expect_identical(r_digest, PY_REFERENCE_SHA256)
})

test_that("hash_body() produces lowercase hex and is stable", {
  body <- "## Some markdown\n\nwith a body."
  d1 <- hash_body(body)
  d2 <- hash_body(body)
  expect_match(d1, "^[0-9a-f]{64}$")
  expect_null(attributes(d1))
  expect_identical(d1, d2)
})

test_that("verify_body_hash() matches via hash_body()", {
  body <- "reviewer body text"
  expect_true(verify_body_hash(body, hash_body(body)))
  expect_false(verify_body_hash(body, hash_body("different text")))
})

test_that("hash_body() rejects invalid input", {
  expect_error(hash_body(NA_character_))
  expect_error(hash_body(character(0)))
})
