---
date: 2026-08-26
title: "Fail-Closed Deterministic Promotion from Immutable Evidence"
category: "data-quality"
language: "Python"
tags: [promotion, reproducibility, git-objects, provenance, trust-boundaries]
root-cause: "Schema-valid candidates and declared aggregates were trusted without proving they were exact deterministic products of immutable governed inputs."
severity: "P0"
reviewed-in: ".cg-docs/reviews/2026-08-25-canonical-non-welfare-inventory-ledger-review.md"
related: [".cg-docs/solutions/testing-patterns/2026-08-06-windows-platform-test-fixes.md", ".cg-docs/solutions/data-quality/2026-08-14-hand-draft-cvs-variable-specs.md"]
---

# Fail-Closed Deterministic Promotion from Immutable Evidence

## Problem

A promotion command could accept a hand-authored candidate that passed schema
and fixed-total checks but was never reproduced from the governed source map,
draft corpus, approval evidence, or immutable guideline bytes. Provenance tied
to mutable `HEAD`, and aggregate totals not derived from rows, created similar
ways for internally consistent metadata to contradict its evidence.

## Root Cause

Validation treated claims at trust boundaries as inputs. Candidate bytes,
commits, hashes, paths, and aggregate counts were checked for shape or totals,
but were not always recomputed from independently resolved evidence.

## Solution

Use one rule at every promotion boundary: resolve immutable inputs, recompute
the complete artifact, and compare exact bytes before replacing the target.

```python
compiled = serialize_ledger(
    compile_ledger(source_repo, source_commit, source_map, draft_root)
)
candidate = candidate_path.read_bytes()
if candidate != compiled:
    raise InventoryError(
        "promotion candidate bytes differ from immutable recompilation"
    )
atomic_write(output_path, compiled)
```

- Read source evidence with `git show <commit>:<path>`, then verify configured
  SHA-256 hashes. Dirty working-tree files never enter the evidence chain.
- Pin supporting repository evidence to an explicit 40-character commit and
  verify its blob SHA-256; never resolve it from mutable `HEAD`.
- Rebuild the closed source map and compare the complete mapping, including
  top-level identity fields.
- Derive denominator and module aggregates from canonical rows, then require
  declared aggregates to equal the derived mapping exactly.
- Serialize with fixed ordering, encoding, line endings, and serializer
  versions. Compile twice and byte-compare candidates during release checks.
- Promote the recomputed bytes through a lock-protected unique temporary file,
  `fsync`, and atomic replacement only after every comparison passes.

## Prevention

- Treat candidate files, metadata, aggregate fields, paths, and repository
  state as untrusted until independently derived or verified.
- Test each trust boundary adversarially: hand-authored candidate, dirty source
  checkout, wrong commit/hash/blob, changed top-level source-map identity,
  aggregate redistribution with an unchanged total, path/symlink escape,
  unsupported parser constructs, lock contention, and byte differences.
- Use binary fixtures and `write_bytes()` where hashes or line endings matter.
- Keep promotion fail-closed: any missing object, mismatch, unsupported input,
  failed test, or lock conflict leaves the prior artifact unchanged.

## Related

- [Binary-exact cross-platform test fixtures](../testing-patterns/2026-08-06-windows-platform-test-fixes.md)
- [Deterministic inventory and committed corpus gates](2026-08-14-hand-draft-cvs-variable-specs.md)
- [Task C fix-triage review](../../reviews/2026-08-25-canonical-non-welfare-inventory-ledger-review.md)
