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
