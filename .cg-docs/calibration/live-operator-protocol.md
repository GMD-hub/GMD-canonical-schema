# Live-Operator Protocol and Friction Log

- **Plan**: `.cg-docs/plans/2026-08-07-calibrate-human-review.md` (Phase 2, Step 8)
- **Requirements**: R16
- **Status**: draft (used by Phase 4 live run)
- **Date**: 2026-08-07

This is the structured protocol for the live calibration run and the format of
the per-step friction log.

## Roles

- **Reviewer**: edits the Markdown body, saves draft, submits for review.
- **Approver**: loads the submitted artifact, applies Layer 2, requests
  revision or approves.

Administrator reopen is covered by `test-integration.R` only (Q7 decision); the
live run does not require an administrator identity.

## Per-artifact steps

Recorded for each artifact the operator touches:

1. **Browse**: open the dashboard; `Refresh`; filter by module/state; locate the
   artifact.
2. **Load detail**: click the row; verify the YAML/evidence panels and the
   Markdown body load from the adapter (R4).
3. **Read**: review the read-only YAML front matter and the guideline evidence.
4. **Edit**: enrich or fix the Markdown body in the editor.
5. **Preview**: check the rendered preview (Layer-1 structural sanity, XSS-safe).
6. **Save draft**: save; verify persistence (companion body file + `saved`
   event on the review branch).
7. **Submit**: submit for review; verify state → `in-review`.
8. **(Approver) Review**: load the artifact; read the enriched Markdown; apply
   Layer 2 ratings per section.
9. **(Approver) Request revision OR Approve**.
10. **If revision**: reviewer revises, re-saves, re-submits; approver approves.
11. **Verify**: confirm the approved artifact in `extraction/40_approved/` on the
    review branch.

## Friction-log record

One entry per step per operator, in `friction-log.yaml`:

```yaml
session_id: RUN-2026-08-07-S01
reviewer_identity: reviewer@example.org   # or approver@example.org
role: reviewer                            # reviewer | approver
artifact_id: VAR-male
step: browse                               # browse|load|read|edit|preview|save|submit|review|request-revision|approve
time_on_task_seconds: 42
error_count: 0
friction_rating: 2                         # 1-5 (5 = worst friction)
severity: slow                             # block | slow | cosmetic
free_text: "Row highlight made the target easy to find."
timestamp: 2026-08-07T14:10:00Z
```

`friction_rating` is the operator's 1–5 rating of how much the step impeded
their work (1 = smooth, 5 = severe). `severity` is the operator's triage label.

## Decision rule

A friction item that **blocks a required path**, or is **rated ≥4 by ≥2
reviewers**, triggers a simplification change before scaling. Cosmetic items
are batched for a later iteration (recorded, not fixed now).

## Known-defect detection

- Reviewers note which seeded defects they identified during review (for
  human catch-rate scoring).
- The rubric's Layer 1 (automated structural) is also run against each draft at
  submission to measure the automated catch rate.
- The known-answer key (Step 9) is the scoring reference; it is kept separate
  from the drafts and used only for scoring in Step 12.

## Logs produced (Phase 4)

- `.cg-docs/calibration/live-run-2026-08-07.md` — run log
- `.cg-docs/calibration/content-error-log.yaml` — content errors
- `.cg-docs/calibration/defect-log.yaml` — app defects
- `.cg-docs/calibration/friction-log.yaml` — friction entries
