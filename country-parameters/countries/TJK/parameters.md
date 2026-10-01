---
country_id: CTY-TJK
iso3: TJK
schema_version: '0.2'
status: draft
country_name: TJK
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: TJK-EDU-01
    national_label_en: Pre-primary education
    national_label_local: "\u0422\u0430\u044A\u043B\u0438\u043C\u0443 \u0442\u0430\
      \u0440\u0431\u0438\u044F\u0438 \u0442\u043E\u043C\u0430\u043A\u0442\u0430\u0431\
      \u0457"
    entry_age: 3
    duration_years: 4
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
  - country_entry_id: TJK-EDU-02
    national_label_en: Primary education
    national_label_local: "\u0422\u0430\u045A\u0441\u0438\u043B\u043E\u0442\u0438\
      \ \u0438\u0431\u0442\u0438\u0434\u043E\u0457"
    entry_age: 7
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
    - TJK-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: TJK-EDU-03
    national_label_en: Basic general education
    national_label_local: "\u0422\u0430\u045A\u0441\u0438\u043B\u043E\u0442\u0438\
      \ \u0443\u043C\u0443\u043C\u0438\u0438 \u043C\u0430\u0445\u0441\u0443\u0441"
    entry_age: 11
    duration_years: 5
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - TJK-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TJK-EDU-04
    national_label_en: General secondary education
    national_label_local: "\u0422\u0430\u045A\u0441\u0438\u043B\u043E\u0442\u0438\
      \ \u0443\u043C\u0443\u043C\u0438\u0438 \u043C\u0438\u0451\u043D\u0430"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - TJK-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    - TJK-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TJK-EDU-05
    national_label_en: "Primary vocational education \n(based on basic general education)"
    national_label_local: "\u0418\u0431\u0442\u0438\u0434\u043E\u0438\u0438 \u043A\
      \u0430\u0441\u0431\u0457 (\u0434\u0430\u0440 \u0430\u0441\u043E\u0441\u0438\
      \ \u0442\u0430\u045A\u0441\u0438\u043B\u043E\u0442\u0438 \u043C\u0430\u0445\u0441\
      \u0443\u0441)"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - TJK-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    - TJK-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TJK-EDU-06
    national_label_en: "Primary vocational education \n(based on general secondary\
      \ education)"
    national_label_local: "\u0418\u0431\u0442\u0438\u0434\u043E\u0438\u0438 \u043A\
      \u0430\u0441\u0431\u0457 (\u0434\u0430\u0440 \u0430\u0441\u043E\u0441\u0438\
      \ \u0442\u0430\u045A\u0441\u0438\u043B\u043E\u0442\u0438 \u0443\u043C\u0443\u043C\
      \u0438\u0438 \u043C\u0438\u0451\u043D\u0430)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 12
    parent_country_entry_ids:
    - TJK-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    - TJK-EDU-04
    - TJK-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TJK-EDU-07
    national_label_en: Secondary vocational education
    national_label_local: "\u0422\u0430\u045A\u0441\u043E\u043B\u0438\u0442\u043E\
      \ \u043C\u0438\u0451\u043D\u0430\u0438 \u043A\u0430\u0441\u0431\u0457"
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
    parent_country_entry_ids:
    - TJK-EDU-04
    cum_years_schooling: 14
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    - TJK-EDU-04
    - TJK-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TJK-EDU-08
    national_label_en: Bachelor
    national_label_local: "\u0411\u0430\u043A\u0430\u043B\u0430\u0432\u0440"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - TJK-EDU-04
    cum_years_schooling: 15
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    - TJK-EDU-04
    - TJK-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TJK-EDU-09
    national_label_en: Specialist
    national_label_local: "\u041C\u0443\u0442\u0430\u0445\u0430\u0441\u0438\u0441"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - TJK-EDU-04
    cum_years_schooling: 16
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    - TJK-EDU-04
    - TJK-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TJK-EDU-10
    national_label_en: Master
    national_label_local: "\u041C\u0430\u0433\u0438\u0441\u0442\u0440"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - TJK-EDU-08
    cum_years_schooling: 17
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    - TJK-EDU-04
    - TJK-EDU-08
    - TJK-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TJK-EDU-11
    national_label_en: Aspirantura
    national_label_local: "\u0410\u0441\u043F\u0438\u0440\u0430\u043D\u0442\u0443\u0440\
      \u0430"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - TJK-EDU-09
    - TJK-EDU-10
    cum_years_schooling: 19
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    - TJK-EDU-04
    - TJK-EDU-09
    - TJK-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: TJK-EDU-09, TJK-EDU-10'
  - country_entry_id: TJK-EDU-12
    national_label_en: Doctorantura
    national_label_local: "\u0414\u043E\u043A\u0442\u043E\u0440\u0430\u043D\u0442\u0443\
      \u0440\u0430"
    entry_age: 27
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - TJK-EDU-09
    - TJK-EDU-10
    cum_years_schooling: 19
    cum_years_computation_path:
    - TJK-EDU-02
    - TJK-EDU-03
    - TJK-EDU-04
    - TJK-EDU-09
    - TJK-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: TJK-EDU-09, TJK-EDU-10'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Tajikistan.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2022
  effective_to: null
  selectors: null
  value:
  - country_entry_id: TJK-SUBNAT-01
    survey_labels: "1 \u2013 Dushanbe | 1\u2013Dushanbe"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: TJK_2022_GADM1_TJK.1_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: TJK_2022_GADM1_TJK.1_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: TJK.1_1
    geo_nvar: NAME_1
    geo_name: Dushanbe
    source_row: 16573
  - country_entry_id: TJK-SUBNAT-02
    survey_labels: "2 \u2013 Sogd | 4\u2013Sogd"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: TJK_2022_GADM1_TJK.4_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: TJK_2022_GADM1_TJK.4_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: TJK.4_1
    geo_nvar: NAME_1
    geo_name: Sughd
    source_row: 16574
  - country_entry_id: TJK-SUBNAT-03
    survey_labels: "3 \u2013 Khatlon | 3\u2013Khatlon"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: TJK_2022_GADM1_TJK.3_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: TJK_2022_GADM1_TJK.3_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: TJK.3_1
    geo_nvar: NAME_1
    geo_name: Khatlon
    source_row: 16575
  - country_entry_id: TJK-SUBNAT-04
    survey_labels: "2\u2013Rrs | 4 \u2013 Rrp"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: TJK_2022_GADM1_TJK.5_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: TJK_2022_GADM1_TJK.5_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: TJK.5_1
    geo_nvar: NAME_1
    geo_name: Districts of Republican Subordin
    source_row: 16576
  - country_entry_id: TJK-SUBNAT-05
    survey_labels: "5 \u2013 Gbao | 5\u2013Gbao"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: TJK_2022_GADM1_TJK.2_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: TJK_2022_GADM1_TJK.2_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: TJK.2_1
    geo_nvar: NAME_1
    geo_name: Gorno-Badakhshan
    source_row: 16577
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
  - country_entry_id: TJK-SAN-01
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
  - country_entry_id: TJK-SAN-02
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: "\u041A\u043E\u043C\u043F\u043E\u0441\u0442\u0438\u0440\u0443\
      \u044E\u0449\u0438\u0439 \u0442\u0443\u0430\u043B\u0435\u0442 (\u0441\u043E\u0431\
      \u0441\u0442\u0432\u0435\u043D\u043D\u044B\u0439)"
    jmp_classification: Composting toilets > Composting toilet (private)
    jmp_id: composting_toilets.composting_toilet_private
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 129
  - country_entry_id: TJK-SAN-03
    source_category_code: flush_to_unknown
    national_label_en: Flush to Unknown
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: TJK-SAN-04
    source_category_code: flush_piped_sewer
    national_label_en: Flush Piped Sewer
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
  - country_entry_id: TJK-SAN-05
    source_category_code: flush_pour_flush_connected_to_a_piped_sewer_system
    national_label_en: Flush/pour flush connected to a piped sewer system
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
  - country_entry_id: TJK-SAN-06
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to Pit Latrine
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: TJK-SAN-07
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to Septic Tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: TJK-SAN-08
    source_category_code: flush_pour_flush_connected_to_a_septic_tank
    national_label_en: Flush/pour flush connected to a septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: TJK-SAN-09
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to Somewhere Else
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
  - country_entry_id: TJK-SAN-10
    source_category_code: flush_to_sewage_system_septic_tank
    national_label_en: Flush to sewage system/septic tank
    national_label_local: "\u0422\u0443\u0430\u043B\u0435\u0442\u044B \u0441\u043E\
      \ \u0441\u043C\u044B\u0432\u043E\u043C"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: TJK-SAN-11
    source_category_code: private_flush_toilet
    national_label_en: Private flush toilet
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
  - country_entry_id: TJK-SAN-12
    source_category_code: wc_inside_house
    national_label_en: WC inside house
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
  - country_entry_id: TJK-SAN-13
    source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: TJK-SAN-14
    source_category_code: flush_pour_flush_to_pit_latrine
    national_label_en: Flush/pour flush to pit latrine
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > Private flush/toilet > to pit
    jmp_id: flush_toilets.private_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 75
  - country_entry_id: TJK-SAN-15
    source_category_code: flush_pour_flush_to_septic_tank
    national_label_en: Flush/pour flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: TJK-SAN-16
    source_category_code: shared_flush_toilet
    national_label_en: Shared flush toilet
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
  - country_entry_id: TJK-SAN-17
    source_category_code: wc_outside_with_piping
    national_label_en: WC outside with piping
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
  - country_entry_id: TJK-SAN-18
    source_category_code: flush_pour_flush_not_to_sewer_septic_tank_pit_latrine
    national_label_en: Flush/pour flush not to sewer/septic tank/pit latrine
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to elsewhere
    jmp_id: flush_toilets.public_shared_flush_toilet.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 83
  - country_entry_id: TJK-SAN-19
    source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: TJK-SAN-20
    source_category_code: flush_pour_flush_to_pit_latrine
    national_label_en: Flush/pour flush to pit latrine
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to pit
    jmp_id: flush_toilets.public_shared_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 81
  - country_entry_id: TJK-SAN-21
    source_category_code: flush_pour_flush_to_septic_tank
    national_label_en: Flush/pour flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 80
  - country_entry_id: TJK-SAN-22
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: TJK-SAN-23
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
  - country_entry_id: TJK-SAN-24
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit (latrine)
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: TJK-SAN-25
    source_category_code: flush_to_pit_latrine
    national_label_en: flush to pit latrine
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: TJK-SAN-26
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
  - country_entry_id: TJK-SAN-27
    source_category_code: flush_to_unknown_place_not_sure_dk_where
    national_label_en: Flush to unknown place/not sure/DK where
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
  - country_entry_id: TJK-SAN-28
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
  - country_entry_id: TJK-SAN-29
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
  - country_entry_id: TJK-SAN-30
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
  - country_entry_id: TJK-SAN-31
    source_category_code: hanging_toilet
    national_label_en: Hanging Toilet
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
  - country_entry_id: TJK-SAN-32
    source_category_code: hanging_toilet_latrine
    national_label_en: hanging toilet/latrine
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
  - country_entry_id: TJK-SAN-33
    source_category_code: river
    national_label_en: River
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
  - country_entry_id: TJK-SAN-34
    source_category_code: covered_pin_latrine
    national_label_en: Covered pin latrine
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
  - country_entry_id: TJK-SAN-35
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
  - country_entry_id: TJK-SAN-36
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
  - country_entry_id: TJK-SAN-37
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
  - country_entry_id: TJK-SAN-38
    source_category_code: pit_latrine_open
    national_label_en: Pit Latrine Open
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
  - country_entry_id: TJK-SAN-39
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
  - country_entry_id: TJK-SAN-40
    source_category_code: uncovered_pin_latrine
    national_label_en: Uncovered pin latrine
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
  - country_entry_id: TJK-SAN-41
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
  - country_entry_id: TJK-SAN-42
    source_category_code: wc_outide_without_piping
    national_label_en: WC outide without piping
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
  - country_entry_id: TJK-SAN-43
    source_category_code: ventilated_improved_latrine
    national_label_en: Ventilated Improved Latrine
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
  - country_entry_id: TJK-SAN-44
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit latrine (VIP)
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
  - country_entry_id: TJK-SAN-45
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: TJK-SAN-46
    source_category_code: private_latrine
    national_label_en: Private latrine
    national_label_local: "\u0422\u0440\u0430\u0434\u0438\u0446\u0438\u043E\u043D\u043D\
      \u0430\u044F \u0443\u0431\u043E\u0440\u043D\u0430\u044F"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 115
  - country_entry_id: TJK-SAN-47
    source_category_code: ventilated_improved_pit_vip_latrine
    national_label_en: Ventilated improved pit (VIP) latrine
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 113
  - country_entry_id: TJK-SAN-48
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: TJK-SAN-49
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0431\
      \u0435\u0437 \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\
      \u0438\u0442\u044B/\u0441 \u043E\u0442\u043A\u0440\u044B\u0442\u043E\u0439 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 124
  - country_entry_id: TJK-SAN-50
    source_category_code: shared_latrine
    national_label_en: Shared latrine
    national_label_local: "\u0422\u0440\u0430\u0434\u0438\u0446\u0438\u043E\u043D\u043D\
      \u0430\u044F \u0443\u0431\u043E\u0440\u043D\u0430\u044F"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: true
    source_row: 123
  - country_entry_id: TJK-SAN-51
    source_category_code: ventilated_improved_pit_vip_latrine
    national_label_en: Ventilated improved pit (VIP) latrine
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Ventilated
      Improved Pit latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 121
  - country_entry_id: TJK-SAN-52
    source_category_code: flush_toilet
    national_label_en: Flush toilet
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u044B\u0435 \u0441\u043E\
      \ \u0441\u043C\u044B\u0432\u043E\u043C"
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 85
  - country_entry_id: TJK-SAN-53
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
  - country_entry_id: TJK-SAN-54
    source_category_code: latrines_connected_to_a_septic_tank
    national_label_en: Latrines connected to a septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Latrines > Pour flush latrines > to septic tank
    jmp_id: latrines.pour_flush_latrines.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: TJK-SAN-55
    source_category_code: no_facilities
    national_label_en: No facilities
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: TJK-SAN-56
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
  - country_entry_id: TJK-SAN-57
    source_category_code: no_facilities_bush_field
    national_label_en: No facilities/bush/field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: TJK-SAN-58
    source_category_code: no_facility
    national_label_en: No Facility
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: TJK-SAN-59
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
  - country_entry_id: TJK-SAN-60
    source_category_code: no_toilet_in_the_house
    national_label_en: No toilet in the house
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: TJK-SAN-61
    source_category_code: none_nature
    national_label_en: None nature
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: TJK-SAN-62
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u0438\u0435 \u043D\u0435\u0443\
      \u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435"
    jmp_classification: Other unimproved
    jmp_id: other_unimproved
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 135
  - country_entry_id: TJK-SAN-63
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_TJK_Tajikistan_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: TJK-WAS-01
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
  - country_entry_id: TJK-WAS-02
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
  - country_entry_id: TJK-WAS-03
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
  - country_entry_id: TJK-WAS-04
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
  - country_entry_id: TJK-WAS-05
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
  - country_entry_id: TJK-WAS-06
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
  - country_entry_id: TJK-WAS-07
    source_category_code: protected_dug_well_or_spring
    national_label_en: Protected dug well or spring
    national_label_local: "\u0417\u0430\u0449\u0438\u0449\u0451\u043D\u043D\u044B\u0435\
      \ \u043A\u043E\u043B\u043E\u0434\u0446\u044B \u0438\u043B\u0438 \u0440\u043E\
      \u0434\u043D\u0438\u043A\u0438"
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: true
    shared_flag: false
    source_row: 46
  - country_entry_id: TJK-WAS-08
    source_category_code: hand_pump
    national_label_en: Hand pump
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
  - country_entry_id: TJK-WAS-09
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
  - country_entry_id: TJK-WAS-10
    source_category_code: tube_well_borehole
    national_label_en: Tube well/borehole
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
  - country_entry_id: TJK-WAS-11
    source_category_code: tubewell
    national_label_en: Tubewell
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
  - country_entry_id: TJK-WAS-12
    source_category_code: tubewell_borehole
    national_label_en: Tubewell/borehole
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
  - country_entry_id: TJK-WAS-13
    source_category_code: tubewell_borehole_with_pump
    national_label_en: Tubewell/Borehole with pump
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
  - country_entry_id: TJK-WAS-14
    source_category_code: spring
    national_label_en: Spring
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0439 \u0440\u043E\u0434\u043D\u0438\u043A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: TJK-WAS-15
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
  - country_entry_id: TJK-WAS-16
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
  - country_entry_id: TJK-WAS-17
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
  - country_entry_id: TJK-WAS-18
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
  - country_entry_id: TJK-WAS-19
    source_category_code: cart_with_small_tank
    national_label_en: Cart with Small Tank
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
  - country_entry_id: TJK-WAS-20
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
  - country_entry_id: TJK-WAS-21
    source_category_code: brought_in_water_truck
    national_label_en: Brought in Water (Truck)
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
  - country_entry_id: TJK-WAS-22
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
  - country_entry_id: TJK-WAS-23
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
  - country_entry_id: TJK-WAS-24
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
  - country_entry_id: TJK-WAS-25
    source_category_code: tanker_truck_cart_with_small_tank
    national_label_en: Tanker truck/cart with small tank
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
  - country_entry_id: TJK-WAS-26
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
  - country_entry_id: TJK-WAS-27
    source_category_code: truck_vendor
    national_label_en: Truck, vendor
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
  - country_entry_id: TJK-WAS-28
    source_category_code: water_truck
    national_label_en: Water truck
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
  - country_entry_id: TJK-WAS-29
    source_category_code: cut_official_pipe
    national_label_en: Cut official pipe
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: TJK-WAS-30
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
  - country_entry_id: TJK-WAS-31
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
  - country_entry_id: TJK-WAS-32
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
  - country_entry_id: TJK-WAS-33
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
  - country_entry_id: TJK-WAS-34
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
  - country_entry_id: TJK-WAS-35
    source_category_code: rainwater
    national_label_en: rainwater
    national_label_local: "\u0414\u043E\u0436\u0434\u0435\u0432\u0430\u044F \u0432\
      \u043E\u0434\u0430"
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 86
  - country_entry_id: TJK-WAS-36
    source_category_code: rain_water
    national_label_en: Rain water
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
  - country_entry_id: TJK-WAS-37
    source_category_code: rainwater
    national_label_en: Rainwater
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
  - country_entry_id: TJK-WAS-38
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
  - country_entry_id: TJK-WAS-39
    source_category_code: lake_river_stream
    national_label_en: Lake, river, stream
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: TJK-WAS-40
    source_category_code: river_lake_pond
    national_label_en: River, lake, pond
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: TJK-WAS-41
    source_category_code: river_dam_lake_ponds_stream_canal_irrigation_channel
    national_label_en: River/dam/lake/ponds/stream/canal/irrigation channel
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: TJK-WAS-42
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
  - country_entry_id: TJK-WAS-43
    source_category_code: river_or_stream
    national_label_en: River or stream
    national_label_local: "\u0420\u0435\u043A\u0430"
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: TJK-WAS-44
    source_category_code: river_lake_pond
    national_label_en: River, lake, pond
    national_label_local: "\u0420\u0435\u043A\u0430"
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: TJK-WAS-45
    source_category_code: centralized_pipeline_standing_water_pipe_at_the_neighbours
    national_label_en: Centralized pipeline/standing water pipe, at the neighbours
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: TJK-WAS-46
    source_category_code: pipe_from_neighbour
    national_label_en: Pipe from neighbour
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: TJK-WAS-47
    source_category_code: piped_to_neighbor
    national_label_en: piped to neighbor
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: TJK-WAS-48
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
  - country_entry_id: TJK-WAS-49
    source_category_code: centralized_pipeline_standing_water_pipe_in_house
    national_label_en: Centralized pipeline/standing water pipe in house
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
  - country_entry_id: TJK-WAS-50
    source_category_code: pipe_in_dwelling_compound
    national_label_en: Pipe in dwelling/compound
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
  - country_entry_id: TJK-WAS-51
    source_category_code: piped_inside_dwelling
    national_label_en: Piped inside dwelling
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
  - country_entry_id: TJK-WAS-52
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
  - country_entry_id: TJK-WAS-53
    source_category_code: piped_into_dwelling_urban_plumbing
    national_label_en: Piped into dwelling (urban plumbing)
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
  - country_entry_id: TJK-WAS-54
    source_category_code: urban_rural_plumbing
    national_label_en: Urban/rural plumbing
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
  - country_entry_id: TJK-WAS-55
    source_category_code: centralized_pipeline_standing_water_pipe_in_yard
    national_label_en: Centralized pipeline/standing water pipe in yard
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
  - country_entry_id: TJK-WAS-56
    source_category_code: piped_into_compound
    national_label_en: Piped Into Compound
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
  - country_entry_id: TJK-WAS-57
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
  - country_entry_id: TJK-WAS-58
    source_category_code: piped_ouside_dwelling
    national_label_en: Piped ouside dwelling
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
  - country_entry_id: TJK-WAS-59
    source_category_code: piped_to_yard_plot
    national_label_en: piped to yard/plot
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
  - country_entry_id: TJK-WAS-60
    source_category_code: piped_to_yard_plot_rural_local_plumbing
    national_label_en: Piped to yard/plot (rural (local) plumbing)
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
  - country_entry_id: TJK-WAS-61
    source_category_code: rural_local_plumbing
    national_label_en: rural (local) plumbing
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
  - country_entry_id: TJK-WAS-62
    source_category_code: centralized_pipeline_standing_water_pipe_in_the_street
    national_label_en: Centralized pipeline/standing water pipe, in the street
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: TJK-WAS-63
    source_category_code: piped_neighbor_or_public_tap
    national_label_en: Piped Neighbor or Public Tap
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: TJK-WAS-64
    source_category_code: public_outdoor_tap
    national_label_en: Public outdoor tap
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: TJK-WAS-65
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
  - country_entry_id: TJK-WAS-66
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_TJK_Tajikistan_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

