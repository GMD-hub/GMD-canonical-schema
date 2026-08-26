---
date: 2026-08-26
depth: full
type: standard
plan: .cg-docs/plans/2026-08-25-complete-release-a-production-queue-cutover.md
findings:
  P0.1: fixed
  P0.2: fixed
  P0.3: fixed
  P0.4: fixed
  P1.1: fixed
  P1.2: fixed
  P1.3: fixed
  P1.4: fixed
  P1.5: fixed
  P1.6: fixed
  P2.1: fixed
  P2.2: fixed
  P2.3: fixed
  P2.4: fixed
---

# Release A Phase 1 Fallback Review

`mode:verify` found no prior fixed finding and therefore fell back to a normal full review.

## P0 - Blocking

- **[P0.1]** `review-app/tools/validate-production-queue.R:56` - Require manifest and computed path digests to independently equal the canonical Release A digest.
- **[P0.2]** `review-app/tools/validate-production-queue.R:65` - Reconcile every persisted index field with records and actual record blob SHAs.
- **[P0.3]** `review-app/tools/validate-production-queue.R:41` - Bind records to canonical filenames, queue identity, checkout commit, and pinned source bytes/hashes.
- **[P0.4]** `review-app/R/index.R:375` - Require production manifest source identity to equal `adapter$expected_source_commit` before exposing queue rows.

## P1 - Critical

- **[P1.1]** `review-app/R/enrollment.R:180` - Add direct bootstrap tests for expected-source mismatch, movement, no-write failures, and success.
- **[P1.2]** `review-app/R/github_adapter.R:29` - Replace shared mutable telemetry with operation-scoped counters.
- **[P1.3]** `review-app/R/github_adapter.R:54` - Distinguish logical reads from actual HTTP attempts/retries.
- **[P1.4]** `review-app/R/mod_dashboard.R:164` - Expose redacted per-refresh telemetry and duration through an observable administrator evidence channel.
- **[P1.5]** `review-app/R/index.R:375` - Convert malformed manifest/index data into a controlled empty `queue_error` state.
- **[P1.6]** `review-app/tools/attest-connect.R:20` - Fail on wrong repository, branch, directory, commit, GUID, inactive bundle, or unhealthy deployment.

## P2 - Important

- **[P2.1]** `review-app/tools/attest-connect.R:3` - Make API key environment-only; add strict parsing, endpoint/redaction tests, response validation, pagination, and deterministic ordering.
- **[P2.2]** `.github/workflows/validate.yml:64` - Replace fixed libgit2 SONAME check with a compatible functional/package check.
- **[P2.3]** `review-app/docs/operator-guide.md:405` - Add exact validator/attestor commands and expected-source equality requirements; reference the tool from README.
- **[P2.4]** `review-app/R/github_adapter.R:268` - Document new constructor and HTTP callback parameters.

## Passed

- No protected canonical content or remote review state was modified.
- Local R, Python, build, and package-check tests executed successfully before review.
