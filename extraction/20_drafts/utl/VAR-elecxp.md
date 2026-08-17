---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-elecxp
canonical_label: "Total annual consumption of electricity"
variable_name: elec_exp
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
  - VAR-utlexp
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 4.5.1 Electricity"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Energy, elec_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`elec_exp` is a continuous variable that refers to total annual household expenditures on electricity.

## Conceptual intent

It captures electricity expenditure including associated costs such as meter hire/reading and standing charges, following COICOP 4.5.1.

## Construction notes

Include electricity and associated expenditures (meter hire, reading, standing charges). Monetary variable at current prices in LCU, non-deflated, including in-kind value.

## Consistency checks

- Cross-check that `utlexp` includes `elecxp`.
- Electricity expenditure may be combined with gas or water in the survey.

## Escalation triggers

- Including equipment purchases in electricity expenditure.

## Common mistakes

- Not annualizing monthly/quarterly reported electricity values.
- Treating zero or skip patterns incorrectly.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
