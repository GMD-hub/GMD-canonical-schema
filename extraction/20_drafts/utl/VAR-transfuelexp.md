---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-transfuelexp
canonical_label: "Total annual consumption of fuels for personal transportation"
variable_name: transfuel_exp
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
  - name: "COICOP 7.2.2"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Additional variables, transfuel_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`transfuel_exp` is a continuous variable that refers to total annual household expenditures on fuels for personal transportation.

## Conceptual intent

It captures transport fuels expenditure, following COICOP 7.2.2 (Fuels and lubricants for personal transport equipment), excluding lubricants.

## Construction notes

Record total annual household expenditure on fuels for personal transportation. Exclude lubricants, which are in COICOP 7.2.2 but excluded from this GMD indicator.

## Consistency checks

- Cross-check exclusion from `utlexp`.
- Fuels and lubricants may be combined in the survey.

## Escalation triggers

- Including lubricants in transport fuel expenditure.

## Common mistakes

- Double counting when fuels are combined across categories.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
