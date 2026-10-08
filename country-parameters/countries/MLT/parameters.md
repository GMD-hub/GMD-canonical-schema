---
country_id: CTY-MLT
iso3: MLT
schema_version: '0.2'
status: draft
country_name: MLT
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MLT-EDU-01
    national_label_en: Primary Education
    national_label_local: Primary Education
    entry_age: 5
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 6
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - MLT-EDU-01
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: MLT-EDU-02
    national_label_en: Lower Secondary Education
    national_label_local: Lower Secondary Education
    entry_age: 11
    duration_years: 10
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 7
    parent_country_entry_ids:
    - MLT-EDU-01
    cum_years_schooling: 16
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-02
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLT-EDU-03
    national_label_en: Lower Secondary General Education
    national_label_local: Lower Secondary Education
    entry_age: 11
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 8
    parent_country_entry_ids:
    - MLT-EDU-01
    cum_years_schooling: 9
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLT-EDU-04
    national_label_en: Lower Secondary Vocational Education
    national_label_local: Lower Secondary Vocational Education
    entry_age: 16
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - MLT-EDU-01
    cum_years_schooling: 7
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLT-EDU-05
    national_label_en: Lower Secondary Vocational Education
    national_label_local: Lower Secondary Vocational Education
    entry_age: 16
    duration_years: 0
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - MLT-EDU-01
    cum_years_schooling: 6
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLT-EDU-06
    national_label_en: Introductory Certificate
    national_label_local: Introductory Certificate
    entry_age: 16
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - MLT-EDU-01
    cum_years_schooling: 7
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLT-EDU-07
    national_label_en: Upper Secondary General Education
    national_label_local: Upper Secondary Education
    entry_age: 14
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - MLT-EDU-02
    - MLT-EDU-03
    - MLT-EDU-04
    - MLT-EDU-05
    - MLT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
  - country_entry_id: MLT-EDU-08
    national_label_en: Higher Secondary Education
    national_label_local: Higher Secondary Education
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - MLT-EDU-02
    - MLT-EDU-03
    - MLT-EDU-04
    - MLT-EDU-05
    - MLT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
  - country_entry_id: MLT-EDU-09
    national_label_en: Higher Secondary education
    national_label_local: Higher Secondary Education
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - MLT-EDU-02
    - MLT-EDU-03
    - MLT-EDU-04
    - MLT-EDU-05
    - MLT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
  - country_entry_id: MLT-EDU-10
    national_label_en: Higher Secondary education
    national_label_local: Higher Secondary Education
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - MLT-EDU-02
    - MLT-EDU-03
    - MLT-EDU-04
    - MLT-EDU-05
    - MLT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
  - country_entry_id: MLT-EDU-11
    national_label_en: Higher Secondary education
    national_label_local: Higher Secondary Education
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - MLT-EDU-02
    - MLT-EDU-03
    - MLT-EDU-04
    - MLT-EDU-05
    - MLT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
  - country_entry_id: MLT-EDU-12
    national_label_en: Foundation Course
    national_label_local: Foundation Certificate
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 18
    parent_country_entry_ids:
    - MLT-EDU-02
    - MLT-EDU-03
    - MLT-EDU-04
    - MLT-EDU-05
    - MLT-EDU-06
    cum_years_schooling: 7
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
  - country_entry_id: MLT-EDU-13
    national_label_en: Secondary Education Certificate/ Diploma/Certificate/National
      Diploma/National Certificate
    national_label_local: Secondary Education Certificate/ Diploma/Certificate/National
      Diploma/National Certificate
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 19
    parent_country_entry_ids:
    - MLT-EDU-02
    - MLT-EDU-03
    - MLT-EDU-04
    - MLT-EDU-05
    - MLT-EDU-06
    cum_years_schooling: 7
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
  - country_entry_id: MLT-EDU-14
    national_label_en: National Diploma/Certificate
    national_label_local: National Diploma/Certificate
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 20
    parent_country_entry_ids:
    - MLT-EDU-02
    - MLT-EDU-03
    - MLT-EDU-04
    - MLT-EDU-05
    - MLT-EDU-06
    cum_years_schooling: 7
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
  - country_entry_id: MLT-EDU-15
    national_label_en: Certificate
    national_label_local: Certificate
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-16
    national_label_en: Certificate/Diploma
    national_label_local: Certificate/Diploma
    entry_age: 16
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-17
    national_label_en: Diploma/Higher National Diploma
    national_label_local: Diploma/Higher National Diploma
    entry_age: 18
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-18
    national_label_en: Diploma
    national_label_local: Diploma
    entry_age: 17
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-19
    national_label_en: Diploma/Higher National Diploma
    national_label_local: Diploma/Higher National Diploma
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 9
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-20
    national_label_en: Level 6 Diploma
    national_label_local: Diploma
    entry_age: 18
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-21
    national_label_en: Level 6 Diploma
    national_label_local: Diploma
    entry_age: 18
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-22
    national_label_en: Bachelors Degree
    national_label_local: Bachelors Degree
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 10
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-23
    national_label_en: Bachelors Degree
    national_label_local: Bachelors Degree
    entry_age: 20
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-24
    national_label_en: Bachelors Degree
    national_label_local: Bachelors Degree
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 10
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-25
    national_label_en: Bachelors Degree
    national_label_local: Bachelors Degree
    entry_age: 20
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-26
    national_label_en: Bachelors Degree
    national_label_local: Bachelors Degree
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 12
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-27
    national_label_en: Higher Diploma
    national_label_local: Higher Diploma
    entry_age: 21
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-28
    national_label_en: Post Graduate Certificate/Diploma
    national_label_local: Post Graduate Certificate/Diploma
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 34
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-29
    national_label_en: Post Graduate Certificate/Diploma
    national_label_local: Post Graduate Certificate/Diploma
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 35
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-30
    national_label_en: Bachelors Degree
    national_label_local: Bachelors Degree
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 36
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 12
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-31
    national_label_en: Bachelors Degree
    national_label_local: Bachelors Degree
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 37
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 12
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-32
    national_label_en: Masters Degree
    national_label_local: Masters Degree
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 38
    parent_country_entry_ids:
    - MLT-EDU-20
    - MLT-EDU-21
    - MLT-EDU-22
    - MLT-EDU-23
    - MLT-EDU-24
    - MLT-EDU-25
    - MLT-EDU-26
    - MLT-EDU-27
    cum_years_schooling: 9
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-20
    - MLT-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
    - 'minimum parent path selected from: MLT-EDU-20, MLT-EDU-21, MLT-EDU-22, MLT-EDU-23,
      MLT-EDU-24, MLT-EDU-25, MLT-EDU-26, MLT-EDU-27'
  - country_entry_id: MLT-EDU-33
    national_label_en: Masters Degree
    national_label_local: Masters Degree
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - MLT-EDU-20
    - MLT-EDU-21
    - MLT-EDU-22
    - MLT-EDU-23
    - MLT-EDU-24
    - MLT-EDU-25
    - MLT-EDU-26
    - MLT-EDU-27
    cum_years_schooling: 9
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-20
    - MLT-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
    - 'minimum parent path selected from: MLT-EDU-20, MLT-EDU-21, MLT-EDU-22, MLT-EDU-23,
      MLT-EDU-24, MLT-EDU-25, MLT-EDU-26, MLT-EDU-27'
  - country_entry_id: MLT-EDU-34
    national_label_en: Doctor of Laws
    national_label_local: Doctor of Laws
    entry_age: 21
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 40
    parent_country_entry_ids:
    - MLT-EDU-07
    - MLT-EDU-08
    - MLT-EDU-09
    - MLT-EDU-10
    - MLT-EDU-11
    - MLT-EDU-12
    - MLT-EDU-13
    - MLT-EDU-14
    cum_years_schooling: 10
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
  - country_entry_id: MLT-EDU-35
    national_label_en: Master of Laws
    national_label_local: Master of Laws
    entry_age: 24
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 41
    parent_country_entry_ids:
    - MLT-EDU-20
    - MLT-EDU-21
    - MLT-EDU-22
    - MLT-EDU-23
    - MLT-EDU-24
    - MLT-EDU-25
    - MLT-EDU-26
    - MLT-EDU-27
    cum_years_schooling: 9
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-20
    - MLT-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
    - 'minimum parent path selected from: MLT-EDU-20, MLT-EDU-21, MLT-EDU-22, MLT-EDU-23,
      MLT-EDU-24, MLT-EDU-25, MLT-EDU-26, MLT-EDU-27'
  - country_entry_id: MLT-EDU-36
    national_label_en: Master of Philosophy
    national_label_local: Master of Philosophy
    entry_age: 24
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 42
    parent_country_entry_ids:
    - MLT-EDU-20
    - MLT-EDU-21
    - MLT-EDU-22
    - MLT-EDU-23
    - MLT-EDU-24
    - MLT-EDU-25
    - MLT-EDU-26
    - MLT-EDU-27
    cum_years_schooling: 11
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-20
    - MLT-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
    - 'minimum parent path selected from: MLT-EDU-20, MLT-EDU-21, MLT-EDU-22, MLT-EDU-23,
      MLT-EDU-24, MLT-EDU-25, MLT-EDU-26, MLT-EDU-27'
  - country_entry_id: MLT-EDU-37
    national_label_en: Masters Degree
    national_label_local: Masters Degree
    entry_age: 24
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 43
    parent_country_entry_ids:
    - MLT-EDU-20
    - MLT-EDU-21
    - MLT-EDU-22
    - MLT-EDU-23
    - MLT-EDU-24
    - MLT-EDU-25
    - MLT-EDU-26
    - MLT-EDU-27
    cum_years_schooling: 10
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-20
    - MLT-EDU-37
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
    - 'minimum parent path selected from: MLT-EDU-20, MLT-EDU-21, MLT-EDU-22, MLT-EDU-23,
      MLT-EDU-24, MLT-EDU-25, MLT-EDU-26, MLT-EDU-27'
  - country_entry_id: MLT-EDU-38
    national_label_en: Masters Degree
    national_label_local: Masters Degree
    entry_age: 24
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 44
    parent_country_entry_ids:
    - MLT-EDU-20
    - MLT-EDU-21
    - MLT-EDU-22
    - MLT-EDU-23
    - MLT-EDU-24
    - MLT-EDU-25
    - MLT-EDU-26
    - MLT-EDU-27
    cum_years_schooling: 10
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-20
    - MLT-EDU-38
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
    - 'minimum parent path selected from: MLT-EDU-20, MLT-EDU-21, MLT-EDU-22, MLT-EDU-23,
      MLT-EDU-24, MLT-EDU-25, MLT-EDU-26, MLT-EDU-27'
  - country_entry_id: MLT-EDU-39
    national_label_en: PhD
    national_label_local: PhD
    entry_age: 24
    duration_years: 2
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 45
    parent_country_entry_ids:
    - MLT-EDU-28
    - MLT-EDU-29
    - MLT-EDU-30
    - MLT-EDU-31
    - MLT-EDU-32
    - MLT-EDU-33
    - MLT-EDU-34
    - MLT-EDU-35
    - MLT-EDU-36
    - MLT-EDU-37
    - MLT-EDU-38
    cum_years_schooling: 10
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-28
    - MLT-EDU-39
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
    - 'minimum parent path selected from: MLT-EDU-28, MLT-EDU-29, MLT-EDU-30, MLT-EDU-31,
      MLT-EDU-32, MLT-EDU-33, MLT-EDU-34, MLT-EDU-35, MLT-EDU-36, MLT-EDU-37, MLT-EDU-38'
  - country_entry_id: MLT-EDU-40
    national_label_en: PhD
    national_label_local: PhD
    entry_age: 24
    duration_years: 2
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 46
    parent_country_entry_ids:
    - MLT-EDU-28
    - MLT-EDU-29
    - MLT-EDU-30
    - MLT-EDU-31
    - MLT-EDU-32
    - MLT-EDU-33
    - MLT-EDU-34
    - MLT-EDU-35
    - MLT-EDU-36
    - MLT-EDU-37
    - MLT-EDU-38
    cum_years_schooling: 10
    cum_years_computation_path:
    - MLT-EDU-01
    - MLT-EDU-05
    - MLT-EDU-12
    - MLT-EDU-28
    - MLT-EDU-40
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLT-EDU-02, MLT-EDU-03, MLT-EDU-04, MLT-EDU-05,
      MLT-EDU-06'
    - 'minimum parent path selected from: MLT-EDU-07, MLT-EDU-08, MLT-EDU-09, MLT-EDU-10,
      MLT-EDU-11, MLT-EDU-12, MLT-EDU-13, MLT-EDU-14'
    - 'minimum parent path selected from: MLT-EDU-28, MLT-EDU-29, MLT-EDU-30, MLT-EDU-31,
      MLT-EDU-32, MLT-EDU-33, MLT-EDU-34, MLT-EDU-35, MLT-EDU-36, MLT-EDU-37, MLT-EDU-38'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Malta.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1990
  effective_to: null
  selectors: null
  value: 16
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

