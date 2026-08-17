---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-hwaterexp
canonical_label: "Total annual household consumption of hot water supply"
variable_name: hwater_exp
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
  - VAR-heatingexp
  - VAR-waterexp
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 4.5.5 Heat energy"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Water, Sanitation and Hygiene (WASH), hwater_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`hwater_exp` is a continuous variable that refers to total annual household expenditure on hot water supply.

## Conceptual intent

It captures expenditure on hot water supply separately from cold water, following COICOP which categorizes hot water under heat energy (4.5.5).

## Construction notes

Record total annual household expenditure on hot water supply. This may be combined with cold water or with central heating in the raw data; separate carefully.

## Consistency checks

- Cross-check that `waterexp` equals `pwaterexp` plus `hwaterexp`.
- Cross-check that `heatingexp` includes hot water where applicable.

## Escalation triggers

- Hot water is combined with central heating or with cold water in the survey.

## Common mistakes

- Double counting hot water in both water and heating aggregates.
- Treating combined values as purely cold-water expenditure.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
