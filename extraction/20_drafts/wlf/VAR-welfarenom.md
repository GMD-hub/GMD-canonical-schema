---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-welfarenom
canonical_label: "Welfare aggregate, nominal (before price adjustment)"
variable_name: welfarenom
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
# Passthrough of the country-provided nominal aggregate. welfaredef is the
# spatially deflated counterpart; welfare is the aggregate used for poverty.
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
    - "nominal welfare"
    - "welfare aggregate"
    - "nominal consumption"
    - "nominal income"
    - "current prices"
  typical_section_names:
    - "Welfare"
    - "Welfare aggregate"
    - "Consumption"
    - "Income"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Welfare aggregates, welfarenom"
  extraction_method: manual
  extracted_on: "2026-09-21"
  human_reviewed: false
  reviewer: null
  notes: "Passthrough scope only; bottom-up derivation out of scope
          (welfare-aggregate workstream)."
---

## Definition

`welfarenom` is the final household welfare aggregate measured in nominal
terms — that is, before any spatial and/or temporal price adjustment. Like
`welfare`, it may be based on income, consumption, or expenditure (concept
recorded in `welfaretype`), and it is on the same welfare basis as `welfare`
(whatever normalization the country prelude applied); it differs only in price
space.

## Conceptual intent

`welfarenom` preserves the welfare aggregate at the prices actually observed in
the data, with no deflation applied. It is the price-space baseline from which
`welfaredef` (the spatially deflated series) is obtained, and it makes the
effect of any deflation transparent and auditable.

## Construction notes

**In scope (passthrough).** Adopt the country's final nominal welfare aggregate
as delivered and record the concept in `welfaretype`. Do not apply any spatial or
temporal deflator here — deflation belongs to `welfaredef` — and do not
re-normalize it: the per-person normalization (per capita, adult equivalent,
etc.) was chosen and applied upstream in the country prelude, exactly as for
`welfare`. Preserve the country's currency and reference period.

**Out of scope.** Constructing the nominal aggregate from component
expenditures is out of scope for this canon (welfare-aggregate workstream). If
only components are available, stop and escalate.

## Consistency checks

- `welfarenom` must be non-negative for all non-missing records.
- Unit of analysis must be household.
- When no price adjustment is applied, `welfare` should equal `welfarenom`.
- `welfaretype` must be present wherever `welfarenom` is non-missing.

## Escalation triggers

- Only components are available and no ready nominal aggregate exists.
- It is unclear whether the provided aggregate is already deflated (which would
  make it `welfaredef`, not `welfarenom`).
- The concept (income / consumption / expenditure) cannot be identified.

## Common mistakes

- Applying a spatial or temporal deflator to `welfarenom` (that produces
  `welfaredef`).
- Re-normalizing a value the country prelude already produced.
- Storing an already-deflated series as `welfarenom`.
- Recording `welfarenom` without setting `welfaretype`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-09-21 | 0.2     | Initial draft | GPID Team  |
