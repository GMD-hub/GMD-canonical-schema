# Production queue manifest and compact queue-index row contracts.

QUEUE_MANIFEST_PATH <- "extraction/30_review/queue-manifest.yml"
QUEUE_INDEX_PATH <- "extraction/30_review/queue-index.yml"
QUEUE_SCHEMA_VERSION <- "1.0"
QUEUE_ID <- "cvs-production-2026-08"
QUEUE_EXPECTED_TOTAL <- 267L
QUEUE_EXPECTED_MODULE_COUNTS <- c(
  idn = 9L,
  geo = 14L,
  dem = 24L,
  lbr = 90L,
  utl = 61L,
  dwl = 69L
)
QUEUE_EXPECTED_MODULE_COUNTS_LIST <- as.list(QUEUE_EXPECTED_MODULE_COUNTS)
QUEUE_EXPECTED_PATH_SET_SHA256 <-
  "8fbe8f677f7431be19d34762ee665f33169f07610e5d3abe1b8b7fbbe9da2b1c"
QUEUE_BOOTSTRAP_MAX_PAYLOAD_BYTES <- 8000000L
QUEUE_GLOBAL_BLOCKER_IDS <- c(
  "SOURCE_LOCK_PENDING",
  "SOURCE_INVENTORY_FREEZE_PENDING",
  "RUBRIC_GATE_PENDING",
  "PRODUCTION_CALIBRATION_PENDING"
)

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

new_queue_blocker <- function(
  id, rationale, evidence_ref = NULL, status = "open", artifact_id = NULL
) {
  blocker <- list(
    id = id,
    rationale = rationale,
    evidence_ref = evidence_ref,
    status = status,
    artifact_id = artifact_id
  )
  validate_queue_blocker(blocker)
  blocker
}

validate_queue_blocker <- function(blocker) {
  required <- c("id", "rationale", "evidence_ref", "status", "artifact_id")
  extra <- setdiff(names(blocker), required)
  if (length(extra)) stop(.queue_error(sprintf(
    "queue blocker contains unsupported fields: %s",
    paste(extra, collapse = ", ")
  )))
  missing <- required[!required %in% names(blocker)]
  if (length(missing)) {
    stop(.queue_error(sprintf(
      "queue blocker missing required fields: %s",
      paste(missing, collapse = ", ")
    )))
  }
  .require_queue_scalar(blocker$id, "blocker.id")
  .require_queue_scalar(blocker$rationale, "blocker.rationale")
  if (!(blocker$status %in% c("open", "closed"))) {
    stop(.queue_error("blocker.status must be open or closed"))
  }
  if (!.is_scalar_character(blocker$evidence_ref)) {
    stop(.queue_error("blocker.evidence_ref must be a non-empty string"))
  }
  if (!is.null(blocker$artifact_id) &&
      !is_valid_artifact_id(blocker$artifact_id)) {
    stop(.queue_error("blocker.artifact_id is invalid"))
  }
  invisible(blocker)
}

.pending_dependency <- function() {
  list(status = "pending", identity = NULL, digest = NULL)
}

new_queue_manifest <- function(
  queue_id = QUEUE_ID,
  created_at,
  created_by,
  source_commit,
  expected_total = QUEUE_EXPECTED_TOTAL,
  expected_module_counts = QUEUE_EXPECTED_MODULE_COUNTS_LIST,
  expected_path_set_sha256 = QUEUE_EXPECTED_PATH_SET_SHA256,
  source_manifest = .pending_dependency(),
  inventory = .pending_dependency(),
  agent_review = .pending_dependency(),
  approval_mode = "disabled",
  approval_enablement = NULL,
  global_blockers = lapply(
    QUEUE_GLOBAL_BLOCKER_IDS,
    function(id) {
      evidence <- switch(
        id,
        SOURCE_LOCK_PENDING = "extraction/config/source-manifest.v1.yaml",
        SOURCE_INVENTORY_FREEZE_PENDING = "extraction/20_drafts/runs/inventory-2026-08-13.md",
        RUBRIC_GATE_PENDING = ".cg-docs/calibration/review-rubric.md",
        PRODUCTION_CALIBRATION_PENDING = ".cg-docs/work-reports/2026-08-07-calibrate-human-review.md"
      )
      new_queue_blocker(
        id,
        "Release B control is not complete.",
        evidence_ref = evidence,
        status = "open"
      )
    }
  ),
  artifact_blockers = list()
) {
  if (identical(approval_mode, "enabled") && is.null(approval_enablement)) {
    stop(.queue_error(
      "enabled approval_mode requires a Release B enablement audit"
    ))
  }
  manifest <- list(
    schema_version = QUEUE_SCHEMA_VERSION,
    queue_id = queue_id,
    created_at = created_at,
    created_by = created_by,
    source_commit = source_commit,
    expected_total = as.integer(expected_total),
    expected_module_counts = expected_module_counts,
    expected_path_set_sha256 = expected_path_set_sha256,
    queue_index_path = QUEUE_INDEX_PATH,
    source_manifest = source_manifest,
    inventory = inventory,
    agent_review = agent_review,
    approval_mode = approval_mode,
    approval_enablement = approval_enablement,
    global_blockers = global_blockers,
    artifact_blockers = artifact_blockers
  )
  validate_queue_manifest(manifest)
  class(manifest) <- c("reviewapp_queue_manifest", "list")
  manifest
}

.validate_dependency <- function(value, field) {
  if (!is.list(value)) {
    stop(.queue_error(sprintf("%s must be a mapping", field)))
  }
  required <- c("status", "identity", "digest")
  missing <- required[!required %in% names(value)]
  if (length(missing)) {
    stop(.queue_error(sprintf(
      "%s missing required fields: %s",
      field,
      paste(missing, collapse = ", ")
    )))
  }
  if (!(value$status %in% c("pending", "available", "verified"))) {
    stop(.queue_error(sprintf("%s.status is invalid", field)))
  }
  if (value$status == "pending") {
    if (!is.null(value$identity) || !is.null(value$digest)) {
      stop(.queue_error(sprintf(
        "%s pending status must not invent identity or digest",
        field
      )))
    }
  } else if (!.is_scalar_character(value$identity) ||
             !.is_sha256(value$digest)) {
    stop(.queue_error(sprintf(
      "%s available status requires identity and SHA-256 digest",
      field
    )))
  }
  invisible(value)
}

validate_queue_manifest <- function(manifest) {
  required <- c(
    "schema_version", "queue_id", "created_at", "created_by", "source_commit",
    "expected_total", "expected_module_counts", "expected_path_set_sha256",
    "queue_index_path", "source_manifest", "inventory", "agent_review",
    "approval_mode", "global_blockers", "artifact_blockers"
  )
  missing <- required[!required %in% names(manifest)]
  if (length(missing)) {
    stop(.queue_error(sprintf(
      "queue manifest missing required fields: %s",
      paste(missing, collapse = ", ")
    )))
  }
  allowed <- c(required, "approval_enablement")
  extra <- setdiff(names(manifest), allowed)
  if (length(extra)) stop(.queue_error(sprintf(
    "queue manifest contains unsupported fields: %s",
    paste(extra, collapse = ", ")
  )))
  if (is.null(manifest$approval_enablement)) {
    manifest$approval_enablement <- NULL
  }
  if (!identical(as.character(manifest$schema_version), QUEUE_SCHEMA_VERSION)) {
    stop(.queue_error(sprintf(
      "unsupported queue manifest schema version '%s'",
      manifest$schema_version
    )))
  }
  .require_queue_scalar(manifest$queue_id, "queue_id")
  .require_queue_scalar(manifest$created_by, "created_by")
  if (!.is_timestamp(manifest$created_at) || !.is_sha1(manifest$source_commit)) {
    stop(.queue_error("queue manifest timestamp or source_commit is invalid"))
  }
  if (!is.numeric(manifest$expected_total) ||
      length(manifest$expected_total) != 1L ||
      as.integer(manifest$expected_total) != QUEUE_EXPECTED_TOTAL) {
    stop(.queue_error("queue manifest expected_total must be 267"))
  }
  actual_counts <- unlist(manifest$expected_module_counts)
  if (!setequal(names(actual_counts), names(QUEUE_EXPECTED_MODULE_COUNTS)) ||
      !identical(
        as.integer(actual_counts[names(QUEUE_EXPECTED_MODULE_COUNTS)]),
        as.integer(QUEUE_EXPECTED_MODULE_COUNTS)
      )) {
    stop(.queue_error(
      "queue manifest module counts do not match the Release A set"
    ))
  }
  if (!.is_sha256(manifest$expected_path_set_sha256)) {
    stop(.queue_error("queue manifest path-set identity must be a SHA-256"))
  }
  if (!identical(manifest$queue_index_path, QUEUE_INDEX_PATH)) {
    stop(.queue_error("queue_index_path must point to queue-index.yml"))
  }
  .validate_dependency(manifest$source_manifest, "source_manifest")
  .validate_dependency(manifest$inventory, "inventory")
  .validate_dependency(manifest$agent_review, "agent_review")
  if (!(manifest$approval_mode %in% c("disabled", "enabled"))) {
    stop(.queue_error("approval_mode must be disabled or enabled"))
  }
  if (identical(manifest$approval_mode, "disabled") &&
      !is.null(manifest$approval_enablement)) {
    stop(.queue_error(
      "disabled approval_mode must not contain an enablement audit"
    ))
  }
  if (identical(manifest$approval_mode, "enabled")) {
    enablement <- manifest$approval_enablement
    fields <- c("enabled_at", "enabled_by", "readiness_command", "audit_event_id")
    if (!is.list(enablement) || any(!fields %in% names(enablement)) ||
        !.is_timestamp(enablement$enabled_at) ||
        !.is_scalar_character(enablement$enabled_by) ||
        !.is_scalar_character(enablement$readiness_command) ||
        !.is_scalar_character(enablement$audit_event_id)) {
      stop(.queue_error(
        "enabled approval_mode requires a complete Release B enablement audit"
      ))
    }
    if (length(manifest$global_blockers)) {
      if (any(vapply(manifest$global_blockers, function(blocker) {
        identical(blocker$status, "open")
      }, logical(1)))) {
        stop(.queue_error("approval cannot be enabled while global blockers are open"))
      }
    }
  }
  if (!is.list(manifest$global_blockers)) {
    stop(.queue_error("global_blockers must be a list"))
  }
  global_ids <- vapply(manifest$global_blockers, function(blocker) {
    blocker$id
  }, character(1))
  if (anyDuplicated(global_ids) ||
      !setequal(global_ids, QUEUE_GLOBAL_BLOCKER_IDS)) {
    stop(.queue_error(
      "global_blockers must contain the stable Release B blocker IDs"
    ))
  }
  for (blocker in manifest$global_blockers) validate_queue_blocker(blocker)
  if (!is.list(manifest$artifact_blockers)) {
    stop(.queue_error("artifact_blockers must be a list"))
  }
  artifact_ids <- if (length(manifest$artifact_blockers)) {
    vapply(manifest$artifact_blockers, function(blocker) blocker$id, character(1))
  } else {
    character(0)
  }
  if (length(artifact_ids) && anyDuplicated(artifact_ids)) {
    stop(.queue_error("artifact blocker IDs must be unique"))
  }
  for (blocker in manifest$artifact_blockers) {
    validate_queue_blocker(blocker)
    if (is.null(blocker$artifact_id)) {
      stop(.queue_error("artifact blockers require an explicit artifact_id"))
    }
  }
  if (length(artifact_ids) && any(artifact_ids %in% global_ids)) {
    stop(.queue_error("artifact blocker IDs must not reuse global blocker IDs"))
  }
  invisible(manifest)
}

parse_queue_manifest <- function(yaml_string) {
  manifest <- yaml::read_yaml(text = yaml_string)
  if (!is.list(manifest)) {
    stop(.queue_error("queue manifest must be a mapping"))
  }
  validate_queue_manifest(manifest)
  class(manifest) <- c("reviewapp_queue_manifest", "list")
  manifest
}

queue_open_blockers <- function(manifest, artifact_id = NULL) {
  validate_queue_manifest(manifest)
  blockers <- c(manifest$global_blockers, manifest$artifact_blockers)
  Filter(function(blocker) {
    identical(blocker$status, "open") &&
      (is.null(blocker$artifact_id) || identical(blocker$artifact_id, artifact_id))
  }, blockers)
}

assessment_approval_complete <- function(assessment, record = NULL) {
  if (is.null(assessment)) return(FALSE)
  tryCatch({
    validate_assessment(assessment)
    identical(assessment$layer1$result, "pass") &&
      !is.null(assessment$binding) &&
      (is.null(record) || assessment_binding_matches(assessment, record)) &&
      identical(
        vapply(assessment$layer2, function(rating) rating$section, character(1)),
        ASSESSMENT_SECTIONS
      ) &&
      all(vapply(assessment$layer2, function(rating) {
        identical(rating$rating, "pass") ||
          (identical(rating$rating, "revise") &&
             .is_scalar_character(rating$note))
      }, logical(1))) &&
      !is.null(assessment$content_errors) &&
      !any(vapply(assessment$content_errors$items, function(error) {
        error$status %in% c("open", "escalated") &&
          error$severity %in% c("block", "major")
      }, logical(1)))
  }, error = function(error) FALSE)
}

queue_approval_eligible <- function(manifest, record) {
  tryCatch({
    validate_queue_manifest(manifest)
    validate_review_record_v2(record)
    dependencies <- c(
      manifest$source_manifest$status,
      manifest$inventory$status,
      manifest$agent_review$status
    )
    identical(manifest$approval_mode, "enabled") &&
      all(dependencies %in% c("available", "verified")) &&
      !length(queue_open_blockers(manifest, record$artifact_id)) &&
      assessment_approval_complete(record$assessment, record)
  }, error = function(error) FALSE)
}

index_row_columns <- function() {
  c(
    "artifact_id", "source_artifact_path", "module", "state", "review_round",
    "assigned_to", "record_path", "record_blob_sha", "governance_blocked",
    "source_drift"
  )
}

new_queue_index_row <- function(
  artifact_id,
  source_artifact_path,
  module,
  state = "draft",
  review_round = 1L,
  assigned_to = character(0),
  record_path = NULL,
  record_blob_sha,
  governance_blocked = TRUE,
  source_drift = FALSE
) {
  row <- list(
    artifact_id = artifact_id,
    source_artifact_path = source_artifact_path,
    module = module,
    state = state,
    review_round = as.integer(review_round),
    assigned_to = .normalize_assignments(assigned_to),
    record_path = record_path %||% sprintf(
      "extraction/30_review/%s.review.yml",
      artifact_id
    ),
    record_blob_sha = record_blob_sha,
    governance_blocked = isTRUE(governance_blocked),
    source_drift = source_drift
  )
  validate_queue_index_row(row)
  row
}

validate_queue_index_row <- function(row) {
  required <- index_row_columns()
  extra <- setdiff(names(row), required)
  if (length(extra)) stop(.queue_error(sprintf(
    "queue index row contains unsupported fields: %s",
    paste(extra, collapse = ", ")
  )))
  missing <- required[!required %in% names(row)]
  if (length(missing)) {
    stop(.queue_error(sprintf(
      "queue index row missing required fields: %s",
      paste(missing, collapse = ", ")
    )))
  }
  if (!is_valid_artifact_id(row$artifact_id) ||
      !is_valid_source_artifact_path(
        row$source_artifact_path,
        row$artifact_id
      ) ||
      !identical(row$record_path, sprintf(
        "extraction/30_review/%s.review.yml",
        row$artifact_id
      )) ||
      !.is_sha1(row$record_blob_sha)) {
    stop(.queue_error("queue index row identity or path is invalid"))
  }
  expected_module <- sub(
    "^extraction/20_drafts/([^/]+)/.*$",
    "\\1",
    row$source_artifact_path
  )
  if (!is.character(row$module) || length(row$module) != 1L ||
      !identical(row$module, expected_module)) {
    stop(.queue_error("queue index row module does not match its source path"))
  }
  if (!(row$state %in% STATES) || !is.integer(row$review_round) ||
      row$review_round < 1L) {
    stop(.queue_error("queue index row state or review_round is invalid"))
  }
  if (length(.normalize_assignments(row$assigned_to)) > 0L &&
      any(!vapply(
        .normalize_assignments(row$assigned_to),
        .is_scalar_character,
        logical(1)
      ))) {
    stop(.queue_error("queue index assignments must be identities"))
  }
  if (!is.logical(row$governance_blocked) ||
      length(row$governance_blocked) != 1L ||
      is.na(row$governance_blocked) ||
      !is.logical(row$source_drift) || length(row$source_drift) != 1L ||
      is.na(row$source_drift)) {
    stop(.queue_error("queue index blocker and drift flags must be scalar logicals"))
  }
  invisible(row)
}

queue_index_rows_to_list <- function(index) {
  if (is.null(index)) return(list())
  if (!is.list(index)) stop(.queue_error("queue index rows must be a list"))
  lapply(index, function(row) {
    if ("assigned_to" %in% names(row)) {
      row$assigned_to <- .normalize_assignments(row$assigned_to)
    }
    validate_queue_index_row(row)
    row
  })
}

validate_queue_index <- function(index, manifest = NULL) {
  rows <- queue_index_rows_to_list(index)
  ids <- vapply(rows, function(row) row$artifact_id, character(1))
  if (anyDuplicated(ids)) {
    stop(.queue_error("queue index contains duplicate artifact IDs"))
  }
  if (!is.null(manifest)) {
    validate_queue_manifest(manifest)
    if (length(rows) != manifest$expected_total) {
      stop(.queue_error("queue index total does not match the queue manifest"))
    }
    modules <- vapply(rows, function(row) row$module, character(1))
    actual <- table(factor(
      modules,
      levels = names(QUEUE_EXPECTED_MODULE_COUNTS)
    ))
    expected <- as.integer(
      unlist(manifest$expected_module_counts)[names(QUEUE_EXPECTED_MODULE_COUNTS)]
    )
    if (!identical(as.integer(actual), expected)) {
      stop(.queue_error(
        "queue index module counts do not match the queue manifest"
      ))
    }
    paths <- vapply(rows, function(row) row$source_artifact_path, character(1))
    if (!identical(
      queue_path_set_digest(paths),
      manifest$expected_path_set_sha256
    )) {
      stop(.queue_error(
        "queue index source path set does not match the queue manifest"
      ))
    }
  }
  invisible(rows)
}

canonical_yaml <- function(value) {
  yaml::as.yaml(value, indent = 2)
}

queue_manifest_digest <- function(manifest) {
  hash_body(canonical_yaml(manifest))
}

queue_index_digest <- function(index) {
  hash_body(canonical_yaml(index))
}

parse_queue_index <- function(yaml_string, manifest = NULL) {
  index <- yaml::read_yaml(text = yaml_string)
  required <- c("schema_version", "queue_id", "rows")
  if (!is.list(index) || any(!required %in% names(index)) ||
      !is.list(index$rows)) {
    stop(.queue_error(
      "queue index must contain schema_version, queue_id, and rows"
    ))
  }
  if (!identical(as.character(index$schema_version), QUEUE_SCHEMA_VERSION)) {
    stop(.queue_error("unsupported queue index schema version"))
  }
  .require_queue_scalar(index$queue_id, "queue_id")
  if (!is.null(manifest) && !identical(index$queue_id, manifest$queue_id)) {
    stop(.queue_error("queue index queue_id does not match queue manifest"))
  }
  index$rows <- queue_index_rows_to_list(index$rows)
  validate_queue_index(index$rows, manifest)
  index
}
