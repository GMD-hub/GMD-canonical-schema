---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-pipedtoprem
canonical_label: "Access to piped water on premises"
variable_name: piped_to_prem
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: binary

# --- Allowed output values ---
value_codes:
  - value: 0
    label: "No"
  - value: 1
    label: "Yes"
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), piped_to_prem"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`piped_to_prem` is a binary variable that specifies whether the household has access to piped water on its premises.

## Conceptual intent

It captures improved water access at the household plot, distinguishing on-premise piped supply from shared public water points.

## Construction notes

Within premises refers to a piped connection to an own tap (household or yard connection); outside premises refers to a public water point shared among houses.

## Consistency checks

- Only define this variable when `water_source` is 1 or 2 (water_source <=2); `piped_to_prem` equals 1 for `water_source` 1/2 and 0 for 3/14.
- Cross-check with `piped` and `water_source`.

## Escalation triggers

- The location of the piped access point (in or out of premise) is unstated.

## Common mistakes

- Coding a public standpipe as on-premise access.
- Creating this variable when `water_source` is missing or greater than 2.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
