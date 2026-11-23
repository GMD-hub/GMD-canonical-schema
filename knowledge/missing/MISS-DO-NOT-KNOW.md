---
# ================================================================
# MISSING VALUE DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
missing_id: MISS-DO-NOT-KNOW
missing_name: do_not_know
canonical_label: "Do not know"
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the missing value ---
level: cell          # cell: describes one observation of a harmonized variable
scope: global        # global: applies to every variable; no variable lists it

# --- Representations ---
# What an output format writes for this value. A format that is not listed writes `missing_name`.
representations:
  stata: ".k"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: null
  extraction_method: manual
  extracted_on: "2026-11-17"
  human_reviewed: false
  reviewer: null
  notes: "Scaffold of a new record kind (missing value definitions), written on instruction of 2026-11-17.
          This value and its Stata code `.k` are NEW: they are proposed in that instruction and
          are not in the source document, which is why `source_section` is null. The label is the
          wording given in the instruction. Not from the extraction pipeline."
---

## Definition

The question was put to the respondent, and the survey records that the respondent did
not know the answer.

## When it applies

- The survey records `do not know` as such, with a code or a marker of its own.

## When it does not apply

- The respondent declined to answer: use `MISS-DECLINED-TO-ANSWER`.
- The survey does not record why the value is missing, or records refusal and
  `do not know` under one code that cannot be told apart: use `MISS-MISSING-INPUT`.
- The variable does not apply to the observation: use `MISS-OUTSIDE-UNIVERSE`.

## Change log

| Date       | Version | Change           | Authority            |
|------------|---------|------------------|----------------------|
| 2026-11-17 | 0.1     | Initial scaffold | GPID Team (proposed) |
