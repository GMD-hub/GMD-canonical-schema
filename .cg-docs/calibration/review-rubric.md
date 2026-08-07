# Two-Layer Review Rubric (draft)

- **Plan**: `.cg-docs/plans/2026-08-07-calibrate-human-review.md` (Phase 2, Step 7 → finalized Step 14)
- **Requirements**: R15
- **Status**: draft (finalized from live-run evidence in Step 14)
- **Date**: 2026-08-07

This rubric defines what makes a CVS draft promotable from
`extraction/30_review/` to `extraction/40_approved/`. It has two layers:

- **Layer 1 — automated structural gate**: machine-checkable, blocks
  submission when it fails.
- **Layer 2 — human content-quality gate**: applied by the approver at review
  time, blocks approval when it fails.

## Layer 1 — Automated structural gate (blocks submission)

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
4. **No section is a stub**: each section has non-trivial content. The precise
   threshold is set from calibration data in Step 14; the provisional rule is
   *more than one sentence and more than 50 characters* of real content in each
   required section.

Layer 1 is the "automated structural" gate referenced by the live-operator
protocol and is measured separately (automated catch rate) in Step 12.

## Layer 2 — Human content-quality gate (blocks approval)

The approver rates each required section on the 7-section template:

| Section | Evaluation focus |
|---|---|
| Definition | Matches the guideline source evidence panel; accurate and unambiguous. |
| Construction notes | All derivation paths documented (e.g. educat4's three paths: derive from educat7, from educat5, direct mapping), with the ordering/priority stated. |
| Consistency checks | Checks are specific and actionable, not vague ("verify values"). |
| Escalation triggers | Present and relevant to the variable's risk profile; actionable conditions. |
| Common mistakes | Real, instructive, non-redundant; reflect actual harmonization pitfalls. |

Each section is rated **`pass` / `revise` / `fail`**:

- `pass` — the section is accurate, complete, and actionable.
- `revise` — the section is usable but needs notes/improvements; revisions are
  recorded per-section for the reviewer.
- `fail` — the section is wrong, missing, or a stub; revision is required
  before approval.

The approver records the per-section rating in the review record's event note
or the calibration run log.

## Promotion gate (30 → 40)

An artifact is promotable to `extraction/40_approved/` only when:

1. **Layer 1 passes** (automated structural), AND
2. **Layer 2 is all-`pass` or `revise`-with-notes** (no `fail` on any section),
   AND
3. **No open `block`/`major` extraction errors** exist on the artifact in the
   content-error log.

The agent-review dimensions are reserved as future gates (not active in this
calibration).

## Section-template reference (for Step 9 materialization)

The 7 required sections mirror the real `knowledge/variables/dem/` artifacts
(`VAR-male`, `VAR-educat4`, `VAR-educy`). Fixtures in Step 9 must carry all 7
sections with non-stub content matching this template.
