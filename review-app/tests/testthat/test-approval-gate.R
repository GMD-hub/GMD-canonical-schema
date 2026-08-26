valid_gate_record <- function() {
  source_sha <- paste(rep("a", 40), collapse = "")
  digest <- paste(rep("b", 64), collapse = "")
  record <- new_review_record_v2(
    artifact_id = "VAR-test", queue_id = "test-queue",
    source_artifact_path = "extraction/20_drafts/dem/VAR-test.md",
    source_commit = source_sha, source_artifact_blob_sha = source_sha,
    source_content_sha256 = digest, enrolled_body_sha256 = digest,
    enrolled_at = "2026-08-25T12:00:00Z", enrolled_by = "reviewer@example.org",
    state = "in-review"
  )
  record$assessment <- list(
    assessment_schema_version = "1.0",
    binding = list(
      source_commit = source_sha, source_artifact_blob_sha = source_sha,
      source_content_sha256 = digest, body_sha256 = digest,
      evidence_commit = source_sha, attestation_blob_sha = source_sha,
      attestation_content_sha256 = digest, context_manifest_sha256 = digest
    ),
    layer1 = list(
      result = "pass", validator_id = "validator+runtime",
      evidence_generated_at = "2026-08-25T12:00:00.123+00:00",
      checked_at = "2026-08-25T12:00:01Z"
    ),
    layer2 = lapply(ASSESSMENT_SECTIONS, function(section) {
      list(section = section, rating = "pass", note = NULL)
    }),
    content_errors = NULL,
    agent_review = list(
      disposition = "findings-present", snapshot_sha256 = digest,
      manifest_identity = "fixture", manifest_digest = digest
    ),
    assessed_by = NULL, assessed_at = NULL
  )
  payload <- list(layer2 = record$assessment$layer2, content_errors = list())
  record$assessment <- stamp_human_assessment(
    record$assessment, payload, "approver@example.org", "2026-08-25T12:01:00Z"
  )
  validate_review_record_v2(record)
  record
}

eligible_manifest <- function() {
  dependency <- list(status = "verified", identity = "fixture", digest = paste(rep("c", 64), collapse = ""))
  blockers <- lapply(QUEUE_GLOBAL_BLOCKER_IDS, function(id) {
    new_queue_blocker(id, "closed fixture", "fixture", status = "closed")
  })
  new_queue_manifest(
    queue_id = "test-queue", created_at = "2026-08-25T12:00:00Z",
    created_by = "test", source_commit = paste(rep("a", 40), collapse = ""),
    source_manifest = dependency, inventory = dependency, agent_review = dependency,
    approval_mode = "enabled",
    approval_enablement = list(
      enabled_at = "2026-08-25T12:00:00Z", enabled_by = "test",
      readiness_command = "fixture", audit_event_id = "fixture"
    ),
    global_blockers = blockers
  )
}

test_that("expanded pending assessment and Release A scaffold are deterministic", {
  pending <- new_pending_assessment()
  expect_no_error(validate_assessment(pending))
  expect_identical(vapply(pending$layer2, `[[`, character(1), "section"), ASSESSMENT_SECTIONS)
  scaffold <- list(
    layer1 = list(status = "pending", evidence_ref = NULL), layer2 = list(),
    content_errors = list(), agent_review = list(status = "pending", evidence_ref = NULL)
  )
  expect_identical(normalize_assessment(scaffold), pending)
})

test_that("exact rubric permits pass and noted revise but rejects failures", {
  record <- valid_gate_record()
  manifest <- eligible_manifest()
  expect_true(queue_approval_eligible(manifest, record))
  record$assessment$layer2[[1L]]$rating <- "revise"
  record$assessment$layer2[[1L]]$note <- "Usable but clarify source wording."
  expect_true(queue_approval_eligible(manifest, record))
  record$assessment$layer2[[1L]]$rating <- "fail"
  expect_false(queue_approval_eligible(manifest, record))
  record$assessment$layer2[[1L]] <- list(
    section = ASSESSMENT_SECTIONS[[1L]], rating = "fail", note = NULL
  )
  expect_error(validate_assessment(record$assessment), "notes are required")
})

test_that("content-error blockers and stale bindings fail closed", {
  record <- valid_gate_record()
  payload <- list(
    layer2 = record$assessment$layer2,
    content_errors = list(list(
      id = "ERR-1", severity = "major", status = "open", evidence_ref = "line 10"
    ))
  )
  record$assessment <- stamp_human_assessment(
    record$assessment, payload, "approver@example.org", "2026-08-25T12:02:00Z"
  )
  expect_false(queue_approval_eligible(eligible_manifest(), record))
  record <- valid_gate_record()
  record$assessment$binding$body_sha256 <- paste(rep("d", 64), collapse = "")
  expect_false(queue_approval_eligible(eligible_manifest(), record))
})

test_that("assessment payload rejects machine-owned injection and missing notes", {
  record <- valid_gate_record()
  payload <- list(layer2 = record$assessment$layer2, content_errors = list(), layer1 = list(result = "pass"))
  expect_error(validate_assessment_payload(payload), "only layer2")
  payload <- list(layer2 = record$assessment$layer2, content_errors = list())
  payload$layer2[[1L]] <- list(
    section = ASSESSMENT_SECTIONS[[1L]], rating = "revise", note = NULL
  )
  expect_error(validate_assessment_payload(payload), "notes are required")
})

test_that("runtime Layer 1 requires exact non-stub sections", {
  front <- "---\nvariable_id: VAR-test\n---\n"
  section <- "This section contains substantive harmonization detail for reviewers. It includes a second actionable sentence."
  body <- paste(vapply(ASSESSMENT_SECTIONS, function(name) {
    paste0("## ", name, "\n\n", section)
  }, character(1)), collapse = "\n\n")
  expect_identical(validate_layer1_body(paste0(front, body), body)$result, "pass")
  expect_identical(validate_layer1_body(paste0(front, body), sub("## Definition", "## Other", body))$result, "fail")
})

test_that("roles and legacy action boundary remain strict", {
  expect_true(authorize("approver", "assessed"))
  expect_false(authorize("reviewer", "assessed"))
  legacy <- new_review_record(
    "VAR-test", "draft.md", current_content_sha256 = paste(rep("a", 64), collapse = ""),
    source_commit = paste(rep("b", 40), collapse = "")
  )
  expect_error(perform_action(
    NULL, legacy, legacy$current_content_sha256, legacy$source_commit,
    legacy$source_commit, "saved", "reviewer@example.org", "reviewer"
  ), "read-only")
})

test_that("detail UI contains namespaced assessment workspace", {
  html <- as.character(mod_detail_ui("detail"))
  expect_match(html, "detail-assessment_workspace", fixed = TRUE)
  expect_match(html, "YAML metadata is read only", fixed = TRUE)
})

test_that("eligibility fails closed across malformed and blocker states", {
  manifest <- eligible_manifest()
  mutate_and_expect <- function(mutator, expected = FALSE) {
    record <- valid_gate_record()
    record <- mutator(record)
    expect_identical(queue_approval_eligible(manifest, record), expected)
  }
  mutate_and_expect(function(x) {
    x$assessment$layer1$result <- "fail"
    x
  })
  mutate_and_expect(function(x) {
    x$assessment$content_errors <- NULL
    x$assessment$assessed_by <- NULL
    x$assessment$assessed_at <- NULL
    x
  })
  mutate_and_expect(function(x) {
    x$assessment$layer2[[1L]]$rating <- "fail"
    x$assessment$layer2[[1L]]$note <- "Confirmed failure."
    x
  })
  for (severity in c("block", "major")) {
    for (status in c("open", "escalated")) {
      mutate_and_expect(function(x) {
        payload <- list(
          layer2 = x$assessment$layer2,
          content_errors = list(list(
            id = "ERR-1", severity = severity, status = status,
            evidence_ref = "line 10"
          ))
        )
        x$assessment <- stamp_human_assessment(
          x$assessment, payload, "approver@example.org",
          "2026-08-25T12:02:00Z"
        )
        x
      })
    }
  }
  mutate_and_expect(function(x) {
    payload <- list(
      layer2 = x$assessment$layer2,
      content_errors = list(list(
        id = "ERR-1", severity = "major", status = "resolved",
        evidence_ref = "line 10"
      ))
    )
    x$assessment <- stamp_human_assessment(
      x$assessment, payload, "approver@example.org", "2026-08-25T12:02:00Z"
    )
    x
  }, TRUE)
  mutate_and_expect(function(x) {
    x$assessment$agent_review$disposition <- "unavailable"
    x
  }, TRUE)
})

test_that("assessment validation rejects malformed matrices", {
  cases <- list(
    unknown_section = function(x) { x$layer2[[1L]]$section <- "Unknown"; x },
    duplicate_section = function(x) { x$layer2[[2L]]$section <- x$layer2[[1L]]$section; x },
    unknown_rating = function(x) { x$layer2[[1L]]$rating <- "maybe"; x },
    bad_timestamp = function(x) { x$layer1$evidence_generated_at <- "yesterday"; x },
    bad_digest = function(x) { x$binding$context_manifest_sha256 <- "bad"; x }
  )
  for (name in names(cases)) {
    assessment <- valid_gate_record()$assessment
    assessment <- cases[[name]](assessment)
    expect_error(validate_assessment(assessment), info = name)
  }
  payload <- list(
    layer2 = valid_gate_record()$assessment$layer2,
    content_errors = list(list(
      id = "ERR", severity = "critical", status = "open", evidence_ref = "line"
    ))
  )
  expect_error(validate_assessment_payload(payload), "content error item")
})

test_that("role matrix keeps namespaced assessment actions separated", {
  roles <- c("reviewer", "approver", "administrator")
  expected_assess <- c(FALSE, TRUE, FALSE)
  expected_submit <- c(TRUE, FALSE, FALSE)
  expect_identical(unname(vapply(roles, authorize, logical(1), action = "assessed")), expected_assess)
  expect_identical(unname(vapply(roles, authorize, logical(1), action = "submitted")), expected_submit)
  html <- as.character(mod_detail_ui("role_detail"))
  expect_match(html, "role_detail-assessment_workspace", fixed = TRUE)
  expect_false(grepl('id="assessment_workspace"', html, fixed = TRUE))
})

gate_action <- function(fixture, action, role, actor, payload = NULL,
                        record = NULL, body = NULL) {
  loaded <- gate_load(fixture)
  perform_action(
    fixture$adapter, record %||% loaded$record,
    body_sha256 = hash_body(body %||% fixture$body),
    blob_sha = loaded$blob_sha, branch_head_sha = loaded$head,
    action = action, actor = actor, role = role,
    approved_content = if (action == "approved") gate_source() else NULL,
    body = if (action == "saved") body %||% fixture$body else NULL,
    assessment_payload = payload,
    expected_manifest_blob_sha = loaded$manifest_sha,
    expected_index_blob_sha = loaded$index_sha
  )
}

test_that("direct submitted, assessed, and approved actions persist atomically", {
  fixture <- gate_memory_adapter()
  submitted <- gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org"
  )
  expect_true(submitted$report$ok)
  after_submit <- gate_load(fixture)$record
  expect_identical(after_submit$state, "in-review")
  expect_identical(after_submit$assessment$layer1$result, "pass")
  expect_identical(after_submit$assessment$binding$evidence_commit,
                   fixture$env$default_head)

  assessed <- gate_action(
    fixture, "assessed", "approver", "approver@example.org",
    gate_payload(after_submit)
  )
  expect_true(assessed$report$ok)
  after_assess <- gate_load(fixture)$record
  expect_identical(after_assess$state, "in-review")
  expect_identical(after_assess$assessment$assessed_by, "approver@example.org")
  expect_true(assessment_approval_complete(after_assess$assessment, after_assess))

  approved <- gate_action(
    fixture, "approved", "approver", "approver@example.org"
  )
  expect_true(approved$report$ok)
  expect_identical(gate_load(fixture)$record$state, "approved")
  approved_path <- approved_path_for(after_assess$source_artifact_path)
  expect_true(approved_path %in% names(fixture$env$commits[[fixture$env$review_head]]))
  expect_identical(fixture$env$patches, 3L)
})

test_that("direct boundary enforces authorization, persisted authority, and payload whitelist", {
  fixture <- gate_memory_adapter()
  before <- fixture$env$review_head
  ineligible <- tryCatch(gate_action(
    fixture, "approved", "approver", "approver@example.org"
  ), error = identity)
  expect_s3_class(ineligible, "error")
  expect_identical(fixture$env$review_head, before)
  expect_error(gate_action(
    fixture, "submitted", "approver", "approver@example.org"
  ), "unauthorized")
  expect_identical(fixture$env$review_head, before)
  loaded <- gate_load(fixture)
  mutated <- loaded$record
  mutated$assigned_to <- "attacker@example.org"
  expect_error(gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org",
    record = mutated
  ), "caller record differs")
  expect_identical(fixture$env$review_head, before)

  expect_true(gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org"
  )$report$ok)
  submitted <- gate_load(fixture)$record
  expect_error(gate_action(
    fixture, "assessed", "reviewer", "reviewer@example.org",
    gate_payload(submitted)
  ), "unauthorized")
  injected <- gate_payload(submitted)
  injected$layer1 <- list(result = "pass")
  before <- fixture$env$review_head
  expect_error(gate_action(
    fixture, "assessed", "approver", "approver@example.org", injected
  ), "only layer2 and content_errors")
  expect_identical(fixture$env$review_head, before)
})

test_that("lazy scaffold migration is serialized by an unrelated authorized write", {
  fixture <- gate_memory_adapter(scaffold = TRUE)
  result <- gate_action(
    fixture, "saved", "reviewer", "reviewer@example.org", body = fixture$body
  )
  expect_true(result$report$ok)
  migrated <- gate_load(fixture)$record$assessment
  expect_identical(migrated$assessment_schema_version, ASSESSMENT_SCHEMA_VERSION)
  expect_length(migrated$layer2, 7L)
  expect_identical(migrated$layer1$result, "pending")
})

test_that("all selected-path races are terminal and publish nothing", {
  race_paths <- c("manifest", "index", "record", "body")
  for (kind in race_paths) {
    fixture <- gate_memory_adapter()
    loaded <- gate_load(fixture)
    before_patches <- fixture$env$patches
    if (kind == "manifest") {
      changed <- fixture$manifest
      changed$created_by <- "concurrent@example.org"
      fixture$mutate_path(QUEUE_MANIFEST_PATH, canonical_yaml(changed))
    } else if (kind == "index") {
      changed <- fixture$index
      changed$rows[[2L]]$assigned_to <- "concurrent@example.org"
      fixture$mutate_path(QUEUE_INDEX_PATH, serialize_queue_index(changed))
    } else if (kind == "record") {
      changed <- loaded$record
      changed$assigned_to <- "concurrent@example.org"
      fixture$mutate_path(ACTION_PATH("VAR-test"), record_to_yaml(changed))
    } else {
      fixture$mutate_path(BODY_PATH("VAR-test"), paste0(fixture$body, "\nConcurrent."))
    }
    result <- tryCatch(
      perform_action(
        fixture$adapter, loaded$record, loaded$body_sha,
        loaded$blob_sha, loaded$head, "submitted",
        "reviewer@example.org", "reviewer",
        expected_manifest_blob_sha = loaded$manifest_sha,
        expected_index_blob_sha = loaded$index_sha
      ), error = identity
    )
    expect_s3_class(result, "error")
    expect_identical(fixture$env$patches, before_patches, info = kind)
  }

  fixture <- gate_memory_adapter()
  expect_true(gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org"
  )$report$ok)
  submitted <- gate_load(fixture)$record
  expect_true(gate_action(
    fixture, "assessed", "approver", "approver@example.org",
    gate_payload(submitted)
  )$report$ok)
  loaded <- gate_load(fixture)
  fixture$env$race <- list(
    stage = "patch", kind = "path",
    path = approved_path_for(loaded$record$source_artifact_path), limit = 1L
  )
  before <- fixture$env$patches
  result <- perform_action(
    fixture$adapter, loaded$record, loaded$body_sha, loaded$blob_sha,
    loaded$head, "approved", "approver@example.org", "approver",
    approved_content = gate_source(),
    expected_manifest_blob_sha = loaded$manifest_sha,
    expected_index_blob_sha = loaded$index_sha
  )
  expect_false(result$report$ok)
  expect_identical(result$report$error$kind, "ref-race")
  expect_identical(fixture$env$patches, before)
})

test_that("source prepublication race is terminal with no reachable publication", {
  fixture <- gate_memory_adapter()
  expect_true(gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org"
  )$report$ok)
  submitted <- gate_load(fixture)$record
  expect_true(gate_action(
    fixture, "assessed", "approver", "approver@example.org",
    gate_payload(submitted)
  )$report$ok)
  before <- fixture$env$patches
  fixture$env$default_reads <- 0L
  fixture$env$race <- list(stage = "prepublish", kind = "source", limit = 1L)
  result <- gate_action(
    fixture, "approved", "approver", "approver@example.org"
  )
  expect_false(result$report$ok)
  expect_identical(result$report$error$kind, "source-drift")
  expect_identical(fixture$env$patches, before)
})

test_that("one unrelated ref race fully rereads and repeated race fails", {
  fixture <- gate_memory_adapter()
  fixture$env$race <- list(stage = "patch", kind = "ref", limit = 1L)
  result <- gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org"
  )
  expect_true(result$report$ok)
  expect_identical(fixture$env$patches, 1L)
  expect_gte(fixture$env$reads$manifest, 3L)
  expect_gte(fixture$env$reads$index, 3L)
  expect_gte(fixture$env$reads$record, 3L)
  expect_gte(fixture$env$reads$body, 2L)

  fixture <- gate_memory_adapter()
  fixture$env$race <- list(stage = "patch", kind = "ref", limit = 2L)
  result <- gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org"
  )
  expect_false(result$report$ok)
  expect_identical(result$report$error$kind, "ref-race")
  expect_identical(fixture$env$patches, 0L)
})

gate_selected_row <- function(fixture) {
  row <- fixture$index$rows[[which(vapply(
    fixture$index$rows, function(item) identical(item$artifact_id, "VAR-test"),
    logical(1)
  ))]]
  lapply(row, function(value) if (is.list(value)) value else value)
}

gate_detail_args <- function(fixture, role, mode = "v2") {
  tree <- fixture$env$commits[[fixture$env$review_head]]
  list(
    id = "detail", adapter = shiny::reactive(fixture$adapter),
    auth = shiny::reactive(list(identity = paste0(role, "@example.org"))),
    role = shiny::reactive(role),
    selected_artifact = shiny::reactive(gate_selected_row(fixture)),
    refresh_counter = shiny::reactiveVal(0L),
    queue_mode = shiny::reactive(mode),
    queue_manifest = shiny::reactive(fixture$manifest),
    queue_manifest_blob_sha = shiny::reactive(tree[[QUEUE_MANIFEST_PATH]]),
    queue_index_blob_sha = shiny::reactive(tree[[QUEUE_INDEX_PATH]]),
    queue_startup = shiny::reactive(NULL)
  )
}

test_that("testServer enforces role-specific assessment persistence controls", {
  fixture <- gate_memory_adapter()
  expect_true(gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org"
  )$report$ok)
  submitted <- gate_load(fixture)$record

  shiny::testServer(mod_detail_server,
    args = gate_detail_args(fixture, "reviewer"), {
      session$flushReact()
      expect_identical(session$returned$phase(), "loaded")
      workspace <- paste(as.character(output$assessment_workspace), collapse = "")
      expect_false(grepl("Save assessment", workspace, fixed = TRUE))
      expect_false(grepl("assessment_rating_definition", workspace, fixed = TRUE))
      expect_match(paste(as.character(output$action_bar), collapse = ""),
                   "No action is available", fixed = TRUE)
    }
  )

  before <- fixture$env$patches
  shiny::testServer(mod_detail_server,
    args = gate_detail_args(fixture, "approver"), {
      session$flushReact()
      workspace <- paste(as.character(output$assessment_workspace), collapse = "")
      expect_match(workspace, "Save assessment", fixed = TRUE)
      values <- list(assessment_content_errors = "[]")
      for (section in ASSESSMENT_SECTIONS) {
        key <- gsub("[^a-z0-9]+", "_", tolower(section))
        values[[paste0("assessment_rating_", key)]] <- "pass"
        values[[paste0("assessment_note_", key)]] <- ""
      }
      do.call(session$setInputs, values)
      session$setInputs(save_assessment = 1L)
      session$flushReact()
      expect_null(session$returned$action_error())
      expect_identical(session$returned$current_record()$assessment$assessed_by,
                       "approver@example.org")
    }
  )
  expect_identical(fixture$env$patches, before + 1L)

  shiny::testServer(mod_detail_server,
    args = gate_detail_args(fixture, "administrator"), {
      session$flushReact()
      workspace <- paste(as.character(output$assessment_workspace), collapse = "")
      expect_false(grepl("Save assessment", workspace, fixed = TRUE))
      expect_false(grepl("assessment_rating_definition", workspace, fixed = TRUE))
    }
  )
})

test_that("testServer dirty assessment suppresses approval until persisted", {
  fixture <- gate_memory_adapter()
  expect_true(gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org"
  )$report$ok)
  submitted <- gate_load(fixture)$record
  expect_true(gate_action(
    fixture, "assessed", "approver", "approver@example.org",
    gate_payload(submitted)
  )$report$ok)
  shiny::testServer(mod_detail_server,
    args = gate_detail_args(fixture, "approver"), {
      session$flushReact()
      expect_match(paste(as.character(output$action_bar), collapse = ""),
                   "Approve", fixed = TRUE)
      session$setInputs(assessment_rating_definition = "revise")
      session$flushReact()
      expect_true(session$returned$assessment_dirty())
      expect_false(grepl(
        "Approve", paste(as.character(output$action_bar), collapse = ""),
        fixed = TRUE
      ))
    }
  )
})

test_that("testServer stale recovery preserves local assessment then reconciles", {
  fixture <- gate_memory_adapter()
  expect_true(gate_action(
    fixture, "submitted", "reviewer", "reviewer@example.org"
  )$report$ok)
  submitted <- gate_load(fixture)$record
  expect_true(gate_action(
    fixture, "assessed", "approver", "approver@example.org",
    gate_payload(submitted)
  )$report$ok)
  shiny::testServer(mod_detail_server,
    args = gate_detail_args(fixture, "approver"), {
      session$flushReact()
      session$setInputs(
        assessment_rating_definition = "revise",
        assessment_note_definition = "Local unsaved reconciliation note.",
        assessment_content_errors = "[]"
      )
      changed <- fixture$index
      changed$rows[[2L]]$assigned_to <- "other@example.org"
      fixture$mutate_path(QUEUE_INDEX_PATH, serialize_queue_index(changed))
      session$setInputs(save_assessment = 1L)
      session$flushReact()
      expect_match(session$returned$action_error(), "changed since load")
      expect_identical(input$assessment_note_definition,
                       "Local unsaved reconciliation note.")
      session$setInputs(confirm_reload = 1L)
      session$flushReact()
      expect_identical(session$returned$phase(), "loaded")
      expect_identical(
        session$returned$current_record()$assessment$layer2[[1L]]$rating,
        "pass"
      )
    }
  )
})

test_that("testServer legacy mode exposes no assessment write controls", {
  fixture <- gate_memory_adapter(state = "in-review")
  shiny::testServer(mod_detail_server,
    args = gate_detail_args(fixture, "approver", mode = "legacy_read_only"), {
      session$flushReact()
      expect_false(any(grepl(
        "Save assessment|Approve|Request revision",
        paste(as.character(output$assessment_workspace),
              as.character(output$action_bar)),
        perl = TRUE
      )))
    }
  )
})
