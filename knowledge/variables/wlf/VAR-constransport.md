---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-constransport
canonical_label: "Household transport consumption component"
variable_name: constransport
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
    label: "Cannot be harmonized — transport module unusable"

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
    - component_id: transport_operation
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: transport_services
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: transport_goods
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: when_present

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "collect transport operation, passenger travel, and relevant services to the household"
  - stage: recall_annualization
    scope: all rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "exclude vehicle purchase from the transport consumption component"
    - "sum of included transport rows equals the transport subtotal"

# --- Cross-references ---
rules:
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.3, p. 38; transport operations and services are included; vehicle purchase is excluded as a durable acquisition."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "transport"
    - "fuel"
    - "bus"
    - "taxi"
    - "travel"
  typical_section_names:
    - "Transport"
    - "Travel and transport"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3, p. 38"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 includes the operation of personal transport equipment and transport services, but excludes vehicle purchase as a durable acquisition."
---

## Definition

`constransport` is the household consumption of transport-related operations and
services, including fuel, maintenance, passenger transport, and goods transport
that are part of current living costs. It is a component of `VAR-welfare`.

## Conceptual intent

Transport is treated as ordinary consumption when it reflects use and operation
of equipment. Its purchase price is not counted here because vehicle acquisition
belongs to the durable-stock framework rather than the current-flow aggregate.

## Construction notes

- Include operating costs and service expenditures.
- Exclude purchase of vehicles and other transport durables.
- Annualize periodic expenditures before summing to household level.

## Escalation triggers

- The survey includes a transport module but the observed expenses mix operating
  costs and vehicle purchases without a clear split.
- A reported value cannot be safely classified as consumption rather than stock
  acquisition.
