# Calibration Sample -- Human Review Application (Phase 5, Step 13 / V9)

- **Plan**: `.cg-docs/plans/2026-08-04-build-human-review-application.md` (Phase 5)
- **Roadmap milestone**: `calibrate-human-review` (`select-calibration-sample`, `review-calibration-sample`)
- **Date**: 2026-08-06
- **Purpose**: define the representative sample the review application is validated
  against before scaling, per plan Step 13 (R21) and the roadmap planned sample of
  five to ten variables across complexity levels.

## Selection method

1. Seed the sample from the only real CVS variables present in this repository
   (`knowledge/variables/`, approved artifacts): `VAR-male`, `VAR-educat4`,
   `VAR-educy`.
2. Extend to cover complexity levels and modules not yet present in the variable
   pool (the extraction milestone has not yet produced drafts under
   `extraction/20_drafts/`), using representative fixture artifacts that mirror
   the dashboard test fixtures already in `review-app/tests/testthat/test-index.R`.
3. Target range: 5-10 members spanning the `simple` / `standard` / `complex`
   tiers. The runnable harness in
   `review-app/tests/testthat/test-integration.R` materializes each member as
   in-memory adaptor store state matching the application's data model.
4. Transparency: members marked `fixture` are representative and MUST be
   replaced by real extraction drafts before the live operator run (see the
   execution-report deployment checklist, `2026-08-04-build-human-review-application.md` Run 5).

## Sample members

| # | artifact_id | module | source_artifact_path (draft) | complexity | origin |
|---|-------------|--------|------------------------------|------------|--------|
| 1 | `VAR-male` | `dem` | `extraction/20_drafts/dem/VAR-male.md` | simple | real (knowledge/variables/dem/VAR-male.md) |
| 2 | `VAR-educat4` | `edu` | `extraction/20_drafts/edu/VAR-educat4.md` | simple | real (knowledge/variables/edu/VAR-educat4.md) |
| 3 | `VAR-educy` | `edu` | `extraction/20_drafts/edu/VAR-educy.md` | standard | real (knowledge/variables/edu/VAR-educy.md) |
| 4 | `VAR-educat7` | `edu` | `extraction/20_drafts/edu/VAR-educat7.md` | standard | fixture (in-review queue fixture) |
| 5 | `VAR-urban` | `geo` | `extraction/20_drafts/geo/VAR-urban.md` | complex | fixture (needs-revision queue fixture) |
| 6 | `VAR-marital` | `dem` | `extraction/20_drafts/dem/VAR-marital.md` | complex | fixture (approved-reopen path) |

## State-machine paths exercised (Step 13 test scenarios)

For at least one artifact per path (verified in `test-integration.R`):

| Path | Members | Flow |
|------|---------|------|
| Approve direct | `VAR-male`, `VAR-educat4` | draft -> submitted -> approved (writes `extraction/40_approved/`) |
| Needs-revision loop | `VAR-educy`, `VAR-educat7` | draft -> submitted -> request-revision -> needs-revision -> submitted (round++) -> approved |
| Admin reopen | `VAR-marital` | approved -> reopened (administrator) -> needs-revision |

Stale-write rejection, unauthorized-action rejection, and the dashboard index
reflecting durable review-branch state are asserted at integration level for the
same sample.

## How this is used

- `review-app/tests/testthat/test-integration.R` is the executed check (V9).
- This manifest is the durable record backing the roadmap `select-calibration-sample`
  feature; the live operator run replaces fixture members with real drafts and
  follows the execution-report deployment checklist.
