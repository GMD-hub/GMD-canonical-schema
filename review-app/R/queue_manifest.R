# Immutable queue descriptor and temporary production-v2 compatibility.

QUEUE_DESCRIPTOR_PATH <- "extraction/30_review/queue-descriptor.yml"
LEGACY_QUEUE_MANIFEST_PATH <- "extraction/30_review/queue-manifest.yml"
LEGACY_QUEUE_INDEX_PATH <- "extraction/30_review/queue-index.yml"
QUEUE_DESCRIPTOR_SCHEMA_VERSION <- "1.0"
LEGACY_QUEUE_SCHEMA_VERSION <- "1.0"

.queue_error <- function(message) {
  structure(
    list(message = message, call = NULL),
    class = c("queue_contract_error", "error", "condition")
  )
}

.require_queue_scalar <- function(value, field) {
  if (!.is_scalar_character(value)) {
    stop(.queue_error(sprintf(
      "queue field '%s' must be a non-empty string",
      field
    )))
  }
}

queue_path_set_digest <- function(paths) {
  paths <- sort(as.character(paths))
  text <- if (length(paths)) {
    paste0(paste(paths, collapse = "\n"), "\n")
  } else {
    ""
  }
  hash_body(text)
}

queue_record_identity <- function(record) {
  validate_review_record_v2(record)
  list(
    record_schema_version = record$record_schema_version,
    artifact_id = record$artifact_id,
    queue_id = record$queue_id,
    source_artifact_path = record$source_artifact_path,
    source_revision = record$source_commit,
    source_artifact_blob_sha = record$source_artifact_blob_sha,
    source_content_sha256 = record$source_content_sha256,
    enrolled_body_sha256 = record$enrolled_body_sha256,
    enrolled_at = record$enrolled_at,
    enrolled_by = record$enrolled_by
  )
}

queue_record_set_digest <- function(records) {
  if (!is.list(records)) stop(.queue_error("queue records must be a list"))
  identities <- lapply(records, queue_record_identity)
  if (!length(identities)) return(hash_body(""))
  order_index <- order(vapply(
    identities,
    function(identity) identity$artifact_id,
    character(1)
  ))
  lines <- vapply(identities[order_index], function(identity) {
    values <- enc2utf8(unlist(identity, use.names = FALSE))
    paste0(nchar(values, type = "bytes"), ":", values, collapse = "")
  }, character(1))
  hash_body(paste0(paste(lines, collapse = "\n"), "\n"))
}

new_queue_descriptor <- function(
  queue_id,
  source_revision,
  created_at,
  created_by,
  expected_record_count,
  record_set_sha256
) {
  descriptor <- list(
    schema_version = QUEUE_DESCRIPTOR_SCHEMA_VERSION,
    queue_id = queue_id,
    source_revision = source_revision,
    created_at = created_at,
    created_by = created_by,
    expected_record_count = as.integer(expected_record_count),
    record_set_sha256 = record_set_sha256
  )
  validate_queue_descriptor(descriptor)
  class(descriptor) <- c("reviewapp_queue_descriptor", "list")
  descriptor
}

validate_queue_descriptor <- function(descriptor) {
  required <- c(
    "schema_version", "queue_id", "source_revision", "created_at",
    "created_by", "expected_record_count", "record_set_sha256"
  )
  if (!is.list(descriptor)) {
    stop(.queue_error("queue descriptor must be a mapping"))
  }
  missing <- required[!required %in% names(descriptor)]
  if (length(missing)) {
    stop(.queue_error(sprintf(
      "queue descriptor missing required fields: %s",
      paste(missing, collapse = ", ")
    )))
  }
  extra <- setdiff(names(descriptor), required)
  if (length(extra)) {
    stop(.queue_error(sprintf(
      "queue descriptor contains unsupported fields: %s",
      paste(extra, collapse = ", ")
    )))
  }
  if (!identical(
    as.character(descriptor$schema_version),
    QUEUE_DESCRIPTOR_SCHEMA_VERSION
  )) {
    stop(.queue_error(sprintf(
      "unsupported queue descriptor schema version '%s'",
      descriptor$schema_version
    )))
  }
  .require_queue_scalar(descriptor$queue_id, "queue_id")
  .require_queue_scalar(descriptor$created_by, "created_by")
  if (!.is_sha1(descriptor$source_revision)) {
    stop(.queue_error("queue descriptor source_revision must be a Git SHA-1"))
  }
  if (!.is_timestamp(descriptor$created_at)) {
    stop(.queue_error("queue descriptor created_at must be a UTC timestamp"))
  }
  count <- descriptor$expected_record_count
  if (!is.numeric(count) || length(count) != 1L || is.na(count) ||
      as.integer(count) < 1L || count != as.integer(count)) {
    stop(.queue_error(
      "queue descriptor expected_record_count must be a positive integer"
    ))
  }
  if (!.is_sha256(descriptor$record_set_sha256)) {
    stop(.queue_error("queue descriptor record_set_sha256 must be a SHA-256"))
  }
  invisible(descriptor)
}

parse_queue_descriptor <- function(yaml_string) {
  descriptor <- yaml::read_yaml(text = yaml_string)
  validate_queue_descriptor(descriptor)
  class(descriptor) <- c("reviewapp_queue_descriptor", "list")
  descriptor
}

parse_legacy_queue_manifest <- function(yaml_string) {
  manifest <- yaml::read_yaml(text = yaml_string)
  required <- c(
    "schema_version", "queue_id", "created_at", "created_by",
    "source_commit", "expected_total", "expected_path_set_sha256"
  )
  if (!is.list(manifest) || any(!required %in% names(manifest))) {
    stop(.queue_error(
      "legacy queue manifest is missing immutable queue identity fields"
    ))
  }
  if (!identical(
    as.character(manifest$schema_version),
    LEGACY_QUEUE_SCHEMA_VERSION
  )) {
    stop(.queue_error("unsupported legacy queue manifest schema version"))
  }
  .require_queue_scalar(manifest$queue_id, "queue_id")
  .require_queue_scalar(manifest$created_by, "created_by")
  if (!.is_timestamp(manifest$created_at) || !.is_sha1(manifest$source_commit)) {
    stop(.queue_error("legacy queue manifest source identity is invalid"))
  }
  if (!is.numeric(manifest$expected_total) ||
      length(manifest$expected_total) != 1L ||
      is.na(manifest$expected_total) ||
      as.integer(manifest$expected_total) < 1L) {
    stop(.queue_error("legacy queue expected_total must be a positive integer"))
  }
  if (!.is_sha256(manifest$expected_path_set_sha256)) {
    stop(.queue_error("legacy queue path-set identity must be a SHA-256"))
  }
  descriptor <- list(
    schema_version = QUEUE_DESCRIPTOR_SCHEMA_VERSION,
    queue_id = manifest$queue_id,
    source_revision = manifest$source_commit,
    created_at = manifest$created_at,
    created_by = manifest$created_by,
    expected_record_count = as.integer(manifest$expected_total),
    record_set_sha256 = manifest$expected_path_set_sha256
  )
  validate_queue_descriptor(descriptor)
  attr(descriptor, "compatibility_format") <- "production_v2"
  class(descriptor) <- c("reviewapp_queue_descriptor", "list")
  descriptor
}

parse_queue_control <- function(yaml_string, path) {
  if (identical(path, QUEUE_DESCRIPTOR_PATH)) {
    return(parse_queue_descriptor(yaml_string))
  }
  if (identical(path, LEGACY_QUEUE_MANIFEST_PATH)) {
    return(parse_legacy_queue_manifest(yaml_string))
  }
  stop(.queue_error(sprintf("unsupported queue control path '%s'", path)))
}

queue_descriptor_is_legacy <- function(descriptor) {
  identical(attr(descriptor, "compatibility_format"), "production_v2")
}

validate_queue_record_set <- function(records, descriptor) {
  validate_queue_descriptor(descriptor)
  if (!is.list(records)) stop(.queue_error("queue records must be a list"))
  if (length(records) != descriptor$expected_record_count) {
    stop(.queue_error(sprintf(
      "queue record count mismatch: expected %d, found %d",
      descriptor$expected_record_count,
      length(records)
    )))
  }
  ids <- vapply(records, function(record) record$artifact_id, character(1))
  paths <- vapply(
    records,
    function(record) record$source_artifact_path,
    character(1)
  )
  if (anyDuplicated(ids)) {
    stop(.queue_error("queue contains duplicate artifact IDs"))
  }
  if (anyDuplicated(paths)) {
    stop(.queue_error("queue contains duplicate source artifact paths"))
  }
  for (record in records) {
    validate_review_record_v2(record)
    if (!identical(record$queue_id, descriptor$queue_id)) {
      stop(.queue_error(sprintf(
        "record '%s' queue_id does not match the queue descriptor",
        record$artifact_id
      )))
    }
    if (!identical(record$source_commit, descriptor$source_revision)) {
      stop(.queue_error(sprintf(
        "record '%s' source revision does not match the queue descriptor",
        record$artifact_id
      )))
    }
  }
  actual_digest <- if (queue_descriptor_is_legacy(descriptor)) {
    queue_path_set_digest(paths)
  } else {
    queue_record_set_digest(records)
  }
  if (!identical(actual_digest, descriptor$record_set_sha256)) {
    stop(.queue_error("queue record-set digest does not match the descriptor"))
  }
  invisible(records)
}

assessment_approval_complete <- function(assessment) {
  if (is.null(assessment)) return(FALSE)
  tryCatch({
    validate_assessment(assessment)
    identical(assessment$layer1$status, "pass") &&
      length(assessment$layer2) > 0L &&
      all(vapply(assessment$layer2, function(rating) {
        identical(rating$rating, "pass")
      }, logical(1))) &&
      !any(vapply(assessment$content_errors, function(error) {
        identical(error$status, "open") &&
          error$severity %in% c("block", "major")
      }, logical(1))) &&
      identical(assessment$agent_review$status, "pass")
  }, error = function(error) FALSE)
}

queue_approval_eligible <- function(record, source_binding = NULL) {
  validate_review_record_v2(record)
  if (!is.null(source_binding) && !source_binding_is_current(source_binding)) {
    return(FALSE)
  }
  # Task D installs the complete human rubric gate. Approval stays unavailable
  # until that server-side predicate replaces this fail-closed foundation.
  FALSE
}

canonical_yaml <- function(value) {
  yaml::as.yaml(unclass(value), indent = 2)
}

queue_descriptor_digest <- function(descriptor) {
  validate_queue_descriptor(descriptor)
  hash_body(canonical_yaml(descriptor))
}
