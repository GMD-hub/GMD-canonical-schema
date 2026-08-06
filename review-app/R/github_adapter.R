# GitHub adapter (R13, R16, R11, R14, R18).
#
# Reads draft artifacts from the default branch (source context) and review
# records/approved artifacts from the review branch. Every read returns content
# plus its blob SHA. Writes build a Git tree from the changed files for one
# logical operation, create one commit, and update the review branch ref --
# atomic from the caller's perspective, with optimistic locking and loud
# partial-failure reporting.
#
# The GitHub HTTP layer is abstracted behind storage-interface functions
# (R20) so tests can prove atomicity/staleness/recovery deterministically with
# an in-memory double, and production uses the real REST/GraphQL calls.

# ---------------------------------------------------------------------------
# Storage interface (default implementations hit the GitHub API over HTTP)
# ---------------------------------------------------------------------------

#' Fetch the current commit SHA that a branch ref points to.
#' @param get function() -> character(1) commit sha (injectable for tests).
adapter_branch_head <- function(owner, repo, branch, token, http = NULL) {
  # http is a function(url, headers, method) returning parsed JSON; provided by
  # the adapter factory in production, injected in tests.
  url <- sprintf("https://api.github.com/repos/%s/%s/git/ref/heads/%s", owner, repo, branch)
  resp <- http("GET", url, token)
  resp$object$sha
}

#' Fetch the full recursive tree for a branch and return a name->blob map.
adapter_fetch_tree <- function(owner, repo, branch, token, http = NULL) {
  head_sha <- adapter_branch_head(owner, repo, branch, token, http)
  url <- sprintf("https://api.github.com/repos/%s/%s/git/trees/%s?recursive=1", owner, repo, head_sha)
  resp <- http("GET", url, token)
  entries <- resp$tree
  out <- list()
  for (e in entries) {
    if (identical(e$type, "blob")) {
      out[[e$path]] <- e$sha
    }
  }
  list(commit = head_sha, blobs = out)
}

#' Fetch a file's content (as text) and its blob SHA.
adapter_fetch_blob <- function(owner, repo, path, ref, token, http = NULL) {
  url <- sprintf("https://api.github.com/repos/%s/%s/contents/%s?ref=%s", owner, repo, path, ref)
  resp <- http("GET", url, token)
  list(content = rawToChar(base64enc::base64decode(resp$content)), sha = resp$sha)
}

# ---------------------------------------------------------------------------
# High-level adapter object
# ---------------------------------------------------------------------------

#' Create a GitHub adapter.
#'
#' @param owner character(1) repository owner.
#' @param repo character(1) repository name.
#' @param default_branch character(1) e.g. "main".
#' @param review_branch character(1) dedicated protected review branch (R13).
#' @param get_token function() returning an installation token.
#' @param http function(method, url, token) returning parsed JSON (injectable;
#'   defaults to a real httr2 implementation wired in `gh_adapter_http()`).
new_github_adapter <- function(owner, repo, default_branch, review_branch,
                               get_token, http = NULL) {
  structure(list(
    owner = owner,
    repo = repo,
    default_branch = default_branch,
    review_branch = review_branch,
    get_token = get_token,
    http = http %||% gh_adapter_http
  ), class = "reviewapp_github_adapter")
}

`%||%` <- function(a, b) if (is.null(a)) b else a

#' Real HTTP transport for the adapter (httr2 over token auth).
gh_adapter_http <- function(method, url, token) {
  req <- httr2::request(url) |>
    httr2::req_method(method) |>
    httr2::req_headers(
      Authorization = paste0("Bearer ", token),
      Accept = "application/vnd.github+json",
      "X-GitHub-Api-Version" = "2022-11-28"
    )
  resp <- httr2::req_perform(req)
  jsonlite::fromJSON(httr2::resp_body_string(resp))
}

# ---------------------------------------------------------------------------
# Reads (Step 5 / R13, R16)
# ---------------------------------------------------------------------------

#' Read a draft artifact from the default branch. Returns content + blob SHA.
adapter_read_draft <- function(adapter, path) {
  token <- adapter$get_token()
  adapter_fetch_blob(adapter$owner, adapter$repo, path, adapter$default_branch, token, adapter$http)
}

#' Read a review record from the review branch. Returns content + blob SHA.
adapter_read_review <- function(adapter, path) {
  token <- adapter$get_token()
  adapter_fetch_blob(adapter$owner, adapter$repo, path, adapter$review_branch, token, adapter$http)
}

#' Read an approved artifact from the review branch. Returns content + blob SHA.
adapter_read_approved <- function(adapter, path) {
  token <- adapter$get_token()
  adapter_fetch_blob(adapter$owner, adapter$repo, path, adapter$review_branch, token, adapter$http)
}
