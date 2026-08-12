# Step 9 -- Dashboard / work-queue index (R4, R15).

library(testthat)

.draft_record_yaml <- function(
  id,
  state = "draft",
  round = 1L,
  assigned = list(),
  path = NULL,
  sha = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
) {
  path <- path %||% sprintf("extraction/20_drafts/dem/%s.md", id)
  assigned_block <- if (length(assigned) == 0L) {
    ""
  } else {
    paste0(paste0("  - ", assigned), collapse = "\n")
  }
  sprintf(
    "artifact_id: %s\nsource_artifact_path: %s\nstate: %s\nreview_round: %d\nassigned_to:\n%scurrent_content_sha256: %s\nsource_commit: abc123\nevents: []\n",
    id,
    path,
    state,
    as.integer(round),
    if (nzchar(assigned_block)) paste0(assigned_block, "\n") else "",
    sha
  )
}

.fixture_records <- function() {
  list(
    list(
      id = "VAR-male",
      yaml_string = .draft_record_yaml("VAR-male", "draft")
    ),
    list(
      id = "VAR-educat7",
      yaml_string = .draft_record_yaml(
        "VAR-educat7",
        "in-review",
        round = 1L,
        assigned = list("approver@example.org")
      )
    ),
    list(
      id = "VAR-urban",
      yaml_string = .draft_record_yaml(
        "VAR-urban",
        "needs-revision",
        round = 1L
      )
    )
  )
}

test_that("index reflects current states across fixture records", {
  idx <- index_review_records(.fixture_records())
  expect_setequal(idx$artifact_id, c("VAR-male", "VAR-educat7", "VAR-urban"))
  expect_identical(idx$state[idx$artifact_id == "VAR-male"], "draft")
  expect_identical(idx$state[idx$artifact_id == "VAR-educat7"], "in-review")
  expect_identical(idx$state[idx$artifact_id == "VAR-urban"], "needs-revision")
})

test_that("a record with malformed YAML surfaces an explicit error row, not silent skip", {
  records <- list(
    list(id = "VAR-good", yaml_string = .draft_record_yaml("VAR-good")),
    list(
      id = "VAR-broken",
      yaml_string = "artifact_id: [unclosed\n  bad: [yaml"
    )
  )
  idx <- index_review_records(records)
  broken <- idx[idx$artifact_id == "VAR-broken", , drop = FALSE]
  expect_identical(broken$state, "ERROR")
  expect_false(is.na(broken$parse_error))
  # the good record is still present
  expect_true("VAR-good" %in% idx$artifact_id)
})

test_that("filters narrow results correctly by module, state, and assignment", {
  idx <- index_review_records(.fixture_records())
  by_state <- filter_review_index(idx, state = "in-review")
  expect_identical(by_state$artifact_id, "VAR-educat7")
  by_assigned <- filter_review_index(idx, assigned_to = "approver@example.org")
  expect_identical(by_assigned$artifact_id, "VAR-educat7")
  none <- filter_review_index(idx, state = "approved")
  expect_equal(nrow(none), 0L)
})

test_that("filters narrow by artifact ID and next step", {
  idx <- index_review_records(.fixture_records())
  by_id <- filter_review_index(idx, artifact_id = "EDUCAT")
  expect_identical(by_id$artifact_id, "VAR-educat7")
  by_step <- filter_review_index(idx, next_step = "Revise")
  expect_identical(by_step$artifact_id, "VAR-urban")
})

test_that("selection resolves against the exact displayed index", {
  idx <- index_review_records(.fixture_records())
  displayed <- filter_review_index(idx, state = "needs-revision")
  selected <- selected_review_artifact(displayed, 1L)
  expect_identical(selected$artifact_id, "VAR-urban")
  expect_null(selected_review_artifact(displayed, 2L))
})

test_that("queue pagination keeps queues above ten records reachable", {
  options <- queue_table_options()
  expect_identical(options$pageLength, 25)
  expect_match(options$dom, "i", fixed = TRUE)
  expect_match(options$dom, "p", fixed = TRUE)

  records <- lapply(seq_len(30L), function(i) {
    id <- sprintf("VAR-fixture-%02d", i)
    list(id = id, yaml_string = .draft_record_yaml(id))
  })
  expect_equal(nrow(index_review_records(records)), 30L)
})

test_that("empty index returns an empty data.frame with correct columns", {
  idx <- index_review_records(list())
  expect_equal(nrow(idx), 0L)
  expect_true(all(
    c("artifact_id", "state", "module", "assigned_to") %in% names(idx)
  ))
})

# --- adapter-backed scan (in-memory double) ---------------------------------

.fake_review_tree <- function(blob_shas) {
  list(commit = "head-1", blobs = blob_shas)
}

test_that("adapter_index_review scans the review dir and indexes records", {
  # simulate a tree containing two review records and an unrelated file
  tree_resp <- .fake_review_tree(list(
    "extraction/30_review/VAR-male.review.yml" = "blob-male",
    "extraction/30_review/VAR-urban.review.yml" = "blob-urban",
    "extraction/30_review/README.md" = "blob-readme",
    "other/file.txt" = "blob-other"
  ))
  contents <- list(
    "extraction/30_review/VAR-male.review.yml" = .draft_record_yaml(
      "VAR-male",
      "draft"
    ),
    "extraction/30_review/VAR-urban.review.yml" = .draft_record_yaml(
      "VAR-urban",
      "needs-revision"
    )
  )
  http_fun <- function(method, url, token, body = NULL) {
    if (grepl("git/ref/heads/review", url)) {
      return(list(object = list(sha = "head-1")))
    }
    if (grepl("git/trees/", url)) {
      entries <- lapply(names(tree_resp$blobs), function(p) {
        list(path = p, type = "blob", sha = tree_resp$blobs[[p]])
      })
      return(list(tree = entries, truncated = FALSE))
    }
    if (grepl("/contents/", url)) {
      path <- sub(".*/contents/(.*)\\?ref=.*", "\\1", url)
      return(list(
        content = base64enc::base64encode(charToRaw(contents[[path]])),
        sha = "blob-x"
      ))
    }
    stop("unexpected url: ", url)
  }
  ad <- reviewapp::new_github_adapter(
    owner = "GMD-hub",
    repo = "fixture-repo",
    default_branch = "main",
    review_branch = "review",
    get_token = function() "tok",
    http = http_fun
  )
  out <- reviewapp::adapter_index_review(ad)
  expect_setequal(out$index$artifact_id, c("VAR-male", "VAR-urban"))
  expect_true("extraction/30_review/README.md" %in% names(out$blobs))
  # only the two .review.yml files made it into the index
  expect_equal(nrow(out$index), 2L)
})

test_that("action_required maps states to their next-action label", {
  expect_identical(action_required("draft"), "Submit")
  expect_identical(action_required("in-review"), "Review")
  expect_identical(action_required("needs-revision"), "Revise")
  expect_identical(action_required("approved"), "Approved")
  expect_identical(action_required("ERROR"), "Repair")
})

test_that("module filter choices derive from unique modules in the index (R10)", {
  mixed <- index_review_records(list(
    list(id = "VAR-male", yaml_string = .draft_record_yaml(
      "VAR-male", "draft", path = "extraction/20_drafts/dem/VAR-male.md")),
    list(id = "VAR-educy", yaml_string = .draft_record_yaml(
      "VAR-educy", "draft", path = "extraction/20_drafts/edu/VAR-educy.md"))
  ))
  ch <- module_filter_choices(mixed)
  # "All" wildcard (value "") plus the unique modules present in the index
  expect_true("" %in% ch)
  expect_identical(names(ch)[ch == ""], "All")
  expect_true("dem" %in% ch)
  expect_true("edu" %in% ch)
  # a geo-only index yields dem/edu absent and geo present
  geo_rec <- list(list(id = "VAR-urban", yaml_string = .draft_record_yaml(
    "VAR-urban", "draft",
    path = "extraction/20_drafts/geo/VAR-urban.md"
  )))
  ch2 <- module_filter_choices(index_review_records(geo_rec))
  expect_true("geo" %in% ch2)
  expect_false("edu" %in% ch2)
  expect_false("dem" %in% ch2)
})

test_that("module filter choices handle an empty index", {
  ch <- module_filter_choices(index_review_records(list()))
  expect_true("" %in% ch)
  expect_length(ch, 1L)
})
