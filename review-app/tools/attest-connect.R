#!/usr/bin/env Rscript

parse_args <- function(args) {
  required <- c(
    "--server", "--guid", "--expected-repository", "--expected-branch",
    "--expected-directory", "--expected-commit"
  )
  flags <- args[startsWith(args, "--")]
  if (any(!flags %in% required) || anyDuplicated(flags) ||
      length(args) != 2L * length(required)) {
    stop("attestor requires exactly the documented arguments")
  }
  value <- function(flag) {
    pos <- match(flag, args)
    if (is.na(pos) || pos == length(args) || startsWith(args[[pos + 1L]], "--")) {
      stop(sprintf("%s is required", flag))
    }
    args[[pos + 1L]]
  }
  opts <- list(
    server = sub("/$", "", value("--server")),
    guid = value("--guid"),
    repository = value("--expected-repository"),
    branch = value("--expected-branch"),
    directory = value("--expected-directory"),
    commit = value("--expected-commit"),
    api_key = Sys.getenv("CONNECT_API_KEY", unset = "")
  )
  if (!nzchar(opts$api_key)) stop("CONNECT_API_KEY is required")
  if (!grepl("^[0-9a-f]{40}$", opts$commit)) {
    stop("--expected-commit must be a lowercase Git SHA-1")
  }
  server <- httr2::url_parse(opts$server)
  if (!identical(server$scheme, "https") || !is.null(server$user) ||
      !is.null(server$password) || !is.null(server$query) ||
      !is.null(server$fragment) ||
      (!is.null(server$path) && !(server$path %in% c("", "/")))) {
    stop("--server must be an HTTPS origin")
  }
  if (!grepl("^[A-Za-z0-9-]{8,}$", opts$guid)) stop("--guid is invalid")
  opts
}

connect_request_json <- function(url, api_key) {
  response <- httr2::request(url) |>
    httr2::req_headers(Authorization = paste("Key", api_key)) |>
    httr2::req_timeout(15) |>
    httr2::req_perform()
  content_type <- httr2::resp_header(response, "content-type") %||% ""
  if (!grepl("^application/json(?:;|$)", content_type)) {
    stop("Connect returned a non-JSON response")
  }
  httr2::resp_body_json(response, simplifyVector = FALSE)
}

allowed_connect_url <- function(url, base) {
  parsed <- httr2::url_parse(url)
  clean <- parsed
  clean$query <- NULL
  clean$fragment <- NULL
  identical(httr2::url_build(clean), base) ||
    httr2::url_build(clean) %in% paste0(base, c("/bundles", "/jobs", "/repository"))
}

collect_pages <- function(url, base, api_key, request_json) {
  results <- list()
  seen <- character()
  repeat {
    if (!allowed_connect_url(url, base) || url %in% seen) {
      stop("Connect request or pagination URL is outside the four-endpoint allowlist")
    }
    seen <- c(seen, url)
    page <- request_json(url, api_key)
    if (!is.list(page)) stop("Connect returned a malformed JSON object")
    results <- c(results, page$results %||% list())
    url <- page[["next"]] %||% ""
    if (!nzchar(url)) break
  }
  results
}

pick <- function(x, fields) x[intersect(fields, names(x))]

attest_connect <- function(opts, request_json = connect_request_json) {
  base <- sprintf("%s/__api__/v1/content/%s", opts$server, opts$guid)
  get_one <- function(suffix = "") {
    url <- paste0(base, suffix)
    if (!allowed_connect_url(url, base)) stop("Connect endpoint is not allowed")
    value <- request_json(url, opts$api_key)
    if (!is.list(value)) stop("Connect returned a malformed JSON object")
    value
  }
  content_raw <- get_one()
  bundles_raw <- collect_pages(
    paste0(base, "/bundles"), base, opts$api_key, request_json
  )
  jobs_raw <- collect_pages(paste0(base, "/jobs"), base, opts$api_key, request_json)
  repository_raw <- get_one("/repository")

  if (!identical(content_raw$guid, opts$guid) ||
      !content_raw$content_status %in% c("ready", "deployed") ||
      !content_raw$runtime_status %in% c("running", "ready") ||
      is.null(content_raw$bundle_id)) {
    stop("Connect content identity or deployment health is not acceptable")
  }
  expected_repository <- c(
    repository_url = opts$repository,
    branch = opts$branch,
    directory = opts$directory,
    last_known_commit = opts$commit
  )
  for (field in names(expected_repository)) {
    if (!identical(repository_raw[[field]], unname(expected_repository[[field]]))) {
      stop(sprintf("Connect repository %s does not match expectation", field))
    }
  }
  if (!is.null(repository_raw$last_error) && nzchar(as.character(repository_raw$last_error))) {
    stop("Connect repository reports a synchronization error")
  }
  active <- Filter(function(bundle) {
    identical(as.character(bundle$id), as.character(content_raw$bundle_id)) &&
      isTRUE(bundle$active)
  }, bundles_raw)
  if (length(active) != 1L) stop("Connect active deployment bundle is missing or ambiguous")
  metadata <- active[[1L]]$metadata %||% list()
  if (!identical(metadata$source_repo, opts$repository) ||
      !identical(metadata$source_branch, opts$branch) ||
      !identical(metadata$source_commit, opts$commit) ||
      !identical(metadata$source, opts$directory)) {
    stop("Connect active bundle source identity does not match expectation")
  }

  bundles <- lapply(bundles_raw, function(x) {
    out <- pick(x, c("id", "created_time", "r_version", "active"))
    out$metadata <- pick(x$metadata %||% list(), c(
      "source", "source_branch", "source_commit", "source_repo"
    ))
    out
  })
  jobs <- lapply(jobs_raw, function(x) {
    out <- pick(x, c(
      "id", "bundle_id", "tag", "start_time", "end_time", "status", "exit_code"
    ))
    out$error_present <- !is.null(x$error) && nzchar(as.character(x$error))
    out
  })
  order_id <- function(values) order(vapply(values, function(x) as.character(x$id), character(1)))
  repository <- pick(repository_raw, c(
    "repository_url", "branch", "directory", "polling", "last_known_commit",
    "last_fetched_time"
  ))
  repository$last_error_present <- FALSE
  list(
    content = pick(content_raw, c(
      "guid", "name", "bundle_id", "last_deployed_time", "r_version",
      "app_mode", "content_status", "runtime_status"
    )),
    bundles = bundles[order_id(bundles)],
    jobs = jobs[order_id(jobs)],
    repository = repository
  )
}

main <- function(args = commandArgs(trailingOnly = TRUE)) {
  evidence <- attest_connect(parse_args(args))
  cat(jsonlite::toJSON(
    evidence, auto_unbox = TRUE, pretty = TRUE, null = "null"
  ), "\n")
  invisible(evidence)
}

`%||%` <- function(a, b) if (is.null(a)) b else a

if (!identical(Sys.getenv("REVIEWAPP_TOOL_TESTING"), "1")) {
if (sys.nframe() == 0L) {
  tryCatch(main(), error = function(error) {
    message("Connect attestation failed: ", conditionMessage(error))
    quit(status = 1L)
  })
}
}
