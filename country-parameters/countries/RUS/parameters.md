---
country_id: CTY-RUS
iso3: RUS
schema_version: '0.2'
status: draft
country_name: RUS
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - national_label_en: Pre-primary education
    national_label_local: Дошкольное образование
    entry_age: 3
    duration_years: 4
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - national_label_en: Primary education
    national_label_local: Начальное образование
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
  - national_label_en: Lower secondary education
    national_label_local: Основное общее образование
    entry_age: 11
    duration_years: 5
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - national_label_en: Upper secondary education
    national_label_local: Полное (среднее) общее образование
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
  - national_label_en: Tertiary education
    national_label_local: Среднее профессиональное образование  на базе основного
      общего образования
    entry_age: 16
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - national_label_en: Upper secondary education
    national_label_local: Начальное профессиональное образование на базе основного
      общего образования
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - national_label_en: Post secondary, non-tertiary education
    national_label_local: Начальное профессиональное образование на базе полного (среднего)
      общего образования
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
  - national_label_en: Tertiary education
    national_label_local: Среднее профессиональное образование на базе полного (среднего)
      общего образования
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - national_label_en: Tertiary education
    national_label_local: Высшее профессиональное образование (бакалавриат)
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - national_label_en: Tertiary education
    national_label_local: Высшее профессиональное образование (специалитет)
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - national_label_en: Tertiary education
    national_label_local: Высшее профессиональное образование (магистратура)
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - national_label_en: Tertiary education
    national_label_local: Высшее профессиональное образование (интернатура)
    entry_age: 23
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - national_label_en: Advanced research programmes
    national_label_local: Послевузовское образование (аспирантура)
    entry_age: 23
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  - national_label_en: Advanced research programmes
    national_label_local: Послевузовское образование (докторантура)
    entry_age: 27
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Russian
      Federation.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: 2015
  selectors: null
  value:
  - survey_labels: 1 - Altai krai | 1 – Altai krai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2490
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2490'
    geo_nvar: ADM1_NAME
    geo_name: Altayskiy Kray
    source_row: 13160
  - survey_labels: 10 - Amur oblast | 10 – Amur oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2491
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2491'
    geo_nvar: ADM1_NAME
    geo_name: Amurskaya Oblast
    source_row: 13161
  - survey_labels: 11 - Arkhangelsk oblast | 11 – Arkhangelsk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAULx_11
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '11'
    geo_nvar: ADM1_NAME
    geo_name: Arkhangelskaya Oblast & Nenetskiy Okrug
    source_row: 13162
  - survey_labels: 12 - Astrakhan oblast | 12 – Astrakhan oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2493
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2493'
    geo_nvar: ADM1_NAME
    geo_name: Astrakhanskaya Oblast
    source_row: 13163
  - survey_labels: 14 - Belgorod oblast | 14 – Belgorod oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2495
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2495'
    geo_nvar: ADM1_NAME
    geo_name: Belgorodskaya Oblast
    source_row: 13164
  - survey_labels: 15 - Bryansk oblast | 15 – Bryansk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2496
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2496'
    geo_nvar: ADM1_NAME
    geo_name: Bryanskaya Oblast
    source_row: 13165
  - survey_labels: 17 - Vladimir oblast | 17 – Vladimir oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2571
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2571'
    geo_nvar: ADM1_NAME
    geo_name: Vladimirskaya Oblast
    source_row: 13166
  - survey_labels: 18 - Volgograd oblast | 18 – Volgograd oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2572
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2572'
    geo_nvar: ADM1_NAME
    geo_name: Volgogradskaya Oblast
    source_row: 13167
  - survey_labels: 19 - Vologda oblast | 19 – Vologda oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2573
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2573'
    geo_nvar: ADM1_NAME
    geo_name: Vologodskaya Oblast
    source_row: 13168
  - survey_labels: 20 - Voronezh oblast | 20 – Voronezh oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2574
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2574'
    geo_nvar: ADM1_NAME
    geo_name: Voronezhskaya Oblast
    source_row: 13169
  - survey_labels: 22 - Nizhny Novgorod oblast | 22 – Nizhny Novgorod oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2539
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2539'
    geo_nvar: ADM1_NAME
    geo_name: Nizhegorodskaya Oblast
    source_row: 13170
  - survey_labels: 24 - Ivanovo oblast | 24 – Ivanovo oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2507
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2507'
    geo_nvar: ADM1_NAME
    geo_name: Ivanovskaya Oblast
    source_row: 13171
  - survey_labels: 25 - Irkutsk oblast | 25 – Irkutsk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAULx_25
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '25'
    geo_nvar: ADM1_NAME
    geo_name: Irkutskaya Oblast & Ustordynskiy Buryatskiy Okrug
    source_row: 13172
  - survey_labels: 26 - Ingush republic | 26 – Ingush republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2505
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2505'
    geo_nvar: ADM1_NAME
    geo_name: Ingushetiya Rep.
    source_row: 13173
  - survey_labels: 27 - Kaliningrad oblast | 27 – Kaliningrad oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2509
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2509'
    geo_nvar: ADM1_NAME
    geo_name: Kaliningradskaya Oblast
    source_row: 13174
  - survey_labels: 28 - Tver oblast | 28 – Tver oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2565
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2565'
    geo_nvar: ADM1_NAME
    geo_name: Tverskaya Oblast
    source_row: 13175
  - survey_labels: 29 - Kaluga oblast | 29 – Kaluga oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2511
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2511'
    geo_nvar: ADM1_NAME
    geo_name: Kaluzhskaya Oblast
    source_row: 13176
  - survey_labels: 3 - Krasnodar krai | 3 – Krasnodar krai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2524
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2524'
    geo_nvar: ADM1_NAME
    geo_name: Krasnodarskiy Kray
    source_row: 13177
  - survey_labels: 30 - Kamchatka krai | 30 – Kamchatka krai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAULx_30
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '30'
    geo_nvar: ADM1_NAME
    geo_name: Kamchatskaya Oblast & Koryakskiy Okrug
    source_row: 13178
  - survey_labels: 32 - Kemerovo oblast | 32 – Kemerovo oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2515
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2515'
    geo_nvar: ADM1_NAME
    geo_name: Kemerovskaya Oblast
    source_row: 13179
  - survey_labels: 33 - Kirov oblast | 33 – Kirov oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2519
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2519'
    geo_nvar: ADM1_NAME
    geo_name: Kirovskaya Oblast
    source_row: 13180
  - survey_labels: 34 - Kostroma oblast | 34 – Kostroma oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2523
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2523'
    geo_nvar: ADM1_NAME
    geo_name: Kostromskaya Oblast
    source_row: 13181
  - survey_labels: 36 - Samara oblast | 36 – Samara oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2553
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2553'
    geo_nvar: ADM1_NAME
    geo_name: Samarskaya Oblast
    source_row: 13182
  - survey_labels: 37 - Kurgan oblast | 37 – Kurgan oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2526
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2526'
    geo_nvar: ADM1_NAME
    geo_name: Kurganskaya Oblast
    source_row: 13183
  - survey_labels: 38 - Kursk oblast | 38 – Kursk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2527
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2527'
    geo_nvar: ADM1_NAME
    geo_name: Kurskaya Oblast
    source_row: 13184
  - survey_labels: 4 - Krasnoyarsk krai | 4 – Krasnoyarsk krai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAULx_4
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '4'
    geo_nvar: ADM1_NAME
    geo_name: Evenkiyskiy Okrug & Krasnoyarskiy Kray & Taymyrskiy Okrug
    source_row: 13185
  - survey_labels: 40 - St. Petersburg city | 40 – St. Petersburg city
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2554
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2554'
    geo_nvar: ADM1_NAME
    geo_name: Sankt-peterburg
    source_row: 13186
  - survey_labels: 41 - Leningrad oblast | 41 – Leningrad oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2529
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2529'
    geo_nvar: ADM1_NAME
    geo_name: Leningradskaya Oblast
    source_row: 13187
  - survey_labels: 42 - Lipetsk oblast | 42 – Lipetsk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2530
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2530'
    geo_nvar: ADM1_NAME
    geo_name: Lipetskaya Oblast
    source_row: 13188
  - survey_labels: 44 - Magadan oblast | 44 – Magadan oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2531
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2531'
    geo_nvar: ADM1_NAME
    geo_name: Magadanskaya Oblast
    source_row: 13189
  - survey_labels: 45 - Moscow city | 45 – Moscow city
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2535
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2535'
    geo_nvar: ADM1_NAME
    geo_name: Moskva
    source_row: 13190
  - survey_labels: 46 - Moskow oblast | 46 – Moskow oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2534
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2534'
    geo_nvar: ADM1_NAME
    geo_name: Moskovskaya Oblast
    source_row: 13191
  - survey_labels: 47 - Murmansk oblast | 47 – Murmansk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2536
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2536'
    geo_nvar: ADM1_NAME
    geo_name: Murmanskaya Oblast
    source_row: 13192
  - survey_labels: 49 - Novgorod oblast | 49 – Novgorod oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2540
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2540'
    geo_nvar: ADM1_NAME
    geo_name: Novgorodskaya Oblast
    source_row: 13193
  - survey_labels: 5 - Primorskii krai | 5 – Primorskii krai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2547
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2547'
    geo_nvar: ADM1_NAME
    geo_name: Primorskiy Kray
    source_row: 13194
  - survey_labels: 50 - Novosibirsk oblast | 50 – Novosibirsk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2541
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2541'
    geo_nvar: ADM1_NAME
    geo_name: Novosibirskaya Oblast
    source_row: 13195
  - survey_labels: 52 - Omsk oblast | 52 – Omsk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2542
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2542'
    geo_nvar: ADM1_NAME
    geo_name: Omskaya Oblast
    source_row: 13196
  - survey_labels: 53 - Orenburg oblast | 53 – Orenburg oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2543
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2543'
    geo_nvar: ADM1_NAME
    geo_name: Orenburgskaya Oblast
    source_row: 13197
  - survey_labels: 54 - Oryol oblast | 54 – Oryol oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2544
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2544'
    geo_nvar: ADM1_NAME
    geo_name: Orlovskaya Oblast
    source_row: 13198
  - survey_labels: 56 - Penza oblast | 56 – Penza oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2545
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2545'
    geo_nvar: ADM1_NAME
    geo_name: Penzenskaya Oblast
    source_row: 13199
  - survey_labels: 57 - Perm krai | 57 – Perm krai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAULx_57
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '57'
    geo_nvar: ADM1_NAME
    geo_name: Komi-permyatskiy Okrug & Permskaya Oblast
    source_row: 13200
  - survey_labels: 58 - Pskov oblast | 58 – Pskov oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2548
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2548'
    geo_nvar: ADM1_NAME
    geo_name: Pskovskaya Oblast
    source_row: 13201
  - survey_labels: 60 - Rostov oblast | 60 – Rostov oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2549
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2549'
    geo_nvar: ADM1_NAME
    geo_name: Rostovskaya Oblast
    source_row: 13202
  - survey_labels: 61 - Ryazan oblast | 61 – Ryazan oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2550
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2550'
    geo_nvar: ADM1_NAME
    geo_name: Ryazanskaya Oblast
    source_row: 13203
  - survey_labels: 63 - Saratov oblast | 63 – Saratov oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2555
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2555'
    geo_nvar: ADM1_NAME
    geo_name: Saratovskaya Oblast
    source_row: 13204
  - survey_labels: 64 - Sakhalin oblast | 64 – Sakhalin oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2552
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2552'
    geo_nvar: ADM1_NAME
    geo_name: Sakhalinskaya Oblast
    source_row: 13205
  - survey_labels: 65 - Sverdlovsk oblast | 65 – Sverdlovsk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2559
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2559'
    geo_nvar: ADM1_NAME
    geo_name: Sverdlovskaya Oblast
    source_row: 13206
  - survey_labels: 66 - Smolensk oblast | 66 – Smolensk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2557
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2557'
    geo_nvar: ADM1_NAME
    geo_name: Smolenskaya Oblast
    source_row: 13207
  - survey_labels: 68 - Tambov oblast | 68 – Tambov oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2560
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2560'
    geo_nvar: ADM1_NAME
    geo_name: Tambovskaya Oblast
    source_row: 13208
  - survey_labels: 69 - Tomsk oblast | 69 – Tomsk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2563
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2563'
    geo_nvar: ADM1_NAME
    geo_name: Tomskaya Oblast
    source_row: 13209
  - survey_labels: 7 - Stavropol krai | 7 – Stavropol krai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2558
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2558'
    geo_nvar: ADM1_NAME
    geo_name: Stavropolskiy Kray
    source_row: 13210
  - survey_labels: 70 - Tula oblast | 70 – Tula oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2564
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2564'
    geo_nvar: ADM1_NAME
    geo_name: Tulskaya Oblast
    source_row: 13211
  - survey_labels: 71 - Tyumen oblast | 71 – Tyumen oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAULx_71
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '71'
    geo_nvar: ADM1_NAME
    geo_name: Khanty-mansyiskiy Okrug & Tyumenskaya Oblast & Yamalo-nenetskiy Okrug
    source_row: 13212
  - survey_labels: 73 - Ulyanovsk oblast | 73 – Ulyanovsk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2569
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2569'
    geo_nvar: ADM1_NAME
    geo_name: Ulyanovskaya Oblast
    source_row: 13213
  - survey_labels: 75 - Chelyabinsk oblast | 75 – Chelyabinsk oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2499
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2499'
    geo_nvar: ADM1_NAME
    geo_name: Chelyabinskaya Oblast
    source_row: 13214
  - survey_labels: 76 - Zabaikalskiy krai | 76 – Zabaikalskiy krai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAULx_76
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '76'
    geo_nvar: ADM1_NAME
    geo_name: Aginskiy Buryatskiy A. Okrug & Chitinskaya Oblast
    source_row: 13215
  - survey_labels: 77 - Chukotka autonomous okrug | 77 – Chukotka autonomous okrug
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2501
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2501'
    geo_nvar: ADM1_NAME
    geo_name: Chukotskiy Okrug
    source_row: 13216
  - survey_labels: 78 - Yaroslavl oblast | 78 – Yaroslavl oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2576
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2576'
    geo_nvar: ADM1_NAME
    geo_name: Yaroslavskaya Oblast
    source_row: 13217
  - survey_labels: 79 - Adygeya republic | 79 – Adygeya republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2487
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2487'
    geo_nvar: ADM1_NAME
    geo_name: Adygeya Rep.
    source_row: 13218
  - survey_labels: 8 - Khabarovsk krai | 8 – Khabarovsk krai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2516
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2516'
    geo_nvar: ADM1_NAME
    geo_name: Khabarovskiy Kray
    source_row: 13219
  - survey_labels: 80 - Bashkortostan republic | 80 – Bashkortostan republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2494
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2494'
    geo_nvar: ADM1_NAME
    geo_name: Bashkortostan Rep.
    source_row: 13220
  - survey_labels: 81 - Buryat republic | 81 – Buryat republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2497
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2497'
    geo_nvar: ADM1_NAME
    geo_name: Buryatiya Rep.
    source_row: 13221
  - survey_labels: 82 - Dagestan republic | 82 – Dagestan republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2503
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2503'
    geo_nvar: ADM1_NAME
    geo_name: Dagestan Rep.
    source_row: 13222
  - survey_labels: 83 - Kabardino-Balkar republic | 83 – Kabardino-Balkar republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2508
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2508'
    geo_nvar: ADM1_NAME
    geo_name: Kabardino-balkariya Rep.
    source_row: 13223
  - survey_labels: 84 - Altai republic | 84 – Altai republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2489
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2489'
    geo_nvar: ADM1_NAME
    geo_name: Altay Rep.
    source_row: 13224
  - survey_labels: 85 - Kalmyk republic | 85 – Kalmyk republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2510
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2510'
    geo_nvar: ADM1_NAME
    geo_name: Kalmykiya Rep.
    source_row: 13225
  - survey_labels: 86 - Karelia republic | 86 – Karelia republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2514
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2514'
    geo_nvar: ADM1_NAME
    geo_name: Karelya Rep.
    source_row: 13226
  - survey_labels: 87 - Komi republic | 87 – Komi republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2520
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2520'
    geo_nvar: ADM1_NAME
    geo_name: Komi Rep.
    source_row: 13227
  - survey_labels: 88 - Mari-El republic | 88 – Mari-El republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2532
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2532'
    geo_nvar: ADM1_NAME
    geo_name: Mariy-el Rep.
    source_row: 13228
  - survey_labels: 89 - Mordovia republic | 89 – Mordovia republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2533
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2533'
    geo_nvar: ADM1_NAME
    geo_name: Mordoviya Rep.
    source_row: 13229
  - survey_labels: 90 - North Osetiya republic | 90 – North Osetiya republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2556
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2556'
    geo_nvar: ADM1_NAME
    geo_name: Severnaya Osetiya-alaniya Rep.
    source_row: 13230
  - survey_labels: 91 - Karachaevo-Cherkess republic | 91 – Karachaevo-Cherkess republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2513
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2513'
    geo_nvar: ADM1_NAME
    geo_name: Karatchayevo-cherkesiya Rep.
    source_row: 13231
  - survey_labels: 92 - Tatarstan republic | 92 – Tatarstan republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2561
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2561'
    geo_nvar: ADM1_NAME
    geo_name: Tatarstan Rep.
    source_row: 13232
  - survey_labels: 93 - Tuva republic | 93 – Tuva republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2567
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2567'
    geo_nvar: ADM1_NAME
    geo_name: Tyva Rep.
    source_row: 13233
  - survey_labels: 94 - Udmurtia Republic | 94 – Udmurtia Republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2568
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2568'
    geo_nvar: ADM1_NAME
    geo_name: Udmurtiya Rep.
    source_row: 13234
  - survey_labels: 95 - Khakasia republic | 95 – Khakasia republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2517
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2517'
    geo_nvar: ADM1_NAME
    geo_name: Khakasiya Rep.
    source_row: 13235
  - survey_labels: 97 - Chuvash republic | 97 – Chuvash republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2502
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2502'
    geo_nvar: ADM1_NAME
    geo_name: Chuvashiya Rep.
    source_row: 13236
  - survey_labels: 98 - Sakha (Yakutia) republic | 98 – Sakha (Yakutia) republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2551
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2551'
    geo_nvar: ADM1_NAME
    geo_name: Sakha Rep.
    source_row: 13237
  - survey_labels: 99 - Evrei autonomous oblast | 99 – Evrei autonomous oblast
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2577
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2577'
    geo_nvar: ADM1_NAME
    geo_name: Yevreyskaya A. Oblast
    source_row: 13238
  - survey_labels: 96 – Chechnya republic
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: RUS_2015_GAUL1_2498
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2498'
    geo_nvar: ADM1_NAME
    geo_name: Chechnya Rep.
    source_row: 13323
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2022
  effective_to: null
  selectors: null
  value:
  - survey_labels: 1 - Central Federal Okrug
    survey_variables: subnatid
    gmd_subnatid1: RUS_2022_UN1_RU001
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: RUS_2022_UN1_RU001
    geo_year: '2022'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: RU001
    geo_nvar: ADM1_EN
    geo_name: Central Federal District
    source_row: 13152
  - survey_labels: 2 - North-Western Federal Okrug
    survey_variables: subnatid
    gmd_subnatid1: RUS_2022_UN1_RU004
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: RUS_2022_UN1_RU004
    geo_year: '2022'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: RU004
    geo_nvar: ADM1_EN
    geo_name: Northwestern Federal District
    source_row: 13153
  - survey_labels: 3 - Southern Federal Okrug
    survey_variables: subnatid
    gmd_subnatid1: RUS_2022_UN1_RU006
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: RUS_2022_UN1_RU006
    geo_year: '2022'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: RU006
    geo_nvar: ADM1_EN
    geo_name: South federal district
    source_row: 13154
  - survey_labels: 4 - North-Caucas Federal Okrug
    survey_variables: subnatid
    gmd_subnatid1: RUS_2022_UN1_RU003
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: RUS_2022_UN1_RU003
    geo_year: '2022'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: RU003
    geo_nvar: ADM1_EN
    geo_name: North Caucasus federal district
    source_row: 13155
  - survey_labels: 5 - Volga Federal Okrug
    survey_variables: subnatid
    gmd_subnatid1: RUS_2022_UN1_RU008
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: RUS_2022_UN1_RU008
    geo_year: '2022'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: RU008
    geo_nvar: ADM1_EN
    geo_name: Volga Federal District
    source_row: 13156
  - survey_labels: 6 - Ural Federal Okrug
    survey_variables: subnatid
    gmd_subnatid1: RUS_2022_UN1_RU007
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: RUS_2022_UN1_RU007
    geo_year: '2022'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: RU007
    geo_nvar: ADM1_EN
    geo_name: Ural Federal District
    source_row: 13157
  - survey_labels: 7 - Siberia Federal Okrug
    survey_variables: subnatid
    gmd_subnatid1: RUS_2022_UN1_RU005
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: RUS_2022_UN1_RU005
    geo_year: '2022'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: RU005
    geo_nvar: ADM1_EN
    geo_name: Siberian Federal District
    source_row: 13158
  - survey_labels: 8 - Far East Federal Okrug
    survey_variables: subnatid
    gmd_subnatid1: RUS_2022_UN1_RU002
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: RUS_2022_UN1_RU002
    geo_year: '2022'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: RU002
    geo_nvar: ADM1_EN
    geo_name: Far Eastern Federal District
    source_row: 13159
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: null
  effective_to: 2014
  selectors:
    geo_year: unknown
  value:
  - survey_labels: 13 – | 72 – | 74 –
    survey_variables: subnatidsurvey
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
    geo_year: ''
    geo_source: ''
    geo_level: ''
    geo_idvar: ''
    geo_id: ''
    geo_nvar: ''
    geo_name: ''
    source_row: 13331
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
  - source_category_code: central_sewerage
    national_label_en: Central sewerage
    national_label_local: в трубопроводную канализационную систему
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - source_category_code: private_domestic_connection_to_sewage_system
    national_label_en: Private domestic connection to sewage system
    national_label_local: в трубопроводную канализационную систему
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - source_category_code: private_flush_to_septic_tank
    national_label_en: Private flush to septic tank
    national_label_local: в септиктенк
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - source_category_code: shared_domestic_connection_to_sewage_system
    national_label_en: Shared domestic connection to sewage system
    national_label_local: в трубопроводную канализационную систему
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - source_category_code: shared_flush_to_septic_tank
    national_label_en: Shared flush to septic tank
    national_label_local: в септиктенк
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 80
  - source_category_code: central_sewerage
    national_label_en: Central sewerage
    national_label_local: в трубопроводную канализационную систему
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - source_category_code: housing_central_sewerage
    national_label_en: housing central sewerage
    national_label_local: в трубопроводную канализационную систему
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - source_category_code: indoor_sewerage
    national_label_en: Indoor sewerage
    national_label_local: в трубопроводную канализационную систему
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - source_category_code: connection_to_septic_tank
    national_label_en: Connection to septic tank
    national_label_local: в септиктенк
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - source_category_code: septic_tank
    national_label_en: Septic tank
    national_label_local: в септиктенк
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - source_category_code: bucket_latrine_where_fresh_excreta_are_manually_removed
    national_label_en: Bucket latrine (where fresh excreta are manually removed)
    national_label_local: Уборная с отхожим ведром
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - source_category_code: uncovered_dry_latrine_without_privacy
    national_label_en: Uncovered dry latrine (without privacy)
    national_label_local: Уборная с выгребной ямой без напольной плиты/с открытой
      выгребной ямой
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - source_category_code: private_covered_dry_latrine_with_privacy
    national_label_en: Private covered dry latrine (with privacy)
    national_label_local: Уборная с выгребной ямой с напольной плитой/с крытой выгребной
      ямой
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - source_category_code: shared_covered_dry_latrine_with_privacy
    national_label_en: Shared covered dry latrine (with privacy)
    national_label_local: Уборная с выгребной ямой с напольной плитой/с крытой выгребной
      ямой
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - source_category_code: private_pour_flush_latrine
    national_label_en: Private pour flush latrine
    national_label_local: Собственная уборная с промывом вручную
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 91
  - source_category_code: shared_pour_flush_latrine
    national_label_en: Shared pour flush latrine
    national_label_local: Общественная/совместного пользования уборная с промывом
      вручную
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 97
  - source_category_code: no_facilities_open_defecation
    national_label_en: No facilities (open defecation)
    national_label_local: Сооружений нет, кусты, поле
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - source_category_code: no_central_sewerage
    national_label_en: no central sewerage
    national_label_local: Другое
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - source_category_code: no_sewerage_and_no_septic
    national_label_en: No sewerage and no septic
    national_label_local: Другое
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - source_category_code: other
    national_label_en: Other
    national_label_local: Другое
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - source_category_code: shared_open_body_of_water_other
    national_label_en: Shared, open body of water, other
    national_label_local: Другое
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_RUS_Russian_Federation_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - source_category_code: natural_spring
    national_label_en: Natural spring
    national_label_local: Все родники
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 74
  - source_category_code: spring
    national_label_en: Spring
    national_label_local: Все родники
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 74
  - source_category_code: well_or_pump
    national_label_en: Well or pump
    national_label_local: Все колодцы
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 54
  - source_category_code: private_well
    national_label_en: Private well
    national_label_local: Частный
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 55
  - source_category_code: communal_well
    national_label_en: Communal well
    national_label_local: Общественный
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 56
  - source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: Защищённые колодцы или родники
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: true
    shared_flag: false
    source_row: 46
  - source_category_code: well_by_the_house
    national_label_en: Well by the house
    national_label_local: Частный
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 63
  - source_category_code: communal_water_well
    national_label_en: Communal water well
    national_label_local: Общественный
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 64
  - source_category_code: communal_water_pump
    national_label_en: Communal water pump
    national_label_local: Трубчатый колодец, скважина
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - source_category_code: protected_tube_well_or_bore_hole
    national_label_en: Protected tube well or bore hole
    national_label_local: Трубчатый колодец, скважина
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: Незащищённые колодцы или родники
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 50
  - source_category_code: independent_water_supply
    national_label_en: independent water supply
    national_label_local: Другое
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - source_category_code: distributor_and_other
    national_label_en: Distributor and other
    national_label_local: Доставляется автоцистерной
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - source_category_code: tanker_truck_vendor
    national_label_en: Tanker-truck, vendor
    national_label_local: Доставляется автоцистерной
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - source_category_code: no_central_water
    national_label_en: No central water
    national_label_local: Другое
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - source_category_code: no_centralised_no_independent_in_house
    national_label_en: no centralised/no independent in house
    national_label_local: Другое
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - source_category_code: other
    national_label_en: Other
    national_label_local: Другое
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - source_category_code: river_lake_pond_distributor_and_other
    national_label_en: River, lake, pond, Distributor and other
    national_label_local: Другое
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Бутилированная вода
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: Крытая цистерна/резервуар
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - source_category_code: river_lake_pond
    national_label_en: River, lake, pond
    national_label_local: Поверхностная вода
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - source_category_code: water_taken_directly_from_pond_water_or_stream
    national_label_en: Water taken directly from pond-water or stream
    national_label_local: Поверхностная вода
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - source_category_code: central_water
    national_label_en: Central water
    national_label_local: Подключения к дому
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - source_category_code: home_has_central_water_supply
    national_label_en: Home has central water supply
    national_label_local: Подключения к дому
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - source_category_code: housing_central_water
    national_label_en: housing-central water
    national_label_local: Подключения к дому
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - source_category_code: indoor_plumbing
    national_label_en: Indoor plumbing
    national_label_local: Подключения к дому
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Подключения к дому
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - source_category_code: running_water_in_house
    national_label_en: Running water in house
    national_label_local: Подключения к дому
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - source_category_code: tap_in_house
    national_label_en: Tap in house
    national_label_local: Подключения к дому
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - source_category_code: water_valve
    national_label_en: Water valve
    national_label_local: Подключения к дому
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - source_category_code: outdoor_plumbing_by_the_house
    national_label_en: Outdoor plumbing, by the house
    national_label_local: Общественный кран, колонка
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - source_category_code: public_standpipe
    national_label_en: Public standpipe
    national_label_local: Общественный кран, колонка
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - source_category_code: standpipe
    national_label_en: Standpipe
    national_label_local: Общественный кран, колонка
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_RUS_Russian_Federation_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---
