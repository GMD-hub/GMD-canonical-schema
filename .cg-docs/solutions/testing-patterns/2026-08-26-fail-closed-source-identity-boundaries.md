---
date: 2026-08-26
title: "Test Fail-Closed Source Identity at Every Boundary"
category: "testing-patterns"
language: "Python"
tags: [source-identity, pydantic, subprocess, filesystem, pytest]
root-cause: "Source verification was incomplete when schema, filesystem, process, governance, and checkout checks were tested as separate happy-path assumptions."
severity: "P1"
plan: ".cg-docs/plans/2026-08-25-lock-extraction-source-resolution.md"
reviewed-in: ".cg-docs/reviews/2026-08-26-lock-extraction-source-resolution-review.md"
related: [".cg-docs/solutions/testing-patterns/2026-08-03-welfare-boundary-content-based-detection.md"]
---

# Test Fail-Closed Source Identity at Every Boundary

## Problem

An extraction source can appear pinned while one identity boundary remains
unchecked: a nullable digest, symbolic Git revision, reordered governed file,
stale governance path, mismatched parser runtime, unreadable file, or failed Git
process. Tests that rely on the current protected manifest also become invalid
after a later human-approved configuration change.

## Root Cause

Source identity is a chain of independent claims. Validating only the manifest
model or only the file hashes does not prove repository revision, governed
ordering, governance agreement, parser identity, and readable bytes together.
Combining multiple invalid mutations in one test can also make an assertion
vacuous because the first validation error masks the second.

## Solution

Use one supported gate that runs these checks in order:

1. Parse manifest and governance YAML through stable domain errors.
2. Validate exact repository, commit, digest, path, scope, and ordering shapes.
3. Cross-check schema/GMD versions and module source paths.
4. Verify the exact parser runtime through a bounded subprocess call.
5. Verify checkout `HEAD` and hash every governed source and supporting file.

Test each invalid identity independently and assert the field or stable error
boundary. Mock only process and failure boundaries; retain an integration test
that uses the real preflight and resolver helpers against an eight-file
temporary checkout. Represent pre-approval states with synthetic fixtures, not
the committed protected configuration, so approved activation cannot invalidate
the test suite.

## Prevention

- Treat file ordering and scope as identity, not merely membership.
- Require lowercase fixed-length commit and digest values in the schema.
- Wrap filesystem inspection, reads, decoding, YAML parsing, and subprocess
  failures in chained domain exceptions.
- Test missing executables, timeouts, nonzero exits, malformed output, and
  version mismatch separately.
- Keep orchestration's source-gate requirement explicit; do not reconstruct a
  weaker proof from caller-supplied partial data.
- Document mutable-checkout TOCTOU as a residual risk until an immutable
  snapshot or in-process verified-byte contract is designed.

## Related

- [Welfare boundary content-based detection](2026-08-03-welfare-boundary-content-based-detection.md)
- [Verification review](../../reviews/2026-08-26-lock-extraction-source-resolution-review.md)
