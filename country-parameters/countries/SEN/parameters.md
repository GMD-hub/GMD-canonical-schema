---
country_id: CTY-SEN
iso3: SEN
schema_version: '0.2'
status: draft
country_name: SEN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SEN-EDU-01
    national_label_en: "\xC9ducation pr\xE9-scolaire"
    national_label_local: "\xC9ducation pr\xE9-scolaire"
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
  - country_entry_id: SEN-EDU-02
    national_label_en: "Enseignement \xE9l\xE9mentaire"
    national_label_local: "Enseignement \xE9l\xE9mentaire"
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
    - SEN-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: SEN-EDU-03
    national_label_en: "Enseignement moyen g\xE9n\xE9ral"
    national_label_local: "Enseignement moyen g\xE9n\xE9ral"
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - SEN-EDU-02
    cum_years_schooling: 10
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SEN-EDU-04
    national_label_en: Enseignement Moyen professionnel
    national_label_local: Enseignement Moyen professionnel
    entry_age: 15
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - SEN-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SEN-EDU-05
    national_label_en: "Enseignement secondaire g\xE9n\xE9ral \n(2-\xE8me cycle)"
    national_label_local: "Enseignement secondaire g\xE9n\xE9ral \n(2-\xE8me cycle)"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - SEN-EDU-03
    - SEN-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-05
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
  - country_entry_id: SEN-EDU-06
    national_label_en: Enseignement secondaire technique (BEP)
    national_label_local: Enseignement secondaire technique (BEP)
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - SEN-EDU-03
    - SEN-EDU-04
    cum_years_schooling: 11
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
  - country_entry_id: SEN-EDU-07
    national_label_en: Enseignement secondaire technique et professionnel
    national_label_local: Enseignement secondaire technique et professionnel
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - SEN-EDU-03
    - SEN-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
  - country_entry_id: SEN-EDU-08
    national_label_en: Enseignement secondaire technique (Bac technique)
    national_label_local: Enseignement secondaire technique (Bac technique)
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - SEN-EDU-03
    - SEN-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
  - country_entry_id: SEN-EDU-09
    national_label_en: Formation professionnelle
    national_label_local: "Capacit\xE9 en droit"
    entry_age: 19
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - SEN-EDU-05
    - SEN-EDU-06
    - SEN-EDU-07
    - SEN-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
  - country_entry_id: SEN-EDU-10
    national_label_en: Formation des instituteurs
    national_label_local: Formation des instituteurs
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - SEN-EDU-05
    - SEN-EDU-06
    - SEN-EDU-07
    - SEN-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
  - country_entry_id: SEN-EDU-11
    national_label_en: "Formation des professeurs des coll\xE8ges d'enseignement moyen"
    national_label_local: "Formation des professeurs des coll\xE8ges d'enseignement\
      \ moyen"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - SEN-EDU-05
    - SEN-EDU-06
    - SEN-EDU-07
    - SEN-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
  - country_entry_id: SEN-EDU-12
    national_label_en: "Enseignement sup\xE9rieur professionnel"
    national_label_local: "Enseignement sup\xE9rieur professionnel"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - SEN-EDU-05
    - SEN-EDU-06
    - SEN-EDU-07
    - SEN-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
  - country_entry_id: SEN-EDU-13
    national_label_en: "Enseignement sup\xE9rieur (Licence)"
    national_label_local: "Enseignement sup\xE9rieur (Licence)"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - SEN-EDU-05
    - SEN-EDU-06
    - SEN-EDU-07
    - SEN-EDU-08
    cum_years_schooling: 14
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
  - country_entry_id: SEN-EDU-14
    national_label_en: Formation d'enseignant du moyen
    national_label_local: Formation d'enseignant du moyen
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - SEN-EDU-05
    - SEN-EDU-06
    - SEN-EDU-07
    - SEN-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
  - country_entry_id: SEN-EDU-15
    national_label_en: "Enseignement universitaire (Formation d'ing\xE9nieurs: agronome,\
      \ g\xE9ologue,statistique, genie civil etc.)"
    national_label_local: "Enseignement universitaire (Formation d'ing\xE9nieurs:\
      \ agronome, g\xE9ologue,statistique, genie civil etc.)"
    entry_age: 19
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - SEN-EDU-05
    - SEN-EDU-06
    - SEN-EDU-07
    - SEN-EDU-08
    cum_years_schooling: 14
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
  - country_entry_id: SEN-EDU-16
    national_label_en: "Docteur en pharmacie ou m\xE9decine"
    national_label_local: "Docteur en pharmacie ou m\xE9decine"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - SEN-EDU-05
    - SEN-EDU-06
    - SEN-EDU-07
    - SEN-EDU-08
    cum_years_schooling: 16
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
  - country_entry_id: SEN-EDU-17
    national_label_en: "Enseignement sup\xE9rieur (Master)"
    national_label_local: "Enseignement sup\xE9rieur (Master)"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - SEN-EDU-13
    - SEN-EDU-14
    cum_years_schooling: 14
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-14
    - SEN-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
    - 'minimum parent path selected from: SEN-EDU-13, SEN-EDU-14'
  - country_entry_id: SEN-EDU-18
    national_label_en: Formation d'enseignant du secondaire
    national_label_local: Formation d'enseignant du secondaire
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - SEN-EDU-05
    - SEN-EDU-06
    - SEN-EDU-07
    - SEN-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
  - country_entry_id: SEN-EDU-19
    national_label_en: "Enseignement sup\xE9rieur (Doctorat)"
    national_label_local: "Enseignement sup\xE9rieur (Doctorat)"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - SEN-EDU-15
    - SEN-EDU-16
    - SEN-EDU-17
    - SEN-EDU-18
    cum_years_schooling: 16
    cum_years_computation_path:
    - SEN-EDU-02
    - SEN-EDU-04
    - SEN-EDU-06
    - SEN-EDU-18
    - SEN-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SEN-EDU-03, SEN-EDU-04'
    - 'minimum parent path selected from: SEN-EDU-05, SEN-EDU-06, SEN-EDU-07, SEN-EDU-08'
    - 'minimum parent path selected from: SEN-EDU-15, SEN-EDU-16, SEN-EDU-17, SEN-EDU-18'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Senegal.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SEN-SUBNAT-01
    survey_labels: 1 - DAKAR | 1 - Dakar | 1 -Dakar
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_2636
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_2636
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2636'
    geo_nvar: ADM1_NAME
    geo_name: Dakar
    source_row: 14530
  - country_entry_id: SEN-SUBNAT-02
    survey_labels: "10 - Thies | 10 - Thi\xE8s | 7 - THIES | 7 - Thi\xE8s"
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_2644
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_2644
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2644'
    geo_nvar: ADM1_NAME
    geo_name: Thies
    source_row: 14531
  - country_entry_id: SEN-SUBNAT-03
    survey_labels: 11 - Ziguinchor | 2 - ZIGUINCHOR | 2 - Ziguinchor
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_2645
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_2645
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2645'
    geo_nvar: ADM1_NAME
    geo_name: Ziguinchor
    source_row: 14532
  - country_entry_id: SEN-SUBNAT-04
    survey_labels: 2 - Diourbel | 3 - DIOURBEL | 3 - Diourbel
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_47585
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_47585
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '47585'
    geo_nvar: ADM1_NAME
    geo_name: Diourbel
    source_row: 14533
  - country_entry_id: SEN-SUBNAT-05
    survey_labels: 3 - Fatick | 9 - FATICK | 9 - Fatick
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_47586
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_47586
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '47586'
    geo_nvar: ADM1_NAME
    geo_name: Fatick
    source_row: 14534
  - country_entry_id: SEN-SUBNAT-06
    survey_labels: 4 - Kaolack | 6 - KAOLACK | 6 - Kaolack
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_1373
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_1373
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1373'
    geo_nvar: ADM1_NAME
    geo_name: Kaolack
    source_row: 14535
  - country_entry_id: SEN-SUBNAT-07
    survey_labels: 10 - KOLDA | 10 - Kolda | 5 - Kolda
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_1375
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_1375
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1375'
    geo_nvar: ADM1_NAME
    geo_name: Kolda
    source_row: 14536
  - country_entry_id: SEN-SUBNAT-08
    survey_labels: 6 - Louga | 8 - LOUGA | 8 - Louga
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_47587
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_47587
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '47587'
    geo_nvar: ADM1_NAME
    geo_name: Louga
    source_row: 14537
  - country_entry_id: SEN-SUBNAT-09
    survey_labels: 11 - MATAM | 11 - Matam | 7 - Matam
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_47588
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_47588
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '47588'
    geo_nvar: ADM1_NAME
    geo_name: Matam
    source_row: 14538
  - country_entry_id: SEN-SUBNAT-10
    survey_labels: 4 - SAINT-LOUIS | 4 - Saint-Louis | 8 - Saint-Louis
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_47589
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_47589
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '47589'
    geo_nvar: ADM1_NAME
    geo_name: Saint louis
    source_row: 14539
  - country_entry_id: SEN-SUBNAT-11
    survey_labels: 5 - TAMBACOUNDA | 5 - Tambacounda | 9 - Tambacounda
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_1377
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_1377
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1377'
    geo_nvar: ADM1_NAME
    geo_name: Tambacounda
    source_row: 14540
  - country_entry_id: SEN-SUBNAT-12
    survey_labels: 12 - KAFFRINE | 12 - Kaffrine | Kaffrine
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_1378
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_1378
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1378'
    geo_nvar: ADM1_NAME
    geo_name: Kaffrine
    source_row: 14552
  - country_entry_id: SEN-SUBNAT-13
    survey_labels: "13 - KEDOUGOU | 13 - K\xE9dougou | Kedougou"
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_1374
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_1374
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1374'
    geo_nvar: ADM1_NAME
    geo_name: Kedougou
    source_row: 14553
  - country_entry_id: SEN-SUBNAT-14
    survey_labels: "14 - SEDHIOU | 14 - S\xE9dhiou | Sedhiou"
    survey_variables: subnatid
    gmd_subnatid1: SEN_2015_GAUL1_1376
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SEN_2015_GAUL1_1376
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1376'
    geo_nvar: ADM1_NAME
    geo_name: Sedhiou
    source_row: 14554
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
  - country_entry_id: SEN-SAN-01
    source_category_code: composting_toilet
    national_label_en: composting toilet
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: SEN-SAN-02
    source_category_code: toilettes_a_compostage
    national_label_en: Toilettes a compostage
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: SEN-SAN-03
    source_category_code: chasse_d_eau_avec_egout
    national_label_en: Chasse d'eau avec egout
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: SEN-SAN-04
    source_category_code: wc_raccorde_avec_chasse
    national_label_en: WC raccorde avec chasse
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: SEN-SAN-05
    source_category_code: wc_fosse
    national_label_en: WC fosse
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: SEN-SAN-06
    source_category_code: chasse_d_eau_avec_fosse_septique
    national_label_en: Chasse d'eau avec fosse septique
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: SEN-SAN-07
    source_category_code: wc_raccorde_sans_chasse
    national_label_en: WC raccorde sans chasse
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: SEN-SAN-08
    source_category_code: wc
    national_label_en: WC
    national_label_local: "Toilette \xE0 chasse d'eau"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: SEN-SAN-09
    source_category_code: chasse_d_eau_personnelle
    national_label_en: Chasse d'eau personnelle
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: SEN-SAN-10
    source_category_code: private_wc
    national_label_en: Private WC
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: SEN-SAN-11
    source_category_code: chasse_branchee_a_un_systeme_d_egout
    national_label_en: "Chasse branch\xE9e \xE0 un syst\xE8me d\u2019\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: SEN-SAN-12
    source_category_code: private_domestic_connection_to_sewage_system
    national_label_en: Private domestic connection to sewage system
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: SEN-SAN-13
    source_category_code: toilette_latrine_fosse_chasse_d_eau_chasse_manuelle_connectee_a_un_systeme_d_egout
    national_label_en: "Toilette/latrine fosse Chasse d\u2019eau/chasse manuelle connect\xE9\
      e \xE0 un syst\xE8me d\u2019\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: SEN-SAN-14
    source_category_code: chasse_branchee_a_une_fosse_septique
    national_label_en: "Chasse branch\xE9e \xE0 une fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: SEN-SAN-15
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_septique
    national_label_en: "Chasse d\u2019eau/chasse manuelle reli\xE9e \xE0 une fosse\
      \ septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: SEN-SAN-16
    source_category_code: private_flush_to_septic_tank
    national_label_en: Private flush to septic tank
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: SEN-SAN-17
    source_category_code: chasse_d_eau_commune
    national_label_en: Chasse d'eau commune
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: SEN-SAN-18
    source_category_code: edicule_public
    national_label_en: Edicule public
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: SEN-SAN-19
    source_category_code: shared_wc
    national_label_en: Shared WC
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: SEN-SAN-20
    source_category_code: chasse_branchee_a_un_systeme_d_egout
    national_label_en: "Chasse branch\xE9e \xE0 un syst\xE8me d\u2019\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: SEN-SAN-21
    source_category_code: shared_domestic_connection_to_sewage_system
    national_label_en: Shared domestic connection to sewage system
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: SEN-SAN-22
    source_category_code: toilette_latrine_fosse_chasse_d_eau_chasse_manuelle_connectee_a_un_systeme_d_egout
    national_label_en: "Toilette/latrine fosse Chasse d\u2019eau/chasse manuelle connect\xE9\
      e \xE0 un syst\xE8me d\u2019\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: SEN-SAN-23
    source_category_code: chasse_branchee_a_une_fosse_septique
    national_label_en: "Chasse branch\xE9e \xE0 une fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 80
  - country_entry_id: SEN-SAN-24
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_septique
    national_label_en: "Chasse d\u2019eau/chasse manuelle reli\xE9e \xE0 une fosse\
      \ septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 80
  - country_entry_id: SEN-SAN-25
    source_category_code: shared_flush_to_septic_tank
    national_label_en: Shared flush to septic tank
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 80
  - country_entry_id: SEN-SAN-26
    source_category_code: chasse_d_eau_connectee_a_quelque_chose_d_autre
    national_label_en: "Chasse d'eau connect\xE9e \xE0 quelque chose d'autre"
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: SEN-SAN-27
    source_category_code: flush_to_somewhere_else
    national_label_en: flush - to somewhere else
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: SEN-SAN-28
    source_category_code: flush_to_somewhere_else
    national_label_en: flush to somewhere else
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: SEN-SAN-29
    source_category_code: chasse_branchee_a_un_systeme_d_egout
    national_label_en: "Chasse branch\xE9e \xE0 un syst\xE8me d\u2019\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-SAN-30
    source_category_code: chasse_d_eau
    national_label_en: Chasse d'eau
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-SAN-31
    source_category_code: chasse_d_eau_connectee_a_un_systeme_d_egout
    national_label_en: "Chasse d'eau connect\xE9e \xE0 un syst\xE8me d\u2019\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-SAN-32
    source_category_code: chasse_eau_avec_egout
    national_label_en: "Chasse eau avec \xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-SAN-33
    source_category_code: chasse_raccordee_a_l_egout
    national_label_en: Chasse raccordee a l'egout
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-SAN-34
    source_category_code: flush_to_piped_sewer_system
    national_label_en: flush - to piped sewer system
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-SAN-35
    source_category_code: flush_to_piped_sewer
    national_label_en: Flush to piped sewer
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-SAN-36
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-SAN-37
    source_category_code: chasse_d_eau_connectee_a_une_fosse_d_aisances
    national_label_en: "Chasse d'eau connect\xE9e \xE0 une Fosse d'aisances"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: SEN-SAN-38
    source_category_code: flush_to_pit_latrine
    national_label_en: flush - to pit latrine
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: SEN-SAN-39
    source_category_code: flush_to_pit_latrine
    national_label_en: flush to pit latrine
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: SEN-SAN-40
    source_category_code: chasse_avec_fosse
    national_label_en: Chasse avec fosse
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: SEN-SAN-41
    source_category_code: chasse_branchee_a_une_fosse_septique
    national_label_en: "Chasse branch\xE9e \xE0 une fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: SEN-SAN-42
    source_category_code: chasse_d_eau_branchee_a_fosse
    national_label_en: "Chasse d'eau branch\xE9e \xE0 fosse"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: SEN-SAN-43
    source_category_code: chasse_d_eau_connectee_a_une_fosse_septique
    national_label_en: "Chasse d'eau connect\xE9e \xE0 une fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: SEN-SAN-44
    source_category_code: chasse_eau_avec_fosse_sceptique
    national_label_en: Chasse eau avec fosse sceptique
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: SEN-SAN-45
    source_category_code: flush_to_septic_tank
    national_label_en: flush - to septic tank
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: SEN-SAN-46
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: SEN-SAN-47
    source_category_code: chasse_d_eau_connectee_a_ne_sait_pas_ou
    national_label_en: "Chasse d'eau connect\xE9e \xE0 ne sait pas o\xF9"
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: SEN-SAN-48
    source_category_code: flush_don_t_know_where
    national_label_en: flush - don't know where
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: SEN-SAN-49
    source_category_code: flush_don_t_know_where
    national_label_en: flush, don't know where
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: SEN-SAN-50
    source_category_code: has_a_flush_toilet
    national_label_en: has a flush toilet
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: SEN-SAN-51
    source_category_code: bucket_latrine_where_fresh_excreta_are_manually_removed
    national_label_en: Bucket latrine (where fresh excreta are manually removed)
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: SEN-SAN-52
    source_category_code: bucket_toilet
    national_label_en: bucket toilet
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: SEN-SAN-53
    source_category_code: cuvette_seau
    national_label_en: Cuvette/Seau
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: SEN-SAN-54
    source_category_code: pots_de_chambre
    national_label_en: Pots de chambre
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: SEN-SAN-55
    source_category_code: seau_tinette
    national_label_en: Seau/tinette
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: SEN-SAN-56
    source_category_code: hanging_toilet_latrine
    national_label_en: hanging toilet/latrine
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: SEN-SAN-57
    source_category_code: toilettes_latrines_suspendues
    national_label_en: Toilettes/latrines suspendues
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: SEN-SAN-58
    source_category_code: fosse_latrine_amelioree
    national_label_en: "Fosse/latrine am\xE9lior\xE9e"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-SAN-59
    source_category_code: fosses_d_aisances_avec_dalle
    national_label_en: "Fosses d\u2019aisances avec dalle"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-SAN-60
    source_category_code: latrine_amelioree
    national_label_en: "Latrine am\xE9lior\xE9e"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-SAN-61
    source_category_code: latrines_couvertes
    national_label_en: Latrines couvertes
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-SAN-62
    source_category_code: pit_latrine_with_slab
    national_label_en: pit latrine - with slab
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-SAN-63
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-SAN-64
    source_category_code: fosse
    national_label_en: Fosse
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: SEN-SAN-65
    source_category_code: latrine_non_couvertes
    national_label_en: Latrine non couvertes
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: SEN-SAN-66
    source_category_code: pit
    national_label_en: Pit
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: SEN-SAN-67
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: pit latrine - without slab / open pit
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: SEN-SAN-68
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: pit latrine without slab/open pit
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: SEN-SAN-69
    source_category_code: uncovered_dry_latrine_without_privacy
    national_label_en: Uncovered dry latrine (without privacy)
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: SEN-SAN-70
    source_category_code: fosse_rudimentaire
    national_label_en: Fosse rudimentaire
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-71
    source_category_code: fosses_d_aisances_sans_dalle
    national_label_en: Fosses d'aisances sans dalle
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-72
    source_category_code: latrine
    national_label_en: Latrine
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-73
    source_category_code: latrine_rudimentaire
    national_label_en: Latrine rudimentaire
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-74
    source_category_code: latrines_non_couvertes
    national_label_en: Latrines non couvertes
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-75
    source_category_code: latrines_seches_tradionelles
    national_label_en: Latrines seches tradionelles
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-76
    source_category_code: latrines_trad
    national_label_en: Latrines Trad.
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-77
    source_category_code: latrines_traditionnelles
    national_label_en: Latrines traditionnelles
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-78
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: pit latrine without slab/open pit
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-79
    source_category_code: traditional_latrine
    national_label_en: Traditional latrine
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-SAN-80
    source_category_code: fosse_d_aisances_ameliorees_ventilees
    national_label_en: "Fosse d\u2019aisances am\xE9lior\xE9es ventil\xE9es"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: SEN-SAN-81
    source_category_code: latrine_a_fosse_ventilee
    national_label_en: Latrine a fosse ventilee
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: SEN-SAN-82
    source_category_code: latrines_ventilees_ameliorees
    national_label_en: "Latrines ventil\xE9es am\xE9lior\xE9es"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: SEN-SAN-83
    source_category_code: pit_latrine_ventilated_improved_pit_vip
    national_label_en: pit latrine - ventilated improved pit (vip)
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: SEN-SAN-84
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated improved pit latrine (vip)
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: SEN-SAN-85
    source_category_code: bucket_toilet
    national_label_en: bucket toilet
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Private Latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.private_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 118
  - country_entry_id: SEN-SAN-86
    source_category_code: hanging_toilet_latrine
    national_label_en: hanging toilet/latrine
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Private Latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.private_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 117
  - country_entry_id: SEN-SAN-87
    source_category_code: fosses_d_aisances_avec_dalle
    national_label_en: "Fosses d\u2019aisances avec dalle"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: SEN-SAN-88
    source_category_code: pit_latrine_with_slab
    national_label_en: pit latrine with slab
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: SEN-SAN-89
    source_category_code: private_covered_dry_latrine_with_privacy
    national_label_en: Private covered dry latrine (with privacy)
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: SEN-SAN-90
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: pit latrine without slab/open pit
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine without
      slab/open pit
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 116
  - country_entry_id: SEN-SAN-91
    source_category_code: fosse_perdue
    national_label_en: fosse perdue
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 115
  - country_entry_id: SEN-SAN-92
    source_category_code: fosse_d_aisances_ameliorees_auto_aerees
    national_label_en: "Fosse d\u2019aisances am\xE9lior\xE9es auto-a\xE9r\xE9es"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 113
  - country_entry_id: SEN-SAN-93
    source_category_code: fosse_d_aisances_ameliorees_ventilees
    national_label_en: "Fosse d\u2019aisances am\xE9lior\xE9es ventil\xE9es"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 113
  - country_entry_id: SEN-SAN-94
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: ventilated improved pit latrine (vip)
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 113
  - country_entry_id: SEN-SAN-95
    source_category_code: fosses_d_aisances_avec_dalle
    national_label_en: "Fosses d\u2019aisances avec dalle"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: SEN-SAN-96
    source_category_code: shared_covered_dry_latrine_with_privacy
    national_label_en: Shared covered dry latrine (with privacy)
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: SEN-SAN-97
    source_category_code: edicule_public
    national_label_en: edicule public
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: true
    source_row: 123
  - country_entry_id: SEN-SAN-98
    source_category_code: fosse_d_aisances_ameliorees_auto_aerees
    national_label_en: "Fosse d\u2019aisances am\xE9lior\xE9es auto-a\xE9r\xE9es"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Ventilated
      Improved Pit latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 121
  - country_entry_id: SEN-SAN-99
    source_category_code: fosse_d_aisances_ameliorees_ventilees
    national_label_en: "Fosse d\u2019aisances am\xE9lior\xE9es ventil\xE9es"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Ventilated
      Improved Pit latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 121
  - country_entry_id: SEN-SAN-100
    source_category_code: latrines_a_chasse_manuelle
    national_label_en: "Latrines \xE0 chasse manuelle"
    national_label_local: "Latrines \xE0 chasse d'eau (priv\xE9es)"
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 91
  - country_entry_id: SEN-SAN-101
    source_category_code: private_pour_flush_latrine
    national_label_en: Private pour flush latrine
    national_label_local: "Latrines \xE0 chasse d'eau (priv\xE9es)"
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 91
  - country_entry_id: SEN-SAN-102
    source_category_code: latrines_a_chasse_manuelle
    national_label_en: "Latrines \xE0 chasse manuelle"
    national_label_local: "Latrines \xE0 chasse d'eau (publiques/partag\xE9es)"
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 97
  - country_entry_id: SEN-SAN-103
    source_category_code: shared_pour_flush_latrine
    national_label_en: Shared pour flush latrine
    national_label_local: "Latrines \xE0 chasse d'eau (publiques/partag\xE9es)"
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 97
  - country_entry_id: SEN-SAN-104
    source_category_code: aucun
    national_label_en: Aucun
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-105
    source_category_code: dans_la_nature
    national_label_en: dans la nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-106
    source_category_code: no_facilities
    national_label_en: No Facilities
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-107
    source_category_code: no_facilities_open_defecation
    national_label_en: No facilities (open defecation)
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-108
    source_category_code: no_facilities_nature
    national_label_en: No Facilities/Nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-109
    source_category_code: no_facility_bush_field
    national_label_en: No facility, bush, field
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-110
    source_category_code: no_facility_bush_field
    national_label_en: No facility/bush/field
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-111
    source_category_code: non_pas_disponible
    national_label_en: Non, pas disponible
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-112
    source_category_code: pas_de_toilette_nature
    national_label_en: Pas de toilette/nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-113
    source_category_code: pas_de_toilettes_nature
    national_label_en: Pas de toilettes/nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-114
    source_category_code: pas_toilette_dans_la_nature
    national_label_en: Pas toilette/dans la nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SEN-SAN-115
    source_category_code: edicule_public
    national_label_en: Edicule public
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: SEN-SAN-116
    source_category_code: latrine_with_manual_flush
    national_label_en: Latrine with manual flush
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: SEN-SAN-117
    source_category_code: latrines_a_chasse_manuelle
    national_label_en: "Latrines \xE0 chasse manuelle"
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: SEN-SAN-118
    source_category_code: latrines_a_chasse_manuelle_non_partagees
    national_label_en: "Latrines \xE0 chasse manuelle, non partagees"
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: SEN-SAN-119
    source_category_code: latrines_a_chasse_manuelle_non_partagee
    national_label_en: "Latrines \xE0 chasse manuelle, non partagee"
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 133
  - country_entry_id: SEN-SAN-120
    source_category_code: all_other_type_of_sanitation
    national_label_en: All other type of sanitation
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: SEN-SAN-121
    source_category_code: autre
    national_label_en: Autre
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: SEN-SAN-122
    source_category_code: autres
    national_label_en: Autres
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: SEN-SAN-123
    source_category_code: other
    national_label_en: Other
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: SEN-SAN-124
    source_category_code: chez_le_voisin
    national_label_en: Chez le voisin
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_SEN_Senegal_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SEN-WAS-01
    source_category_code: source
    national_label_en: Source
    national_label_local: Toutes les sources
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 74
  - country_entry_id: SEN-WAS-02
    source_category_code: spring
    national_label_en: Spring
    national_label_local: Toutes les sources
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 74
  - country_entry_id: SEN-WAS-03
    source_category_code: public_spring
    national_label_en: Public Spring
    national_label_local: Public
    jmp_classification: Ground water > All springs > Public
    jmp_id: ground_water.all_springs.public
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: true
    source_row: 76
  - country_entry_id: SEN-WAS-04
    source_category_code: private_well
    national_label_en: Private Well
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 55
  - country_entry_id: SEN-WAS-05
    source_category_code: public_well
    national_label_en: Public Well
    national_label_local: Public
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 56
  - country_entry_id: SEN-WAS-06
    source_category_code: eau_de_source_protegee
    national_label_en: "Eau de source prot\xE9g\xE9e"
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: SEN-WAS-07
    source_category_code: protected_spring
    national_label_en: protected spring
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: SEN-WAS-08
    source_category_code: source_d_eau_protegee
    national_label_en: "Source d\u2019eau prot\xE9g\xE9e"
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: SEN-WAS-09
    source_category_code: source_protegee
    national_label_en: Source protegee
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: SEN-WAS-10
    source_category_code: protected_well
    national_label_en: protected well
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: SEN-WAS-11
    source_category_code: puits_creuse_protege
    national_label_en: "Puits creus\xE9 prot\xE9g\xE9"
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: SEN-WAS-12
    source_category_code: puits_protege
    national_label_en: "Puits prot\xE9g\xE9"
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: SEN-WAS-13
    source_category_code: puits_interieur
    national_label_en: "puits int\xE9rieur"
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-WAS-14
    source_category_code: puits_protege_dans_le_logement_cour
    national_label_en: "Puits prot\xE9g\xE9 dans le logement/cour"
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SEN-WAS-15
    source_category_code: puits_exterieur
    national_label_en: "puits ext\xE9rieur"
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 68
  - country_entry_id: SEN-WAS-16
    source_category_code: puits_public_protege
    national_label_en: "Puits public prot\xE9g\xE9"
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 68
  - country_entry_id: SEN-WAS-17
    source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: "Puits ou sources prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: true
    shared_flag: false
    source_row: 46
  - country_entry_id: SEN-WAS-18
    source_category_code: covered_well_into_dwelling
    national_label_en: Covered well into dwelling
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 63
  - country_entry_id: SEN-WAS-19
    source_category_code: puits_dans_le_logement
    national_label_en: Puits dans le logement
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 63
  - country_entry_id: SEN-WAS-20
    source_category_code: puits_interieur
    national_label_en: puits interieur
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 63
  - country_entry_id: SEN-WAS-21
    source_category_code: well_in_yard
    national_label_en: Well in Yard
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 63
  - country_entry_id: SEN-WAS-22
    source_category_code: covered_well_into_yard_plot
    national_label_en: Covered well into yard/plot
    national_label_local: Public
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 64
  - country_entry_id: SEN-WAS-23
    source_category_code: public_well
    national_label_en: Public Well
    national_label_local: Public
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 64
  - country_entry_id: SEN-WAS-24
    source_category_code: puits_ext_forage_pompe
    national_label_en: puits ext.forage-pompe
    national_label_local: Public
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 64
  - country_entry_id: SEN-WAS-25
    source_category_code: puits_public
    national_label_en: Puits public
    national_label_local: Public
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 64
  - country_entry_id: SEN-WAS-26
    source_category_code: borehole
    national_label_en: Borehole
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: SEN-WAS-27
    source_category_code: forage
    national_label_en: Forage
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: SEN-WAS-28
    source_category_code: forage_ou_puits_a_pompe
    national_label_en: "Forage ou Puits \xE0 pompe"
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: SEN-WAS-29
    source_category_code: protected_tube_well_or_bore_hole
    national_label_en: Protected tube well or bore hole
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: SEN-WAS-30
    source_category_code: public_pump
    national_label_en: Public Pump
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: SEN-WAS-31
    source_category_code: puits_a_pompe_forage
    national_label_en: "Puits \xE0 pompe/ forage"
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: SEN-WAS-32
    source_category_code: puits_tubulaire_ou_forage
    national_label_en: Puits tubulaire ou forage
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: SEN-WAS-33
    source_category_code: tube_well_or_borehole
    national_label_en: tube well or borehole
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: SEN-WAS-34
    source_category_code: forage_motorise
    national_label_en: Forage motorise
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Tubewell, borehole > Private
    jmp_id: ground_water.tubewell_borehole.private
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 59
  - country_entry_id: SEN-WAS-35
    source_category_code: forage_a_pompe_manuel
    national_label_en: Forage a pompe manuel
    national_label_local: Public
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 60
  - country_entry_id: SEN-WAS-36
    source_category_code: eau_de_source_non_protegee
    national_label_en: "Eau de source non prot\xE9g\xE9e"
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: SEN-WAS-37
    source_category_code: source_d_eau_non_protegee
    national_label_en: "Source d\u2019eau non prot\xE9g\xE9e"
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: SEN-WAS-38
    source_category_code: source_non_protegee
    national_label_en: Source non protegee
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: SEN-WAS-39
    source_category_code: unprotected_spring
    national_label_en: unprotected spring
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: SEN-WAS-40
    source_category_code: puits_creuse_non_protege
    national_label_en: "Puits creus\xE9 non prot\xE9g\xE9"
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: SEN-WAS-41
    source_category_code: puits_non_protege
    national_label_en: "Puits non prot\xE9g\xE9"
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: SEN-WAS-42
    source_category_code: unprotected_well
    national_label_en: unprotected well
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: SEN-WAS-43
    source_category_code: puits_interieur
    national_label_en: "puits int\xE9rieur"
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: SEN-WAS-44
    source_category_code: puits_ouvert_dans_le_logement_cour
    national_label_en: Puits ouvert dans le logement/cour
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: SEN-WAS-45
    source_category_code: puits_exterieur
    national_label_en: "puits ext\xE9rieur"
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 72
  - country_entry_id: SEN-WAS-46
    source_category_code: puits_public_ouvert
    national_label_en: Puits public ouvert
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 72
  - country_entry_id: SEN-WAS-47
    source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: "Puits ou sources non prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 50
  - country_entry_id: SEN-WAS-48
    source_category_code: achetee_d_un_chariot_avec_un_petit_reservoir_ou_tambour
    national_label_en: "Achet\xE9e d\u2019un chariot avec un petit r\xE9servoir ou\
      \ tambour"
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: SEN-WAS-49
    source_category_code: cart_with_small_tank
    national_label_en: cart with small tank
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: SEN-WAS-50
    source_category_code: charrette_avec_petite_citerne
    national_label_en: Charrette avec petite citerne
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: SEN-WAS-51
    source_category_code: vendeur_d_eau
    national_label_en: Vendeur d'eau
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: SEN-WAS-52
    source_category_code: vendeur_d_eau_citerne
    national_label_en: vendeur d'eau/citerne
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: SEN-WAS-53
    source_category_code: achetee_d_une_citerne
    national_label_en: "Achet\xE9e d\u2019une citerne"
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-54
    source_category_code: camion_citerne
    national_label_en: Camion citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-55
    source_category_code: camion_citerne_vandeur_d_eau
    national_label_en: Camion citerne, vandeur d'eau
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-56
    source_category_code: camion_citerne_charrette_avec_petite_citerne
    national_label_en: Camion citerne/charrette avec petite citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-57
    source_category_code: camion_citerne
    national_label_en: Camion-citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-58
    source_category_code: camion_citerne_charrette_avec_petite_citerne
    national_label_en: 'Camion-citerne/charrette avec petite

      citerne'
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-59
    source_category_code: service_de_camion_citerne
    national_label_en: Service de camion citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-60
    source_category_code: service_de_camion_citerne
    national_label_en: service de camion-citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-61
    source_category_code: tanker
    national_label_en: Tanker
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-62
    source_category_code: tanker_truck
    national_label_en: tanker truck
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-63
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker-truck, vendor
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-64
    source_category_code: vendeur_d_eau_camion_citerne
    national_label_en: Vendeur d'eau/camion citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SEN-WAS-65
    source_category_code: autre
    national_label_en: autre
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-WAS-66
    source_category_code: autres
    national_label_en: autres
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-WAS-67
    source_category_code: other
    national_label_en: Other
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-WAS-68
    source_category_code: private_other
    national_label_en: Private Other
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-WAS-69
    source_category_code: vendeur_d_eau
    national_label_en: Vendeur d'eau
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: SEN-WAS-70
    source_category_code: a_refuse
    national_label_en: A refuse
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-WAS-71
    source_category_code: public_other
    national_label_en: Public Other
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: SEN-WAS-72
    source_category_code: eau_minerale_filtree
    national_label_en: Eau minerale/filtree
    national_label_local: "Eau conditionn\xE9e"
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 89
  - country_entry_id: SEN-WAS-73
    source_category_code: bottled_water
    national_label_en: bottled water
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: SEN-WAS-74
    source_category_code: eau_en_bouteille
    national_label_en: Eau en bouteille
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: SEN-WAS-75
    source_category_code: bottled_water
    national_label_en: Bottled Water
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: SEN-WAS-76
    source_category_code: eau_de_bouteille
    national_label_en: Eau de bouteille
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: SEN-WAS-77
    source_category_code: eau_en_bouteille
    national_label_en: Eau en bouteille
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: SEN-WAS-78
    source_category_code: water_bag
    national_label_en: water bag
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: SEN-WAS-79
    source_category_code: collecte_d_eau_de_pluie
    national_label_en: "Collecte d\u2019eau de pluie"
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: SEN-WAS-80
    source_category_code: eau_de_pluie
    national_label_en: Eau de pluie
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: SEN-WAS-81
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: SEN-WAS-82
    source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: SEN-WAS-83
    source_category_code: eau_de_surface
    national_label_en: Eau de surface
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-84
    source_category_code: eau_de_surface_telle_que_riviere_barrage_lac_etang_ruisseau_canal_ou_canaux_d_irrigation
    national_label_en: "Eau de surface, telle que rivi\xE8re, barrage, lac, \xE9tang,\
      \ ruisseau, canal ou canaux d\u2019irrigation"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-85
    source_category_code: mare_ruisseau_ou_fleuve
    national_label_en: mare ruisseau ou fleuve
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-86
    source_category_code: river_dam_lake_ponds_stream_canal_irirgation_channel
    national_label_en: river/dam/lake/ponds/stream/canal/irirgation channel
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-87
    source_category_code: river_dam_lake_ponds_stream_canal_irrigation_channel
    national_label_en: River/dam/lake/ponds/stream/canal/irrigation channel
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-88
    source_category_code: riviere_ou_marigot
    national_label_en: "rivi\xE8re ou marigot"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-89
    source_category_code: source_ou_cours_d_eau
    national_label_en: source ou cours d'eau
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-90
    source_category_code: source_cour_d_eau
    national_label_en: Source/cour d'eau
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-91
    source_category_code: source_cours_d_eau
    national_label_en: Source/cours d'eau
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-92
    source_category_code: water_taken_directly_from_pond_water_or_stream
    national_label_en: Water taken directly from pond-water or stream
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SEN-WAS-93
    source_category_code: dam
    national_label_en: Dam
    national_label_local: Endiguer
    jmp_classification: Surface water > Dam
    jmp_id: surface_water.dam
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 95
  - country_entry_id: SEN-WAS-94
    source_category_code: lake
    national_label_en: Lake
    national_label_local: Lac
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 94
  - country_entry_id: SEN-WAS-95
    source_category_code: mare_lac
    national_label_en: Mare, lac
    national_label_local: "\xC9tang"
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 96
  - country_entry_id: SEN-WAS-96
    source_category_code: mare_marigot
    national_label_en: Mare/Marigot
    national_label_local: "\xC9tang"
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 96
  - country_entry_id: SEN-WAS-97
    source_category_code: pond_lake
    national_label_en: Pond/Lake
    national_label_local: "\xC9tang"
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 96
  - country_entry_id: SEN-WAS-98
    source_category_code: river
    national_label_en: River
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: SEN-WAS-99
    source_category_code: river_stream
    national_label_en: River/Stream
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: SEN-WAS-100
    source_category_code: riviere_fleuve
    national_label_en: "Rivi\xE8re, fleuve"
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: SEN-WAS-101
    source_category_code: riviere_ruisseau_fleuve
    national_label_en: Riviere/Ruisseau/fleuve
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: SEN-WAS-102
    source_category_code: autre_concession
    national_label_en: autre concession
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: SEN-WAS-103
    source_category_code: piped_to_neighbor
    national_label_en: piped to neighbor
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: SEN-WAS-104
    source_category_code: robinet_du_voisin
    national_label_en: Robinet du voisin
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: SEN-WAS-105
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: SEN-WAS-106
    source_category_code: private_running_water
    national_label_en: Private Running Water
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: SEN-WAS-107
    source_category_code: robinet_dans_logement_concession
    national_label_en: Robinet dans logement/concession
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: SEN-WAS-108
    source_category_code: robinet_interieur
    national_label_en: "Robinet int\xE9rieur"
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: SEN-WAS-109
    source_category_code: eau_du_robinet_dans_le_logement
    national_label_en: Eau du robinet dans le logement
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: SEN-WAS-110
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: SEN-WAS-111
    source_category_code: robinet_dans_la_maison
    national_label_en: Robinet dans la maison
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: SEN-WAS-112
    source_category_code: robinet_dans_le_logement
    national_label_en: Robinet dans le logement
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: SEN-WAS-113
    source_category_code: robinet_dans_logement
    national_label_en: Robinet dans logement
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: SEN-WAS-114
    source_category_code: robinet_interieur
    national_label_en: "robinet int\xE9rieur"
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: SEN-WAS-115
    source_category_code: tap_in_household
    national_label_en: Tap in Household
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: SEN-WAS-116
    source_category_code: eau_du_robinet_dans_la_cour_concession
    national_label_en: Eau du robinet dans la cour/concession
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: SEN-WAS-117
    source_category_code: piped_into_yard
    national_label_en: Piped into yard
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: SEN-WAS-118
    source_category_code: piped_to_yard_plot
    national_label_en: piped to yard/plot
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: SEN-WAS-119
    source_category_code: robinet_dans_la_concession
    national_label_en: Robinet dans la concession
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: SEN-WAS-120
    source_category_code: robinet_dans_la_cour_dans_la_parcelle_ou_dans_la_concession
    national_label_en: Robinet dans la cour, dans la parcelle, ou dans la concession
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: SEN-WAS-121
    source_category_code: robinet_dans_la_cour_parcelle
    national_label_en: Robinet dans la cour/parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: SEN-WAS-122
    source_category_code: robinet_exterieur
    national_label_en: "robinet ext\xE9rieur"
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: SEN-WAS-123
    source_category_code: borne_fontaine
    national_label_en: Borne Fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: SEN-WAS-124
    source_category_code: fontaine_publique
    national_label_en: Fontaine publique
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: SEN-WAS-125
    source_category_code: public_standpipe
    national_label_en: Public standpipe
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: SEN-WAS-126
    source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: SEN-WAS-127
    source_category_code: public_tap_standpipe
    national_label_en: public tap/standpipe
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: SEN-WAS-128
    source_category_code: public_fontaine
    national_label_en: Public/fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: SEN-WAS-129
    source_category_code: robinet_ou_fontaine_publique
    national_label_en: Robinet ou fontaine publique
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: SEN-WAS-130
    source_category_code: robinet_public
    national_label_en: robinet public
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: SEN-WAS-131
    source_category_code: robinet_public_fontaine
    national_label_en: Robinet public/fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: SEN-WAS-132
    source_category_code: standpipe
    national_label_en: Standpipe
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_SEN_Senegal_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1999
  effective_to: null
  selectors: null
  value: 15
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

