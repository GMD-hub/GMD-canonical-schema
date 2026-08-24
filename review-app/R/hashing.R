# R-native SHA-256 hashing, digest-format compatible with the Python pipeline
# (lowercase hex). No cross-language code reuse; verified by the cross-language
# fixture test in test-hashing.R.

#' Compute the lowercase-hex SHA-256 digest of a text string.
#' @param text character(1) -- the Markdown body (or any string) to hash.
#' @return character(1) lowercase hex digest.
hash_body <- function(text) {
  if (!is.character(text) || length(text) != 1L || is.na(text)) {
    stop("hash_body() requires a single non-NA character string")
  }
  hex <- as.character(openssl::sha256(charToRaw(enc2utf8(text))))
  attributes(hex) <- NULL
  hex
}

#' Verify a body against an expected lowercase-hex SHA-256 digest.
verify_body_hash <- function(text, expected_sha256) {
  identical(hash_body(text), expected_sha256)
}

#' Compute the Git SHA-1 object ID for a blob's exact bytes.
#'
#' Git hashes the object header and payload, not the payload alone. This helper
#' is used for optimistic-lock identities of generated review records and keeps
#' those identities distinct from their SHA-256 content digests.
git_blob_sha_raw <- function(payload) {
  if (!is.raw(payload)) {
    stop("git_blob_sha_raw() requires a raw vector")
  }
  header <- c(charToRaw(paste0("blob ", length(payload))), as.raw(0L))
  sha <- as.character(openssl::sha1(c(header, payload)))
  attributes(sha) <- NULL
  sha
}

git_blob_sha <- function(text) {
  if (!is.character(text) || length(text) != 1L || is.na(text)) {
    stop("git_blob_sha() requires a single non-NA character string")
  }
  git_blob_sha_raw(charToRaw(enc2utf8(text)))
}
