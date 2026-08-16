---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-utlexp
canonical_label: "Total annual consumption of all utilities excluding telecom and other housing"
variable_name: utl_exp
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
  - VAR-waterexp
  - VAR-wasteexp
  - VAR-elecxp
  - VAR-gasexp
  - VAR-liquidexp
  - VAR-solidexp
  - VAR-centralexp
  - VAR-othfuelexp
derives_to: []
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  []
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Energy, utl_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`utl_exp` is a continuous aggregate variable of total annual household expenditure on all utilities excluding telecom and other housing expenses.

## Conceptual intent

It aggregates core utility expenditures into a single indicator at current-year prices, the main utilities affordability aggregate.

## Construction notes

Derived as the sum of `waterexp`, `wasteexp`, `elecxp`, `gasexp`, `liquidexp`, `solidexp`, `centralexp`, and `othfuelexp` (`egen utl_exp=rsum(water_exp waste_exp elec_exp gas_exp liquid_exp solid_exp central_exp othfuel_exp)`). Excludes `othhousingexp`, `transfuelexp`, `commexp`, and `tvexp`.

## Consistency checks

- `utlexp` should equal the sum of its listed components when present.
- Verify that telecom (`commexp`) and other housing (`othhousingexp`) are excluded.

## Escalation triggers

- A component uses a different reference period or is missing.

## Common mistakes

- Including telecom, transport fuel, television, or other housing in the aggregate.
- Double counting components that overlap (e.g. hot water in both water and heating).
- Treating missing components as 0 instead of leaving them missing.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
