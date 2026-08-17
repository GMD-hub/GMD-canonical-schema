---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-dwelsvcexp
canonical_label: "Total annual consumption of services for the maintenance and repair of the dwelling"
variable_name: dwelsvc_exp
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
  - VAR-othhousingexp
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 4.3.2"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Additional variables, dwelsvc_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`dwelsvc_exp` is a continuous variable that refers to total annual household expenditures on services for minor maintenance and repair of the dwelling.

## Conceptual intent

It captures service expenditure for minor maintenance and repair, following COICOP 4.3.2.

## Construction notes

Include services of plumbers, electricians, carpenters, glaziers, painters, and decorators, covering both labor and materials. Exclude separate material purchases by the household, services for major maintenance/repair, and extension/conversion.

## Consistency checks

- Cross-check that `othhousingexp` equals `dwelmatexp` plus `dwelsvcexp`.
- Materials and services may be combined in the survey.

## Escalation triggers

- Including separately purchased materials or major repair services.

## Common mistakes

- Double counting when combined with `dwelmatexp`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
