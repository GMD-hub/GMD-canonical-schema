---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-welfshprosperity
canonical_label: "Welfare aggregate for shared prosperity"
variable_name: welfshprosperity
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
# Passthrough. Often identical to VAR-welfare; may be a different aggregate when
# shared prosperity uses a different welfare concept. Relationship expressed in
# prose rather than by value derivation.
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
    - "shared prosperity"
    - "welfare aggregate"
    - "bottom 40"
    - "growth of the bottom"
  typical_section_names:
    - "Welfare"
    - "Shared prosperity"
    - "Consumption"
    - "Income"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Welfare aggregates, welfshprosperity"
  extraction_method: manual
  extracted_on: "2026-09-21"
  human_reviewed: false
  reviewer: null
  notes: "Passthrough scope only. Equals VAR-welfare when the same aggregate is
          used for poverty and shared prosperity; otherwise a distinct
          aggregate with its own type in VAR-welfshprtype."
---

## Definition

`welfshprosperity` is the final household welfare aggregate used to compute the
shared prosperity indicator. It is either the same as `welfare` — when the same welfare
aggregate is used for both poverty and shared prosperity — or a different
aggregate when shared prosperity is measured on a different welfare concept. Its
type is recorded in `welfshprtype`.

## Conceptual intent

Shared prosperity (the growth of welfare among the less well-off part of the
distribution) is sometimes measured on a welfare concept that differs from the
one used for poverty headcounts. `welfshprosperity` gives that indicator its own
explicit welfare column so the two measures are never silently conflated.

## Construction notes

**In scope (passthrough).** If the country uses the same aggregate as for
poverty, set `welfshprosperity` equal to `welfare` and set `welfshprtype` equal
to `welfaretype`. If a different aggregate is used, adopt the country's final
shared-prosperity aggregate as delivered, recording its concept in
`welfshprtype`. Do not re-normalize or rebuild it — any normalization was applied
upstream in the country prelude, as for `welfare`.

**Out of scope.** Bottom-up construction of the shared-prosperity aggregate is
out of scope for this canon (welfare-aggregate workstream).

## Consistency checks

- `welfshprosperity` must be non-negative for all non-missing records.
- Unit of analysis must be household.
- When it equals `welfare`, `welfshprtype` must equal `welfaretype`.
- `welfshprtype` must be present wherever `welfshprosperity` is non-missing.

## Escalation triggers

- It is unclear whether shared prosperity uses the same aggregate as poverty.
- A separate shared-prosperity aggregate is referenced but not provided.
- The concept behind the shared-prosperity aggregate is not documented.

## Common mistakes

- Assuming `welfshprosperity` always equals `welfare` without checking the
  country's methodology.
- Setting `welfshprosperity` but leaving `welfshprtype` blank.
- Re-deflating a provided shared-prosperity aggregate.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-09-21 | 0.2     | Initial draft | GPID Team  |
