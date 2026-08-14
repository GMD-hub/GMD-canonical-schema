---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-gauladm2code
canonical_label: "GAUL code - second administrative level"
variable_name: gaul_adm2_code
module_id: MOD-GEO
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: integer

# --- Allowed output values ---
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "gaul"
    - "adm2"
    - "administrative code"
    - "shapefile code"
    - "subnational code"
  typical_section_names:
    - "Geography"
    - "Identification"
    - "Administrative boundaries"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), Mapping and Description of Variables, gaul_adm2_code"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`gaul_adm2_code` is a numeric, country-specific variable that holds the Global
Administrative Unit Layers (GAUL) code for the second administrative level in
which the household is located. It is taken from the GAUL database where the
geographic area can be identified in the survey based on the location or area
name.

## Conceptual intent

`gaul_adm2_code` provides a standardized, globally comparable code for the
second-level administrative division, supporting cross-survey comparability of
more localized subnational statistics.

## Construction notes

`gaul_adm2_code` is numeric (integer) and country-specific, derived from the GAUL
database. The geographic area is identified in the survey on the basis of the
location or area name.

`value_codes` is intentionally null because GAUL codes come from an external
database and are not enumerated in the harmonized value space. Load the country
parameters and exceptions valid for the survey's ID year. Assign the code by
matching the household's recorded location name to the GAUL database geometry.

## Consistency checks

- `gaul_adm2_code` must be numeric (integer).
- The code assigned must correspond to the GAUL second-level unit containing the
  household's recorded location.
- Every second-level GAUL unit must be consistent with the first-level GAUL unit
  (`gaul_adm1_code`) in which it is nested.
- No household with an identifiable location may carry a standard missing (`.`).

## Escalation triggers

- The household's location cannot be matched to any GAUL second-level unit.
- The GAUL-to-survey mapping is internally inconsistent (e.g., conflicting nested
  codes).

## Common mistakes

- Storing `gaul_adm2_code` as a string rather than an integer.
- Fabricating or renumbering GAUL codes instead of using the GAUL database.
- Confusing the GAUL second-level code with `subnatid2` values.
- Assigning a second-level code inconsistent with the first-level code.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
