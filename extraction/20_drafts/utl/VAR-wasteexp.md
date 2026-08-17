---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-wasteexp
canonical_label: "Total annual consumption of garbage and sewage collection"
variable_name: waste_exp
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

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
  - VAR-garbageexp
  - VAR-sewageexp
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
  - name: "COICOP 4.4.2/4.4.3"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Water, Sanitation and Hygiene (WASH), waste_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`waste_exp` is a continuous aggregate variable of total annual household expenditure on garbage and sewage collection.

## Conceptual intent

It aggregates refuse and sewage collection into a single waste-expenditure indicator, following COICOP 4.4.2 and 4.4.3.

## Construction notes

Derived as the sum of `garbageexp` and `sewageexp` (`egen waste_exp=rsum(garbage_exp sewage_exp)`). Surveys reporting only the aggregate may leave the components missing.

## Consistency checks

- `wasteexp` should equal `garbageexp` plus `sewageexp` when both are present.
- Cross-check against `utlexp` which includes `wasteexp`.

## Escalation triggers

- Directly reported aggregate differs from the sum of components.

## Common mistakes

- Double counting when garbage and sewage are combined.
- Treating missing components (aggregate-only survey) as 0.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
