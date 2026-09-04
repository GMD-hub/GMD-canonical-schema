---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-consalcoholtobacco
canonical_label: "Household alcohol and tobacco consumption component"
variable_name: consalcoholtobacco
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
    label: "Cannot be harmonized — alcohol/tobacco module unusable"

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
    - component_id: alcohol_tobacco_purchased
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: alcohol_tobacco_in_kind
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "aggregate direct expenditure values; do not assume quantity × unit price records are the primary construction path for these items"
  - stage: recall_annualization
    scope: all item rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "no negative item values"
    - "sum of all alcohol and tobacco items equals household subtotal"

# --- Cross-references ---
rules:
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "Mancini & Vecchi (2022), §4.3, alcohol/tobacco/narcotics; includes these items in the NCA under revealed preferences and non-paternalism."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "alcohol"
    - "tobacco"
    - "cigarettes"
    - "liquor"
    - "narcotics"
  typical_section_names:
    - "Alcohol and tobacco"
    - "Tobacco and narcotics"
    - "Household expenditure"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3, p. 37"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 explicitly includes alcohol, tobacco, and narcotics in the consumption aggregate; no special exclusion rule is given for these goods."
---

## Definition

`consalcoholtobacco` is the household consumption of alcoholic beverages,
 tobacco, and narcotic products, standardized to the common annual reference
 period and summed to the household. It is a component of `VAR-welfare`.

## Conceptual intent

These goods are included under MV22's welfare-consistent approach because the
aggregate is designed to reflect revealed individual preferences rather than an
external moral ranking. They are not treated as a special excluded category.

## Construction notes

- Include purchased items and any in-kind receipts that are actually consumed.
- Annualize to a common period before aggregation.
- If related household modules contain both a direct value and quantity/price,
  use the direct value unless a documented data-quality rule says otherwise.

## Escalation triggers

- An item that appears to be a production input or a transfer not representing
  consumer use should be excluded by manual classification, not by default.
- If the survey's alcohol/tobacco module is not usable, mark `.b`.
