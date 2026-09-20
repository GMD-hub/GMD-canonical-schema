---
country_id: CTY-UZB
iso3: UZB
schema_version: '0.2'
status: draft
country_name: UZB
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - national_label_en: pre-school education
    national_label_local: Maktabgacha ta'lim va tarbiya
    entry_age: 3
    duration_years: 4
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - national_label_en: primary education
    national_label_local: Boshlang'ich ta'lim
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
  - national_label_en: Lower secondary education
    national_label_local: Tayanch o‘rta ta’lim
    entry_age: 11
    duration_years: 5
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - national_label_en: General secondary education
    national_label_local: Umumiy o‘rta
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
  - national_label_en: Secondary technical and vocational education and initial vocational
      education (Academic Lyceum, Vocational School)
    national_label_local: O‘rta maxsus ta’lim va boshlang‘ich professional ta'lim
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - national_label_en: Secondary vocational education (College)
    national_label_local: O'rta professional ta'lim
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 12
  - national_label_en: Secondary technical-vocational education (Technical College)
    national_label_local: O'rta maxsus professional ta'lim
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
  - national_label_en: Bachelor
    national_label_local: Bakalavriat
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - national_label_en: Bachelor
    national_label_local: Bakalavriat
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - national_label_en: Master
    national_label_local: Magistratura
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - national_label_en: Master
    national_label_local: Magistratura
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - national_label_en: Postgraduate education
    national_label_local: Oliy ta'limdan keyingi ta'lim
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Uzbekistan.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - survey_labels: 1-Karakalpakstan | 101 -  Karakalpakstan | 1735 -  Karakalpakstan
      | Karakalpakstan -  Karakalpakstan
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3287
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3287
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3287'
    geo_nvar: ADM1_NAME
    geo_name: Karakalpakstan
    source_row: 18366
  - survey_labels: 10-Syrdarya | 106 -  Navoi region | 1712 -  Navoi | 1724 -  Syrdarya
      | Navoi -  Navoi
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_39697
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_39697
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '39697'
    geo_nvar: ADM1_NAME
    geo_name: Navoiy
    source_row: 18367
  - survey_labels: 11-Tashkent | 111 -  Tashkent region | Tashkent (Region) -  Tashkent
      (Region)
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3295
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3295
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3295'
    geo_nvar: ADM1_NAME
    geo_name: Tashkent
    source_row: 18368
  - survey_labels: 112 -  Fergana region | 12-Fergana | 1730 -  Fergana | Fergana
      -  Fergana
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3286
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3286
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3286'
    geo_nvar: ADM1_NAME
    geo_name: Fergana
    source_row: 18369
  - survey_labels: 113 -  Khorezm region | 13-Khorezm | Khorasm -  Khorasm
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3289
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3289
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3289'
    geo_nvar: ADM1_NAME
    geo_name: Khorezm
    source_row: 18370
  - survey_labels: 114 -  Tashkent city | 14-Tashkent city | 1726 -  Tashkent (city)
      | Tashkent (City) -  Tashkent (City)
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_39698
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_39698
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '39698'
    geo_nvar: ADM1_NAME
    geo_name: Tashkent city
    source_row: 18371
  - survey_labels: 102 -  Andijan region | 1703 -  Andijan | 2-Andijan | Andijan -  Andijan
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3284
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3284
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3284'
    geo_nvar: ADM1_NAME
    geo_name: Andijan
    source_row: 18372
  - survey_labels: 103 -  Bukhara region | 1706 -  Bukhara | 3-Bukhara | Bukhara -  Bukhara
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3285
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3285
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3285'
    geo_nvar: ADM1_NAME
    geo_name: Bukhara
    source_row: 18373
  - survey_labels: 104 -  Jizzakh region | 4-Jizzak | Jizzakh -  Jizzakh
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_39696
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_39696
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '39696'
    geo_nvar: ADM1_NAME
    geo_name: Jizzakh
    source_row: 18374
  - survey_labels: 105 -  Kashkadarya region | 1710 -  Kashkadarya | 5-Kashkadarya
      | Kashkadarya -  Kashkadarya
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3288
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3288
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3288'
    geo_nvar: ADM1_NAME
    geo_name: Kashkadarya
    source_row: 18375
  - survey_labels: 110 -  Syrdarya region | 1712 -  Navoi | 1724 -  Syrdarya | 6-Navoi
      | Syrdarya -  Syrdarya
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3294
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3294
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3294'
    geo_nvar: ADM1_NAME
    geo_name: Sirdarya
    source_row: 18376
  - survey_labels: 107 -  Namangan region | 1714 -  Namangan | 7-Namangan | Namangan
      -  Namangan
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3291
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3291
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3291'
    geo_nvar: ADM1_NAME
    geo_name: Namangan
    source_row: 18377
  - survey_labels: 108 -  Samarkand region | 1718 -  Samarkand | 8-Samarkand | Samarkand
      -  Samarkand
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3292
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3292
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3292'
    geo_nvar: ADM1_NAME
    geo_name: Samarkand
    source_row: 18378
  - survey_labels: 109 -  Surkhandarya region | 1722 -  Surkhandarya | 9-Surkhandarya
      | Surkhandarya -  Surkhandarya
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: UZB_2015_GAUL1_3293
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UZB_2015_GAUL1_3293
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3293'
    geo_nvar: ADM1_NAME
    geo_name: Surkhandarya
    source_row: 18379
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: Компостирующие туалеты
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - source_category_code: to_open_drain
    national_label_en: to open drain
    national_label_local: куда-то в другое место
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - source_category_code: to_piped_sewer_system
    national_label_en: to piped sewer system
    national_label_local: в трубопроводную канализационную систему
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - source_category_code: to_pit
    national_label_en: to pit
    national_label_local: в выгребную яму
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - source_category_code: to_septic_tank
    national_label_en: to septic tank
    national_label_local: в септиктенк
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - source_category_code: to_dk_where
    national_label_en: to DK where
    national_label_local: в неизвестное место/не знаю/не уверен(а)
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - source_category_code: flush_to_sewage_system_or_septic_tank
    national_label_en: Flush to sewage system or septic tank
    national_label_local: Туалеты со смывом
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - source_category_code: flush_toilet
    national_label_en: Flush toilet
    national_label_local: Туалеты со смывом
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - source_category_code: own_flush_toilet
    national_label_en: Own flush toilet
    national_label_local: Собственный туалет со смывом
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - source_category_code: shared_flush_toilet
    national_label_en: Shared flush toilet
    national_label_local: Общественный/совместного пользования туалет со смывом
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: куда-то в другое место
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: в трубопроводную канализационную систему
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit (latrine)
    national_label_local: в выгребную яму
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: в септиктенк
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - source_category_code: bucket
    national_label_en: Bucket
    national_label_local: Уборная с отхожим ведром
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet/hanging latrine
    national_label_local: Подвесной туалет/подвесная уборная
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: Уборная с выгребной ямой с напольной плитой/с крытой выгребной
      ямой
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - source_category_code: pit_latrine_with_slab_covered_latrine
    national_label_en: Pit latrine with slab/covered latrine
    national_label_local: Уборная с выгребной ямой с напольной плитой/с крытой выгребной
      ямой
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - source_category_code: open_pit
    national_label_en: Open pit
    national_label_local: Уборная с выгребной ямой без напольной плиты/с открытой
      выгребной ямой
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: Уборная с выгребной ямой без напольной плиты/с открытой
      выгребной ямой
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - source_category_code: traditional_pit_latrine
    national_label_en: Traditional pit latrine
    national_label_local: Традиционная уборная
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - source_category_code: traditional_pit_toilet
    national_label_en: Traditional pit toilet
    national_label_local: Традиционная уборная
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - source_category_code: traditional_pit_toilet
    national_label_en: Traditional pit toilet*
    national_label_local: Традиционная уборная
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - source_category_code: improved_pit_latrine_vip
    national_label_en: Improved pit latrine (VIP)
    national_label_local: Вентилируемые улучшенные уборные с выгребной ямой
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated Improved Pit latrine
    national_label_local: Вентилируемые улучшенные уборные с выгребной ямой
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit latrine (VIP)
    national_label_local: Вентилируемые улучшенные уборные с выгребной ямой
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - source_category_code: vip_latrine
    national_label_en: VIP latrine
    national_label_local: Вентилируемые улучшенные уборные с выгребной ямой
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - source_category_code: pour_flush_latrine_water_seal_type
    national_label_en: Pour flush latrine (water seal type)
    national_label_local: Уборные со смывом
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 85
  - source_category_code: no_facilities_bush_field
    national_label_en: No facilities/ bush/ field
    national_label_local: Сооружений нет, кусты, поле
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: no_facility_bush
    national_label_en: No facility/bush
    national_label_local: Сооружений нет, кусты, поле
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: other
    national_label_en: Other
    national_label_local: Другое
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_UZB_Uzbekistan_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - source_category_code: spring
    national_label_en: Spring
    national_label_local: Все родники
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - source_category_code: well_in_residence
    national_label_en: Well in residence
    national_label_local: Частный
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - source_category_code: public_well
    national_label_en: Public well
    national_label_local: Общественный
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 56
  - source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: Защищённый родник
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - source_category_code: protected_dug_well
    national_label_en: Protected dug well
    national_label_local: Защищённый колодец
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: Защищённый колодец
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - source_category_code: protected_well_in_residence
    national_label_en: Protected well in residence
    national_label_local: Частный
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - source_category_code: public_well
    national_label_en: Public well
    national_label_local: Общественный
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 64
  - source_category_code: tube_well_bore_hole_with_pump
    national_label_en: Tube well/ bore hole with pump
    national_label_local: Трубчатый колодец, скважина
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: tubewell_borehole
    national_label_en: Tubewell, borehole
    national_label_local: Трубчатый колодец, скважина
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: tubewell_borehole
    national_label_en: Tubewell/borehole
    national_label_local: Трубчатый колодец, скважина
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: Незащищённый родник
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - source_category_code: unprotected_dug_well
    national_label_en: Unprotected dug well
    national_label_local: Незащищённый колодец
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: Незащищённый колодец
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - source_category_code: open_well_in_residence
    national_label_en: Open well in residence
    national_label_local: Частный
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank/drum
    national_label_local: Тележка с небольшим баком/бочкой
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: Доставляется автоцистерной
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: tanker_truck
    national_label_en: Tanker-truck
    national_label_local: Доставляется автоцистерной
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: tanker_truck_vendor
    national_label_en: Tanker/ truck/ vendor
    national_label_local: Доставляется автоцистерной
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: other
    national_label_en: Other
    national_label_local: Другое
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Бутилированная вода
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Вода в пакетах
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - source_category_code: sachet_water
    national_label_en: Sachet water
    national_label_local: Вода в пакетах
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - source_category_code: rain_water_collection
    national_label_en: Rain water collection
    national_label_local: Крытая цистерна/резервуар
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: Крытая цистерна/резервуар
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: pond_river_or_stream
    national_label_en: Pond, river or stream
    national_label_local: Поверхностная вода
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: Поверхностная вода
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: pond_lake
    national_label_en: Pond/lake
    national_label_local: Пруд
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - source_category_code: pond_lake_dam
    national_label_en: Pond/lake/dam
    national_label_local: Пруд
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - source_category_code: river_stream
    national_label_en: River/stream
    national_label_local: Река
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - source_category_code: piped_water_piped_to_neighbour
    national_label_en: 'Piped water: piped to neighbour'
    national_label_local: Другое
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - source_category_code: piped_into_residence
    national_label_en: Piped into residence
    national_label_local: Подключения к дому
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: Водопроводная вода подается в жилище
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: Водопроводная вода подается в жилище
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
    national_label_local: Водопроводная вода подается во двор/на участок
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
    national_label_local: Водопроводная вода подается во двор/на участок
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: public_tap
    national_label_en: Public tap
    national_label_local: Общественный кран, колонка
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: Общественный кран, колонка
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: Общественный кран, колонка
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_UZB_Uzbekistan_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

