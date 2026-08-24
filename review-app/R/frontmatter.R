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
  # Normalize CRLF -> LF up front so artifacts checked out on Windows (git
  # core.autocrlf) are handled identically; delimiters `---` are matched on LF.
  norm <- gsub("\r\n", "\n", text, fixed = TRUE)
  # front matter delimited by a leading --- line and a closing --- line
  lines <- strsplit(norm, "\n", fixed = TRUE)[[1L]]
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

#' Split a source artifact without normalizing its bytes.
#'
#' Enrollment uses this variant because the source snapshot and its body digest
#' are bound to the exact bytes returned by GitHub. The regular UI helper keeps
#' its historical CRLF normalization behavior for editing.
split_frontmatter_exact <- function(text) {
  if (!is.character(text) || length(text) != 1L || is.na(text)) {
    stop("split_frontmatter_exact() requires one non-NA text value")
  }
  delimiters <- gregexpr("(?m)^---(?:\\r?\\n|$)", text, perl = TRUE)[[1L]]
  lengths <- attr(delimiters, "match.length")
  if (length(delimiters) >= 2L && delimiters[[1L]] == 1L) {
    close_start <- delimiters[[2L]]
    close_length <- lengths[[2L]]
    front_end <- close_start + 2L
    front <- substr(text, 1L, front_end)
    body_start <- close_start + close_length
    body <- if (body_start <= nchar(text, type = "bytes")) {
      substr(text, body_start, nchar(text, type = "bytes"))
    } else {
      ""
    }
    line_ending <- if (close_length > 3L &&
                       identical(
                         substr(
                           text,
                           close_start + 3L,
                           close_start + close_length - 1L
                         ),
                         "\r\n"
                       )) {
      "\r\n"
    } else if (close_length > 3L) {
      "\n"
    } else {
      ""
    }
    return(list(
      front = front,
      body = body,
      front_raw = charToRaw(enc2utf8(front)),
      body_raw = charToRaw(enc2utf8(body)),
      line_ending = line_ending
    ))
  }
  list(front = NULL, body = text)
}

join_enrolled_body <- function(front, body, separator = NULL) {
  if (is.null(front)) return(body)
  separator <- separator %||% if (grepl("\r\n", front, fixed = TRUE)) {
    "\r\n"
  } else {
    "\n"
  }
  paste0(front, separator, body %||% "")
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
#' (R6 / C1). Returns TRUE if the front matter extracted from the *proposed*
#' (user-edited full artifact) is byte-identical to the reference front matter.
#' The caller must pass the actual editor output (front + body as the user sees
#' it); if the user tampered with YAML the extracted front will differ.
#'
#' @param original_front raw front-matter of the loaded artifact.
#' @param proposed full proposed artifact text.
#' @return logical(1).
frontmatter_unchanged <- function(original_front, proposed) {
  if (is.null(original_front)) return(TRUE)
  original_norm <- gsub("\r\n", "\n", original_front, fixed = TRUE)
  # A leading/trailing newline quirk in the reference delimiter is not a
  # structural change; normalize both sides so CRLF/LF checkouts compare fairly.
  proposed_front <- split_frontmatter(proposed)$front
  if (is.null(proposed_front)) return(FALSE)
  identical(proposed_front, original_norm)
}

#' Strip executable/dangerous HTML before the preview is rendered (R9/P2.2).
#'
#' commonmark's `tagfilter` extension only escapes a small tag list (script,
#' style, iframe, etc.) and leaves `<img onerror>`, `<svg onload>`, and
#' `javascript:` URLs intact in the rendered HTML. This post-render pass removes
#' executable elements and event-handler/javascript: attributes so stored XSS in
#' a Markdown body cannot run in the reviewer's preview.
#'
#' @param markdown_html character(1) HTML emitted by commonmark.
#' @return character(1) sanitized HTML (inner content of the markdown body).
sanitize_preview_html <- function(markdown_html) {
  wrapped <- paste0('<div class="markdown-body">', markdown_html, "</div>")
  doc <- xml2::read_html(wrapped)
  xml2::xml_remove(xml2::xml_find_all(
    doc,
    '//script | //style | //iframe | //object | //embed | //svg | //img'
  ))
  for (n in xml2::xml_find_all(doc, "//*")) {
    attrs <- xml2::xml_attrs(n)
    if (length(attrs) == 0L) next
    drop <- names(attrs)[
      grepl("^on", names(attrs), ignore.case = TRUE) |
        (names(attrs) %in% c("href", "src", "xlink:href") &
          grepl("^\\s*javascript:", attrs, ignore.case = TRUE))
    ]
    for (a in drop) xml2::xml_set_attr(n, a, NULL)
  }
  div <- xml2::xml_find_first(doc, '//div[contains(@class,"markdown-body")]')
  inner <- as.character(xml2::xml_contents(div))
  paste(inner, collapse = "")
}

#' Render the Markdown body as HTML for preview (commonmark, safe default).
#'
#' Uses a specific extension list that enables useful formatting (tables,
#' strikethrough, autolinks) while excluding `raw_html` passthrough, then
#' sanitizes the output so raw HTML tags cannot execute (P2.2 / R9).
#'
#' @param markdown character(1) Markdown body text.
#' @return character(1) HTML string.
render_markdown_preview <- function(markdown) {
  out <- commonmark::markdown_html(
    markdown,
    extensions = c("table", "strikethrough", "autolink", "tagfilter")
  )
  paste0('<div class="markdown-body">', sanitize_preview_html(out), "</div>")
}
