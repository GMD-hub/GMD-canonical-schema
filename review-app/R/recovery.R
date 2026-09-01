# Atomic multi-file commit writes with scoped optimistic locking.

`%+%` <- function(a, b) paste0(a, b)

stale_write_error <- function(msg) {
  structure(
    list(message = msg, call = NULL),
    class = c("stale_write", "error", "condition")
  )
}

partial_failure_error <- function(detail) {
  structure(
    list(message = "partial git write failure", detail = detail, call = NULL),
    class = c("partial_failure", "error", "condition")
  )
}

.partial_failure_with_steps <- function(detail, steps) {
  error <- partial_failure_error(detail)
  error$steps_completed <- steps
  error
}

ref_race_error <- function(msg) {
  structure(
    list(message = msg, call = NULL),
    class = c("ref_race", "error", "condition")
  )
}

indeterminate_publication_error <- function(msg, commit_sha) {
  structure(
    list(message = msg, commit_sha = commit_sha, call = NULL),
    class = c("indeterminate_publication", "error", "condition")
  )
}

.expected_blob_matches <- function(actual, expected) {
  if (length(expected) == 1L && is.na(expected)) return(is.null(actual))
  if (is.null(expected)) return(is.null(actual))
  identical(actual, expected)
}

.recoverable_partial <- function(error, steps) {
  if (!inherits(error, "partial_failure")) return(error)
  error$steps_completed <- steps
  error
}

adapter_check_stale <- function(
  adapter, expected_ref_sha = NULL, expected_blob_shas = list(),
  expected_tree = NULL, reject_unrelated_head = FALSE
) {
  owner <- adapter$owner
  repo <- adapter$repo
  branch <- adapter$review_branch
  token <- adapter$get_token()
  current <- adapter_branch_head(owner, repo, branch, token, adapter$http)
  if (!is.null(expected_ref_sha) && !identical(current, expected_ref_sha) &&
      isTRUE(reject_unrelated_head)) {
    stop(stale_write_error(
      "stale, please reload: the review branch HEAD moved since load"
    ))
  }
  tree <- adapter_fetch_tree_at(owner, repo, current, token, adapter$http)
  dependencies <- expected_blob_shas
  if (!is.null(expected_tree)) dependencies <- c(dependencies, expected_tree)
  entries <- tree$entries %||% lapply(tree$blobs, function(sha) {
    list(type = "blob", sha = sha)
  })
  for (path in names(dependencies)) {
    actual <- tree$blobs[[path]] %||% NULL
    expected <- dependencies[[path]]
    expected_absent <- is.null(expected) ||
      (length(expected) == 1L && is.na(expected))
    path_occupied <- any(
      names(entries) == path |
        startsWith(names(entries), paste0(path, "/"))
    )
    if (expected_absent && path_occupied) {
      stop(stale_write_error(sprintf(
        "stale, please reload: path '%s' is no longer absent",
        path
      )))
    }
    if (!.expected_blob_matches(actual, expected)) {
      stop(stale_write_error(sprintf(
        "stale, please reload: blob SHA for '%s' changed since load",
        path
      )))
    }
  }
  tree
}

.write_blob <- function(adapter, path, content, token) {
  response <- adapter$http(
    "POST",
    sprintf("https://api.github.com/repos/%s/%s/git/blobs", adapter$owner, adapter$repo),
    token,
    body = list(
      content = base64enc::base64encode(charToRaw(enc2utf8(content))),
      encoding = "base64"
    )
  )
  if (!.is_scalar_character(response$sha %||% NULL)) {
      stop(partial_failure_error("blob creation returned no valid SHA at path: " %+% path))
  }
  response$sha
}

.assert_writable_adapter <- function(adapter) {
  if (!inherits(adapter, "reviewapp_github_adapter")) {
    stop("review writes require a validated GitHub adapter")
  }
  if (!.is_scalar_character(adapter$default_branch) ||
      !.is_scalar_character(adapter$review_branch)) {
    stop("review writes require configured source and review branches")
  }
  if (isTRUE(adapter$read_only) || identical(adapter$review_branch, "review")) {
    stop("the configured review branch is read-only")
  }
  if (identical(adapter$review_branch, adapter$default_branch)) {
    stop("review writes cannot target the source branch")
  }
  invisible(TRUE)
}

adapter_write_atomic <- function(
  adapter, changes, expected_ref_sha = NULL, expected_blob_shas = list(),
  message, inline_changes = NULL, max_payload_bytes = 900000L,
  reject_unrelated_head = NULL, preflight_tree = NULL,
  pre_publish_check = NULL
) {
  .assert_writable_adapter(adapter)
  if (!is.list(changes) || !length(changes)) stop("atomic write requires changes")
  paths <- names(changes)
  if (is.null(paths) || any(!nzchar(paths)) || anyDuplicated(paths)) {
    stop("atomic write paths must be non-empty and unique")
  }
  if (any(!vapply(changes, function(content) {
    is.null(content) ||
      (is.character(content) && length(content) == 1L && !is.na(content))
  }, logical(1)))) {
    stop("atomic write contents must be scalar text or NULL deletions")
  }
  if (!is.null(pre_publish_check) && !is.function(pre_publish_check)) {
    stop("pre_publish_check must be a function or NULL")
  }
  owner <- adapter$owner
  repo <- adapter$repo
  branch <- adapter$review_branch
  token <- adapter$get_token()
  if (is.null(reject_unrelated_head)) {
    reject_unrelated_head <- TRUE
  }
  if (is.null(preflight_tree)) {
    tree <- adapter_check_stale(
      adapter,
      expected_ref_sha = expected_ref_sha,
      expected_blob_shas = expected_blob_shas,
      reject_unrelated_head = reject_unrelated_head
    )
  } else {
    current <- adapter_branch_head(owner, repo, branch, token, adapter$http)
    if (isTRUE(reject_unrelated_head) &&
        !is.null(expected_ref_sha) && !identical(current, expected_ref_sha)) {
      stop(stale_write_error(
        "stale, please reload: the review branch HEAD moved since load"
      ))
    }
    if (!identical(preflight_tree$commit %||% NULL, current)) {
      stop(stale_write_error(
        "stale, please reload: the preflight review tree is no longer current"
      ))
    }
    tree <- preflight_tree
  }
  payload_changes <- inline_changes %||% NULL
  if (!is.null(payload_changes) &&
      (!is.list(payload_changes) ||
       !identical(sort(names(payload_changes)), sort(paths)))) {
    stop("inline changes must have the same named paths as changes")
  }
  if (is.null(payload_changes)) {
    blob_shas <- list()
    blob_created <- FALSE
    for (path in names(changes)) {
      if (is.null(changes[[path]])) next
      blob_shas[[path]] <- tryCatch(
        .write_blob(adapter, path, changes[[path]], token),
        error = function(error) {
          if (inherits(error, "partial_failure")) {
            stop(.recoverable_partial(
              error,
              if (blob_created) c("staleness-check", "blob-creation") else "staleness-check"
            ))
          }
          stop(.partial_failure_with_steps(
            conditionMessage(error),
            if (blob_created) {
              c("staleness-check", "blob-creation")
            } else {
              "staleness-check"
            }
          ))
        }
      )
      blob_created <- TRUE
    }
    entries <- lapply(names(changes), function(path) {
      if (is.null(changes[[path]])) {
        return(list(path = path, mode = "100644", type = "blob", sha = NULL))
      }
      list(path = path, mode = "100644", type = "blob", sha = blob_shas[[path]])
    })
    completed <- c("staleness-check", "blob-creation")
  } else {
    entries <- lapply(names(payload_changes), function(path) {
      if (is.null(payload_changes[[path]])) {
        return(list(path = path, mode = "100644", type = "blob", sha = NULL))
      }
      list(
        path = path,
        mode = "100644",
        type = "blob",
        content = enc2utf8(payload_changes[[path]])
      )
    })
    completed <- "staleness-check"
  }
  body <- list(base_tree = tree$tree_sha %||% tree$commit, tree = entries)
  encoded_size <- nchar(jsonlite::toJSON(body, auto_unbox = TRUE), type = "bytes")
  if (encoded_size > max_payload_bytes) {
    stop(stale_write_error(sprintf(
      "atomic write payload exceeds configured limit of %d bytes",
      max_payload_bytes
    )))
  }
  response <- tryCatch(
    adapter$http(
      "POST",
      sprintf("https://api.github.com/repos/%s/%s/git/trees", owner, repo),
      token,
      body = body
    ),
    error = function(error) {
      if (inherits(error, "partial_failure")) stop(error)
      stop(.partial_failure_with_steps(conditionMessage(error), completed))
    }
  )
  if (!.is_scalar_character(response$sha %||% NULL)) {
    stop(.partial_failure_with_steps("tree creation failed partway", completed))
  }
  new_tree <- response$sha
  completed <- c(completed, "tree-creation")
  response <- tryCatch(
    adapter$http(
      "POST",
      sprintf("https://api.github.com/repos/%s/%s/git/commits", owner, repo),
      token,
      body = list(
        message = message,
        tree = new_tree,
        parents = list(tree$commit)
      )
    ),
    error = function(error) {
      if (inherits(error, "partial_failure")) stop(error)
      stop(.partial_failure_with_steps(conditionMessage(error), completed))
    }
  )
  if (!.is_scalar_character(response$sha %||% NULL)) {
    stop(.partial_failure_with_steps("commit creation failed partway", completed))
  }
  new_commit <- response$sha
  completed <- c(completed, "commit-creation")
  if (!is.null(pre_publish_check)) {
    tryCatch(
      pre_publish_check(),
      error = function(error) {
        error$steps_completed <- completed
        stop(error)
      }
    )
    completed <- c(completed, "pre-publication-check")
  }
  patch_error <- NULL
  response <- tryCatch(
    adapter$http(
      "PATCH",
      sprintf(
        "https://api.github.com/repos/%s/%s/git/refs/heads/%s",
        owner,
        repo,
        utils::URLencode(branch, reserved = FALSE)
      ),
      token,
      body = list(sha = new_commit, force = FALSE)
    ),
    error = function(error) {
      patch_error <<- error
      NULL
    }
  )
  if (!is.null(patch_error)) {
    current <- tryCatch(
      adapter_branch_head(owner, repo, branch, token, adapter$http),
      error = function(error) NULL
    )
    if (identical(current, new_commit)) {
      response <- list(object = list(sha = new_commit))
    } else if (inherits(patch_error, "ref_race") ||
               grepl(
                 paste0(
                   "409|422|non-fast-forward|fast.?forward|",
                   "reference.*match|not a fast forward"
                 ),
                 conditionMessage(patch_error),
                 ignore.case = TRUE
               )) {
      error <- ref_race_error(conditionMessage(patch_error))
      error$steps_completed <- completed
      stop(error)
    } else if (identical(current, tree$commit)) {
      stop(.partial_failure_with_steps(
        conditionMessage(patch_error),
        completed
      ))
    } else {
      error <- indeterminate_publication_error(
        paste(
          "review ref update result is indeterminate; reconcile the branch",
          "before retrying"
        ),
        new_commit
      )
      error$steps_completed <- completed
      stop(error)
    }
  }
  if (!identical(response$object$sha %||% NULL, new_commit)) {
    current <- tryCatch(
      adapter_branch_head(owner, repo, branch, token, adapter$http),
      error = function(error) NULL
    )
    if (identical(current, new_commit)) {
      response <- list(object = list(sha = new_commit))
    } else if (identical(current, tree$commit)) {
      error <- ref_race_error(
        "review branch ref did not publish the new commit"
      )
      error$steps_completed <- completed
      stop(error)
    } else {
      error <- indeterminate_publication_error(
        paste(
          "review ref response was invalid and publication is indeterminate;",
          "reconcile the branch before retrying"
        ),
        new_commit
      )
      error$steps_completed <- completed
      stop(error)
    }
  }
  completed <- c(completed, "ref-update")
  list(ok = TRUE, commit_sha = new_commit, steps_completed = completed)
}

adapter_write_with_recovery <- function(
  adapter, changes, expected_ref_sha = NULL, expected_blob_shas = list(), message,
  inline_changes = NULL, max_payload_bytes = 900000L,
  reject_unrelated_head = NULL, preflight_tree = NULL,
  pre_publish_check = NULL
) {
  tryCatch(
    {
      result <- adapter_write_atomic(
        adapter,
        changes,
        expected_ref_sha,
        expected_blob_shas,
        message,
        inline_changes = inline_changes,
        max_payload_bytes = max_payload_bytes,
        reject_unrelated_head = reject_unrelated_head,
        preflight_tree = preflight_tree,
        pre_publish_check = pre_publish_check
      )
      list(
        ok = TRUE,
        transition_applied = TRUE,
        commit_sha = result$commit_sha,
        steps_completed = result$steps_completed,
        error = NULL
      )
    },
    stale_write = function(error) {
      list(
        ok = FALSE,
        transition_applied = FALSE,
        commit_sha = NULL,
        steps_completed = error$steps_completed %||% character(0),
        error = list(kind = "stale", message = conditionMessage(error), detail = NULL)
      )
    },
    ref_race = function(error) {
      list(
        ok = FALSE,
        transition_applied = FALSE,
        commit_sha = NULL,
        steps_completed = error$steps_completed %||% c(
          "staleness-check", "blob-creation", "tree-creation", "commit-creation"
        ),
        error = list(kind = "ref-race", message = conditionMessage(error), detail = NULL)
      )
    },
    source_drift = function(error) {
      list(
        ok = FALSE,
        transition_applied = FALSE,
        commit_sha = NULL,
        steps_completed = error$steps_completed %||% character(0),
        error = list(
          kind = "source-drift",
          message = conditionMessage(error),
          detail = NULL
        )
      )
    },
    indeterminate_publication = function(error) {
      list(
        ok = FALSE,
        transition_applied = NA,
        commit_sha = error$commit_sha %||% NULL,
        steps_completed = error$steps_completed %||% character(0),
        error = list(
          kind = "indeterminate",
          message = conditionMessage(error),
          detail = NULL
        )
      )
    },
    partial_failure = function(error) {
      list(
        ok = FALSE,
        transition_applied = FALSE,
        commit_sha = NULL,
        steps_completed = error$steps_completed %||% character(0),
        error = list(
          kind = "partial",
          message = conditionMessage(error),
          detail = error$detail %||% NULL
        )
      )
    },
    error = function(error) {
      list(
        ok = FALSE,
        transition_applied = FALSE,
        commit_sha = NULL,
        steps_completed = error$steps_completed %||% character(0),
        error = list(kind = "other", message = conditionMessage(error), detail = NULL)
      )
    }
  )
}

recovery_report_text <- function(report) {
  if (isTRUE(report$noop)) return("No write was needed; the requested state already exists.")
  if (report$ok) return(sprintf("Write succeeded (commit %s).", report$commit_sha))
  if (report$error$kind == "stale") {
    return(paste(
      "Stale write rejected -- no transition applied. Reload and reapply.",
      report$error$message
    ))
  }
  if (report$error$kind == "ref-race") {
    return(paste(
      "Concurrent publication rejected -- no transition applied.",
      report$error$message
    ))
  }
  if (report$error$kind == "source-drift") {
    return(paste(
      "Source drift rejected publication -- no transition applied.",
      report$error$message
    ))
  }
  if (report$error$kind == "indeterminate") {
    return(paste(
      "Publication result is indeterminate. Do not retry until an operator",
      "reconciles the review branch.",
      report$error$message
    ))
  }
  if (report$error$kind == "partial") {
    return(paste0(
      "PARTIAL FAILURE: transition NOT applied. Completed steps: [",
      paste(report$steps_completed, collapse = ", "), "]. ",
      report$error$message
    ))
  }
  paste("Write failed:", report$error$message)
}
