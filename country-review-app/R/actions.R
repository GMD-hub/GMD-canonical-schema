# Local persistence and action handlers for country-input reviews.

REVIEW_ROOT <- file.path("extraction", "30_review", "country-inputs")
APPROVED_ROOT <- file.path("extraction", "40_approved", "country-parameters")
COUNTRY_LAYER_ROOT <- file.path("country-parameters", "countries")

ensure_parent_dir <- function(path) {
  parent <- dirname(path)
  if (!dir.exists(parent)) {
    dir.create(parent, recursive = TRUE, showWarnings = FALSE)
  }
}

safe_record_stem <- function(artifact_id) {
  gsub("[^A-Za-z0-9._-]", "_", artifact_id)
}

review_record_path <- function(artifact_id) {
  file.path(REVIEW_ROOT, sprintf("%s.review.yml", safe_record_stem(artifact_id)))
}

review_body_path <- function(artifact_id) {
  file.path(REVIEW_ROOT, sprintf("%s.body.yaml", safe_record_stem(artifact_id)))
}

approved_path_for <- function(item) {
  if (identical(item$artifact_type, "benchmark")) {
    return(NA_character_)
  }
  if (!is_iso3(item$iso3)) {
    stop("cannot compute approved path without valid ISO3")
  }
  base <- basename(item$source_artifact_path)
  file.path(APPROVED_ROOT, item$iso3, base)
}

read_text_file <- function(path) {
  if (!file.exists(path)) return(NULL)
  paste(readLines(path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
}

write_text_file <- function(path, text) {
  ensure_parent_dir(path)
  writeLines(enc2utf8(text), path, useBytes = TRUE)
}

country_parameters_md_path <- function(iso3) {
  file.path(COUNTRY_LAYER_ROOT, iso3, "parameters.md")
}

country_exceptions_md_path <- function(iso3) {
  file.path(COUNTRY_LAYER_ROOT, iso3, "exceptions.md")
}

parse_frontmatter_markdown <- function(path) {
  if (!file.exists(path)) {
    return(list(frontmatter = NULL, body = ""))
  }
  lines <- readLines(path, warn = FALSE, encoding = "UTF-8")
  if (!length(lines) || !identical(trimws(lines[[1L]]), "---")) {
    text <- paste(lines, collapse = "\n")
    return(list(frontmatter = NULL, body = text))
  }
  end_idx <- which(trimws(lines[-1L]) == "---")
  if (!length(end_idx)) {
    text <- paste(lines, collapse = "\n")
    return(list(frontmatter = NULL, body = text))
  }
  fm_end <- end_idx[[1L]] + 1L
  yaml_lines <- lines[2:(fm_end - 1L)]
  body_lines <- if (fm_end < length(lines)) lines[(fm_end + 1L):length(lines)] else character(0)
  fm <- yaml::yaml.load(paste(yaml_lines, collapse = "\n"))
  list(frontmatter = fm, body = paste(body_lines, collapse = "\n"))
}

render_frontmatter_markdown <- function(frontmatter, body = "") {
  fm_yaml <- yaml::as.yaml(frontmatter)
  body_text <- body %||% ""
  if (nzchar(body_text)) {
    paste0("---\n", fm_yaml, "---\n\n", body_text)
  } else {
    paste0("---\n", fm_yaml, "---\n")
  }
}

normalize_scalar <- function(value) {
  if (is.null(value)) return("null")
  if (is.logical(value) && length(value) == 1L) return(if (isTRUE(value)) "true" else "false")
  if (is.numeric(value) && length(value) == 1L) return(format(value, scientific = FALSE, trim = TRUE))
  if (is.character(value) && length(value) == 1L) return(value)
  as.character(value)
}

normalize_mapping <- function(value) {
  if (is.null(value)) return("null")
  if (!is.list(value) || !length(value)) return("null")
  keys <- sort(names(value))
  pairs <- vapply(keys, function(key) {
    sprintf("%s=%s", key, normalize_scalar(value[[key]]))
  }, FUN.VALUE = character(1), USE.NAMES = FALSE)
  paste(pairs, collapse = "|")
}

parameter_record_key <- function(rec) {
  paste(
    rec$parameter_id %||% "",
    normalize_scalar(rec$effective_from),
    normalize_scalar(rec$effective_to),
    normalize_mapping(rec$selectors),
    sep = "||"
  )
}

dedupe_parameter_records <- function(records) {
  out <- list()
  seen <- character(0)
  for (rec in records) {
    key <- parameter_record_key(rec)
    if (key %in% seen) {
      idx <- match(key, seen)
      out[[idx]] <- rec
    } else {
      seen <- c(seen, key)
      out <- c(out, list(rec))
    }
  }
  out
}

dedupe_exception_records <- function(records) {
  out <- list()
  seen <- character(0)
  for (rec in records) {
    key <- rec$exception_id %||% ""
    if (key %in% seen) {
      idx <- match(key, seen)
      out[[idx]] <- rec
    } else {
      seen <- c(seen, key)
      out <- c(out, list(rec))
    }
  }
  out
}

default_country_frontmatter <- function(iso3, type = c("parameters", "exceptions")) {
  type <- match.arg(type)
  fm <- list(
    country_id = sprintf("CTY-%s", iso3),
    iso3 = iso3,
    schema_version = "0.2",
    status = "draft"
  )
  if (identical(type, "parameters")) {
    fm$country_name <- iso3
    fm$parameters <- list()
  } else {
    fm$exceptions <- list()
  }
  fm
}

ensure_country_layer_scaffold <- function(iso3, country_name = NULL) {
  param_path <- country_parameters_md_path(iso3)
  exc_path <- country_exceptions_md_path(iso3)

  if (!file.exists(param_path)) {
    param_fm <- default_country_frontmatter(iso3, "parameters")
    if (.is_scalar_character(country_name)) {
      param_fm$country_name <- country_name
    }
    write_text_file(param_path, render_frontmatter_markdown(param_fm, ""))
  }

  if (!file.exists(exc_path)) {
    exc_fm <- default_country_frontmatter(iso3, "exceptions")
    write_text_file(exc_path, render_frontmatter_markdown(exc_fm, ""))
  }
}

promote_approved_to_country_layer <- function(item, body_text) {
  if (!is_iso3(item$iso3)) {
    stop("cannot promote approved artifact without valid ISO3")
  }
  incoming <- yaml::yaml.load(enc2utf8(body_text %||% ""))
  if (!is.list(incoming)) {
    stop("approved body does not contain valid YAML mapping")
  }

  if (identical(item$artifact_type, "parameter")) {
    if (!is.list(incoming$parameters)) {
      stop("approved parameter artifact missing 'parameters' list")
    }
    ensure_country_layer_scaffold(item$iso3, incoming$country_name %||% NULL)
    target <- country_parameters_md_path(item$iso3)
    parsed <- parse_frontmatter_markdown(target)
    fm <- parsed$frontmatter %||% default_country_frontmatter(item$iso3, "parameters")
    existing <- if (is.list(fm$parameters)) fm$parameters else list()
    merged <- c(existing, incoming$parameters)
    fm$parameters <- dedupe_parameter_records(merged)
    write_text_file(target, render_frontmatter_markdown(fm, parsed$body))
    return(target)
  }

  if (identical(item$artifact_type, "exception")) {
    if (!is.list(incoming$exceptions)) {
      stop("approved exception artifact missing 'exceptions' list")
    }
    ensure_country_layer_scaffold(item$iso3, incoming$country_name %||% NULL)
    target <- country_exceptions_md_path(item$iso3)
    parsed <- parse_frontmatter_markdown(target)
    fm <- parsed$frontmatter %||% default_country_frontmatter(item$iso3, "exceptions")
    existing <- if (is.list(fm$exceptions)) fm$exceptions else list()
    merged <- c(existing, incoming$exceptions)
    fm$exceptions <- dedupe_exception_records(merged)
    write_text_file(target, render_frontmatter_markdown(fm, parsed$body))
    return(target)
  }

  NA_character_
}

load_review_record <- function(item, source_text, actor) {
  path <- review_record_path(item$artifact_id)
  if (!file.exists(path)) {
    return(new_review_record(item, source_text, actor = actor))
  }
  parsed <- yaml::read_yaml(path)
  validate_review_record(parsed)
  parsed
}

save_review_record <- function(rec) {
  validate_review_record(rec)
  path <- review_record_path(rec$artifact_id)
  ensure_parent_dir(path)
  writeLines(yaml::as.yaml(rec), path, useBytes = TRUE)
  path
}

save_body <- function(artifact_id, body_text) {
  path <- review_body_path(artifact_id)
  write_text_file(path, body_text)
  path
}

perform_action <- function(item, record, body_text, action, actor, role, note = NULL) {
  if (identical(item$artifact_type, "benchmark") && action != "saved") {
    stop("benchmark artifacts are read-only references")
  }
  body_sha <- sha256_text(body_text %||% "")

  if (identical(action, "saved")) {
    if (!authorize(role, "saved")) {
      stop(sprintf("role '%s' cannot save", role %||% "(none)"))
    }
    updated <- record_action(record, "saved", actor, role, note = note, content_sha256 = body_sha)
    save_body(item$artifact_id, body_text)
    save_review_record(updated)
    return(updated)
  }

  if (!authorize(role, action)) {
    stop(sprintf("role '%s' cannot perform '%s'", role %||% "(none)", action))
  }

  updated <- transition(record, action, actor, role, note = note, content_sha256 = body_sha)
  save_body(item$artifact_id, body_text)
  save_review_record(updated)

  if (identical(action, "approved") && !identical(item$artifact_type, "benchmark")) {
    approved_path <- approved_path_for(item)
    write_text_file(approved_path, body_text)
    promote_approved_to_country_layer(item, body_text)
  }

  updated
}