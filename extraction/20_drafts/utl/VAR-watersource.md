---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-watersource
canonical_label: "Main source of drinking water"
variable_name: water_source
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
    label: "Piped water into dwelling"
  - value: 2
    label: "Piped water to yard/plot"
  - value: 3
    label: "Public tap or standpipe"
  - value: 4
    label: "Tubewell or borehole"
  - value: 5
    label: "Protected dug well"
  - value: 6
    label: "Protected spring"
  - value: 7
    label: "Bottled water"
  - value: 8
    label: "Rainwater"
  - value: 9
    label: "Unprotected spring"
  - value: 10
    label: "Unprotected dug well"
  - value: 11
    label: "Cart with small tank/drum"
  - value: 12
    label: "Tanker-truck"
  - value: 13
    label: "Surface water"
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), water_source"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`water_source` is a categorical variable that indicates the main source of drinking water for the household, harmonized into fourteen standardized categories.

## Conceptual intent

It is the core WASH water access indicator, distinguishing improved from unimproved sources and feeding the `piped`, `piped_to_prem`, and `imp_wat_rec` variables.

## Construction notes

Code from `water_original` unless otherwise justified, referring to the survey questionnaire for the best match. If several water types are used, record only the main source. If the source differs between wet and dry season, use the dry-season source. Apply the detailed category definitions (e.g. piped into dwelling means a service pipe with in-house plumbing).

## Consistency checks

- `piped` equals 1 if `water_source` is 1, 2, or 3.
- `piped_to_prem` equals 1 only if `water_source` is 1 or 2.
- `imp_wat_rec` equals 1 for codes 1 through 8.

## Escalation triggers

- The survey uses a water category that does not map cleanly to any standardized code.
- Water source differs by season and the dry-season source cannot be determined.

## Common mistakes

- Coding bottled water (7) as if it were a protected source.
- Treating a borehole with a reticulated piped system as tubewell instead of piped water.
- Not consulting the questionnaire and guessing the correspondence.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
