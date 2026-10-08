# Benchmark Documentation Track

This folder stores non-executable benchmarking references used for quality
assurance and contextual comparison.

## Scope

Artifacts in this folder are observational and must not be interpreted as
prescriptive harmonization canon.

Use this track for:

- JMP benchmark estimates used for QA comparisons.
- Narrative benchmark notes and reconciliation logs.
- Country-year benchmark tables that are not direct runtime inputs.

Do not use this track for:

- Parameter records consumed by runtime construction logic.
- Country exception records consumed by runtime decision logic.
- Any record intended to be compiled into `build/output/` bundles.

## Boundary with executable canon

If a JMP-derived value directly drives harmonization logic, it must be encoded
as a governed country parameter or country exception in
`country-parameters/countries/<ISO3>/` with full provenance.

If the value is benchmarking-only, keep it here and reference it from audits,
validation notes, or reviewer documentation.

## Recommended metadata

Benchmark artifacts should include, at minimum:

- country ISO3 code
- survey year or period
- benchmark source and retrieval date
- benchmark definition and units
- comparison target variable IDs
- notes on interpretation limits
