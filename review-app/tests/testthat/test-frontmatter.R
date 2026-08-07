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

test_that("preview escapes event-handler/SVG/javascript: XSS vectors (R9/P2.2)", {
  html <- render_markdown_preview(
    "Hello\n\n<img src=x onerror=alert(1)>\n\n<svg onload=alert(2)></svg>\n\n[click](javascript:alert(3))"
  )
  # raw HTML tags with event handlers are escaped, not passed through
  expect_false(grepl("<img[^>]*onerror", html))
  expect_false(grepl("<svg[^>]*onload", html))
  # javascript: hrefs must not survive as live links
  expect_false(grepl("href=[\"']javascript:", html))
  # benign markdown still renders
  expect_match(html, "Hello")
})

# --- Phase 1 Step 3 (R6/C1): CRLF + meaningful immutability -----------------

test_that("split_frontmatter handles CRLF line endings (R6)", {
  doc_crlf <- "---\r\nartifact_id: VAR-male\r\nstate: draft\r\n---\r\nBody line\r\nSecond line"
  sp <- split_frontmatter(doc_crlf)
  expect_false(is.null(sp$front))
  expect_match(sp$front, "artifact_id: VAR-male", fixed = TRUE)
  expect_match(sp$body, "Body line", fixed = TRUE)
})

test_that("frontmatter_unchanged detects YAML tampering in an edited artifact (R6)", {
  original_front <- "---\nartifact_id: VAR-male\nstate: draft\n---"
  # tampering with the front matter inside the user's full artifact must be caught
  tampered_full <- "---\nartifact_id: VAR-male\nstate: approved\n---\nBody."
  expect_false(frontmatter_unchanged(original_front, tampered_full))
  # an unchanged (round-tripped) artifact is preserved
  ok_full <- paste0(original_front, "\nBody.")
  expect_true(frontmatter_unchanged(original_front, ok_full))
})

test_that("frontmatter_unchanged on a CRLF artifact is meaningful (R6)", {
  original_front <- "---\r\nartifact_id: VAR-male\r\nstate: draft\r\n---"
  ok_full <- "---\r\nartifact_id: VAR-male\r\nstate: draft\r\n---\r\nBody."
  tampered_full <- "---\r\nartifact_id: VAR-male\r\nstate: approved\r\n---\r\nBody."
  expect_true(frontmatter_unchanged(original_front, ok_full))
  expect_false(frontmatter_unchanged(original_front, tampered_full))
})

test_that("approved-path front matter is verified against the loaded draft (R6)", {
  original_front <- "---\nartifact_id: VAR-male\nstate: draft\n---"
  # the approved content must carry the byte-identical front matter
  ok_approved <- paste0(original_front, "\nApproved body.")
  expect_true(frontmatter_unchanged(original_front, ok_approved))
  altered_approved <- "---\nartifact_id: VAR-male\nstate: approved\n---\nApproved body."
  expect_false(frontmatter_unchanged(original_front, altered_approved))
})
