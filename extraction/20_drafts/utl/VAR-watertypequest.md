---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-watertypequest
canonical_label: "Type of water questions used in the survey"
variable_name: watertype_quest
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: categorical

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Drinking water"
  - value: 2
    label: "General water"
  - value: 3
    label: "Both"
  - value: 4
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), watertype_quest"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`watertype_quest` is a categorical variable that records the type of water question(s) asked in the survey about the type of water source used by the household.

## Conceptual intent

The type of water question determines which water-related variables can be harmonized and how subsequent water access variables (e.g. `water_source`) are interpreted.

## Construction notes

Harmonize into four categories: drinking water only (1), general water only (2), both (3), or other (4). When the type of water question is unknown, code as 4 (Other). Subsequent water questions depend on this response.

## Consistency checks

- Every household should receive a valid category or an extended missing code when the questionnaire used no water-type question.
- Cross-check that `water_source` and related water variables are consistent with the recorded type of water question.

## Escalation triggers

- The questionnaire does not state clearly which type of water question was asked.
- More than 5 percent of households are coded 4 (Other) without documentation.

## Common mistakes

- Coding unknown water question type as 3 (Both) instead of 4 (Other).
- Assuming the water question refers to drinking water when the survey only asked about general water.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
