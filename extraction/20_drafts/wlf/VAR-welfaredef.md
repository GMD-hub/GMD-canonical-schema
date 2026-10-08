---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-welfaredef
canonical_label: "Welfare aggregate, spatially deflated"
variable_name: welfaredef
module_id: MOD-WLF
gmd_version: "3.0"
schema_version: "0.2"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: derived_preferred
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
# Passthrough of the country-provided deflated aggregate. welfarenom is the
# nominal counterpart; welfare is the aggregate used for poverty.
derived_from: []
derives_to: []

# --- Country parameter declarations ---
country_parameters: []

# --- Universe / skip gate ---
gates: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "World Bank Poverty and Inequality Platform (PIP)"
    url: https://pip.worldbank.org/home

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "deflated welfare"
    - "spatially deflated"
    - "real welfare"
    - "spatial price index"
    - "regional price deflator"
  typical_section_names:
    - "Welfare"
    - "Welfare aggregate"
    - "Deflation"
    - "Spatial price adjustment"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Welfare aggregates, welfaredef"
  extraction_method: manual
  extracted_on: "2026-09-21"
  human_reviewed: false
  reviewer: null
  notes: "Passthrough scope only; construction of the spatial deflator and its
          application is out of scope (welfare-aggregate workstream)."
---

## Definition

`welfaredef` is the final household welfare aggregate after spatial deflation — a
spatial or within-year inflation adjustment that expresses the aggregate in
comparable prices across regions or areas within the survey year. Like
`welfare`, it may be based on income, consumption, or expenditure (concept
recorded in `welfaretype`), and it is on the same welfare basis as `welfare`
(whatever normalization the country prelude applied); it differs only in price
space.

## Conceptual intent

`welfaredef` adjusts `welfarenom` for cost-of-living differences within the
survey (for example rural vs. urban or regional price differences) so that a
given value represents the same real living standard regardless of where the
household lives. It is typically the series carried into `welfare` for poverty
measurement when a spatial adjustment is used.

## Construction notes

**In scope (passthrough).** Adopt the country's final spatially deflated welfare
aggregate as delivered and record the concept in `welfaretype`. Do not re-deflate
it, substitute a different deflator, or re-normalize it: the per-person
normalization was applied upstream in the country prelude, exactly as for
`welfare`.

**Out of scope.** Deriving the spatial deflator and applying it to a nominal
aggregate is out of scope for this canon (welfare-aggregate workstream). If only
`welfarenom` and raw price data are available, do not compute the deflation
inside GMD harmonization — stop and escalate.

## Consistency checks

- `welfaredef` must be non-negative for all non-missing records.
- Unit of analysis must be household.
- Where a spatial adjustment is applied, `welfare` should equal `welfaredef`.
- `welfaredef` and `welfarenom` should be equal only where the spatial deflator
  is 1 (no adjustment for that stratum); large systematic gaps in the wrong
  direction may signal a mislabeled series.
- `welfaretype` must be present wherever `welfaredef` is non-missing.

## Escalation triggers

- Only `welfarenom` is available and the spatial deflator is not provided.
- It is unclear whether the deflation is spatial (within-year) or also temporal.
- The deflated and nominal series are indistinguishable or mislabeled.

## Common mistakes

- Applying a second deflation to an already-deflated series.
- Swapping `welfarenom` and `welfaredef`.
- Computing the spatial deflator inside GMD harmonization (out of scope).

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-09-21 | 0.2     | Initial draft | GPID Team  |
