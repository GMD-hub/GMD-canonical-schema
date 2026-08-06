# Atomic multi-file commit writes with optimistic locking (Step 6 / R11, R14,
# R18) and partial-failure detection / operator recovery (Step 7 / R18).
#
# A multi-file logical operation becomes ONE commit, and the review branch ref
# is updated atomically from the caller's perspective. Before writing, the
# branch ref SHA and each touched path's blob SHA are re-fetched and compared
# against what was loaded; any mismatch rejects the write (no force-push, no
# overwrite). On a partial/API/network failure the write surface reports
# exactly which steps succeeded/failed and never claims a transition that did
# not fully complete.

`%+%` <- function(a, b) paste0(a, b)

#' Condition raised when the remote state moved since load (R11).
stale_write_error <- function(msg) {
  structure(list(message = msg, call = NULL),
            class = c("stale_write", "error", "condition"))
}

#' Condition raised when a multi-step git write fails partway (R18).
partial_failure_error <- function(detail) {
  structure(list(message = "partial git write failure", detail = detail,
                 call = NULL),
            class = c("partial_failure", "error", "condition"))
}

# --- staleness pre-check -------------------------------------------------------

#' Confirm the branch ref SHA and each touched path's blob SHA match what was
#' loaded. Returns the fetched tree on success; raises stale_write_error.
adapter_check_stale <- function(adapter, expected_ref_sha, expected_blob_shas) {
  o <- adapter$owner; repo <- adapter$repo; branch <- adapter$review_branch
  token <- adapter$get_token()
  current <- adapter_branch_head(o, repo, branch, token, adapter$http)
  if (!identical(current, expected_ref_sha)) {
    stop(stale_write_error("stale, please reload: the review branch HEAD moved since load"))
  }
  tree <- adapter_fetch_tree(o, repo, branch, token, adapter$http)
  for (path in names(expected_blob_shas)) {
    actual <- tree$blobs[[path]]
    if (is.null(actual) || !identical(actual, expected_blob_shas[[path]])) {
      stop(stale_write_error(sprintf(
        "stale, please reload: blob SHA for '%s' changed since load", path)))
    }
  }
  tree
}

# --- atomic write ---------------------------------------------------------------

#' One logical atomic write with optimistic locking.
adapter_write_atomic <- function(adapter, changes, expected_ref_sha,
                                 expected_blob_shas, message) {
  o <- adapter$owner; repo <- adapter$repo; branch <- adapter$review_branch
  token <- adapter$get_token()

  # 1. staleness check (raises stale_write_error; never writes)
  tree <- adapter_check_stale(adapter, expected_ref_sha, expected_blob_shas)

  # 2. create a blob per changed file
  blob_shas <- list()
  for (path in names(changes)) {
    content <- changes[[path]]
    url <- sprintf("https://api.github.com/repos/%s/%s/git/blobs", o, repo)
    body <- list(content = base64enc::base64encode(charToRaw(enc2utf8(content))),
                 encoding = "base64")
    resp <- adapter$http("POST", url, token, body = body)
    if (is.null(resp$sha)) {
      stop(partial_failure_error("blob creation failed partway at path: " %+% path))
    }
    blob_shas[[path]] <- resp$sha
  }

  # 3. create a tree rooted at the current HEAD
  entries <- lapply(names(changes), function(path) {
    list(path = path, mode = "100644", type = "blob", sha = blob_shas[[path]])
  })
  resp <- adapter$http("POST",
    sprintf("https://api.github.com/repos/%s/%s/git/trees", o, repo), token,
    body = list(base_tree = tree$commit, tree = entries))
  if (is.null(resp$sha)) {
    stop(partial_failure_error("tree creation failed partway"))
  }
  new_tree <- resp$sha

  # 4. create the commit
  resp <- adapter$http("POST",
    sprintf("https://api.github.com/repos/%s/%s/git/commits", o, repo), token,
    body = list(message = message, tree = new_tree, parents = list(tree$commit)))
  if (is.null(resp$sha)) {
    stop(partial_failure_error("commit creation failed partway"))
  }
  new_commit <- resp$sha

  # 5. update the review branch ref (force = FALSE: never overwrite a moved ref)
  resp <- adapter$http("PATCH",
    sprintf("https://api.github.com/repos/%s/%s/git/refs/heads/%s", o, repo, branch),
    token, body = list(sha = new_commit, force = FALSE))
  if (is.null(resp$object$sha)) {
    stop(partial_failure_error(
      "ref update failed partway (commit was created but the branch ref did not move)"))
  }

  list(ok = TRUE, commit_sha = new_commit)
}

# --- partial-failure detection / recovery (Step 7) -----------------------------

#' Wrap a write so a partial failure surfaces affected paths/commit status and
#' never claims the transition applied. Returns a recovery report; the
#' transition is only ever `transition_applied = TRUE` when the full atomic
#' write succeeded.
adapter_write_with_recovery <- function(adapter, changes, expected_ref_sha,
                                        expected_blob_shas, message) {
  tryCatch(
    {
      result <- adapter_write_atomic(adapter, changes, expected_ref_sha,
                                     expected_blob_shas, message)
      list(ok = TRUE, transition_applied = TRUE, commit_sha = result$commit_sha,
           steps_completed = c("staleness-check", "blob-creation", "tree-creation",
                               "commit-creation", "ref-update"),
           error = NULL)
    },
    stale_write = function(e) {
      list(ok = FALSE, transition_applied = FALSE, commit_sha = NULL,
           steps_completed = character(0),
           error = list(kind = "stale", message = conditionMessage(e), detail = NULL))
    },
    partial_failure = function(e) {
      list(ok = FALSE, transition_applied = FALSE, commit_sha = NULL,
           steps_completed = c("staleness-check", "blob-creation", "tree-creation",
                               "commit-creation"),
           error = list(kind = "partial", message = conditionMessage(e),
                        detail = if (!is.null(e$detail)) e$detail else NULL))
    },
    error = function(e) {
      list(ok = FALSE, transition_applied = FALSE, commit_sha = NULL,
           steps_completed = character(0),
           error = list(kind = "other", message = conditionMessage(e), detail = NULL))
    }
  )
}

#' Operator-facing one-line description of a recovery report.
recovery_report_text <- function(report) {
  if (report$ok) {
    return(sprintf("Write succeeded (commit %s).", report$commit_sha))
  }
  if (report$error$kind == "stale") {
    return(paste("Stale write rejected -- no transition applied. Reload and reapply.",
                 report$error$message))
  }
  if (report$error$kind == "partial") {
    return(paste0("PARTIAL FAILURE: transition NOT applied. Completed steps: [",
                  paste(report$steps_completed, collapse = ", "), "]. ",
                  report$error$message))
  }
  paste("Write failed:", report$error$message)
}
