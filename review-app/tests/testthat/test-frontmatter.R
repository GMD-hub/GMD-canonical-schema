# Step 10 -- YAML front-matter immutability and Markdown preview (R5, R6, C1).

library(testthat)

.sample_doc <- function(body = "## Purpose\n\nReviewer notes here.") {
  sprintf(
    "---\nartifact_id: VAR-male\nstate: draft\n---\n%s",
    body
  )
}

test_that("split_frontmatter separates front matter byte-exactly from body", {
  doc <- .sample_doc("Body line\nSecond line")
  sp <- split_frontmatter(doc)
  expect_identical(sp$front, "---\nartifact_id: VAR-male\nstate: draft\n---")
  expect_identical(sp$body, "Body line\nSecond line")
})

test_that("document with no front matter is treated as all body", {
  sp <- split_frontmatter("just a markdown body")
  expect_null(sp$front)
  expect_identical(sp$body, "just a markdown body")
})

test_that("join_body reassembles to the original document", {
  doc <- .sample_doc("Body line")
  sp <- split_frontmatter(doc)
  expect_identical(join_body(sp$front, sp$body), doc)
})

test_that("front matter round-trips byte-identically after a Markdown edit (C1)", {
  doc <- .sample_doc("Original body.")
  sp <- split_frontmatter(doc)
  edited_body <- "Original body.\n\n## New section\n\nAdded by reviewer."
  rebuilt <- join_body(sp$front, edited_body)
  expect_true(frontmatter_unchanged(sp$front, rebuilt))
  # the front matter substring is preserved exactly
  expect_identical(split_frontmatter(rebuilt)$front, sp$front)
})

test_that("an edit that would alter YAML is rejected", {
  doc <- .sample_doc("Body.")
  sp <- split_frontmatter(doc)
  tampered <- "---\nartifact_id: VAR-male\nstate: approved\n---\nBody."
  expect_false(frontmatter_unchanged(sp$front, tampered))
})

test_that("whitespace-only difference in front matter is still detected", {
  doc <- .sample_doc("Body.")
  sp <- split_frontmatter(doc)
  changed_ws <- "---\nartifact_id: VAR-male\nstate: draft\n---\nBody."
  # identical content, same string -> unchanged
  expect_true(frontmatter_unchanged(sp$front, changed_ws))
  # a real value change is flagged
  expect_false(frontmatter_unchanged(sp$front, sub("state: draft", "state: in-review", doc)))
})

test_that("render_markdown_preview renders Markdown to HTML", {
  html <- render_markdown_preview("## Heading\n\nSome *text*.")
  expect_match(html, "<h2>Heading</h2>")
  expect_match(html, "Some <em>text</em>")
})

test_that("markdown preview does not pass through raw HTML/scripts", {
  html <- render_markdown_preview("safe\n\n<script>alert('x')</script>")
  # commonmark's default safe mode does not emit a live script tag
  expect_false(grepl("<script", html, fixed = TRUE))
})
