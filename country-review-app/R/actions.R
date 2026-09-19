# Local persistence and action handlers for country-input reviews.

REVIEW_ROOT <- file.path("extraction", "30_review", "country-inputs")
APPROVED_ROOT <- file.path("extraction", "40_approved", "country-parameters")

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
  }

  updated
}