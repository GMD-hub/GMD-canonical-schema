---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-gasexp
canonical_label: "Total annual consumption of network/natural and liquefied gas"
variable_name: gas_exp
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
  - VAR-ngasexp
  - VAR-lpgexp
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
  - name: "COICOP 4.5.2 Gas"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Energy, gas_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`gas_exp` is a continuous aggregate variable of total annual household expenditures on network/natural gas and liquefied gas (LPG).

## Conceptual intent

It aggregates both gas types into a single gas-expenditure indicator, following COICOP 4.5.2.

## Construction notes

Derived as the sum of `ngasexp` and `lpgexp` (`egen gas_exp=rsum(ngas_exp LPG_exp)`). Include associated expenditures (meter hire, storage containers, standing charges). Surveys reporting only the aggregate may leave the components missing.

## Consistency checks

- `gasexp` should equal `ngasexp` plus `lpgexp` when both are present.
- Cross-check against `cooksource`/`gas` access where available.

## Escalation triggers

- Directly reported aggregate differs from the sum of components.

## Common mistakes

- Double counting when both piped and bottled gas are recorded.
- Treating missing components (aggregate-only survey) as 0.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
