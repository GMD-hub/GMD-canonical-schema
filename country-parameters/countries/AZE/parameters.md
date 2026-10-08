---
country_id: CTY-AZE
iso3: AZE
schema_version: '0.2'
status: draft
country_name: AZE
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: AZE-EDU-01
    national_label_en: Early childhood education
    national_label_local: "m\u0259kt\u0259b\u0259q\u0259d\u0259r t\u0259hsil"
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
  - country_entry_id: AZE-EDU-02
    national_label_en: Early childhood education
    national_label_local: "m\u0259kt\u0259b\u0259q\u0259d\u0259r t\u0259hsil"
    entry_age: 3
    duration_years: 2
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
  - country_entry_id: AZE-EDU-03
    national_label_en: Early childhood education (preparatory Grade)
    national_label_local: "m\u0259kt\u0259b\u0259q\u0259d\u0259r t\u0259hsil     \
      \                                            (haz\u0131rl\u0131q sinifi)"
    entry_age: 5
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: AZE-EDU-04
    national_label_en: elementary education
    national_label_local: "ibtidai t\u0259hsil"
    entry_age: 6
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - AZE-EDU-04
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: AZE-EDU-05
    national_label_en: general secondary education
    national_label_local: "\xFCmumi orta t\u0259hsil"
    entry_age: 10
    duration_years: 5
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - AZE-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-06
    national_label_en: complete secondary education
    national_label_local: "tam orta t\u0259hsil"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - AZE-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-07
    national_label_en: initial vocational education combined with complete secondary
      education
    national_label_local: "ilk pe\u015F\u0259-ixtisas t\u0259hsili tam orta t\u0259\
      hsil il\u0259 birlikd\u0259"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - AZE-EDU-05
    cum_years_schooling: 12
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-08
    national_label_en: initial vocational education
    national_label_local: "ilk pe\u015F\u0259-ixtisas t\u0259hsili"
    entry_age: 17
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - AZE-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-06
    - AZE-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-09
    national_label_en: 1st-2nd years of vocational secondary education
    national_label_local: "orta ixtisas t\u0259hsili 1-2-ci kurslar"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - AZE-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-10
    national_label_en: 3rd-4th years of vocational specialized education
    national_label_local: "orta ixtisas t\u0259hsili 3-4 kurslar"
    entry_age: 17
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - AZE-EDU-06
    cum_years_schooling: 13
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-06
    - AZE-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-11
    national_label_en: vocational specialized education
    national_label_local: "orta ixtisas t\u0259hsili"
    entry_age: 17
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - AZE-EDU-06
    cum_years_schooling: 13
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-06
    - AZE-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-12
    national_label_en: the first stage of tertiary education - bachelor's degree
    national_label_local: "ali t\u0259hsilin birinci m\u0259rh\u0259l\u0259si - bakalavriat"
    entry_age: 17
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - AZE-EDU-06
    cum_years_schooling: 15
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-06
    - AZE-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-13
    national_label_en: Long-term first degree (5 years or more) (Master's or equivalent)
    national_label_local: "Uzunm\xFCdd\u0259tli birinci d\u0259r\u0259c\u0259 (5 ild\u0259\
      n az olmas\u0131n) (Magistr v\u0259 ya ekvivalenti)"
    entry_age: 17
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - AZE-EDU-12
    cum_years_schooling: 21
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-06
    - AZE-EDU-12
    - AZE-EDU-13
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-14
    national_label_en: second stage of tertiary education - master's degree
    national_label_local: "ali t\u0259hsilin ikinci m\u0259rh\u0259l\u0259si - maqistratura"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - AZE-EDU-12
    cum_years_schooling: 17
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-06
    - AZE-EDU-12
    - AZE-EDU-14
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AZE-EDU-15
    national_label_en: doctoral studies for the preparation of a doctor of philosophy
    national_label_local: "f\u0259ls\u0259f\u0259 doktoru haz\u0131rl\u0131\u011F\u0131\
      \ \xFCzr\u0259 doktorantura"
    entry_age: 23
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - AZE-EDU-13
    - AZE-EDU-14
    cum_years_schooling: 20
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-06
    - AZE-EDU-12
    - AZE-EDU-14
    - AZE-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AZE-EDU-13, AZE-EDU-14'
  - country_entry_id: AZE-EDU-16
    national_label_en: doctoral studies for the preparation of doctors of sciences
      (PhD)
    national_label_local: "elml\u0259r doktoru haz\u0131rl\u0131\u011F\u0131 \xFC\
      zr\u0259 doktorantura"
    entry_age: 26
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - AZE-EDU-13
    - AZE-EDU-14
    cum_years_schooling: 21
    cum_years_computation_path:
    - AZE-EDU-04
    - AZE-EDU-05
    - AZE-EDU-06
    - AZE-EDU-12
    - AZE-EDU-14
    - AZE-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AZE-EDU-13, AZE-EDU-14'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Azerbaijan.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: AZE-SUBNAT-01
    survey_labels: "1 \u2013 Absheron | 1 \u2013 ab\uFFFDeron"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAULx_147297
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAULx_147297
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: ADM1_CODE
    geo_id: '147297'
    geo_nvar: ADM1_NAME
    geo_name: Absheron
    source_row: 511
  - country_entry_id: AZE-SUBNAT-02
    survey_labels: "0 \u2013 Nakhchyvan | 0 \u2013 nax\uFFFD\uFFFDvan mr | 1 \u2013\
      \ nax\uFFFD\uFFFDvan mr"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAUL1_147304
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAUL1_147304
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147304'
    geo_nvar: ADM1_NAME
    geo_name: Nakhchivan
    source_row: 512
  - country_entry_id: AZE-SUBNAT-03
    survey_labels: "2 \u2013 Ganja-Gazakh | 2 \u2013 g\uFFFDnc\uFFFD- qazax | 4 \u2013\
      \ g\uFFFDnc\uFFFD-qazax"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAUL1_147300
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAUL1_147300
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147300'
    geo_nvar: ADM1_NAME
    geo_name: Ganja-Gazakh
    source_row: 513
  - country_entry_id: AZE-SUBNAT-04
    survey_labels: "3 \u2013 Shaki-Zagatala | 3 \u2013 \uFFFD\uFFFDki- zaqatala |\
      \ 5 \u2013 \uFFFD\uFFFDki-zaqatala"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAUL1_147305
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAUL1_147305
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147305'
    geo_nvar: ADM1_NAME
    geo_name: Shaki-Zaqatala
    source_row: 514
  - country_entry_id: AZE-SUBNAT-05
    survey_labels: "4 \u2013 Lankaran | 4 \u2013 l\uFFFDnk\uFFFDran- astara | 6 \u2013\
      \ l\uFFFDnk\uFFFDran-astara"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAUL1_147303
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAUL1_147303
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147303'
    geo_nvar: ADM1_NAME
    geo_name: Lankaran
    source_row: 515
  - country_entry_id: AZE-SUBNAT-06
    survey_labels: "7 \u2013 Yukhary Garabagh | 7 \u2013 yuxari qaraba\uFFFD"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAUL1_147306
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAUL1_147306
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147306'
    geo_nvar: ADM1_NAME
    geo_name: Yukhari Garabakh
    source_row: 516
  - country_entry_id: AZE-SUBNAT-07
    survey_labels: "8 \u2013 Baku City | 8 \u2013 bak\uFFFD | 9 \u2013 bak\uFFFD"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAUL2_495
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAUL2_495
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '2'
    geo_idvar: ADM2_CODE
    geo_id: '495'
    geo_nvar: ADM2_NAME
    geo_name: Baku
    source_row: 517
  - country_entry_id: AZE-SUBNAT-08
    survey_labels: "9 \u2013 Daghlig Shirvan | 9 \u2013 dagliq \uFFFDirvan"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAUL1_147299
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAUL1_147299
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147299'
    geo_nvar: ADM1_NAME
    geo_name: Daghlig Shirvan
    source_row: 518
  - country_entry_id: AZE-SUBNAT-09
    survey_labels: "5 \u2013 Guba-Khachmaz | 5 \u2013 quba- xacmaz"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAUL1_147301
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAUL1_147301
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147301'
    geo_nvar: ADM1_NAME
    geo_name: Guba-Khachmaz
    source_row: 532
  - country_entry_id: AZE-SUBNAT-10
    survey_labels: "6 \u2013 Aran | 6 \u2013 aran"
    survey_variables: subnatid
    gmd_subnatid1: AZE_2015_GAUL1_147298
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AZE_2015_GAUL1_147298
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147298'
    geo_nvar: ADM1_NAME
    geo_name: Aran
    source_row: 533
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
  - country_entry_id: AZE-SAN-01
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
  - country_entry_id: AZE-SAN-02
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: AZE-SAN-03
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
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
  - country_entry_id: AZE-SAN-04
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: AZE-SAN-05
    source_category_code: don_t_know_where
    national_label_en: Don't know where
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
  - country_entry_id: AZE-SAN-06
    source_category_code: flush_to_sewage_system_septic_tank
    national_label_en: Flush to sewage system/ septic tank
    national_label_local: "\u0422\u0443\u0430\u043B\u0435\u0442\u044B \u0441\u043E\
      \ \u0441\u043C\u044B\u0432\u043E\u043C"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: AZE-SAN-07
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush - to somewhere else
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: AZE-SAN-08
    source_category_code: flush_pour_flush_flush_to_open_drain
    national_label_en: 'flush / pour flush: flush to open drain'
    national_label_local: to elsewhere
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: AZE-SAN-09
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush - to piped sewer system
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
  - country_entry_id: AZE-SAN-10
    source_category_code: to_piped_sewer_system
    national_label_en: to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: AZE-SAN-11
    source_category_code: to_pit
    national_label_en: to pit
    national_label_local: to pit
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: AZE-SAN-12
    source_category_code: flush_to_septic_tank
    national_label_en: Flush - to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: AZE-SAN-13
    source_category_code: to_septic_tank
    national_label_en: to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: AZE-SAN-14
    source_category_code: flush_pour_flush_flush_to_dk_where
    national_label_en: 'flush / pour flush: flush to dk where'
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: AZE-SAN-15
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
  - country_entry_id: AZE-SAN-16
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
  - country_entry_id: AZE-SAN-17
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine - with slab
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
  - country_entry_id: AZE-SAN-18
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
  - country_entry_id: AZE-SAN-19
    source_category_code: pit_latrine_pit_latrine_with_slab
    national_label_en: 'pit latrine: pit latrine with slab'
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: AZE-SAN-20
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
  - country_entry_id: AZE-SAN-21
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine - without slab / open pit
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
  - country_entry_id: AZE-SAN-22
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab / Open pit
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
  - country_entry_id: AZE-SAN-23
    source_category_code: pit_latrine_pit_latrine_without_slab_open_pit
    national_label_en: 'pit latrine: pit latrine without slab / open pit'
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: AZE-SAN-24
    source_category_code: traditional_pit_latrine
    national_label_en: Traditional pit latrine
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
  - country_entry_id: AZE-SAN-25
    source_category_code: pit_latrine_ventilated_improved_pit_latrine
    national_label_en: 'pit latrine: ventilated improved pit latrine'
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: AZE-SAN-26
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet, Hanging latrine
    national_label_local: "\u041F\u043E\u0434\u0432\u0435\u0441\u043D\u043E\u0439\
      \ \u0442\u0443\u0430\u043B\u0435\u0442/\u043F\u043E\u0434\u0432\u0435\u0441\u043D\
      \u0430\u044F \u0443\u0431\u043E\u0440\u043D\u0430\u044F"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Hanging
      toilet/hanging latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 125
  - country_entry_id: AZE-SAN-27
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
  - country_entry_id: AZE-SAN-28
    source_category_code: no_facility_bush_field
    national_label_en: No facility, Bush, Field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: AZE-SAN-29
    source_category_code: no_facility_bush_field
    national_label_en: No facility/ bush/ field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: AZE-SAN-30
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
  - country_entry_id: AZE-SAN-31
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_AZE_Azerbaijan_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: AZE-WAS-01
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
  - country_entry_id: AZE-WAS-02
    source_category_code: spring_protected_spring
    national_label_en: 'spring: protected spring'
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: AZE-WAS-03
    source_category_code: dug_well_protected_well
    national_label_en: 'dug well: protected well'
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: AZE-WAS-04
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
  - country_entry_id: AZE-WAS-05
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
  - country_entry_id: AZE-WAS-06
    source_category_code: tube_well_borehole
    national_label_en: tube well / borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: AZE-WAS-07
    source_category_code: tube_well_or_borehole
    national_label_en: Tube well or borehole
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
  - country_entry_id: AZE-WAS-08
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
  - country_entry_id: AZE-WAS-09
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
  - country_entry_id: AZE-WAS-10
    source_category_code: spring_unprotected_spring
    national_label_en: 'spring: unprotected spring'
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: AZE-WAS-11
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
  - country_entry_id: AZE-WAS-12
    source_category_code: dug_well_unprotected_well
    national_label_en: 'dug well: unprotected well'
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: AZE-WAS-13
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
  - country_entry_id: AZE-WAS-14
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
  - country_entry_id: AZE-WAS-15
    source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0435 \u043A\u043E\u043B\u043E\u0434\u0446\u044B \u0438\u043B\u0438 \u0440\
      \u043E\u0434\u043D\u0438\u043A\u0438"
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 50
  - country_entry_id: AZE-WAS-16
    source_category_code: cart_with_small_tank_or_drum
    national_label_en: Cart with small tank or drum
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
  - country_entry_id: AZE-WAS-17
    source_category_code: tanker_truck_cartwith_small_tank
    national_label_en: Tanker truck, cartwith small tank
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
  - country_entry_id: AZE-WAS-18
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker, truck, vendor
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
  - country_entry_id: AZE-WAS-19
    source_category_code: tanker_truck
    national_label_en: Tanker-truck
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
  - country_entry_id: AZE-WAS-20
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
  - country_entry_id: AZE-WAS-21
    source_category_code: other_missing
    national_label_en: Other, missing
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: AZE-WAS-22
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
  - country_entry_id: AZE-WAS-23
    source_category_code: bottled_water_with_improved_source_for_cooking_washing
    national_label_en: Bottled water, with improved source for cooking/washing
    national_label_local: "\u0411\u0443\u0442\u0438\u043B\u0438\u0440\u043E\u0432\u0430\
      \u043D\u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: AZE-WAS-24
    source_category_code: packaged_water_water_bottles
    national_label_en: 'packaged water: water bottles'
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: AZE-WAS-25
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "\u0412\u043E\u0434\u0430 \u0432 \u043F\u0430\u043A\u0435\
      \u0442\u0430\u0445"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: AZE-WAS-26
    source_category_code: bottled_water_non_improved_source_for_cooking_washing
    national_label_en: Bottled water, non-improved source for cooking/washing
    national_label_local: "\u0412\u043E\u0434\u0430 \u0432 \u043F\u0430\u043A\u0435\
      \u0442\u0430\u0445"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: AZE-WAS-27
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
  - country_entry_id: AZE-WAS-28
    source_category_code: pond_river_or_stream
    national_label_en: Pond, river or stream
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: AZE-WAS-29
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
  - country_entry_id: AZE-WAS-30
    source_category_code: surface_water_river_lake_canal
    national_label_en: surface water (river, lake, canal)
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: AZE-WAS-31
    source_category_code: piped_to_neighbour
    national_label_en: Piped to neighbour
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: AZE-WAS-32
    source_category_code: piped_water_piped_to_neighbour
    national_label_en: 'piped water: piped to neighbour'
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: AZE-WAS-33
    source_category_code: piped_water_into_dwelling_yard_plot
    national_label_en: Piped water into dwelling, yard,plot
    national_label_local: "\u041F\u043E\u0434\u043A\u043B\u044E\u0447\u0435\u043D\u0438\
      \u044F \u043A \u0434\u043E\u043C\u0443"
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: AZE-WAS-34
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
  - country_entry_id: AZE-WAS-35
    source_category_code: piped_water_piped_into_house_apartment
    national_label_en: 'piped water: piped into house / apartment'
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: AZE-WAS-36
    source_category_code: piped_into_compound_yard_or_plot
    national_label_en: Piped into compound, yard or plot
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
  - country_entry_id: AZE-WAS-37
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
  - country_entry_id: AZE-WAS-38
    source_category_code: piped_water_piped_to_yard_plot
    national_label_en: 'piped water: piped to yard / plot'
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: AZE-WAS-39
    source_category_code: piped_water_public_tap_standpipe
    national_label_en: 'piped water: public tap / standpipe'
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: AZE-WAS-40
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
  - country_entry_id: AZE-WAS-41
    source_category_code: public_tap_standpipe
    national_label_en: Public tap / standpipe
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: AZE-WAS-42
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
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_AZE_Azerbaijan_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1992
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

