---
# ================================================================
# MISSING VALUE DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
missing_id: MISS-OTHER-CATEGORY
missing_name: other_category
canonical_label: "Other category not covered in the harmonized categories"
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the missing value ---
level: cell          # cell: describes one observation of a harmonized variable
scope: variable      # variable: applies only where a variable lists it in missing_codes

# --- Representations ---
# What an output format writes for this value. A format that is not listed writes `missing_name`.
representations:
  stata: ".o"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: null
  extraction_method: manual
  extracted_on: "2026-11-17"
  human_reviewed: false
  reviewer: null
  notes: "Scaffold of a new record kind (missing value definitions), written on instruction of 2026-11-17.
          The label is the wording given in that instruction. The Stata code `.o` is the one the
          drafted VAR records already use in `missing_codes`. The section of the source document
          that defines the missing codes was not located in this repository (the source document
          is not vendored here), so `source_section` is null. Not from the extraction pipeline."
---

## Definition

The observation has a valid answer in the survey, and none of the variable's harmonized
categories covers it.

## When it applies

- The survey's category is a real answer with no counterpart among the harmonized
  categories.
- The survey holds a value that has no entry in the reference the variable is built
  from. For example, a survey area with no entry in the geography crosswalk
  (`geo_code`).

## When it does not apply

- The respondent declined to answer: use `MISS-DECLINED-TO-ANSWER`.
- The respondent did not know the answer: use `MISS-DO-NOT-KNOW`.
- The observation has no answer in the survey: use `MISS-MISSING-INPUT`.
- The variable does not apply to the observation: use `MISS-OUTSIDE-UNIVERSE`.

## Open questions

- Whether a survey category that cannot be placed because it spans several harmonized
  categories belongs here is undecided.

## Change log

| Date       | Version | Change           | Authority            |
|------------|---------|------------------|----------------------|
| 2026-11-17 | 0.1     | Initial scaffold | GPID Team (proposed) |
