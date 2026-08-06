# YAML front-matter handling (Step 10 / R5, R6, C1).
#
# CVS drafts are Markdown files with a YAML front-matter block delimited by
# `---` at the top. The app preserves the front matter BYTE-EXACTLY across
# edits: only the Markdown body is editable. `split_frontmatter()` separates
# the raw blocks so they can be reassembled unchanged; `reserialize()` checks
# that a save round-trips the front matter to a byte-identical string.

#' Split a full artifact string into its front-matter and body blocks.
#'
#' Expects a leading `---\n...\n---\n` block. The front matter is returned raw
#' (including its delimiters) so it can be preserved byte-exactly. If no front
#' matter is present, front is NULL and the whole document is treated as body.
#'
#' @param text full artifact text.
#' @return list(front = raw frontmatter string incl. delimiters or NULL,
#'   body = remaining Markdown body).
split_frontmatter <- function(text) {
  # front matter delimited by a leading --- line and a closing --- line
  lines <- strsplit(text, "\n", fixed = TRUE)[[1L]]
  if (length(lines) >= 3L && identical(lines[[1L]], "---")) {
    close <- which(lines[-1L] == "---")[1L]
    if (!is.na(close)) {
      end <- close + 1L  # index in original (line 1 = open; close-th from line 2)
      front <- paste0(lines[seq_len(end)], collapse = "\n")
      body <- if (end < length(lines)) paste0(lines[(end + 1L):length(lines)], collapse = "\n") else ""
      return(list(front = front, body = body))
    }
  }
  list(front = NULL, body = text)
}

#' Reassemble an artifact from a (possibly edited) body and the ORIGINAL front
#' matter, preserving the front matter byte-exactly.
#'
#' @param front raw front-matter string (as returned by split_frontmatter).
#' @param body edited Markdown body.
#' @return full artifact string.
join_body <- function(front, body) {
  if (is.null(front)) return(body)
  paste0(front, "\n", body)
}

#' Check that a proposed full artifact preserves the front matter byte-exactly.
#'
#' A "structural alteration" (front matter changed at all) must be rejected
#' (R6 / C1). Returns TRUE if the reassembled front matter is byte-identical to
#' the reference; otherwise FALSE.
#'
#' @param original_front raw front-matter of the loaded artifact.
#' @param proposed full proposed artifact text.
#' @return logical(1).
frontmatter_unchanged <- function(original_front, proposed) {
  if (is.null(original_front)) return(TRUE)
  split_frontmatter(proposed)$front == original_front
}

#' Render the Markdown body as HTML for preview (commonmark, safe default).
#'
#' Uses `commonmark::markdown_html(text, extensions = TRUE)` with its default
#' safe rendering so raw HTML/script tags in the source Markdown are not passed
#' through. No smart/raw-HTML-passthrough option is enabled.
#'
#' @param markdown character(1) Markdown body text.
#' @return character(1) HTML string.
render_markdown_preview <- function(markdown) {
  out <- commonmark::markdown_html(markdown, extensions = TRUE)
  paste0('<div class="markdown-body">', out, "</div>")
}
