---
# ================================================================
# MISSING VALUE DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
missing_id: MISS-MISSING-INPUT
missing_name: missing_input
canonical_label: "Input variable was missing"
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the missing value ---
level: cell          # cell: describes one observation of a harmonized variable
scope: global        # global: applies to every variable; no variable lists it

# --- Representations ---
# What an output format writes for this value. A format that is not listed writes `missing_name`.
representations:
  stata: ".i"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: null
  extraction_method: manual
  extracted_on: "2026-11-17"
  human_reviewed: false
  reviewer: null
  notes: "Scaffold of a new record kind (missing value definitions), written on instruction of 2026-11-17.
          This value and its Stata code `.i` are NEW: they are proposed in that instruction and
          are not in the source document, which is why `source_section` is null. The label is the
          wording given in the instruction. Not from the extraction pipeline."
---

## Definition

The observation is inside the variable's universe, and the survey input the harmonized
value is built from holds no value for it.

## When it applies

- The source value is missing for the observation.
- A derived variable lacks one of the inputs it needs for the observation.
- The survey marks the value as a non-answer and does not say which kind (a refusal,
  `do not know`, another reason), or its kinds cannot be told apart.

## When it does not apply

- The survey records that the respondent declined to answer or did not know: use
  `MISS-DECLINED-TO-ANSWER` or `MISS-DO-NOT-KNOW`.
- The survey's value was censored in the delivered data: use `MISS-CENSORED`.
- The variable does not apply to the observation: use `MISS-OUTSIDE-UNIVERSE`.
- The survey holds an answer that no harmonized category covers: use
  `MISS-OTHER-CATEGORY`.
- The whole variable is missing from the survey: that is a column missing.

## Open questions

- Which missing value an input takes when it holds a value that is not valid (a code
  outside the survey's own declared codes) is undecided.

## Change log

| Date       | Version | Change           | Authority            |
|------------|---------|------------------|----------------------|
| 2026-11-17 | 0.1     | Initial scaffold | GPID Team (proposed) |
