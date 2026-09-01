.versioned_queue_http_fixture <- function(use_legacy_control = FALSE) {
  records <- list(
    .queue_record_fixture("VAR-one", "alpha"),
    .queue_record_fixture("VAR-two", "beta"),
    .queue_record_fixture("VAR-three", "gamma")
  )
  contents <- stats::setNames(
    lapply(records, record_to_yaml),
    vapply(records, function(record) ACTION_PATH(record$artifact_id), character(1))
  )
  contents <- contents[order(names(contents))]
  source_contents <- stats::setNames(
    lapply(records, function(record) sprintf(
      "---\nvariable_id: %s\n---\nbody",
      record$artifact_id
    )),
    vapply(records, function(record) record$source_artifact_path, character(1))
  )
  source_contents <- source_contents[order(names(source_contents))]
  if (use_legacy_control) {
    paths <- vapply(records, function(record) {
      record$source_artifact_path
    }, character(1))
    descriptor <- list(
      schema_version = "1.0",
      queue_id = "fixture-queue",
      created_at = "2026-08-24T13:25:07Z",
      created_by = "admin@example.org",
      source_commit = .sha1_fixture,
      expected_total = length(records),
      expected_path_set_sha256 = queue_path_set_digest(paths),
      approval_mode = "disabled"
    )
    control_path <- LEGACY_QUEUE_MANIFEST_PATH
  } else {
    descriptor <- .queue_descriptor_fixture(records)
    control_path <- QUEUE_DESCRIPTOR_PATH
  }
  control_raw <- charToRaw(canonical_yaml(descriptor))
  control_sha <- git_blob_sha_raw(control_raw)
  record_shas <- lapply(contents, git_blob_sha)
  head <- paste(rep("d", 40L), collapse = "")
  calls <- character()
  http <- function(method, url, token, body = NULL) {
    calls <<- c(calls, paste(method, url))
    if (grepl("git/ref/heads/", url) && identical(method, "GET")) {
      return(list(object = list(sha = head)))
    }
    if (grepl("git/commits/", url) && identical(method, "GET")) {
      return(list(
        sha = .sha1_fixture,
        tree = list(sha = paste(rep("f", 40L), collapse = ""))
      ))
    }
    if (grepl("git/trees/", url) && identical(method, "GET")) {
      if (grepl(.sha1_fixture, url, fixed = TRUE)) {
        entries <- lapply(names(source_contents), function(path) {
          list(path = path, type = "blob", sha = git_blob_sha(source_contents[[path]]))
        })
        return(list(
          tree = entries,
          truncated = FALSE,
          sha = paste(rep("f", 40L), collapse = "")
        ))
      }
      entries <- c(
        list(list(path = control_path, type = "blob", sha = control_sha)),
        lapply(names(contents), function(path) {
          list(path = path, type = "blob", sha = record_shas[[path]])
        })
      )
      return(list(tree = entries, truncated = FALSE, sha = paste(rep("e", 40L), collapse = "")))
    }
    if (grepl(paste0("git/blobs/", control_sha), url, fixed = TRUE)) {
      return(list(
        sha = control_sha,
        encoding = "base64",
        content = base64enc::base64encode(control_raw)
      ))
    }
    if (grepl("/graphql$", url) && identical(method, "POST")) {
      selected <- if (grepl("extraction/20_drafts/", body$query, fixed = TRUE)) {
        matches <- gregexpr(
          "extraction/20_drafts/[a-z0-9_-]+/VAR-[a-z0-9]+[.]md",
          body$query
        )[[1L]]
        paths <- regmatches(body$query, list(matches))[[1L]]
        source_contents[paths]
      } else {
        contents
      }
      repository <- list()
      for (i in seq_along(selected)) {
        repository[[sprintf("b%03d", i)]] <- list(
          oid = git_blob_sha(selected[[i]]),
          text = selected[[i]]
        )
      }
      return(list(data = list(repository = repository)))
    }
    stop("unexpected request: ", method, " ", url)
  }
  list(
    http = http,
    calls = function() calls,
    records = records,
    descriptor = descriptor
  )
}

test_that("versioned queues use batched authoritative record reads", {
  fixture <- .versioned_queue_http_fixture()
  adapter <- new_github_adapter(
    "GMD-hub", "fixture", "main", "fixture-review",
    get_token = function() "secret",
    http = fixture$http,
    telemetry = new_repository_read_telemetry()
  )
  result <- adapter_index_review(adapter)
  expect_identical(result$mode, "versioned")
  expect_equal(nrow(result$index), 3L)
  expect_identical(result$request_telemetry$logical_reads, 7L)
  expect_identical(result$request_telemetry$per_record_reads, 0L)
  expect_identical(result$request_telemetry$batch_reads, 2L)
  expect_identical(result$request_telemetry$records_read, 6L)
  expect_false(any(grepl("queue-index", fixture$calls(), fixed = TRUE)))
})

test_that("versioned queue startup rejects a tampered record source identity", {
  fixture <- .versioned_queue_http_fixture()
  http <- function(method, url, token, body = NULL) {
    response <- fixture$http(method, url, token, body)
    if (identical(method, "POST") && grepl("/graphql$", url) &&
        grepl("extraction/20_drafts/", body$query, fixed = TRUE)) {
      response$data$repository$b001$oid <- paste(rep("9", 40L), collapse = "")
    }
    response
  }
  adapter <- new_github_adapter(
    "GMD-hub", "fixture", "main", "fixture-review",
    get_token = function() "secret",
    http = http
  )
  result <- adapter_index_review(adapter)
  expect_identical(result$mode, "queue_error")
  expect_match(result$error, "source Git identity")
})

test_that("record batch count scales with generic queue size", {
  record_count <- 113L
  paths <- sprintf(
    "extraction/30_review/VAR-fixture%03d.review.yml",
    seq_len(record_count)
  )
  batches <- split(paths, ceiling(seq_along(paths) / 50L))
  request <- 0L
  http <- function(method, url, token, body = NULL) {
    request <<- request + 1L
    batch <- batches[[request]]
    repository <- list()
    for (i in seq_along(batch)) {
      repository[[sprintf("b%03d", i)]] <- list(
        oid = paste(rep(sprintf("%x", i %% 16L), 40L), collapse = ""),
        text = sprintf("record %d", i)
      )
    }
    list(data = list(repository = repository))
  }
  adapter <- new_github_adapter(
    "GMD-hub", "fixture", "main", "fixture-review",
    get_token = function() "secret",
    http = http,
    telemetry = new_repository_read_telemetry()
  )
  operation <- repository_telemetry_operation(adapter)
  records <- adapter_fetch_review_records_graphql(
    operation$adapter,
    .sha1_fixture,
    paths
  )
  telemetry <- operation$snapshot()
  expect_length(records, record_count)
  expect_identical(request, 3L)
  expect_identical(telemetry$batch_reads, 3L)
  expect_identical(telemetry$records_read, record_count)
  expect_identical(telemetry$per_record_reads, 0L)
})

test_that("production-v2 controls remain readable without the queue index", {
  fixture <- .versioned_queue_http_fixture(use_legacy_control = TRUE)
  adapter <- new_github_adapter(
    "GMD-hub", "fixture", "main", "fixture-review",
    get_token = function() "secret",
    http = fixture$http
  )
  result <- adapter_index_review(adapter)
  expect_identical(result$mode, "production_v2_read_only")
  expect_true(queue_descriptor_is_legacy(result$descriptor))
  expect_equal(nrow(result$index), 3L)
})

test_that("repository read telemetry is isolated by operation", {
  adapter <- new_github_adapter(
    "GMD-hub", "fixture", "main", "fixture-review",
    get_token = function() "secret",
    http = function(method, url, token, body = NULL) list(),
    telemetry = new_repository_read_telemetry()
  )
  first <- repository_telemetry_operation(adapter)
  second <- repository_telemetry_operation(adapter)
  first$adapter$http(
    "GET",
    "https://api.github.com/repos/o/r/git/trees/a",
    "secret"
  )
  expect_identical(first$snapshot()$logical_reads, 1L)
  expect_identical(second$snapshot()$logical_reads, 0L)
})

test_that("the dashboard has no queue bootstrap UI or handlers", {
  html <- as.character(mod_dashboard_ui("dashboard"))
  expect_false(grepl("bootstrap_queue", html, fixed = TRUE))
  expect_false(grepl("Bootstrap production queue", html, fixed = TRUE))
  server_source <- paste(deparse(body(mod_dashboard_server)), collapse = "\n")
  expect_false(grepl("bootstrap", server_source, ignore.case = TRUE))
  expect_false("bootstrap_production_queue" %in% getNamespaceExports("reviewapp"))
})

test_that("non-administrators cannot initialize a queue", {
  .local_queue_role_map()
  adapter <- new_github_adapter(
    "o", "r", "main", "fixture-review",
    get_token = function() stop("token access is not allowed"),
    http = function(...) stop("network access is not allowed")
  )
  expect_error(
    initialize_review_queue(
      adapter,
      actor = "bbrunckhorst",
      source_revision = .sha1_fixture,
      queue_id = "fixture-queue"
    ),
    "authenticated administrator"
  )
})

test_that("initialization rejects every non-empty governed namespace", {
  .local_queue_role_map()
  adapter <- list(
    owner = "o", repo = "r", review_branch = "fixture-review",
    default_branch = "main", read_only = FALSE,
    get_token = function() "secret", http = function(...) list()
  )
  class(adapter) <- "reviewapp_github_adapter"
  occupied_paths <- c(
    "extraction/30_review/VAR-one.review.yml",
    "extraction/30_review/VAR-one.body.md",
    "extraction/30_review/events/VAR-one.yml",
    "extraction/40_approved/dem/VAR-one.md"
  )
  for (path in occupied_paths) {
    local_mocked_bindings(
      adapter_branch_head = function(...) .sha1_fixture_2,
      adapter_fetch_tree_at = function(...) {
        list(commit = .sha1_fixture_2, blobs = stats::setNames(list("blob"), path))
      },
      .package = "reviewapp"
    )
    expect_error(
      initialize_review_queue(
        adapter,
        actor = "acastanedaa",
        source_revision = .sha1_fixture,
        queue_id = "fixture-queue"
      ),
      "requires an empty review and approved namespace"
    )
  }
})

test_that("initializer publishes one generic descriptor and record set", {
  .local_queue_role_map()
  paths <- c(
    "extraction/20_drafts/alpha/VAR-one.md",
    "extraction/20_drafts/beta/VAR-two.md",
    "extraction/20_drafts/gamma/VAR-three.md"
  )
  contents <- stats::setNames(
    lapply(seq_along(paths), function(i) {
      sprintf("---\nartifact_id: VAR-%s\n---\nbody %d", c("one", "two", "three")[[i]], i)
    }),
    paths
  )
  source_blobs <- lapply(contents, function(content) list(
    content = content,
    raw = charToRaw(content),
    sha = git_blob_sha(content)
  ))
  source_tree <- list(
    commit = .sha1_fixture,
    tree_sha = paste(rep("c", 40L), collapse = ""),
    blobs = lapply(source_blobs, function(blob) blob$sha)
  )
  review_tree <- list(
    commit = .sha1_fixture_2,
    tree_sha = paste(rep("d", 40L), collapse = ""),
    blobs = list(
      "extraction/30_review/.gitkeep" = paste(rep("e", 40L), collapse = "")
    )
  )
  published <- NULL
  local_mocked_bindings(
    adapter_branch_head = function(...) .sha1_fixture_2,
    adapter_fetch_tree_at = function(owner, repo, commit_sha, ...) {
      if (identical(commit_sha, .sha1_fixture)) source_tree else review_tree
    },
    adapter_fetch_commit = function(...) list(
      sha = .sha1_fixture,
      tree_sha = source_tree$tree_sha
    ),
    adapter_fetch_blobs_graphql = function(...) source_blobs,
    adapter_write_with_recovery = function(adapter, changes, ...) {
      published <<- changes
      list(ok = TRUE, commit_sha = paste(rep("f", 40L), collapse = ""))
    },
    .package = "reviewapp"
  )
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    review_branch = "fixture-review", read_only = FALSE,
    get_token = function() "secret", http = function(...) list()
  )
  class(adapter) <- "reviewapp_github_adapter"
  result <- initialize_review_queue(
    adapter,
    actor = "acastanedaa",
    source_revision = .sha1_fixture,
    queue_id = "generic-fixture",
    expected_record_count = length(paths),
    expected_path_set_sha256 = queue_path_set_digest(paths)
  )
  expect_true(result$ok)
  expect_identical(result$record_count, length(paths))
  expect_setequal(
    names(published),
    c(QUEUE_DESCRIPTOR_PATH, vapply(
      c("VAR-one", "VAR-two", "VAR-three"),
      ACTION_PATH,
      character(1)
    ))
  )
  descriptor <- parse_queue_descriptor(published[[QUEUE_DESCRIPTOR_PATH]])
  records <- lapply(setdiff(names(published), QUEUE_DESCRIPTOR_PATH), function(path) {
    parse_review_record(published[[path]])
  })
  expect_no_error(validate_queue_record_set(records, descriptor))
})

test_that("production-v2 migration is deterministic and preserves record blobs", {
  .local_queue_role_map()
  source_content <- "---\nvariable_id: VAR-one\n---\nbody"
  source_raw <- charToRaw(source_content)
  record <- .queue_record_fixture("VAR-one", source_content = source_content)
  record$assigned_to <- list("reviewer@example.org")
  record$blocker_refs <- "BLOCK-1"
  record <- record_action(
    record,
    "saved",
    "reviewer@example.org",
    "reviewer",
    body_sha256 = record$current_content_sha256,
    blob_sha = .sha1_fixture_2
  )
  record_path <- ACTION_PATH(record$artifact_id)
  record_content <- record_to_yaml(record)
  record_sha <- git_blob_sha(record_content)
  manifest <- list(
    schema_version = "1.0",
    queue_id = record$queue_id,
    created_at = record$enrolled_at,
    created_by = record$enrolled_by,
    source_commit = record$source_commit,
    expected_total = 1L,
    expected_path_set_sha256 = queue_path_set_digest(record$source_artifact_path),
    approval_mode = "disabled"
  )
  manifest_content <- canonical_yaml(manifest)
  manifest_sha <- git_blob_sha(manifest_content)
  index <- list(
    schema_version = "1.0",
    queue_id = record$queue_id,
    rows = list(list(
      artifact_id = record$artifact_id,
      source_artifact_path = record$source_artifact_path,
      record_path = record_path,
      record_blob_sha = record_sha
    ))
  )
  index_content <- canonical_yaml(index)
  index_sha <- git_blob_sha(index_content)
  tree <- list(
    commit = .sha1_fixture_2,
    tree_sha = paste(rep("c", 40L), collapse = ""),
    blobs = list()
  )
  tree$blobs[record_path] <- list(record_sha)
  tree$blobs[LEGACY_QUEUE_MANIFEST_PATH] <- list(manifest_sha)
  tree$blobs[LEGACY_QUEUE_INDEX_PATH] <- list(index_sha)
  body_path <- BODY_PATH(record$artifact_id)
  approved_path <- approved_path_for(record$source_artifact_path)
  tree$blobs[body_path] <- list(git_blob_sha("body"))
  tree$blobs[approved_path] <- list(git_blob_sha(source_content))
  source_tree <- list(
    commit = record$source_commit,
    tree_sha = paste(rep("d", 40L), collapse = ""),
    blobs = stats::setNames(
      list(record$source_artifact_blob_sha),
      record$source_artifact_path
    )
  )
  captured <- list()
  local_mocked_bindings(
    adapter_branch_head = function(...) .sha1_fixture_2,
    adapter_fetch_tree_at = function(owner, repo, commit_sha, ...) {
      if (identical(commit_sha, record$source_commit)) source_tree else tree
    },
    adapter_fetch_commit = function(...) list(
      sha = record$source_commit,
      tree_sha = source_tree$tree_sha
    ),
    adapter_fetch_blob_by_sha = function(owner, repo, sha, token, http) {
      content <- if (identical(sha, manifest_sha)) manifest_content else index_content
      list(content = content, sha = sha, raw = charToRaw(content))
    },
    adapter_fetch_review_records_graphql = function(...) {
      stats::setNames(list(list(
        content = record_content,
        sha = record_sha,
        raw = charToRaw(record_content)
      )), record_path)
    },
    adapter_fetch_blobs_graphql = function(...) {
      stats::setNames(list(list(
        content = source_content,
        sha = record$source_artifact_blob_sha,
        raw = source_raw
      )), record$source_artifact_path)
    },
    adapter_write_with_recovery = function(adapter, changes, ...) {
      captured[[length(captured) + 1L]] <<- changes
      list(ok = TRUE, commit_sha = paste(rep("f", 40L), collapse = ""))
    },
    .package = "reviewapp"
  )
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    review_branch = "fixture-review",
    read_only = FALSE, get_token = function() "secret", http = function(...) list()
  )
  class(adapter) <- "reviewapp_github_adapter"
  first <- migrate_review_queue(adapter, "acastanedaa", .sha1_fixture_2)
  second <- migrate_review_queue(adapter, "acastanedaa", .sha1_fixture_2)
  expect_identical(
    captured[[1L]][[QUEUE_DESCRIPTOR_PATH]],
    captured[[2L]][[QUEUE_DESCRIPTOR_PATH]]
  )
  expect_setequal(
    names(captured[[1L]]),
    c(
      QUEUE_DESCRIPTOR_PATH,
      LEGACY_QUEUE_MANIFEST_PATH,
      LEGACY_QUEUE_INDEX_PATH
    )
  )
  expect_identical(first$preserved_record_blobs[[record_path]], record_sha)
  expect_identical(second$descriptor, first$descriptor)
  expect_identical(first$descriptor$schema_version, "1.1")
  expect_false(first$descriptor$approvals_enabled)
  expect_false(body_path %in% names(captured[[1L]]))
  expect_false(approved_path %in% names(captured[[1L]]))
})

test_that("descriptor 1.0 migration replaces only the descriptor", {
  .local_queue_role_map()
  source_content <- "---\nvariable_id: VAR-one\n---\nbody"
  source_raw <- charToRaw(source_content)
  record <- .queue_record_fixture("VAR-one", source_content = source_content)
  record$assigned_to <- list("reviewer@example.org")
  record$blocker_refs <- "BLOCK-1"
  record_path <- ACTION_PATH(record$artifact_id)
  record_content <- record_to_yaml(record)
  record_sha <- git_blob_sha(record_content)
  old_descriptor <- .queue_descriptor_fixture(
    list(record),
    schema_version = "1.0"
  )
  descriptor_content <- canonical_yaml(old_descriptor)
  descriptor_sha <- git_blob_sha(descriptor_content)
  body_path <- BODY_PATH(record$artifact_id)
  approved_path <- approved_path_for(record$source_artifact_path)
  tree <- list(
    commit = .sha1_fixture_2,
    tree_sha = paste(rep("c", 40L), collapse = ""),
    blobs = list()
  )
  tree$blobs[record_path] <- list(record_sha)
  tree$blobs[QUEUE_DESCRIPTOR_PATH] <- list(descriptor_sha)
  tree$blobs[body_path] <- list(git_blob_sha("body"))
  tree$blobs[approved_path] <- list(git_blob_sha(source_content))
  source_tree <- list(
    commit = record$source_commit,
    tree_sha = paste(rep("d", 40L), collapse = ""),
    blobs = stats::setNames(
      list(record$source_artifact_blob_sha),
      record$source_artifact_path
    )
  )
  captured <- NULL
  local_mocked_bindings(
    adapter_branch_head = function(...) .sha1_fixture_2,
    adapter_fetch_tree_at = function(owner, repo, commit_sha, ...) {
      if (identical(commit_sha, record$source_commit)) source_tree else tree
    },
    adapter_fetch_commit = function(...) list(
      sha = record$source_commit,
      tree_sha = source_tree$tree_sha
    ),
    adapter_fetch_blob_by_sha = function(owner, repo, sha, token, http) {
      expect_identical(sha, descriptor_sha)
      list(
        content = descriptor_content,
        sha = sha,
        raw = charToRaw(descriptor_content)
      )
    },
    adapter_fetch_review_records_graphql = function(...) {
      stats::setNames(list(list(
        content = record_content,
        sha = record_sha,
        raw = charToRaw(record_content)
      )), record_path)
    },
    adapter_fetch_blobs_graphql = function(...) {
      stats::setNames(list(list(
        content = source_content,
        sha = record$source_artifact_blob_sha,
        raw = source_raw
      )), record$source_artifact_path)
    },
    adapter_write_with_recovery = function(
      adapter, changes, expected_blob_shas, ...
    ) {
      captured <<- list(changes = changes, expected = expected_blob_shas)
      list(ok = TRUE, commit_sha = paste(rep("f", 40L), collapse = ""))
    },
    .package = "reviewapp"
  )
  adapter <- list(
    owner = "o", repo = "r", default_branch = "main",
    review_branch = "fixture-review", read_only = FALSE,
    get_token = function() "secret", http = function(...) list()
  )
  class(adapter) <- "reviewapp_github_adapter"
  result <- migrate_review_queue(adapter, "acastanedaa", .sha1_fixture_2)
  expect_true(result$ok)
  expect_identical(result$source_format, "descriptor_1_0")
  expect_setequal(names(captured$changes), QUEUE_DESCRIPTOR_PATH)
  expect_identical(captured$expected[[QUEUE_DESCRIPTOR_PATH]], descriptor_sha)
  expect_identical(result$descriptor$schema_version, "1.1")
  expect_false(result$descriptor$approvals_enabled)
  expect_false(body_path %in% names(captured$changes))
  expect_false(approved_path %in% names(captured$changes))
})

test_that("stateful migrations preserve governed blobs and parent history", {
  .local_queue_role_map()
  for (control in c("production_v2", "descriptor_1_0")) {
    fixture <- .stateful_git_fixture(control = control)
    old_head <- fixture$env$review_head
    old_tree <- fixture$tree(old_head)
    old_controls <- if (identical(control, "production_v2")) {
      c(LEGACY_QUEUE_MANIFEST_PATH, LEGACY_QUEUE_INDEX_PATH)
    } else {
      QUEUE_DESCRIPTOR_PATH
    }
    old_control_bytes <- lapply(old_controls, function(path) {
      fixture$blob_text(old_tree[[path]])
    })
    result <- migrate_review_queue(fixture$adapter, "acastanedaa", old_head)
    expect_true(result$ok, info = control)
    expect_false(identical(fixture$env$review_head, old_head), info = control)
    expect_identical(
      fixture$env$commits[[fixture$env$review_head]]$parent,
      old_head,
      info = control
    )
    expect_identical(fixture$env$patches, 1L, info = control)
    expect_identical(fixture$env$last_patch$force, FALSE, info = control)
    new_tree <- fixture$tree()
    for (path in c(
      fixture$record_path,
      fixture$body_path,
      fixture$approved_path
    )) {
      expect_identical(new_tree[[path]], old_tree[[path]], info = paste(control, path))
    }
    descriptor <- parse_queue_descriptor(
      fixture$blob_text(new_tree[[QUEUE_DESCRIPTOR_PATH]])
    )
    expect_identical(descriptor$schema_version, "1.1", info = control)
    expect_false(descriptor$approvals_enabled, info = control)
    if (identical(control, "production_v2")) {
      expect_null(new_tree[[LEGACY_QUEUE_MANIFEST_PATH]])
      expect_null(new_tree[[LEGACY_QUEUE_INDEX_PATH]])
    }
    parent_tree <- fixture$tree(old_head)
    for (i in seq_along(old_controls)) {
      expect_identical(
        fixture$blob_text(parent_tree[[old_controls[[i]]]]),
        old_control_bytes[[i]],
        info = paste(control, old_controls[[i]])
      )
    }
    preserved <- parse_review_record(
      fixture$blob_text(new_tree[[fixture$record_path]])
    )
    expect_identical(preserved$assigned_to, list("reviewer@example.org"))
    expect_identical(preserved$blocker_refs, "BLOCK-1")
    expect_length(preserved$events, 1L)
  }
})

test_that("stateful migration failure preserves exact production-v2 state", {
  .local_queue_role_map()
  fixture <- .stateful_git_fixture(control = "production_v2")
  old_head <- fixture$env$review_head
  old_tree <- fixture$tree(old_head)
  old_bytes <- lapply(old_tree, fixture$blob_text)
  fixture$env$fail_patch <- TRUE
  expect_error(
    migrate_review_queue(fixture$adapter, "acastanedaa", old_head),
    "was not migrated"
  )
  expect_identical(fixture$env$review_head, old_head)
  expect_identical(fixture$env$patches, 0L)
  expect_identical(fixture$tree(old_head), old_tree)
  expect_identical(lapply(fixture$tree(old_head), fixture$blob_text), old_bytes)
})

test_that("production-v2 migration requires explicit disabled approval", {
  .local_queue_role_map()
  for (mode in list("enabled", NULL)) {
    fixture <- .stateful_git_fixture(
      control = "production_v2",
      approval_mode = mode
    )
    old_head <- fixture$env$review_head
    expect_error(
      migrate_review_queue(fixture$adapter, "acastanedaa", old_head),
      "approval_mode to be disabled"
    )
    expect_identical(fixture$env$review_head, old_head)
    expect_identical(fixture$env$patches, 0L)
  }
})

test_that("migration rejects invalid expected heads before authentication", {
  adapter <- new_github_adapter(
    "o", "r", "main", "fixture-review",
    get_token = function() stop("token access is not allowed"),
    http = function(...) stop("network access is not allowed")
  )
  expect_error(
    migrate_review_queue(
      adapter,
      "acastanedaa",
      paste(rep("A", 40L), collapse = "")
    ),
    "expected lowercase Git SHA-1"
  )
})

test_that("migration requires an authenticated administrator", {
  .local_queue_role_map()
  fixture <- .stateful_git_fixture(control = "production_v2")
  old_head <- fixture$env$review_head
  expect_error(
    migrate_review_queue(fixture$adapter, "bbrunckhorst", old_head),
    "authenticated administrator"
  )
  expect_identical(fixture$env$token_calls, 0L)
  expect_identical(fixture$env$review_head, old_head)
  expect_identical(fixture$env$patches, 0L)
})

test_that("expected-head mismatch reads no queue and publishes no commit", {
  .local_queue_role_map()
  fixture <- .stateful_git_fixture(control = "production_v2")
  old_head <- fixture$env$review_head
  commit_count <- length(fixture$env$commits)
  wrong_head <- paste(rep("d", 40L), collapse = "")
  expect_error(
    migrate_review_queue(fixture$adapter, "acastanedaa", wrong_head),
    "operator-supplied expected head"
  )
  expect_identical(fixture$env$review_head, old_head)
  expect_identical(length(fixture$env$commits), commit_count)
  expect_identical(fixture$env$patch_attempts, 0L)
  expect_identical(fixture$env$patches, 0L)
})

test_that("branch race publishes no migration commit", {
  .local_queue_role_map()
  fixture <- .stateful_git_fixture(control = "production_v2")
  old_head <- fixture$env$review_head
  fixture$env$race_approved <- TRUE
  expect_error(
    migrate_review_queue(fixture$adapter, "acastanedaa", old_head),
    "was not migrated"
  )
  expect_false(identical(fixture$env$review_head, old_head))
  expect_identical(fixture$env$review_head, fixture$env$last_competing_commit)
  expect_identical(fixture$env$patch_attempts, 0L)
  expect_identical(fixture$env$patches, 0L)
})
