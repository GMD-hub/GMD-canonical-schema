---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-welfare
canonical_label: "Household welfare aggregate"
variable_name: welfare
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.2"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: derived
data_type: numeric_continuous

# --- Allowed output values ---
value_codes: null
allowed_range:
  min: 0
  max: 1000000000

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because required inputs are incomplete"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions:
  - EXC-PER-001
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "welfare"
    - "consumption"
    - "income aggregate"
    - "household total"
  typical_section_names:
    - "Welfare"
    - "Consumption"
    - "Income"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Welfare aggregates"
  extraction_method: manual
  extracted_on: "2026-09-06"
  human_reviewed: false
  reviewer: null
  notes: "Added to support country exception reference EXC-PER-001."
---

## Definition

`welfare` is the harmonized household-level welfare aggregate used in poverty
and distributional analysis.

## Conceptual intent

This variable represents the total welfare measure selected for analysis
(consumption- or income-based, depending on survey design and harmonization
rules).

## Construction notes

Construction is survey-specific and follows the approved harmonization
pipeline. Country exceptions may apply additional transformations when
explicitly documented.

## Consistency checks

- Welfare values must be non-negative for all non-missing records.
- Unit of analysis must be household.
- Any country exception affecting welfare must be explicitly referenced.

## Escalation triggers

- Required welfare components are missing from source data.
- Country exception logic conflicts with approved harmonization policy.
- Survey documentation does not identify the welfare concept used.

## Common mistakes

- Mixing person-level and household-level welfare units.
- Applying country exception factors without a valid condition match.
- Treating nominal and real welfare as interchangeable without adjustment.

## Change log

| Date       | Version | Change                                   | Authority |
|------------|---------|------------------------------------------|-----------|
| 2026-09-06 | 0.2     | Add canonical variable for welfare usage | GPID Team |
