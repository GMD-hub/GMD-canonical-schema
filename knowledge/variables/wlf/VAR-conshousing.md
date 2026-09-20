---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-conshousing
canonical_label: "Household housing services consumption component"
variable_name: conshousing
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
    label: "Cannot be harmonized — no credible housing-flow estimate"

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
    - component_id: housing_market_rent
      native_unit_of_analysis: household
      roll_up_key: hhid
      value_path: direct_value
      include: when_present
      governed_by: imputed_rent
    - component_id: housing_imputed_rent
      native_unit_of_analysis: household
      roll_up_key: hhid
      value_path: direct_value | model_estimate
      include: when_present
      governed_by: imputed_rent
    - component_id: housing_utilities
      native_unit_of_analysis: household
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: dwelling_repairs
      native_unit_of_analysis: household
      roll_up_key: hhid
      value_path: direct_value
      include: when_present

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: housing_flow_selection
    rule: "use actual rent for renters; for owners/nonmarket tenants use imputed rent under the selected method"
  - stage: value_assembly
    rule: "sum rent, imputed-rent flow, utilities, and qualifying repairs to the household"
  - stage: annualization
    rule: "convert periodic values to annual-equivalent terms"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "exclude house purchase value"
    - "housing flow should represent service consumption, not stock acquisition"

# --- Cross-references ---
rules:
  - RULE-WLF-001
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.5, pp. 55–62; housing is a durable service and the relevant flow is rent or imputed rental value."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "rent"
    - "housing"
    - "imputed rent"
    - "utilities"
    - "repairs"
  typical_section_names:
    - "Housing"
    - "Dwelling"
    - "Rent and utilities"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.5, pp. 55–62"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 defines housing as a durable service; the welfare-relevant measure is the housing flow, not the purchase price."
---

## Definition

`conshousing` is the household's flow of housing services: actual rent for
market tenants, implicit rent for owners and nonmarket tenants, and housing
related utility and repair flows that represent current consumption. It is a
component of `VAR-welfare`.

## Conceptual intent

Housing is treated as a durable service rather than as acquisition of a stock.
The consumption concept is the rental-equivalent service flow during the
reference period, not the value of the dwelling itself.

## Construction notes

- Do not include house purchase or mortgage principal.
- Use actual rent when available for renters.
- For owners and nonmarket tenants, apply the survey's imputed-rent method
  selected in the harmonization spec.
- Include utilities and minor dwelling repairs that qualify as current
  consumption; exclude major maintenance or capital-like investment.

## Escalation triggers

- No credible housing-flow estimate is available, and a silent fallback would
  mis-rank households.
- The housing-valuation method is unset or contradicted by the survey data.
- The dataset has a housing module but no usable rent or imputation information.
