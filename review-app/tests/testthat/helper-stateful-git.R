.stateful_git_fixture <- function(control = "descriptor_1_1",
                                  state = "approved",
                                  approval_mode = "disabled") {
  env <- new.env(parent = emptyenv())
  env$blobs <- list()
  env$trees <- list()
  env$commits <- list()
  env$counter <- 1000L
  env$patches <- 0L
  env$last_patch <- NULL
  env$fail_patch <- FALSE
  env$corrupt_source_after_commit <- FALSE
  env$corrupt_source_reads <- FALSE
  env$corrupt_blob_sha <- NULL
  env$race_approved <- FALSE

  next_sha <- function() {
    env$counter <- env$counter + 1L
    sprintf("%040x", env$counter)
  }
  put_blob <- function(content) {
    raw <- charToRaw(enc2utf8(content))
    sha <- git_blob_sha_raw(raw)
    env$blobs[[sha]] <- raw
    sha
  }
  put_tree <- function(entries) {
    sha <- next_sha()
    env$trees[[sha]] <- entries
    sha
  }
  put_commit <- function(entries, sha = next_sha(), parent = NULL) {
    tree_sha <- put_tree(entries)
    env$commits[[sha]] <- list(tree_sha = tree_sha, parent = parent)
    sha
  }
  commit_tree <- function(commit) {
    env$trees[[env$commits[[commit]]$tree_sha]]
  }

  source_content <- "---\nvariable_id: VAR-one\n---\nbody"
  source_path <- "extraction/20_drafts/alpha/VAR-one.md"
  source_blob_sha <- put_blob(source_content)
  source_commit <- paste(rep("a", 40L), collapse = "")
  put_commit(
    stats::setNames(list(source_blob_sha), source_path),
    sha = source_commit
  )
  env$source_head <- source_commit

  reviewed_body <- "reviewed body"
  record <- new_review_record_v2(
    artifact_id = "VAR-one",
    queue_id = "stateful-queue",
    source_artifact_path = source_path,
    source_commit = source_commit,
    source_artifact_blob_sha = source_blob_sha,
    source_content_sha256 = hash_body(source_content),
    enrolled_body_sha256 = hash_body("body"),
    current_content_sha256 = hash_body(reviewed_body),
    enrolled_at = "2026-08-24T13:25:07Z",
    enrolled_by = "admin@example.org",
    state = state,
    assigned_to = list("reviewer@example.org"),
    blocker_refs = "BLOCK-1"
  )
  record <- record_action(
    record,
    "saved",
    "reviewer@example.org",
    "reviewer",
    note = "Persist reviewed body.",
    body_sha256 = hash_body(reviewed_body),
    blob_sha = paste(rep("b", 40L), collapse = "")
  )
  record_path <- ACTION_PATH(record$artifact_id)
  body_path <- BODY_PATH(record$artifact_id)
  approved_path <- approved_path_for(record$source_artifact_path)
  record_sha <- put_blob(record_to_yaml(record))
  body_sha <- put_blob(reviewed_body)
  approved_content <- paste0(
    "---\nvariable_id: VAR-one\n---\n",
    reviewed_body
  )
  approved_sha <- put_blob(approved_content)
  review_entries <- list()
  review_entries[record_path] <- list(record_sha)
  review_entries[body_path] <- list(body_sha)
  review_entries[approved_path] <- list(approved_sha)

  if (identical(control, "production_v2")) {
    manifest <- list(
      schema_version = "1.0",
      queue_id = record$queue_id,
      created_at = record$enrolled_at,
      created_by = record$enrolled_by,
      source_commit = record$source_commit,
      expected_total = 1L,
      expected_path_set_sha256 = queue_path_set_digest(source_path),
      approval_mode = approval_mode
    )
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
    review_entries[LEGACY_QUEUE_MANIFEST_PATH] <- list(
      put_blob(canonical_yaml(manifest))
    )
    review_entries[LEGACY_QUEUE_INDEX_PATH] <- list(
      put_blob(canonical_yaml(index))
    )
  } else {
    descriptor <- if (identical(control, "descriptor_1_0")) {
      .queue_descriptor_fixture(list(record), schema_version = "1.0")
    } else {
      .queue_descriptor_fixture(list(record))
    }
    review_entries[QUEUE_DESCRIPTOR_PATH] <- list(
      put_blob(canonical_yaml(descriptor))
    )
  }
  review_head <- paste(rep("c", 40L), collapse = "")
  put_commit(review_entries, sha = review_head)
  env$review_head <- review_head
  env$initial_review_head <- review_head
  env$initial_tree <- commit_tree(review_head)

  resolve_commit <- function(ref) {
    if (identical(ref, "fixture-review")) return(env$review_head)
    if (identical(ref, "main")) return(env$source_head)
    ref
  }
  compete_approved <- function() {
    tree <- commit_tree(env$review_head)
    competitor <- paste0(
      "---\nvariable_id: VAR-one\n---\n",
      "concurrent approved body"
    )
    tree[approved_path] <- list(put_blob(competitor))
    env$review_head <- put_commit(tree, parent = env$review_head)
  }
  add_source_revision <- function(content, commit_sha = next_sha()) {
    blob_sha <- put_blob(content)
    put_commit(
      stats::setNames(list(blob_sha), source_path),
      sha = commit_sha
    )
    list(commit = commit_sha, blob_sha = blob_sha, content = content)
  }
  http <- function(method, url, token, body = NULL) {
    if (identical(method, "GET") && grepl("git/ref/heads/", url)) {
      branch <- utils::URLdecode(sub(".*git/ref/heads/", "", url))
      head <- if (identical(branch, "main")) {
        env$source_head
      } else {
        env$review_head
      }
      return(list(object = list(sha = head)))
    }
    if (identical(method, "GET") && grepl("/git/commits/", url)) {
      sha <- sub(".*/git/commits/", "", url)
      commit <- env$commits[[sha]] %||% NULL
      if (is.null(commit)) stop("commit not found")
      return(list(sha = sha, tree = list(sha = commit$tree_sha)))
    }
    if (identical(method, "GET") && grepl("/git/trees/", url)) {
      object <- sub(".*git/trees/([^?]+).*", "\\1", url)
      if (isTRUE(env$race_approved) && identical(object, env$review_head)) {
        env$race_approved <- FALSE
        compete_approved()
      }
      tree_sha <- if (!is.null(env$commits[[object]])) {
        env$commits[[object]]$tree_sha
      } else {
        object
      }
      tree <- env$trees[[tree_sha]] %||% stop("tree not found")
      entries <- lapply(names(tree), function(path) {
        list(path = path, type = "blob", sha = tree[[path]])
      })
      return(list(sha = tree_sha, truncated = FALSE, tree = entries))
    }
    if (identical(method, "GET") && grepl("/git/blobs/", url)) {
      sha <- sub(".*/git/blobs/", "", url)
      raw <- env$blobs[[sha]] %||% stop("blob not found")
      if (isTRUE(env$corrupt_source_reads) &&
          identical(sha, env$corrupt_blob_sha %||% source_blob_sha)) {
        raw <- c(raw, charToRaw("corrupt"))
      }
      return(list(
        sha = sha,
        encoding = "base64",
        content = base64enc::base64encode(raw)
      ))
    }
    if (identical(method, "GET") && grepl("/contents/", url)) {
      match <- regexec("/contents/(.*)[?]ref=(.*)$", url)
      parts <- regmatches(url, match)[[1L]]
      path <- utils::URLdecode(parts[[2L]])
      commit <- resolve_commit(utils::URLdecode(parts[[3L]]))
      tree <- commit_tree(commit)
      sha <- tree[[path]] %||% stop("blob not found")
      return(list(
        sha = sha,
        content = base64enc::base64encode(env$blobs[[sha]])
      ))
    }
    if (identical(method, "POST") && grepl("/graphql$", url)) {
      matches <- gregexpr(
        "[0-9a-f]{40}:extraction/[0-9A-Za-z_./-]+",
        body$query
      )[[1L]]
      expressions <- regmatches(body$query, list(matches))[[1L]]
      repository <- list()
      for (i in seq_along(expressions)) {
        commit <- sub(":.*$", "", expressions[[i]])
        path <- sub("^[0-9a-f]{40}:", "", expressions[[i]])
        sha <- commit_tree(commit)[[path]] %||% stop("blob not found")
        repository[[sprintf("b%03d", i)]] <- list(
          oid = sha,
          text = rawToChar(env$blobs[[sha]])
        )
      }
      return(list(data = list(repository = repository)))
    }
    if (identical(method, "POST") && grepl("/git/blobs$", url)) {
      raw <- base64enc::base64decode(body$content)
      sha <- git_blob_sha_raw(raw)
      env$blobs[[sha]] <- raw
      return(list(sha = sha))
    }
    if (identical(method, "POST") && grepl("/git/trees$", url)) {
      tree <- env$trees[[body$base_tree]]
      if (is.null(tree) && !is.null(env$commits[[body$base_tree]])) {
        tree <- commit_tree(body$base_tree)
      }
      tree <- tree %||% stop("base tree not found")
      for (entry in body$tree) {
        if (is.null(entry$sha) && is.null(entry$content)) {
          tree[entry$path] <- list(NULL)
        } else if (!is.null(entry$content)) {
          tree[entry$path] <- list(put_blob(entry$content))
        } else {
          tree[entry$path] <- list(entry$sha)
        }
      }
      return(list(sha = put_tree(tree)))
    }
    if (identical(method, "POST") && grepl("/git/commits$", url)) {
      sha <- next_sha()
      env$commits[[sha]] <- list(
        tree_sha = body$tree,
        parent = body$parents[[1L]]
      )
      if (isTRUE(env$corrupt_source_after_commit)) {
        env$corrupt_source_reads <- TRUE
      }
      return(list(sha = sha))
    }
    if (identical(method, "PATCH") && grepl("/git/refs/heads/", url)) {
      if (isTRUE(env$fail_patch)) stop("fixture ref update failure")
      commit <- env$commits[[body$sha]] %||% stop("commit not found")
      if (!identical(commit$parent, env$review_head) || isTRUE(body$force)) {
        stop(ref_race_error("non-fast-forward fixture race"))
      }
      env$review_head <- body$sha
      env$patches <- env$patches + 1L
      env$last_patch <- body
      return(list(object = list(sha = body$sha)))
    }
    stop(sprintf("unexpected fixture request: %s %s", method, url))
  }
  adapter <- new_github_adapter(
    "GMD-hub",
    "fixture",
    "main",
    "fixture-review",
    get_token = function() "secret",
    http = http
  )
  list(
    adapter = adapter,
    env = env,
    record = record,
    record_path = record_path,
    body_path = body_path,
    approved_path = approved_path,
    source_path = source_path,
    source_commit = source_commit,
    source_blob_sha = source_blob_sha,
    add_source_revision = add_source_revision,
    tree = function(commit = env$review_head) commit_tree(commit),
    blob_text = function(sha) rawToChar(env$blobs[[sha]])
  )
}
