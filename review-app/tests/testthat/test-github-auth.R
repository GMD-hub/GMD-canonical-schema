# Step 4 -- GitHub App authentication tests (R12).
#
# Covers JWT signing, token exchange, and the per-session token cache. The HTTP
# exchange is injected so tests need no network. A real disposable-app
# integration check is documented as a manual step in the operator guide.

# --- JWT signing ---

test_that("sign_github_app_jwt produces a 3-part JWT with expected claims", {
  key <- openssl::rsa_keygen(2048)
  pem <- openssl::write_pem(key)
  jwt <- reviewapp::sign_github_app_jwt("12345", pem, now_sec = as.POSIXct("2030-01-01 00:00:00", tz = "UTC"))
  parts <- strsplit(jwt, ".", fixed = TRUE)[[1L]]
  expect_length(parts, 3L)

  # decode header + payload
  b64 <- function(s) {
    pad_needed <- (4 - nchar(s) %% 4) %% 4
    rawToChar(base64enc::base64decode(paste0(s, strrep("=", pad_needed))))
  }
  header <- jsonlite::fromJSON(b64(parts[[1L]]))
  payload <- jsonlite::fromJSON(b64(parts[[2L]]))
  expect_identical(header$alg, "RS256")
  expect_identical(payload$iss, "12345")
  # iat == fixed time, exp == iat + 600
  expect_identical(as.numeric(payload$iat), as.numeric(as.POSIXct("2030-01-01 00:00:00", tz = "UTC")))
  expect_identical(as.numeric(payload$exp), as.numeric(payload$iat) + 600)
})

test_that("JWT signature verifies with the corresponding public key", {
  key <- openssl::rsa_keygen(2048)
  pem <- openssl::write_pem(key)
  jwt <- reviewapp::sign_github_app_jwt("9", pem, now_sec = as.POSIXct("2030-01-01 00:00:00", tz = "UTC"))
  parts <- strsplit(jwt, ".", fixed = TRUE)[[1L]]
  b64 <- function(s) {
    pad_needed <- (4 - nchar(s) %% 4) %% 4
    rawToChar(base64enc::base64decode(paste0(s, strrep("=", pad_needed))))
  }
  signing_input <- paste0(parts[[1L]], ".", parts[[2L]])
  sig_b64url <- parts[[3L]]
  pad_needed <- (4 - nchar(sig_b64url) %% 4) %% 4
  sig_b64 <- gsub("-", "+", gsub("_", "/", paste0(sig_b64url, strrep("=", pad_needed))))
  sig <- base64enc::base64decode(sig_b64)
  # P2.4: write the temporary public key to a unique tempfile (not tempdir()) so
  # parallel test runs never collide, and clean it up even on failure.
  tmp_pem <- tempfile(fileext = ".pem")
  on.exit(unlink(tmp_pem), add = TRUE)
  openssl::write_pem(key, tmp_pem)
  expect_true(openssl::signature_verify(charToRaw(signing_input), sig, hash = openssl::sha256, pubkey = openssl::read_pubkey(openssl::write_pem(key, tmp_pem))))
})

test_that("JWT signing fails loudly on an invalid private key", {
  expect_error(reviewapp::sign_github_app_jwt("1", "not a pem"), "failed to parse GitHub App private key")
})

# --- Token exchange ---

test_that("gh_exchange_installation_token returns a token and sends the Bearer JWT", {
  key <- openssl::rsa_keygen(2048)
  pem <- openssl::write_pem(key)
  captured <- NULL
  fake_post <- function(url, body, headers) {
    captured <<- list(url = url, body = body, headers = headers)
    list(token = "ghu_testtoken123", expires_at = "2030-01-01T00:10:00Z")
  }
  resp <- reviewapp::gh_exchange_installation_token("4242", pem, "99999",
                                                    http_post = fake_post,
                                                    now_sec = as.POSIXct("2030-01-01 00:00:00", tz = "UTC"))
  expect_identical(resp$token, "ghu_testtoken123")
  expect_match(captured$url, "/app/installations/99999/access_tokens")
  expect_true(grepl("^Bearer ", captured$headers[["Authorization"]]))
})

test_that("gh_exchange_installation_token fails loudly when no token is returned", {
  key <- openssl::rsa_keygen(2048)
  pem <- openssl::write_pem(key)
  fake_post <- function(url, body, headers) list(message = "boom")
  expect_error(
    reviewapp::gh_exchange_installation_token("4242", pem, "99999", http_post = fake_post),
    "returned no token"
  )
})

# --- Token cache ---

test_that("installation_token caches and refreshes around expiry", {
  cache <- reviewapp::new_token_cache()
  calls <- 0L
  provider <- function() {
    calls <<- calls + 1L
    list(token = "tok1", expires_at = format(Sys.time() + 3600, tz = "UTC", usetz = TRUE))
  }
  expect_identical(reviewapp::installation_token(provider, cache), "tok1")
  # cached -> no extra provider call
  expect_identical(reviewapp::installation_token(provider, cache), "tok1")
  expect_identical(calls, 1L)
})

test_that("installation_token refreshes when the cached token is expired", {
  cache <- reviewapp::new_token_cache()
  # seed an expired token directly
  cache$set("expired", "2000-01-01T00:00:00Z")
  calls <- 0L
  provider <- function() {
    calls <<- calls + 1L
    list(token = "fresh", expires_at = "2030-01-01T00:00:00Z")
  }
  expect_identical(reviewapp::installation_token(provider, cache), "fresh")
  expect_identical(calls, 1L)
})

test_that("installation_token fails loudly when provider returns no token", {
  cache <- reviewapp::new_token_cache()
  expect_error(reviewapp::installation_token(function() list(), cache), "returned no token")
})
