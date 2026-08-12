library(testthat)

test_that("editor availability follows the reviewer and state matrix", {
  expect_true(detail_is_editable("reviewer", "draft"))
  expect_true(detail_is_editable("reviewer", "needs-revision"))
  expect_false(detail_is_editable("reviewer", "in-review"))
  expect_false(detail_is_editable("approver", "in-review"))
  expect_false(detail_is_editable("administrator", "approved"))
  expect_false(detail_is_editable(NULL, "draft"))
})

test_that("approval assembly uses the persisted body", {
  front <- "---\nartifact_id: VAR-male\n---"
  persisted <- "Persisted reviewed content."
  approver_local_text <- "Unsaved approver modification."
  approved <- approved_artifact_content(front, persisted)

  expect_identical(approved, join_body(front, persisted))
  expect_false(grepl(approver_local_text, approved, fixed = TRUE))
})

test_that("role-aware next steps accurately describe permissions", {
  expect_match(next_step_text("reviewer", "draft"), "Edit and save")
  expect_match(next_step_text("approver", "in-review"), "persisted")
  expect_match(next_step_text("administrator", "approved"), "reopen")
  expect_match(next_step_text(NULL, "draft"), "read-only")
})

test_that("front matter summaries expose available source references", {
  front <- paste(
    "---",
    "canonical_label: Example label",
    "module_id: MOD-DEM",
    "rules:",
    "  - RULE-EXAMPLE-001",
    "provenance:",
    "  source_document: source.md",
    "---",
    sep = "\n"
  )
  summary <- parse_frontmatter_summary(front)
  expect_identical(summary$canonical_label, "Example label")
  expect_identical(summary$module_id, "MOD-DEM")
  expect_identical(summary$rules[[1L]], "RULE-EXAMPLE-001")
  expect_identical(summary$provenance$source_document, "source.md")
})
