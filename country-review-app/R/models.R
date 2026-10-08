# Country review artifact model helpers.

ARTIFACT_TYPES <- c("parameter", "exception", "benchmark")
STATES <- c("draft", "in-review", "needs-revision", "approved")
ACTIONS <- c(
  "submitted", "request-revision", "approved", "assigned", "reopened", "saved"
)
ROLES <- c("reviewer", "approver", "administrator")

.is_scalar_character <- function(value) {
  is.character(value) && length(value) == 1L && !is.na(value) && nzchar(value)
}

is_iso3 <- function(value) {
  .is_scalar_character(value) && grepl("^[A-Z]{3}$", value)
}

is_parameter_id <- function(value) {
  .is_scalar_character(value) && grepl("^PARAM-[A-Z0-9-]+$", value)
}

is_exception_id <- function(value) {
  .is_scalar_character(value) && grepl("^EXC-[A-Z0-9-]+$", value)
}

is_benchmark_filename <- function(filename) {
  .is_scalar_character(filename) && grepl(
    "^[A-Z]{3}_[a-z0-9-]+_benchmark_draft[.]yaml$",
    filename
  )
}

detect_artifact_type_from_path <- function(path, parsed_yaml = NULL) {
  filename <- basename(path)
  if (grepl("^PARAM-", filename)) return("parameter")
  if (grepl("^EXC-", filename)) return("exception")
  if (is_benchmark_filename(filename)) return("benchmark")
  if (is.list(parsed_yaml) && "parameters" %in% names(parsed_yaml)) return("parameter")
  if (is.list(parsed_yaml) && "exceptions" %in% names(parsed_yaml)) return("exception")
  NULL
}

extract_iso3_from_path <- function(path, parsed_yaml = NULL) {
  parts <- strsplit(path, "[/\\\\]", perl = TRUE)[[1L]]
  if (length(parts) >= 2L) {
    maybe_iso3 <- parts[[length(parts) - 1L]]
    if (is_iso3(maybe_iso3)) return(maybe_iso3)
  }
  filename <- basename(path)
  if (grepl("^[A-Z]{3}_", filename)) {
    return(sub("^([A-Z]{3})_.*$", "\\1", filename))
  }
  if (is.list(parsed_yaml) && is_iso3(parsed_yaml$iso3 %||% NULL)) {
    return(parsed_yaml$iso3)
  }
  NA_character_
}

build_artifact_id <- function(path, artifact_type, iso3) {
  filename <- basename(path)
  stem <- sub("[.]yaml$", "", filename)
  if (identical(artifact_type, "benchmark")) {
    return(stem)
  }
  if (!is_iso3(iso3)) return(NA_character_)
  sprintf("%s_CTY-%s", stem, iso3)
}

raw_to_hex <- function(raw_value) {
  paste(sprintf("%02x", as.integer(raw_value)), collapse = "")
}

sha256_text <- function(text) {
  value <- enc2utf8(text %||% "")
  if (requireNamespace("openssl", quietly = TRUE)) {
    return(raw_to_hex(openssl::sha256(charToRaw(value))))
  }
  if (requireNamespace("digest", quietly = TRUE)) {
    return(digest::digest(value, algo = "sha256", serialize = FALSE))
  }
  stop("sha256 hashing requires either the 'openssl' or 'digest' package")
}

new_review_event <- function(action, from_state, to_state, actor, role, note = NULL) {
  if (!(action %in% ACTIONS)) stop(sprintf("invalid action '%s'", action))
  if (!(role %in% ROLES)) stop(sprintf("invalid role '%s'", role))
  list(
    event_id = paste0(as.integer(Sys.time()), "-", sample.int(999999, 1L)),
    action = action,
    from_state = from_state,
    to_state = to_state,
    actor = actor,
    actor_role = role,
    note = note,
    occurred_at = format(
      Sys.time(),
      tz = "UTC",
      usetz = FALSE,
      format = "%Y-%m-%dT%H:%M:%SZ"
    )
  )
}

new_review_record <- function(item, source_text, actor = "system") {
  if (!is.list(item)) stop("item must be a mapping")
  if (!(item$artifact_type %in% ARTIFACT_TYPES)) stop("unknown artifact_type")
  record <- list(
    artifact_id = item$artifact_id,
    artifact_type = item$artifact_type,
    iso3 = item$iso3,
    source_artifact_path = item$source_artifact_path,
    state = "draft",
    review_round = 1L,
    assigned_to = list(),
    current_content_sha256 = sha256_text(source_text),
    source_content_sha256 = sha256_text(source_text),
    events = list(
      new_review_event(
        action = "saved",
        from_state = "draft",
        to_state = "draft",
        actor = actor,
        role = "reviewer",
        note = "record initialized"
      )
    )
  )
  validate_review_record(record)
  record
}

validate_review_record <- function(record) {
  required <- c(
    "artifact_id", "artifact_type", "iso3", "source_artifact_path", "state",
    "review_round", "assigned_to", "current_content_sha256",
    "source_content_sha256", "events"
  )
  if (!is.list(record)) stop("review record must be a mapping")
  missing <- required[!required %in% names(record)]
  if (length(missing)) {
    stop(sprintf(
      "review record missing required fields: %s",
      paste(missing, collapse = ", ")
    ))
  }
  if (!(record$state %in% STATES)) stop("invalid state")
  if (!(record$artifact_type %in% ARTIFACT_TYPES)) stop("invalid artifact_type")
  if (!is.integer(record$review_round) || record$review_round < 1L) {
    stop("review_round must be integer >= 1")
  }
  if (!is.character(record$current_content_sha256) ||
      !grepl("^[0-9a-f]{64}$", record$current_content_sha256)) {
    stop("current_content_sha256 must be a sha256")
  }
  if (!is.character(record$source_content_sha256) ||
      !grepl("^[0-9a-f]{64}$", record$source_content_sha256)) {
    stop("source_content_sha256 must be a sha256")
  }
  if (!is.list(record$assigned_to)) stop("assigned_to must be a list")
  if (!is.list(record$events)) stop("events must be a list")
  invisible(record)
}

`%||%` <- function(a, b) if (is.null(a)) b else a
