---
# ================================================================
# MISSING VALUE DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
missing_id: MISS-CANNOT-HARMONIZE
missing_name: cannot_harmonize
canonical_label: "Variable cannot be harmonized because data does not meet harmonization definition"
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the missing value ---
level: column        # column: describes the variable as a whole in a survey
scope: global        # global: applies to every variable; no variable lists it

# --- Representations ---
# What an output format writes for this value. A format that is not listed writes `missing_name`.
representations:
  stata: ".b"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: null
  extraction_method: manual
  extracted_on: "2026-11-17"
  human_reviewed: false
  reviewer: null
  notes: "Scaffold of a new record kind (missing value definitions), written on instruction of 2026-11-17.
          The label is the wording given in that instruction, completed with the word `definition` (the instruction's wording ended at
          `harmonization`; the drafted VAR records say `harmonization definition`). The Stata code `.b` is the one the
          drafted VAR records already use in `missing_codes`. The section of the source document
          that defines the missing codes was not located in this repository (the source document
          is not vendored here), so `source_section` is null. Not from the extraction pipeline."
---

## Definition

The survey holds data related to the variable, but that data does not meet the
harmonization definition, so the variable cannot be produced from it.

## When it applies

- A candidate source exists and was examined, and it does not meet the definition. For
  example, the definition asks for a graded response and the survey asks a yes/no
  question.

## When it does not apply

- No candidate source exists in the survey: use `MISS-NOT-AVAILABLE`.
- The variable was not attempted: use `MISS-NOT-HARMONIZED`.
- A single observation has no value: a column missing describes the variable as a whole
  in a survey, never one observation.

## Open questions

- The drafted rules used `.b` for single observations. RULE-EDU-002's residual
  categories and RULE-EDU-003's `educy` now take cell-level values.

## Change log

| Date       | Version | Change           | Authority            |
|------------|---------|------------------|----------------------|
| 2026-11-17 | 0.1     | Initial scaffold | GPID Team (proposed) |
