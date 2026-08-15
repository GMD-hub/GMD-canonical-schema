# Two-Layer Review Rubric (finalized)

- **Plan**: `.cg-docs/plans/2026-08-07-calibrate-human-review.md` (Phase 2, Step 7 -> finalized Step 14)
- **Requirements**: R15
- **Status**: finalized (evidence-backed from solo calibration run 2026-08-14)
- **Date**: 2026-08-14

This rubric defines what makes a CVS draft promotable from
`extraction/30_review/` to `extraction/40_approved/`. It has two layers:

- **Layer 1 -- automated structural gate**: machine-checkable, blocks
  submission when it fails.
- **Layer 2 -- human content-quality gate**: applied by the approver at review
  time, blocks approval when it fails.

## Layer 1 -- Automated structural gate (blocks submission)

A draft passes Layer 1 only when **all** of the following hold:

1. **YAML front matter parses** as valid YAML and validates against the CVS
   variable-spec Pydantic model (`schema/variable.py`).
2. **Front matter is byte-unchanged** from the loaded draft (C1). Any
   structural alteration is rejected.
3. **All required Markdown sections are present**:
   - `## Definition`
   - `## Conceptual intent`
   - `## Construction notes`
   - `## Consistency checks`
   - `## Escalation triggers`
   - `## Common mistakes`
   - `## Change log`
4. **No section is a stub**: each section has non-trivial content. The
   threshold is *more than one sentence and more than 50 characters* of real
   content in each required section. This threshold was validated during the
   solo calibration run (2026-08-14) and is appropriate for the current
   sample size (N=6 artifacts).

## Layer 2 -- Human content-quality gate (blocks approval)

The approver rates each required section on the 7-section template:

| Section | Evaluation focus |
|---|---|
| Definition | Matches the guideline source evidence panel; accurate and unambiguous. |
| Conceptual intent | Clear statement of what the variable represents and why it matters. |
| Construction notes | All derivation paths documented (e.g. educat4's three paths: derive from educat7, from educat5, direct mapping), with the ordering/priority stated. |
| Consistency checks | Checks are specific and actionable, not vague ("verify values"). |
| Escalation triggers | Present and relevant to the variable's risk profile; actionable conditions. |
| Common mistakes | Real, instructive, non-redundant; reflect actual harmonization pitfalls. |
| Change log | Records meaningful changes with dates and reasons. |

Each section is rated **`pass` / `revise` / `fail`**:

- `pass` -- the section is accurate, complete, and actionable.
- `revise` -- the section is usable but needs notes/improvements; revisions are
  recorded per-section for the reviewer.
- `fail` -- the section is wrong, missing, or a stub; revision is required
  before approval.

The approver records the per-section rating in the review record's event note
or the calibration run log.

## Promotion gate (30 -> 40)

An artifact is promotable to `extraction/40_approved/` only when:

1. **Layer 1 passes** (automated structural), AND
2. **Layer 2 is all-`pass` or `revise`-with-notes** (no `fail` on any section),
   AND
3. **No open `block`/`major` extraction errors** exist on the artifact in the
   content-error log.

The agent-review dimensions are reserved as future gates (not active until
the independent-agent-review milestone is complete).

## Calibration evidence

This rubric was validated during the solo calibration run (2026-08-14):
- 6 drafts processed through the full state machine
- All Layer 1 structural checks passed for the 3 real artifacts
- The 3 fixtures with seeded defects were identified through the workflow
- No friction or interface issues detected
- The 50-char/1-sentence stub threshold is appropriate for the current scale

## Known limitations

- **Sample size**: N=6 artifacts, 1 operator (solo run). The rubric should be
  re-calibrated when a larger sample is reviewed by domain-expert reviewers.
- **No agent review**: Agent-review gates (source-grounding, schema-compliance,
  rules-caveats, consistency-derivation) are not yet active. These will be
  added when the independent-agent-review milestone is complete.
- **Domain expertise**: The solo operator is not a harmonizer; Layer 2 ratings
  were not scored. A second calibration with real reviewers on 5-10 extracted
  variables is recommended before scaling to all variables.

## When to re-calibrate

- After the independent-agent-review milestone adds agent-review gates
- After a sample of 5-10 variables is reviewed by domain-expert reviewers
- When the sample grows beyond the current calibration scale (N > 20)
