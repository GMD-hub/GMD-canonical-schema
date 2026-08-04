# Authorization tests (V2 beside state machine; extended in Phase 3 with
# identity-resolution cases).

test_that("authorize() enforces role gates for every action", {
  # reviewer
  expect_true(reviewapp::authorize("reviewer", "submitted"))
  expect_false(reviewapp::authorize("reviewer", "approved"))
  expect_false(reviewapp::authorize("reviewer", "request-revision"))
  expect_false(reviewapp::authorize("reviewer", "reopened"))
  expect_false(reviewapp::authorize("reviewer", "assigned"))

  # approver
  expect_false(reviewapp::authorize("approver", "submitted"))
  expect_true(reviewapp::authorize("approver", "approved"))
  expect_true(reviewapp::authorize("approver", "request-revision"))
  expect_false(reviewapp::authorize("approver", "reopened"))
  expect_false(reviewapp::authorize("approver", "assigned"))

  # administrator
  expect_false(reviewapp::authorize("administrator", "submitted"))
  expect_false(reviewapp::authorize("administrator", "approved"))
  expect_false(reviewapp::authorize("administrator", "request-revision"))
  expect_true(reviewapp::authorize("administrator", "reopened"))
  expect_true(reviewapp::authorize("administrator", "assigned"))
})

test_that("authorize() denies unmapped (NULL) roles for all gated actions", {
  for (action in c("submitted", "approved", "request-revision", "reopened", "assigned")) {
    expect_false(reviewapp::authorize(NULL, action), info = action)
  }
})

test_that("authorize() allows saved for a mapped role", {
  expect_true(reviewapp::authorize("reviewer", "saved"))
  expect_true(reviewapp::authorize("approver", "saved"))
  expect_false(reviewapp::authorize(NULL, "saved"))
})
