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
mapping_role: derived
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
derived_from:
  - VAR-geocode
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters:
  - PARAM-GEO-GMD-CROSSWALK

# --- Universe / skip gate ---
gates: []

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
  notes: "country_parameters updated 2026-09-30 to declare
      PARAM-GEO-GMD-CROSSWALK: when a country's crosswalk rows carry
      geo_source=GAUL, the GAUL code is already embedded in geo_id on the
      same row VAR-geocode matches, avoiding a separate GAUL database
      lookup. Verified against committed data (geo_idvar values ADM2_CODE
      and gaul2_code at geo_level='2')."
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

**Reusing the geography crosswalk.** Resolve `PARAM-GEO-GMD-CROSSWALK` from
the country layer for the survey ISO3 code and survey ID year (the same
match `VAR-geocode` performs). If the matched row has `geo_source: GAUL` and
a `geo_level` corresponding to the second administrative level, `geo_id` on
that row is already the GAUL code: set `gaul_adm2_code = int(geo_id)`
directly, with no separate GAUL database lookup required.

If the country's crosswalk instead uses a different `geo_source` (GADM,
NUTS, NSO, UN, DHS), the crosswalk does not carry a GAUL code for that
country; fall back to matching the household's recorded location name
directly against the GAUL database geometry as originally specified.

`value_codes` is intentionally null because GAUL codes come from an external
database (or, when available, the matched crosswalk row) and are not
enumerated in the harmonized value space.

## Consistency checks

- `gaul_adm2_code` must be numeric (integer).
- The code assigned must correspond to the GAUL second-level unit containing the
  household's recorded location.
- When sourced from the crosswalk, the matched row's `geo_source` must equal
  `GAUL`; never reinterpret a non-GAUL `geo_id` as a GAUL code.
- Every second-level GAUL unit must be consistent with the first-level GAUL unit
  (`gaul_adm1_code`) in which it is nested.
- No household with an identifiable location may carry a standard missing (`.`).

## Escalation triggers

- The household's location cannot be matched to any GAUL second-level unit.
- The GAUL-to-survey mapping is internally inconsistent (e.g., conflicting nested
  codes).
- The country's crosswalk uses a non-GAUL `geo_source` and no external GAUL
  database match is available either.

## Common mistakes

- Storing `gaul_adm2_code` as a string rather than an integer.
- Fabricating or renumbering GAUL codes instead of using the GAUL database
  (or the crosswalk's embedded GAUL `geo_id`).
- Confusing the GAUL second-level code with `subnatid2` values.
- Assigning a second-level code inconsistent with the first-level code.
- Treating `geo_id` from a non-GAUL-sourced crosswalk row as a genuine GAUL
  code.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
| 2026-09-30 | 0.2     | Reuse PARAM-GEO-GMD-CROSSWALK's embedded GAUL geo_id when geo_source=GAUL, instead of always requiring a separate GAUL database match | GPID Team |
