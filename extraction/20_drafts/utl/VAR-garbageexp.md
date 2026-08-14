---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-garbageexp
canonical_label: "Total annual consumption of garbage collection"
variable_name: garbage_exp
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: numeric_continuous

# --- Allowed output values ---
value_codes:
  null
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
  - name: "COICOP 4.4.2 Refuse collection"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Water, Sanitation and Hygiene (WASH), garbage_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`garbage_exp` is a continuous variable that refers to total annual household expenditures on collection and disposal of garbage or refuse.

## Conceptual intent

It captures refuse collection and disposal expenditure, following COICOP 4.4.2.

## Construction notes

Record total annual household expenditure on collection and disposal of garbage or refuse.

## Consistency checks

- Cross-check that `wasteexp` equals `garbageexp` plus `sewageexp`.
- Cross-check against `waste` disposal type where available.

## Escalation triggers

- Garbage and sewage expenditure cannot be separated in the survey.

## Common mistakes

- Including sewage/waterwater disposal in garbage expenditure.
- Treating zero or skip patterns incorrectly as missing.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
