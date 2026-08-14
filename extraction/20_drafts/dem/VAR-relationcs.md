---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-relationcs
canonical_label: "Relationship to head of household country/region specific"
variable_name: relationcs
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: string

# --- Allowed output values ---
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Relationship to head not collected in this survey"

# --- Derivation graph ---
derived_from: []
derives_to:
  - VAR-relationharm

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
    - "relationship to head"
    - "relationship to head of household"
    - "relation to head"
    - "relationship"
  typical_section_names:
    - "Household roster"
    - "Household composition"
    - "Demographics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, relationcs"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "A country-specific categorical variable. Categories are defined according to
          region or country requirements. It is the raw input from which the
          harmonized relationharm is derived."
---

## Definition

`relationcs` is a country-specific categorical variable that records each
individual's relationship to the head of the household as defined by the
region's or the country's own categories.

## Conceptual intent

Survey questionnaires use country-specific relationship-to-head categories that
vary across countries and regions. `relationcs` preserves these original
categories verbatim so they can be mapped into the common six-category
`relationharm` variable for cross-country comparability.

## Construction notes

Record the relationship-to-head category exactly as defined by the country or
region. The categories are country-specific and should not be recoded into the
harmonized scheme at this stage.

Variable values coded as `98` or other numeric placeholder characters should be
excluded from the values of `relationcs` and handled as missing.

`relationcs` is the source from which `relationharm` is derived.

## Consistency checks

- `relationcs` should map cleanly and losslessly into `relationharm` for the
  harmonized six categories.
- Exclude numeric placeholder codes (e.g. 98, 99, 9) that do not correspond to
  defined relationship categories.
- Each individual should have exactly one relationship-to-head category.

## Escalation triggers

- Country relationship categories are ambiguous or overlap, so the mapping to
  `relationharm` is not well defined.
- Many individuals fall into capture-all or "other" categories that make the
  harmonized mapping uncertain.

## Common mistakes

- Recoding `relationcs` directly into the harmonized scheme without retaining
  the original country-specific categories.
- Keeping numeric placeholder codes (98, 99, 9) as valid relationship values.
- Confusing country-specific categories with the harmonized categories.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
