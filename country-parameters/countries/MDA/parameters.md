---
country_id: CTY-MDA
iso3: MDA
schema_version: '0.2'
status: draft
country_name: MDA
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MDA-EDU-01
    national_label_en: Early childhood development
    national_label_local: "Educa\u0163ie timpurie"
    entry_age: 1
    duration_years: 2
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
  - country_entry_id: MDA-EDU-02
    national_label_en: Pre-primary
    national_label_local: "\xCEnv\u0103\u0163\u0103m\xEEntul pre\u015Fcolar"
    entry_age: 3
    duration_years: 4
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: MDA-EDU-03
    national_label_en: Primary education
    national_label_local: "\xCEnv\u0103\u0163\u0103m\xEEntul primar"
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - MDA-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: MDA-EDU-04
    national_label_en: Gymnasium education, 1st cycle
    national_label_local: "\xCEnv\u0103\u0163\u0103m\xEEntul secundar, ciclul I (gimnazial)"
    entry_age: 11
    duration_years: 5
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - MDA-EDU-03
    cum_years_schooling: 9
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-05
    national_label_en: Secondary education, II cycle (lyceum)
    national_label_local: "\xCEnv\u0103\u0163\u0103m\xEEntul secundar, ciclul II (liceal)"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - MDA-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-06
    national_label_en: Secondary technical vocational education (related vocations)
    national_label_local: "\xCEnv\u0103\u0163\u0103m\xEEntul profesional tehnic secundar\
      \ (meserii conexe)"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - MDA-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-07
    national_label_en: Secondary technical vocational education (one or two vocations)
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xEEntul profesional tehnic secundar\
      \ (o meserie/dual)"
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - MDA-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-08
    national_label_en: Post-Secondary technical vocational education (Grades 1-2 of
      Secondary integrated programme)
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xEEntul profesional tehnic postsecundar\
      \ (primii 2 ani ai programului integrat)"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - MDA-EDU-04
    cum_years_schooling: 11
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-09
    national_label_en: Secondary technical vocational education
    national_label_local: "\xCEnv\u0103\u0163\u0103m\xEEntul profesional tehnic secundar"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - MDA-EDU-05
    cum_years_schooling: 13
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-05
    - MDA-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-10
    national_label_en: 'Postsecondary technical vocational education

      (Year 3 and 4 of the integrated program)'
    national_label_local: "\xCEnv\u0103\u0163\u0103m\xEEntul profesional tehnic postsecundar\
      \ \n(Anul 3 si 4 al programului integrat)"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - MDA-EDU-05
    cum_years_schooling: 14
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-05
    - MDA-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-11
    national_label_en: Higher education licentiate (1st cycle)
    national_label_local: "Studii superioare de licen\u0163\u0103 (Ciclul I)"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - MDA-EDU-05
    cum_years_schooling: 15
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-05
    - MDA-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-12
    national_label_en: Higher integrated education
    national_label_local: Studiile superioare integrate
    entry_age: 19
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - MDA-EDU-05
    cum_years_schooling: 18
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-05
    - MDA-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-13
    national_label_en: Higher education - Master (2nd cycle)
    national_label_local: Studii superioare de master (Ciclul II)
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - MDA-EDU-11
    cum_years_schooling: 17
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-05
    - MDA-EDU-11
    - MDA-EDU-13
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MDA-EDU-14
    national_label_en: Higher education - Doctorantura (3rd cycle)
    national_label_local: Studii superioare de doctorat (Ciclul III)
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - MDA-EDU-12
    - MDA-EDU-13
    cum_years_schooling: 20
    cum_years_computation_path:
    - MDA-EDU-03
    - MDA-EDU-04
    - MDA-EDU-05
    - MDA-EDU-11
    - MDA-EDU-13
    - MDA-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MDA-EDU-12, MDA-EDU-13'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Republic_of_Moldova.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MDA-SUBNAT-01
    survey_labels: "1 -  Nord | 1 - Nord | 1 \u2013 Nord"
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: MDA_2015_GAULx_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MDA_2015_GAULx_1
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '1'
    geo_nvar: ADM1_NAME
    geo_name: Balti & Edinet & Soroca
    source_row: 9269
  - country_entry_id: MDA-SUBNAT-02
    survey_labels: "2 -  Centru | 2 - Centru | 2 \u2013 Centru"
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: MDA_2015_GAULx_2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MDA_2015_GAULx_2
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '2'
    geo_nvar: ADM1_NAME
    geo_name: Orhei & Ungheni & Lapusna
    source_row: 9270
  - country_entry_id: MDA-SUBNAT-03
    survey_labels: "3 -  Sud | 3 - Sud | 3 \u2013 Sud"
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: MDA_2015_GAULx_3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MDA_2015_GAULx_3
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '3'
    geo_nvar: ADM1_NAME
    geo_name: Cahul & Gagauzia & Tighina
    source_row: 9271
  - country_entry_id: MDA-SUBNAT-04
    survey_labels: "4 -  Chisinau | 4 - Chisinau | 4 \u2013 Chisinau"
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: MDA_2015_GAUL1_2064
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MDA_2015_GAUL1_2064
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2064'
    geo_nvar: ADM1_NAME
    geo_name: Chisinau
    source_row: 9272
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
  - country_entry_id: MDA-SAN-01
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: "\u041A\u043E\u043C\u043F\u043E\u0441\u0442\u0438\u0440\u0443\
      \u044E\u0449\u0438\u0435 \u0442\u0443\u0430\u043B\u0435\u0442\u044B"
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: MDA-SAN-02
    source_category_code: composting_toilets
    national_label_en: composting toilets
    national_label_local: "\u041A\u043E\u043C\u043F\u043E\u0441\u0442\u0438\u0440\u0443\
      \u044E\u0449\u0438\u0435 \u0442\u0443\u0430\u043B\u0435\u0442\u044B"
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: MDA-SAN-03
    source_category_code: flush_pour_flush_to_elsewhere
    national_label_en: Flush/pour flush to elsewhere
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: MDA-SAN-04
    source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
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
  - country_entry_id: MDA-SAN-05
    source_category_code: public_system
    national_label_en: Public system
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
  - country_entry_id: MDA-SAN-06
    source_category_code: flush_pour_flush_to_pit
    national_label_en: Flush/pour flush to pit
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: MDA-SAN-07
    source_category_code: flush_pour_flush_to_septic_tank
    national_label_en: Flush/pour flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: MDA-SAN-08
    source_category_code: flush_pour_flush_to_unknown_place_not_sure_dk
    national_label_en: Flush/pour flush to unknown place/not sure/DK
    national_label_local: "\u0432 \u043D\u0435\u0438\u0437\u0432\u0435\u0441\u0442\
      \u043D\u043E\u0435 \u043C\u0435\u0441\u0442\u043E/\u043D\u0435 \u0437\u043D\u0430\
      \u044E/\u043D\u0435 \u0443\u0432\u0435\u0440\u0435\u043D(\u0430)"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: MDA-SAN-09
    source_category_code: flush_toilet
    national_label_en: flush toilet
    national_label_local: "\u0422\u0443\u0430\u043B\u0435\u0442\u044B \u0441\u043E\
      \ \u0441\u043C\u044B\u0432\u043E\u043C"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: MDA-SAN-10
    source_category_code: flush_to_piped_sewage_system
    national_label_en: Flush to piped sewage system
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
  - country_entry_id: MDA-SAN-11
    source_category_code: flush_to_sewage_system_septic_tank
    national_label_en: Flush to sewage system/ septic tank
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
  - country_entry_id: MDA-SAN-12
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
  - country_entry_id: MDA-SAN-13
    source_category_code: bucket_toilet
    national_label_en: bucket toilet
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u043E\
      \u0442\u0445\u043E\u0436\u0438\u043C \u0432\u0435\u0434\u0440\u043E\u043C"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: MDA-SAN-14
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet/hanging latrine
    national_label_local: "\u041F\u043E\u0434\u0432\u0435\u0441\u043D\u043E\u0439\
      \ \u0442\u0443\u0430\u043B\u0435\u0442/\u043F\u043E\u0434\u0432\u0435\u0441\u043D\
      \u0430\u044F \u0443\u0431\u043E\u0440\u043D\u0430\u044F"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: MDA-SAN-15
    source_category_code: improved_pit_latrine
    national_label_en: Improved pit latrine
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
  - country_entry_id: MDA-SAN-16
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
  - country_entry_id: MDA-SAN-17
    source_category_code: pit_latrine_with_slab_covered_latrine
    national_label_en: Pit latrine with slab/covered latrine
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
  - country_entry_id: MDA-SAN-18
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
  - country_entry_id: MDA-SAN-19
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
  - country_entry_id: MDA-SAN-20
    source_category_code: traditional_pit_latrine
    national_label_en: Traditional pit latrine*
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
  - country_entry_id: MDA-SAN-21
    source_category_code: pit_latrine_vip
    national_label_en: Pit Latrine - VIP
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
  - country_entry_id: MDA-SAN-22
    source_category_code: pit_latrine_ventilated
    national_label_en: pit latrine ventilated
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
  - country_entry_id: MDA-SAN-23
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
  - country_entry_id: MDA-SAN-24
    source_category_code: pour_flush_latrine
    national_label_en: Pour flush latrine
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u044B\u0435 \u0441\u043E\
      \ \u0441\u043C\u044B\u0432\u043E\u043C"
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 85
  - country_entry_id: MDA-SAN-25
    source_category_code: no_faciliity_bush_field
    national_label_en: no faciliity/bush/field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MDA-SAN-26
    source_category_code: no_facilities_bush_field
    national_label_en: No facilities/ bush/ field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MDA-SAN-27
    source_category_code: open_defecation_no_facility_bush_field
    national_label_en: Open defecation (no facility, bush, field)
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MDA-SAN-28
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: MDA-SAN-29
    source_category_code: 'no'
    national_label_en: 'No'
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: MDA-SAN-30
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
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MDA_Republic_of_Moldova_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MDA-WAS-01
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
  - country_entry_id: MDA-WAS-02
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
  - country_entry_id: MDA-WAS-03
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
  - country_entry_id: MDA-WAS-04
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
  - country_entry_id: MDA-WAS-05
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
  - country_entry_id: MDA-WAS-06
    source_category_code: artesian_well_with_pump
    national_label_en: artesian well with pump
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
  - country_entry_id: MDA-WAS-07
    source_category_code: tubewell_borehole
    national_label_en: Tubewell, borehole
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
  - country_entry_id: MDA-WAS-08
    source_category_code: tubewell_borehole_with_pump
    national_label_en: Tubewell/ borehole with pump
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
  - country_entry_id: MDA-WAS-09
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
  - country_entry_id: MDA-WAS-10
    source_category_code: unprotected_dug_well
    national_label_en: Unprotected dug well
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0439 \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MDA-WAS-11
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
  - country_entry_id: MDA-WAS-12
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank/drum
    national_label_local: "\u0422\u0435\u043B\u0435\u0436\u043A\u0430 \u0441 \u043D\
      \u0435\u0431\u043E\u043B\u044C\u0448\u0438\u043C \u0431\u0430\u043A\u043E\u043C\
      /\u0431\u043E\u0447\u043A\u043E\u0439"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MDA-WAS-13
    source_category_code: cart_trailer_with_water_tank
    national_label_en: cart/trailer with water tank
    national_label_local: "\u0422\u0435\u043B\u0435\u0436\u043A\u0430 \u0441 \u043D\
      \u0435\u0431\u043E\u043B\u044C\u0448\u0438\u043C \u0431\u0430\u043A\u043E\u043C\
      /\u0431\u043E\u0447\u043A\u043E\u0439"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MDA-WAS-14
    source_category_code: tanker_truck_provided
    national_label_en: Tanker truck provided
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
  - country_entry_id: MDA-WAS-15
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker truck vendor
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
  - country_entry_id: MDA-WAS-16
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
  - country_entry_id: MDA-WAS-17
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
  - country_entry_id: MDA-WAS-18
    source_category_code: bottled_with_improved
    national_label_en: Bottled with improved
    national_label_local: "\u0411\u0443\u0442\u0438\u043B\u0438\u0440\u043E\u0432\u0430\
      \u043D\u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: MDA-WAS-19
    source_category_code: bottled_without_improved
    national_label_en: Bottled without improved
    national_label_local: "\u0412\u043E\u0434\u0430 \u0432 \u043F\u0430\u043A\u0435\
      \u0442\u0430\u0445"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: MDA-WAS-20
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: "\u041A\u0440\u044B\u0442\u0430\u044F \u0446\u0438\u0441\
      \u0442\u0435\u0440\u043D\u0430/\u0440\u0435\u0437\u0435\u0440\u0432\u0443\u0430\
      \u0440"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: MDA-WAS-21
    source_category_code: water_tank
    national_label_en: water tank
    national_label_local: "\u041A\u0440\u044B\u0442\u0430\u044F \u0446\u0438\u0441\
      \u0442\u0435\u0440\u043D\u0430/\u0440\u0435\u0437\u0435\u0440\u0432\u0443\u0430\
      \u0440"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: MDA-WAS-22
    source_category_code: pond_river_stream
    national_label_en: Pond, river, stream
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MDA-WAS-23
    source_category_code: piped_water_to_neighbour
    national_label_en: Piped water to neighbour
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: MDA-WAS-24
    source_category_code: aqueduct
    national_label_en: Aqueduct
    national_label_local: "\u041F\u043E\u0434\u043A\u043B\u044E\u0447\u0435\u043D\u0438\
      \u044F \u043A \u0434\u043E\u043C\u0443"
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: MDA-WAS-25
    source_category_code: aqueduct_in_the_dwelling
    national_label_en: aqueduct in the dwelling
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
  - country_entry_id: MDA-WAS-26
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
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
  - country_entry_id: MDA-WAS-27
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
  - country_entry_id: MDA-WAS-28
    source_category_code: aqueduct_in_the_courtyard
    national_label_en: aqueduct in the courtyard
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
  - country_entry_id: MDA-WAS-29
    source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
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
  - country_entry_id: MDA-WAS-30
    source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
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
  - country_entry_id: MDA-WAS-31
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
  - country_entry_id: MDA-WAS-32
    source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: MDA-WAS-33
    source_category_code: standpost
    national_label_en: Standpost
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MDA_Republic_of_Moldova_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1999
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

