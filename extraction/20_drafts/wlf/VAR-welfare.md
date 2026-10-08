---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-welfare
canonical_label: "Welfare aggregate for poverty measurement"
variable_name: welfare
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
# In scope: welfare is a PASSTHROUGH of the country's final welfare aggregate.
# It is already normalized to the country's welfare basis (per capita, per adult
# equivalent, or other) upstream in the country prelude -- that normalization is
# a country-parameter / methodology choice, not something the canon imposes or
# performs. Bottom-up construction of the aggregate is out of scope
# (welfare-aggregate workstream). No derived_from inputs are declared: the final
# aggregate is adopted, not derived within the canon.
derived_from: []
derives_to: []

# --- Country parameter declarations ---
country_parameters: []

# --- Universe / skip gate ---
gates: []

# --- Cross-references ---
rules: []
exceptions:
  - EXC-PER-001
external_standards:
  - name: "World Bank Poverty and Inequality Platform (PIP)"
    url: https://pip.worldbank.org/home

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "welfare"
    - "welfare aggregate"
    - "consumption aggregate"
    - "income aggregate"
    - "disposable income"
    - "total expenditure"
    - "per capita consumption"
  typical_section_names:
    - "Welfare"
    - "Welfare aggregate"
    - "Consumption"
    - "Income"
    - "Poverty"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Welfare aggregates, welfare"
  extraction_method: manual
  extracted_on: "2026-09-21"
  human_reviewed: false
  reviewer: null
  notes: "Full spec supersedes the earlier VAR-welfare stub added for
          EXC-PER-001. welfare is a passthrough of the country's final welfare
          aggregate; the per-person normalization (per capita / adult
          equivalent) and any bottom-up construction happen upstream in the
          country prelude and are out of scope here."
---

## Definition

`welfare` is the harmonized, final household welfare aggregate that the country
uses to measure poverty. It is the aggregate provided to the World Bank Poverty
and Inequality Platform (PIP, https://pip.worldbank.org/home) as the input to
the estimation of international poverty.

The aggregate may be based on income, consumption, or expenditure; which of
these is used is recorded in `welfaretype`. `welfare` is the **final** welfare
value — already normalized to the country's welfare basis — and is expressed in
the currency and reference period the country uses for its own poverty
measurement.

## Conceptual intent

`welfare` is the single, analysis-ready measure of household living standards on
which poverty headcounts and distributional statistics are computed. It exists
so that downstream poverty measurement has one unambiguous welfare column,
regardless of whether the underlying concept is income, consumption, or
expenditure, and regardless of how the country built and normalized it.

By convention `welfare` carries the aggregate in the price space used for
poverty lines — the spatially deflated series (`welfaredef`) when a within-year
spatial adjustment is applied, otherwise the nominal series (`welfarenom`).

## Construction notes

**In scope: passthrough of the country's final welfare aggregate.**
Adopt the final welfare variable exactly as the country's harmonization process
delivers it, and record the concept in `welfaretype` (`INC`, `CONS`, `EXP`). Do
not re-scale, re-normalize, or re-deflate it. The value is already on the
country's chosen welfare basis.

**Normalization is a country / prelude concern, not a canon requirement.**
The per-person normalization is chosen and applied *upstream*, in the
country-specific prelude, and is governed by the country's methodology (a
country-parameter matter). It varies across countries — for example one country
may produce income divided by household size, another consumption divided by the
number of adult equivalents. Per-capita is the majority practice but **not** a
GMD requirement, so this canonical variable neither mandates nor performs a
particular normalization; it receives whatever final, normalized aggregate the
prelude produces.

*Illustration (EU-SILC, ALB 2019 — income welfare):* the country prelude takes
`HY020` (total disposable household income) and produces a final per-capita
income welfare (`HY020 / hhsize`, `welfaretype = INC`). `welfare` then passes
that final value through unchanged. The choice of `/ hhsize` (vs an
adult-equivalent scale) lives in the prelude, not here.

**Out of scope: bottom-up construction.**
Building the aggregate from component expenditures, imputed rents, durable-use
values, and spatial deflators is out of scope for this canon and is handled by
the separate welfare-aggregate workstream. When no final aggregate is available,
stop and escalate rather than constructing it under this variable.

Country exceptions may apply an explicitly documented adjustment on top of the
final aggregate (for example `EXC-PER-001`). Apply such an exception only when
its conditions match and it is recorded in the country layer.

## Consistency checks

- `welfare` must be non-negative for all non-missing records.
- Unit of analysis must be household.
- `welfaretype` must be present and one of `INC`, `CONS`, `EXP` wherever
  `welfare` is non-missing.
- `welfare` should equal `welfaredef` when a spatial deflation is applied and
  `welfarenom` when it is not; the three share the same welfare basis and differ
  only by price space.
- Any country exception affecting `welfare` (e.g. `EXC-PER-001`) must be
  explicitly referenced and its validity window must cover the survey year.

## Escalation triggers

- No final welfare aggregate is available and only components exist (would
  require out-of-scope bottom-up construction).
- Survey documentation does not identify whether the aggregate is income,
  consumption, or expenditure.
- A country exception's adjustment logic conflicts with approved harmonization
  policy, or its condition cannot be evaluated from available fields.
- The provided series' price space cannot be reconciled with `welfarenom` /
  `welfaredef`.

## Common mistakes

- Re-normalizing, re-scaling, or re-deflating a value the country prelude has
  already produced (welfare is passthrough of the final aggregate).
- Recording `welfare` without setting `welfaretype`.
- Treating nominal and spatially deflated welfare as interchangeable.
- Constructing an aggregate from components under this variable instead of
  escalating (that is the out-of-scope path / welfare-aggregate workstream).
- Applying a country exception factor without a valid condition match.

## Change log

| Date       | Version | Change                                                      | Authority |
|------------|---------|-------------------------------------------------------------|-----------|
| 2026-09-06 | 0.2     | Initial stub added to anchor EXC-PER-001                    | GPID Team |
| 2026-09-21 | 0.2     | Full spec; moved to MOD-WLF / wlf/                          | GPID Team |
| 2026-09-21 | 0.2     | Passthrough of the country's final aggregate; per-person normalization (per capita / adult equivalent) is a country prelude / country-parameter concern, not imposed by the canon | GPID Team |
