---
date: 2026-08-10
depth: light
parent-review: .cg-docs/reviews/2026-08-07-calibrate-human-review-review.md
type: verification
findings:
  P1.1: fixed
  P3.1: fixed
---

# Verify Review — calibrate-human-review

**Review mode**: light (mode:verify)
**Prior review**: `.cg-docs/reviews/2026-08-07-calibrate-human-review-review.md`
**Files reviewed**: fix-triage change set (test-app-smoke.R, .Rbuildignore,
defect-log.yaml, active-state/current.json, work-report Run 3,
.posit/publish configs + auto-generated deployment record)
**Findings**: 2 (P1: 1, P3: 1)

Agents: @cg-code-quality, @cg-testing (light, verify mode).

## Verification results — P0.1, P1.1, P1.2, P2.1, P2.2 from the prior review

All five fixed findings verified present and correct; the full `testthat` suite
is green (**371 passed, 0 failed, 0 skipped**; smoke filter 8 passed):

- **P0.1** — DEF-001 re-reconciled (status `fixed`, fix_reference bundle 88084);
  no stale `open` / "re-deploy pending" phrasing remains except schema vocabulary
  templates in `measurement-framework.md`. CONTAINS a refreshed staleness (see P1.1).
- **P1.1** — no bare `%+%` remains in `test-app-smoke.R` (both fixtures use
  `paste0("blob-", basename(...))`); package-internal `%+%` in `R/recovery.R`
  is unaffected.
- **P1.2** — `^inst/app$` removed from `.Rbuildignore`; fresh `R CMD build`
  tarball contains `inst/app/www/custom.css` and `inst/golem-config.yml`.
- **P2.1** — `.smoke_roles_path()` used by both tests; `skip()`s (never errors)
  when the role map is missing.
- **P2.2** — `withr::local_envvar()` in both tests; no `Sys.setenv`/`Sys.unsetenv`
  remains; `withr` is declared in DESCRIPTION Suggests.

## Findings

### P1 — CRITICAL
- **[P1.1]** [cg-code-quality/cg-testing] `review-app/.posit/publish/deployments/deployment-U42S.toml:13-14` vs `.cg-docs/calibration/defect-log.yaml:24-25`, `.cg-docs/active-state/current.json:26,34-35`, `.cg-docs/work-reports/2026-08-07-calibrate-human-review.md:322,359` — the authoritative deployment record now lists **bundle 88147 @ 2026-08-10T22:52:40Z** (a newer deploy than the audit trail was reconciled to), but the hand-maintained trail cites **bundle 88084 @ 2026-08-10T21:23Z**; `current.json.updatedAt` (21:50:25Z) also predates the recorded deploy.
  **Why**: the audit trail is once again self-contradictory w.r.t. the deployed bundle — the exact staleness class P0.1 was filed to eliminate — and would mislead the next `/cg-work phase4-5`/reproducibility run. The golem file set IS present in bundle 88147, so DEF-001's substance still holds; only the fix-reference citations need updating.
  **Fix**: reconcile defect-log `fix_reference`, current.json D1/artifactRefs/updatedAt, and work-report Run 3 to **bundle 88147 @ 2026-08-10T22:52:40Z** (or annotate the newer deploy); do NOT edit the auto-generated `deployment-U42S.toml`.

### P3 — MINOR
- **[P3.1]** [cg-testing] `.cg-docs/active-state/current.json:11` — V1 artifact text says "372 tests" but the suite now runs **371** (the P2.1 fix removed one `expect_true(file.exists(roles))` assertion, folded into the skip condition).
  **Why**: stale count in the evidence pointer.
  **Fix**: update the V1 count to 371.

### ✅ Passed
- @cg-code-quality: fixes are idylomatic/DRY; `.Rbuildignore`/`.cg-docs` evaluation correct (no exclusion needed).
- @cg-testing: targeted + full suite green; per-fix behavioral verification passed.

> Verify report saved to `.cg-docs/reviews/2026-08-07-calibrate-human-review-verify-review.md`.
