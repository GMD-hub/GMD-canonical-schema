---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.2
# ================================================================

parameter_id: PARAM-WASH-SANITATION-CROSSWALK
parameter_name: "Country sanitation source crosswalk rows"
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
  gmd_target: string
  gmd_spans: string
  improved_flag: boolean
  shared_flag: boolean
  source_row: integer

applies_to_variables:
  - VAR-sanitationsource
  - VAR-impsanrec

fallback_policy: block_and_escalate
global_default: null

provenance:
  source_document: "GMD_household_survey_harmonization.md"
  extraction_method: manual
  extracted_on: "2026-09-06"
  human_reviewed: false
  reviewer: null
  notes: "Canonical contract for row-based country sanitation crosswalk values.
          2026-10-27 (proposed, pending GPID Team approval): applies_to_variables
          filled (VAR-sanitationsource, VAR-impsanrec) for RULE-WASH-001: every category is placed
          through this crosswalk, and improved_flag serves the direct path for
          problematic categories."
---

## Definition

Defines row-level country sanitation-source crosswalk records linking national
labels to JMP classifications and GMD targets.

## Parameter notes

- Includes structured JMP classification identifiers and source row traceability.
- Supports direct harmonization input while keeping benchmark-only logic out of
  executable country canon.

## Fallback behavior

`block_and_escalate` is required when no valid country record exists.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-09-06 | 0.2 | Add table contract for sanitation crosswalk extraction | GPID Team |
| 2026-10-27 | 0.3 | Draft: fill applies_to_variables (VAR-sanitationsource, VAR-impsanrec) for RULE-WASH-001 | GPID Team (proposed) |
