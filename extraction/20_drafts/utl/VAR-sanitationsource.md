---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-sanitationsource
canonical_label: "Main toilet facility"
variable_name: sanitation_source
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: categorical

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "A flush toilet"
  - value: 2
    label: "A piped sewer system"
  - value: 3
    label: "A septic tank"
  - value: 4
    label: "Pit latrine"
  - value: 5
    label: "Ventilated improved pit latrine (VIP)"
  - value: 6
    label: "Pit latrine with slab"
  - value: 7
    label: "Composting toilet"
  - value: 8
    label: "Special case"
  - value: 9
    label: "A flush/pour flush to elsewhere"
  - value: 10
    label: "A pit latrine without slab"
  - value: 11
    label: "Bucket"
  - value: 12
    label: "Hanging toilet or hanging latrine"
  - value: 13
    label: "No facilities or bush or field"
  - value: 14
    label: "Other"
allowed_range: null
# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Information not available because the item was not collected in this survey"
  - code: ".o"
    label: "Other value not covered by harmonized codes"
# --- Derivation graph ---
derived_from:
  []
derives_to: []
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  []
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), sanitation_source"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`sanitation_source` is a categorical variable that specifies the main source/facility of sanitation for the household, harmonized into fourteen standardized categories.

## Conceptual intent

It is the core WASH sanitation access indicator, distinguishing improved from unimproved facilities and feeding `sewer`, `open_def`, and `imp_san_rec`.

## Construction notes

Code from `sanitation_original` unless otherwise justified, referring to the survey questionnaire for the best match. If several toilet types are used, record only the main source. Apply the detailed definitions (e.g. flush toilet excludes pour-flush and flush to elsewhere).

## Consistency checks

- `sewer` equals 1 when the facility is a flush/pour flush to a piped sewer system.
- `imp_san_rec` equals 1 for improved facilities (flush/pour-flush to sewer, septic tank, or pit latrine; VIP; pit latrine with slab; composting toilet).

## Escalation triggers

- The survey uses a toilet category that does not map cleanly to any standardized code.
- A toilet is shared with other households, affecting improved-status determination.

## Common mistakes

- Coding a pour-flush toilet as a flush toilet.
- Treating bucket, hanging toilet, or no facility as improved.
- Not consulting the questionnaire and guessing the correspondence.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
