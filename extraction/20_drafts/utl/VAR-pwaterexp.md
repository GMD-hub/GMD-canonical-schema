---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-pwaterexp
canonical_label: "Total annual consumption of water supply"
variable_name: pwater_exp
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
  - name: "COICOP 4.4.1 Water supply"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Water, Sanitation and Hygiene (WASH), pwater_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`pwater_exp` is a continuous variable that refers to total annual household expenditures on water supply/piped water.

## Conceptual intent

It captures expenditure on water supply including associated costs such as hire and reading of meters and standing charges, following COICOP 4.4.1.

## Construction notes

Include associated expenditure (meter hire/reading, standing charges). Exclude expenditure on hot water (captured in `hwater_exp`) and bottled/container drinking water. Monetary variable at current prices in LCU, non-deflated, including the value of in-kind acquisitions.

## Consistency checks

- Should not include hot water expenditure (`hwater_exp`).
- Cross-check that `waterexp` equals `pwaterexp` plus `hwaterexp`.

## Escalation triggers

- Separate water supply and hot water expenditures cannot be distinguished in the survey.

## Common mistakes

- Including bottled water or hot water in water supply expenditure.
- Treating true 0 as missing, or adding skip patterns as 0.
- Not annualizing monthly/quarterly reported values.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
