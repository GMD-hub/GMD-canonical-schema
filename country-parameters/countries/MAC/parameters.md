---
country_id: CTY-MAC
iso3: MAC
schema_version: '0.2'
status: draft
country_name: MAC
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MAC-EDU-01
    national_label_en: Infant education
    national_label_local: "\u5E7C\u5152\u6559\u80B2\nEnsino infantil"
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
  - country_entry_id: MAC-EDU-02
    national_label_en: Primary education
    national_label_local: "\u5C0F\u5B78\u6559\u80B2\nEnsino prim\xE1rio"
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
    - MAC-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: MAC-EDU-03
    national_label_en: Junior secondary education
    national_label_local: "\u521D\u4E2D\u6559\u80B2\nEnsino secund\xE1rio geral"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - MAC-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAC-EDU-04
    national_label_en: Senior secondary education
    national_label_local: "\u9AD8\u4E2D\u6559\u80B2\nEnsino secund\xE1rio complementar"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - MAC-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAC-EDU-05
    national_label_en: Senior secondary education (Courses of vocational and technical
      education)
    national_label_local: "\u9AD8\u4E2D\u6559\u80B2\uFF08\u8077\u696D\u6280\u8853\u6559\
      \u80B2\u8AB2\u7A0B\uFF09\nEnsino secund\xE1rio complementar (cursos do ensino\
      \ t\xE9cnico-profissional)"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - MAC-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAC-EDU-06
    national_label_en: Senior secondary education (Courses of vocational and technical
      education)
    national_label_local: "\u9AD8\u4E2D\u6559\u80B2\uFF08\u8077\u696D\u6280\u8853\u6559\
      \u80B2\u8AB2\u7A0B\uFF09\nEnsino secund\xE1rio complementar (cursos do ensino\
      \ t\xE9cnico-profissional)"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - MAC-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAC-EDU-07
    national_label_en: Higher education diploma programme (2 years)
    national_label_local: "\u9AD8\u7B49\u6559\u80B2\u6587\u6191\nDiploma de ensino\
      \ superior"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
    parent_country_entry_ids:
    - MAC-EDU-04
    cum_years_schooling: 14
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-04
    - MAC-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAC-EDU-08
    national_label_en: "Bacharelato \nprogramme (3 years)"
    national_label_local: "\u9AD8\u7B49\u5C08\u79D1\u5B78\u4F4D\nBacharelato"
    entry_age: 17
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - MAC-EDU-04
    cum_years_schooling: 15
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-04
    - MAC-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAC-EDU-09
    national_label_en: Bachelor's degree programme (4 years)
    national_label_local: "\u5B78\u58EB\u5B78\u4F4D\nLicenciatura"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - MAC-EDU-04
    cum_years_schooling: 16
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-04
    - MAC-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAC-EDU-10
    national_label_en: Bachelor's degree programme  (5 years)
    national_label_local: "\u5B78\u58EB\u5B78\u4F4D\nLicenciatura"
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - MAC-EDU-04
    cum_years_schooling: 17
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-04
    - MAC-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAC-EDU-11
    national_label_en: Master's degree programme
    national_label_local: "\u78A9\u58EB\u5B78\u4F4D\nMestrado"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - MAC-EDU-09
    - MAC-EDU-10
    cum_years_schooling: 18
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-04
    - MAC-EDU-09
    - MAC-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAC-EDU-09, MAC-EDU-10'
  - country_entry_id: MAC-EDU-12
    national_label_en: Postgraduate diploma programme
    national_label_local: "\u5B78\u4F4D\u5F8C\u6587\u6191\nDiploma de P\xF3s-Gradua\xE7\
      \xE3o"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - MAC-EDU-04
    cum_years_schooling: 13
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-04
    - MAC-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAC-EDU-13
    national_label_en: Doctor's degree programme
    national_label_local: "\u535A\u58EB\u5B78\u4F4D\nDoutoramente"
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - MAC-EDU-11
    - MAC-EDU-12
    cum_years_schooling: 16
    cum_years_computation_path:
    - MAC-EDU-02
    - MAC-EDU-03
    - MAC-EDU-04
    - MAC-EDU-12
    - MAC-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAC-EDU-11, MAC-EDU-12'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_China,
      Macao Special Administrative Region.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

