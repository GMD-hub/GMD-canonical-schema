---
country_id: CTY-COG
iso3: COG
schema_version: '0.2'
status: draft
country_name: COG
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: COG-EDU-01
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
  - country_entry_id: COG-EDU-02
    national_label_en: Enseignement primaire
    national_label_local: Enseignement primaire
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
    - COG-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: COG-EDU-03
    national_label_en: "Enseignement secondaire g\xE9n\xE9ral 1 e cycle"
    national_label_local: "Enseignement secondaire g\xE9n\xE9ral 1 e cycle"
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - COG-EDU-02
    cum_years_schooling: 10
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: COG-EDU-04
    national_label_en: "Centre de m\xE9tiers"
    national_label_local: "Centre de m\xE9tiers"
    entry_age: 12
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - COG-EDU-02
    cum_years_schooling: 8
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: COG-EDU-05
    national_label_en: Enseignement secondaire technique 1 e cycle
    national_label_local: Enseignement secondaire technique 1 e cycle
    entry_age: 14
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - COG-EDU-02
    cum_years_schooling: 8
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: COG-EDU-06
    national_label_en: "Enseignement secondaire g\xE9n\xE9ral 2 e cycle"
    national_label_local: "Enseignement secondaire g\xE9n\xE9ral 2 e cycle"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - COG-EDU-03
    - COG-EDU-04
    - COG-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
  - country_entry_id: COG-EDU-07
    national_label_en: Enseignement secondaire professionnelle (BEP)
    national_label_local: Enseignement secondaire professionnelle (BEP)
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - COG-EDU-03
    - COG-EDU-04
    - COG-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
  - country_entry_id: COG-EDU-08
    national_label_en: Enseignement secondaire professionnelle (CAP)
    national_label_local: Enseignement secondaire professionnelle (CAP)
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - COG-EDU-03
    - COG-EDU-04
    - COG-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
  - country_entry_id: COG-EDU-09
    national_label_en: Enseignement secondaire technique 2 e cycle
    national_label_local: Enseignement secondaire technique 2 e cycle
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - COG-EDU-03
    - COG-EDU-04
    - COG-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
  - country_entry_id: COG-EDU-10
    national_label_en: "Enseignement sup\xE9rieur (cycle court)"
    national_label_local: "Enseignement sup\xE9rieur (cycle court)"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - COG-EDU-06
    - COG-EDU-07
    - COG-EDU-08
    - COG-EDU-09
    cum_years_schooling: 12
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-07
    - COG-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
    - 'minimum parent path selected from: COG-EDU-06, COG-EDU-07, COG-EDU-08, COG-EDU-09'
  - country_entry_id: COG-EDU-11
    national_label_en: "Enseignement sup\xE9rieur (cycle moyen sup\xE9rieur, licence)"
    national_label_local: "Enseignement sup\xE9rieur (cycle moyen sup\xE9rieur, licence)"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - COG-EDU-06
    - COG-EDU-07
    - COG-EDU-08
    - COG-EDU-09
    cum_years_schooling: 13
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-07
    - COG-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
    - 'minimum parent path selected from: COG-EDU-06, COG-EDU-07, COG-EDU-08, COG-EDU-09'
  - country_entry_id: COG-EDU-12
    national_label_en: "Enseignement sup\xE9rieur (cycle moyen sup\xE9rieur, licence\
      \ professionnelle)"
    national_label_local: "Enseignement sup\xE9rieur (cycle moyen sup\xE9rieur, licence\
      \ professionnelle)"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - COG-EDU-06
    - COG-EDU-07
    - COG-EDU-08
    - COG-EDU-09
    cum_years_schooling: 13
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-07
    - COG-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
    - 'minimum parent path selected from: COG-EDU-06, COG-EDU-07, COG-EDU-08, COG-EDU-09'
  - country_entry_id: COG-EDU-13
    national_label_en: "Etudes de m\xE9decine"
    national_label_local: "Etudes de m\xE9decine"
    entry_age: 19
    duration_years: 7
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - COG-EDU-06
    - COG-EDU-07
    - COG-EDU-08
    - COG-EDU-09
    cum_years_schooling: 17
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-07
    - COG-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
    - 'minimum parent path selected from: COG-EDU-06, COG-EDU-07, COG-EDU-08, COG-EDU-09'
  - country_entry_id: COG-EDU-14
    national_label_en: "Enseignement sup\xE9rieur (cycle  sup\xE9rieur, master)"
    national_label_local: "Enseignement sup\xE9rieur (cycle  sup\xE9rieur, master)"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - COG-EDU-11
    - COG-EDU-12
    cum_years_schooling: 15
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-07
    - COG-EDU-11
    - COG-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
    - 'minimum parent path selected from: COG-EDU-06, COG-EDU-07, COG-EDU-08, COG-EDU-09'
    - 'minimum parent path selected from: COG-EDU-11, COG-EDU-12'
  - country_entry_id: COG-EDU-15
    national_label_en: "Enseignement sup\xE9rieur (Cycle doctorat)"
    national_label_local: "Enseignement sup\xE9rieur (Cycle doctorat)"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - COG-EDU-13
    - COG-EDU-14
    cum_years_schooling: 18
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-07
    - COG-EDU-11
    - COG-EDU-14
    - COG-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
    - 'minimum parent path selected from: COG-EDU-06, COG-EDU-07, COG-EDU-08, COG-EDU-09'
    - 'minimum parent path selected from: COG-EDU-11, COG-EDU-12'
    - 'minimum parent path selected from: COG-EDU-13, COG-EDU-14'
  - country_entry_id: COG-EDU-16
    national_label_en: "Certificat d'etudes sp\xE9ciales"
    national_label_local: "Certificat d'etudes sp\xE9ciales"
    entry_age: 26
    duration_years: 5
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - COG-EDU-13
    - COG-EDU-14
    cum_years_schooling: 20
    cum_years_computation_path:
    - COG-EDU-02
    - COG-EDU-04
    - COG-EDU-07
    - COG-EDU-11
    - COG-EDU-14
    - COG-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COG-EDU-03, COG-EDU-04, COG-EDU-05'
    - 'minimum parent path selected from: COG-EDU-06, COG-EDU-07, COG-EDU-08, COG-EDU-09'
    - 'minimum parent path selected from: COG-EDU-11, COG-EDU-12'
    - 'minimum parent path selected from: COG-EDU-13, COG-EDU-14'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Congo.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: COG-SUBNAT-01
    survey_labels: 1 - Brazzaville | 11 - Brazzaville
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_190432
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_190432
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '190432'
    geo_nvar: ADM1_NAME
    geo_name: Brazzaville
    source_row: 2522
  - country_entry_id: COG-SUBNAT-02
    survey_labels: 12 - Pointe-Noire | 2 - Pointe Noire
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_190434
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_190434
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '190434'
    geo_nvar: ADM1_NAME
    geo_name: Point-Noire
    source_row: 2523
  - country_entry_id: COG-SUBNAT-03
    survey_labels: 1 - Kouilou
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_190433
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_190433
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '190433'
    geo_nvar: ADM1_NAME
    geo_name: Kouilou
    source_row: 2527
  - country_entry_id: COG-SUBNAT-04
    survey_labels: 10 - Likouala
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_975
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_975
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '975'
    geo_nvar: ADM1_NAME
    geo_name: Likouala
    source_row: 2528
  - country_entry_id: COG-SUBNAT-05
    survey_labels: 2 - Niari
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_976
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_976
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '976'
    geo_nvar: ADM1_NAME
    geo_name: Niari
    source_row: 2531
  - country_entry_id: COG-SUBNAT-06
    survey_labels: "3 - L\xE9koumou"
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_974
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_974
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '974'
    geo_nvar: ADM1_NAME
    geo_name: Lekoumou
    source_row: 2532
  - country_entry_id: COG-SUBNAT-07
    survey_labels: 4 - Bouenza
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_970
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_970
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '970'
    geo_nvar: ADM1_NAME
    geo_name: Bouenza
    source_row: 2533
  - country_entry_id: COG-SUBNAT-08
    survey_labels: 5 - Pool
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_190431
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_190431
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '190431'
    geo_nvar: ADM1_NAME
    geo_name: Pool
    source_row: 2534
  - country_entry_id: COG-SUBNAT-09
    survey_labels: 6 - Plateaux
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_977
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_977
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '977'
    geo_nvar: ADM1_NAME
    geo_name: Plateaux
    source_row: 2535
  - country_entry_id: COG-SUBNAT-10
    survey_labels: 7 - Cuvette
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_971
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_971
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '971'
    geo_nvar: ADM1_NAME
    geo_name: Cuvette
    source_row: 2536
  - country_entry_id: COG-SUBNAT-11
    survey_labels: 8 - Cuvette-Ouest
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_972
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_972
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '972'
    geo_nvar: ADM1_NAME
    geo_name: Cuvette-Ouest
    source_row: 2537
  - country_entry_id: COG-SUBNAT-12
    survey_labels: 9 - Sangha
    survey_variables: subnatid
    gmd_subnatid1: COG_2015_GAUL1_979
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COG_2015_GAUL1_979
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '979'
    geo_nvar: ADM1_NAME
    geo_name: Sangha
    source_row: 2538
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
  - country_entry_id: COG-SUBNAT-01
    survey_labels: 3 - Autres communes | 4 - Semi urbain | 5 - Milieu rural
    survey_variables: subnatid
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: ''
    geo_source: ''
    geo_level: ''
    geo_idvar: ''
    geo_id: ''
    geo_nvar: ''
    geo_name: ''
    source_row: 2524
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
  - country_entry_id: COG-SAN-01
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
  - country_entry_id: COG-SAN-02
    source_category_code: wc_avec_chasse_d_eau
    national_label_en: WC avec chasse d'eau
    national_label_local: "Toilette \xE0 chasse d'eau"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: COG-SAN-03
    source_category_code: chasse_d_eau_pour_le_menage_seul
    national_label_en: "Chasse d'eau pour le m\xE9nage seul"
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: COG-SAN-04
    source_category_code: chasse_d_eau_pour_le_menage_seul
    national_label_en: "Chasse d'eau pour le m\xE9nage seul"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: COG-SAN-05
    source_category_code: chasse_d_eau_chasse_manuelle_connectee_a_un_systeme_d_egout
    national_label_en: "Chasse d'eau/chasse manuelle connect\xE9e \xE0 un syst\xE8\
      me d'\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: COG-SAN-06
    source_category_code: private_domestic_connection_to_sewage_system
    national_label_en: Private domestic connection to sewage system (*)
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: COG-SAN-07
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_d_aisances
    national_label_en: "Chasse d'eau/chasse manuelle reli\xE9e \xE0 une fosse d'aisances"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > Private flush/toilet > to pit
    jmp_id: flush_toilets.private_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 75
  - country_entry_id: COG-SAN-08
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_septique
    national_label_en: "Chasse d'eau/chasse manuelle reli\xE9e \xE0 une fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: COG-SAN-09
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
  - country_entry_id: COG-SAN-10
    source_category_code: chasse_d_eau_en_commun
    national_label_en: Chasse d'eau en commun
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: COG-SAN-11
    source_category_code: chasse_d_eau_en_commun
    national_label_en: Chasse d'eau en commun
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: COG-SAN-12
    source_category_code: chasse_d_eau_chasse_manuelle_connectee_a_un_systeme_d_egout
    national_label_en: "Chasse d'eau/chasse manuelle connect\xE9e \xE0 un syst\xE8\
      me d'\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: COG-SAN-13
    source_category_code: shared_domestic_connection_to_sewage_system
    national_label_en: Shared domestic connection to sewage system (*)
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: COG-SAN-14
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_d_aisances
    national_label_en: "Chasse d'eau/chasse manuelle reli\xE9e \xE0 une fosse d'aisances"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to pit
    jmp_id: flush_toilets.public_shared_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 81
  - country_entry_id: COG-SAN-15
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_septique
    national_label_en: "Chasse d'eau/chasse manuelle reli\xE9e \xE0 une fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 80
  - country_entry_id: COG-SAN-16
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
  - country_entry_id: COG-SAN-17
    source_category_code: reliee_a_autre_chose
    national_label_en: "Reliee a\_autre chose"
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: COG-SAN-18
    source_category_code: reliee_a_des_latrines
    national_label_en: "Reliee a\_ des latrines"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: COG-SAN-19
    source_category_code: connectee_a_fosse_septique
    national_label_en: "Connectee a\_ fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: COG-SAN-20
    source_category_code: reliee_a_endroit_inconnu_nsp_ou
    national_label_en: "Reliee a\_ endroit inconnu/ NSP ou"
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: COG-SAN-21
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
  - country_entry_id: COG-SAN-22
    source_category_code: seau
    national_label_en: Seau
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: COG-SAN-23
    source_category_code: seaux
    national_label_en: Seaux
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: COG-SAN-24
    source_category_code: latrines_suspendues_sur_pilotis
    national_label_en: Latrines suspendues/sur pilotis
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: COG-SAN-25
    source_category_code: toilettes_latrines_suspendues
    national_label_en: Toilettes / latrines suspendues
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: COG-SAN-26
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
  - country_entry_id: COG-SAN-27
    source_category_code: latrines_a_fosses_avec_dalle
    national_label_en: Latrines a fosses avec dalle
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: COG-SAN-28
    source_category_code: fosse_d_aisances_sans_dalle_trou_ouvert
    national_label_en: Fosse d'aisances sans dalle/trou ouvert
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: COG-SAN-29
    source_category_code: latrines_a_fosses_sans_dalle_trou_ouvert
    national_label_en: Latrines a fosses sans dalle/trou ouvert
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: COG-SAN-30
    source_category_code: latrines_non_couvertes
    national_label_en: Latrines non couvertes
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: COG-SAN-31
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
  - country_entry_id: COG-SAN-32
    source_category_code: latrines_couvertes
    national_label_en: Latrines couvertes
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: COG-SAN-33
    source_category_code: latrines_ameliorees_ventilees_lav
    national_label_en: Latrines ameliorees ventilees (LAV)
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: COG-SAN-34
    source_category_code: latrines_ventillees_ameliorees
    national_label_en: "Latrines ventill\xE9es am\xE9lior\xE9es"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: COG-SAN-35
    source_category_code: fosse_latrines_ameliorees_privees
    national_label_en: "Fosse/latrines am\xE9lior\xE9es priv\xE9es"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: COG-SAN-36
    source_category_code: fosses_d_aisances_avec_dalle
    national_label_en: Fosses d'aisances avec dalle
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: COG-SAN-37
    source_category_code: fosse_latrine_rudimentaire_privee
    national_label_en: "Fosse/latrine rudimentaire priv\xE9e"
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine without
      slab/open pit
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 116
  - country_entry_id: COG-SAN-38
    source_category_code: fosse_latrine_ameioree_privee
    national_label_en: "Fosse/latrine am\xE9ior\xE9e priv\xE9e"
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 115
  - country_entry_id: COG-SAN-39
    source_category_code: fosse_latrines_rudimentaires_privees
    national_label_en: "Fosse/latrines rudimentaires priv\xE9es"
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 115
  - country_entry_id: COG-SAN-40
    source_category_code: private_covered_dry_latrine_with_privacy
    national_label_en: Private covered dry latrine (with privacy)
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 115
  - country_entry_id: COG-SAN-41
    source_category_code: fosse_d_aisances_amelioree_auto_aeree
    national_label_en: "Fosse d'aisances am\xE9lior\xE9e auto-a\xE9r\xE9e"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 113
  - country_entry_id: COG-SAN-42
    source_category_code: fosse_latrines_ameliorees_en_commun
    national_label_en: "Fosse/latrines am\xE9lior\xE9es en commun"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: COG-SAN-43
    source_category_code: fosses_d_aisances_avec_dalle
    national_label_en: Fosses d'aisances avec dalle
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: COG-SAN-44
    source_category_code: fosse_latrine_rudimentaire_en_commun
    national_label_en: Fosse/latrine rudimentaire en commun
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 124
  - country_entry_id: COG-SAN-45
    source_category_code: fosse_latrine_amelioree_en_commun
    national_label_en: "Fosse/latrine am\xE9lior\xE9e en commun"
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: true
    source_row: 123
  - country_entry_id: COG-SAN-46
    source_category_code: fosse_latrines_rudimentaires_en_commun
    national_label_en: Fosse/latrines rudimentaires en commun
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: true
    source_row: 123
  - country_entry_id: COG-SAN-47
    source_category_code: shared_covered_dry_latrine_with_privacy
    national_label_en: Shared covered dry latrine (with privacy)
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: true
    source_row: 123
  - country_entry_id: COG-SAN-48
    source_category_code: fosse_d_aisances_amelioree_auto_aeree
    national_label_en: "Fosse d'aisances am\xE9lior\xE9e auto-a\xE9r\xE9e"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Ventilated
      Improved Pit latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 121
  - country_entry_id: COG-SAN-49
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
  - country_entry_id: COG-SAN-50
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
  - country_entry_id: COG-SAN-51
    source_category_code: aucun_dans_la_nature
    national_label_en: Aucun/dans la nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: COG-SAN-52
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
  - country_entry_id: COG-SAN-53
    source_category_code: pa_de_toilette_nature
    national_label_en: Pa de toilette/nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: COG-SAN-54
    source_category_code: pas_de_toilettes_nature
    national_label_en: Pas de toilettes, nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: COG-SAN-55
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
  - country_entry_id: COG-SAN-56
    source_category_code: autre
    national_label_en: Autre
    national_label_local: "Autre non amelior\xE9e"
    jmp_classification: Other unimproved
    jmp_id: other_unimproved
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 135
  - country_entry_id: COG-SAN-57
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
  - country_entry_id: COG-SAN-58
    source_category_code: autre_a_preciser
    national_label_en: "Autre(\xE0 pr\xE9ciser)"
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: COG-SAN-59
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
  - country_entry_id: COG-SAN-60
    source_category_code: autre
    national_label_en: Autre
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_COG_Congo_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: COG-WAS-01
    source_category_code: source_d_eau_protegee
    national_label_en: "Source d'eau prot\xE9g\xE9e"
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: COG-WAS-02
    source_category_code: source_protege
    national_label_en: "Source prot\xE9g\xE9"
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: COG-WAS-03
    source_category_code: source_protegee
    national_label_en: "Source prot\xE9g\xE9e"
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: COG-WAS-04
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
  - country_entry_id: COG-WAS-05
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
  - country_entry_id: COG-WAS-06
    source_category_code: puits_protege_dans_la_parcelle
    national_label_en: "Puits prot\xE9g\xE9 dans la parcelle"
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: COG-WAS-07
    source_category_code: puits_protege_dans_parcelle
    national_label_en: "Puits prot\xE9g\xE9 dans parcelle"
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: COG-WAS-08
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
  - country_entry_id: COG-WAS-09
    source_category_code: pompe_villageoise_forage_a_pompe_manuelle
    national_label_en: "Pompe villageoise/Forage \xE1 pompe manuelle"
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: COG-WAS-10
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
  - country_entry_id: COG-WAS-11
    source_category_code: puits_a_pompe_forage
    national_label_en: "Puits \xE0 pompe / forage"
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: COG-WAS-12
    source_category_code: forage_puits_a_pompe_public
    national_label_en: "Forage, puits \xE0 pompe public"
    national_label_local: Public
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 60
  - country_entry_id: COG-WAS-13
    source_category_code: forage_puits_a_pompe_public
    national_label_en: "Forage/puits \xE0 pompe public"
    national_label_local: Public
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 60
  - country_entry_id: COG-WAS-14
    source_category_code: source_d_eau_non_protegee
    national_label_en: "Source d'eau non-prot\xE9g\xE9e"
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: COG-WAS-15
    source_category_code: source_non_protege
    national_label_en: "Source non prot\xE9g\xE9"
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: COG-WAS-16
    source_category_code: source_non_protegee
    national_label_en: "Source non prot\xE9g\xE9e"
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: COG-WAS-17
    source_category_code: puits_creuse_non_protege
    national_label_en: "Puits creus\xE9 non-prot\xE9g\xE9"
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: COG-WAS-18
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
  - country_entry_id: COG-WAS-19
    source_category_code: puits_non_protege_dans_la_parcelle
    national_label_en: "Puits non prot\xE9g\xE9 dans la parcelle"
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: COG-WAS-20
    source_category_code: puits_non_protege_dans_parcelle
    national_label_en: "Puits non prot\xE9g\xE9 dans parcelle"
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: COG-WAS-21
    source_category_code: puits_non_protege_public
    national_label_en: "Puits non prot\xE9g\xE9 public"
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 72
  - country_entry_id: COG-WAS-22
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
  - country_entry_id: COG-WAS-23
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
  - country_entry_id: COG-WAS-24
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
  - country_entry_id: COG-WAS-25
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
  - country_entry_id: COG-WAS-26
    source_category_code: autre
    national_label_en: Autre
    national_label_local: "Autres non am\xE9lior\xE9es"
    jmp_classification: Other non-improved
    jmp_id: other_non_improved
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 105
  - country_entry_id: COG-WAS-27
    source_category_code: autre
    national_label_en: Autre
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: COG-WAS-28
    source_category_code: autre_a_preciser
    national_label_en: "Autre(\xE0 pr\xE9ciser)"
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: COG-WAS-29
    source_category_code: autre
    national_label_en: Autre
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: COG-WAS-30
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
  - country_entry_id: COG-WAS-31
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
  - country_entry_id: COG-WAS-32
    source_category_code: bache_a_eau_citerne
    national_label_en: "Bache \xE1 eau/citerne"
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: COG-WAS-33
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
  - country_entry_id: COG-WAS-34
    source_category_code: rainwater
    national_label_en: rainwater
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: COG-WAS-35
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
  - country_entry_id: COG-WAS-36
    source_category_code: pluie
    national_label_en: Pluie
    national_label_local: "Citerne/r\xE9servoir d\xE9couvert"
    jmp_classification: Rainwater > Uncovered cistern/tank
    jmp_id: rainwater.uncovered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 88
  - country_entry_id: COG-WAS-37
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
  - country_entry_id: COG-WAS-38
    source_category_code: eau_de_surface_rivia_re_fleuve_barrage_lac_mare_canal_canal_d_irrigation
    national_label_en: "Eau de surface (rivi\xC3\xA8re, fleuve, barrage, lac, mare,\
      \ canal, canal d?irrigation)"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: COG-WAS-39
    source_category_code: riviere_fleuve_marigot
    national_label_en: "Rivi\xE8re/fleuve/marigot"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: COG-WAS-40
    source_category_code: riviere_marigot_source
    national_label_en: "Rivi\xE8re/marigot/source"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: COG-WAS-41
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
  - country_entry_id: COG-WAS-42
    source_category_code: fontaine_robinet_public
    national_label_en: Fontaine/Robinet public
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: COG-WAS-43
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
  - country_entry_id: COG-WAS-44
    source_category_code: eau_courante_snde_a_la_maison
    national_label_en: "Eau courante SNDE \xE1 la maison"
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: COG-WAS-45
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
  - country_entry_id: COG-WAS-46
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
  - country_entry_id: COG-WAS-47
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
  - country_entry_id: COG-WAS-48
    source_category_code: robinet_dans_la_concession_cour_ou_parcelle
    national_label_en: Robinet dans la concession, cour ou parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COG-WAS-49
    source_category_code: robinet_dans_la_cour_concession
    national_label_en: Robinet dans la cour/concession
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COG-WAS-50
    source_category_code: robinet_dans_la_parcelle
    national_label_en: Robinet dans la parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COG-WAS-51
    source_category_code: robinet_dans_parcelle
    national_label_en: Robinet dans parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COG-WAS-52
    source_category_code: eau_courante_snde_ailleurs
    national_label_en: Eau courante SNDE ailleurs
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: COG-WAS-53
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
  - country_entry_id: COG-WAS-54
    source_category_code: robinet_exterieur
    national_label_en: "Robinet ext\xE9rieur"
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: COG-WAS-55
    source_category_code: robinet_public_borne_fontaine
    national_label_en: Robinet public / Borne fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: COG-WAS-56
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
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_COG_Congo_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

