---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-sanitationsource
canonical_label: "Main toilet facility"
variable_name: sanitation_source
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: categorical

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "A flush toilet"
  - value: 2
    label: "A piped sewer system"
  - value: 3
    label: "A septic tank"
  - value: 4
    label: "Pit latrine"
  - value: 5
    label: "Ventilated improved pit latrine (VIP)"
  - value: 6
    label: "Pit latrine with slab"
  - value: 7
    label: "Composting toilet"
  - value: 8
    label: "Special case"
  - value: 9
    label: "A flush/pour flush to elsewhere"
  - value: 10
    label: "A pit latrine without slab"
  - value: 11
    label: "Bucket"
  - value: 12
    label: "Hanging toilet or hanging latrine"
  - value: 13
    label: "No facilities or bush or field"
  - value: 14
    label: "Other"
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
  []
derives_to:
  - VAR-impsanrec
# --- Country parameter declarations ---
country_parameters:
  - PARAM-WASH-SANITATION-CROSSWALK

# --- Correspondence output (machine-readable construction recipe) ---
correspondence_output:
  method: external_standard
  standard: "JMP-2025"
  level: sanitation_source
  map:
    "flush_and_pour_flush": [2, 3, 9]
    "flush_and_pour_flush.to_piped_sewer_system": 2
    "flush_and_pour_flush.to_septic_tank": 3
    "flush_and_pour_flush.to_unknown_place_not_sure_dk": 9
    "flush_and_pour_flush.to_elsewhere": 9
    "flush_toilets": [2, 3, 9]
    "flush_toilets.to_piped_sewer_system": 2
    "flush_toilets.to_septic_tank": 3
    "flush_toilets.to_unknown_place_not_sure_dk": 9
    "flush_toilets.to_elsewhere": 9
    "flush_toilets.private_flush_toilet": [2, 3, 9]
    "flush_toilets.private_flush_toilet.to_piped_sewer_system": 2
    "flush_toilets.private_flush_toilet.to_septic_tank": 3
    "flush_toilets.private_flush_toilet.to_unknown_place_not_sure_dk": 9
    "flush_toilets.private_flush_toilet.to_elsewhere": 9
    "flush_toilets.public_shared_flush_toilet": [2, 3, 9]
    "flush_toilets.public_shared_flush_toilet.to_piped_sewer_system": 2
    "flush_toilets.public_shared_flush_toilet.to_septic_tank": 3
    "flush_toilets.public_shared_flush_toilet.to_unknown_place_not_sure_dk": 9
    "flush_toilets.public_shared_flush_toilet.to_elsewhere": 9
    "latrines": [2, 3, 5, 6, 9, 10, 11, 12, 14]
    "latrines.pour_flush_latrines": [2, 3, 9]
    "latrines.pour_flush_latrines.to_piped_sewer_system": 2
    "latrines.pour_flush_latrines.to_septic_tank": 3
    "latrines.pour_flush_latrines.to_unknown_place_not_sure_dk": 9
    "latrines.pour_flush_latrines.to_elsewhere": 9
    "latrines.pour_flush_latrines.private_pour_flush_latrine": [2, 3, 9]
    "latrines.pour_flush_latrines.private_pour_flush_latrine.to_piped_sewer_system": 2
    "latrines.pour_flush_latrines.private_pour_flush_latrine.to_septic_tank": 3
    "latrines.pour_flush_latrines.private_pour_flush_latrine.to_unknown_place_not_sure_dk": 9
    "latrines.pour_flush_latrines.private_pour_flush_latrine.to_elsewhere": 9
    "latrines.pour_flush_latrines.public_shared_pour_flush_latrine": [2, 3, 9]
    "latrines.pour_flush_latrines.public_shared_pour_flush_latrine.to_piped_sewer_system": 2
    "latrines.pour_flush_latrines.public_shared_pour_flush_latrine.to_septic_tank": 3
    "latrines.pour_flush_latrines.public_shared_pour_flush_latrine.to_unknown_place_not_sure_dk": 9
    "latrines.pour_flush_latrines.public_shared_pour_flush_latrine.to_elsewhere": 9
    "latrines.dry_latrines": [5, 6, 10, 11, 12, 14]
    "latrines.dry_latrines.improved_latrines": [5, 6, 10, 11, 12, 14]
    "latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine": 5
    "latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine": 6
    "latrines.dry_latrines.improved_latrines.traditional_latrine": [6, 10]
    "latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit": 10
    "latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine": 12
    "latrines.dry_latrines.improved_latrines.bucket_latrine": 11
    "latrines.dry_latrines.improved_latrines.other": 14
    "latrines.dry_latrines.private_latrines": [5, 6, 10, 11, 12, 14]
    "latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine": 5
    "latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine": 6
    "latrines.dry_latrines.private_latrines.traditional_latrine": [6, 10]
    "latrines.dry_latrines.private_latrines.pit_latrine_without_slab_open_pit": 10
    "latrines.dry_latrines.private_latrines.hanging_toilet_hanging_latrine": 12
    "latrines.dry_latrines.private_latrines.bucket_latrine": 11
    "latrines.dry_latrines.private_latrines.other": 14
    "latrines.dry_latrines.public_shared_latrines": [5, 6, 10, 11, 12, 14]
    "latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine": 5
    "latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine": 6
    "latrines.dry_latrines.public_shared_latrines.traditional_latrine": [6, 10]
    "latrines.dry_latrines.public_shared_latrines.pit_latrine_without_slab_open_pit": 10
    "latrines.dry_latrines.public_shared_latrines.hanging_toilet_hanging_latrine": 12
    "latrines.dry_latrines.public_shared_latrines.bucket_latrine": 11
    "latrines.dry_latrines.public_shared_latrines.other": 14
    "composting_toilets": 7
    "composting_toilets.composting_toilet_private": 7
    "composting_toilets.composting_toilet_shared": 7
    "other_improved": 14
    "other_improved.other": 14
    "other_improved.other#2": 14
    "no_facility_bush_field": 13
    "other_unimproved": 14
    "other_unimproved.other": 14
    "other_unimproved.other#2": 14

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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), sanitation_source"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "2026-10-27 (proposed, pending GPID Team approval): added derives_to VAR-impsanrec (the
          guidelines: sanitation_source feeds imp_san_rec), PARAM-WASH-SANITATION-CROSSWALK (the
          national route), RULE-WASH-001, and correspondence_output (until now kept
          only in the survey-harmonization vendored copy).
          2026-10-28 (proposed): correspondence_output is the JMP-2025 anchor: each node of
          the JMP country-file sanitation tree (jmp_id, which the national categories carry) ->
          its sanitation_source code, transcribed from the gmd and spans fields of the JMP
          master tree (extraction/10_source/country-parameters-inputs, gmd_wash_concordance).
          A coarse node maps to the list of codes it spans. Flush/pour flush to pit has no
          sanitation_source code (imp_san_rec is set for it directly, VAR-impsanrec), so a
          coarse flush node lists 2, 3 and 9 only. It replaces the category_keyword placeholder."
---

## Definition

`sanitation_source` is a categorical variable that specifies the main source/facility of sanitation for the household, harmonized into fourteen standardized categories.

## Conceptual intent

It is the core WASH sanitation access indicator, distinguishing improved from unimproved facilities and feeding `sewer`, `open_def`, and `imp_san_rec`.

## Construction notes

Code from `sanitation_original` unless otherwise justified, referring to the survey questionnaire for the best match. If several toilet types are used, record only the main source. Apply the detailed definitions (e.g. flush toilet excludes pour-flush and flush to elsewhere).

## Consistency checks

- `sewer` equals 1 when the facility is a flush/pour flush to a piped sewer system.
- `imp_san_rec` equals 1 for improved facilities (flush/pour-flush to sewer, septic tank, or pit latrine; VIP; pit latrine with slab; composting toilet).

## Escalation triggers

- The survey uses a toilet category that does not map cleanly to any standardized code.
- A toilet is shared with other households, affecting improved-status determination.

## Common mistakes

- Coding a pour-flush toilet as a flush toilet.
- Treating bucket, hanging toilet, or no facility as improved.
- Not consulting the questionnaire and guessing the correspondence.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
| 2026-10-27 | 0.2     | Add derives_to VAR-impsanrec, PARAM-WASH-SANITATION-CROSSWALK, RULE-WASH-001 and correspondence_output | GPID Team (proposed) |
| 2026-10-28 | 0.3     | correspondence_output: JMP-2025 anchor (jmp_id -> sanitation_source code or span), replacing category_keyword; external_standards JMP | GPID Team (proposed) |
