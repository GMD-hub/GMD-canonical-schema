---
country_id: CTY-GHA
country_name: Ghana
iso3: GHA
schema_version: '0.1'
status: draft
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: GHA-EDU-01
    national_label_en: ECD programme
    national_label_local: ECD programme
    entry_age: 0
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: GHA-EDU-02
    national_label_en: Kindergarten
    national_label_local: Kindergarten
    entry_age: 4
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 8
  - country_entry_id: GHA-EDU-03
    national_label_en: Primary school
    national_label_local: Primary school
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
  - country_entry_id: GHA-EDU-04
    national_label_en: Junior high school
    national_label_local: Junior high school
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
  - country_entry_id: GHA-EDU-05
    national_label_en: Senior high school
    national_label_local: Senior high school
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - country_entry_id: GHA-EDU-06
    national_label_en: Technical and vocational education
    national_label_local: Technical and vocational education
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: GHA-EDU-07
    national_label_en: Polytechnics non-tertiary programmes
    national_label_local: Polytechnics non-tertiary programmes
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
  - country_entry_id: GHA-EDU-08
    national_label_en: Polytechnics Tertiary programmes
    national_label_local: Polytechnics Tertiary programmes
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - country_entry_id: GHA-EDU-09
    national_label_en: Teacher training diploma
    national_label_local: Teacher training diploma
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - country_entry_id: GHA-EDU-10
    national_label_en: Professional bodies programmes
    national_label_local: Professional bodies programmes
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: GHA-EDU-11
    national_label_en: Polytechnics Tertiary programmes
    national_label_local: Polytechnics Tertiary programmes
    entry_age: 21
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: GHA-EDU-12
    national_label_en: University education - first degree
    national_label_local: University education - first degree
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - country_entry_id: GHA-EDU-13
    national_label_en: University education - second degree
    national_label_local: University education - second degree
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  - country_entry_id: GHA-EDU-14
    national_label_en: PhD programme
    national_label_local: PhD programme
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Ghana.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: GHA-SUBNAT-01
    survey_labels: 1 - Western | 1 – Western
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1333
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1333
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1333'
    geo_nvar: ADM1_NAME
    geo_name: Western
    source_row: 5645
  - country_entry_id: GHA-SUBNAT-02
    survey_labels: 10 - Upper West | 10 – Upper West
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1331
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1331
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1331'
    geo_nvar: ADM1_NAME
    geo_name: Upper West
    source_row: 5646
  - country_entry_id: GHA-SUBNAT-03
    survey_labels: 2 - Central | 2 – Central
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1326
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1326
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1326'
    geo_nvar: ADM1_NAME
    geo_name: Central
    source_row: 5647
  - country_entry_id: GHA-SUBNAT-04
    survey_labels: 3 - Greater Accra | 3 – Greater Accra
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1328
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1328
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1328'
    geo_nvar: ADM1_NAME
    geo_name: Greater Accra
    source_row: 5648
  - country_entry_id: GHA-SUBNAT-05
    survey_labels: 4 - Volta | 4 – Volta
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1332
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1332
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1332'
    geo_nvar: ADM1_NAME
    geo_name: Volta
    source_row: 5649
  - country_entry_id: GHA-SUBNAT-06
    survey_labels: 5 - Eastern | 5 – Eastern
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1327
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1327
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1327'
    geo_nvar: ADM1_NAME
    geo_name: Eastern
    source_row: 5650
  - country_entry_id: GHA-SUBNAT-07
    survey_labels: 6 - Ashanti | 6 – Ashanti
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1324
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1324
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1324'
    geo_nvar: ADM1_NAME
    geo_name: Ashanti
    source_row: 5651
  - country_entry_id: GHA-SUBNAT-08
    survey_labels: 7 - Brong Ahafo | 7 – Brong Ahafo
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1325
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1325
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1325'
    geo_nvar: ADM1_NAME
    geo_name: Brong Ahafo
    source_row: 5652
  - country_entry_id: GHA-SUBNAT-09
    survey_labels: 8 - Northern | 8 – Northern
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1329
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1329
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1329'
    geo_nvar: ADM1_NAME
    geo_name: Northern
    source_row: 5653
  - country_entry_id: GHA-SUBNAT-10
    survey_labels: 9 - Upper East | 9 – Upper East
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: GHA_2015_GAUL1_1330
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: GHA_2015_GAUL1_1330
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1330'
    geo_nvar: ADM1_NAME
    geo_name: Upper East
    source_row: 5654
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
  - country_entry_id: GHA-SAN-01
    source_category_code: bio_digester_e_g_bio_fill
    national_label_en: Bio-digester (e.g. bio fill)
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: GHA-SAN-02
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: GHA-SAN-03
    source_category_code: composting_toilets
    national_label_en: Composting toilets
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: GHA-SAN-04
    source_category_code: composting_toilet
    national_label_en: composting toilet
    national_label_local: Composting toilet (private)
    jmp_classification: Composting toilets > Composting toilet (private)
    jmp_id: composting_toilets.composting_toilet_private
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 129
  - country_entry_id: GHA-SAN-05
    source_category_code: flush_or_pour_flush_toilet
    national_label_en: Flush or pour flush toilet
    national_label_local: Flush and pour flush
    jmp_classification: Flush and pour flush
    jmp_id: flush_and_pour_flush
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 60
  - country_entry_id: GHA-SAN-06
    source_category_code: flush_pour_flush_flush_to_open_drain
    national_label_en: 'Flush / pour flush: flush to open drain'
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: GHA-SAN-07
    source_category_code: flush_to_somewhere_else
    national_label_en: flush to somewhere else
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: GHA-SAN-08
    source_category_code: flush_don_t_know_where
    national_label_en: Flush, don't know where
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: GHA-SAN-09
    source_category_code: flush_pour_flush_not_to_sewer_septic_tank
    national_label_en: Flush/ pour flush not to sewer/septic tank
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: GHA-SAN-10
    source_category_code: flush_pour_flush_flush_to_piped_sewer_system
    national_label_en: 'Flush / pour flush: flush to piped sewer system'
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: GHA-SAN-11
    source_category_code: flush_to_piped_sewer_system
    national_label_en: flush to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: GHA-SAN-12
    source_category_code: flush_toilet_to_piped_sewer_system
    national_label_en: Flush toilet to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: GHA-SAN-13
    source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: GHA-SAN-14
    source_category_code: private_flush_pour_flush_to_piped_sewer_system
    national_label_en: 'Private: Flush/pour flush to piped sewer system'
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: GHA-SAN-15
    source_category_code: flush_pour_flush_flush_to_pit_latrine
    national_label_en: 'Flush / pour flush: flush to pit latrine'
    national_label_local: to pit
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: GHA-SAN-16
    source_category_code: flush_to_pit_latrine
    national_label_en: flush to pit latrine
    national_label_local: to pit
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: GHA-SAN-17
    source_category_code: flushed_toilet_to_pit_latrine
    national_label_en: Flushed toilet to pit latrine
    national_label_local: to pit
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: GHA-SAN-18
    source_category_code: flush_pour_flush_flush_to_septic_tank
    national_label_en: 'Flush / pour flush: flush to septic tank'
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: GHA-SAN-19
    source_category_code: flush_to_septic_tank
    national_label_en: flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: GHA-SAN-20
    source_category_code: flush_pour_flush_to_septic_tank_or_pit_latrine
    national_label_en: Flush/ pour flush to septic tank or pit latrine
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: GHA-SAN-21
    source_category_code: flushed_toilet_to_septic_tank
    national_label_en: Flushed toilet to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: GHA-SAN-22
    source_category_code: private_flush_pour_flush_to_septic_tank_or_pit_latrine
    national_label_en: 'Private: Flush/ pour flush to septic tank or pit latrine'
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: GHA-SAN-23
    source_category_code: flush_pour_flush_flush_to_dk_where
    national_label_en: 'Flush / pour flush: flush to dk where'
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: GHA-SAN-24
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: GHA-SAN-25
    source_category_code: flush_to_unknown_place_not_sure_don_t_know_where
    national_label_en: Flush to unknown place/not sure / don't know where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: GHA-SAN-26
    source_category_code: flush_don_t_know_where
    national_label_en: flush, don't know where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: GHA-SAN-27
    source_category_code: flush_pour_flush_to_unknown
    national_label_en: Flush/pour flush to unknown
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: GHA-SAN-28
    source_category_code: domestic_connection
    national_label_en: Domestic Connection*
    national_label_local: Flush/toilets
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: GHA-SAN-29
    source_category_code: flush_toilet
    national_label_en: Flush toilet
    national_label_local: Flush/toilets
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: GHA-SAN-30
    source_category_code: flush_toilets
    national_label_en: Flush toilets
    national_label_local: Flush/toilets
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: GHA-SAN-31
    source_category_code: w_c
    national_label_en: W.C.
    national_label_local: Flush/toilets
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: GHA-SAN-32
    source_category_code: own_flush_toilet
    national_label_en: Own Flush Toilet
    national_label_local: Private flush/toilet
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: GHA-SAN-33
    source_category_code: private_domestic_connection_to_sewage_system
    national_label_en: Private domestic connection to sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - country_entry_id: GHA-SAN-34
    source_category_code: private_flush_to_septic_tank
    national_label_en: Private flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 74
  - country_entry_id: GHA-SAN-35
    source_category_code: share_flush_toilet
    national_label_en: Share flush toilet
    national_label_local: Public/shared flush/toilet
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: GHA-SAN-36
    source_category_code: shared_flush_toilet
    national_label_en: Shared Flush Toilet
    national_label_local: Public/shared flush/toilet
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: GHA-SAN-37
    source_category_code: shared_domestic_connection_to_sewage_system
    national_label_en: Shared domestic connection to sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - country_entry_id: GHA-SAN-38
    source_category_code: shared_flush_to_septic_tank
    national_label_en: Shared flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 80
  - country_entry_id: GHA-SAN-39
    source_category_code: flush_to_elsewhere
    national_label_en: Flush to elsewhere
    national_label_local: to elsewhere
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: GHA-SAN-40
    source_category_code: flush_to_somewhere_else
    national_label_en: flush to somewhere else
    national_label_local: to elsewhere
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: GHA-SAN-41
    source_category_code: to_elsewhere
    national_label_en: to elsewhere
    national_label_local: to elsewhere
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: GHA-SAN-42
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: GHA-SAN-43
    source_category_code: flush_pour_to_piped_sewage_system
    national_label_en: flush/pour to piped sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: GHA-SAN-44
    source_category_code: sewer
    national_label_en: Sewer
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: GHA-SAN-45
    source_category_code: to_piped_sewer_system
    national_label_en: to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: GHA-SAN-46
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit (latrine)
    national_label_local: to pit
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: GHA-SAN-47
    source_category_code: flush_to_pit_latrine
    national_label_en: flush to pit latrine
    national_label_local: to pit
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: GHA-SAN-48
    source_category_code: flush_to_pit_latrine_bio_digester_biofil
    national_label_en: flush to pit latrine + bio-digester (biofil)
    national_label_local: to pit
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: GHA-SAN-49
    source_category_code: to_pit
    national_label_en: to pit
    national_label_local: to pit
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: GHA-SAN-50
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: GHA-SAN-51
    source_category_code: flush_pour_to_septic_tank
    national_label_en: flush/pour to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: GHA-SAN-52
    source_category_code: to_septic_tank
    national_label_en: to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: GHA-SAN-53
    source_category_code: flush_to_don_t_know_where
    national_label_en: Flush to don't know where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GHA-SAN-54
    source_category_code: flush_don_t_know_where
    national_label_en: flush, don't know where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GHA-SAN-55
    source_category_code: public_toilet
    national_label_en: Public toilet
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GHA-SAN-56
    source_category_code: to_unknown_place_not_sure_dk
    national_label_en: to unknown place/ not sure/DK
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GHA-SAN-57
    source_category_code: latrine
    national_label_en: Latrine
    national_label_local: Dry latrines
    jmp_classification: Latrines > Dry latrines
    jmp_id: latrines.dry_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: no
    shared_flag: no
    source_row: 103
  - country_entry_id: GHA-SAN-58
    source_category_code: bucket
    national_label_en: Bucket
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-59
    source_category_code: bucket_latrine
    national_label_en: Bucket latrine
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-60
    source_category_code: bucket_latrine_where_fresh_excreta_are_manually_removed
    national_label_en: Bucket latrine (where fresh excreta are manually removed)
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-61
    source_category_code: bucket_toilet
    national_label_en: bucket toilet
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-62
    source_category_code: bucket_pan
    national_label_en: Bucket, pan
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-63
    source_category_code: bucket_pan
    national_label_en: Bucket/Pan
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-64
    source_category_code: bucket_pan_toilet
    national_label_en: Bucket/pan toilet
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-65
    source_category_code: pan
    national_label_en: Pan
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-66
    source_category_code: pan_bucket
    national_label_en: Pan / Bucket
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-67
    source_category_code: pan_or_bucket
    national_label_en: Pan or bucket
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-68
    source_category_code: pan_bucket
    national_label_en: Pan/bucket
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: GHA-SAN-69
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet, Hanging latrine
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: GHA-SAN-70
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet/hanging latrine
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: GHA-SAN-71
    source_category_code: hanging_toilet_latrine
    national_label_en: hanging toilet/latrine
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: GHA-SAN-72
    source_category_code: portable_toilet_e_g_water_potti
    national_label_en: Portable toilet (e.g. Water potti)
    national_label_local: Other
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: GHA-SAN-73
    source_category_code: covered
    national_label_en: Covered
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-SAN-74
    source_category_code: covered_pit_latrine
    national_label_en: Covered pit latrine
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-SAN-75
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine - with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-SAN-76
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-SAN-77
    source_category_code: pit_latrine_with_slab_covered_latrine
    national_label_en: Pit latrine with slab/covered latrine
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-SAN-78
    source_category_code: pit_with_slab
    national_label_en: pit with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-SAN-79
    source_category_code: private_pit_latrine_with_slab
    national_label_en: 'Private: Pit latrine with slab'
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-SAN-80
    source_category_code: pit_latrine
    national_label_en: Pit latrine
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-81
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine - without slab / open pit
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-82
    source_category_code: pit_latrine_without_slab
    national_label_en: Pit latrine without slab
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-83
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab / Open pit
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-84
    source_category_code: pit_latrine_without_slab_bucket_toilet
    national_label_en: Pit latrine without slab/bucket toilet
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-85
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-86
    source_category_code: pit_witout_slap_open
    national_label_en: pit witout slap/open
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-87
    source_category_code: uncovered
    national_label_en: Uncovered
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-88
    source_category_code: uncovered_dry_latrine_without_privacy
    national_label_en: Uncovered dry latrine (without privacy)
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-89
    source_category_code: uncovered_pit_latrine
    national_label_en: Uncovered pit latrine
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: GHA-SAN-90
    source_category_code: pit
    national_label_en: Pit
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: GHA-SAN-91
    source_category_code: pit_latrine
    national_label_en: Pit latrine
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: GHA-SAN-92
    source_category_code: traditional_pit_latrine
    national_label_en: Traditional Pit Latrine
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: GHA-SAN-93
    source_category_code: traditional_pit_toilet
    national_label_en: Traditional pit toilet
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: GHA-SAN-94
    source_category_code: kvip
    national_label_en: KVIP
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: GHA-SAN-95
    source_category_code: pit_latrine_ventilated_improved_pit_vip
    national_label_en: Pit latrine - ventilated improved pit (VIP)
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: GHA-SAN-96
    source_category_code: private_ventilated_improved_pit_latrine
    national_label_en: 'Private: Ventilated improved pit latrine'
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: GHA-SAN-97
    source_category_code: ventilated_improved_pit_vip_latrine
    national_label_en: Ventilated improved pit (VIP) latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: GHA-SAN-98
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated improved pit latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: GHA-SAN-99
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit latrine (VIP)
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: GHA-SAN-100
    source_category_code: ventilated_improved_pit_toilet
    national_label_en: Ventilated improved pit toilet
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: GHA-SAN-101
    source_category_code: ventilation_improved_pit_latrine
    national_label_en: ventilation improved pit latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: GHA-SAN-102
    source_category_code: vip
    national_label_en: VIP
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: GHA-SAN-103
    source_category_code: bucket_pan
    national_label_en: Bucket/Pan
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.private_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 118
  - country_entry_id: GHA-SAN-104
    source_category_code: private_covered_dry_latrine_with_privacy
    national_label_en: Private covered dry latrine (with privacy)
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 114
  - country_entry_id: GHA-SAN-105
    source_category_code: pit_latrine
    national_label_en: Pit latrine
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: GHA-SAN-106
    source_category_code: kvip_vip
    national_label_en: KVIP/VIP
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 113
  - country_entry_id: GHA-SAN-107
    source_category_code: shared_covered_dry_latrine_with_privacy
    national_label_en: Shared covered dry latrine (with privacy)
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 122
  - country_entry_id: GHA-SAN-108
    source_category_code: private_pour_flush_latrine
    national_label_en: Private pour flush latrine
    national_label_local: Private pour flush latrine
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 91
  - country_entry_id: GHA-SAN-109
    source_category_code: shared_pour_flush_latrine
    national_label_en: Shared pour flush latrine
    national_label_local: Public/shared pour flush latrine
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 97
  - country_entry_id: GHA-SAN-110
    source_category_code: flush_pour_to_other_location
    national_label_en: flush/pour to other location
    national_label_local: to elsewhere
    jmp_classification: Latrines > Pour flush latrines > to elsewhere
    jmp_id: latrines.pour_flush_latrines.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 90
  - country_entry_id: GHA-SAN-111
    source_category_code: flush_pour_to_pit_latrine
    national_label_en: flush/pour to pit latrine
    national_label_local: to pit
    jmp_classification: Latrines > Pour flush latrines > to pit
    jmp_id: latrines.pour_flush_latrines.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 88
  - country_entry_id: GHA-SAN-112
    source_category_code: septic_tank_manhole
    national_label_en: Septic tank (manhole)
    national_label_local: to septic tank
    jmp_classification: Latrines > Pour flush latrines > to septic tank
    jmp_id: latrines.pour_flush_latrines.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: GHA-SAN-113
    source_category_code: flush_pour_to_unknown
    national_label_en: flush/pour to unknown
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Latrines > Pour flush latrines > to unknown place/ not sure/DK
    jmp_id: latrines.pour_flush_latrines.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 89
  - country_entry_id: GHA-SAN-114
    source_category_code: no_facilities
    national_label_en: No Facilities
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-115
    source_category_code: no_facilities_bush_field
    national_label_en: no facilities (bush, field)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-116
    source_category_code: no_facilities_bush_beach_field
    national_label_en: No facilities (bush/beach/field)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-117
    source_category_code: no_facilities_open_defecation
    national_label_en: No facilities (open defecation)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-118
    source_category_code: no_facilities_or_bush_or_field
    national_label_en: No facilities or bush or field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-119
    source_category_code: no_facilities_bush
    national_label_en: No Facilities/Bush
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-120
    source_category_code: no_facility
    national_label_en: No facility
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-121
    source_category_code: no_facility_bush_field_etc
    national_label_en: No facility (bush, field, etc)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-122
    source_category_code: no_facility_bush_beach_field
    national_label_en: No facility (bush/beach/field)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-123
    source_category_code: no_facility_bush_field
    national_label_en: No facility / bush / field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-124
    source_category_code: no_facility_bush_field
    national_label_en: No facility, bush, field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-125
    source_category_code: no_facility_bush
    national_label_en: No facility/bush
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-126
    source_category_code: no_facility_bush_field
    national_label_en: No facility/bush/field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-127
    source_category_code: no_latrine
    national_label_en: No latrine
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-128
    source_category_code: no_toilet
    national_label_en: No toilet
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-129
    source_category_code: no_toilet_facility
    national_label_en: No toilet facility
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-130
    source_category_code: no_toilet_facility_bush_beach
    national_label_en: No toilet facility (bush, beach)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-131
    source_category_code: non_pas_disponible
    national_label_en: Non, pas disponible
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-132
    source_category_code: none_bush_or_field
    national_label_en: None (bush or field)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-133
    source_category_code: open_defecation
    national_label_en: Open defecation
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GHA-SAN-134
    source_category_code: enviro_loo
    national_label_en: Enviro Loo
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: GHA-SAN-135
    source_category_code: flush_bio_digester_biofil
    national_label_en: Flush, bio-digester (biofil)
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: GHA-SAN-136
    source_category_code: pit_latrine_with_seat
    national_label_en: Pit latrine with seat
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: GHA-SAN-137
    source_category_code: public_toilet_flush_bucket_kvip
    national_label_en: Public toilet (flush bucket/KVIP)
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: GHA-SAN-138
    source_category_code: public_toilet_flush_bucket_kvip
    national_label_en: Public toilet (flush, bucket, KVIP)
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: GHA-SAN-139
    source_category_code: public_toilet_wc_kvip_pit_pan_etc
    national_label_en: Public toilet (WC,KVIP,Pit,Pan, etc)
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: GHA-SAN-140
    source_category_code: bio_gas
    national_label_en: Bio gas
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 133
  - country_entry_id: GHA-SAN-141
    source_category_code: mobile_toilet
    national_label_en: Mobile toilet
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 133
  - country_entry_id: GHA-SAN-142
    source_category_code: mobile_toilet
    national_label_en: Mobile Toilet
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: GHA-SAN-143
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: GHA-SAN-144
    source_category_code: other_incl_bucket_open_pit_latrine
    national_label_en: Other (incl. bucket, open pit latrine)
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: GHA-SAN-145
    source_category_code: other_specify
    national_label_en: Other (Specify)
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: GHA-SAN-146
    source_category_code: other_type_of_sanitation
    national_label_en: Other type of sanitation
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: GHA-SAN-147
    source_category_code: other_unimproved_we_don_t_know_the_type_of_facilities
    national_label_en: Other unimproved (we don't know the type of facilities)
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: GHA-SAN-148
    source_category_code: other_specify
    national_label_en: other, specify
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: GHA-SAN-149
    source_category_code: public_toilet_wc_kvip_pit_pan_etc
    national_label_en: Public toilet (WC, KVIP, Pit, Pan etc.)
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: GHA-SAN-150
    source_category_code: toilet_in_another_house
    national_label_en: Toilet in another house
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: GHA-SAN-151
    source_category_code: don_t_know
    national_label_en: don't know
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  - country_entry_id: GHA-SAN-152
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  - country_entry_id: GHA-SAN-153
    source_category_code: others
    national_label_en: Others
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_GHA_Ghana_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: GHA-WAS-01
    source_category_code: spring
    national_label_en: Spring
    national_label_local: All springs
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: GHA-WAS-02
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: GHA-WAS-03
    source_category_code: protected_spring_closed
    national_label_en: Protected spring (closed)
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: GHA-WAS-04
    source_category_code: spring
    national_label_en: Spring
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: GHA-WAS-05
    source_category_code: spring_protected
    national_label_en: Spring - protected
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: GHA-WAS-06
    source_category_code: dug_protected_well
    national_label_en: Dug protected well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: GHA-WAS-07
    source_category_code: dug_well_protected
    national_label_en: 'Dug Well: Protected'
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: GHA-WAS-08
    source_category_code: protected_dug_well
    national_label_en: Protected dug well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: GHA-WAS-09
    source_category_code: protected_dug_well_closed_or_with_handpump
    national_label_en: Protected dug well (closed) or with handpump
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: GHA-WAS-10
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: GHA-WAS-11
    source_category_code: protected_well_in_dwelling_yard
    national_label_en: Protected well in dwelling/yard
    national_label_local: Private
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: GHA-WAS-12
    source_category_code: protected_public_well
    national_label_en: Protected public well
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 68
  - country_entry_id: GHA-WAS-13
    source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: Protected wells or springs
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: yes
    shared_flag: no
    source_row: 46
  - country_entry_id: GHA-WAS-14
    source_category_code: well
    national_label_en: Well
    national_label_local: Traditional wells
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: GHA-WAS-15
    source_category_code: well_without_pump
    national_label_en: Well without pump
    national_label_local: Traditional wells
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: GHA-WAS-16
    source_category_code: well_in_residence
    national_label_en: Well in Residence
    national_label_local: Private
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 63
  - country_entry_id: GHA-WAS-17
    source_category_code: public_well
    national_label_en: Public Well
    national_label_local: Public
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 64
  - country_entry_id: GHA-WAS-18
    source_category_code: bore_hole
    national_label_en: Bore hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-19
    source_category_code: bore_hole_pump_tube_well
    national_label_en: Bore-hole/Pump/Tube well
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-20
    source_category_code: borehole
    national_label_en: Borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-21
    source_category_code: borehole_with_handpump_pump
    national_label_en: Borehole (with handpump/pump)
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-22
    source_category_code: borehole_pump_tube_well
    national_label_en: Borehole/Pump/Tube well
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-23
    source_category_code: protected_tube_well_or_bore_hole
    national_label_en: Protected tube well or bore hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-24
    source_category_code: tube_well_or_borehole
    national_label_en: tube well or borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-25
    source_category_code: tube_well_borehole
    national_label_en: Tube well, borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-26
    source_category_code: tubewell_or_borehole
    national_label_en: Tubewell or borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-27
    source_category_code: tubewell_borehole
    national_label_en: Tubewell, borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-28
    source_category_code: tubewell_bore_hole
    national_label_en: Tubewell/bore hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-29
    source_category_code: tubewell_borehole
    national_label_en: Tubewell/borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-30
    source_category_code: well_with_pump
    national_label_en: Well with pump
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GHA-WAS-31
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: GHA-WAS-32
    source_category_code: spring
    national_label_en: Spring
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: GHA-WAS-33
    source_category_code: spring_unprotected
    national_label_en: Spring - unprotected
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: GHA-WAS-34
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: GHA-WAS-35
    source_category_code: unprotected_spring_open
    national_label_en: Unprotected spring (open)
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: GHA-WAS-36
    source_category_code: dug_unprotected_well
    national_label_en: Dug unprotected well
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GHA-WAS-37
    source_category_code: dug_well_unprotected
    national_label_en: 'Dug Well: Unprotected'
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GHA-WAS-38
    source_category_code: unprotected_dug_well
    national_label_en: Unprotected dug well
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GHA-WAS-39
    source_category_code: unprotected_dug_well_open
    national_label_en: Unprotected dug well (open)
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GHA-WAS-40
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GHA-WAS-41
    source_category_code: water_from_open_or_covered_well_or_borehole
    national_label_en: Water from open or covered well or borehole
    national_label_local: Other
    jmp_classification: Ground water > Unprotected well > Other
    jmp_id: ground_water.unprotected_well.other
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 73
  - country_entry_id: GHA-WAS-42
    source_category_code: open_well_in_dwelling_yard
    national_label_en: Open well in dwelling/yard
    national_label_local: Private
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: GHA-WAS-43
    source_category_code: open_public_well
    national_label_en: Open public well
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 72
  - country_entry_id: GHA-WAS-44
    source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: Unprotected wells or springs
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 50
  - country_entry_id: GHA-WAS-45
    source_category_code: cart_with_small_tank
    national_label_en: cart with small tank
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: GHA-WAS-46
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank / drum
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: GHA-WAS-47
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank/drum
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: GHA-WAS-48
    source_category_code: purchased_from_a_cart_with_a_small_tank_or_drum
    national_label_en: Purchased from a cart with a small tank or drum
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: GHA-WAS-49
    source_category_code: small_scale_vendor
    national_label_en: small scale vendor
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: GHA-WAS-50
    source_category_code: vendor
    national_label_en: Vendor,
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: GHA-WAS-51
    source_category_code: water_vendor
    national_label_en: Water vendor
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: GHA-WAS-52
    source_category_code: neighbouring_household
    national_label_en: Neighbouring household
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: GHA-WAS-53
    source_category_code: water_vendor
    national_label_en: Water vendor
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: GHA-WAS-54
    source_category_code: purchased_from_a_tanker_truck
    national_label_en: Purchased from a tanker truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-55
    source_category_code: tanker_supply_vendor_provided
    national_label_en: Tanker supply/vendor provided
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-56
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-57
    source_category_code: tanker_truck
    national_label_en: Tanker-truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-58
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker-truck, vendor
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-59
    source_category_code: tanker_truck_lorry
    national_label_en: tanker-truck/lorry
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-60
    source_category_code: tanker_truck
    national_label_en: Tanker/truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-61
    source_category_code: truck_vendor
    national_label_en: Truck, vendor
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-62
    source_category_code: vendor_truck
    national_label_en: Vendor, truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-63
    source_category_code: water_truck_tanker_service
    national_label_en: Water truck/tanker service
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-64
    source_category_code: water_selling_cart_or_truck
    national_label_en: Water-selling cart or truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GHA-WAS-65
    source_category_code: bottled_without_improved
    national_label_en: Bottled without improved
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-WAS-66
    source_category_code: dugout
    national_label_en: Dugout
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-WAS-67
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-WAS-68
    source_category_code: other_specify
    national_label_en: Other, specify
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: GHA-WAS-69
    source_category_code: bottled_water_users_with_unimproved_source
    national_label_en: Bottled water users with unimproved source
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: GHA-WAS-70
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: GHA-WAS-71
    source_category_code: refused_don_t_know
    national_label_en: Refused + Don't know
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: GHA-WAS-72
    source_category_code: sachet_water
    national_label_en: Sachet water
    national_label_local: Packaged water
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 89
  - country_entry_id: GHA-WAS-73
    source_category_code: sachet_bottled_water
    national_label_en: Sachet/bottled water
    national_label_local: Packaged water
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 89
  - country_entry_id: GHA-WAS-74
    source_category_code: bottled_or_sachet_water
    national_label_en: Bottled or sachet water
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: GHA-WAS-75
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: GHA-WAS-76
    source_category_code: bottled_water_users_with_other_improved_source
    national_label_en: Bottled water users with other improved source
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: GHA-WAS-77
    source_category_code: bottled_with_improved
    national_label_en: Bottled with improved
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: GHA-WAS-78
    source_category_code: bottled_sachet_water
    national_label_en: Bottled/sachet water
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: GHA-WAS-79
    source_category_code: sachet_water
    national_label_en: Sachet water
    national_label_local: Sachet water
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: GHA-WAS-80
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: Rainwater
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: GHA-WAS-81
    source_category_code: rain_water
    national_label_en: Rain water
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: GHA-WAS-82
    source_category_code: rain_water_collection
    national_label_en: Rain water collection
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: GHA-WAS-83
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: GHA-WAS-84
    source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: GHA-WAS-85
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: GHA-WAS-86
    source_category_code: river_lake_pond
    national_label_en: River, lake, pond
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-87
    source_category_code: river_lake_spring_pond
    national_label_en: River, lake, spring, pond
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-88
    source_category_code: river_lake_stream
    national_label_en: River, lake, stream
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-89
    source_category_code: river_dam_lake_ponds_stream_canal_irrigation_channel
    national_label_en: river/dam/lake/ponds/stream/canal/irrigation channel
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-90
    source_category_code: river_stream_dam_lake_pond_canal_irrigation_channel
    national_label_en: River/stream + Dam, lake, pond, canal, irrigation channel
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-91
    source_category_code: river_stream_dugout_pond_lake_dam
    national_label_en: River/Stream + Dugout/pond/lake/dam
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-92
    source_category_code: stream_lake_river
    national_label_en: Stream/Lake/River
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-93
    source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-94
    source_category_code: surface_water_pond_river_stream
    national_label_en: Surface water (pond/river/stream)
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-95
    source_category_code: surface_water_river_lake_etc
    national_label_en: surface water (river, lake, etc)
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-96
    source_category_code: surface_water_river_stream_dam_lake_pond_canal_irrigation_channel
    national_label_en: Surface water (river, stream, dam, lake, pond, canal, irrigation
      channel)
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-97
    source_category_code: surface_water_river_dam_lake_pond_stream_canal_irrigation_c
    national_label_en: Surface water (river/dam/lake/pond/stream/canal/irrigation
      c
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-98
    source_category_code: surface_water_like_a_river_dam_lake_pond_stream_canal_or_irrigation_channel
    national_label_en: Surface water, like a river, dam, lake, pond, stream, canal
      or irrigation channel
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-99
    source_category_code: water_taken_directly_from_pond_water_or_stream
    national_label_en: Water taken directly from pond-water or stream
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GHA-WAS-100
    source_category_code: dam
    national_label_en: Dam
    national_label_local: Dam
    jmp_classification: Surface water > Dam
    jmp_id: surface_water.dam
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 95
  - country_entry_id: GHA-WAS-101
    source_category_code: dam_lake_pond_canal_irrigation_channel
    national_label_en: Dam/lake/pond/canal/irrigation channel
    national_label_local: Dam
    jmp_classification: Surface water > Dam
    jmp_id: surface_water.dam
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 95
  - country_entry_id: GHA-WAS-102
    source_category_code: dugout_pond_lake_dam_canal
    national_label_en: Dugout/Pond/Lake/Dam/Canal
    national_label_local: Lake
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 94
  - country_entry_id: GHA-WAS-103
    source_category_code: pond_lake
    national_label_en: Pond, lake
    national_label_local: Pond
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - country_entry_id: GHA-WAS-104
    source_category_code: pond_lake
    national_label_en: Pond/lake
    national_label_local: Pond
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - country_entry_id: GHA-WAS-105
    source_category_code: surface_water_pond_canal_irrigation_channel
    national_label_en: Surface water (pond, canal,irrigation channel)
    national_label_local: Pond
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - country_entry_id: GHA-WAS-106
    source_category_code: river_stream
    national_label_en: River, stream
    national_label_local: River
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: GHA-WAS-107
    source_category_code: river_stream
    national_label_en: River/Stream
    national_label_local: River
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: GHA-WAS-108
    source_category_code: surface_water_river_stream_dam_lake
    national_label_en: Surface water (river,stream,dam, lake)
    national_label_local: River
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: GHA-WAS-109
    source_category_code: pipe_in_neighbouring_household
    national_label_en: Pipe in neighbouring household
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: GHA-WAS-110
    source_category_code: pipe_borne_from_neighbour_s_tap
    national_label_en: Pipe-borne from neighbour's tap
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: GHA-WAS-111
    source_category_code: pipe_borne_outside_dwelling_but_from_neighbour_s_house
    national_label_en: Pipe-borne outside dwelling but from neighbour's house
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: GHA-WAS-112
    source_category_code: pipe_borne_outside_dwelling_but_from_neighbours_house
    national_label_en: Pipe-borne outside dwelling but from neighbours house
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: GHA-WAS-113
    source_category_code: piped_to_neighbor
    national_label_en: piped to neighbor
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: GHA-WAS-114
    source_category_code: piped_to_neighbour
    national_label_en: Piped to neighbour
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: GHA-WAS-115
    source_category_code: private_outside_standpipe_tap
    national_label_en: Private outside standpipe/tap
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: GHA-WAS-116
    source_category_code: sachet_water
    national_label_en: Sachet water
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: GHA-WAS-117
    source_category_code: water_piped_to_neighbour_water_pipe_outside_compound_yard_or_plot
    national_label_en: Water piped to neighbour + Water pipe outside compound, yard
      or plot
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: GHA-WAS-118
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: GHA-WAS-119
    source_category_code: piped_into_dwelling_or_compound
    national_label_en: Piped into dwelling or compound
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: GHA-WAS-120
    source_category_code: piped_into_residence
    national_label_en: Piped into residence
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: GHA-WAS-121
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: GHA-WAS-122
    source_category_code: standpipe_in_house
    national_label_en: Standpipe in House
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: GHA-WAS-123
    source_category_code: indoor_plumbing_inside_standpipe
    national_label_en: Indoor plumbing + Inside standpipe
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GHA-WAS-124
    source_category_code: indoor_plumbing_standpipe
    national_label_en: Indoor plumbing/standpipe
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GHA-WAS-125
    source_category_code: pipe_borne_inside_dwelling
    national_label_en: Pipe-borne inside dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GHA-WAS-126
    source_category_code: piped_own_tap
    national_label_en: Piped (own tap)
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GHA-WAS-127
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GHA-WAS-128
    source_category_code: piped_private
    national_label_en: piped private
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GHA-WAS-129
    source_category_code: piped_water
    national_label_en: Piped water
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GHA-WAS-130
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GHA-WAS-131
    source_category_code: water_piped_into_dwelling
    national_label_en: Water piped into dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GHA-WAS-132
    source_category_code: pipe_borne_outside_dwelling_but_not_on_compound
    national_label_en: Pipe-borne outside dwelling but not on compound
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-133
    source_category_code: pipe_borne_outside_dwelling_but_on_compound
    national_label_en: Pipe-borne outside dwelling but on compound
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-134
    source_category_code: piped_into_compound_yard_or_plot
    national_label_en: Piped into compound, yard or plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-135
    source_category_code: piped_into_compound_plot
    national_label_en: Piped into compound/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-136
    source_category_code: piped_into_yard
    national_label_en: Piped into yard
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-137
    source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-138
    source_category_code: piped_to_yard_plot
    national_label_en: piped to yard/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-139
    source_category_code: piped_water_into_yard
    national_label_en: Piped water into yard
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-140
    source_category_code: piped_water_into_yard_plot_or_compound
    national_label_en: Piped water into yard, plot or compound
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-141
    source_category_code: piped_water_to_compound_yard_plot
    national_label_en: Piped water to compound yard/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-142
    source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-143
    source_category_code: private_outside_standpipe_tap
    national_label_en: Private outside standpipe/tap
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-144
    source_category_code: water_piped_into_compound
    national_label_en: Water piped into compound
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GHA-WAS-145
    source_category_code: public_outdoor_tap
    national_label_en: Public outdoor tap
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: GHA-WAS-146
    source_category_code: public_standpipe
    national_label_en: Public standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: GHA-WAS-147
    source_category_code: public_tap
    national_label_en: Public Tap
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: GHA-WAS-148
    source_category_code: public_tap_standpipe
    national_label_en: Public tap / standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: GHA-WAS-149
    source_category_code: public_tap_or_standpipe
    national_label_en: Public tap or standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: GHA-WAS-150
    source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: GHA-WAS-151
    source_category_code: public_tap_neighbour
    national_label_en: Public Tap/Neighbour
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: GHA-WAS-152
    source_category_code: public_tap_neighbour_s_house
    national_label_en: Public tap/neighbour's house
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: GHA-WAS-153
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: GHA-WAS-154
    source_category_code: standpipe_outside_house
    national_label_en: Standpipe outside house
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_GHA_Ghana_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---









No country-specific content has been supplied yet. The regional focal point
must be consulted before harmonization relies on this country layer.
