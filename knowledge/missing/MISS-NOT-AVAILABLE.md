---
# ================================================================
# MISSING VALUE DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
missing_id: MISS-NOT-AVAILABLE
missing_name: not_available
canonical_label: "Variable was not harmonized because information is not available"
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the missing value ---
level: column        # column: describes the variable as a whole in a survey
scope: global        # global: applies to every variable; no variable lists it

# --- Representations ---
# What an output format writes for this value. A format that is not listed writes `missing_name`.
representations:
  stata: ".c"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: null
  extraction_method: manual
  extracted_on: "2026-11-17"
  human_reviewed: false
  reviewer: null
  notes: "Scaffold of a new record kind (missing value definitions), written on instruction of 2026-11-17.
          The label is the wording given in that instruction. The Stata code `.c` is the one the
          drafted VAR records already use in `missing_codes`. The section of the source document
          that defines the missing codes was not located in this repository (the source document
          is not vendored here), so `source_section` is null. Not from the extraction pipeline."
---

## Definition

The survey does not hold the information the variable needs, so the variable was not
harmonized.

## When it applies

- The survey did not collect the information, or the information is not in the data that
  was delivered.

## When it does not apply

- The information was collected but does not meet the harmonization definition: use
  `MISS-CANNOT-HARMONIZE`.
- An observation is outside the variable's universe: use `MISS-OUTSIDE-UNIVERSE`.
- An observation's input holds no value: use `MISS-MISSING-INPUT`.

## Open questions

- The records used `.c` for single observations outside the universe. Those observations
  take `MISS-OUTSIDE-UNIVERSE`: the variable drafts are changed; RULE-EDU-001 and the
  minimum-age parameters under `knowledge/` are not yet.
- The variable drafts once labelled `.c` with two other meanings (subnational
  classification unchanged since the previous survey; not specified by the
  questionnaire or manual). Those entries were removed with the other column-level
  entries; whether either needs a value of its own is undecided.

## Change log

| Date       | Version | Change           | Authority            |
|------------|---------|------------------|----------------------|
| 2026-11-17 | 0.1     | Initial scaffold | GPID Team (proposed) |
