# GitHub App authentication (R12).
#
# Signs a GitHub App JWT from a Connect-secret private key, exchanges it for an
# installation access token scoped to this repository, and caches/refreshes the
# token per its expiry. Credentials come only from Connect environment
# variables/secrets, never from reviewer PATs. The HTTP exchange is injectable
# so tests can stub it without network access.

.gh_app_env <- function(name, cfg = NULL) {
  if (!is.null(cfg) && !is.null(cfg[[name]])) return(cfg[[name]])
  val <- Sys.getenv(name, unset = "")
  if (identical(val, "")) return(NULL)
  val
}

#' URL-safe (base64url) encode without padding.
b64url_encode <- function(x) {
  b64 <- base64enc::base64encode(x)
  b64 <- gsub("\\+", "-", b64)
  b64 <- gsub("/", "_", b64)
  gsub("=+$", "", b64)
}

#' Build a GitHub App JWT (RS256).
sign_github_app_jwt <- function(app_id, private_key_pem, now_sec = Sys.time()) {
  key <- tryCatch(openssl::read_key(private_key_pem), error = function(e) {
    stop(sprintf("failed to parse GitHub App private key: %s", conditionMessage(e)))
  })
  now <- as.numeric(now_sec)
  header <- jsonlite::toJSON(list(alg = "RS256", typ = "JWT"), auto_unbox = TRUE)
  payload <- jsonlite::toJSON(list(iat = now, exp = now + 600L, iss = as.character(app_id)), auto_unbox = TRUE)
  h <- b64url_encode(charToRaw(header))
  p <- b64url_encode(charToRaw(payload))
  signing_input <- paste0(h, ".", p)
  sig_raw <- openssl::signature_create(charToRaw(signing_input), hash = openssl::sha256, key = key)
  paste0(signing_input, ".", b64url_encode(sig_raw))
}

#' Default HTTP POST used by the token exchange (injectable for tests).
#'
#' Carries an explicit timeout, bounded retries for transient responses, and
#' `req_error` details that surface the GitHub-provided message (e.g. the
#' "Bad credentials" reason behind a 401) so auth failures self-diagnose in the
#' Connect logs.
gh_http_post <- function(url, body, headers) {
  resp <- httr2::request(url) |>
    httr2::req_method("POST") |>
    httr2::req_body_json(body) |>
    httr2::req_headers(!!!headers) |>
    httr2::req_timeout(seconds = 10) |>
    httr2::req_retry(
      is_transient = .is_transient_github_response
    ) |>
    httr2::req_error(
      is_error = function(resp) httr2::resp_status(resp) >= 400L,
      body = .github_api_error_body
    ) |>
    httr2::req_perform()
  jsonlite::fromJSON(httr2::resp_body_string(resp))
}

#' Exchange an app JWT for a repository installation access token.
gh_exchange_installation_token <- function(app_id, private_key_pem, installation_id,
                                           http_post = gh_http_post, now_sec = Sys.time()) {
  jwt <- sign_github_app_jwt(app_id, private_key_pem, now_sec = now_sec)
  url <- sprintf("https://api.github.com/app/installations/%s/access_tokens", installation_id)
  headers <- c(
    Authorization = paste0("Bearer ", jwt),
    Accept = "application/vnd.github+json",
    "X-GitHub-Api-Version" = "2022-11-28"
  )
  resp <- http_post(url, list(), headers)
  if (is.null(resp$token)) {
    stop(sprintf("GitHub installation token exchange returned no token (response keys: %s)",
                 paste(names(resp), collapse = ", ")))
  }
  resp
}

#' A small mutable token cache (per-session object). Not persisted.
new_token_cache <- function() {
  cache <- new.env(parent = emptyenv())
  cache$token <- NULL
  cache$expires_at <- NULL
  structure(list(
    get = function() if (is.null(cache$token)) NULL else list(token = cache$token, expires_at = cache$expires_at),
    set = function(token, expires_at) {
      cache$token <- token
      cache$expires_at <- expires_at
      invisible(TRUE)
    }
  ), class = "reviewapp_token_cache")
}

.expires_soon <- function(expires_at, lead_sec = 60) {
  if (is.null(expires_at)) return(TRUE)
  parsed <- tryCatch(as.POSIXct(expires_at, tz = "UTC"), error = function(e) NA_real_)
  if (is.na(parsed) || length(parsed) != 1L) return(TRUE)
  difftime(parsed, Sys.time(), units = "secs") < lead_sec
}

#' Return a fresh (or cached, unexpired) installation token.
installation_token <- function(get_token, cache, force = FALSE) {
  cached <- cache$get()
  if (!force && !is.null(cached) && !.expires_soon(cached$expires_at)) {
    return(cached$token)
  }
  fresh <- get_token()
  if (is.null(fresh$token) || nchar(fresh$token) == 0L) {
    stop("installation token provider returned no token")
  }
  cache$set(fresh$token, fresh$expires_at)
  fresh$token
}
