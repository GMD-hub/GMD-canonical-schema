# Calibration Measurement Framework

- **Plan**: `.cg-docs/plans/2026-08-07-calibrate-human-review.md` (Phase 2, Step 6)
- **Requirements**: R13, R14
- **Status**: draft (finalized alongside the rubric in Step 14)
- **Date**: 2026-08-07

This framework defines how content errors are classified, recorded, and
aggregated during the calibration run, and how app defects are logged
separately so they never dilute content-error rates (C13).

## 1. Content-error taxonomy

Errors are classified along two axes per artifact review: an `agent-review`
category (reserved for the future `independent-agent-review` milestone) and a
`human-review` category (active in this calibration). Each dimension maps to
one of each, keeping the taxonomy aligned with the four planned agent-review
dimensions.

| Dimension | Agent-review category | Human-review category |
|---|---|---|
| Source-grounding | `source-grounding` | `content-accuracy` |
| Schema-compliance | `schema-compliance` | `formatting` |
| Rules-caveats | `rules-caveats` | `completeness` |
| Consistency-derivation | `consistency-derivation` | `clarity` |

In this calibration, only `extraction` and `human-review` stages are
populated. `agent-review` categories are reserved and tagged-but-not-populated
(they become active when the `independent-agent-review` milestone lands).

## 2. Content-error record schema

Each content-error record is a structured YAML mapping:

```yaml
error_id: ERR-<artifact_id>-<seq>
artifact_id: VAR-male
stage: extraction            # extraction | human-review | agent-review
category: content-accuracy   # one of the active categories above
severity: major              # block | major | minor | info
description: One clear, self-contained sentence describing the error.
detected_by: reviewer@example.org        # reviewer identity, rubric layer, or automated check name
detected_at: 2026-08-07T14:00:00Z         # RFC 3339 UTC
section: "Construction notes"             # which Markdown section, or frontmatter/field name
status: open                 # open | resolved | escalated
```

Field rules:

- `severity` uses the content-error scale only (`block` / `major` / `minor` /
  `info`). App-defect severity (P0/P1/P2/P3) belongs in the defect log only.
- `detected_by` records the reviewer identity for human findings, `Layer 1` or
  `Layer 2` for rubric-driven findings, or the automated-check name for
  extraction-time findings.
- `detected_at` is RFC 3339 UTC timestamps (matching the review-record
  `occurred_at` convention).
- `stage` describes where the error was introduced/detected. Calibration
  yields `extraction` (materialization inconsistencies) and `human-review`
  (quality defects found by reviewers).

## 3. App-defect log schema (separate; C13)

App defects are defects in the review application itself, not in the reviewed
content. They are recorded in a **separate** log and use a different severity
scale so they cannot dilute content-error rates.

```yaml
defect_id: DEF-<seq>
component: github_adapter          # e.g. github_adapter, frontmatter, preview, editor, index
severity: P1                        # P0 | P1 | P2 | P3
description: One clear sentence describing the app defect.
source: live-run-observation        # execution-report-review | live-run-observation
status: open                        # open | fixed | deferred
fix_reference: null                 # plan step or commit that fixed it, when fixed
```

Aggregation must keep content-error rates computed from the content-error log
only. App defects are reported separately (counts and severities), never added
to content-error numerators/denominators.

## 4. Aggregation outputs (consumed by Step 12)

- Content-error count by `category` and `severity`, per artifact.
- Catch rate vs known-answer key (detected / total seeded defects).
- False negatives (seeded defects not detected).
- Layer 1 (automated) catch rate separately from human catch rate.
- App-defect counts by severity; where Phase 1 had already "fixed" the defect
  versus newly discovered in the live run.

## 5. Self-describing examples

See the populated logs created in Phase 4 (Step 11):
`content-error-log.yaml` and `defect-log.yaml` under `.cg-docs/calibration/`.
