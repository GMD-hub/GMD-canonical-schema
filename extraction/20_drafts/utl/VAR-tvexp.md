---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-tvexp
canonical_label: "Total annual consumption of television broadcasting services"
variable_name: tv_exp
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
derives_to:
  - VAR-tvintphexp
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 9.4.2"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Additional variables, tv_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`tv_exp` is a continuous variable that refers to total annual household expenditures on television broadcasting services.

## Conceptual intent

It captures TV broadcasting expenditure, license fees, and subscriptions, following COICOP 9.4.2 (Cultural services).

## Construction notes

Include television broadcasting services, license fees for television equipment, and subscriptions to television networks. Exclude spending on theatres, museums, and historic monuments.

## Consistency checks

- Cross-check that `tvintphexp` includes `tvexp`.
- Cross-check exclusion from `utlexp`.

## Escalation triggers

- TV services may be bundled with internet or telephone.

## Common mistakes

- Including spending on other cultural services (theatres, museums).
- Bundling TV with internet/phone without separation.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
