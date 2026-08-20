---
date: 2026-08-20
title: "Exclude runs/ from the review runner to eliminate 40 false-positive errors"
status: completed
completed-date: 2026-08-20
scope: "Standard"
brainstorm: null
language: "Python"
estimated-effort: "small"
deviation-policy: "ask"
artifact-schema-version: 1
tags: [agent-review, review-runner, list-drafts, bugfix, false-positive, exclude-dirs]
phases: 2  # convenience hint -- may be stale; always recount from ## Phase headers
completed-phases: [1, 2]
execution-report: .cg-docs/work-reports/2026-08-20-exclude-runs-from-review-runner.md
---

# Plan: Exclude runs/ from the review runner to eliminate 40 false-positive errors

## Objective

Drive the agent review error count from **40 -> 0** by aligning
`extraction_pipeline/review_agents/helpers.py::list_drafts` with the
`EXCLUDE_DIRS` convention already used by `fix_derivation_asymmetry.py`. The
four `extraction/20_drafts/runs/` files are run-tracking metadata (frontmatter
= `date`/`plan`/`source-commit`, no `variable_id`), not `VariableDefinition`s;
misvalidating them produced all 40 review errors. Zero variable drafts (267
`VAR-*`) have errors. After the fix the runner reports `Errors: 0`, exit code
0, and the 16 stale `runs/` findings are removed without reappearing.

## Context

- Agent review run (commit `203cba9`, 2026-08-20) reported **40 errors / 497
  warnings** across 271 drafts.
- **All 40 errors** come from the 4 files in `extraction/20_drafts/runs/`
  (`completeness-2026-08-13.md`, `inventory-2026-08-13.md`,
  `source-acquisition-2026-08-13.md`, `source-lock-2026-08-13.md`). These
  contributed **40 errors and 0 warnings**, so excluding them drops the total
  to **0 errors / 497 warnings** (no signal lost).
- **Root cause:** `helpers.py:44-53` `list_drafts` skips only
  `project-documentation/`, while `fix_derivation_asymmetry.py:25` already
  excludes both via `EXCLUDE_DIRS = {"project-documentation", "runs"}`. The
  review runner's exclude *set* drifted out of sync.
- **Safe to delete stale findings:** no test references the 16 `runs/`
  findings by name (grep of `tests/` for the four basenames returns nothing).
  `fix_derivation_asymmetry.py` is the only other `20_drafts` enumerator; the
  review-app R tests reference specific draft files, not enumeration, so they
  are unaffected.
- **Prior related work (completed):** `.cg-docs/plans/2026-08-17-fix-parameter-registry-loading-review-runner.md`
  (status: done) fixed a *different* false-positive class (parameter-registry
  loading). This plan is complementary — a distinct false-positive source.

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | `list_drafts` must exclude `runs/` and `project-documentation/` (any-depth) | D1, D3 |
| R2 | `EXCLUDE_DIRS` centralized as a module constant matching `fix_derivation_asymmetry.py:25` | D2 |
| R3 | `test_runner_exit_code` must assert exit code `0` (was `1`) | D5 |
| R4 | New unit test must assert `runs/` and `project-documentation/` exclusion | Task 3 |
| R5 | The 16 stale `runs/` findings yml must be deleted from `25_agent_review/` | D4 |
| R6 | Runner regeneration must report `Errors: 0`, exit 0, no `runs/` findings reappear | Tasks 5-6 |
| R7 | Full test suite must pass with no regressions outside `review_agents/` | Task 7 |

## Implementation Steps

## Phase 1: Core fix and test reconciliation

### 1. Fix `list_drafts` exclusion (the core fix)

- **Requirements**: R1, R2
- **Files**: `extraction_pipeline/review_agents/helpers.py`
- **Details**:
  - Add a module constant near `REQUIRED_SECTIONS` (after line 23):
    ```python
    EXCLUDE_DIRS = {"project-documentation", "runs"}
    ```
  - Replace `list_drafts` (lines 44-53). Current:
    ```python
    def list_drafts(drafts_dir: Path) -> list[Path]:
        """Yield all .md files recursively from the drafts directory.
        Skips files inside the ``project-documentation/`` subdirectory
        (process docs, not variable definitions).
        """
        return sorted(
            p for p in drafts_dir.rglob("*.md")
            if "project-documentation" not in p.parts
        )
    ```
    New (any-depth, now also skips `runs/`):
    ```python
    def list_drafts(drafts_dir: Path) -> list[Path]:
        """Yield all .md files recursively from the drafts directory.
        Skips files inside the ``project-documentation/`` (process docs)
        and ``runs/`` (run-tracking metadata) subdirectories, which are not
        variable definitions. Matches the exclude set used by
        ``fix_derivation_asymmetry.py`` (EXCLUDE_DIRS).
        """
        return sorted(
            p for p in drafts_dir.rglob("*.md")
            if not (EXCLUDE_DIRS & set(p.parts))
        )
    ```
  - `from __future__ import annotations` is already present (line 4), so no
    version concern on either Python 3.11 (CI) or 3.14 (local `.venv`).
- **Test Scenarios**: `runs/x.md` excluded; `project-documentation/x.md`
  excluded; nested excluded dir (e.g. `sub/runs/x.md`) excluded by any-depth;
  top-level `VAR-x.md` retained; non-excluded subdir `dem/VAR-y.md` retained.
- **Tests**: `tests/review_agents/test_helpers.py` (Task 3)
- **Acceptance criteria**: `list_drafts` returns no path containing `runs` or
  `project-documentation` as a component.

### 2. Flip the test that locks in the bug

- **Requirements**: R3
- **Files**: `tests/review_agents/test_integration.py`, method
  `test_runner_exit_code` (lines 91-93)
- **Details**: Current:
  ```python
  def test_runner_exit_code(self, tmp_path):
      _, exit_code = run(DRAFTS_DIR, tmp_path)
      assert exit_code == 1, "Expected exit code 1 due to known errors in non-variable calibration files"
  ```
  New:
  ```python
  def test_runner_exit_code(self, tmp_path):
      _, exit_code = run(DRAFTS_DIR, tmp_path)
      assert exit_code == 0, "Expected exit code 0: runs/ and project-documentation/ are excluded; no variable draft has errors"
  ```
- **Test Scenarios**: runner against real `extraction/20_drafts` returns exit
  0; previously returned 1 (regression guard).
- **Tests**: `pytest tests/review_agents/test_integration.py::TestFullPipeline::test_runner_exit_code -v`
- **Acceptance criteria**: assertion is `== 0`; comment updated to reflect
  the fix rationale.

### 3. Add skip-behavior unit test

- **Requirements**: R4
- **Files**: `tests/review_agents/test_helpers.py`, class `TestListDrafts`
- **Details**: Add `test_excludes_runs_and_project_documentation` that builds a
  tmp tree:
  - `<tmp>/VAR-x.md` (top-level draft)
  - `<tmp>/runs/inventory.md`
  - `<tmp>/project-documentation/wiki.md`
  - Assert `list_drafts(tmp)` returns exactly one path whose name is
    `VAR-x.md`.
  - Existing `test_finds_md_files` (creates `a.md`, `b.txt`, `sub/c.md`, no
    excluded dirs -> 2 `.md`) still passes unchanged.
- **Test Scenarios**: excluded dirs produce zero results; included draft
  retained; non-`.md` files ignored (covered by existing test).
- **Tests**: `pytest tests/review_agents/test_helpers.py::TestListDrafts -v`
- **Acceptance criteria**: new test passes; existing `TestListDrafts` tests
  still pass.

## Phase 2: Stale-artifact cleanup and verification

### 4. Delete stale `runs/` findings (before regenerating)

- **Requirements**: R5
- **Files**: `extraction/25_agent_review/` (16 yml files)
- **Details**: `git rm` these 16 files (stages the deletions):
  ```
  completeness-2026-08-13.schema_compliance.yml
  completeness-2026-08-13.source_grounding.yml
  completeness-2026-08-13.rules_caveats.yml
  completeness-2026-08-13.consistency_derivation.yml
  inventory-2026-08-13.schema_compliance.yml
  inventory-2026-08-13.source_grounding.yml
  inventory-2026-08-13.rules_caveats.yml
  inventory-2026-08-13.consistency_derivation.yml
  source-acquisition-2026-08-13.schema_compliance.yml
  source-acquisition-2026-08-13.source_grounding.yml
  source-acquisition-2026-08-13.rules_caveats.yml
  source-acquisition-2026-08-13.consistency_derivation.yml
  source-lock-2026-08-13.schema_compliance.yml
  source-lock-2026-08-13.source_grounding.yml
  source-lock-2026-08-13.rules_caveats.yml
  source-lock-2026-08-13.consistency_derivation.yml
  ```
  Leave `parameter-stub-audit.md` and all `VAR-*.*.yml` untouched. Do this
  **before** Task 5 so regeneration confirms the runner no longer emits them
  (they will not reappear because `runs/` is now excluded).
- **Test Scenarios**: the 16 files are staged for deletion; non-`runs/`
  findings untouched.
- **Tests**: `git status --short extraction/25_agent_review/` shows 16 `D`
  entries.
- **Acceptance criteria**: 16 files staged for deletion; no other
  `25_agent_review/` file touched.

### 5. Regenerate findings

- **Requirements**: R6
- **Files**: `extraction/25_agent_review/` (output)
- **Details**:
  ```bash
  .venv/bin/python -m extraction_pipeline.review_agents.run_all_agents
  ```
  - Expected stdout: `Errors: 0`; exit code 0 (no longer 1).
  - The runner overwrites the 267 `VAR-*` findings and `SUMMARY.md`; the 16
    deleted `runs/` files must **not** reappear.
- **Test Scenarios**: stdout reports 0 errors; exit 0; deleted files absent.
- **Tests**: Task 6 verification.
- **Acceptance criteria**: runner stdout reads `Errors: 0`; exit code 0.

### 6. Verify outputs

- **Requirements**: R6
- **Files**: `extraction/25_agent_review/SUMMARY.md`, `extraction/25_agent_review/`
- **Details**:
  - `SUMMARY.md`: no rows for
    `completeness/inventory/source-acquisition/source-lock-2026-08-13`;
    header reads `**Total errors:** 0 | **Total warnings:** 497`.
  - `25_agent_review/` contains no `completeness-*` / `inventory-*` /
    `source-acquisition-*` / `source-lock-*` yml (confirm the 16 deletions
    stuck and none regenerated).
  - Warnings count is still ~497 (confirms only the 40 errors were removed;
    `runs/` files contributed 0 warnings).
- **Test Scenarios**: SUMMARY header matches expected counts; no orphaned
  `runs/` findings; warnings stable.
- **Tests**: manual inspection of `SUMMARY.md` + `ls` of `25_agent_review/`.
- **Acceptance criteria**: `Total errors: 0 | Total warnings: 497`; zero
  `runs/`-prefixed yml.

### 7. Run tests

- **Requirements**: R7
- **Files**: `tests/review_agents/`, `tests/`
- **Details**:
  ```bash
  .venv/bin/python -m pytest tests/review_agents/ -v
  ```
  - All green. Key checks: `test_runner_exit_code` (now expects 0), new
    `test_excludes_runs_and_project_documentation`, existing
    `TestListDrafts.test_finds_md_files` still passes.
  - Optional full-suite (matches CI `.github/workflows/validate.yml` step
    `python3 -m pytest tests/ -v`):
    ```bash
    .venv/bin/python -m pytest tests/ -q
    ```
    Expected: no regressions outside `review_agents/`.
- **Test Scenarios**: targeted suite green; full suite green.
- **Tests**: the commands above.
- **Acceptance criteria**: `tests/review_agents/` all pass; full suite (if
  run) shows no failures outside `review_agents/`.

### 8. Commit

- **Requirements**: R5, R6, R7
- **Files**: working tree
- **Details**:
  ```bash
  git add extraction_pipeline/review_agents/helpers.py tests/review_agents/
  git add -A extraction/25_agent_review/
  git commit -m "fix(review-agents): exclude runs/ from list_drafts, drop 40 false-positive errors -- Aligns list_drafts' exclude set with EXCLUDE_DIRS already used by fix_derivation_asymmetry.py. The 4 files in extraction/20_drafts/runs/ are run-tracking metadata (no variable_id), not VariableDefinitions; they produced all 40 review errors. Zero variable drafts had errors. Stale runs/ findings yml removed; SUMMARY regenerated to 0 errors."
  ```
  - `git add -A extraction/25_agent_review/` captures both the 16 deletions
    (staged by `git rm`) and the regenerated `VAR-*` / `SUMMARY.md`
    modifications in one step.
- **Test Scenarios**: commit contains exactly the intended files.
- **Tests**: `git show --stat HEAD`.
- **Acceptance criteria**: clean commit with the helpers change, test
  changes, 16 deletions, and regenerated findings.

## Testing Strategy

- **Unit**: `TestListDrafts` gains `test_excludes_runs_and_project_documentation`
  (Task 3) — directly locks in the exclusion contract.
- **Integration**: `test_runner_exit_code` flips from `==1` to `==0` (Task 2)
  — end-to-end guard against regression; runs the real runner against
  `extraction/20_drafts`.
- **Full suite**: `pytest tests/ -q` (Task 7) ensures no regression outside
  `review_agents/` (matches the CI step in
  `.github/workflows/validate.yml`).
- **Runtime verification**: regeneration (Task 5) + output inspection (Task 6)
  confirms the real-world error count dropped to 0 and the 16 stale files do
  not reappear.

## Documentation Checklist

- [ ] `helpers.py` `list_drafts` docstring updated to mention `runs/` and the
      `EXCLUDE_DIRS` convention (inline in Task 1).
- [ ] No README changes required for this fix (the runner README's stale
      calibration notes are a separate, already-tracked follow-up).
- [ ] Commit message documents the root cause and the alignment with
      `fix_derivation_asymmetry.py`.

## Risks & Mitigations

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|-----------|--------|-----------|
| R1 | CI test breakage: `test_runner_exit_code` asserts `==1` | Low (after Task 2) | High | Task 2 flips the assertion; if skipped, CI `pytest tests/ -v` fails. |
| R2 | Future drift: a new non-variable subdir under `20_drafts/` is scanned until added to `EXCLUDE_DIRS` | Medium | Low | Centralizing the constant (D2) makes the one-place fix obvious. Auto-detecting new dirs is out of scope. |
| R3 | Loss of historical flags: deleting 16 `runs/` findings drops the record they were once flagged | Low | Low | Acceptable — the flags were false positives; the source `runs/*.md` files themselves remain in `20_drafts/runs/`. |
| R4 | Divergent matching models: `list_drafts` (any-depth) vs `fix_derivation_asymmetry.py` (top-level) keep different models, same set | Low | Low | They diverge only for hypothetical nested dirs like `dem/runs/x.md`. No such case exists today; none expected given the top-level convention. Unifying is out of scope. |
| R5 | Regeneration overwrites 267 `VAR-*` findings + `SUMMARY.md`; a latent runner issue could introduce noise | Low | Medium | Task 6 verifies `SUMMARY` shows `0 errors / 497 warnings` (matches expected); deviation triggers Iteration Policy 2. |

## Out of Scope

- Filling ~200 empty stub sections (`Common mistakes`, `Escalation triggers`)
  — governed by `.cg-docs/plans/2026-08-13-complete-non-welfare-extraction.md`
  and the sequencing decision that extraction precedes review-agent tuning.
- Tuning `rules_caveats` vague-text regex and escalation IF/WHEN heuristic
  (~150 false-positive warnings) — runner calibration, separate task.
- Real draft-content warnings: `derived_from` dependency not mentioned in
  Construction notes (55, e.g. `VAR-laborincome`->`VAR-lincnc`);
  `VAR-primarycomp` value-codes mismatch (2); `VAR-urban` unresolved ref to
  not-yet-extracted `VAR-rurality` (expected, not a defect).
- Optional hardening: have `fix_derivation_asymmetry.py` import `EXCLUDE_DIRS`
  from `helpers` to unify the set (and optionally the matching model) and
  prevent future drift.
- Optional doc nit: `extraction_pipeline/review_agents/README.md` calibration
  notes still say the `PARAM-*`/`RULE-*` registries are empty (stale since
  the parameter-registry runner fix `42f5c56`).
- Relocating the 4 `runs/` files out of `20_drafts/` (breaks path references
  and diverges from `fix_derivation_asymmetry.py`'s assumption).

## Completion Contract

### Outcome

The review runner reports **0 errors** (down from 40) with exit code 0;
`runs/` and `project-documentation/` are excluded from `list_drafts` via a
centralized `EXCLUDE_DIRS` constant matching `fix_derivation_asymmetry.py`;
the 16 stale `runs/` findings are deleted and do not reappear after
regeneration; the full test suite passes with `test_runner_exit_code`
expecting 0.

### Verification Surface

| ID | Evidence Required | Command/Artifact | Required | Phase |
|----|-------------------|------------------|----------|-------|
| V1 | `list_drafts` excludes `runs/` + `project-documentation/` | `pytest tests/review_agents/test_helpers.py::TestListDrafts::test_excludes_runs_and_project_documentation -v` | yes | 1 |
| V2 | Runner exit code is 0 (was 1) | `pytest tests/review_agents/test_integration.py::TestFullPipeline::test_runner_exit_code -v` | yes | 1 |
| V3 | Runner stdout: `Errors: 0`, exit 0 | `.venv/bin/python -m extraction_pipeline.review_agents.run_all_agents` | yes | 2 |
| V4 | `SUMMARY.md`: `Total errors: 0`, no `runs/` rows, warnings ~497 | `extraction/25_agent_review/SUMMARY.md` | yes | 2 |
| V5 | No `runs/` findings yml in `25_agent_review/` | `ls extraction/25_agent_review/ \| grep -E 'completeness\|inventory\|source-acquisition\|source-lock'` (empty) | yes | 2 |
| V6 | Full suite green, no regressions | `.venv/bin/python -m pytest tests/ -q` | yes | 2 |

### Constraints

| ID | Constraint | Check |
|----|------------|-------|
| C1 | `EXCLUDE_DIRS` set matches `fix_derivation_asymmetry.py:25` exactly | `{"project-documentation", "runs"}` |
| C2 | `list_drafts` keeps any-depth matching (not top-level-only) | `not (EXCLUDE_DIRS & set(p.parts))` |
| C3 | Do not refactor `fix_derivation_asymmetry.py` to import the constant | out of scope |
| C4 | Do not relocate `runs/` files out of `20_drafts/` | AGENTS.md sanctions their location |
| C5 | Delete 16 stale findings *before* regeneration so non-reappearance confirms the fix | Task 4 precedes Task 5 |

### Boundaries

- **Allowed**: `helpers.py` (`EXCLUDE_DIRS` + `list_drafts`);
  `test_integration.py` (exit-code flip); `test_helpers.py` (new exclusion
  test); `git rm` 16 stale yml; regenerate findings; run tests.
- **Out of scope**: 497 warnings; stub-section filling; vague-text/escalation
  heuristic tuning; unifying the two matching models;
  `fix_derivation_asymmetry.py` import refactor; relocating `runs/` files.

### Iteration Policy

1. If regeneration shows >0 errors from a `VAR-*` draft (not `runs/`),
   investigate — may indicate a real defect, not a false positive.
2. If warnings count deviates from ~497, check whether a real `VAR-*` draft
   was accidentally excluded.
3. If a new non-variable subdir is later added under `20_drafts/`, add it to
   `EXCLUDE_DIRS` (same maintenance burden as today).

### Blocked-Stop Conditions

- Regeneration reports errors from a `VAR-*` draft — real defect requiring
  investigation before proceeding.
- Any test outside `review_agents/` regresses after the change.
- `SUMMARY.md` warnings count deviates significantly from 497 — suggests the
  exclusion affected real drafts.
