gate_body <- function() {
  sentence <- paste(
    "This section contains complete harmonization evidence for human review.",
    "A second sentence records an actionable and independently checkable decision."
  )
  paste(vapply(ASSESSMENT_SECTIONS, function(section) {
    paste0("## ", section, "\n\n", sentence)
  }, character(1)), collapse = "\n\n")
}

gate_source <- function() {
  paste0("---\nvariable_id: VAR-test\nmodule_id: MOD-DEM\n---\n", gate_body())
}

gate_payload <- function(record) {
  list(
    layer2 = lapply(ASSESSMENT_SECTIONS, function(section) {
      list(section = section, rating = "pass", note = NULL)
    }),
    content_errors = list()
  )
}

gate_memory_adapter <- function(state = "draft", scaffold = FALSE) {
  env <- new.env(parent = emptyenv())
  env$default_head <- paste(rep("a", 40), collapse = "")
  env$review_head <- paste(rep("b", 40), collapse = "")
  env$blobs <- list()
  env$commits <- list()
  env$trees <- list()
  env$pending_blobs <- list()
  env$parents <- list()
  env$external <- 100L
  env$reads <- list(manifest = 0L, index = 0L, record = 0L, body = 0L)
  env$patches <- 0L
  env$default_reads <- 0L
  env$race <- NULL
  env$race_count <- 0L

  put_blob <- function(content) {
    sha <- git_blob_sha(content)
    env$blobs[[sha]] <- content
    sha
  }
  source <- gate_source()
  source_path <- "extraction/20_drafts/dem/VAR-test.md"
  source_sha <- put_blob(source)
  body <- gate_body()
  body_sha <- put_blob(body)
  context_contents <- list(
    "extraction_pipeline/review_agents/layer1_attestations.py" = "compiler\n",
    "schema/variable.py" = "validator\n",
    "knowledge/rules/dem/RULE-TEST.md" = "rule\n",
    "knowledge/parameters/PARAM-TEST.md" = "parameter\n"
  )
  context_contents[[source_path]] <- source
  context <- lapply(sort(names(context_contents)), function(path) {
    content <- context_contents[[path]]
    list(path = path, git_blob_sha = put_blob(content),
         content_sha256 = source_content_hash(content))
  })
  context_identity <- paste0(vapply(context, function(item) {
    paste0(item$path, "|", item$git_blob_sha, "|", item$content_sha256, "\n")
  }, character(1)), collapse = "")
  attestation <- list(
    schema_version = "1.0", validator_id = "fixture-validator",
    generated_at = "2026-08-25T12:00:00Z",
    context_manifest_sha256 = hash_body(context_identity),
    context_manifest = context,
    artifacts = list(list(
      artifact_id = "VAR-test", source_path = source_path,
      source_git_blob_sha = source_sha,
      source_content_sha256 = source_content_hash(source),
      pydantic_result = "pass"
    ))
  )
  attestation_content <- yaml::as.yaml(attestation, indent.mapping.sequence = TRUE)
  attestation_sha <- put_blob(attestation_content)
  agent_paths <- sprintf(
    "extraction/25_agent_review/VAR-test.%s.yml",
    c("schema_compliance", "source_grounding", "rules_caveats", "consistency_derivation")
  )
  agent_shas <- setNames(lapply(seq_along(agent_paths), function(i) {
    put_blob(yaml::as.yaml(list(
      agent = sub(".*VAR-test[.]|[.]yml$", "", agent_paths[[i]]),
      artifact_id = "VAR-test", checked_at = "2026-08-25T12:00:00Z",
      findings = list(), summary = list(errors = 0L, warnings = 0L, passed = 1L)
    )))
  }), agent_paths)
  main_tree <- setNames(lapply(context, `[[`, "git_blob_sha"),
                        vapply(context, `[[`, character(1), "path"))
  main_tree[[LAYER1_ATTESTATION_PATH]] <- attestation_sha
  for (path in agent_paths) main_tree[[path]] <- agent_shas[[path]]
  env$commits[[env$default_head]] <- main_tree

  record <- new_review_record_v2(
    artifact_id = "VAR-test", queue_id = "test-queue",
    source_artifact_path = source_path, source_commit = env$default_head,
    source_artifact_blob_sha = source_sha,
    source_content_sha256 = source_content_hash(source),
    enrolled_body_sha256 = hash_body(body),
    enrolled_at = "2026-08-25T12:00:00Z",
    enrolled_by = "reviewer@example.org", state = state
  )
  if (scaffold) {
    record$assessment <- list(
      layer1 = list(status = "pending", evidence_ref = NULL), layer2 = list(),
      content_errors = list(),
      agent_review = list(status = "pending", evidence_ref = NULL)
    )
  }
  record_content <- canonical_yaml(record)
  record_sha <- put_blob(record_content)
  modules <- QUEUE_EXPECTED_MODULE_COUNTS
  paths <- character()
  rows <- list()
  for (module in names(modules)) {
    for (i in seq_len(modules[[module]])) {
      id <- if (module == "dem" && i == 1L) "VAR-test" else
        sprintf("VAR-%s%03d", module, i)
      path <- sprintf("extraction/20_drafts/%s/%s.md", module, id)
      paths <- c(paths, path)
      rows[[length(rows) + 1L]] <- new_queue_index_row(
        id, path, module, state = if (id == "VAR-test") state else "draft",
        record_blob_sha = if (id == "VAR-test") record_sha else
          paste0(sprintf("%039x", length(rows)), "1"),
        governance_blocked = FALSE
      )
    }
  }
  dependency <- list(
    status = "verified", identity = "fixture-agent-authority",
    digest = paste(rep("c", 64), collapse = "")
  )
  blockers <- lapply(QUEUE_GLOBAL_BLOCKER_IDS, function(id) {
    new_queue_blocker(id, "closed fixture", "fixture", status = "closed")
  })
  manifest <- new_queue_manifest(
    queue_id = "test-queue", created_at = "2026-08-25T12:00:00Z",
    created_by = "fixture", source_commit = env$default_head,
    expected_path_set_sha256 = queue_path_set_digest(paths),
    source_manifest = dependency, inventory = dependency, agent_review = dependency,
    approval_mode = "enabled",
    approval_enablement = list(
      enabled_at = "2026-08-25T12:00:00Z", enabled_by = "fixture",
      readiness_command = "fixture", audit_event_id = "fixture"
    ), global_blockers = blockers
  )
  index <- list(schema_version = QUEUE_SCHEMA_VERSION,
                queue_id = "test-queue", rows = rows)
  manifest_content <- canonical_yaml(manifest)
  index_content <- serialize_queue_index(index)
  review_tree <- list()
  review_tree[[QUEUE_MANIFEST_PATH]] <- put_blob(manifest_content)
  review_tree[[QUEUE_INDEX_PATH]] <- put_blob(index_content)
  review_tree[[ACTION_PATH("VAR-test")]] <- record_sha
  review_tree[[BODY_PATH("VAR-test")]] <- body_sha
  env$commits[[env$review_head]] <- review_tree

  branch_for_ref <- function(ref) {
    if (ref %in% c("main", env$default_head)) env$default_head else
      if (ref %in% c("review", env$review_head)) env$review_head else ref
  }
  mutate_path <- function(path, content = paste0("race-", path)) {
    tree <- env$commits[[env$review_head]]
    tree[[path]] <- put_blob(content)
    env$external <- env$external + 1L
    env$review_head <- sprintf("%040x", env$external)
    env$commits[[env$review_head]] <- tree
  }
  trigger <- function(stage) {
    race <- env$race
    if (is.null(race) || !identical(race$stage, stage)) return()
    if (!is.null(race$limit) && env$race_count >= race$limit) return()
    env$race_count <- env$race_count + 1L
    if (identical(race$kind, "ref")) {
      old <- env$review_head
      env$external <- env$external + 1L
      env$review_head <- sprintf("%040x", env$external)
      env$commits[[env$review_head]] <- env$commits[[old]]
    } else if (identical(race$kind, "source")) {
      env$default_head <- paste0(sprintf("%039x", env$race_count + 20L), "f")
      changed <- env$commits[[names(env$commits)[[1L]]]]
      changed[[source_path]] <- put_blob(paste0(source, "\nchanged"))
      env$commits[[env$default_head]] <- changed
    } else {
      mutate_path(race$path)
    }
  }
  http <- function(method, url, token, body = NULL) {
    if (method == "GET" && grepl("git/ref/heads/", url)) {
      branch <- sub(".*git/ref/heads/", "", url)
      if (branch == "main") {
        env$default_reads <- env$default_reads + 1L
        if (!is.null(env$race) && identical(env$race$stage, "prepublish") &&
            env$default_reads >= 2L) trigger("prepublish")
      }
      return(list(object = list(sha = if (branch == "main") env$default_head else env$review_head)))
    }
    if (method == "GET" && grepl("git/trees/", url)) {
      commit <- sub(".*git/trees/([^?]+).*", "\\1", url)
      tree <- env$commits[[commit]] %||% list()
      return(list(sha = commit, truncated = FALSE, tree = lapply(names(tree), function(path) {
        list(path = path, type = "blob", sha = tree[[path]])
      })))
    }
    if (method == "GET" && grepl("/git/blobs/", url)) {
      sha <- sub(".*/git/blobs/", "", url)
      content <- env$blobs[[sha]]
      return(list(sha = sha, encoding = "base64",
                  content = base64enc::base64encode(charToRaw(content))))
    }
    if (method == "GET" && grepl("/contents/", url)) {
      match <- regexec("/contents/(.*)[?]ref=(.*)$", url)
      parts <- regmatches(url, match)[[1L]]
      path <- utils::URLdecode(parts[[2L]])
      ref <- utils::URLdecode(parts[[3L]])
      commit <- branch_for_ref(ref)
      if (ref == "review") {
        key <- if (path == QUEUE_MANIFEST_PATH) "manifest" else if
          (path == QUEUE_INDEX_PATH) "index" else if
          (path == ACTION_PATH("VAR-test")) "record" else if
          (path == BODY_PATH("VAR-test")) "body" else NULL
        if (!is.null(key)) env$reads[[key]] <- env$reads[[key]] + 1L
      }
      tree <- env$commits[[commit]] %||% list()
      sha <- tree[[path]]
      if (is.null(sha)) stop("blob not found: ", path)
      content <- env$blobs[[sha]]
      return(list(sha = sha,
                  content = base64enc::base64encode(charToRaw(content))))
    }
    if (method == "POST" && grepl("git/blobs$", url)) {
      content <- rawToChar(base64enc::base64decode(body$content))
      sha <- put_blob(content)
      env$pending_blobs[[sha]] <- content
      return(list(sha = sha))
    }
    if (method == "POST" && grepl("git/trees$", url)) {
      trigger("tree")
      base <- env$commits[[env$review_head]]
      for (entry in body$tree) base[[entry$path]] <- entry$sha
      sha <- paste0(sprintf("%039x", length(env$trees) + 1L), "1")
      env$trees[[sha]] <- base
      return(list(sha = sha))
    }
    if (method == "POST" && grepl("git/commits$", url)) {
      sha <- paste0(sprintf("%039x", length(env$commits) + 1L), "2")
      env$commits[[sha]] <- env$trees[[body$tree]]
      env$parents[[sha]] <- body$parents[[1L]]
      return(list(sha = sha))
    }
    if (method == "PATCH") {
      trigger("patch")
      expected_parent <- body$sha
      commit_tree <- env$commits[[expected_parent]]
      if (is.null(commit_tree) ||
          !identical(env$parents[[expected_parent]], env$review_head)) {
        stop(ref_race_error("non-fast-forward fixture race"))
      }
      env$review_head <- expected_parent
      env$patches <- env$patches + 1L
      return(list(object = list(sha = expected_parent)))
    }
    stop("unhandled fixture request: ", method, " ", url)
  }
  adapter <- new_github_adapter(
    "fixture", "fixture", "main", "review", function() "token", http
  )
  list(adapter = adapter, env = env, record = record, body = body,
       record_sha = record_sha, manifest = manifest, index = index,
       put_blob = put_blob, mutate_path = mutate_path)
}

gate_load <- function(fixture) {
  blob <- adapter_read_review(fixture$adapter, ACTION_PATH("VAR-test"))
  tree <- fixture$env$commits[[fixture$env$review_head]]
  list(
    record = parse_review_record(blob$content), blob_sha = blob$sha,
    body_sha = hash_body(fixture$body),
    manifest_sha = tree[[QUEUE_MANIFEST_PATH]],
    index_sha = tree[[QUEUE_INDEX_PATH]],
    head = adapter_branch_head(
      fixture$adapter$owner, fixture$adapter$repo,
      fixture$adapter$review_branch, fixture$adapter$get_token(),
      fixture$adapter$http
    )
  )
}
