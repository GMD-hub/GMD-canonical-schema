---
date: 2026-08-26
depth: full
type: review
findings:
  P0.1: fixed
  P0.2: fixed
  P1.1: fixed
  P1.2: fixed
  P1.3: fixed
  P1.4: fixed
  P1.5: fixed
  P2.1: fixed
  P2.2: skipped
---

## Review Report

**Review mode**: verify, mandated fallback to normal full review because no prior fixed review existed
**Files reviewed**: `schema/extraction/inventory.py`, `extraction_pipeline/inventory.py`, `tests/extraction/test_inventory.py`, `tests/extraction/test_completeness.py`, `extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml`, `extraction/20_drafts/runs/non-welfare-inventory.v1.yaml`, `.cg-docs/active-state/current.json`, `.cg-docs/plans/2026-08-25-canonical-non-welfare-inventory-ledger.md`, `.cg-docs/work-reports/2026-08-25-canonical-non-welfare-inventory-ledger.md`, and `roadmap.json`
**Findings**: 9 (P0: 2, P1: 5, P2: 2; fixed: 3, open: 6)

This report consolidates and deduplicates the ten full-route agent outputs. All findings were recorded open before remediation. Only findings classified `[safe_auto]` and limited to local schema/test invariants were changed; manual and advisory findings remain open.

### P0 - CRITICAL (must fix)

- **[P0.1] [open] [manual]** [cg-security, cg-reproducibility] `extraction_pipeline/inventory.py:501-505` - Promotion can bypass immutable-source recompilation and source-map validation.
  **Why**: `promote` validates only the candidate's Pydantic shape and fixed totals before copying its bytes. A hand-authored candidate can satisfy those checks without being reproduced from the configured immutable guideline objects, closed source map, draft corpus, approval-section hashes, or deterministic serializer. This bypasses the principal review and provenance gate while writing the named ledger path.
  **Required fix**: Make promotion accept the compile inputs and recompile/revalidate the candidate against immutable source objects immediately before replacement, or promote only a cryptographically bound validation receipt produced by the same invocation. This changes CLI and promotion semantics and therefore requires explicit manual design approval.

- **[P0.2] [fixed] [safe_auto]** [cg-correctness] `schema/extraction/inventory.py:176-192` - Aggregate module counts were not tied to canonical row ownership.
  **Why**: The model previously checked only the sum of declared module counts. A ledger could move counts between modules, duplicate a module entry, or omit modules while preserving denominator 267, so the ownership aggregate could contradict every canonical row.
  **Fix applied**: Reject duplicate module aggregates and require the declared module-to-count mapping to equal counts derived from canonical `owner_module` values. Added a regression test that preserves the denominator while assigning its aggregate to the wrong owner.

### P1 - HIGH (should fix before merge)

- **[P1.1] [open] [manual]** [cg-reproducibility] `extraction_pipeline/inventory.py:374-394` - Obsolete-claim provenance is resolved from mutable canonical-schema `HEAD`.
  **Why**: Compilation records whichever commit happens to be checked out and reads `HEAD:<claim_path>`, so identical Task C source inputs can generate different provenance after unrelated repository commits. The ledger is not reproducible solely from its declared inputs.
  **Required fix**: Add an explicit canonical-schema claim commit/blob identity to the closed source map and read that object via a repository-scoped Git command. Changing the governed provenance baseline is manual.

- **[P1.2] [open] [manual]** [cg-correctness] `extraction_pipeline/inventory.py:112-143` - The bounded parser fails open on unsupported inventory-like rows.
  **Why**: Lines that do not match `^\|\s*\d+\s*\|` are silently ignored after a recognized caption. Malformed numeric rows, changed grid-table row shapes, or non-pipe inventory constructs can disappear rather than raising the promised source-delta error; total counts alone may not identify which construct was skipped.
  **Required fix**: Define table boundaries and explicitly reject non-separator/non-header row constructs inside configured inventory tables. This alters parser semantics against the source corpus and is not safe to infer automatically.

- **[P1.3] [fixed] [safe_auto]** [cg-schema, cg-security] `schema/extraction/inventory.py:114-192` - Source identity fields accepted malformed or incomplete identities.
  **Why**: `source_commit` and discrepancy claim commits accepted arbitrary strings, `source_repository` was unconstrained, and `chapter_sha256` accepted missing, extra, non-governed paths or malformed digests. A schema-valid ledger could therefore claim an unusable source identity.
  **Fix applied**: Require lowercase 40-character Git SHA-1 commits, the governed guideline repository, exactly the seven governed chapter paths, and lowercase 64-character SHA-256 chapter/blob/section hashes. Added malformed commit, repository, and chapter-set tests.

- **[P1.4] [open] [manual]** [cg-security, cg-correctness] `extraction_pipeline/inventory.py:299-308` - Closed source-map comparison excludes top-level identity fields.
  **Why**: The compiler regenerates and compares selected nested fields but omits `source_map_version`, `source_repository`, `source_commit`, and `source_identity_status` from the closed-map equality check. Separate commit/toolchain checks cover only part of this set, leaving declared top-level identity metadata outside the closed contract.
  **Required fix**: Validate the complete source-map model or compare every top-level identity field against regenerated values. Coordinate this with Task B's source-lock ownership rather than silently defining approval semantics in Task C.

- **[P1.5] [open] [manual]** [cg-security, cg-portability] `extraction_pipeline/inventory.py:286-294,297-324` - Draft-root containment and repository-relative path identity are not enforced.
  **Why**: Callers may supply an arbitrary or absolute draft root. `_drafts` follows that root and serializes `path.as_posix()`, so an absolute root leaks machine-specific paths into the ledger and a redirected root can substitute a different corpus while still satisfying IDs/counts.
  **Required fix**: Resolve the repository root explicitly, require the draft root to equal or remain within `extraction/20_drafts`, reject symlink escapes, and serialize normalized repository-relative paths. CLI/path semantics require manual approval.

### P2 - IMPORTANT

- **[P2.1] [fixed] [safe_auto]** [cg-testing] `tests/extraction/test_completeness.py:35-37` - Candidate-only coverage silently passed when no candidate was configured.
  **Why**: A bare `return` reported the test as passed even though no ledger was exercised, obscuring the distinction between executed coverage and an unavailable candidate.
  **Fix applied**: Replace the return with `pytest.skip("candidate-directed integration test")`, matching the inventory-suite convention and making the unexecuted condition explicit.

- **[P2.2] [open] [advisory]** [cg-governance] `.cg-docs/active-state/current.json:1-35` - Task C modified the shared active-state pointer outside its recorded workflow-managed allowlist.
  **Why**: The approved plan names the plan, roadmap, and work report as workflow-managed paths, but not `.cg-docs/active-state/current.json`. The implementation's own content audit excluded or tolerated this changed shared state while claiming only authorized paths changed.
  **Required fix**: Restore or reconcile the shared pointer through the owning workflow after review, and include active-state ownership explicitly in future approval records. This review does not modify another workflow's state.

### Verification

- Focused tests after safe fixes: `.venv/bin/python -m pytest tests/extraction/test_inventory.py tests/extraction/test_completeness.py -q` - **40 passed, 2 skipped**.
- Full repository tests: `.venv/bin/python -m pytest tests/ -q` - **307 passed, 4 skipped**.
- Protected artifacts were not modified by remediation.
