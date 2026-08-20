---
date: 2026-08-20
depth: light
parent-review: .cg-docs/reviews/2026-08-13-complete-non-welfare-extraction-review.md
type: verification
findings:
  P2.1: fixed
  P2.2: fixed
  P3.1: fixed
  P3.2: fixed
  P3.3: fixed
---

## Review Report

**Review mode**: verify (light)
**Files reviewed**: extraction_pipeline/review_agents/helpers.py, tests/review_agents/test_helpers.py, tests/review_agents/test_integration.py, extraction/25_agent_review/ (regenerated), roadmap.json
**Findings**: 5 (P0: 0, P1: 0, P2: 2, P3: 3)

Verification pass following the 2026-08-20 runner false-positive fix (exclude `runs/` from `list_drafts`). Core exclusion logic and its new unit tests are sound and deterministic; `pytest tests/review_agents/` = 54 passed; runner reports Errors: 0 | Warnings: 497, exit 0; no `runs/`/`project-documentation/` findings remain.

### P2 — IMPORTANT (should fix)

- **[P2.1]** [cg-testing] `extraction_pipeline/review_agents/helpers.py:52` — Docstring parity claim exceeds what code/tests verify.
  **Why**: `list_drafts` excludes at *any* depth, but `fix_derivation_asymmetry.py:43` excludes only when the *first* relative component matches (`rel.parts[0] in EXCLUDE_DIRS`). The docstring claims the exclusion "matches the exclude set used by fix_derivation_asymmetry.py", and `test_exclude_set_matches_asymmetry_tool` asserts only set identity, not behavioral parity. Divergence is latent today but re-creating the false-positive class if a nested excluded dir appears.
  **Fix**: Extract a shared `is_excluded_path(rel_path)` used by both `list_drafts` and `fix_derivation_asymmetry._collect_drafts`, or align `_collect_drafts` to any-depth; add a parity test over one fixture tree asserting identical result sets.

- **[P2.2]** [cg-testing] `tests/review_agents/test_integration.py:91-93` — `==0` flip is right direction but guards the wrong invariant.
  **Why**: `exit_code == 0` asserts the entire live corpus has zero errors — the runner's own job state — not the exclusion fix. Extraction is only ~15% complete; a genuine error in an in-progress draft fails this test identically to a broken `EXCLUDE_DIRS`, and cannot distinguish the empty-corpus shortcut from a real clean run, nor detect zombie findings for deleted drafts.
  **Fix**: Keep the corpus smoke assertion but add a fixture-based regression guard: tmp corpus with a `runs/` file that would error plus one clean VAR draft; assert `exit_code == 0` and no finding artifact_id under an excluded path.

### P3 — MINOR (nice to have)

- **[P3.1]** [cg-testing] `tests/review_agents/test_helpers.py:70-77` — Nested-exclusion coverage is one-sided.
  **Why**: `test_excludes_nested_excluded_dirs` only nests `runs`; nested `project-documentation` untested even though both names share identical code.
  **Fix**: Parametrize over both names (or nest both) so an accidental routing difference is caught.

- **[P3.2]** [cg-testing] `extraction_pipeline/review_agents/helpers.py:56` — Case sensitivity neither handled nor documented.
  **Why**: `EXCLUDE_DIRS & set(p.parts)` is case-sensitive exact match. A `Runs/`/`RUNS/` dir silently re-enters the corpus on case-sensitive filesystems (Linux CI).
  **Fix**: Document the lowercase convention on `EXCLUDE_DIRS`; if case-insensitive exclusion is intended, normalize parts (`.lower()`); add a regression test with a case variant.

- **[P3.3]** [cg-testing] `extraction_pipeline/review_agents/run_all_agents.py:105-115` — Regeneration never purges stale findings for files dropped from the corpus.
  **Why**: The 16 stale `runs/` yml required manual deletion (`write_findings` only writes, never cleans). Future draft deletions leave zombie findings, so findings drift from the corpus.
  **Fix**: Make the runner delete `output_dir/*.yml` whose `artifact_id` is not in the current corpus before writing; add an integration assertion.

### ⚠️ Incomplete Reviews

- `@cg-code-quality` did not produce usable output (empty result). Consider re-running `/cg-review` with a higher model tier, or invoke `@cg-code-quality` directly.

### ✅ Passed

- `@cg-testing`: No P0/P1 issues; core exclusion logic, new unit tests, and regeneration outputs verified sound.
