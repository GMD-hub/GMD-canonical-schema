---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-gasolineexp
canonical_label: "Total annual consumption of gasoline"
variable_name: gasoline_exp
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

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
  - VAR-liquidexp
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
  source_section: "Utilities (UTL), Affordability, Essential variables - Energy, gasoline_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`gasoline_exp` is a continuous variable that refers to total annual household expenditure on gasoline.

## Conceptual intent

It captures gasoline expenditure, mostly used in vehicles and motorcycles, a component of liquid fuels expenditure.

## Construction notes

Record total annual household expenditure on gasoline.

## Consistency checks

- Cross-check that `liquidexp` includes `gasolineexp`.
- Gasoline and other liquid fuels may be combined in the survey.

## Escalation triggers

- Including lubricants (excluded per COICOP 7.2.2).

## Common mistakes

- Conflating gasoline with diesel expenditure.
- Including lubricants in gasoline expenditure (excluded per COICOP 7.2.2).

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
