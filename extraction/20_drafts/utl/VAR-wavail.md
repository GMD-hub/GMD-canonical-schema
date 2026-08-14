---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-wavail
canonical_label: "Water is available when needed"
variable_name: w_avail
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
    label: "Water is available continuously, reliable source"
  - value: 0
    label: "Water source is unreliable"
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), w_avail"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`w_avail` is a binary variable that specifies whether water is available when needed.

## Conceptual intent

Used with `imp_wat_rec` to identify where the improved water source is available reliably 24/7, a safely-managed water service criterion.

## Construction notes

Code 1 if the water source is available continuously and considered reliable, 0 if the source is unreliable.

## Consistency checks

- Cross-check the reliability response is consistent with the water source type.
- Verify against `imp_wat_rec` when constructing water service level indicators.

## Escalation triggers

- Water availability/continuity was not collected in the survey.

## Common mistakes

- Confusing availability with physical collection time captured in `w_30m`.
- Marking a source reliable when the survey indicates frequent interruptions.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
