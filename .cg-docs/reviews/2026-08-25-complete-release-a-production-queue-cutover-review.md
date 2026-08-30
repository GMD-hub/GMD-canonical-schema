---
date: 2026-08-26
depth: full
type: standard
plan: .cg-docs/plans/2026-08-25-complete-release-a-production-queue-cutover.md
findings:
  P0.1: fixed
  P0.2: fixed
  P0.3: fixed
  P1.1: fixed
  P1.2: fixed
  P1.3: fixed
  P1.4: fixed
  P1.5: fixed
  P2.1: fixed
  P2.2: fixed
  P2.3: fixed
  P2.4: fixed
---

# Release A Phase 1 Review

**Review mode**: full (`review:auto`, release/security risk)
**Findings**: 12 (P0: 3, P1: 5, P2: 4)

## P0 - Blocking

- **[P0.1]** `review-app/tools/validate-production-queue.R:56` - Path-set validation trusts the manifest digest instead of requiring the canonical `QUEUE_EXPECTED_PATH_SET_SHA256`. A substituted but self-consistent population can pass.
- **[P0.2]** `review-app/tools/validate-production-queue.R:65` - The validator compares only artifact-ID sets and does not reconcile index rows with record paths, blob SHAs, state, assignments, rounds, blockers, or drift.
- **[P0.3]** `review-app/tools/validate-production-queue.R:41` - Records are not bound to filenames, queue identity, checkout commit, or pinned source bytes and hashes.

## P1 - Critical

- **[P1.1]** `review-app/R/enrollment.R:230` - Bootstrap source mismatch, source movement, and no-write-on-failure behavior are not tested through `bootstrap_production_queue()`.
- **[P1.2]** `review-app/R/github_adapter.R:30` - Telemetry is shared mutable adapter state, so concurrent Shiny sessions can reset or combine one another's counts.
- **[P1.3]** `review-app/R/github_adapter.R:54` - Telemetry counts logical adapter calls rather than actual HTTP retry attempts.
- **[P1.4]** `review-app/R/mod_dashboard.R:164` - Refresh telemetry is not exposed through an observable non-secret operational evidence channel.
- **[P1.5]** `review-app/R/index.R:375` - Malformed manifest or index content propagates errors instead of returning a controlled empty `queue_error` state.

## P2 - Important

- **[P2.1]** `review-app/tools/attest-connect.R:3` - Tool argument handling, endpoint allowlisting, redaction, response validation, pagination, and deterministic ordering lack tests; API keys should be environment-only.
- **[P2.2]** `.github/workflows/validate.yml:64` - CI couples `ubuntu-latest` to the literal `libgit2.so.1.7` SONAME.
- **[P2.3]** `review-app/docs/operator-guide.md:405` - Operator instructions omit exact validator/attestor commands and explicit expected-source equality checks.
- **[P2.4]** `review-app/R/github_adapter.R:268` - Roxygen documentation omits new adapter parameters and the supported HTTP body argument.

## Passed

- Legacy `review` remains read-only and protected content is untouched.
- Production branch naming correctly uses `review-production`.
- No secrets or unintended generated build artifacts were found.
- Local R, Python, package build, and package-check test gates executed successfully.
