# Step 8 -- Connect identity resolution to role (R2, R3, V6).

library(testthat)

test_that("connect_identity reads session$user when present", {
  session <- list(user = "reviewer@example.org")
  expect_identical(connect_identity(session), "reviewer@example.org")
})

test_that("connect_identity falls back to empty/NULL when session has no user", {
  withr::with_envvar(
    c(REVIEW_APP_USER = ""),
    expect_null(connect_identity(list(user = NULL)))
  )
})

test_that("connect_identity honours REVIEW_APP_USER override for local dev", {
  withr::with_envvar(
    c(REVIEW_APP_USER = "local-reviewer@example.org"),
    expect_identical(connect_identity(NULL), "local-reviewer@example.org")
  )
})

test_that("mapped identity resolves to its correct role", {
  role_map <- new_role_map(list(
    list(identity = "reviewer@example.org", role = "reviewer"),
    list(identity = "approver@example.org", role = "approver"),
    list(identity = "admin@example.org", role = "administrator")
  ))
  auth <- session_auth("reviewer@example.org", role_map)
  expect_identical(auth$role, "reviewer")
  expect_true(auth$authorized)
})

test_that("unmapped identity is denied all write actions (no default role)", {
  role_map <- new_role_map(list(
    list(identity = "reviewer@example.org", role = "reviewer")
  ))
  auth <- session_auth("some-other@example.org", role_map)
  expect_null(auth$role)
  expect_false(auth$authorized)
  # authorize() gate must deny every action for a NULL role
  for (action in ACTIONS) {
    expect_false(authorize(auth$role, action), info = action)
  }
})

test_that("NULL identity yields unauthenticated, unauthorized state", {
  role_map <- new_role_map(list(
    list(identity = "reviewer@example.org", role = "reviewer")
  ))
  auth <- session_auth(NULL, role_map)
  expect_null(auth$identity)
  expect_null(auth$role)
  expect_false(auth$authorized)
})

test_that("role map load failure fails loudly", {
  expect_error(
    session_auth("x@example.org", "/nonexistent/roles.yml"),
    "role map file not found"
  )
})

test_that("malformed role map object fails loudly", {
  expect_error(
    session_auth("x@example.org", list(roles = list(list(identity = "a")))),
    "must have identity and role"
  )
})

test_that("auth_text reflects the three identity states", {
  role_map <- new_role_map(list(list(
    identity = "r@example.org",
    role = "reviewer"
  )))
  expect_match(auth_text(session_auth(NULL, role_map)), "Not authenticated")
  expect_match(
    auth_text(session_auth("unknown@example.org", role_map)),
    "not authorized"
  )
  expect_match(
    auth_text(session_auth("r@example.org", role_map)),
    "role: reviewer"
  )
})

test_that("committed roles.yml resolves its three identities", {
  path <- testthat::test_path("../..", "config", "roles.yml")
  skip_if_not(file.exists(path), "source-tree role map is not included in the package tarball")
  role_map <- load_role_map(path)
  expect_identical(resolve_role(role_map, "bbrunckhorst"), "reviewer")
  expect_identical(resolve_role(role_map, "clakner"), "approver")
  expect_identical(resolve_role(role_map, "acastanedaa"), "administrator")
  expect_null(resolve_role(role_map, "outsider@example.org"))
})
