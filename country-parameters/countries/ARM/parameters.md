---
country_id: CTY-ARM
iso3: ARM
schema_version: '0.2'
status: draft
country_name: ARM
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ARM-EDU-01
    national_label_en: Pre-primary
    national_label_local: "\u0546\u0561\u056D\u0561\u0564\u057A\u0580\u0578\u0581\u0561\
      \u056F\u0561\u0576 \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0578\u0582\u0576"
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
  - country_entry_id: ARM-EDU-02
    national_label_en: Primary general education
    national_label_local: "\u054F\u0561\u0580\u0580\u0561\u056F\u0561\u0576 \u0568\
      \u0576\u0564\u0570\u0561\u0576\u0578\u0582\u0580 \u056F\u0580\u0569\u0578\u0582\
      \u0569\u0575\u0578\u0582\u0576"
    entry_age: 6
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - ARM-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: ARM-EDU-03
    national_label_en: Basic general education (1st stage of secondary education)
    national_label_local: "\u0540\u056B\u0574\u0576\u0561\u056F\u0561\u0576 \u0568\
      \u0576\u0564\u0570\u0561\u0576\u0578\u0582\u0580 \u056F\u0580\u0569\u0578\u0582\
      \u0569\u0575\u0578\u0582\u0576 (\u0574\u056B\u057B\u0576\u0561\u056F\u0561\u0580\
      \u0563 \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0561\u0576 1-\u056B\u0576\
      \ \u0574\u0561\u056F\u0561\u0580\u0564\u0561\u056F)"
    entry_age: 10
    duration_years: 5
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - ARM-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARM-EDU-04
    national_label_en: Secondary general education (2nd stage of secondary education)
    national_label_local: "\u0544\u056B\u057B\u0576\u0561\u056F\u0561\u0580\u0563\
      \ \u0568\u0576\u0564\u0570\u0561\u0576\u0578\u0582\u0580 \u056F\u0580\u0569\u0578\
      \u0582\u0569\u0575\u0578\u0582\u0576 (\u0574\u056B\u057B\u0576\u0561\u056F\u0561\
      \u0580\u0563 \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0561\u0576 2-\u0580\
      \u0564 \u0574\u0561\u056F\u0561\u0580\u0564\u0561\u056F)"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - ARM-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARM-EDU-05
    national_label_en: Initial vocational (handicraft) training, long programme
    national_label_local: "\u0546\u0561\u056D\u0576\u0561\u056F\u0561\u0576 \u0574\
      \u0561\u057D\u0576\u0561\u0563\u056B\u057F\u0561\u056F\u0561\u0576 (\u0561\u0580\
      \u0570\u0565\u057D\u057F\u0561\u0563\u0578\u0580\u056E\u0561\u056F\u0561\u0576\
      ) \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0578\u0582\u0576"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - ARM-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARM-EDU-06
    national_label_en: Advanced vocational education on the basis of general basic
      education (Grades 1-2)
    national_label_local: "\u0544\u056B\u057B\u056B\u0576 \u0574\u0561\u057D\u0576\
      \u0561\u0563\u056B\u057F\u0561\u056F\u0561\u0576 \u056F\u0580\u0569\u0578\u0582\
      \u0569\u0575\u0578\u0582\u0576 \u0570\u056B\u0574\u0576\u0561\u056F\u0561\u0576\
      \ \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0561\u0576 \u0570\u056B\u0574\u0584\
      \u056B \u057E\u0580\u0561"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - ARM-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARM-EDU-07
    national_label_en: Advanced vocational education on the basis of general basic
      education (Grades 3-4/5)
    national_label_local: "\u0544\u056B\u057B\u056B\u0576 \u0574\u0561\u057D\u0576\
      \u0561\u0563\u056B\u057F\u0561\u056F\u0561\u0576 \u056F\u0580\u0569\u0578\u0582\
      \u0569\u0575\u0578\u0582\u0576 \u0570\u056B\u0574\u0576\u0561\u056F\u0561\u0576\
      \ \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0561\u0576 \u0570\u056B\u0574\u0584\
      \u056B \u057E\u0580\u0561"
    entry_age: 17
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
    parent_country_entry_ids:
    - ARM-EDU-04
    cum_years_schooling: 14
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-04
    - ARM-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARM-EDU-08
    national_label_en: Advanced vocational education on the basis of secondary general
      education
    national_label_local: "\u0544\u0561\u057D\u0576\u0561\u0563\u056B\u057F\u0561\u056F\
      \u0561\u0576 \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0578\u0582\u0576  \u0574\
      \u056B\u057B\u0576\u0561\u056F\u0561\u0580\u0563 \u0568\u0576\u0564\u0570\u0561\
      \u0576\u0578\u0582\u0580 \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0561\u0576\
      \ \u0570\u056B\u0574\u0561\u0576 \u057E\u0580\u0561"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - ARM-EDU-04
    cum_years_schooling: 14
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-04
    - ARM-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARM-EDU-09
    national_label_en: "Bachelor\u2019s degree education programme"
    national_label_local: "\u0532\u0561\u056F\u0561\u056C\u0561\u057E\u0580\u056B\
      \ \u0561\u057D\u057F\u056B\u0573\u0561\u0576 \u056F\u0580\u0569\u0561\u056F\u0561\
      \u0576 \u056E\u0580\u0561\u0563\u056B\u0580\u0568"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - ARM-EDU-04
    cum_years_schooling: 16
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-04
    - ARM-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARM-EDU-10
    national_label_en: Long first degree tertiary programme, leading to a specialist
      diploma
    national_label_local: "\u0535\u0580\u0580\u0578\u0580\u0564\u0561\u0575\u056B\u0576\
      \ \u056E\u0580\u0561\u0563\u0580\u056B \u0565\u0580\u056F\u0561\u0580 \u0561\
      \u057C\u0561\u057B\u056B\u0576 \u0561\u057D\u057F\u056B\u0573\u0561\u0576\u0568\
      ` \u0564\u056B\u057A\u056C\u0578\u0574\u0561\u057E\u0578\u0580\u057E\u0561\u056E\
      \ \u0574\u0561\u057D\u0576\u0561\u0563\u0565\u057F"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - ARM-EDU-04
    cum_years_schooling: 17
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-04
    - ARM-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARM-EDU-11
    national_label_en: Master's degree
    national_label_local: "\u0544\u0561\u0563\u056B\u057D\u057F\u0580\u0578\u057D\u056B\
      \ \u0561\u057D\u057F\u056B\u0573\u0561\u0576"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - ARM-EDU-09
    cum_years_schooling: 18
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-04
    - ARM-EDU-09
    - ARM-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARM-EDU-12
    national_label_en: Postgraduate education, kandidat nauk programme
    national_label_local: "\u0540\u0565\u057F\u0562\u0578\u0582\u0570\u0561\u056F\u0561\
      \u0576 \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0578\u0582\u0576, \u0563\u056B\
      \u057F\u0578\u0582\u0569\u0575\u0578\u0582\u0576\u0576\u0565\u0580\u056B \u0569\
      \u0565\u056F\u0576\u0561\u056E\u0578\u0582"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - ARM-EDU-10
    - ARM-EDU-11
    cum_years_schooling: 20
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-04
    - ARM-EDU-10
    - ARM-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ARM-EDU-10, ARM-EDU-11'
  - country_entry_id: ARM-EDU-13
    national_label_en: Postgraduate education, doktor nauk programme
    national_label_local: "\u0540\u0565\u057F\u0562\u0578\u0582\u0570\u0561\u056F\u0561\
      \u0576 \u056F\u0580\u0569\u0578\u0582\u0569\u0575\u0578\u0582\u0576,  \u0563\
      \u056B\u057F\u0578\u0582\u0569\u0575\u0578\u0582\u0576\u0576\u0565\u0580\u056B\
      \ \u0564\u0578\u056F\u057F\u0578\u0580"
    entry_age: 27
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - ARM-EDU-10
    - ARM-EDU-11
    cum_years_schooling: 20
    cum_years_computation_path:
    - ARM-EDU-02
    - ARM-EDU-03
    - ARM-EDU-04
    - ARM-EDU-10
    - ARM-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ARM-EDU-10, ARM-EDU-11'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Armenia.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ARM-SUBNAT-01
    survey_labels: 1 - Yerevan | 1-Yerevan
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_464
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_464
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '464'
    geo_nvar: ADM1_NAME
    geo_name: Yerevan
    source_row: 267
  - country_entry_id: ARM-SUBNAT-02
    survey_labels: 10 - Vayots Dzor | 10-Vayots Dzor
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_463
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_463
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '463'
    geo_nvar: ADM1_NAME
    geo_name: Vayots Dzor
    source_row: 268
  - country_entry_id: ARM-SUBNAT-03
    survey_labels: 11 - Tavush | 11-Tavush
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_462
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_462
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '462'
    geo_nvar: ADM1_NAME
    geo_name: Tavush
    source_row: 269
  - country_entry_id: ARM-SUBNAT-04
    survey_labels: 2 - Aragatsotn | 2-Aragatsotn
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_453
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_453
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '453'
    geo_nvar: ADM1_NAME
    geo_name: Aragatsotn
    source_row: 270
  - country_entry_id: ARM-SUBNAT-05
    survey_labels: 3 - Arara | 3 - Ararat | 3-Ararat
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_454
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_454
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '454'
    geo_nvar: ADM1_NAME
    geo_name: Ararat
    source_row: 271
  - country_entry_id: ARM-SUBNAT-06
    survey_labels: 4 - Armavir | 4-Armavir
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_455
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_455
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '455'
    geo_nvar: ADM1_NAME
    geo_name: Armavir
    source_row: 272
  - country_entry_id: ARM-SUBNAT-07
    survey_labels: 5 - Gegharkunik | 5-Gegharkunik
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_456
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_456
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '456'
    geo_nvar: ADM1_NAME
    geo_name: Gergharkunik
    source_row: 273
  - country_entry_id: ARM-SUBNAT-08
    survey_labels: 6 - Lori | 6-Lori
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_458
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_458
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '458'
    geo_nvar: ADM1_NAME
    geo_name: Lori
    source_row: 274
  - country_entry_id: ARM-SUBNAT-09
    survey_labels: 7 - Kotayk | 7-Kotayk
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_457
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_457
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '457'
    geo_nvar: ADM1_NAME
    geo_name: Kotayk
    source_row: 275
  - country_entry_id: ARM-SUBNAT-10
    survey_labels: 8 - Shirak | 8-Shirak
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_460
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_460
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '460'
    geo_nvar: ADM1_NAME
    geo_name: Shirak
    source_row: 276
  - country_entry_id: ARM-SUBNAT-11
    survey_labels: 9 - Sjunik | 9-Sjunik
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: ARM_2015_GAUL1_461
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARM_2015_GAUL1_461
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '461'
    geo_nvar: ADM1_NAME
    geo_name: Syunik
    source_row: 277
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ARM-SAN-01
    source_category_code: flush_pour_type_toilet_connected_elsewhere_connection_unknown
    national_label_en: flush / pour type toilet connected elsewhere/ connection unknown
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: ARM-SAN-02
    source_category_code: flush_pour_type_toilet_connected_to_piped_sewer_system
    national_label_en: flush / pour type toilet connected to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: ARM-SAN-03
    source_category_code: sewerage_system
    national_label_en: sewerage system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: ARM-SAN-04
    source_category_code: flush_pour_type_toilet_connected_to_pit_latrine
    national_label_en: flush / pour type toilet connected to pit latrine
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: ARM-SAN-05
    source_category_code: flush_pour_type_toilet_connected_to_septic_tank
    national_label_en: flush / pour type toilet connected to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: ARM-SAN-06
    source_category_code: a_inside_house_and_exclusive
    national_label_en: "\xC2\_Inside house and exclusive"
    national_label_local: "\u0421\u043E\u0431\u0441\u0442\u0432\u0435\u043D\u043D\u044B\
      \u0439 \u0442\u0443\u0430\u043B\u0435\u0442 \u0441\u043E \u0441\u043C\u044B\u0432\
      \u043E\u043C"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: ARM-SAN-07
    source_category_code: own_flush_toilet
    national_label_en: Own flush toilet
    national_label_local: "\u0421\u043E\u0431\u0441\u0442\u0432\u0435\u043D\u043D\u044B\
      \u0439 \u0442\u0443\u0430\u043B\u0435\u0442 \u0441\u043E \u0441\u043C\u044B\u0432\
      \u043E\u043C"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: ARM-SAN-08
    source_category_code: a_inside_house_and_shared
    national_label_en: "\xC2\_Inside house and shared"
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439/\u0441\u043E\u0432\u043C\u0435\u0441\u0442\u043D\u043E\u0433\u043E\
      \ \u043F\u043E\u043B\u044C\u0437\u043E\u0432\u0430\u043D\u0438\u044F \u0442\u0443\
      \u0430\u043B\u0435\u0442 \u0441\u043E \u0441\u043C\u044B\u0432\u043E\u043C"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: ARM-SAN-09
    source_category_code: flush_to_somewhere_else
    national_label_en: flush to somewhere else
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: ARM-SAN-10
    source_category_code: flush_pour_flush_not_to_sewer_septic_tank_pit_latrine
    national_label_en: Flush/pour flush not to sewer/septic tank/pit latrine
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: ARM-SAN-11
    source_category_code: pour_flush_not_to_sewer_septic_tank_pit_latrine
    national_label_en: Pour flush not to sewer, septic tank, pit latrine
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: ARM-SAN-12
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: ARM-SAN-13
    source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: ARM-SAN-14
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit latrine
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: ARM-SAN-15
    source_category_code: flush_pour_flush_to_a_pit_latrine
    national_label_en: Flush/pour flush to a pit latrine
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: ARM-SAN-16
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: ARM-SAN-17
    source_category_code: flush_pour_flush_to_septic_tank
    national_label_en: Flush/pour flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: ARM-SAN-18
    source_category_code: flush_to_do_not_know_where
    national_label_en: Flush to do not know where
    national_label_local: "\u0432 \u043D\u0435\u0438\u0437\u0432\u0435\u0441\u0442\
      \u043D\u043E\u0435 \u043C\u0435\u0441\u0442\u043E/\u043D\u0435 \u0437\u043D\u0430\
      \u044E/\u043D\u0435 \u0443\u0432\u0435\u0440\u0435\u043D(\u0430)"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: ARM-SAN-19
    source_category_code: flush_don_t_know_where
    national_label_en: flush, don't know where
    national_label_local: "\u0432 \u043D\u0435\u0438\u0437\u0432\u0435\u0441\u0442\
      \u043D\u043E\u0435 \u043C\u0435\u0441\u0442\u043E/\u043D\u0435 \u0437\u043D\u0430\
      \u044E/\u043D\u0435 \u0443\u0432\u0435\u0440\u0435\u043D(\u0430)"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: ARM-SAN-20
    source_category_code: bucket
    national_label_en: Bucket
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u043E\
      \u0442\u0445\u043E\u0436\u0438\u043C \u0432\u0435\u0434\u0440\u043E\u043C"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: ARM-SAN-21
    source_category_code: bucket_toilet
    national_label_en: Bucket toilet
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u043E\
      \u0442\u0445\u043E\u0436\u0438\u043C \u0432\u0435\u0434\u0440\u043E\u043C"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: ARM-SAN-22
    source_category_code: pit_latrine_with_a_slab
    national_label_en: Pit latrine with a slab
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: ARM-SAN-23
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: ARM-SAN-24
    source_category_code: open_pit
    national_label_en: Open pit
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0431\
      \u0435\u0437 \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\
      \u0438\u0442\u044B/\u0441 \u043E\u0442\u043A\u0440\u044B\u0442\u043E\u0439 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: ARM-SAN-25
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0431\
      \u0435\u0437 \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\
      \u0438\u0442\u044B/\u0441 \u043E\u0442\u043A\u0440\u044B\u0442\u043E\u0439 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: ARM-SAN-26
    source_category_code: pitlatrine_without_slab_open_pit
    national_label_en: Pitlatrine without slab/open pit
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0431\
      \u0435\u0437 \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\
      \u0438\u0442\u044B/\u0441 \u043E\u0442\u043A\u0440\u044B\u0442\u043E\u0439 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: ARM-SAN-27
    source_category_code: traditional_pit_toilet
    national_label_en: Traditional pit toilet
    national_label_local: "\u0422\u0440\u0430\u0434\u0438\u0446\u0438\u043E\u043D\u043D\
      \u0430\u044F \u0443\u0431\u043E\u0440\u043D\u0430\u044F"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARM-SAN-28
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated Improved Pit latrine
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: ARM-SAN-29
    source_category_code: outside_house_and_exclusive
    national_label_en: Outside house and exclusive
    national_label_local: "\u0421\u043E\u0431\u0441\u0442\u0432\u0435\u043D\u043D\u044B\
      \u0435 \u0443\u0431\u043E\u0440\u043D\u044B\u0435"
    jmp_classification: Latrines > Dry latrines > Private Latrines
    jmp_id: latrines.dry_latrines.private_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: false
    shared_flag: false
    source_row: 112
  - country_entry_id: ARM-SAN-30
    source_category_code: outside_house_and_shared
    national_label_en: Outside house and shared
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u044B\u0435 \u043E\u0431\
      \u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\u044B\u0435/\u0441\u043E\u0432\
      \u043C\u0435\u0441\u0442\u043D\u043E\u0433\u043E \u043F\u043E\u043B\u044C\u0437\
      \u043E\u0432\u0430\u043D\u0438\u044F"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines
    jmp_id: latrines.dry_latrines.public_shared_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: false
    shared_flag: true
    source_row: 120
  - country_entry_id: ARM-SAN-31
    source_category_code: no_facilities_or_bush_or_field
    national_label_en: No facilities or bush or field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: ARM-SAN-32
    source_category_code: no_facility_bush_field
    national_label_en: No facility/bush/field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: ARM-SAN-33
    source_category_code: any_facility_shared_with_others
    national_label_en: Any facility shared with others
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: ARM-SAN-34
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: ARM-SAN-35
    source_category_code: other_missing
    national_label_en: Other/missing
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: ARM-SAN-36
    source_category_code: public_toilet
    national_label_en: Public toilet
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: ARM-SAN-37
    source_category_code: no_sewerage_system
    national_label_en: No sewerage system
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_ARM_Armenia_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ARM-WAS-01
    source_category_code: spring_water_well
    national_label_en: Spring water, well
    national_label_local: "\u0413\u0440\u0443\u043D\u0442\u043E\u0432\u044B\u0435\
      \ \u0432\u043E\u0434\u044B"
    jmp_classification: Ground water
    jmp_id: ground_water
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well|protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 43
  - country_entry_id: ARM-WAS-02
    source_category_code: spring_water_wells
    national_label_en: Spring water, wells
    national_label_local: "\u0413\u0440\u0443\u043D\u0442\u043E\u0432\u044B\u0435\
      \ \u0432\u043E\u0434\u044B"
    jmp_classification: Ground water
    jmp_id: ground_water
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well|protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 43
  - country_entry_id: ARM-WAS-03
    source_category_code: spring_water_wells
    national_label_en: Spring, water, wells
    national_label_local: "\u0413\u0440\u0443\u043D\u0442\u043E\u0432\u044B\u0435\
      \ \u0432\u043E\u0434\u044B"
    jmp_classification: Ground water
    jmp_id: ground_water
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well|protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 43
  - country_entry_id: ARM-WAS-04
    source_category_code: spring_well
    national_label_en: Spring/well
    national_label_local: "\u0413\u0440\u0443\u043D\u0442\u043E\u0432\u044B\u0435\
      \ \u0432\u043E\u0434\u044B"
    jmp_classification: Ground water
    jmp_id: ground_water
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well|protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 43
  - country_entry_id: ARM-WAS-05
    source_category_code: springs_wells
    national_label_en: Springs, wells
    national_label_local: "\u0413\u0440\u0443\u043D\u0442\u043E\u0432\u044B\u0435\
      \ \u0432\u043E\u0434\u044B"
    jmp_classification: Ground water
    jmp_id: ground_water
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well|protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 43
  - country_entry_id: ARM-WAS-06
    source_category_code: spring
    national_label_en: Spring
    national_label_local: "\u0412\u0441\u0435 \u0440\u043E\u0434\u043D\u0438\u043A\
      \u0438"
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 74
  - country_entry_id: ARM-WAS-07
    source_category_code: well
    national_label_en: Well
    national_label_local: "\u0412\u0441\u0435 \u043A\u043E\u043B\u043E\u0434\u0446\
      \u044B"
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 54
  - country_entry_id: ARM-WAS-08
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: "\u0417\u0430\u0449\u0438\u0449\u0451\u043D\u043D\u044B\u0439\
      \ \u0440\u043E\u0434\u043D\u0438\u043A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: ARM-WAS-09
    source_category_code: protected_dug_well
    national_label_en: Protected dug well
    national_label_local: "\u0417\u0430\u0449\u0438\u0449\u0451\u043D\u043D\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: ARM-WAS-10
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: "\u0417\u0430\u0449\u0438\u0449\u0451\u043D\u043D\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: ARM-WAS-11
    source_category_code: tube_well_or_borehole
    national_label_en: tube well or borehole
    national_label_local: "\u0422\u0440\u0443\u0431\u0447\u0430\u0442\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446, \u0441\u043A\u0432\u0430\u0436\
      \u0438\u043D\u0430"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: ARM-WAS-12
    source_category_code: tubewell_borehole
    national_label_en: Tubewell/ borehole
    national_label_local: "\u0422\u0440\u0443\u0431\u0447\u0430\u0442\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446, \u0441\u043A\u0432\u0430\u0436\
      \u0438\u043D\u0430"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: ARM-WAS-13
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0439 \u0440\u043E\u0434\u043D\u0438\u043A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: ARM-WAS-14
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0439 \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: ARM-WAS-15
    source_category_code: open_well_in_yard_plot
    national_label_en: Open well in yard/plot
    national_label_local: "\u0427\u0430\u0441\u0442\u043D\u044B\u0439"
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: ARM-WAS-16
    source_category_code: brought
    national_label_en: Brought
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: ARM-WAS-17
    source_category_code: delivered_imported_water
    national_label_en: Delivered (imported) water
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: ARM-WAS-18
    source_category_code: other_protected
    national_label_en: other protected
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: ARM-WAS-19
    source_category_code: own_system
    national_label_en: own system
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: ARM-WAS-20
    source_category_code: own_system_of_water_supply
    national_label_en: Own system of water supply
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: ARM-WAS-21
    source_category_code: bought
    national_label_en: Bought
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 104
  - country_entry_id: ARM-WAS-22
    source_category_code: delevered_water
    national_label_en: Delevered water
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 104
  - country_entry_id: ARM-WAS-23
    source_category_code: own_system
    national_label_en: Own system
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 104
  - country_entry_id: ARM-WAS-24
    source_category_code: delivered_imported_water
    national_label_en: delivered (imported) water
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: ARM-WAS-25
    source_category_code: delivered_water
    national_label_en: Delivered water
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: ARM-WAS-26
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: ARM-WAS-27
    source_category_code: tanker_truck_cart_with_drum
    national_label_en: Tanker truck/cart with drum
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: ARM-WAS-28
    source_category_code: vendor
    national_label_en: Vendor
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: ARM-WAS-29
    source_category_code: water_ven_dor
    national_label_en: water ven dor
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: ARM-WAS-30
    source_category_code: water_vendor
    national_label_en: water vendor
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: ARM-WAS-31
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u0438\u0435 \u043D\u0435\u0443\
      \u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435"
    jmp_classification: Other non-improved
    jmp_id: other_non_improved
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 105
  - country_entry_id: ARM-WAS-32
    source_category_code: bought_water
    national_label_en: bought water
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: ARM-WAS-33
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: ARM-WAS-34
    source_category_code: other_sources
    national_label_en: Other sources
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: ARM-WAS-35
    source_category_code: other_unprotected
    national_label_en: Other unprotected
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: ARM-WAS-36
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARM-WAS-37
    source_category_code: other_sources
    national_label_en: Other sources
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARM-WAS-38
    source_category_code: secondary
    national_label_en: Secondary
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARM-WAS-39
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "\u0424\u0430\u0441\u043E\u0432\u0430\u043D\u043D\u0430\u044F\
      \ \u0432\u043E\u0434\u0430"
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 89
  - country_entry_id: ARM-WAS-40
    source_category_code: bought_water
    national_label_en: Bought water
    national_label_local: "\u0424\u0430\u0441\u043E\u0432\u0430\u043D\u043D\u0430\u044F\
      \ \u0432\u043E\u0434\u0430"
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 89
  - country_entry_id: ARM-WAS-41
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "\u0411\u0443\u0442\u0438\u043B\u0438\u0440\u043E\u0432\u0430\
      \u043D\u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: ARM-WAS-42
    source_category_code: bought_water_noy_byuregh_etc
    national_label_en: Bought water (Noy, Byuregh, etc.)
    national_label_local: "\u0411\u0443\u0442\u0438\u043B\u0438\u0440\u043E\u0432\u0430\
      \u043D\u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: ARM-WAS-43
    source_category_code: river
    national_label_en: River
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: ARM-WAS-44
    source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: ARM-WAS-45
    source_category_code: river_stream
    national_label_en: River/stream
    national_label_local: "\u0420\u0435\u043A\u0430"
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: ARM-WAS-46
    source_category_code: pipe_into_dwelling_own_artesian
    national_label_en: Pipe into dwelling (own artesian)
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: ARM-WAS-47
    source_category_code: water_pipe_outside_compound
    national_label_en: water pipe outside compound
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: ARM-WAS-48
    source_category_code: centralized_system
    national_label_en: Centralized system
    national_label_local: "\u041F\u043E\u0434\u043A\u043B\u044E\u0447\u0435\u043D\u0438\
      \u044F \u043A \u0434\u043E\u043C\u0443"
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: ARM-WAS-49
    source_category_code: centralized_water_supply
    national_label_en: centralized water supply
    national_label_local: "\u041F\u043E\u0434\u043A\u043B\u044E\u0447\u0435\u043D\u0438\
      \u044F \u043A \u0434\u043E\u043C\u0443"
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: ARM-WAS-50
    source_category_code: piped_water_into_dwelling_yard_plot
    national_label_en: Piped water into dwelling/yard/plot
    national_label_local: "\u041F\u043E\u0434\u043A\u043B\u044E\u0447\u0435\u043D\u0438\
      \u044F \u043A \u0434\u043E\u043C\u0443"
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: ARM-WAS-51
    source_category_code: central_water_supply_inside_house
    national_label_en: Central water supply inside house
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: ARM-WAS-52
    source_category_code: centralized_water_supply
    national_label_en: centralized water supply
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: ARM-WAS-53
    source_category_code: piped_into_residence
    national_label_en: Piped into residence
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: ARM-WAS-54
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: ARM-WAS-55
    source_category_code: water_pipe_into_dwelling
    national_label_en: water pipe into dwelling
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: ARM-WAS-56
    source_category_code: central_water_supply_outside_house
    national_label_en: Central water supply outside house
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: ARM-WAS-57
    source_category_code: piped_into_yard_plot
    national_label_en: Piped into yard/plot
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: ARM-WAS-58
    source_category_code: water_pipe_into_compound
    national_label_en: water pipe into compound
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: ARM-WAS-59
    source_category_code: public_tap
    national_label_en: Public tap
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: ARM-WAS-60
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_ARM_Armenia_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

