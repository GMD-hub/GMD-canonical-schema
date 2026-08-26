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

is_json_object <- function(value) {
  is.list(value) && !is.null(names(value)) &&
    length(names(value)) == length(value) &&
    !anyNA(names(value)) && all(nzchar(names(value))) &&
    !anyDuplicated(names(value))
}

exact_field <- function(value, field) {
  if (!is.list(value)) return(NULL)
  value[[field, exact = TRUE]]
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
    if (is.null(names(page))) {
      return(c(results, page))
    }
    if (!is_json_object(page) || !("results" %in% names(page))) {
      stop("Connect returned a malformed collection object")
    }
    page_results <- exact_field(page, "results")
    if (!is.list(page_results) || !is.null(names(page_results))) {
      stop("Connect returned a malformed collection object")
    }
    results <- c(results, page_results)
    next_url <- exact_field(page, "next")
    if (is.null(next_url)) break
    if (!is.character(next_url) || length(next_url) != 1L ||
        is.na(next_url)) {
      stop("Connect returned a malformed collection object")
    }
    if (!nzchar(next_url)) break
    url <- next_url
  }
  results
}

pick <- function(x, fields) x[intersect(fields, names(x))]

is_nonempty_scalar <- function(value) {
  is.atomic(value) && length(value) == 1L && !is.na(value) &&
    nzchar(as.character(value))
}

same_scalar_text <- function(left, right) {
  is_nonempty_scalar(left) && is_nonempty_scalar(right) &&
    identical(as.character(left), as.character(right))
}

has_nonempty_value <- function(value) {
  if (is.null(value) || length(value) == 0L) return(FALSE)
  text <- tryCatch(
    as.character(value),
    error = function(error) "malformed"
  )
  any(!is.na(text) & nzchar(text))
}

is_successful_job_status <- function(status) {
  numeric_success <- is.numeric(status) && length(status) == 1L &&
    !is.na(status) && identical(as.numeric(status), 2)
  named_success <- is.character(status) && length(status) == 1L &&
    !is.na(status) && status %in% c("finished", "success", "succeeded")
  numeric_success || named_success
}

contains_secret <- function(value, secret) {
  if (!nzchar(secret)) return(FALSE)
  if (is.list(value)) {
    secret_name <- !is.null(names(value)) && any(
      !is.na(names(value)) & grepl(secret, names(value), fixed = TRUE)
    )
    return(secret_name || any(vapply(
      value,
      contains_secret,
      logical(1),
      secret = secret
    )))
  }
  is.character(value) && any(
    !is.na(value) & grepl(secret, value, fixed = TRUE)
  )
}

attest_connect <- function(opts, request_json = connect_request_json) {
  base <- sprintf("%s/__api__/v1/content/%s", opts$server, opts$guid)
  get_one <- function(suffix = "") {
    url <- paste0(base, suffix)
    if (!allowed_connect_url(url, base)) stop("Connect endpoint is not allowed")
    value <- request_json(url, opts$api_key)
    if (!is_json_object(value)) {
      stop("Connect returned a malformed JSON object")
    }
    value
  }
  content_raw <- get_one()
  bundles_raw <- collect_pages(
    paste0(base, "/bundles"), base, opts$api_key, request_json
  )
  jobs_raw <- collect_pages(paste0(base, "/jobs"), base, opts$api_key, request_json)
  repository_raw <- get_one("/repository")

  if (!all(vapply(bundles_raw, is_json_object, logical(1))) ||
      !all(vapply(jobs_raw, is_json_object, logical(1)))) {
    stop("Connect returned a malformed collection object")
  }
  for (bundle in bundles_raw) {
    metadata <- exact_field(bundle, "metadata")
    if (!is.null(metadata) && !is_json_object(metadata)) {
      stop("Connect returned malformed bundle metadata")
    }
  }
  if (!all(vapply(
    bundles_raw,
    function(bundle) is_nonempty_scalar(exact_field(bundle, "id")),
    logical(1)
  )) || !all(vapply(
    jobs_raw,
    function(job) is_nonempty_scalar(exact_field(job, "id")),
    logical(1)
  ))) {
    stop("Connect collection records require nonempty IDs")
  }

  content_status <- exact_field(content_raw, "content_status")
  runtime_status <- exact_field(content_raw, "runtime_status")
  content_status_ok <- is.null(content_status) ||
    (is.character(content_status) && length(content_status) == 1L &&
      !is.na(content_status) &&
      content_status %in% c("ready", "deployed"))
  runtime_status_ok <- is.null(runtime_status) ||
    (is.character(runtime_status) && length(runtime_status) == 1L &&
      !is.na(runtime_status) &&
      runtime_status %in% c("running", "ready"))
  content_bundle_id <- exact_field(content_raw, "bundle_id")
  if (!identical(exact_field(content_raw, "guid"), opts$guid) ||
      !is_nonempty_scalar(content_bundle_id) ||
      !identical(exact_field(content_raw, "app_mode"), "shiny") ||
      !is_nonempty_scalar(exact_field(content_raw, "last_deployed_time")) ||
      !is_nonempty_scalar(exact_field(content_raw, "r_version")) ||
      !content_status_ok || !runtime_status_ok) {
    stop("Connect content identity or deployment health is not acceptable")
  }
  repository_url_legacy <- exact_field(repository_raw, "repository_url")
  repository_url_current <- exact_field(repository_raw, "repository")
  repository_url <- repository_url_legacy %||% repository_url_current
  if (!is.null(repository_url_legacy) &&
      !is.null(repository_url_current) &&
      !identical(repository_url_legacy, repository_url_current)) {
    stop("Connect repository URL aliases disagree")
  }
  expected_repository <- list(
    repository_url = opts$repository,
    branch = opts$branch,
    directory = opts$directory,
    last_known_commit = opts$commit
  )
  repository_identity <- list(
    repository_url = repository_url,
    branch = exact_field(repository_raw, "branch"),
    directory = exact_field(repository_raw, "directory"),
    last_known_commit = exact_field(repository_raw, "last_known_commit")
  )
  for (field in names(expected_repository)) {
    if (!identical(repository_identity[[field]], expected_repository[[field]])) {
      stop(sprintf("Connect repository %s does not match expectation", field))
    }
  }
  if (has_nonempty_value(exact_field(repository_raw, "last_error"))) {
    stop("Connect repository reports a synchronization error")
  }
  active <- Filter(
    function(bundle) isTRUE(exact_field(bundle, "active")),
    bundles_raw
  )
  if (length(active) != 1L) stop("Connect active deployment bundle is missing or ambiguous")
  active_bundle <- active[[1L]]
  active_bundle_id <- exact_field(active_bundle, "id")
  if (!same_scalar_text(active_bundle_id, content_bundle_id)) {
    stop("Connect active deployment bundle is missing or ambiguous")
  }
  metadata <- exact_field(active_bundle, "metadata") %||% list()
  metadata_source <- exact_field(metadata, "source")
  source_ok <- identical(metadata_source, opts$directory) ||
    (identical(metadata_source, "git") &&
      identical(
        exact_field(repository_raw, "directory"),
        opts$directory
      ))
  if (!identical(exact_field(metadata, "source_repo"), opts$repository) ||
      !identical(exact_field(metadata, "source_branch"), opts$branch) ||
      !identical(exact_field(metadata, "source_commit"), opts$commit) ||
      !source_ok) {
    stop("Connect active bundle source identity does not match expectation")
  }
  successful_jobs <- Filter(function(job) {
    exit_code <- exact_field(job, "exit_code")
    same_scalar_text(exact_field(job, "bundle_id"), active_bundle_id) &&
      is_successful_job_status(exact_field(job, "status")) &&
      is.numeric(exit_code) && length(exit_code) == 1L &&
      !is.na(exit_code) && exit_code == 0 &&
      !has_nonempty_value(exact_field(job, "error"))
  }, jobs_raw)
  if (length(successful_jobs) < 1L) {
    stop("Connect active deployment bundle has no successful job")
  }

  bundles <- lapply(bundles_raw, function(x) {
    out <- pick(x, c("id", "created_time", "r_version", "active"))
    out$metadata <- pick(exact_field(x, "metadata") %||% list(), c(
      "source", "source_branch", "source_commit", "source_repo"
    ))
    out
  })
  jobs <- lapply(jobs_raw, function(x) {
    out <- pick(x, c(
      "id", "bundle_id", "tag", "start_time", "end_time", "status", "exit_code"
    ))
    out$error_present <- has_nonempty_value(exact_field(x, "error"))
    out
  })
  order_id <- function(values) {
    order(vapply(
      values,
      function(x) as.character(exact_field(x, "id")),
      character(1)
    ))
  }
  repository <- c(
    list(repository_url = repository_url),
    pick(repository_raw, c(
      "branch", "directory", "polling", "last_known_commit",
      "last_fetched_time"
    ))
  )
  repository$last_error_present <- FALSE
  evidence <- list(
    content = pick(content_raw, c(
      "guid", "name", "bundle_id", "last_deployed_time", "r_version",
      "app_mode", "content_status", "runtime_status"
    )),
    bundles = bundles[order_id(bundles)],
    jobs = jobs[order_id(jobs)],
    repository = repository
  )
  if (contains_secret(evidence, opts$api_key)) {
    stop("Connect evidence contains secret material")
  }
  evidence
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
