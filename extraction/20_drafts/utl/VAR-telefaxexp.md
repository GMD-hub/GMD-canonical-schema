---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-telefaxexp
canonical_label: "Total annual consumption of other telefax services"
variable_name: telefax_exp
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
  - VAR-commexp
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 8.3.0"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Additional variables, telefax_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`telefax_exp` is a continuous variable that refers to total annual household expenditures on telegraphy, telex, and telefax services.

## Conceptual intent

It captures telefax/telegraphy expenditure, a component of telecommunication services following COICOP 8.3.0.

## Construction notes

Include telegraphy, telex, and telefax services, as well as radiotelephony, radiotelegraphy, and radio-telex services. Exclude equipment.

## Consistency checks

- Cross-check that `commexp` includes `telefaxexp`.
- Telefax usage may be combined with telephone or internet in the survey.

## Escalation triggers

- Including telefax equipment purchases.
- Telefax services are bundled with telephone or internet in the survey data.

## Common mistakes

- Treating telefax bundled with telephone as pure telephone expenditure.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
