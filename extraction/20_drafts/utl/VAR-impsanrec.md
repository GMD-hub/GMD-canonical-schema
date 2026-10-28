---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-impsanrec
canonical_label: "Improved sanitation facility"
variable_name: imp_san_rec
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: derived_preferred
data_type: binary

# --- Allowed output values ---
value_codes:
  - value: 0
    label: "No"
  - value: 1
    label: "Yes"
allowed_range: null
# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Information not available because the item was not collected in this survey"
  - code: ".o"
    label: "Other value not covered by harmonized codes"
# --- Derivation graph ---
derived_from:
  - VAR-sanitationsource
derives_to: []
# --- Country parameter declarations ---
country_parameters:
  - PARAM-WASH-SANITATION-CROSSWALK

# --- Correspondence output (machine-readable construction recipe) ---
correspondence_output:
  - method: recode
    from: VAR-sanitationsource
    map: {"2/3": 1, "5/7": 1, "9/14": 0}
  - method: external_standard
    standard: "JMP-2025"
    level: imp_san_rec
    map:
      "flush_and_pour_flush.to_pit": 1
      "flush_toilets.to_pit": 1
      "flush_toilets.private_flush_toilet.to_pit": 1
      "flush_toilets.public_shared_flush_toilet.to_pit": 1
      "latrines.pour_flush_latrines.to_pit": 1
      "latrines.pour_flush_latrines.private_pour_flush_latrine.to_pit": 1
      "latrines.pour_flush_latrines.public_shared_pour_flush_latrine.to_pit": 1

# --- Universe / skip gate ---
gates: []

# --- Cross-references ---
rules:
  - RULE-WASH-001
exceptions: []
external_standards:
  - name: "WHO/UNICEF JMP"
    url: https://washdata.org
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), imp_san_rec"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "2026-10-27 (proposed, pending GPID Team approval): imp_san_rec is derived from
          sanitation_source when the category reaches one fine code and set directly
          otherwise (RULE-WASH-001), so mapping_role atomic -> derived_preferred (the
          educat4 pattern) and derived_from VAR-sanitationsource. The recode map is the
          guidelines' consistency check; it replaces the category_keyword placeholder
          of the survey-harmonization vendored copy. Added PARAM-WASH-SANITATION-CROSSWALK
          (improved_flag on the national category serves the direct path).
          2026-10-28 (proposed): correspondence_output is a list: the recode from
          VAR-sanitationsource, then the direct path for the JMP-2025 nodes that have no
          sanitation_source code: flush/pour flush to pit (improved: the guidelines list
          flush/pour-flush to pit latrine)."
---

## Definition

`imp_san_rec` is a binary variable that estimates the recommended categorization of access to improved sanitation facilities in each country.

## Conceptual intent

It flags whether a household's sanitation facility is improved according to recommended access, minimizing expected misclassification and aligning with JMP/SDG monitoring.

## Construction notes

If the survey is on file in the SDG computations, set 1 if most of the problematic category was estimated improved at the rural level, otherwise 0. Otherwise base recommendations on standard international classifications and country insights; use 0 where there is no evidence.

## Consistency checks

- `imp_san_rec` equals 1 for improved facilities: flush/pour-flush to sewer, septic tank, or pit latrine; VIP; pit latrine with slab; composting toilet.
- Note: facilities shared with other households or open to the public are not considered improved.

## Escalation triggers

- A problematic facility category's improved status is disputed.
- No evidence exists for a problematic category and 0 is applied without documentation.

## Common mistakes

- Counting shared facilities as improved.
- Counting bucket, hanging toilet, flush to elsewhere, or no facility as improved.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
| 2026-10-27 | 0.2     | Derive from VAR-sanitationsource (recode correspondence_output); add PARAM-WASH-SANITATION-CROSSWALK and RULE-WASH-001 | GPID Team (proposed) |
| 2026-10-28 | 0.3     | correspondence_output list: recode from VAR-sanitationsource, then the JMP-2025 direct path | GPID Team (proposed) |
