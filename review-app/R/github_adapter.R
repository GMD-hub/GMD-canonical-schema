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

PRODUCTION_REVIEW_BRANCH <- "review-production"

expected_source_commit <- function(value = Sys.getenv(
  "REVIEW_APP_EXPECTED_SOURCE_COMMIT", unset = ""
)) {
  if (!.is_sha1(value)) {
    stop("REVIEW_APP_EXPECTED_SOURCE_COMMIT must be a lowercase Git SHA-1")
  }
  value
}

new_repository_read_telemetry <- function() {
  list(
    begin = function(http) {
      logical_reads <- 0L
      actual_attempts <- 0L
      per_record_reads <- 0L
      started <- proc.time()[["elapsed"]]
      list(
        http = function(method, url, token, body = NULL) {
          if (identical(method, "GET")) {
            logical_reads <<- logical_reads + 1L
            if (grepl("/contents/extraction/30_review/[^?]+[.]review[.]yml", url)) {
              per_record_reads <<- per_record_reads + 1L
            }
          }
          if (identical(http, gh_adapter_http)) {
            http(method, url, token, body = body, attempt_hook = function() {
              actual_attempts <<- actual_attempts + 1L
            })
          } else {
            actual_attempts <<- actual_attempts + 1L
            http(method, url, token, body = body)
          }
        },
        snapshot = function() list(
          logical_reads = logical_reads,
          actual_attempts = actual_attempts,
          per_record_reads = per_record_reads,
          duration_ms = as.integer(round(
            (proc.time()[["elapsed"]] - started) * 1000
          ))
        )
      )
    }
  )
}

repository_telemetry_operation <- function(adapter) {
  if (is.null(adapter$telemetry)) {
    return(list(adapter = adapter, snapshot = function() NULL))
  }
  operation <- adapter$telemetry$begin(adapter$http)
  scoped <- adapter
  scoped$http <- operation$http
  list(adapter = scoped, snapshot = operation$snapshot)
}

#' Fetch the current commit SHA that a branch ref points to.
#' @param get function() -> character(1) commit sha (injectable for tests).
adapter_branch_head <- function(owner, repo, branch, token, http = NULL) {
  # http is a function(url, headers, method) returning parsed JSON; provided by
  # the adapter factory in production, injected in tests.
  url <- sprintf(
    "https://api.github.com/repos/%s/%s/git/ref/heads/%s",
    owner,
    repo,
    utils::URLencode(branch, reserved = FALSE)
  )
  resp <- http("GET", url, token)
  sha <- resp$object$sha %||% NULL
  if (!.is_scalar_character(sha)) {
    stop(sprintf("GitHub branch response did not contain a head SHA for '%s'", branch))
  }
  sha
}

#' Fetch the full recursive tree for a branch and return a name->blob map.
adapter_fetch_tree_at <- function(owner, repo, commit_sha, token, http = NULL) {
  if (!.is_scalar_character(commit_sha)) {
    stop("a commit SHA is required to read a Git tree")
  }
  url <- sprintf(
    "https://api.github.com/repos/%s/%s/git/trees/%s?recursive=1",
    owner,
    repo,
    commit_sha
  )
  resp <- http("GET", url, token)
  if (isTRUE(resp$truncated)) {
    stop("GitHub returned a truncated recursive tree; refusing an incomplete queue")
  }
  entries <- resp$tree
  out <- list()
  if (is.data.frame(entries)) {
    blobs <- entries[entries$type == "blob", , drop = FALSE]
    for (i in seq_len(nrow(blobs))) {
      if (!.is_scalar_character(blobs$path[i]) ||
          !.is_scalar_character(blobs$sha[i])) {
        stop("GitHub tree contained an invalid blob entry")
      }
      out[[blobs$path[i]]] <- blobs$sha[i]
    }
  } else if (is.list(entries)) {
    for (entry in entries) {
      if (identical(entry$type, "blob")) {
        if (!.is_scalar_character(entry$path) ||
            !.is_scalar_character(entry$sha)) {
          stop("GitHub tree contained an invalid blob entry")
        }
        out[[entry$path]] <- entry$sha
      }
    }
  } else {
    stop("GitHub tree response did not contain a tree list")
  }
  list(
    commit = commit_sha,
    tree_sha = resp$sha %||% commit_sha,
    blobs = out
  )
}

adapter_fetch_tree <- function(owner, repo, branch, token, http = NULL) {
  head_sha <- adapter_branch_head(owner, repo, branch, token, http)
  adapter_fetch_tree_at(owner, repo, head_sha, token, http)
}

#' Fetch a file's content (as text) and its blob SHA.
adapter_fetch_blob <- function(owner, repo, path, ref, token, http = NULL) {
  url <- sprintf(
    "https://api.github.com/repos/%s/%s/contents/%s?ref=%s",
    owner,
    repo,
    utils::URLencode(path, reserved = FALSE),
    utils::URLencode(ref, reserved = FALSE)
  )
  resp <- http("GET", url, token)
  if (!.is_scalar_character(resp$content) || !.is_scalar_character(resp$sha)) {
    stop(sprintf("GitHub contents response for '%s' was incomplete", path))
  }
  raw <- tryCatch(
    base64enc::base64decode(resp$content),
    error = function(e) stop(sprintf("failed to decode GitHub blob '%s': %s", path, conditionMessage(e)))
  )
  list(content = rawToChar(raw), sha = resp$sha, raw = raw)
}

adapter_fetch_blob_by_sha <- function(owner, repo, blob_sha, token, http = NULL) {
  if (!.is_sha1(blob_sha)) {
    stop("immutable blob reads require a lowercase Git SHA-1")
  }
  url <- sprintf(
    "https://api.github.com/repos/%s/%s/git/blobs/%s",
    owner,
    repo,
    blob_sha
  )
  resp <- http("GET", url, token)
  if (!identical(resp$sha, blob_sha)) {
    stop(sprintf("immutable blob response SHA did not match '%s'", blob_sha))
  }
  if (!identical(resp$encoding, "base64") ||
      !.is_scalar_character(resp$content)) {
    stop(sprintf("immutable blob '%s' was not a verified base64 response", blob_sha))
  }
  raw <- tryCatch(
    base64enc::base64decode(resp$content),
    error = function(e) stop(sprintf("failed to decode immutable blob '%s': %s", blob_sha, conditionMessage(e)))
  )
  if (!identical(git_blob_sha_raw(raw), blob_sha)) {
    stop(sprintf("immutable blob '%s' content did not verify against its SHA", blob_sha))
  }
  list(content = rawToChar(raw), sha = resp$sha, raw = raw)
}

adapter_graphql <- function(owner, repo, query, variables, token, http = NULL) {
  if (!.is_scalar_character(query) || !is.list(variables)) {
    stop("GraphQL requests require a query and variables mapping")
  }
  resp <- http(
    "POST",
    "https://api.github.com/graphql",
    token,
    body = list(query = query, variables = variables)
  )
  if (!is.null(resp$errors) && length(resp$errors) > 0L) {
    messages <- vapply(resp$errors, function(error) {
      error$message %||% "unknown GraphQL error"
    }, character(1))
    stop(sprintf("GitHub GraphQL request failed: %s", paste(messages, collapse = "; ")))
  }
  if (is.null(resp$data)) stop("GitHub GraphQL response did not contain data")
  resp$data
}

adapter_fetch_blobs_graphql <- function(
  adapter, commit_sha, paths, batch_size = 50L, progress = NULL
) {
  if (!.is_scalar_character(commit_sha) || !length(paths)) return(list())
  if (!is.numeric(batch_size) || length(batch_size) != 1L || batch_size < 1L ||
      batch_size > 50L) {
    stop("GraphQL batch_size must be between 1 and 50")
  }
  paths <- as.character(paths)
  if (any(!grepl(
    "^extraction/20_drafts/(idn|geo|dem|lbr|utl|dwl)/VAR-[a-z0-9]+[.]md$",
    paths
  ))) {
    stop("GraphQL source blob batches contain an unsafe path")
  }
  if (anyDuplicated(paths)) stop("GraphQL blob paths must be unique")
  batches <- split(paths, ceiling(seq_along(paths) / as.integer(batch_size)))
  result <- list()
  for (i in seq_along(batches)) {
    batch <- batches[[i]]
    aliases <- sprintf("b%03d", seq_along(batch))
    fields <- vapply(seq_along(batch), function(j) {
      expression <- paste0(commit_sha, ":", batch[[j]])
      expression <- gsub("\\\\", "\\\\\\\\", expression)
      expression <- gsub('"', '\\\\"', expression, fixed = TRUE)
      sprintf(
        "%s: object(expression: \"%s\") { ... on Blob { oid text } }",
        aliases[[j]],
        expression
      )
    }, character(1))
    query <- paste0(
      "query { repository(owner: \"", adapter$owner,
      "\", name: \"", adapter$repo, "\") { ",
      paste(fields, collapse = " "), " } }"
    )
    data <- adapter_graphql(
      adapter$owner,
      adapter$repo,
      query,
      list(),
      adapter$get_token(),
      adapter$http
    )
    repository <- data$repository %||% NULL
    if (is.null(repository)) stop("GitHub GraphQL response omitted repository")
    for (j in seq_along(batch)) {
      blob <- repository[[aliases[[j]]]] %||% NULL
      if (is.null(blob) || !.is_scalar_character(blob$oid) ||
          is.null(blob$text)) {
        stop(sprintf("GitHub GraphQL response omitted source blob '%s'", batch[[j]]))
      }
      result[[batch[[j]]]] <- list(
        content = blob$text,
        sha = blob$oid,
        raw = charToRaw(enc2utf8(blob$text))
      )
    }
    if (!is.null(progress)) progress(min(i * as.integer(batch_size), length(paths)), length(paths))
  }
  result
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
#' @param http function(method, url, token, body) returning parsed JSON
#'   (injectable; defaults to `gh_adapter_http()`).
#' @param expected_source_commit optional pinned lowercase Git SHA-1 required
#'   for production queue manifest validation.
#' @param telemetry optional operation telemetry factory created by
#'   `new_repository_read_telemetry()`.
new_github_adapter <- function(owner, repo, default_branch, review_branch,
                               get_token, http = NULL,
                               expected_source_commit = NULL,
                               telemetry = NULL) {
  transport <- http %||% gh_adapter_http
  structure(list(
    owner = owner,
    repo = repo,
    default_branch = default_branch,
    review_branch = review_branch,
    expected_source_commit = expected_source_commit,
    telemetry = telemetry,
    get_token = get_token,
    http = transport
  ), class = "reviewapp_github_adapter")
}

`%||%` <- function(a, b) if (is.null(a)) b else a

#' Build the production GitHub adapter from Connect secrets.
#'
#' Reads the Connect environment variables/secrets required to authenticate as
#' the GitHub App and construct a live adapter:
#'
#' - `REVIEW_APP_GH_OWNER`, `REVIEW_APP_GH_REPO`,
#'   `REVIEW_APP_GH_DEFAULT_BRANCH`, `REVIEW_APP_GH_REVIEW_BRANCH`
#' - `GITHUB_APP_ID`, `GITHUB_APP_INSTALLATION_ID`, `GITHUB_APP_PRIVATE_KEY`
#'
#' Returns `NULL` in offline/local mode (when `REVIEW_APP_OFFLINE=1` is set or
#' when an adapter is injected via `options(reviewapp.adapter)`), which is what
#' the local/dev smoke tests rely on. If the app is not in offline mode and no
#' injected adapter is present but the required secrets are missing, this fails
#' loudly instead of silently running with an empty queue (R3).
#'
#' @return a `reviewapp_github_adapter`, or NULL in offline/injected mode.
#' @export
review_app_adapter <- function() {
  injected <- getOption("reviewapp.adapter")
  if (!is.null(injected)) {
    return(injected)
  }
  offline <- Sys.getenv("REVIEW_APP_OFFLINE", unset = "")
  if (identical(tolower(offline), "1") || identical(tolower(offline), "true")) {
    return(NULL)
  }
  owner <- Sys.getenv("REVIEW_APP_GH_OWNER", unset = "")
  repo <- Sys.getenv("REVIEW_APP_GH_REPO", unset = "")
  default_branch <- Sys.getenv("REVIEW_APP_GH_DEFAULT_BRANCH", unset = "")
  review_branch <- Sys.getenv("REVIEW_APP_GH_REVIEW_BRANCH", unset = "")
  app_id <- .gh_app_env("GITHUB_APP_ID")
  installation_id <- .gh_app_env("GITHUB_APP_INSTALLATION_ID")
  private_key <- .gh_app_env("GITHUB_APP_PRIVATE_KEY")
  source_commit <- expected_source_commit()

  missing <- c(
    owner = !nzchar(owner), repo = !nzchar(repo),
    default_branch = !nzchar(default_branch), review_branch = !nzchar(review_branch),
    app_id = is.null(app_id), installation_id = is.null(installation_id),
    private_key = is.null(private_key)
  )
  if (any(missing)) {
    stop(
      "review app adapter not configured: set REVIEW_APP_GH_OWNER, ",
      "REVIEW_APP_GH_REPO, REVIEW_APP_GH_DEFAULT_BRANCH, ",
      "REVIEW_APP_GH_REVIEW_BRANCH, GITHUB_APP_ID, ",
      "GITHUB_APP_INSTALLATION_ID, GITHUB_APP_PRIVATE_KEY ",
      "(or set REVIEW_APP_OFFLINE=1 for local/offline mode, or inject ",
      "`options(reviewapp.adapter = ...)` for dev/tests)"
    )
  }

  token_cache <- new_token_cache()
  new_github_adapter(
    owner = owner,
    repo = repo,
    default_branch = default_branch,
    review_branch = review_branch,
    expected_source_commit = source_commit,
    telemetry = new_repository_read_telemetry(),
    get_token = function() {
      installation_token(
        get_token = function() gh_exchange_installation_token(
          app_id = app_id,
          private_key_pem = private_key,
          installation_id = installation_id
        ),
         cache = token_cache
      )
    }
  )
}

#' Test whether a GitHub API response indicates a transient error eligible for
#' retry (429 rate-limit, 500/502/503/504 server errors).
#'
#' Used as the `is_transient` handler for [httr2::req_retry()] in both
#' [gh_adapter_http] and [gh_http_post] so the transient-status set is defined
#' once.
#'
#' @param resp an `httr2_response`.
#' @return logical(1).
.is_transient_github_response <- function(resp) {
  httr2::resp_status(resp) %in% c(429L, 500L, 502L, 503L, 504L)
}

#' Extract the GitHub-provided reason from an HTTP error response.
#'
#' Used as the `body` handler for [httr2::req_error()] so a 401/403/404 surfaces
#' GitHub's own message (e.g. "Bad credentials") instead of a bare HTTP status.
#' Falls back to the raw response body, then to NULL (default httr2 message)
#' when nothing usable is present.
#' @param resp an `httr2_response`.
#' @return character(1) error detail or NULL.
.github_api_error_body <- function(resp) {
  raw_body <- tryCatch(httr2::resp_body_string(resp), error = function(e) "")
  parsed <- tryCatch(jsonlite::fromJSON(raw_body), error = function(e) NULL)
  if (!is.null(parsed) && !is.null(parsed$message) && nzchar(parsed$message)) {
    return(parsed$message)
  }
  if (nzchar(raw_body)) raw_body else NULL
}

#' Real HTTP transport for the adapter (httr2 over token auth).
#'
#' Every request carries an explicit timeout and bounded retries so a slow or
#' transient GitHub response can never block the Shiny event loop indefinitely,
#' and `req_error` augments failures with GitHub's message. 4xx responses that
#' are not transient (notably 401 during the token exchange) fail fast with a
#' descriptive error.
#'
#' @param method HTTP method (GET/POST/PATCH).
#' @param url request URL.
#' @param token GitHub installation token.
#' @param body optional (named) list sent as a JSON request body via
#'   `httr2::req_body_json` when not NULL (e.g. blob/tree/commit/ref writes).
gh_adapter_http <- function(method, url, token, body = NULL, attempt_hook = NULL) {
  req <- httr2::request(url) |>
    httr2::req_method(method) |>
    httr2::req_headers(
      Authorization = paste0("Bearer ", token),
      Accept = "application/vnd.github+json",
      "X-GitHub-Api-Version" = "2022-11-28"
    ) |>
    httr2::req_timeout(seconds = 10) |>
    httr2::req_retry(
      is_transient = function(resp) {
        transient <- .is_transient_github_response(resp)
        if (transient && !is.null(attempt_hook)) attempt_hook()
        transient
      }
    ) |>
    httr2::req_error(
      is_error = function(resp) httr2::resp_status(resp) >= 400L,
      body = .github_api_error_body
    )
  if (!is.null(body)) {
    req <- httr2::req_body_json(req, body)
  }
  if (!is.null(attempt_hook)) attempt_hook()
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
