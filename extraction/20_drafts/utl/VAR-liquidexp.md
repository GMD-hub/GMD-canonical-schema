---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-liquidexp
canonical_label: "Total annual consumption of all liquid fuels"
variable_name: liquid_exp
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: derived
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
  - VAR-gasolineexp
  - VAR-dieselexp
  - VAR-kerosenexp
  - VAR-othliqexp
derives_to:
  - VAR-utlexp
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 4.5.3 Liquid fuels"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Energy, liquid_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`liquid_exp` is a continuous aggregate variable of total annual household expenditures on all liquid fuels.

## Conceptual intent

It aggregates all liquid fuel expenditures, following COICOP 4.5.3.

## Construction notes

Derived as the sum of `gasolineexp`, `dieselexp`, `kerosenexp`, and `othliqexp` (`egen liquid_exp=rsum(gasoline_exp diesel_exp kerosene_exp othliq_exp)`). Surveys reporting only the aggregate may leave components missing.

## Consistency checks

- `liquidexp` should equal the sum of its four components when present.
- Cross-check against `utlexp` which includes `liquidexp`.

## Escalation triggers

- Directly reported aggregate differs from the sum of components.

## Common mistakes

- Double counting when liquid fuels are combined in the raw data.
- Treating missing components as 0.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
