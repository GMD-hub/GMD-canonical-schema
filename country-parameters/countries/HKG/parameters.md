---
country_id: CTY-HKG
iso3: HKG
schema_version: '0.2'
status: draft
country_name: HKG
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: HKG-EDU-01
    national_label_en: Kindergarten
    national_label_local: na
    entry_age: 3
    duration_years: 3
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
  - country_entry_id: HKG-EDU-02
    national_label_en: Primary 1 to 6 (Local curriculum)
    national_label_local: na
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - HKG-EDU-02
    cum_years_status: computed
    review_flags: []
  - country_entry_id: HKG-EDU-03
    national_label_en: Grade 1 to 6 (Non-local curriculum)
    national_label_local: na
    entry_age: 5
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
    - HKG-EDU-03
    cum_years_status: computed
    review_flags: []
  - country_entry_id: HKG-EDU-04
    national_label_en: Secondary 1 to 3 (Local curriculum)
    national_label_local: na
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - HKG-EDU-02
    - HKG-EDU-03
    cum_years_schooling: 9
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
  - country_entry_id: HKG-EDU-05
    national_label_en: Grade 7 to 9 (Non-local curriculum)
    national_label_local: na
    entry_age: 11
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - HKG-EDU-02
    - HKG-EDU-03
    cum_years_schooling: 9
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-05
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
  - country_entry_id: HKG-EDU-06
    national_label_en: Grade 10 to 11 (Non-local curriculum)
    national_label_local: na
    entry_age: 14
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - HKG-EDU-04
    - HKG-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
  - country_entry_id: HKG-EDU-07
    national_label_en: Secondary 4 to 6 (Local curriculum)
    national_label_local: na
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - HKG-EDU-04
    - HKG-EDU-05
    cum_years_schooling: 12
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
  - country_entry_id: HKG-EDU-08
    national_label_en: Grade 12 to 13 (Non-local curriculum)
    national_label_local: na
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - HKG-EDU-04
    - HKG-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
  - country_entry_id: HKG-EDU-09
    national_label_en: Diploma Yi Jin programme
    national_label_local: na
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - HKG-EDU-04
    - HKG-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
  - country_entry_id: HKG-EDU-10
    national_label_en: Certificate of Vocational Education (CVE) programmes
    national_label_local: na
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - HKG-EDU-04
    - HKG-EDU-05
    cum_years_schooling: 12
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
  - country_entry_id: HKG-EDU-11
    national_label_en: 'Certificate programmes

      offered by Hotel and Tourism Institute, International Culinary Institute and
      Chinese Culinary Institute of VTC'
    national_label_local: na
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 17
    parent_country_entry_ids:
    - HKG-EDU-04
    - HKG-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
  - country_entry_id: HKG-EDU-12
    national_label_en: 'Diploma / Advanced certificate / Advanced diploma

      (self-financing programmes by public-funded institutions)'
    national_label_local: na
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-13
    national_label_en: 'Certificate / Diploma programmes

      (non-local tertiary institutions)'
    national_label_local: na
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-14
    national_label_en: Diploma of Foundation Studies
    national_label_local: na
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-15
    national_label_en: Diploma of in Vocational Education (DVE) programmes
    national_label_local: na
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-16
    national_label_en: 'Diploma programmes

      offered by Hotel and Tourism Institute, International Culinary Institute and
      Chinese Culinary Institute of VTC'
    national_label_local: na
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-17
    national_label_en: Diploma programmes offered by the Hong Kong Academy for Performing
      Arts (HKAPA)
    national_label_local: na
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-18
    national_label_en: Certificate programmes offered by HKAPA
    national_label_local: na
    entry_age: 18
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-19
    national_label_en: 'Associate degree or Higher diploma

      (non-local tertiary institutions)'
    national_label_local: na
    entry_age: 18
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-20
    national_label_en: Associate degree or Higher diploma
    national_label_local: na
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-21
    national_label_en: Advanced Diploma offered by HKAPA
    national_label_local: na
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-22
    national_label_en: Bachelor's degree
    national_label_local: na
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 14
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-23
    national_label_en: Bachelor's degree (non-local institutions)
    national_label_local: na
    entry_age: 18
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-24
    national_label_en: Bachelor's degree  (continuation of sub-degree programmes)
    national_label_local: na
    entry_age: 20
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-25
    national_label_en: "Bachelor's degree (continuation of sub-degree programmes)\
      \ \n(non-local tertiary institutions)"
    national_label_local: na
    entry_age: 20
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-26
    national_label_en: Graduate certificate / Graduate diploma / Postgraduate certificate
      / Postgraduate diploma
    national_label_local: na
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - HKG-EDU-06
    - HKG-EDU-07
    - HKG-EDU-08
    - HKG-EDU-09
    - HKG-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
  - country_entry_id: HKG-EDU-27
    national_label_en: Master's degree
    national_label_local: na
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - HKG-EDU-22
    - HKG-EDU-23
    - HKG-EDU-24
    - HKG-EDU-25
    - HKG-EDU-26
    cum_years_schooling: 13
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-25
    - HKG-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
    - 'minimum parent path selected from: HKG-EDU-22, HKG-EDU-23, HKG-EDU-24, HKG-EDU-25,
      HKG-EDU-26'
  - country_entry_id: HKG-EDU-28
    national_label_en: Master of Philosophy
    national_label_local: na
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 34
    parent_country_entry_ids:
    - HKG-EDU-22
    - HKG-EDU-23
    - HKG-EDU-24
    - HKG-EDU-25
    - HKG-EDU-26
    cum_years_schooling: 13
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-25
    - HKG-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
    - 'minimum parent path selected from: HKG-EDU-22, HKG-EDU-23, HKG-EDU-24, HKG-EDU-25,
      HKG-EDU-26'
  - country_entry_id: HKG-EDU-29
    national_label_en: Doctorate degree
    national_label_local: na
    entry_age: 24
    duration_years: 2
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 35
    parent_country_entry_ids:
    - HKG-EDU-27
    - HKG-EDU-28
    cum_years_schooling: 15
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-25
    - HKG-EDU-27
    - HKG-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
    - 'minimum parent path selected from: HKG-EDU-22, HKG-EDU-23, HKG-EDU-24, HKG-EDU-25,
      HKG-EDU-26'
    - 'minimum parent path selected from: HKG-EDU-27, HKG-EDU-28'
  - country_entry_id: HKG-EDU-30
    national_label_en: Doctor of Philosophy
    national_label_local: na
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 36
    parent_country_entry_ids:
    - HKG-EDU-27
    - HKG-EDU-28
    cum_years_schooling: 16
    cum_years_computation_path:
    - HKG-EDU-02
    - HKG-EDU-04
    - HKG-EDU-09
    - HKG-EDU-25
    - HKG-EDU-27
    - HKG-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HKG-EDU-02, HKG-EDU-03'
    - 'minimum parent path selected from: HKG-EDU-04, HKG-EDU-05'
    - 'minimum parent path selected from: HKG-EDU-06, HKG-EDU-07, HKG-EDU-08, HKG-EDU-09,
      HKG-EDU-11'
    - 'minimum parent path selected from: HKG-EDU-22, HKG-EDU-23, HKG-EDU-24, HKG-EDU-25,
      HKG-EDU-26'
    - 'minimum parent path selected from: HKG-EDU-27, HKG-EDU-28'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_China,
      Hong Kong Special Administrative Region.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

