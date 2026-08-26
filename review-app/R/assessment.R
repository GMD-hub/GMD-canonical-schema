# Human assessment, immutable evidence, and Layer 1 domain helpers.

ASSESSMENT_SCHEMA_VERSION <- "1.0"
LAYER1_ATTESTATION_PATH <-
  "extraction/25_agent_review/evidence/layer1-attestations.v1.yml"
LAYER1_RUNTIME_VALIDATOR_ID <- "reviewapp-layer1-v1"

.is_evidence_timestamp <- function(value) {
  if (!.is_scalar_character(value) || !grepl(
    "^20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$",
    value
  )) return(FALSE)
  normalized <- sub("Z$", "+0000", value)
  normalized <- sub("([+-][0-9]{2}):([0-9]{2})$", "\\1\\2", normalized)
  !is.na(as.POSIXct(normalized, format = "%Y-%m-%dT%H:%M:%OS%z", tz = "UTC"))
}

canonical_utc_timestamp <- function(value) {
  if (!.is_evidence_timestamp(value)) stop("evidence timestamp is not strict RFC 3339")
  normalized <- sub("Z$", "+0000", value)
  normalized <- sub("([+-][0-9]{2}):([0-9]{2})$", "\\1\\2", normalized)
  parsed <- as.POSIXct(normalized, format = "%Y-%m-%dT%H:%M:%OS%z", tz = "UTC")
  format(parsed, tz = "UTC", format = "%Y-%m-%dT%H:%M:%SZ")
}

new_pending_assessment <- function() {
  list(
    assessment_schema_version = ASSESSMENT_SCHEMA_VERSION,
    binding = NULL,
    layer1 = list(
      result = "pending", validator_id = NULL, evidence_generated_at = NULL,
      checked_at = NULL
    ),
    layer2 = lapply(ASSESSMENT_SECTIONS, function(section) {
      list(section = section, rating = NULL, note = NULL)
    }),
    content_errors = NULL,
    agent_review = list(
      disposition = "unavailable", snapshot_sha256 = NULL,
      manifest_identity = NULL, manifest_digest = NULL
    ),
    assessed_by = NULL,
    assessed_at = NULL
  )
}

.is_release_a_assessment <- function(value) {
  identical(value, list(
    layer1 = list(status = "pending", evidence_ref = NULL),
    layer2 = list(), content_errors = list(),
    agent_review = list(status = "pending", evidence_ref = NULL)
  ))
}

normalize_assessment <- function(value) {
  if (.is_release_a_assessment(value)) return(new_pending_assessment())
  value
}

assessment_binding_matches <- function(assessment, record, body_sha256 = NULL) {
  binding <- assessment$binding %||% NULL
  if (!is.list(binding)) return(FALSE)
  expected_body <- body_sha256 %||% record$current_content_sha256
  identical(binding$source_commit, record$source_commit) &&
    identical(binding$source_artifact_blob_sha, record$source_artifact_blob_sha) &&
    identical(binding$source_content_sha256, record$source_content_sha256) &&
    identical(binding$body_sha256, expected_body)
}

validate_layer1_body <- function(enrolled_content, body) {
  split <- split_frontmatter_exact(enrolled_content)
  if (is.null(split$front)) return(list(result = "fail", reason = "YAML front matter is missing"))
  tryCatch(yaml::read_yaml(text = split$front), error = function(error) {
    return(list(result = "fail", reason = "YAML front matter does not parse"))
  }) -> parsed
  if (is.list(parsed) && identical(parsed$result %||% NULL, "fail")) return(parsed)
  failures <- character(0)
  for (section in ASSESSMENT_SECTIONS) {
    pattern <- paste0("(?m)^##[ ]+", gsub("([.()])", "\\\\\\1", section), "[ ]*$")
    hits <- gregexpr(pattern, body, perl = TRUE)[[1L]]
    count <- if (identical(hits[[1L]], -1L)) 0L else length(hits)
    if (count != 1L) {
      failures <- c(failures, sprintf("section '%s' must occur exactly once", section))
      next
    }
    start <- hits[[1L]] + attr(hits, "match.length")[[1L]]
    remainder <- substring(body, start)
    next_heading <- regexpr("(?m)^##[ ]+", remainder, perl = TRUE)[[1L]]
    text <- if (next_heading == -1L) remainder else substring(remainder, 1L, next_heading - 1L)
    compact <- gsub("\\s+", "", text, perl = TRUE)
    sentences <- gregexpr("[.!?](?:\\s|$)", text, perl = TRUE)[[1L]]
    sentence_count <- if (sentences[[1L]] == -1L) 0L else length(sentences)
    if (nchar(compact) <= 50L || sentence_count <= 1L) {
      failures <- c(failures, sprintf("section '%s' is a stub", section))
    }
  }
  if (length(failures)) {
    return(list(result = "fail", reason = paste(failures, collapse = "; ")))
  }
  list(result = "pass", reason = NULL)
}

validate_assessment_payload <- function(payload) {
  if (!is.list(payload) || !identical(sort(names(payload)), c("content_errors", "layer2"))) {
    stop("assessment payload may contain only layer2 and content_errors")
  }
  if (!is.list(payload$layer2) || length(payload$layer2) != length(ASSESSMENT_SECTIONS)) {
    stop("assessment payload requires exactly seven section ratings")
  }
  sections <- vapply(payload$layer2, function(item) item$section %||% "", character(1))
  if (!identical(sections, ASSESSMENT_SECTIONS)) stop("assessment sections are missing, unknown, or out of order")
  for (item in payload$layer2) {
    if (!identical(sort(names(item)), c("note", "rating", "section")) ||
        !(item$rating %in% c("pass", "revise", "fail"))) {
      stop("assessment section rating is invalid")
    }
    if (item$rating %in% c("revise", "fail") &&
        !.is_scalar_character(trimws(item$note %||% ""))) {
      stop("assessment notes are required for revise and fail ratings")
    }
  }
  if (!is.list(payload$content_errors)) stop("content_errors must be a list")
  for (item in payload$content_errors) {
    if (!identical(sort(names(item)), c("evidence_ref", "id", "severity", "status")) ||
        !.is_scalar_character(item$id) ||
        !(item$severity %in% c("block", "major", "minor", "info")) ||
        !(item$status %in% c("open", "resolved", "escalated")) ||
        !.is_scalar_character(item$evidence_ref)) {
      stop("content error item is invalid")
    }
  }
  invisible(payload)
}

stamp_human_assessment <- function(machine_assessment, payload, actor, occurred_at) {
  validate_assessment_payload(payload)
  if (!.is_scalar_character(actor) || !.is_timestamp(occurred_at)) {
    stop("assessment actor or timestamp is invalid")
  }
  updated <- machine_assessment
  updated$layer2 <- payload$layer2
  snapshot <- list(items = payload$content_errors, captured_by = actor, captured_at = occurred_at)
  snapshot$snapshot_sha256 <- hash_body(canonical_yaml(snapshot))
  updated$content_errors <- snapshot
  updated$assessed_by <- actor
  updated$assessed_at <- occurred_at
  validate_assessment(updated)
  updated
}

.attestation_input_path <- function(path) {
  identical(path, "extraction_pipeline/review_agents/layer1_attestations.py") ||
    grepl("^schema/.*[.]py$", path) ||
    grepl("^extraction/20_drafts/(idn|geo|dem|lbr|utl|dwl)/VAR-[a-z0-9]+[.]md$", path) ||
    grepl("^knowledge/rules/.*[.]md$", path) ||
    grepl("^knowledge/parameters/[^/]+[.]md$", path)
}

build_machine_assessment <- function(
  adapter, record, body, binding, evidence_commit = NULL,
  agent_review_authority = NULL
) {
  checked_at <- format(Sys.time(), tz = "UTC", format = "%Y-%m-%dT%H:%M:%SZ")
  if (is.null(evidence_commit)) {
    evidence_commit <- adapter_branch_head(
      adapter$owner, adapter$repo, adapter$default_branch,
      adapter$get_token(), adapter$http
    )
  }
  if (!.is_sha1(evidence_commit)) stop("Layer 1 evidence commit is invalid")
  tree <- adapter_fetch_tree_at(
    adapter$owner, adapter$repo, evidence_commit,
    adapter$get_token(), adapter$http
  )
  attestation_sha <- tree$blobs[[LAYER1_ATTESTATION_PATH]] %||% NULL
  if (!.is_sha1(attestation_sha)) stop("Layer 1 evidence attestation is unavailable")
  blob <- adapter_fetch_blob_by_sha(
    adapter$owner, adapter$repo, attestation_sha,
    adapter$get_token(), adapter$http
  )
  attestation <- tryCatch(
    yaml::read_yaml(text = blob$content),
    error = function(error) stop("Layer 1 evidence attestation is malformed")
  )
  required <- c(
    "schema_version", "validator_id", "generated_at",
    "context_manifest_sha256", "context_manifest", "artifacts"
  )
  if (!is.list(attestation) || any(!required %in% names(attestation)) ||
      !identical(as.character(attestation$schema_version), "1.0") ||
      !.is_evidence_timestamp(attestation$generated_at) ||
      !.is_sha256(attestation$context_manifest_sha256)) {
    stop("Layer 1 evidence attestation contract is invalid")
  }
  manifest <- attestation$context_manifest
  manifest_paths <- vapply(manifest, function(item) item$path, character(1))
  expected_paths <- sort(names(tree$blobs)[vapply(
    names(tree$blobs), .attestation_input_path, logical(1)
  )])
  if (!identical(manifest_paths, expected_paths) || anyDuplicated(manifest_paths)) {
    stop("Layer 1 validator/context path manifest is stale")
  }
  for (item in manifest) {
    if (!identical(tree$blobs[[item$path]], item$git_blob_sha)) {
      stop(sprintf("Layer 1 validator/context blob changed at '%s'", item$path))
    }
    input_blob <- adapter_fetch_blob_by_sha(
      adapter$owner, adapter$repo, item$git_blob_sha,
      adapter$get_token(), adapter$http
    )
    if (!identical(git_blob_sha(input_blob$content), item$git_blob_sha) ||
        !identical(source_content_hash(input_blob$content), item$content_sha256)) {
      stop(sprintf("Layer 1 validator/context content changed at '%s'", item$path))
    }
  }
  manifest_identity <- paste0(vapply(manifest, function(item) {
    paste0(item$path, "|", item$git_blob_sha, "|", item$content_sha256, "\n")
  }, character(1)), collapse = "")
  if (!identical(hash_body(manifest_identity), attestation$context_manifest_sha256)) {
    stop("Layer 1 context manifest digest is invalid")
  }
  matches <- Filter(function(item) {
    identical(item$artifact_id, record$artifact_id)
  }, attestation$artifacts)
  if (length(matches) != 1L) stop("Layer 1 evidence must contain exactly one artifact entry")
  entry <- matches[[1L]]
  if (!identical(entry$source_path, record$source_artifact_path) ||
      !identical(entry$source_git_blob_sha, record$source_artifact_blob_sha) ||
      !identical(entry$source_content_sha256, record$source_content_sha256)) {
    stop("Layer 1 evidence does not match enrolled source identity")
  }
  runtime <- validate_layer1_body(binding$enrolled$content, body)
  result <- if (identical(entry$pydantic_result, "pass") &&
                identical(runtime$result, "pass")) "pass" else "fail"
  agent_paths <- sprintf(
    "extraction/25_agent_review/%s.%s.yml", record$artifact_id,
    c("schema_compliance", "source_grounding", "rules_caveats", "consistency_derivation")
  )
  agent_snapshot <- .build_agent_review_snapshot(
    adapter, tree, agent_paths, agent_review_authority
  )
  list(
    assessment_schema_version = ASSESSMENT_SCHEMA_VERSION,
    binding = list(
      source_commit = record$source_commit,
      source_artifact_blob_sha = record$source_artifact_blob_sha,
      source_content_sha256 = record$source_content_sha256,
      body_sha256 = hash_body(body),
      evidence_commit = evidence_commit,
      attestation_blob_sha = attestation_sha,
      attestation_content_sha256 = source_content_hash(blob$content),
      context_manifest_sha256 = attestation$context_manifest_sha256
    ),
    layer1 = list(
      result = result,
      validator_id = paste(attestation$validator_id, LAYER1_RUNTIME_VALIDATOR_ID, sep = "+"),
      evidence_generated_at = attestation$generated_at,
      checked_at = checked_at
    ),
    layer2 = new_pending_assessment()$layer2,
    content_errors = NULL,
    agent_review = agent_snapshot,
    assessed_by = NULL,
    assessed_at = NULL
  )
}

.build_agent_review_snapshot <- function(adapter, tree, paths, authority) {
  unavailable <- list(
    disposition = "unavailable", snapshot_sha256 = NULL,
    manifest_identity = authority$identity %||% NULL,
    manifest_digest = authority$digest %||% NULL
  )
  if (!is.list(authority) ||
      !.is_scalar_character(authority$identity %||% NULL) ||
      !.is_sha256(authority$digest %||% NULL) ||
      !all(paths %in% names(tree$blobs))) return(unavailable)
  payloads <- lapply(paths, function(path) {
    sha <- tree$blobs[[path]]
    blob <- adapter_fetch_blob_by_sha(
      adapter$owner, adapter$repo, sha,
      adapter$get_token(), adapter$http
    )
    if (!identical(git_blob_sha(blob$content), sha)) {
      stop(sprintf("agent-review blob identity is invalid at '%s'", path))
    }
    parsed <- tryCatch(yaml::read_yaml(text = blob$content), error = function(error) NULL)
    if (!is.list(parsed) || !identical(parsed$artifact_id %||% NULL,
                                       sub("[.][^.]+[.]yml$", "", basename(path))) ||
        !is.list(parsed$findings %||% NULL)) return(NULL)
    list(path = path, sha = sha, content_sha256 = source_content_hash(blob$content),
         findings = parsed$findings)
  })
  if (any(vapply(payloads, is.null, logical(1)))) return(unavailable)
  identity <- list(
    manifest_identity = authority$identity,
    manifest_digest = authority$digest,
    files = lapply(payloads, function(item) item[c("path", "sha", "content_sha256")])
  )
  list(
    disposition = if (any(vapply(payloads, function(item) length(item$findings) > 0L,
                                  logical(1)))) "findings-present" else "clear",
    snapshot_sha256 = hash_body(canonical_yaml(identity)),
    manifest_identity = authority$identity,
    manifest_digest = authority$digest
  )
}
