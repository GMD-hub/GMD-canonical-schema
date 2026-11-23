---
# ================================================================
# MISSING VALUE DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
missing_id: MISS-NOT-HARMONIZED
missing_name: not_harmonized
canonical_label: "Variable had not been harmonized"
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the missing value ---
level: column        # column: describes the variable as a whole in a survey
scope: global        # global: applies to every variable; no variable lists it

# --- Representations ---
# What an output format writes for this value. A format that is not listed writes `missing_name`.
representations:
  stata: ".a"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: null
  extraction_method: manual
  extracted_on: "2026-11-17"
  human_reviewed: false
  reviewer: null
  notes: "Scaffold of a new record kind (missing value definitions), written on instruction of 2026-11-17.
          The label is the wording given in that instruction. The Stata code `.a` is the one the
          drafted VAR records already use in `missing_codes`. The section of the source document
          that defines the missing codes was not located in this repository (the source document
          is not vendored here), so `source_section` is null. Not from the extraction pipeline."
---

## Definition

The variable has not been harmonized for this survey. No harmonization of it was carried
out, so the value says nothing about whether the survey could support the variable.

## When it applies

- Harmonization of the variable was not attempted, or was not completed, for the survey.

## When it does not apply

- The survey's data was examined and does not meet the harmonization definition: use
  `MISS-CANNOT-HARMONIZE`.
- The survey does not hold the information: use `MISS-NOT-AVAILABLE`.
- A single observation has no value: a column missing describes the variable as a whole
  in a survey, never one observation.

## Open questions

- The drafted rules also use `.a` for single observations (RULE-SEX-001: numeric
  placeholder codes such as 98 and 99). Under this record that use ends: such an
  observation takes the cell missing that matches what the code means in the survey
  (`MISS-DECLINED-TO-ANSWER`, `MISS-DO-NOT-KNOW`, `MISS-MISSING-INPUT`). The rule is
  not yet changed.

## Change log

| Date       | Version | Change           | Authority            |
|------------|---------|------------------|----------------------|
| 2026-11-17 | 0.1     | Initial scaffold | GPID Team (proposed) |
