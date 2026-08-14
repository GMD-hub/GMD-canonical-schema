---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-relationharm
canonical_label: "Relationship to head of household harmonized across all regions"
variable_name: relationharm
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: derived
data_type: categorical

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Head"
  - value: 2
    label: "Spouse"
  - value: 3
    label: "Children"
  - value: 4
    label: "Parents"
  - value: 5
    label: "Other relative"
  - value: 6
    label: "Non-relative"
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".o"
    label: "Other relationship not covered by harmonized codes"

# --- Derivation graph ---
derived_from:
  - VAR-relationcs
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites:
  - variable_id: VAR-relationcs
    condition: "Must be constructed first. relationharm maps the country-specific
                relationship categories into the harmonized six categories."

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "relationship to head"
    - "relationship to head of household"
    - "head"
    - "spouse"
  typical_section_names:
    - "Household roster"
    - "Household composition"
    - "Demographics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, relationharm"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "Derived from the country-specific relationcs. Where the head is missing or
          a migrant, assign the spouse as head; if the spouse is also unavailable,
          use the oldest member and recode all relations to head accordingly."
---

## Definition

`relationharm` records, in six harmonized categories, each individual's
relationship to the reference person of the household (usually the head):
1 = Head, 2 = Spouse, 3 = Children, 4 = Parents, 5 = Other relative,
6 = Non-relative.

## Conceptual intent

`relationharm` provides a cross-country comparable measure of household
structure. It enables identification of household heads and spouses, household
composition analysis, and consistent handling of headship across harmonized
surveys.

## Construction notes

Derive `relationharm` by mapping the country-specific `relationcs` categories
into the six harmonized codes. Where the head is missing or a migrant, assign
the spouse as the head of the household; if the spouse is also unavailable, use
the oldest member of the household as the head and recode all relations to head
accordingly.

Variable values coded as `98` or other numeric placeholder characters should be
excluded from the values of `relationharm`.

## Consistency checks

- Every household must have exactly one head (`relationharm = 1`) that is not
  missing.
- `relationharm` must be an integer in the range [1, 6]. Flag any value outside
  this range.
- Cross-check that head and spouse have different values for `male` (in most
  country contexts); flag households where they share the same sex.
- Missing heads: assign the oldest member as head if not collected, or
  `pid = 1` as head otherwise.

## Escalation triggers

- More than one head per household, or no head identified.
- Head and spouse have the same recorded sex without a country-context
  explanation.
- Country relationship categories cannot be mapped unambiguously to the six
  harmonized categories.

## Common mistakes

- Keeping numeric placeholder codes (98, 99) as valid relationship values.
- Allowing more than one head per household.
- Not reassigning headship when the recorded head is missing or a migrant.
- Confusing `relationcs` (country-specific) with `relationharm` (harmonized).

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
