---
country_id: CTY-IRQ
iso3: IRQ
schema_version: '0.2'
status: draft
country_name: IRQ
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - national_label_en: Kindergarten
    national_label_local: رياض الأطفال
    entry_age: 4
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - national_label_en: Primary education
    national_label_local: التعليم الابتدائي
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
  - national_label_en: Adult primary education
    national_label_local: التعليم الابتدائي للكبار
    entry_age: 10
    duration_years: 3
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
  - national_label_en: Intermediate education
    national_label_local: التعليم المتوسط
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
  - national_label_en: Preparatory education
    national_label_local: التعليم الإعدادي
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - national_label_en: Vocational education
    national_label_local: التعليم المهني
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - national_label_en: Fine Arts Institutes Programs (First to third year)
    national_label_local: برامج معاهد الفنون الجميلة (سنة أولى إلى ثالثة)
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
  - national_label_en: Fine Arts Institutes Programs (Fourth and fifth Years)
    national_label_local: برامج معاهد الفنون الجميلة (سنة رابعة وخامسة)
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - national_label_en: Technical diploma
    national_label_local: دبلوم تقني
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - national_label_en: 4 years Bachelor's programmes
    national_label_local: برامج بكالوريوس 4 سنوات
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - national_label_en: 5 years Bachelor's programmes
    national_label_local: برامج بكالوريوس 5 سنوات
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - national_label_en: High diploma
    national_label_local: دبلوم عالي
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - national_label_en: Bachelor's in medicine
    national_label_local: بكالوريوس الطب
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  - national_label_en: Master's programmes
    national_label_local: برامج الماجستير
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
  - national_label_en: Doctoral programme
    national_label_local: برامج الدكتوراه
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Iraq.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - survey_labels: 11 - DUHOK | 11 - Duhouk
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1574
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1574
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1574'
    geo_nvar: ADM1_NAME
    geo_name: Dahuk
    source_row: 7846
  - survey_labels: 12 - NINEVEH | 12 - Nineveh
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1578
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1578
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1578'
    geo_nvar: ADM1_NAME
    geo_name: Ninewa
    source_row: 7847
  - survey_labels: 13 - SULAYMANIYAH | 13 - Suleimaniya
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1580
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1580
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1580'
    geo_nvar: ADM1_NAME
    geo_name: Sulaymaniyah
    source_row: 7848
  - survey_labels: 14 - KIRKUK | 14 - Karkouk
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1570
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1570
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1570'
    geo_nvar: ADM1_NAME
    geo_name: Kirkuk
    source_row: 7849
  - survey_labels: 15 - ERBIL | 15 - Erbil
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1569
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1569
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1569'
    geo_nvar: ADM1_NAME
    geo_name: Erbil
    source_row: 7850
  - survey_labels: 21 - DIYALA | 21 - Diala
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1575
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1575
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1575'
    geo_nvar: ADM1_NAME
    geo_name: Diyala
    source_row: 7851
  - survey_labels: 22 - AL-ANBAR | 22 - Al-Anbar
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1564
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1564
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1564'
    geo_nvar: ADM1_NAME
    geo_name: Anbar
    source_row: 7852
  - survey_labels: 23 - BAGHDAD | 23 - Baghdad
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1572
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1572
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1572'
    geo_nvar: ADM1_NAME
    geo_name: Baghdad
    source_row: 7853
  - survey_labels: 24 - BABYLON | 24 - Babil
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1571
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1571
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1571'
    geo_nvar: ADM1_NAME
    geo_name: Babil
    source_row: 7854
  - survey_labels: 25 - KARBALA | 25 - Kerbala
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1576
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1576
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1576'
    geo_nvar: ADM1_NAME
    geo_name: Kerbala
    source_row: 7855
  - survey_labels: 26 - WASIT | 26 - Wasit
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1581
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1581
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1581'
    geo_nvar: ADM1_NAME
    geo_name: Wassit
    source_row: 7856
  - survey_labels: 27 - SALAH AL-DIN | 27 - Salahuddin
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1579
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1579
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1579'
    geo_nvar: ADM1_NAME
    geo_name: Salah al-Din
    source_row: 7857
  - survey_labels: 28 - Al-Najaf | 28 - NAJAF
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1568
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1568
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1568'
    geo_nvar: ADM1_NAME
    geo_name: Najaf
    source_row: 7858
  - survey_labels: 31 - AL-QADISIYAH | 31 - Al-Qadisiya
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1567
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1567
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1567'
    geo_nvar: ADM1_NAME
    geo_name: Qadissiya
    source_row: 7859
  - survey_labels: 32 - Al-Muthanna | 32 - MUTHANNA
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1566
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1566
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1566'
    geo_nvar: ADM1_NAME
    geo_name: Muthanna
    source_row: 7860
  - survey_labels: 33 - DHI QAR | 33 - Thi-Qar
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1573
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1573
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1573'
    geo_nvar: ADM1_NAME
    geo_name: Thi-Qar
    source_row: 7861
  - survey_labels: 34 - MAYSAN | 34 - Missan
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1577
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1577
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1577'
    geo_nvar: ADM1_NAME
    geo_name: Missan
    source_row: 7862
  - survey_labels: 35 - BASRA | 35 - Basrah
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1565
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: IRQ_2015_GAUL1_1565
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1565'
    geo_nvar: ADM1_NAME
    geo_name: Basrah
    source_row: 7863
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
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: مرحاض سماد (خاص)
    jmp_classification: Composting toilets > Composting toilet (private)
    jmp_id: composting_toilets.composting_toilet_private
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 129
  - source_category_code: flush_pour_flush_to_somewhere_else
    national_label_en: Flush/pour flush to somewhere else
    national_label_local: إلى مكان آخر
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - source_category_code: public_network_covered_drain
    national_label_en: Public network+covered drain
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - source_category_code: flush_pour_flush_to_pit_latrine
    national_label_en: Flush/pour flush to pit latrine
    national_label_local: للحفر
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - source_category_code: flush_pour_flush_to_septic_tank
    national_label_en: Flush/pour flush to septic tank
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - source_category_code: septic_tank
    national_label_en: Septic tank
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - source_category_code: flush_to_unknown_place_not_sure_dk_where
    national_label_en: Flush to unknown place/not sure/DK where
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - source_category_code: flush_to_sewage_system_septic_tank
    national_label_en: Flush to sewage system/septic tank
    national_label_local: دافق / مراحيض
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - source_category_code: flush_toilet_inside_outside_dwelling_exclusive_use_of_the_household
    national_label_en: Flush toilet, inside/outside dwelling exclusive use of the
      household
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - source_category_code: flushed_toilet_inside_outside_dwelling_and_shared
    national_label_en: flushed toilet inside/outside dwelling and shared
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - source_category_code: flush_to_open_drain
    national_label_en: Flush to open drain
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit (latrine)
    national_label_local: للحفر
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - source_category_code: flush_pour_flush_to_pit_latrine_septic_tank
    national_label_en: Flush/pour flush to pit latrine (septic tank)
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - source_category_code: flush_to_unknown_place_not_sure_dk_where
    national_label_en: Flush to unknown place/not sure/DK where
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - source_category_code: flush_pour_flush_to_don_t_know_where
    national_label_en: Flush/pour flush to don't know where
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - source_category_code: bucket
    national_label_en: Bucket
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet/hanging latrine
    national_label_local: دورة مياه معلقة / مرحاض معلق
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - source_category_code: improved_pit_latrine
    national_label_en: Improved pit latrine
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - source_category_code: pit_latirne_with_slab
    national_label_en: Pit latirne with slab
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated improved pit latrine
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
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
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
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
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - source_category_code: traditional_pit_latrine
    national_label_en: Traditional pit latrine*
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
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
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - source_category_code: non_flush_toilet_inside_outside_dwelling_exclusive_use_of_the_household
    national_label_en: non Flush toilet, inside/outside dwelling exclusive use of
      the household
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - source_category_code: non_flush_toilet_inside_outside_dwelling_exclusive_and_shared
    national_label_en: non Flush toilet, inside/outside dwelling exclusive and shared
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - source_category_code: pour_flush_latrine
    national_label_en: Pour flush latrine
    national_label_local: صب المراحيض المتدفقة
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 85
  - source_category_code: no_facilities_or_bush_or_field
    national_label_en: No facilities or bush or field
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: no_facilities_bush_field
    national_label_en: No facilities/bush field
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: no_toilet
    national_label_en: No toilet
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: open_defecation_no_facility_bush_field
    national_label_en: Open defecation (no facility, bush, field)
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: other
    national_label_en: other
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - source_category_code: use_of_other_facility
    national_label_en: Use of other facility
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - source_category_code: other
    national_label_en: other
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_IRQ_Iraq_0.xlsx
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
    national_label_local: كل الينابيع
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - source_category_code: kehriz_man_built_spring
    national_label_en: Kehriz (man built spring)
    national_label_local: آخر
    jmp_classification: Ground water > All springs > Other
    jmp_id: ground_water.all_springs.other
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 77
  - source_category_code: open_well_covered_well
    national_label_en: open well / covered well
    national_label_local: كل الآبار
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 54
  - source_category_code: open_well_covered_well
    national_label_en: Open well/Covered well
    national_label_local: كل الآبار
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 54
  - source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - source_category_code: protected_dug_well
    national_label_en: Protected dug well
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - source_category_code: tube_well_bore_hole
    national_label_en: Tube well / bore-hole
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: tube_well_borehole_with_pump
    national_label_en: Tube well/Borehole with pump
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: tubewell_borehole
    national_label_en: Tubewell, borehole
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: tubewell_borehole
    national_label_en: Tubewell/borehole
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - source_category_code: unprotected_dug_well
    national_label_en: unprotected dug well
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - source_category_code: cart_with_small_tank
    national_label_en: Cart with small tank
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank/drum
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - source_category_code: cart_with_tank_drum
    national_label_en: Cart with tank / drum
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - source_category_code: reverse_osmosis
    national_label_en: Reverse Osmosis
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - source_category_code: water_kiosk
    national_label_en: Water kiosk
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - source_category_code: desalinized_water_and_sterilized_water
    national_label_en: Desalinized water and sterilized water
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 104
  - source_category_code: tanker
    national_label_en: Tanker
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: tanker_truck
    national_label_en: Tanker Truck
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: tanker_truck_vendor
    national_label_en: Tanker truck, vendor
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: tanker_truck
    national_label_en: Tanker-truck
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: other
    national_label_en: other
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: مياه معبأة
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - source_category_code: bottled_water_big_small
    national_label_en: Bottled water (big/small)
    national_label_local: مياه معبأة
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: كيس ماء
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - source_category_code: bottled_water_without_other_improved
    national_label_en: Bottled Water (without other improved)
    national_label_local: كيس ماء
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - source_category_code: rain_water_collection
    national_label_en: Rain water collection
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: rain_water
    national_label_en: Rain-water
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: pond_river_or_stream
    national_label_en: Pond, river, or stream
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: river_canal_creek_wheel
    national_label_en: river/canal/creek/ wheel
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: river_canal_creek_wheel
    national_label_en: River/Canal/creek/Wheel
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: pond_lake
    national_label_en: Pond/lake
    national_label_local: آخر
    jmp_classification: Surface water > Other
    jmp_id: surface_water.other
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 99
  - source_category_code: piped_to_neigbhour
    national_label_en: Piped to neigbhour
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - source_category_code: piped_water_to_neighbour
    national_label_en: Piped water to neighbour
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - source_category_code: hh_directly_linked_to_the_water_network
    national_label_en: HH directly linked to the water network
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: public_network_housing_unit_connected
    national_label_en: 'Public network: housing unit connected'
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: piped_into_the_yard_or_plot
    national_label_en: Piped into the yard or plot
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: piped_water_into_yard_plot
    national_label_en: Piped water into yard/plot
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: public_network_tap
    national_label_en: Public network tap
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: pubic_network_tap
    national_label_en: pubic network tap
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: public_tap
    national_label_en: Public tap
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: public_tap_stand_pipe
    national_label_en: Public tap / stand-pipe
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_IRQ_Iraq_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

