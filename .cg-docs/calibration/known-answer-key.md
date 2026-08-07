# Calibration Known-Answer Key

- **Plan**: `.cg-docs/plans/2026-08-07-calibrate-human-review.md` (Phase 3, Step 9)
- **Requirements**: R19, R11 (C11)
- **Date**: 2026-08-07
- **Purpose**: scoring reference for the live run (Step 12). Kept separate from
  the drafts; used only for scoring, never shared with reviewers during the run.

## Seeded known defects

| # | Artifact | Location | Category | Severity | Description |
|---|----------|----------|----------|----------|-------------|
| 1 | `VAR-educat7` | frontmatter `rules` | schema-compliance | block | Hallucinated rule reference `RULE-EDU-999` (does not exist in `knowledge/index.md`). |
| 2 | `VAR-educat7` | `## Escalation triggers` | completeness | major | Missing escalation-trigger content: section is a stub (`(TODO: escalate when mapping is ambiguous.)`). |
| 3 | `VAR-urban` | frontmatter `module_id` | consistency-derivation | block | `module_id: MOD-DEM` while the file lives under `extraction/20_drafts/geo/` (should be `MOD-GEO`; P1.3/Q3 module_id-authoritative). |
| 4 | `VAR-urban` | frontmatter `derived_from` | consistency-derivation | major | Derivation-graph break: `derived_from` references `VAR-rurality`, a non-existent variable. |
| 5 | `VAR-marital` | `## Construction notes` | completeness | block | Stub section: content is `TODO.` (< 50 characters, Layer 1 non-stub rule). |
| 6 | `VAR-marital` | frontmatter `value_codes` | formatting | minor | `value: 5` label is `"unknown"` — not a valid/canonical category label (should be a capitalized, self-describing label). |

## Scoring reference

- Human catch rate = (seeded defects identified by reviewers) / 6.
- Layer 1 (automated structural) catch rate = seeded defects the automated
  rubric gate flags / 6.
- False negatives = seeded defects not detected by either layer.
- If all or none are caught, the calibration is uninformative and Step 12
  recommends a re-run with adjusted defects.

## Materialization-time errors (not seeded; logged to content-error log)

- **E-EDU-MOD**: the calibration manifest and `test-integration.R` originally
  assigned `module = "edu"` to `VAR-educat4`, `VAR-educy`, `VAR-educat7`, but
  the real artifacts carry `module_id: MOD-DEM` and live under
  `knowledge/variables/dem/`; `knowledge/variables/edu/` is empty. Corrected to
  `dem/` (P1.3); logged as `consistency-derivation`, stage `extraction`,
  severity `major`.
