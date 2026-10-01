---
country_id: CTY-CAN
iso3: CAN
schema_version: '0.2'
status: draft
country_name: CAN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CAN-EDU-01
    national_label_en: Early childhood development programmes
    national_label_local: Early learning programs
    entry_age: 0
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
  - country_entry_id: CAN-EDU-02
    national_label_en: Pre-primary
    national_label_local: Preschool programs
    entry_age: 3
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
  - country_entry_id: CAN-EDU-03
    national_label_en: Pre-primary
    national_label_local: Kindergarten or maternelle or Grade Primary
    entry_age: 3
    duration_years: 1
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
  - country_entry_id: CAN-EDU-04
    national_label_en: Elementary education or equivalent
    national_label_local: Elementary
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - CAN-EDU-04
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: CAN-EDU-05
    national_label_en: Lower secondary or equivalent
    national_label_local: Junior High/Middle School
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 9
    parent_country_entry_ids:
    - CAN-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-06
    national_label_en: Upper secondary education or equivalent - General
    national_label_local: High School/Secondary School/Senior Secondary
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - CAN-EDU-05
    cum_years_schooling: 12
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-07
    national_label_en: Upper secondary education or equivalent - Vocational/Technical
    national_label_local: Vocational/Technical High School/Formation Professionnelle
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - CAN-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-08
    national_label_en: Postsecondary short general, career or  technical education
      or equivalent- General or Equivalent
    national_label_local: Upgrading Program
    entry_age: 18
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 12
    parent_country_entry_ids:
    - CAN-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-09
    national_label_en: Postsecondary short general, career or  technical education
      or equivalent -Career, Technical or Professional or equivalent
    national_label_local: 'Trade certificate/

      Career, technical or professional training program'
    entry_age: 18
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
    parent_country_entry_ids:
    - CAN-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-10
    national_label_en: Postsecondary short general, career or  technical education
      or equivalent  - Apprenticeship or equivalent
    national_label_local: Apprenticeship program
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - CAN-EDU-06
    cum_years_schooling: 14
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-11
    national_label_en: 'Postsecondary general, career or  technical education or equivalent

      - General or equivalent'
    national_label_local: Undergraduate diploma/certificate program
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - CAN-EDU-06
    cum_years_schooling: 13
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-12
    national_label_en: Postsecondary general, career or  technical education or equivalent
      - Career or technical or equivalent
    national_label_local: College Diploma program
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - CAN-EDU-06
    cum_years_schooling: 14
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-13
    national_label_en: "Postsecondary general, career or  technical education or equivalent\
      \ \n-Above career or technical certificate or diploma or equivalent"
    national_label_local: Post career, technical or professional training program
    entry_age: 21
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - CAN-EDU-06
    cum_years_schooling: 13
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-13
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-14
    national_label_en: Bachelor's degree education or equivalent
    national_label_local: Bachelor's degree education or equivalent
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - CAN-EDU-06
    cum_years_schooling: 15
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-14
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-15
    national_label_en: "Above bachelor\u2019s degree credential or equivalent"
    national_label_local: "Above bachelor\u2019s degree credential or equivalent"
    entry_age: 21
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - CAN-EDU-06
    cum_years_schooling: 13
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-15
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-16
    national_label_en: Professional degree
    national_label_local: Professional degree
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - CAN-EDU-06
    cum_years_schooling: 17
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-16
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CAN-EDU-17
    national_label_en: Master's degree education or equivalent
    national_label_local: Master's degree education or equivalent
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - CAN-EDU-14
    - CAN-EDU-15
    cum_years_schooling: 14
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-15
    - CAN-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CAN-EDU-14, CAN-EDU-15'
  - country_entry_id: CAN-EDU-18
    national_label_en: Above master's degree credential or equivalent
    national_label_local: Above master's degree credential or equivalent
    entry_age: 23
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - CAN-EDU-14
    - CAN-EDU-15
    cum_years_schooling: 14
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-15
    - CAN-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CAN-EDU-14, CAN-EDU-15'
  - country_entry_id: CAN-EDU-19
    national_label_en: Doctorate degree education or equivalent
    national_label_local: Doctorate degree education or equivalent
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - CAN-EDU-16
    - CAN-EDU-17
    - CAN-EDU-18
    cum_years_schooling: 17
    cum_years_computation_path:
    - CAN-EDU-04
    - CAN-EDU-05
    - CAN-EDU-06
    - CAN-EDU-15
    - CAN-EDU-17
    - CAN-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CAN-EDU-14, CAN-EDU-15'
    - 'minimum parent path selected from: CAN-EDU-16, CAN-EDU-17, CAN-EDU-18'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Canada.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CAN-SUBNAT-01
    survey_labels: '[10]Newfoundland and Labrador'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '829'
    geo_nvar: ADM1_NAME
    geo_name: Newfoundland and Labrador / Terre-Neuve-et-Labrador
    source_row: 2018
  - country_entry_id: CAN-SUBNAT-02
    survey_labels: '[11]Prince Edward Island'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '834'
    geo_nvar: ADM1_NAME
    geo_name: "Prince Edward Island / \xCEle-du-Prince-\xC9douard"
    source_row: 2019
  - country_entry_id: CAN-SUBNAT-03
    survey_labels: '[12]Nova Scotia'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '831'
    geo_nvar: ADM1_NAME
    geo_name: "Nova Scotia / Nouvelle-\xC9cosse"
    source_row: 2020
  - country_entry_id: CAN-SUBNAT-04
    survey_labels: '[13]New Brunswick'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '828'
    geo_nvar: ADM1_NAME
    geo_name: New Brunswick / Nouveau-Brunswick
    source_row: 2021
  - country_entry_id: CAN-SUBNAT-05
    survey_labels: '[24]Quebec'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '835'
    geo_nvar: ADM1_NAME
    geo_name: "Quebec / Qu\xE9bec"
    source_row: 2022
  - country_entry_id: CAN-SUBNAT-06
    survey_labels: '[35]Ontario'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '833'
    geo_nvar: ADM1_NAME
    geo_name: Ontario
    source_row: 2023
  - country_entry_id: CAN-SUBNAT-07
    survey_labels: '[46]Manitoba'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '827'
    geo_nvar: ADM1_NAME
    geo_name: Manitoba
    source_row: 2024
  - country_entry_id: CAN-SUBNAT-08
    survey_labels: '[47]Saskatchewan'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '836'
    geo_nvar: ADM1_NAME
    geo_name: Saskatchewan
    source_row: 2025
  - country_entry_id: CAN-SUBNAT-09
    survey_labels: '[48]Alberta'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '825'
    geo_nvar: ADM1_NAME
    geo_name: Alberta
    source_row: 2026
  - country_entry_id: CAN-SUBNAT-10
    survey_labels: '[59]British Columbia'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '826'
    geo_nvar: ADM1_NAME
    geo_name: British Columbia / Colombie-Britannique
    source_row: 2027
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
  - country_entry_id: CAN-SAN-01
    source_category_code: the_sewer_system_of_your_city_town_or_municipality
    national_label_en: The sewer system of your city, town or  municipality
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: CAN-SAN-02
    source_category_code: a_private_or_communal_septic_system_including_holding_tanks
    national_label_en: A private or communal septic system, including holding tanks
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: CAN-SAN-03
    source_category_code: don_t_know
    national_label_en: Don't know
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: CAN-SAN-04
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CAN_Canada_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CAN-WAS-01
    source_category_code: spring_water
    national_label_en: Spring water
    national_label_local: All springs
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 74
  - country_entry_id: CAN-WAS-02
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: CAN-WAS-03
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: CAN-WAS-04
    source_category_code: bottled_water_including_purchased_water_in_a_water_cooler
    national_label_en: Bottled water including purchased water in a water cooler
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: CAN-WAS-05
    source_category_code: bottled_water_including_purchased_water_in_a_water_cooler_t
    national_label_en: Bottled water including purchased water in a water cooler,
      t
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: CAN-WAS-06
    source_category_code: both_tap_water_and_bottled_water
    national_label_en: Both tap water and bottled water
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: CAN-WAS-07
    source_category_code: tap_water
    national_label_en: Tap water
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CAN_Canada_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

