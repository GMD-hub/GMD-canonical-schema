---
project-name: "GMD Canonical Variable Schema"
team: "DECDG / GPID -- World Bank"
created: "2026-07-29"
last-reviewed: "2026-07-29"
---

# GMD Canonical Variable Schema

## Objective

The GMD Canonical Variable Schema (CVS) is the governed knowledge base for AI-assisted household survey harmonization. It translates the GMD harmonization guidelines into versioned records that are readable by people, validated by software, and consumable by harmonization agents.

## Key Deliverables

- Universal knowledge base: variable specs, rules, parameters, modules, rubrics, and exceptions
- Country parameter layer: governed country-specific parameter values and exceptions by ISO3 country code and validity window
- Pydantic schema models for validating structured artifacts
- Validation framework for structural, governance, and country-layer checks
- Build/compiler system for country-and-year runtime JSON bundles
- Artifact lifecycle workflow from agent draft through human review and canonical promotion

## Constraints

- The GMD household survey harmonization guidelines in `GMD-hub/GMD-guidelines` are authoritative.
- Agents may write only to `extraction/20_drafts/`; humans own review, approval, and promotion to `knowledge/` and `country-parameters/`.
- All work must comply with `AGENTS.md`, including naming, fallback-policy, and structural rules.
- Generated files under `build/output/` must not be edited manually.
- Python 3.10 or newer is required.

## Current Focus

We are building the framework for the CVS and developing tools to restructure rules for GMD harmonization and country-specific conditions and exceptions.