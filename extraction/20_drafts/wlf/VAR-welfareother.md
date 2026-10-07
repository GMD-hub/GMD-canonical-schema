---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-welfareother
canonical_label: "Alternative welfare aggregate (secondary concept)"
variable_name: welfareother
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
# Passthrough of an additional, differently-typed aggregate present in the data.
derived_from: []
derives_to: []

# --- Country parameter declarations ---
country_parameters: []

# --- Universe / skip gate ---
gates: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "alternative welfare"
    - "secondary aggregate"
    - "income aggregate"
    - "consumption aggregate"
    - "expenditure aggregate"
  typical_section_names:
    - "Welfare"
    - "Welfare aggregate"
    - "Income"
    - "Consumption"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Welfare aggregates, welfareother"
  extraction_method: manual
  extracted_on: "2026-09-21"
  human_reviewed: false
  reviewer: null
  notes: "Optional secondary aggregate of a different type from
          welfare/welfarenom/welfaredef; passthrough scope only. Its type is
          recorded in VAR-welfareothertype."
---

## Definition

`welfareother` is a secondary, final welfare aggregate present in the data file
when a welfare type different from that of `welfare`, `welfarenom`, and
`welfaredef` is also available. For example, if consumption is used for `welfare` / `welfarenom`
/ `welfaredef` but an income aggregate also exists, the income aggregate can be
carried here. Its type is recorded in `welfareothertype`.

## Conceptual intent

`welfareother` preserves an additional, differently-based welfare measure that
the survey provides, so that a country's alternative aggregate is retained
alongside the primary one without overwriting or being confused with it. It is
optional and present only when such a second aggregate exists.

## Construction notes

**In scope (passthrough).** When the data file contains a second final aggregate
whose type differs from the primary welfare series, adopt it as `welfareother` as
delivered and record its concept in `welfareothertype`. Do not re-normalize or
rebuild it — any normalization was applied upstream in the country prelude, on
the same basis as `welfare`. Leave `welfareother` missing (`.a`) when no such
secondary aggregate exists.

**Out of scope.** Constructing a secondary aggregate from components is out of
scope for this canon (welfare-aggregate workstream).

## Consistency checks

- `welfareother` must be non-negative for all non-missing records.
- Unit of analysis must be household.
- `welfareothertype` must be present wherever `welfareother` is non-missing.
- `welfareothertype` should differ from `welfaretype` (a secondary aggregate of
  the same type as the primary is unusual; flag for review).

## Escalation triggers

- A second aggregate is referenced but its concept (income / consumption /
  expenditure) is not documented.
- It is unclear whether the second series is genuinely a different concept or a
  duplicate of the primary aggregate.

## Common mistakes

- Storing `welfareother` without setting `welfareothertype`.
- Using `welfareother` to hold a nominal/deflated variant of the primary series
  (those belong in `welfarenom` / `welfaredef`).
- Re-deflating or re-scaling the provided secondary aggregate.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-09-21 | 0.2     | Initial draft | GPID Team  |
