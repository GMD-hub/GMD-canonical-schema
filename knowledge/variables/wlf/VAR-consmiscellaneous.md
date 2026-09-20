---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-consmiscellaneous
canonical_label: "Household miscellaneous goods and services consumption component"
variable_name: consmiscellaneous
module_id: MOD-WLF
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: aggregate
data_type: numeric_continuous

value_codes: null
allowed_range:
  min: 0
  max: null

missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized — miscellaneous category unusable"

# --- Derivation graph ---
derived_from: []
derives_to:
  - VAR-welfare

country_parameters: []
prerequisites: []

# --- Aggregate: component structure ---
component_structure:
  operation: sum
  output_unit_of_analysis: household
  components:
    - component_id: miscellaneous_goods
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: miscellaneous_services
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "sum direct misc goods and services that fit the current-use concept in the household budget; these are usually expenditure values, not quantity × unit price records"
  - stage: recall_annualization
    scope: all rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "exclude taxes, financial services, and other clearly non-consumption activities"
    - "sum of included rows equals the miscellaneous subtotal"

# --- Cross-references ---
rules:
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.3, pp. 35–40; personal care, social protection, and remaining miscellaneous consumption are included under the nonfood aggregate."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "miscellaneous"
    - "personal care"
    - "social protection"
    - "other goods"
  typical_section_names:
    - "Miscellaneous"
    - "Personal care"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3, pp. 35–40"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 includes personal care, social protection, and remaining miscellaneous goods/services that pass the current-use test."
---

## Definition

`consmiscellaneous` is the household's residual current-use spending in the
miscellaneous goods and services category, such as personal care and other small
nonfood expenditures that are part of ordinary consumption. It is a component of
`VAR-welfare`.

## Conceptual intent

This category captures the remaining nonfood items that are not better placed in
other divisions but still represent current-period consumption under the MV22
checklist. It is deliberately broad and must be controlled with a clear item-level
classification rule.

## Construction notes

- Include eligible personal care and miscellaneous spending.
- Exclude taxes, financial services, and transfer-like outlays.
- Annualize and sum to household units after validation.

## Escalation triggers

- Items appear to be financial, transfer, or investment-related rather than
  current consumption.
- The module is poorly coded and cannot be mapped into valid consumption items.
