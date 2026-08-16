---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-childyr
canonical_label: "Child age in years for those under 5"
variable_name: childyr
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: numeric

# --- Allowed output values ---
value_codes: null
allowed_range:
  min: 0
  max: 5

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Not collected in this survey"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites:
  - variable_id: VAR-age
    condition: "Applied only to children aged under 5 years (less than 60 months)."

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "age in years"
    - "child age"
    - "age of child under 5"
  typical_section_names:
    - "Child health"
    - "Anthropometrics"
    - "Child roster"
    - "Demographics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, childyr"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "childyr and childmth were included in the GMD harmonization for the first
          time in the December 2023 revision. If there is no information available,
          they must nonetheless be created. childyr is used to interpret
          Anthropometrics data for children aged under 5."
---

## Definition

`childyr` records the age in complete years of children aged under 5 years
(less than 60 months). It is used to interpret Anthropometrics data.

## Conceptual intent

Age expressed in complete years is too coarse to interpret anthropometric
indicators for young children. `childyr` provides a finer age reference in
completed years so that growth and nutrition data for the under-five population
can be correctly interpreted alongside `childmth`.

## Construction notes

For children under 5 years of age (aged less than 60 months), record the age in
complete years. Confirm the value is consistent with the age in completed years
reported in the `age` variable.

The variable must be constructed even if information is not directly available;
if a value cannot be derived, record the appropriate missing code and document
why.

## Consistency checks

- `childyr` must be consistent with `age`: for children under 5, age in
  completed years should match.
- `childyr` must be consistent with `childmth`: the completed-year value implied
  by the completed-month value must match (year = floor(months / 12)).
- `childyr` should only be non-missing for individuals under 5 years of age.

## Escalation triggers

- Systematic inconsistency between `childyr`, `childmth`, and `age` for the
  under-five population.
- No source information exists to construct `childyr` and no reasonable basis
  for imputation is documented.

## Common mistakes

- Recording `childyr` for children 5 years or older.
- Failing to create the variable at all when the survey lacks it, contrary to
  the December 2023 revision requirement.
- Leaving `childyr` inconsistent with `childmth` or `age`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
