---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.2
# ================================================================

parameter_id: PARAM-WASH-WATER-CROSSWALK
parameter_name: "Country water source crosswalk rows"
module_id: MOD-DWL
schema_version: "0.2"
status: draft
authority: "GPID Team"

kind: construction
value_type: table
value_schema: null
row_schema:
  country_entry_id: string
  source_category_code: string
  national_label_en: string
  national_label_local: string
  jmp_classification: string
  jmp_id: string
  improved_flag: boolean
  shared_flag: boolean
  source_row: integer

applies_to_variables:
  - VAR-watersource
  - VAR-impwatrec

fallback_policy: block_and_escalate
global_default: null

provenance:
  source_document: "GMD_household_survey_harmonization.md"
  extraction_method: manual
  extracted_on: "2026-09-06"
  human_reviewed: false
  reviewer: null
  notes: "Canonical contract for row-based country water crosswalk values.
          2026-10-27 (proposed, pending GPID Team approval): applies_to_variables
          filled (VAR-watersource, VAR-impwatrec) for RULE-WASH-001: every category is placed
          through this crosswalk, and improved_flag serves the direct path for
          problematic categories.
          2026-10-28 (proposed): gmd_target and gmd_spans dropped from row_schema: the
          GMD code (or the codes a coarse node spans) follows from jmp_id through the
          VAR-watersource JMP-2025 anchor, and the direct path for a node with no fine code
          is VAR-impwatrec's (not improved_flag). improved_flag is JMP's own improved status,
          kept as information: it differs from GMD's for delivered water (JMP
          improved, GMD codes 11-12 not improved)."
---

## Definition

Defines row-level country water-source crosswalk records linking national
labels to JMP classifications (`jmp_id`), from which the GMD codes follow
through the `VAR-watersource` JMP-2025 anchor.

## Parameter notes

- `improved_flag` and `shared_flag` preserve modeled access attributes.

## Fallback behavior

`block_and_escalate` is required when no valid country record exists.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-09-06 | 0.2 | Add table contract for water crosswalk extraction | GPID Team |
| 2026-10-27 | 0.3 | Draft: fill applies_to_variables (VAR-watersource, VAR-impwatrec) for RULE-WASH-001 | GPID Team (proposed) |
| 2026-10-28 | 0.3 | Draft: drop gmd_target and gmd_spans from row_schema: precomputed duplicates of jmp_id, whose GMD code (or the codes a coarse node spans) follows from the VAR-watersource JMP-2025 anchor; no consumer reads them | GPID Team (proposed) |
