---
country_id: CTY-GIB
iso3: GIB
schema_version: '0.2'
status: draft
country_name: GIB
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: GIB-EDU-01
    national_label_en: 'Nursery (Private)

      Early Childhood Educational Development'
    national_label_local: 'Nursery (Private)

      Early Childhood Educational Development'
    entry_age: 0
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: GIB-EDU-02
    national_label_en: Nursery (Private)
    national_label_local: Nursery (Private)
    entry_age: 3
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: GIB-EDU-03
    national_label_en: Nursery (Government)
    national_label_local: Nursery (Government)
    entry_age: 3
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: GIB-EDU-04
    national_label_en: Reception
    national_label_local: Reception
    entry_age: 4
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: GIB-EDU-05
    national_label_en: Key Stage 1 (KS1)
    national_label_local: Key Stage 1
    entry_age: 5
    duration_years: 2
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 11
    parent_country_entry_ids: []
    cum_years_schooling: 2
    cum_years_computation_path:
    - GIB-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: GIB-EDU-06
    national_label_en: Key Stage 2 (KS2)
    national_label_local: Key Stage 2
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 12
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - GIB-EDU-06
    cum_years_status: computed
    review_flags: []
  - country_entry_id: GIB-EDU-07
    national_label_en: Key Stage 3 (KS3)
    national_label_local: Key Stage 3
    entry_age: 11
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - GIB-EDU-05
    - GIB-EDU-06
    cum_years_schooling: 5
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    cum_years_status: computed
    review_flags: &id001
    - 'minimum parent path selected from: GIB-EDU-05, GIB-EDU-06'
  - country_entry_id: GIB-EDU-08
    national_label_en: GCSE
    national_label_local: GCSE (General Certificate of Secondary Education)
    entry_age: 14
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - GIB-EDU-07
    cum_years_schooling: 7
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: GIB-EDU-09
    national_label_en: AS Level
    national_label_local: AS Level
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - GIB-EDU-07
    cum_years_schooling: 6
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: GIB-EDU-10
    national_label_en: A Level
    national_label_local: A Level
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - GIB-EDU-07
    cum_years_schooling: 7
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: GIB-EDU-11
    national_label_en: NVQ Level 1
    national_label_local: NVQ Level 1
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - GIB-EDU-07
    cum_years_schooling: 6
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: GIB-EDU-12
    national_label_en: NVQ Level 2
    national_label_local: NVQ Level 2
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - GIB-EDU-07
    cum_years_schooling: 6
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: GIB-EDU-13
    national_label_en: NVQ Level 3
    national_label_local: NVQ Level 3
    entry_age: 18
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - GIB-EDU-08
    - GIB-EDU-09
    - GIB-EDU-10
    - GIB-EDU-11
    - GIB-EDU-12
    cum_years_schooling: 7
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-09
    - GIB-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GIB-EDU-05, GIB-EDU-06'
    - 'minimum parent path selected from: GIB-EDU-08, GIB-EDU-09, GIB-EDU-10, GIB-EDU-11,
      GIB-EDU-12'
  - country_entry_id: GIB-EDU-14
    national_label_en: NVQ Level 4
    national_label_local: NVQ Level 4
    entry_age: 20
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - GIB-EDU-08
    - GIB-EDU-09
    - GIB-EDU-10
    - GIB-EDU-11
    - GIB-EDU-12
    cum_years_schooling: 7
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-09
    - GIB-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GIB-EDU-05, GIB-EDU-06'
    - 'minimum parent path selected from: GIB-EDU-08, GIB-EDU-09, GIB-EDU-10, GIB-EDU-11,
      GIB-EDU-12'
  - country_entry_id: GIB-EDU-15
    national_label_en: Bachelor's Degree
    national_label_local: Bachelor's Degree
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - GIB-EDU-08
    - GIB-EDU-09
    - GIB-EDU-10
    - GIB-EDU-11
    - GIB-EDU-12
    cum_years_schooling: 9
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-09
    - GIB-EDU-15
    cum_years_status: computed
    review_flags: &id002
    - 'minimum parent path selected from: GIB-EDU-05, GIB-EDU-06'
    - 'minimum parent path selected from: GIB-EDU-08, GIB-EDU-09, GIB-EDU-10, GIB-EDU-11,
      GIB-EDU-12'
  - country_entry_id: GIB-EDU-16
    national_label_en: Post -graduate diplomas and certificates
    national_label_local: Post -graduate diplomas and certificates
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - GIB-EDU-08
    - GIB-EDU-09
    - GIB-EDU-10
    - GIB-EDU-11
    - GIB-EDU-12
    cum_years_schooling: 7
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-09
    - GIB-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GIB-EDU-05, GIB-EDU-06'
    - 'minimum parent path selected from: GIB-EDU-08, GIB-EDU-09, GIB-EDU-10, GIB-EDU-11,
      GIB-EDU-12'
  - country_entry_id: GIB-EDU-17
    national_label_en: Master's  Degree
    national_label_local: Master's  Degree
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - GIB-EDU-15
    cum_years_schooling: 10
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-09
    - GIB-EDU-15
    - GIB-EDU-17
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: GIB-EDU-18
    national_label_en: Doctorate
    national_label_local: Doctorate
    entry_age: 23
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - GIB-EDU-16
    - GIB-EDU-17
    cum_years_schooling: 10
    cum_years_computation_path:
    - GIB-EDU-05
    - GIB-EDU-07
    - GIB-EDU-09
    - GIB-EDU-16
    - GIB-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GIB-EDU-05, GIB-EDU-06'
    - 'minimum parent path selected from: GIB-EDU-08, GIB-EDU-09, GIB-EDU-10, GIB-EDU-11,
      GIB-EDU-12'
    - 'minimum parent path selected from: GIB-EDU-16, GIB-EDU-17'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Gib.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

