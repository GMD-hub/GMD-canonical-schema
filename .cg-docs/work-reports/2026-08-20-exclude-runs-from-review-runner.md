---
date: 2026-08-20
plan: .cg-docs/plans/2026-08-20-exclude-runs-from-review-runner.md
plan-title: "Exclude runs/ from the review runner to eliminate 40 false-positive errors"
status: complete
run: 1
---

# Work Report: Exclude runs/ from the review runner

## Run 1 (2026-08-20)

### Plan reference
- plan: `.cg-docs/plans/2026-08-20-exclude-runs-from-review-runner.md`

### Active deviation policy
- `ask` (plan stored value; no runtime deviate override)

### Setup / context
- Branch: `fix/exclude-runs-from-list-drafts`
- Plan validation: `cg-render-artifact --validate-only` PASSED (exit 0).
- Roadmap feature `fix-review-runner-runs-exclusion` set to `active` -> `done`.
- Baseline: runner reported 40 errors / 497 warnings; all errors from 4 `runs/` files.

### Completed steps / phases
- Phase 1 (2026-08-20): core fix + test reconciliation
  - Task 1: added `EXCLUDE_DIRS = {"project-documentation", "runs"}` to `helpers.py`; rewrote `list_drafts` to any-depth exclude via `not (EXCLUDE_DIRS & set(p.parts))`.
  - Task 2: flipped `test_runner_exit_code` from `==1` to `==0`.
  - Task 3: added `TestListDrafts::test_excludes_runs_and_project_documentation`, `test_excludes_nested_excluded_dirs`, `test_exclude_set_matches_asymmetry_tool`.
  - Red-phase confirmed: new tests failed against unfixed code (ImportError: EXCLUDE_DIRS missing); green after fix.
- Phase 2 (2026-08-20): stale-artifact cleanup + verification
  - Task 4: `git rm` 16 stale `runs/` findings (staged `D` entries, verified count == 16, no other files).
  - Task 5: runner regeneration: `Checked 267 drafts with 4 agents; Total findings: 497; Errors: 0; Warnings: 497; exit 0`.
  - Task 6: verified SUMMARY header `Total errors: 0 | Total warnings: 497`; no `runs/` rows; zero `runs/`-prefixed yml in 25_agent_review.
  - Task 7: full suite `pytest tests/ -q` -> 281 passed, 2 skipped.
  - Task 8: git commit deferred to Operation 5 `/cg-commit-push-pr` per user's sequential operation list (working tree intentionally left uncommitted).

### Deviations
- Commit (plan Task 8) deferred to `/cg-commit-push-pr` (Op5 of the user's requested sequence). No code deviation; delivery sequencing only.

### Accepted exceptions
- (none)

### Evidence table (plan Verification Surface)
| ID | Evidence | Status |
|----|----------|--------|
| V1 | list_drafts excludes runs/ + project-documentation/ (unit test) | passed |
| V2 | Runner exit code is 0 (was 1) | passed |
| V3 | Runner stdout: Errors: 0, exit 0 | passed |
| V4 | SUMMARY.md: Total errors 0, no runs/ rows, warnings 497 | passed |
| V5 | No runs/ yml in 25_agent_review/ | passed |
| V6 | Full suite green (281 passed, 2 skipped) | passed |

### Constraints check (plan Constraints)
| ID | Check | Status |
|----|-------|--------|
| C1 | EXCLUDE_DIRS matches fix_derivation_asymmetry.py:25 = {"project-documentation", "runs"} | passed |
| C2 | any-depth matching `not (EXCLUDE_DIRS & set(p.parts))` | passed |
| C3 | no refactor of fix_derivation_asymmetry.py to import constant | passed |
| C4 | no relocation of runs/ files out of 20_drafts/ | passed |
| C5 | delete 16 stale findings before regeneration | passed |

### Remaining uncertainty
- Commit not yet created (deferred to Op5); PR/CI not yet run.

### Final status
- completed (plan marked `completed`, completed-date 2026-08-20)
