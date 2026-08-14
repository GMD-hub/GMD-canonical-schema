---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-opendef
canonical_label: "Access to any sanitation facility"
variable_name: open_def
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
  - value: 0
    label: "Availability of any facility"
  - value: 1
    label: "No facility, or bush, or field"
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), open_def"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`open_def` is a categorical variable that specifies whether the household has access to any sanitation facility, flagging open defecation.

## Conceptual intent

It identifies households with no sanitation facility at all, a critical indicator of open defecation.

## Construction notes

Code 0 when any sanitation facility is available, and 1 when there is no facility or the household uses bush or field.

## Consistency checks

- `open_def` should equal 1 when `sanitation_source` is 13 (no facilities or bush or field).
- Cross-check with `sanitation_source`.

## Escalation triggers

- The survey does not distinguish sharing status or the absence of a facility clearly.

## Common mistakes

- Coding shared facilities as open defecation (they are not).
- Treating the presence of any facility, including shared, inconsistently.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
