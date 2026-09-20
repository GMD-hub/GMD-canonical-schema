---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-consclothing
canonical_label: "Household clothing and footwear consumption component"
variable_name: consclothing
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
    label: "Cannot be harmonized — clothing module unusable"

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
    - component_id: clothing_purchased
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: footwear_purchased
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "sum direct expenditure values for clothing and footwear; quantity and unit price are not the primary construction path for these item records"
  - stage: recall_annualization
    scope: all rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "no negative item values"
    - "sum of clothing and footwear rows equals household subtotal"

# --- Cross-references ---
rules:
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.3, p. 37; clothing and footwear are ordinary nondurable consumption and are included."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "clothing"
    - "footwear"
    - "garments"
    - "apparel"
  typical_section_names:
    - "Clothing and footwear"
    - "Household expenditure"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3, p. 37"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 treats clothing and footwear as ordinary nondurable consumption and annualizes it."
---

## Definition

`consclothing` is the household consumption of clothing, footwear, and related
apparel items, annualized to the common reference period and summed to the
household. It is a component of `VAR-welfare`.

## Conceptual intent

This category is a standard nondurable consumption item in the MV22 checklist:
no special materiality adjustment is needed beyond annualization and item-level
coverage control.

## Construction notes

- Include ordinary clothing and footwear expenditures.
- If reported as value, keep that value; otherwise compute from quantity and
  unit price.
- Annualize to a common period before aggregation.

## Escalation triggers

- Clothing module present but unusable → `.b`.
- Survey item lists mix clothing with major durable or business-use items; item
  classification must be reviewed by the survey-specific spec.
