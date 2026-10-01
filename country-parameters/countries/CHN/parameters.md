---
country_id: CTY-CHN
iso3: CHN
schema_version: '0.2'
status: draft
country_name: CHN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CHN-EDU-01
    national_label_en: Pre-primary education
    national_label_local: "\u5B66\u524D\u6559\u80B2"
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
  - country_entry_id: CHN-EDU-02
    national_label_en: Primary education
    national_label_local: "\u5C0F\u5B66"
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
    - CHN-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: CHN-EDU-03
    national_label_en: Junior secondary education
    national_label_local: "\u666E\u901A\u521D\u4E2D"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - CHN-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHN-EDU-04
    national_label_en: Senior secondary education
    national_label_local: "\u666E\u901A\u9AD8\u4E2D"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - CHN-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHN-EDU-05
    national_label_en: Vocational high school education
    national_label_local: "\u804C\u4E1A\u9AD8\u4E2D"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - CHN-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHN-EDU-06
    national_label_en: Post-secondary non-tertiary education (general)
    national_label_local: "\u9AD8\u4E2D\u540E\u975E\u9AD8\u7B49\u6559\u80B2"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 12
    parent_country_entry_ids:
    - CHN-EDU-04
    cum_years_schooling: 13
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-04
    - CHN-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHN-EDU-07
    national_label_en: Post-secondary non-tertiary education (vocational)
    national_label_local: "\u9AD8\u4E2D\u540E\u975E\u9AD8\u7B49\u6559\u80B2"
    entry_age: 18
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
    parent_country_entry_ids:
    - CHN-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-04
    - CHN-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHN-EDU-08
    national_label_en: Short-cycle tertiary education
    national_label_local: "\u5927\u4E13\u3001\u9AD8\u804C"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - CHN-EDU-04
    cum_years_schooling: 14
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-04
    - CHN-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHN-EDU-09
    national_label_en: Bachelor' s or equivalent level
    national_label_local: "\u5927\u5B66\u672C\u79D1"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - CHN-EDU-04
    cum_years_schooling: 16
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-04
    - CHN-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHN-EDU-10
    national_label_en: Bachelor's or equivalent level
    national_label_local: "\u5927\u5B66\u672C\u79D1"
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - CHN-EDU-04
    cum_years_schooling: 17
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-04
    - CHN-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHN-EDU-11
    national_label_en: "Bachelor\u2019s or\nequivalent level,\nprofessional"
    national_label_local: "\u7B2C\u4E8C\u5B66\u58EB\u5B66\u4F4D"
    entry_age: 22
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - CHN-EDU-04
    cum_years_schooling: 14
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-04
    - CHN-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHN-EDU-12
    national_label_en: "Master\u2018s or equivalent level"
    national_label_local: "\u7855\u58EB\u7814\u7A76\u751F"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - CHN-EDU-09
    - CHN-EDU-10
    - CHN-EDU-11
    cum_years_schooling: 16
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-04
    - CHN-EDU-11
    - CHN-EDU-12
    cum_years_status: computed
    review_flags: &id002
    - 'minimum parent path selected from: CHN-EDU-09, CHN-EDU-10, CHN-EDU-11'
  - country_entry_id: CHN-EDU-13
    national_label_en: Doctor's degree or equivalent level
    national_label_local: "\u535A\u58EB\u7814\u7A76\u751F"
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - CHN-EDU-12
    cum_years_schooling: 19
    cum_years_computation_path:
    - CHN-EDU-02
    - CHN-EDU-03
    - CHN-EDU-04
    - CHN-EDU-11
    - CHN-EDU-12
    - CHN-EDU-13
    cum_years_status: computed
    review_flags: *id002
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_China.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CHN-SUBNAT-01
    survey_labels: Beijing | [11]Beijing, North China (municipality
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_899
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_899
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '899'
    geo_nvar: ADM1_NAME
    geo_name: Beijing Shi
    source_row: 2333
  - country_entry_id: CHN-SUBNAT-02
    survey_labels: Shanxi | [14]Shanxi, North China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_923
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_923
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '923'
    geo_nvar: ADM1_NAME
    geo_name: Shanxi Sheng
    source_row: 2334
  - country_entry_id: CHN-SUBNAT-03
    survey_labels: Liaoning | [21]Liaoning, Northeast China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_916
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_916
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '916'
    geo_nvar: ADM1_NAME
    geo_name: Liaoning Sheng
    source_row: 2335
  - country_entry_id: CHN-SUBNAT-04
    survey_labels: Jiangsu | [32]Jiangsu, East China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_913
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_913
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '913'
    geo_nvar: ADM1_NAME
    geo_name: Jiangsu Sheng
    source_row: 2336
  - country_entry_id: CHN-SUBNAT-05
    survey_labels: Anhui | [34]Anhui, East China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_898
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_898
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '898'
    geo_nvar: ADM1_NAME
    geo_name: Anhui Sheng
    source_row: 2337
  - country_entry_id: CHN-SUBNAT-06
    survey_labels: Shandong | [37]Shandong, East China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_921
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_921
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '921'
    geo_nvar: ADM1_NAME
    geo_name: Shandong Sheng
    source_row: 2338
  - country_entry_id: CHN-SUBNAT-07
    survey_labels: Henan | [41]Henan, South Central China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_909
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_909
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '909'
    geo_nvar: ADM1_NAME
    geo_name: Henan Sheng
    source_row: 2339
  - country_entry_id: CHN-SUBNAT-08
    survey_labels: Hubei | [42]Hubei, South Central China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_911
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_911
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '911'
    geo_nvar: ADM1_NAME
    geo_name: Hubei Sheng
    source_row: 2340
  - country_entry_id: CHN-SUBNAT-09
    survey_labels: Hunan | [43]Hunan, South Central China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_912
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_912
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '912'
    geo_nvar: ADM1_NAME
    geo_name: Hunan Sheng
    source_row: 2341
  - country_entry_id: CHN-SUBNAT-10
    survey_labels: Guangdong | [44]Guangdong, South Central China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_903
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_903
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '903'
    geo_nvar: ADM1_NAME
    geo_name: Guangdong Sheng
    source_row: 2342
  - country_entry_id: CHN-SUBNAT-11
    survey_labels: Chongqing | [50]Chongqing, Southwest China (municip
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_900
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_900
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '900'
    geo_nvar: ADM1_NAME
    geo_name: Chongqing Shi
    source_row: 2343
  - country_entry_id: CHN-SUBNAT-12
    survey_labels: Sichuan | [51]Sichuan, Southwest China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_924
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_924
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '924'
    geo_nvar: ADM1_NAME
    geo_name: Sichuan Sheng
    source_row: 2344
  - country_entry_id: CHN-SUBNAT-13
    survey_labels: Yunnan | [53]Yunnan, Southwest China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_929
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_929
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '929'
    geo_nvar: ADM1_NAME
    geo_name: Yunnan Sheng
    source_row: 2345
  - country_entry_id: CHN-SUBNAT-14
    survey_labels: Gansu | [62]Gansu, Northwest China
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_902
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_902
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '902'
    geo_nvar: ADM1_NAME
    geo_name: Gansu Sheng
    source_row: 2346
  - country_entry_id: CHN-SUBNAT-15
    survey_labels: Inner Mongolia
    survey_variables: subnatid
    gmd_subnatid1: CHN_2015_GAUL1_917
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHN_2015_GAUL1_917
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '917'
    geo_nvar: ADM1_NAME
    geo_name: Nei Mongol Zizhiqu
    source_row: 2355
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
  - country_entry_id: CHN-SAN-01
    source_category_code: composting_toilet
    national_label_en: composting toilet
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: CHN-SAN-02
    source_category_code: private_domestic_connection_to_sewage_system
    national_label_en: Private domestic connection to sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: CHN-SAN-03
    source_category_code: private_flush_to_septic_tank
    national_label_en: Private flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: CHN-SAN-04
    source_category_code: shared_domestic_connection_to_sewage_system
    national_label_en: Shared domestic connection to sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: CHN-SAN-05
    source_category_code: shared_flush_to_septic_tank
    national_label_en: Shared flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 80
  - country_entry_id: CHN-SAN-06
    source_category_code: flush_pour_to_other_location
    national_label_en: flush/pour to other location
    national_label_local: to elsewhere
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: CHN-SAN-07
    source_category_code: flush_pour_to_piped_sewage_system
    national_label_en: flush/pour to piped sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: CHN-SAN-08
    source_category_code: flush_pour_to_pit_latrine
    national_label_en: flush/pour to pit latrine
    national_label_local: to pit
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: CHN-SAN-09
    source_category_code: flush_pour_to_septic_tank
    national_label_en: flush/pour to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: CHN-SAN-10
    source_category_code: bucket
    national_label_en: bucket
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: CHN-SAN-11
    source_category_code: bucket_latrine_where_fresh_excreta_are_manually_removed
    national_label_en: Bucket latrine (where fresh excreta are manually removed)
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: CHN-SAN-12
    source_category_code: hanging_toilet_latrine
    national_label_en: hanging toilet/latrine
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: CHN-SAN-13
    source_category_code: pit_with_slab
    national_label_en: pit with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: CHN-SAN-14
    source_category_code: pit_without_slab_open
    national_label_en: pit without slab/open
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: CHN-SAN-15
    source_category_code: uncovered_dry_latrine_without_privacy
    national_label_en: Uncovered dry latrine (without privacy)
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: CHN-SAN-16
    source_category_code: ventilation_improved_pit_latrine
    national_label_en: ventilation improved pit latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: CHN-SAN-17
    source_category_code: private_covered_dry_latrine_with_privacy
    national_label_en: Private covered dry latrine (with privacy)
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: CHN-SAN-18
    source_category_code: shared_covered_dry_latrine_with_privacy
    national_label_en: Shared covered dry latrine (with privacy)
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: CHN-SAN-19
    source_category_code: private_pour_flush_latrine
    national_label_en: Private pour flush latrine
    national_label_local: Private pour flush latrine
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 91
  - country_entry_id: CHN-SAN-20
    source_category_code: shared_pour_flush_latrine
    national_label_en: Shared pour flush latrine
    national_label_local: Public/shared pour flush latrine
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 97
  - country_entry_id: CHN-SAN-21
    source_category_code: no_facilities_bush_field
    national_label_en: no facilities (bush, field)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: CHN-SAN-22
    source_category_code: no_facilities_open_defecation
    national_label_en: No facilities (open defecation)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: CHN-SAN-23
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
  - country_entry_id: CHN-SAN-24
    source_category_code: other_specify
    national_label_en: other, specify
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CHN_China_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CHN-WAS-01
    source_category_code: protected_spring
    national_label_en: protected spring
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: CHN-WAS-02
    source_category_code: protected_dug_well
    national_label_en: protected dug well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: CHN-WAS-03
    source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: Protected wells or springs
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: true
    shared_flag: false
    source_row: 46
  - country_entry_id: CHN-WAS-04
    source_category_code: protected_tube_well_or_bore_hole
    national_label_en: Protected tube well or bore hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: CHN-WAS-05
    source_category_code: tubewell_borehole
    national_label_en: tubewell/borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: CHN-WAS-06
    source_category_code: unprotected_spring
    national_label_en: unprotected spring
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: CHN-WAS-07
    source_category_code: unprotected_dug_well
    national_label_en: unprotected dug well
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: CHN-WAS-08
    source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: Unprotected wells or springs
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 50
  - country_entry_id: CHN-WAS-09
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker-truck, vendor
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: CHN-WAS-10
    source_category_code: other_specify
    national_label_en: other, specify
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: CHN-WAS-11
    source_category_code: bottled_water
    national_label_en: bottled water
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: CHN-WAS-12
    source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: CHN-WAS-13
    source_category_code: rainwater_collection
    national_label_en: rainwater collection
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: CHN-WAS-14
    source_category_code: surface_water_river_lake_etc
    national_label_en: surface water (river, lake, etc)
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: CHN-WAS-15
    source_category_code: water_taken_directly_from_pond_water_or_stream
    national_label_en: Water taken directly from pond-water or stream
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: CHN-WAS-16
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: CHN-WAS-17
    source_category_code: piped_private
    national_label_en: piped private
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: CHN-WAS-18
    source_category_code: piped_to_yard_plot
    national_label_en: piped to yard/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: CHN-WAS-19
    source_category_code: public_standpipe
    national_label_en: Public standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: CHN-WAS-20
    source_category_code: public_tap_standpipe
    national_label_en: public tap/standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CHN_China_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

