---
country_id: CTY-IRL
iso3: IRL
schema_version: '0.2'
status: draft
country_name: IRL
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: IRL-EDU-01
    national_label_en: Early start
    national_label_local: Early start
    entry_age: 3
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 5
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: IRL-EDU-02
    national_label_en: Privately provided Pre-Primary education - Early Childhood
      Care and Education (ECCE) Scheme and the Community Childcare Subvention (CCS)
      Programme
    national_label_local: Privately provided Pre-Primary education - Early Childhood
      Care and Education (ECCE) Scheme and the Community Childcare Subvention (CCS)
      Programme
    entry_age: 0
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 6
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: IRL-EDU-03
    national_label_en: Primary Education
    national_label_local: Primary Education
    entry_age: 4
    duration_years: 8
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 8
    cum_years_computation_path:
    - IRL-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: IRL-EDU-04
    national_label_en: Adult Literacy Programme
    national_label_local: Adult Literacy Programme
    entry_age: 0
    duration_years: 1
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 1
    cum_years_computation_path:
    - IRL-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: IRL-EDU-05
    national_label_en: Community Training Centres
    national_label_local: Community Education
    entry_age: 0
    duration_years: 0
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - IRL-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRL-EDU-06
    national_label_en: Bridging/Foundation
    national_label_local: Bridging/Foundation
    entry_age: 0
    duration_years: 0
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - IRL-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRL-EDU-07
    national_label_en: Specialist Training Providers
    national_label_local: Specialist Training Providers
    entry_age: 0
    duration_years: 0
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - IRL-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRL-EDU-08
    national_label_en: European and Other Initiatives
    national_label_local: European and Other Initiatives
    entry_age: 0
    duration_years: 0
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - IRL-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRL-EDU-09
    national_label_en: Junior Certificate
    national_label_local: Junior Certificate
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - IRL-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRL-EDU-10
    national_label_en: Junior Certificate Schools Programme
    national_label_local: Junior Certificate Schools Programme
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - IRL-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRL-EDU-11
    national_label_en: Transition Year Programme
    national_label_local: Transition Year Programme
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - IRL-EDU-05
    - IRL-EDU-06
    - IRL-EDU-07
    - IRL-EDU-08
    - IRL-EDU-09
    - IRL-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
  - country_entry_id: IRL-EDU-12
    national_label_en: Leaving Certificate Applied
    national_label_local: Leaving Certificate Applied
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - IRL-EDU-05
    - IRL-EDU-06
    - IRL-EDU-07
    - IRL-EDU-08
    - IRL-EDU-09
    - IRL-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
  - country_entry_id: IRL-EDU-13
    national_label_en: Leaving Certificate Vocational Programme
    national_label_local: Leaving Certificate Vocational Programme
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - IRL-EDU-05
    - IRL-EDU-06
    - IRL-EDU-07
    - IRL-EDU-08
    - IRL-EDU-09
    - IRL-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
  - country_entry_id: IRL-EDU-14
    national_label_en: Leaving Certificate (Established)
    national_label_local: Leaving Certificate (Established)
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - IRL-EDU-05
    - IRL-EDU-06
    - IRL-EDU-07
    - IRL-EDU-08
    - IRL-EDU-09
    - IRL-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
  - country_entry_id: IRL-EDU-15
    national_label_en: Local Training Initiatives
    national_label_local: Local Training Initiatives
    entry_age: 0
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - IRL-EDU-05
    - IRL-EDU-06
    - IRL-EDU-07
    - IRL-EDU-08
    - IRL-EDU-09
    - IRL-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
  - country_entry_id: IRL-EDU-16
    national_label_en: Specific Skills Training
    national_label_local: Specific Skills Training
    entry_age: 0
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - IRL-EDU-05
    - IRL-EDU-06
    - IRL-EDU-07
    - IRL-EDU-08
    - IRL-EDU-09
    - IRL-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
  - country_entry_id: IRL-EDU-17
    national_label_en: Traineeship
    national_label_local: Traineeship
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - IRL-EDU-05
    - IRL-EDU-06
    - IRL-EDU-07
    - IRL-EDU-08
    - IRL-EDU-09
    - IRL-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
  - country_entry_id: IRL-EDU-18
    national_label_en: Secretarial/Technical Training Programme
    national_label_local: Secretarial/Technical Training Programme
    entry_age: 17
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 10
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-19
    national_label_en: Apprenticeship
    national_label_local: Apprenticeship
    entry_age: 16
    duration_years: 4
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 13
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-20
    national_label_en: PLC
    national_label_local: Post Leaving Certificate Programmes
    entry_age: 0
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 10
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-21
    national_label_en: Momentum
    national_label_local: Momentum
    entry_age: 0
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 9
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-22
    national_label_en: Higher Certificate
    national_label_local: Higher Certificate
    entry_age: 17
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 11
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-23
    national_label_en: Higher Certificate
    national_label_local: Higher Certificate
    entry_age: 17
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 11
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-24
    national_label_en: University Certificate (University)
    national_label_local: University Certificate (University)
    entry_age: 17
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 10
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-25
    national_label_en: University Diploma (University)
    national_label_local: University Diploma (University)
    entry_age: 17
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 11
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-26
    national_label_en: Ordinary Bachelor Degree
    national_label_local: Ordinary Bachelor Degree
    entry_age: 17
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 12
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-27
    national_label_en: Honours Bachelor Degree
    national_label_local: Honours Bachelor Degree
    entry_age: 17
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 34
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 12
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-28
    national_label_en: Higher Diploma
    national_label_local: Higher Diploma/ Graduate Diploma (Conversion)
    entry_age: 21
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 35
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 10
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-29
    national_label_en: Post-Graduate Diploma
    national_label_local: Post-Graduate Diploma
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 36
    parent_country_entry_ids:
    - IRL-EDU-11
    - IRL-EDU-12
    - IRL-EDU-14
    - IRL-EDU-15
    - IRL-EDU-16
    - IRL-EDU-17
    cum_years_schooling: 10
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
  - country_entry_id: IRL-EDU-30
    national_label_en: Masters Degree
    national_label_local: Masters Degree
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 37
    parent_country_entry_ids:
    - IRL-EDU-26
    - IRL-EDU-27
    - IRL-EDU-28
    cum_years_schooling: 11
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-28
    - IRL-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
    - 'minimum parent path selected from: IRL-EDU-26, IRL-EDU-27, IRL-EDU-28'
  - country_entry_id: IRL-EDU-31
    national_label_en: Doctoral Degree
    national_label_local: Doctoral Degree
    entry_age: 22
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 38
    parent_country_entry_ids:
    - IRL-EDU-29
    - IRL-EDU-30
    cum_years_schooling: 13
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-29
    - IRL-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
    - 'minimum parent path selected from: IRL-EDU-29, IRL-EDU-30'
  - country_entry_id: IRL-EDU-32
    national_label_en: Higher Doctorate
    national_label_local: Higher Doctorate
    entry_age: 0
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - IRL-EDU-29
    - IRL-EDU-30
    cum_years_schooling: 13
    cum_years_computation_path:
    - IRL-EDU-03
    - IRL-EDU-05
    - IRL-EDU-11
    - IRL-EDU-29
    - IRL-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRL-EDU-05, IRL-EDU-06, IRL-EDU-07, IRL-EDU-08,
      IRL-EDU-09, IRL-EDU-10'
    - 'minimum parent path selected from: IRL-EDU-11, IRL-EDU-12, IRL-EDU-14, IRL-EDU-15,
      IRL-EDU-16, IRL-EDU-17'
    - 'minimum parent path selected from: IRL-EDU-29, IRL-EDU-30'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Ireland.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

