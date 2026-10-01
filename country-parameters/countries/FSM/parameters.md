---
country_id: CTY-FSM
iso3: FSM
schema_version: '0.2'
status: draft
country_name: FSM
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: FSM-EDU-01
    national_label_en: Pre-School
    national_label_local: Pre-School
    entry_age: 3
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
  - country_entry_id: FSM-EDU-02
    national_label_en: ECE/kindergarten
    national_label_local: ECE/kindergarten
    entry_age: 5
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
  - country_entry_id: FSM-EDU-03
    national_label_en: Elementary Education (Grades 1 - 6)
    national_label_local: Elementary Education (Grades 1 - 6)
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - FSM-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: FSM-EDU-04
    national_label_en: Elementary Education (Grades 7-8)
    national_label_local: Elementary Education (Grades 7-8)
    entry_age: 12
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - FSM-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FSM-EDU-05
    national_label_en: High School
    national_label_local: High School
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - FSM-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    - FSM-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FSM-EDU-06
    national_label_en: High School Vocational/Life Skills Programme
    national_label_local: High School Vocational/Life Skills Programme
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - FSM-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    - FSM-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FSM-EDU-07
    national_label_en: T3 Vocational/Life Skills Programme
    national_label_local: T3 Vocational/Life Skills Programme
    entry_age: 14
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - FSM-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    - FSM-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FSM-EDU-08
    national_label_en: College of Micronesia Teacher Preparation Program
    national_label_local: College of Micronesia Teacher Preparation Program
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - FSM-EDU-05
    cum_years_schooling: 14
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    - FSM-EDU-05
    - FSM-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FSM-EDU-09
    national_label_en: College of Micronesia Certificates
    national_label_local: College of Micronesia Certificates
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - FSM-EDU-05
    cum_years_schooling: 14
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    - FSM-EDU-05
    - FSM-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FSM-EDU-10
    national_label_en: FSM Maritime Institute Certificate
    national_label_local: FSM Maritime Institute Certificate
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - FSM-EDU-05
    cum_years_schooling: 14
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    - FSM-EDU-05
    - FSM-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FSM-EDU-11
    national_label_en: College of Micronesia Associate of Arts or Science Degrees
    national_label_local: College of Micronesia Associate of Arts or Science Degrees
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - FSM-EDU-05
    cum_years_schooling: 14
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    - FSM-EDU-05
    - FSM-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FSM-EDU-12
    national_label_en: Third Year Program
    national_label_local: Third Year Program
    entry_age: 20
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - FSM-EDU-05
    cum_years_schooling: 13
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    - FSM-EDU-05
    - FSM-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FSM-EDU-13
    national_label_en: Bachelor Degrees by distance
    national_label_local: Bachelor Degrees by distance
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - FSM-EDU-05
    cum_years_schooling: 16
    cum_years_computation_path:
    - FSM-EDU-03
    - FSM-EDU-04
    - FSM-EDU-05
    - FSM-EDU-13
    cum_years_status: computed
    review_flags: *id001
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Micronesia
      (Federated States of).xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

