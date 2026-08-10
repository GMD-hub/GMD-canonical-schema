---
date: 2026-08-10
title: "Golem module tests: capture moduleServer returns, drive namespaced inputs, keep fixtures R CMD check-safe"
category: "testing-patterns"
language: "R"
tags: [golem, shiny, testthat, testServer, module, namespacing, R CMD check, Rbuildignore, shinytest2]
root-cause: "Restructuring a flat Shiny app into golem modules changed module scoping and input namespacing; `shiny::testServer()` does not bind a moduleServer() return list into the test environment, and unexported package helpers are invisible under installed-package / R CMD check semantics."
severity: "P1"
---

# Golem module tests: capture moduleServer returns, drive namespaced inputs

## Problem

When the review-app was restructured into the `{golem}` layout
(`R/mod_dashboard.R`, `R/mod_detail.R`, `app_ui.R` → `run_app()`), the existing
dashboard smoke test regressed:

- It called a module-server local (`selected_artifact()`) as a bare function.
  In golem that value lives in the **list returned by `moduleServer()`**, which
  `shiny::testServer(module, ...)` does NOT bind into the test expression's
  environment (verified empirically: `exists("selected_artifact")` is `FALSE`
  inside the test block).
- It drove un-namespaced inputs (`queue_table_rows_selected`). Golem modules
  namespace their inputs (`dashboard-queue_table_rows_selected`), so the
  selection never registered.
- The fixture used a bare `%+%` operator that is an **unexported** package
  helper. It only worked under `devtools::test()` because `load_all()` exports
  internals; under `library(reviewapp)` + `testthat::test_check()` (R CMD check)
  it fails with `could not find function "%+%"`.

The suite was green locally while being broken under check semantics — the
classic "untested code passes review" failure mode.

## Root Cause

Golem encapsulation changes three things a pre-module test never anticipated:

1. **Module return values** (`moduleServer(id, ...)` returning a list) are not
   hoisted into the `testServer` test-environment; only reactive locals created
   inside the server core are in scope.
2. **Inputs and outputs are namespaced** with `NS(id)`, so
   `session$setInputs("id-input_name" = ...)` is required.
3. **Namespace/export model**: `R CMD check` loads the package via `library()`,
   which only exports what NAMESPACE declares; in-test references to
   unexported helpers fail.

## Solution

Use a **module-style wrapper** inside `shiny::testServer()` that captures the
module's returned list into an outer variable, then drive inputs with the
explicit module id prefix (matching how `app_server.R` mounts the module, e.g.
`mod_dashboard_server("dashboard", ...)`):

```r
dashboard_out <- NULL
wrapped_dashboard <- function(id, adapter, refresh_counter) {
  shiny::moduleServer(id, function(input, output, session) {
    dashboard_out <<- reviewapp::mod_dashboard_server(
      "dashboard", adapter, refresh_counter
    )
  })
}

shiny::testServer(
  wrapped_dashboard,
  args = list(adapter = adapter_reactive, refresh_counter = refresh_counter),
  {
    session$setInputs("dashboard-refresh_queue" = 1L)
    q <- dashboard_out$queue_index()          # module return list member
    session$setInputs("dashboard-queue_table_rows_selected" = 1L)
    sel <- dashboard_out$selected_artifact()  # module return list member
  }
)
```

Additional hardening:
- **Never call unexported helpers in tests.** Replace `x %+% y` with
  `paste0(x, y)` (or scope as `reviewapp:::"%+%"`). Grep for bare internal
  operators in `tests/` as a check.
- **Hermetic env**: set/reset test environment with `withr::local_envvar()`
  (auto-restores prior values) instead of `Sys.setenv` + `on.exit(Sys.unsetenv)`.
- **Robust fixture paths**: resolve config/role-map paths via the package
  helper first, then a source-tree candidate, and `skip()` (not
  `normalizePath(mustWork=TRUE)` hard-error) when missing
  (`review-app/tests/testthat/test-app-smoke.R` `.smoke_roles_path()`).
- **Package build ships runtime assets**: after a golem restructure, check
  `.Rbuildignore` does not exclude `inst/app/...` (`.Rbuildignore ^inst/app$`
  silently dropped `inst/app/www/custom.css`, which
  `golem_add_external_resources()` requires at boot). Verify with
  `R CMD build` + `tar tf` that CSS/config actually ship.

## Prevention

- After any golem/module restructure, run the full `testthat` suite AND attempt
  `R CMD check` (or at least confirm tests pass under installed-package
  semantics), not just `devtools::test()`.
- In module tests, always interact through the module's return list and its
  namespaced IDs; never assume pre-module scoping.
- Treat `.Rbuildignore` as deploy-critical: anything `app_sys()`/`system.file()`
  loads at runtime must not be excluded.

## Related

- `.cg-docs/solutions/bugs/2026-08-03-orchestrator-cross-file-attribute-mismatch.md` —
  tests that pass without exercising real behavior let defects slip through review.
- `.cg-docs/reviews/2026-08-07-calibrate-human-review-review.md` and
  `-verify-review.md` — the findings (P1.1, P2.1, P2.2, P1.2) this entry documents.
- `review-app/tests/testthat/test-app-smoke.R` — worked example.
