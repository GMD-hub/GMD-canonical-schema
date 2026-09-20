---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-consfurnishings
canonical_label: "Household furnishings and household-equipment consumption component"
variable_name: consfurnishings
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
    label: "Cannot be harmonized — household-furnishings module unusable"

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
    - component_id: furnishings_items
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: household_equipment
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: when_present
    - component_id: routine_maintenance
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: when_present

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "sum direct household expenditure values; the category is usually recorded as expenditure, not quantity × unit price"
  - stage: recall_annualization
    scope: all rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "exclude major durable acquisitions from this component"
    - "sum item rows constitutes the furnishings subtotal"

# --- Cross-references ---
rules:
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.3, pp. 35–40; furnishings and routine household equipment are included as ordinary nondurables or routine maintenance."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "furnishings"
    - "household equipment"
    - "utensils"
    - "tools"
    - "maintenance"
  typical_section_names:
    - "Household goods"
    - "Furnishings and equipment"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3, pp. 35–40"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 includes furnishings, household utensils, routine maintenance, and similar ordinary household-goods expenditures in the nonfood aggregate."
---

## Definition

`consfurnishings` is the household's consumption of furnishings, household
equipment, tools, utensils, and routine maintenance services that are not
capital-like durable acquisitions. It is a component of `VAR-welfare`.

## Conceptual intent

These items are part of regular household consumption, subject to the standard
item-level review for durable boundaries and investment-like purchases.

## Construction notes

- Keep ordinary household goods and repairs.
- Exclude major acquisitions that belong to the durable stock definition.
- Annualize any periodic expenditure before assembling the household total.

## Escalation triggers

- Items are borderline between routine household maintenance and durable capital
  formation; the case should be resolved by the survey spec.
- Household-goods expenditure is reported but not attributable to ordinary
  consumption rather than acquisition.
