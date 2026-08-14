---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-gauladm1code
canonical_label: "GAUL code - first administrative level"
variable_name: gaul_adm1_code
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
    - "adm1"
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
  source_section: "Geography (GEO), Mapping and Description of Variables, gaul_adm1_code"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`gaul_adm1_code` is a numeric, country-specific variable that holds the Global
Administrative Unit Layers (GAUL) code for the first administrative level in
which the household is located. It is taken from the GAUL database (a copy is
available to the D4G team) where the geographic area can be identified in the
survey based on the location or area name.

## Conceptual intent

`gaul_adm1_code` provides a standardized, globally comparable code for the
first-level administrative division, independent of the survey's own classification.
It supports the cross-survey comparability of subnational statistics.

## Construction notes

`gaul_adm1_code` is numeric (integer) and country-specific, derived from the GAUL
database. The geographic area is identified in the survey on the basis of the
location or area name. The number of unique values from `subnatid1` and
`gaul_adm1_code` may be the same or different: e.g., if the survey is
representative at statistical regions while GAUL provides state-level codes, the
mapping reveals how the regions are constructed.

`value_codes` is intentionally null because GAUL codes come from an external
database and are not enumerated in the harmonized value space. Load the country
parameters and exceptions valid for the survey's ID year. Assign the code by
matching the household's recorded location name to the GAUL database geometry.

## Consistency checks

- `gaul_adm1_code` must be numeric (integer).
- The code assigned must correspond to the GAUL first-level unit containing the
  household's recorded location.
- The number of distinct codes and their relationship to `subnatid1` must be
  documented and reviewed for plausibility.
- No household with an identifiable location may carry a standard missing (`.`).

## Escalation triggers

- The household's location cannot be matched to any GAUL first-level unit.
- The GAUL-to-survey mapping is internally inconsistent (e.g., one location maps
  to conflicting codes).

## Common mistakes

- Storing `gaul_adm1_code` as a string rather than an integer.
- Fabricating or renumbering GAUL codes instead of using the GAUL database.
- Confusing the GAUL first-level code with `subnatid1` values.
- Matching by name loosely and assigning the wrong GAUL unit.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
