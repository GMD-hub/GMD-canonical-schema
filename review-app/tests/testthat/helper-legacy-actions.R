.perform_legacy_test_action <- function(
  adapter, rec, body_sha256, blob_sha, branch_head_sha, action, actor, role,
  approved_content = NULL, body = NULL, note = NULL,
  assigned_identities = NULL
) {
  if (!authorize(role, action)) {
    stop(sprintf(
      "unauthorized: role '%s' cannot perform action '%s'",
      role %||% "(none)",
      action
    ))
  }
  updated <- if (action %in% c("saved", "assigned")) {
    record_action(
      rec,
      action,
      actor,
      role,
      note = note,
      body_sha256 = body_sha256,
      blob_sha = blob_sha
    )
  } else {
    transition(
      rec,
      action,
      actor,
      role,
      note = note,
      body_sha256 = body_sha256,
      blob_sha = blob_sha
    )
  }
  if (action == "assigned" && !is.null(assigned_identities)) {
    updated <- set_assigned_to(updated, assigned_identities)
  }
  record_path <- ACTION_PATH(rec$artifact_id)
  changes <- stats::setNames(list(record_to_yaml(updated)), record_path)
  if (action == "approved") {
    if (is.null(approved_content)) {
      stop("performing 'approved' requires approved_content")
    }
    changes[[approved_path_for(rec$source_artifact_path)]] <- approved_content
  }
  if (action == "saved" && !is.null(body)) {
    changes[[BODY_PATH(rec$artifact_id)]] <- body
  }
  report <- adapter_write_with_recovery(
    adapter,
    changes = changes,
    expected_ref_sha = branch_head_sha,
    expected_blob_shas = stats::setNames(list(blob_sha), record_path),
    message = sprintf(
      "legacy fixture action '%s' by %s on %s",
      action,
      actor,
      rec$artifact_id
    ),
    reject_unrelated_head = TRUE
  )
  list(report = report, record = updated)
}
