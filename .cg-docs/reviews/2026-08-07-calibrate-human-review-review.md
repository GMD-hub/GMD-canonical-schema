---
date: 2026-08-10
depth: standard
type: standard
plan: .cg-docs/plans/2026-08-07-calibrate-human-review.md
findings:
  P0.1: fixed
  P1.1: fixed
  P1.2: fixed
  P1.3: skipped
  P1.4: skipped
  P1.5: skipped
  P2.1: fixed
  P2.2: fixed
  P2.3: skipped
  P2.4: skipped
  P2.5: skipped
  P2.6: skipped
  P2.7: skipped
  P3.1: skipped
  P3.2: skipped
---

# Review Report — calibrate-human-review

**Review mode**: standard (explicit user request; publishing/deployment config kept in focus as a high-risk signal)
**Files reviewed**: 6 changed files
**Findings**: 15 (P0: 1, P1: 4, P2: 7, P3: 2)

Scope: uncommitted changes from the `/cg-work phase4-5` resume run plus the
re-deploy that recorded bundle 88084 (deployed 2026-08-10T21:23Z) —
`review-app/tests/testthat/test-app-smoke.R`,
`review-app/.posit/publish/review-app-9KP9.toml`,
`review-app/.posit/publish/deployments/deployment-U42S.toml` (auto-generated),
`.cg-docs/calibration/defect-log.yaml`,
`.cg-docs/work-reports/2026-08-07-calibrate-human-review.md`,
`.cg-docs/active-state/current.json`.

Agents: @cg-code-quality, @cg-testing, @cg-documentation, @cg-version-control,
@cg-reproducibility, @cg-performance, @cg-architecture, @cg-data-quality.

### P0 — BLOCKING
- **[P0.1]** [safe_auto] cg-documentation/cg-reproducibility/cg-architecture/cg-data-quality — `.cg-docs/calibration/defect-log.yaml`, `.cg-docs/active-state/current.json`, `.cg-docs/work-reports/2026-08-07-calibrate-human-review.md` — DEF-001 and the active-state/report claims are stale relative to the re-deploy: defect-log pins bundle 87929 @17:23Z and "re-deploy has not yet been executed"; current.json D1/artifactRefs and the Run 3 report say "re-deploy pending". A corrected re-deploy (bundle 88084 @21:23Z) now ships the full golem file set (DESCRIPTION, NAMESPACE, R/*, inst/, config/), so DEF-001's root cause is resolved.
  **Why**: leaving the audit trail self-contradictory breaks calibration reproducibility and misleads the next `/cg-work phase4-5` run.
  **Fix**: set DEF-001 status `fixed` with `fix_reference` = bundle 88084 and a corrected description; refresh current.json (updatedAt, D1 one-liner, artifactRefs, V1 wording); update the Run 3 report to record the executed re-deploy, keep boot verification as the outstanding item, and avoid overclaiming V1 as "passed" (local suite only, Connect boot unverified).

### P1 — CRITICAL
- **[P1.1]** [safe_auto] cg-code-quality/cg-architecture — `review-app/tests/testthat/test-app-smoke.R:60,67` — the fixture `http_fun` calls the **unexported** `%+%` operator bare; it only passes under `devtools::test()` (load_all export_all); under installed-package / `R CMD check` semantics it fails with `could not find function "%+%"`.
  **Why**: the "untested code passes review" failure mode; the suite must pass under check semantics.
  **Fix**: replace with `paste0("blob-", basename(p))` / `paste0("blob-", basename(path))`.
- **[P1.2]** [manual→applied] cg-reproducibility — `review-app/.Rbuildignore:10` — `^inst/app$` excludes `inst/app/www/custom.css`, which `golem_add_external_resources()` (R/app_config.R) hard-requires at boot; `R CMD build`/check tarball drops it.
  **Why**: latent boot-breakage on any build/tarball/check deploy path (R CMD INSTALL keeps it, so the current Publisher bundle is fine, but the build path is broken).
  **Fix**: remove `^inst/app$` so custom.css ships.
- **[P1.3]** [manual→deferred] cg-version-control — `review-app/.posit/publish/deployments/deployment-U42S.toml` is git-tracked and churns machine-generated diffs on every deploy; recommend gitignoring `deployments/` + `git rm --cached`.
  **Why**: noisy diffs and internal infra URLs/guids in version control.
  **Fix**: add `review-app/.posit/publish/deployments/` to a `.gitignore` and untrack it — CONFLICTS with reproducibility (bundle 88084 is DEF-001's fix reference in the audit trail); deferred to user decision, not auto-applied.
- **[P1.4]** [advisory] cg-architecture — `review-app/tests/testthat/test-app-smoke.R:26` — the only end-to-end boot check auto-skips under `R CMD check` when `NOT_CRAN` is unset, so checks-only pipelines lose all boot coverage (the exact class DEF-001 exposed).
  **Why**: boot regressions only surface under devtools::test().
  **Fix**: set `NOT_CRAN=true` in any R CI/check gate (no R CI workflow currently exists here; advisory).
- **[P1.5]** [advisory] cg-reproducibility — `review-app/R/identity.R:107-117` + `.Rbuildignore:7` — role-map `system.file("config","roles.yml")` priority is dead code (config/ is excluded from the installed package); production resolution silently falls back to bundle-relative `config/roles.yml` from the process cwd.
  **Why**: documented resolution priority does not match the shipped layout; boot depends on cwd == bundle root.
  **Fix**: user decision — either ship roles via `inst/config/` (golem convention) or amend the docstring to state the bundle-relative mechanism as source of truth (structural; not auto-applied).

### P2 — IMPORTANT
- **[P2.1]** [safe_auto] cg-reproducibility — `review-app/tests/testthat/test-app-smoke.R:16-19,88` — `normalizePath(..., mustWork=TRUE)` hard-errors when `config/roles.yml` is absent (e.g. installed-package/check), and test 2 has no fallback like test 1.
  **Fix**: resolve the role map via `reviewapp_role_map_path()` first, fall back to the bundle path, and `skip()` when missing.
- **[P2.2]** [safe_auto] cg-reproducibility/cg-code-quality — `review-app/tests/testthat/test-app-smoke.R:21-24,89-90` — cleanup uses `Sys.unsetenv`, clobbering pre-existing `REVIEW_APP_ROLES`/`REVIEW_APP_OFFLINE` overrides.
  **Fix**: use `withr::local_envvar(...)` (auto-restores), matching the suite's own idiom.
- **[P2.3]** [advisory] cg-testing/cg-code-quality — `review-app/tests/testthat/test-app-smoke.R:33-41` — queue and auth assertions are near-vacuous (`grepl("queue_table", ...)` self-matches the element id; `||` hedges).
  **Why**: gives false confidence about rendering/auth state.
  **Fix**: needs a maintainer decision on what the offline queue renders; not auto-applied.
- **[P2.4]** [advisory] cg-testing — `review-app/tests/testthat/test-app-smoke.R:83-124` — module test covers the happy path only; NULL-adapter → empty queue, no-selection → NULL `selected_artifact`, and `refresh_counter`-driven reload are untested.
  **Fix**: add short edge-case `test_that` blocks (future change; advisory).
- **[P2.5]** [advisory] cg-architecture/cg-reproducibility — `review-app/R/identity.R:112-118` — `rprojroot::find_root()` candidate depends on `rprojroot` (Suggests, absent from renv.lock).
  **Fix**: declare rprojroot in Imports or drop the candidate (structural; user decision).
- **[P2.6]** [advisory] cg-architecture — `review-app/app.R` — `library(reviewapp)` requires Connect to install the local package; necessary-but-not-sufficient. Boot on Connect for bundle 88084 remains unverified.
  **Fix**: smoke-check the deployed content URL (external operator action).
- **[P2.7]** [advisory] cg-reproducibility — `.cg-docs/calibration/defect-log.yaml` — entries carry no per-entry timestamp/schema version, so status history is unrecoverable.
  **Fix**: add `logged_at`/`updated` and schema-version fields (future change).

### P3 — MINOR
- **[P3.1]** [advisory] cg-data-quality/cg-architecture — `2026-08-07-calibrate-human-review.md:24-36` — the legacy Run 1 evidence table lists V4/V6–V10 twice with opposing statuses (held over; predates the reviewed Run 3 changes).
  **Fix**: dedupe historical rows (out of review scope; noted).
- **[P3.2]** [advisory] cg-data-quality — `review-app/tests/testthat/test-app-smoke.R:52` — the in-memory double's `current_content_sha256` does not equal the SHA of the body it serves; currently unexercised.
  **Fix**: make the fixture sha consistent with the served body.

### ✅ Passed
- @cg-performance: No issues found.
- Verifications: secrets scan clean; publish config now complete for the golem package; smoke test regression-fix confirmed (red→green); module namespacing/return-list wiring correct.

> Review report saved to `.cg-docs/reviews/2026-08-07-calibrate-human-review-review.md`. Use `/cg-fix-triage P1.2 P2.1` etc. in a future session to apply findings by ID, or `/cg-fix-triage P0` by priority.
