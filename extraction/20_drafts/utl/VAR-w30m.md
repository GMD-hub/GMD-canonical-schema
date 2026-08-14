---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-w30m
canonical_label: "Access to water within 30 minutes"
variable_name: w_30m
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: binary

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Time to water source less than or equal to 30 mins"
  - value: 0
    label: "Time to water source more than 30 mins"
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), w_30m"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`w_30m` is a binary variable that specifies whether the household has access to water within 30 minutes, including round-trip and waiting time.

## Conceptual intent

Used with `imp_wat_rec` to identify whether the improved water source is available within 30 minutes, a key safely-managed service criterion.

## Construction notes

Include round-trip collection time and waiting time in case of queues. Code 1 if the time to the water source is 30 minutes or less, 0 if more than 30 minutes.

## Consistency checks

- Cross-check the reported collection time is consistent with the water source type.
- Verify against `imp_wat_rec` when constructing water service level indicators.

## Escalation triggers

- Collection time was not collected in the survey.

## Common mistakes

- Using round-trip time but excluding waiting time, understating access.
- Treating missing collection time as 0 (more than 30 minutes).

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
