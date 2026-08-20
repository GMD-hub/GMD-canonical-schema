---
date: 2026-08-20
title: "Exclude non-variable dirs from the review runner to eliminate false-positive errors"
category: "testing-patterns"
language: "Python"
tags: [agent-review, review-runner, list_drafts, exclude-dirs, false-positive, regression-guard, stale-findings, EXCLUDE_DIRS]
root-cause: "The review runner's draft enumerator (helpers.list_drafts) only excluded project-documentation/, while fix_derivation_asymmetry.py already excluded project-documentation/ AND runs/ via EXCLUDE_DIRS. The runs/ tracking files (date/plan/source-commit frontmatter, no variable_id) were misvalidated as VariableDefinitions, producing all 40 runner errors."
severity: "P2"
---

# Exclude non-variable dirs from the review runner to eliminate false-positive errors

## Problem

The agent review runner reported **40 errors / 497 warnings** across 271 drafts
(`extraction/25_agent_review/`). All 40 errors traced to the 4 files in
`extraction/20_drafts/runs/` (`completeness-2026-08-13.md`, `inventory-2026-08-13.md`,
`source-acquisition-2026-08-13.md`, `source-lock-2026-08-13.md`) — run-tracking
metadata, not variable definitions. Zero actual `VAR-*` drafts had errors.
The runner exited 1, blocking CI and drowning real findings in noise.

## Root Cause

`extraction_pipeline/review_agents/helpers.py::list_drafts` skipped only the
`project-documentation/` directory during recursive `.md` enumeration, while
`extraction_pipeline/fix_derivation_asymmetry.py` already excluded both
`project-documentation/` and `runs/` via its `EXCLUDE_DIRS` constant. The two
enumerators drifted out of sync: the runner validated run-tracking files
(which have no `variable_id`) as if they were `VariableDefinition`s, and
schema compliance flagged them en masse.

## Solution

1. **Centralize the exclude set in `helpers.py`** (matching
   `fix_derivation_asymmetry.py`):
   ```python
   EXCLUDE_DIRS: set[str] = {"project-documentation", "runs"}
   ```
2. **Rewrite `list_drafts`** to use any-depth set intersection:
   ```python
   return sorted(
       p for p in drafts_dir.rglob("*.md")
       if not (EXCLUDE_DIRS & set(p.parts))
   )
   ```
   (Chosen over top-level-only matching so a nested `dem/runs/x.md` never
   slips through — a deliberate, documented divergence from
   `fix_derivation_asymmetry._collect_drafts`, which matches only the first
   path component.)
3. **Flip the exit-code integration test** from `==1` to `==0` (the old value
   locked in the bug).
4. **Delete the 16 stale `runs/` findings yml** (`git rm`) *before*
   regenerating, so non-reappearance confirms the fix.
5. **Regenerate** via
   `.venv/bin/python -m extraction_pipeline.review_agents.run_all_agents`
   → `Errors: 0 | Warnings: 497`, exit 0.
6. **Hardening from review (this session)**:
   - `_purge_stale_findings()` in `run_all_agents.py` deletes
     `output_dir/*.yml` whose `artifact_id` is no longer in the corpus, so
     findings can never drift from SUMMARY.md again.
   - Fixture-based integration test (`test_runner_excludes_runs_fixture`)
     builds a tmp corpus with a broken `runs/` file + one clean draft and
     asserts exit 0 — guards the *exclusion itself*, not just the live corpus.

## Prevention

- **Centralize exclude constants** in one module (`EXCLUDE_DIRS`) and keep the
  enumerators' exclude *sets* in sync. Unifying matching depth across both is
  an accepted low-risk divergence (documented in plan Risk R4).
- **Never assert a runner's exit/product as the core regression guard** by
  itself — the live corpus can have real errors unrelated to your change. Add
  a fixture that isolates the exact behavior.
- **Add stale-output purge to any regenerator**: writing findings/artifacts
  per corpus member without cleaning files for members that disappeared lets
  zombie outputs silently drift from the summary.
- When enumerating a knowledge repo, treat every non-`variable_id` subdir as a
  candidate exclusion and record the convention (e.g. lowercase, case-sensitive
  exact match) next to the constant.

## Related

- `testing-patterns/2026-08-17-parameter-registry-loading.md` — companion
  false-positive source in the same runner (registry not loaded).
- Plan: `.cg-docs/plans/2026-08-20-exclude-runs-from-review-runner.md`
- Work report: `.cg-docs/work-reports/2026-08-20-exclude-runs-from-review-runner.md`
