---
date: 2026-08-26
title: "Testing release queues with distinct commits and exact regeneration"
category: "testing-patterns"
language: "R"
tags: [release-validator, git-commits, canonical-inventory, hash-binding, index-reconciliation]
root-cause: "Tests using one commit and aggregate set comparisons could not detect source-resolution errors or stale values attached to valid queue IDs."
severity: "P0"
plan: ".cg-docs/plans/2026-08-25-complete-release-a-production-queue-cutover.md"
reviewed-in: ".cg-docs/reviews/2026-08-25-complete-release-a-production-queue-cutover-review.md"
related: [".cg-docs/solutions/data-quality/2026-08-26-validate-canonical-queue-identity.md", ".cg-docs/solutions/testing-patterns/2026-08-03-welfare-boundary-content-based-detection.md"]
---

# Testing Release Queues With Distinct Commits and Exact Regeneration

This is the testing companion to
`data-quality/2026-08-26-validate-canonical-queue-identity.md`; that document
defines the identity chain, while this entry focuses on fixtures and assertions
that prevent regressions in its implementation.

## Problem

A production queue validator initially treated checkout `HEAD` as the pinned
source commit. That fails after bootstrap because the queue branch necessarily
points to a later commit containing generated queue state. Other checks compared
counts, ID sets, or manifest-provided hashes, allowing a substituted but
self-consistent population or stale index fields to pass.

## Root Cause

Three distinct identities were collapsed or trusted transitively:

- the queue commit containing the files being validated;
- the pinned source commit whose artifact bytes were enrolled;
- the canonical inventory and its expected path-set digest.

The aggregate index was also treated as evidence rather than a cache that must
be exactly derivable from authoritative records and their actual Git blob SHAs.

## Solution

### Keep queue and source commits independent

Validate queue files from the checked-out queue commit, but resolve every source
artifact explicitly from the pinned source commit:

```r
source_raw <- git_blob_raw(repo, expected_source, record$source_artifact_path)
```

Do not require `HEAD == expected_source`. Require the manifest and every record
to name `expected_source`, then bind the record to bytes read from that commit.
Add a real temporary-Git-repository test that creates a source commit followed
by a distinct queue commit and proves the source blob is still resolved from
the first commit. An equality-only unit fixture will not catch this regression.

### Bind both inventory identity and source bytes

Compute the sorted source-path digest from validated records. Require all three
values to match independently:

```r
identical(manifest$expected_path_set_sha256, CANONICAL_PATH_SET_SHA256)
identical(computed_path_digest, manifest$expected_path_set_sha256)
identical(computed_path_digest, CANONICAL_PATH_SET_SHA256)
```

For each record, verify canonical filename, queue ID, pinned source commit,
source Git blob SHA, complete-content SHA-256, enrolled-body SHA-256, and current
body SHA-256. Counts and artifact-ID sets are necessary but insufficient.

### Regenerate the index row by row

Parse and validate each record, calculate its actual queue-record blob SHA from
the bytes on disk, regenerate the complete index rows, and compare the persisted
rows with strict structural equality:

```r
items <- lapply(record_paths, parse_validate_and_hash_record)
regenerated <- queue_index_from_record_items(items, manifest)
if (!identical(index$rows, regenerated)) {
  stop("queue index rows or record blob SHAs differ from exact regeneration")
}
```

This reconciles artifact ID, path, state, assignment, review round, governance
blockers, source drift, and record blob SHA together. Set equality cannot detect
wrong values attached to otherwise valid IDs.

## Prevention

- Name commit roles explicitly (`queue_commit`, `expected_source`) and test them
  with different SHAs.
- Treat canonical constants as an independent trust anchor; never accept a
  manifest hash merely because generated content agrees with it.
- Treat aggregate indexes as rebuildable caches, not authorities.
- Hash the bytes actually read at the revision being validated.
- Include mutation tests for one wrong index field, one wrong record blob SHA,
  one substituted path set, and one source/queue commit mismatch.

## Related

- [Canonical queue identity validation](../data-quality/2026-08-26-validate-canonical-queue-identity.md) is the authoritative design-level pattern for the identity chain tested here.
- [Content-based boundary detection](2026-08-03-welfare-boundary-content-based-detection.md) applies the same principle: validate authoritative content and provenance rather than proxy identifiers.
- `.cg-docs/reviews/2026-08-25-complete-release-a-production-queue-cutover-review-2.md` records the canonical digest, byte binding, and row-reconciliation findings.
- `.cg-docs/reviews/2026-08-25-complete-release-a-production-queue-cutover-verify-review.md` records the distinct queue/source commit regression.
- `review-app/tools/validate-production-queue.R` contains the fail-closed validator.
- `review-app/tests/testthat/test-production-queue.R` contains the distinct-commit integration test.
