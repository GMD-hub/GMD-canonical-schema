---
date: 2026-08-03
title: "Extraction Preflight Governance Decisions"
status: draft
authority: GPID Team
supersedes: []
related:
  - governance/decisions/Open-Decisions.md
  - governance/audits/Gap-Audit-2026-07.md
---

# Extraction Preflight Governance Decisions, August 2026

## Approval Reference

The GMD Canonical Variable Schema approval was recorded during the GPID Team
meeting on 2026-07-29. **TODO: GPID Team must provide a locatable source reference
for this schema approval** (meeting notes URL, decision log entry, or recorded vote).
The `roadmap.json` status and strategy summary are not sufficient evidence alone.

## Decision 1: AGENTS.md Clarification — Supervised Implementation Write Policy

**Context**: The current `AGENTS.md` states that agents may write only to
`extraction/20_drafts/` and that `schema/` is for "Human or agent under
supervision." This is insufficient for the extraction pipeline, which requires
new Pydantic models, validators, fixtures, tests, and configuration outside
`extraction/20_drafts/`.

**Decision**: Clarify that:

1. Generated **CVS content artifacts** (variable specs, rule specs, parameter
   definitions, module definitions) are restricted to `extraction/20_drafts/`
   and must never be written to `knowledge/`, `extraction/30_review/`,
   `extraction/40_approved/`, or `country-parameters/`.

2. **Supervised implementation artifacts** (Python schemas, orchestrators,
   validators, tests, fixtures, configuration, CI workflows, documentation)
   created by coding agents under human direction may be written to `schema/`,
   `extraction_pipeline/`, `tests/`, `.github/workflows/`, `docs/`, and
   `extraction/config/`.

3. Human review is required before any generated CVS content is promoted from
   `extraction/20_drafts/` into `knowledge/`.

**Implementation**: This decision record is authoritative pending an `AGENTS.md`
update. The AGENTS.md change requires explicit human authorization per its own
governance rules.

## Decision 2: Module Registry

**Context**: The extraction pipeline must know which modules to process, their
canonical codes, source chapter aliases, and tier assignments.

**Decision**: The following module registry is approved:

| Code | Name | Source chapter | Tier | Scope |
|------|------|---------------|------|-------|
| IDN | Identification | chapter2-IDN.qmd | canonical | Non-welfare extraction |
| GEO | Geography | chapter3-GEO.qmd | canonical | Non-welfare extraction |
| DEM | Demographics (including Education, Disability) | chapter4-DEM.qmd | canonical | Non-welfare extraction |
| LBR | Labor | chapter5-LMR.qmd (alias: LMR) | canonical | Non-welfare extraction |
| UTL | Utilities/Access | chapter6-UTL.qmd | canonical | Non-welfare extraction |
| DWL | Durable Welfare | chapter7-DWL.qmd | canonical | Non-welfare extraction |

**Disambiguation**: `IDN` and `GEO` are **module codes** (Identification,
Geography), not ISO 3166-1 alpha-3 country codes. Do not confuse `MOD-IDN`
(module) with `CTY-IDN` (Indonesia in `country-parameters/countries/IDN/`).

## Decision 3: Basic Tier Policy

**Context**: The GMD guidelines reference a `basic` tier for some variables.
The extraction pipeline must know whether to treat `basic` as canonical,
inventory-only, or excluded.

**Decision**: `basic` tier is **inventory-only**. Variables tagged `basic`
appear in the frozen inventory and exclusion ledger but are not extracted as
full canonical drafts in the initial extraction. They may be promoted to
`canonical` in a future extraction wave with GPID Team approval.

## Decision 4: Schema and GMD Versions

**Decision**: During extraction:
- `schema_version`: `"0.1"` (current CVS schema version)
- `gmd_version`: `"1.0"` (GMD harmonization guideline version)
- `status`: `"draft"` (all extraction output is draft)
- `authority`: `"GMD harmonization guidelines"`

## Decision 5: Rule Priority Ownership

**Context**: Existing DEM rules use priorities 95, 90, 80. Extraction may
produce rules for other modules.

**Decision**: Rule priority is a **governed constant** during extraction.
All extracted rules receive `priority: 0` (unranked) until GPID Team review.
Country exceptions do not receive a priority field pending
`governance/decisions/Open-Decisions.md` A3 resolution.

## Decision 6: Effective Dates

**Decision**: During extraction:
- `effective_from`: `2000-01-01` (GMD baseline)
- `effective_to`: `null` (no expiration until reviewed)
These are governed constants; the extraction pipeline does not infer dates
from guideline prose.

## Decision 7: Provenance Date Semantics

**Decision**: `provenance.extracted_on` is a **generated metadata** field
populated with the ISO-8601 timestamp of the extraction run. Its stable
canonical semantics are: "the date the extraction pipeline produced this draft."
Run timestamps belong in the separate run ledger, not in content identifiers.

## Decision 8: Body Sections Contract

**Decision**: Every extracted variable, rule, and parameter Markdown draft must
include these body sections:

**Variable drafts**: `## Summary`, `## Value codes`, `## Derivation`,
`## Source note`, `## Prerequisites`, `## Country parameters`,
`## External standards`, `## Provenance`

**Rule drafts**: `## Condition`, `## Action`, `## Examples`, `## Notes`,
`## Provenance`

**Parameter drafts**: `## Description`, `## Values`, `## Applies to`,
`## Fallback`, `## Provenance`

## Decision 9: Module Model

**Decision**: A new `ModuleDefinition` Pydantic model is approved with fields:
`module_id`, `module_name`, `tier`, `source_chapter`, `description`,
`provenance`. Modules are extraction governance constants, not extracted from
the guidelines.

## Decision 10: Welfare vs. In-Scope UTL Expenditure Boundary

**Decision**: The following rule governs every expenditure mention in chapters
2-7:

| Context | Classification | Disposition |
|---------|---------------|-------------|
| Chapter 8 (CONS) output | Welfare | Excluded from inventory |
| Chapter 7 (DWL) output | Non-welfare | Included in inventory |
| Chapter 6 (UTL) expenditure variable | Non-welfare | Included in inventory |
| Cross-reference to chapter 8 from chapters 2-7 | Welfare | Recorded in exclusion ledger |
| Aggregate consumption/expenditure reference | Welfare | Excluded unless it's a DWL durable |

**Examples**:
- `expenditure_food` in chapter 8 → welfare, excluded
- `access_electricity` in chapter 6 → UTL, included
- `durable_assets_count` in chapter 7 → DWL, included
- "See chapter 8 for consumption aggregate" in chapter 4 → welfare reference, ledger entry

## Decision 11: Non-Null Weight Rule

**Decision**: The GMD guidelines' non-null weight invariant is encoded as a
cited prohibition in the extraction rubric and validator contract. It applies
to all harmonization variables that require survey weights. The extraction
pipeline records this as a sourced invariant; it does not inspect raw survey
observations or test weight values at runtime.

**Citation**: GMD household survey harmonization guidelines, weight handling
section.

## Pending Human Authorization

This decision record is a **draft**. The following items require GPID Team
approval before Phase 1 is complete:

- [ ] D1: AGENTS.md clarification
- [ ] D5: Rule priority ownership confirmed
- [ ] D6: Effective date baseline confirmed
- [ ] Approval reference for 2026-07-29 meeting located
- [ ] Module names and source aliases verified against guidelines
- [ ] D9: Confirm whether `ModuleDefinition.provenance` field is required.
      Decision 9 lists `provenance` in the approved field set, but modules
      are governance constants (per the decision's own closing sentence).
      The schema model now accepts `provenance: str | None = None` to match
      the decision; GPID Team must confirm whether this field should be
      required or dropped from the approved field list.
