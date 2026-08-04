# Universal Extraction Rubric v1

Common rules and conventions applied to all module extractions.

## Field Classification Rules

- **source-explicit**: Copy exactly from cited evidence. No reinterpretation.
  Example: variable name, label, tier, value codes.
- **deterministically-derived**: Compute from versioned Python rule.
  Example: VAR-id generation, source order normalization.
- **governed-constant**: Read from `extraction-governance.v1.yaml`.
  Example: schema_version, gmd_version, status, authority.
- **agent-interpreted**: Propose with confidence < 1.0 and citations.
  Example: mapping_role, prerequisites, rules.
- **generated-metadata**: Set by orchestrator, not agent.
  Example: extracted_on, extraction_method.
- **unresolved**: Store null, create blocking issue. Never emit canonical.

## Non-Null Weight Invariant

Variables that require survey weights must document the non-null weight
constraint. This is a cited prohibition from the GMD harmonization guidelines
weight handling section. The extraction rubric records this invariant; the
pipeline does not inspect raw survey data.

## Welfare Boundary

- Chapter 8 (CONS) outputs → welfare, excluded from inventory
- Chapter 7 (DWL) outputs → non-welfare, included
- Chapter 6 (UTL) expenditure variables → non-welfare, included
- Cross-references to chapter 8 → exclusion ledger entry

## Body Section Contract

Every variable draft must include:
`## Summary`, `## Value codes`, `## Derivation`, `## Source note`,
`## Prerequisites`, `## Country parameters`, `## External standards`,
`## Provenance`
