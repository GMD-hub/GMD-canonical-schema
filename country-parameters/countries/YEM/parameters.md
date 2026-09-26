---
country_id: CTY-YEM
iso3: YEM
schema_version: '0.2'
status: draft
country_name: YEM
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: YEM-EDU-01
    national_label_en: Nursery
    national_label_local: حضانة
    entry_age: 0
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 8
  - country_entry_id: YEM-EDU-02
    national_label_en: Preparatory
    national_label_local: ما قبل المدرسي
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 9
  - country_entry_id: YEM-EDU-03
    national_label_en: Basic education (Grade 1-6)
    national_label_local: التعليم الأساسي (الصفوف من 1-6)
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 10
  - country_entry_id: YEM-EDU-04
    national_label_en: Basic education (Grade 7-9)
    national_label_local: التعليم الأساسي (الصفوف من 7-9)
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
  - country_entry_id: YEM-EDU-05
    national_label_en: Secondary education
    national_label_local: التعليم الثانوي
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: YEM-EDU-06
    national_label_en: Technical secondary
    national_label_local: الثانوية التقنية
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
  - country_entry_id: YEM-EDU-07
    national_label_en: Technical and vocational education
    national_label_local: التعليم المهني والفني
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
  - country_entry_id: YEM-EDU-08
    national_label_en: Bachelor's programme
    national_label_local: برامج البكالوريوس
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - country_entry_id: YEM-EDU-09
    national_label_en: Post graduate diploma
    national_label_local: دبلوم بعد الجامعة
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: YEM-EDU-10
    national_label_en: Medicine programme
    national_label_local: برنامج الطب
    entry_age: 18
    duration_years: 7
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: YEM-EDU-11
    national_label_en: Master's programmes
    national_label_local: برامج الماجستير
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - country_entry_id: YEM-EDU-12
    national_label_en: Doctoral programmes
    national_label_local: برامج الدكتوراه
    entry_age: 24
    duration_years: 2
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Yemen.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: YEM-SUBNAT-01
    survey_labels: 11 - ibb
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3419
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3419
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3419'
    geo_nvar: ADM1_NAME
    geo_name: Ibb
    source_row: 18634
  - country_entry_id: YEM-SUBNAT-02
    survey_labels: 12 - abyan
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3407
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3407
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3407'
    geo_nvar: ADM1_NAME
    geo_name: Abyan
    source_row: 18635
  - country_entry_id: YEM-SUBNAT-03
    survey_labels: 13 - sanaa city
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_144969
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_144969
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '144969'
    geo_nvar: ADM1_NAME
    geo_name: Amanat Al Asimah
    source_row: 18636
  - country_entry_id: YEM-SUBNAT-04
    survey_labels: 14 - al-baida
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3410
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3410
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3410'
    geo_nvar: ADM1_NAME
    geo_name: Al Bayda
    source_row: 18637
  - country_entry_id: YEM-SUBNAT-05
    survey_labels: 15 - taiz
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3425
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3425
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3425'
    geo_nvar: ADM1_NAME
    geo_name: Taizz
    source_row: 18638
  - country_entry_id: YEM-SUBNAT-06
    survey_labels: 16 - al-jawf
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3412
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3412
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3412'
    geo_nvar: ADM1_NAME
    geo_name: Al Jawf
    source_row: 18639
  - country_entry_id: YEM-SUBNAT-07
    survey_labels: 17 - hajja
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3418
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3418
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3418'
    geo_nvar: ADM1_NAME
    geo_name: Hajjah
    source_row: 18640
  - country_entry_id: YEM-SUBNAT-08
    survey_labels: 18 - al-hodeida
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3411
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3411
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3411'
    geo_nvar: ADM1_NAME
    geo_name: Al Hudaydah
    source_row: 18641
  - country_entry_id: YEM-SUBNAT-09
    survey_labels: 19 - hadramout
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_144970
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_144970
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '144970'
    geo_nvar: ADM1_NAME
    geo_name: Hadramaut
    source_row: 18642
  - country_entry_id: YEM-SUBNAT-10
    survey_labels: 20 - dhamar
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3416
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3416
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3416'
    geo_nvar: ADM1_NAME
    geo_name: Dhamar
    source_row: 18643
  - country_entry_id: YEM-SUBNAT-11
    survey_labels: 21 - shabwah
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3424
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3424
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3424'
    geo_nvar: ADM1_NAME
    geo_name: Shabwah
    source_row: 18644
  - country_entry_id: YEM-SUBNAT-12
    survey_labels: 22 - saadah
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3422
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3422
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3422'
    geo_nvar: ADM1_NAME
    geo_name: Sa'ada
    source_row: 18645
  - country_entry_id: YEM-SUBNAT-13
    survey_labels: 23 - sanaa region
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_144972
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_144972
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '144972'
    geo_nvar: ADM1_NAME
    geo_name: Sana'a
    source_row: 18646
  - country_entry_id: YEM-SUBNAT-14
    survey_labels: 24 - aden
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_144973
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_144973
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '144973'
    geo_nvar: ADM1_NAME
    geo_name: Aden
    source_row: 18647
  - country_entry_id: YEM-SUBNAT-15
    survey_labels: 25 - laheg
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3420
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3420
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3420'
    geo_nvar: ADM1_NAME
    geo_name: Lahj
    source_row: 18648
  - country_entry_id: YEM-SUBNAT-16
    survey_labels: 26 - mareb
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3421
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3421
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3421'
    geo_nvar: ADM1_NAME
    geo_name: Marib
    source_row: 18649
  - country_entry_id: YEM-SUBNAT-17
    survey_labels: 27 - al-mahweet
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3414
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3414
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3414'
    geo_nvar: ADM1_NAME
    geo_name: Al Mahwit
    source_row: 18650
  - country_entry_id: YEM-SUBNAT-18
    survey_labels: 28 - al-maharh
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3413
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3413
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3413'
    geo_nvar: ADM1_NAME
    geo_name: Al Maharah
    source_row: 18651
  - country_entry_id: YEM-SUBNAT-19
    survey_labels: 29 - amran
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3415
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3415
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3415'
    geo_nvar: ADM1_NAME
    geo_name: Amran
    source_row: 18652
  - country_entry_id: YEM-SUBNAT-20
    survey_labels: 30 - al-dhale
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_3408
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_3408
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '3408'
    geo_nvar: ADM1_NAME
    geo_name: Al Dhale'e
    source_row: 18653
  - country_entry_id: YEM-SUBNAT-21
    survey_labels: 31 - remah
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAUL1_144971
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAUL1_144971
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '144971'
    geo_nvar: ADM1_NAME
    geo_name: Raymah
    source_row: 18654
  - country_entry_id: YEM-SUBNAT-22
    survey_labels: 19 - hadramout
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAULx_144970
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAULx_144970
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: ADM1_CODE
    geo_id: '144970'
    geo_nvar: ADM1_NAME
    geo_name: Hadramaut
    source_row: 18663
  - country_entry_id: YEM-SUBNAT-23
    survey_labels: 31 - socatra
    survey_variables: subnatid
    gmd_subnatid1: YEM_2015_GAULx_31
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: YEM_2015_GAULx_31
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '31'
    geo_nvar: ADM1_NAME
    geo_name: Hidaybu & Qulensya Wa Abd Al Kuri
    source_row: 18676
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
  - country_entry_id: YEM-SAN-01
    source_category_code: flsuh_to_somewhere_else
    national_label_en: flsuh to somewhere else
    national_label_local: إلى مكان آخر
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: YEM-SAN-02
    source_category_code: to_open_drain
    national_label_en: to open drain
    national_label_local: إلى مكان آخر
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: YEM-SAN-03
    source_category_code: flush_to_piped
    national_label_en: flush to piped
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: YEM-SAN-04
    source_category_code: flush_to_piped_sewer_system
    national_label_en: flush to piped sewer system
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: YEM-SAN-05
    source_category_code: to_piped_sewer_system
    national_label_en: to piped sewer system
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: YEM-SAN-06
    source_category_code: fluh_to_pit
    national_label_en: fluh to pit
    national_label_local: للحفر
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: YEM-SAN-07
    source_category_code: to_pit
    national_label_en: to pit
    national_label_local: للحفر
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: YEM-SAN-08
    source_category_code: flus_to_septic
    national_label_en: flus to septic
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: YEM-SAN-09
    source_category_code: flush_to_septic_tank
    national_label_en: flush to septic tank
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: YEM-SAN-10
    source_category_code: flush_to_dk_where
    national_label_en: flush to DK where
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: YEM-SAN-11
    source_category_code: to_unknown_place_not_sure_dk
    national_label_en: to unknown place/ not sure/DK
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: YEM-SAN-12
    source_category_code: street_toilet
    national_label_en: Street toilet
    national_label_local: عام / دافق مشترك / مرحاض
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: YEM-SAN-13
    source_category_code: toilet_connected_to_open_drainage
    national_label_en: Toilet connected to open drainage
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: YEM-SAN-14
    source_category_code: connected_flush_toilet
    national_label_en: Connected flush toilet
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: YEM-SAN-15
    source_category_code: flush_toilet_with_sewer
    national_label_en: Flush toilet with sewer
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: YEM-SAN-16
    source_category_code: public_network
    national_label_en: Public network
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: YEM-SAN-17
    source_category_code: disconnected_flush_toilet
    national_label_en: Disconnected flush toilet
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: YEM-SAN-18
    source_category_code: flush_toilet_without_sewer
    national_label_en: Flush toilet without sewer
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: YEM-SAN-19
    source_category_code: bucket
    national_label_en: Bucket
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: YEM-SAN-20
    source_category_code: bucket_toilet
    national_label_en: bucket toilet
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: YEM-SAN-21
    source_category_code: other_used_facility
    national_label_en: other used facility
    national_label_local: آخر
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: YEM-SAN-22
    source_category_code: improved_pit
    national_label_en: Improved pit
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: YEM-SAN-23
    source_category_code: pit_latrine_with_slab_covered_latrine
    national_label_en: Pit latrine with slab/covered latrine
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: YEM-SAN-24
    source_category_code: pit_with_slab
    national_label_en: pit with slab
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: YEM-SAN-25
    source_category_code: sealed_pit
    national_label_en: Sealed pit
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: YEM-SAN-26
    source_category_code: open_pit
    national_label_en: Open pit
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: YEM-SAN-27
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: YEM-SAN-28
    source_category_code: pit_without_slab
    national_label_en: pit without slab
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: YEM-SAN-29
    source_category_code: uncovered_toilet
    national_label_en: Uncovered toilet
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: YEM-SAN-30
    source_category_code: latrine_plus_pit
    national_label_en: latrine plus pit
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: YEM-SAN-31
    source_category_code: traditional_pit
    national_label_en: Traditional pit*
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: YEM-SAN-32
    source_category_code: improved_pit_with_ventilation
    national_label_en: Improved pit with ventilation
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: YEM-SAN-33
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated Improved Pit latrine
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: YEM-SAN-34
    source_category_code: pit
    national_label_en: Pit
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: YEM-SAN-35
    source_category_code: latrine_shared
    national_label_en: Latrine shared
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - country_entry_id: YEM-SAN-36
    source_category_code: flush_toilet
    national_label_en: Flush toilet
    national_label_local: مراحيض خاصة
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 91
  - country_entry_id: YEM-SAN-37
    source_category_code: in_the_nature
    national_label_en: In the nature
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: YEM-SAN-38
    source_category_code: no_facility_bush_field
    national_label_en: no facility, bush, field
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: YEM-SAN-39
    source_category_code: none
    national_label_en: None
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: YEM-SAN-40
    source_category_code: open_air
    national_label_en: Open air
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: YEM-SAN-41
    source_category_code: open_defecation
    national_label_en: Open defecation
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: YEM-SAN-42
    source_category_code: unavailable
    national_label_en: Unavailable
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: YEM-SAN-43
    source_category_code: improved_sanitation_facility_network_flush_toilet_vip_latrine_public_latrine
    national_label_en: Improved sanitation facility (network, flush toilet, VIP latrine,
      public latrine)
    national_label_local: آخر
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: YEM-SAN-44
    source_category_code: non_flush_but_with_severals_sewage_connections
    national_label_en: Non flush (But with severals sewage connections)
    national_label_local: آخر
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: YEM-SAN-45
    source_category_code: other
    national_label_en: Other
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: YEM-SAN-46
    source_category_code: other_unimproved_facility
    national_label_en: other unimproved  facility
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: YEM-SAN-47
    source_category_code: others
    national_label_en: Others
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: YEM-SAN-48
    source_category_code: unimproved_open_hole_tube_pipe_outside_house_other
    national_label_en: Unimproved (open hole, tube/pipe outside house, other)
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: YEM-SAN-49
    source_category_code: ambiguous_pit_latrine_closed_pit_latrine
    national_label_en: Ambiguous (pit latrine, closed pit latrine)
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_YEM_Yemen_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: YEM-WAS-01
    source_category_code: spring
    national_label_en: Spring
    national_label_local: كل الينابيع
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: YEM-WAS-02
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: YEM-WAS-03
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: YEM-WAS-04
    source_category_code: covered_well_spring
    national_label_en: Covered well/spring
    national_label_local: آبار أو ينابيع محمية
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: yes
    shared_flag: no
    source_row: 46
  - country_entry_id: YEM-WAS-05
    source_category_code: artesian_well
    national_label_en: Artesian well
    national_label_local: الآبار التقليدية
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: YEM-WAS-06
    source_category_code: well
    national_label_en: Well
    national_label_local: الآبار التقليدية
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: YEM-WAS-07
    source_category_code: well
    national_label_en: well
    national_label_local: آخر
    jmp_classification: Ground water > Traditional wells > Other
    jmp_id: ground_water.traditional_wells.other
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: YEM-WAS-08
    source_category_code: well_without_pump
    national_label_en: well without pump
    national_label_local: آخر
    jmp_classification: Ground water > Traditional wells > Other
    jmp_id: ground_water.traditional_wells.other
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: YEM-WAS-09
    source_category_code: artesian_well
    national_label_en: Artesian well
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: YEM-WAS-10
    source_category_code: tube_well_or_borehole
    national_label_en: tube well or borehole
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: YEM-WAS-11
    source_category_code: tubewell_borehole
    national_label_en: Tubewell, borehole
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: YEM-WAS-12
    source_category_code: tubewell_borehole
    national_label_en: Tubewell/borehole
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: YEM-WAS-13
    source_category_code: well_with_pump
    national_label_en: Well with pump
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: YEM-WAS-14
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: YEM-WAS-15
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: YEM-WAS-16
    source_category_code: unprotected_stream_well
    national_label_en: Unprotected stream/well
    national_label_local: الآبار أو الينابيع غير المحمية
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 50
  - country_entry_id: YEM-WAS-17
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank/drum
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: YEM-WAS-18
    source_category_code: container
    national_label_en: container
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: YEM-WAS-19
    source_category_code: private_owned_water_source
    national_label_en: private owned water source
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 104
  - country_entry_id: YEM-WAS-20
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: YEM-WAS-21
    source_category_code: tanker_truck_provided
    national_label_en: Tanker truck provided
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: YEM-WAS-22
    source_category_code: water_trucking
    national_label_en: Water trucking
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: YEM-WAS-23
    source_category_code: from_neighbours
    national_label_en: From neighbours
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: YEM-WAS-24
    source_category_code: other
    national_label_en: Other
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: YEM-WAS-25
    source_category_code: other
    national_label_en: Other
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: YEM-WAS-26
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: مياه معبأة
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: YEM-WAS-27
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: كيس ماء
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: YEM-WAS-28
    source_category_code: sachet_water
    national_label_en: Sachet water
    national_label_local: كيس ماء
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: YEM-WAS-29
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: مياه الأمطار
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: YEM-WAS-30
    source_category_code: covered_cistern
    national_label_en: Covered Cistern
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: YEM-WAS-31
    source_category_code: rainwater
    national_label_en: rainwater
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: YEM-WAS-32
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: YEM-WAS-33
    source_category_code: uncovered_cistern
    national_label_en: Uncovered Cistern
    national_label_local: خزان / خزان غير مغطى
    jmp_classification: Rainwater > Uncovered cistern/tank
    jmp_id: rainwater.uncovered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 88
  - country_entry_id: YEM-WAS-34
    source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: YEM-WAS-35
    source_category_code: surface_water_protected_and_unprotected
    national_label_en: surface water (protected and unprotected)
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: YEM-WAS-36
    source_category_code: dam
    national_label_en: Dam
    national_label_local: سد
    jmp_classification: Surface water > Dam
    jmp_id: surface_water.dam
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 95
  - country_entry_id: YEM-WAS-37
    source_category_code: dam_reservoir
    national_label_en: Dam, reservoir
    national_label_local: سد
    jmp_classification: Surface water > Dam
    jmp_id: surface_water.dam
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 95
  - country_entry_id: YEM-WAS-38
    source_category_code: open_pond
    national_label_en: Open pond
    national_label_local: آخر
    jmp_classification: Surface water > Other
    jmp_id: surface_water.other
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 99
  - country_entry_id: YEM-WAS-39
    source_category_code: uncovered_pond
    national_label_en: Uncovered pond
    national_label_local: آخر
    jmp_classification: Surface water > Other
    jmp_id: surface_water.other
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 99
  - country_entry_id: YEM-WAS-40
    source_category_code: covered_pond
    national_label_en: Covered Pond
    national_label_local: بركة ماء
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - country_entry_id: YEM-WAS-41
    source_category_code: stream
    national_label_en: Stream
    national_label_local: تدفق
    jmp_classification: Surface water > Stream
    jmp_id: surface_water.stream
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 97
  - country_entry_id: YEM-WAS-42
    source_category_code: stream_fountain
    national_label_en: Stream/fountain
    national_label_local: تدفق
    jmp_classification: Surface water > Stream
    jmp_id: surface_water.stream
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 97
  - country_entry_id: YEM-WAS-43
    source_category_code: stream_spring_water
    national_label_en: stream/spring water
    national_label_local: تدفق
    jmp_classification: Surface water > Stream
    jmp_id: surface_water.stream
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 97
  - country_entry_id: YEM-WAS-44
    source_category_code: cooperative_network
    national_label_en: cooperative network
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: YEM-WAS-45
    source_category_code: local_network
    national_label_en: local network
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: YEM-WAS-46
    source_category_code: piped_to_neighbour
    national_label_en: Piped to neighbour
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: YEM-WAS-47
    source_category_code: piped_water
    national_label_en: Piped water
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: YEM-WAS-48
    source_category_code: private_network
    national_label_en: Private network
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: YEM-WAS-49
    source_category_code: private_project
    national_label_en: Private project
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: YEM-WAS-50
    source_category_code: government_project
    national_label_en: Government project
    national_label_local: اتصالات المنزل
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: YEM-WAS-51
    source_category_code: piped_into_residence
    national_label_en: Piped into Residence
    national_label_local: اتصالات المنزل
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: YEM-WAS-52
    source_category_code: government_network
    national_label_en: government network
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: YEM-WAS-53
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: YEM-WAS-54
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: YEM-WAS-55
    source_category_code: public_network
    national_label_en: Public network
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: YEM-WAS-56
    source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: YEM-WAS-57
    source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: YEM-WAS-58
    source_category_code: cooperative_network
    national_label_en: Cooperative network
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: YEM-WAS-59
    source_category_code: cooperative_project
    national_label_en: Cooperative project
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: YEM-WAS-60
    source_category_code: piped_outside
    national_label_en: Piped outside
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: YEM-WAS-61
    source_category_code: public_tap
    national_label_en: Public tap
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: YEM-WAS-62
    source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: YEM-WAS-63
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: YEM-WAS-64
    source_category_code: public_top_outside_the_house
    national_label_en: public top outside the house
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_YEM_Yemen_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

