---
country_id: CTY-MRT
iso3: MRT
schema_version: '0.2'
status: draft
country_name: MRT
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MRT-EDU-01
    national_label_en: "\xC9ducation de la petite enfance"
    national_label_local: "\xC9ducation de la petite enfance"
    entry_age: 0
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
  - country_entry_id: MRT-EDU-02
    national_label_en: "Pr\xE9-primaire"
    national_label_local: "Pr\xE9-primaire"
    entry_age: 3
    duration_years: 3
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
  - country_entry_id: MRT-EDU-03
    national_label_en: Primaire
    national_label_local: Primaire
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - MRT-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: MRT-EDU-04
    national_label_en: 1 e cycle de l'enseignement secondaire
    national_label_local: 1 e cycle de l'enseignement secondaire
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - MRT-EDU-03
    cum_years_schooling: 10
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MRT-EDU-05
    national_label_en: Brevet technicien
    national_label_local: Brevet technicien
    entry_age: 16
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - MRT-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MRT-EDU-06
    national_label_en: 2 e cycle de l'enseignement secondaire
    national_label_local: 2 e cycle de l'enseignement secondaire
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - MRT-EDU-04
    - MRT-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
  - country_entry_id: MRT-EDU-07
    national_label_en: 2 e cycle de l'enseignement secondaire professionnel
    national_label_local: 2 e cycle de l'enseignement secondaire professionnel
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - MRT-EDU-04
    - MRT-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
  - country_entry_id: MRT-EDU-08
    national_label_en: Formation d'enseignants au primaire
    national_label_local: Formation d'enseignants au primaire
    entry_age: 19
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - MRT-EDU-06
    - MRT-EDU-07
    cum_years_schooling: 13
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
  - country_entry_id: MRT-EDU-09
    national_label_en: "Brevet de technicien sup\xE9rieur (BTS)"
    national_label_local: "Brevet de technicien sup\xE9rieur (BTS)"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - MRT-EDU-06
    - MRT-EDU-07
    cum_years_schooling: 12
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
  - country_entry_id: MRT-EDU-10
    national_label_en: La formation des inspecteurs  adjoint de l'enseignement fondamental
    national_label_local: La formation des inspecteurs  adjoint de l'enseignement
      fondamental
    entry_age: 30
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - MRT-EDU-06
    - MRT-EDU-07
    cum_years_schooling: 12
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
  - country_entry_id: MRT-EDU-11
    national_label_en: Licence
    national_label_local: Licence
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - MRT-EDU-06
    - MRT-EDU-07
    cum_years_schooling: 13
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
  - country_entry_id: MRT-EDU-12
    national_label_en: "Bac en m\xE9decine"
    national_label_local: "Bac en m\xE9decine"
    entry_age: 19
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - MRT-EDU-06
    - MRT-EDU-07
    cum_years_schooling: 16
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
  - country_entry_id: MRT-EDU-13
    national_label_en: La formation des inspecteurs de l'enseignement fondamental
    national_label_local: La formation des inspecteurs de l'enseignement fondamental
    entry_age: 35
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - MRT-EDU-06
    - MRT-EDU-07
    cum_years_schooling: 12
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
  - country_entry_id: MRT-EDU-14
    national_label_en: Formation des enseignants au Secondaire
    national_label_local: Formation des enseignants au Secondaire
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - MRT-EDU-06
    - MRT-EDU-07
    cum_years_schooling: 12
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
  - country_entry_id: MRT-EDU-15
    national_label_en: Master
    national_label_local: Master
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - MRT-EDU-10
    - MRT-EDU-11
    cum_years_schooling: 14
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-10
    - MRT-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
    - 'minimum parent path selected from: MRT-EDU-10, MRT-EDU-11'
  - country_entry_id: MRT-EDU-16
    national_label_en: Formation pour l'obtention du titre de professorat des enseignants
      au Secondaire
    national_label_local: Formation pour l'obtention du titre de professorat des enseignants
      au Secondaire
    entry_age: 23
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - MRT-EDU-06
    - MRT-EDU-07
    cum_years_schooling: 11
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
  - country_entry_id: MRT-EDU-17
    national_label_en: Doctorat
    national_label_local: Doctorat
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - MRT-EDU-12
    - MRT-EDU-13
    - MRT-EDU-14
    - MRT-EDU-15
    - MRT-EDU-16
    cum_years_schooling: 14
    cum_years_computation_path:
    - MRT-EDU-03
    - MRT-EDU-05
    - MRT-EDU-07
    - MRT-EDU-16
    - MRT-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MRT-EDU-04, MRT-EDU-05'
    - 'minimum parent path selected from: MRT-EDU-06, MRT-EDU-07'
    - 'minimum parent path selected from: MRT-EDU-12, MRT-EDU-13, MRT-EDU-14, MRT-EDU-15,
      MRT-EDU-16'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Mauritanie.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MRT-SUBNAT-01
    survey_labels: "1 - Hodh El Charghi | 1 \u2013 Hodh El Charghi"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2010
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2010
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2010'
    geo_nvar: ADM1_NAME
    geo_name: Hodh Ech Chargi
    source_row: 10370
  - country_entry_id: MRT-SUBNAT-02
    survey_labels: "10 - Guidimagha | 10 \u2013 Guidimagha"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2009
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2009
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2009'
    geo_nvar: ADM1_NAME
    geo_name: Guidimakha
    source_row: 10371
  - country_entry_id: MRT-SUBNAT-03
    survey_labels: "11 - Tiris Zemmour | 11 \u2013 Tiris Zemmour"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2015
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2015
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2015'
    geo_nvar: ADM1_NAME
    geo_name: Tiris-Zemmour
    source_row: 10372
  - country_entry_id: MRT-SUBNAT-04
    survey_labels: "12 - Inchiri | 12 \u2013 Inchiri"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2012
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2012
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2012'
    geo_nvar: ADM1_NAME
    geo_name: Inchiri
    source_row: 10373
  - country_entry_id: MRT-SUBNAT-05
    survey_labels: "13 - Nouakchott | 13 \u2013 Nouakchott"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2013
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2013
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2013'
    geo_nvar: ADM1_NAME
    geo_name: Nouakchott
    source_row: 10374
  - country_entry_id: MRT-SUBNAT-06
    survey_labels: "2 - Hodh El Gharbi | 2 \u2013 Hodh El Gharbi"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2011
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2011
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2011'
    geo_nvar: ADM1_NAME
    geo_name: Hodh El Gharbi
    source_row: 10375
  - country_entry_id: MRT-SUBNAT-07
    survey_labels: "3 - Assaba | 3 \u2013 Assaba"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2005
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2005
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2005'
    geo_nvar: ADM1_NAME
    geo_name: Assaba
    source_row: 10376
  - country_entry_id: MRT-SUBNAT-08
    survey_labels: "4 - Gorgol | 4 \u2013 Gorgol"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2008
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2008
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2008'
    geo_nvar: ADM1_NAME
    geo_name: Gorgol
    source_row: 10377
  - country_entry_id: MRT-SUBNAT-09
    survey_labels: "5 - Brakna | 5 \u2013 Brakna"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2006
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2006
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2006'
    geo_nvar: ADM1_NAME
    geo_name: Brakna
    source_row: 10378
  - country_entry_id: MRT-SUBNAT-10
    survey_labels: "6 - Trarza | 6 \u2013 Trarza"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2016
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2016
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2016'
    geo_nvar: ADM1_NAME
    geo_name: Trarza
    source_row: 10379
  - country_entry_id: MRT-SUBNAT-11
    survey_labels: "7 - Adrar | 7 \u2013 Adrar"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2004
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2004
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2004'
    geo_nvar: ADM1_NAME
    geo_name: Adrar
    source_row: 10380
  - country_entry_id: MRT-SUBNAT-12
    survey_labels: "8 - Dakhlet Nouadhibou | 8 \u2013 Dakhlet Nouadhibou"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2007
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2007
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2007'
    geo_nvar: ADM1_NAME
    geo_name: Dakhlet-Nouadhibou
    source_row: 10381
  - country_entry_id: MRT-SUBNAT-13
    survey_labels: "9 - Tagant | 9 \u2013 Tagant"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: MRT_2015_GAUL1_2014
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MRT_2015_GAUL1_2014
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2014'
    geo_nvar: ADM1_NAME
    geo_name: Tagant
    source_row: 10382
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
  - country_entry_id: MRT-SAN-01
    source_category_code: composting_toilet
    national_label_en: composting toilet
    national_label_local: "\u0645\u0631\u0627\u062D\u064A\u0636 \u0627\u0644\u062A\
      \u0633\u0645\u064A\u062F"
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: MRT-SAN-02
    source_category_code: toilette_a_compostage
    national_label_en: TOILETTE A COMPOSTAGE
    national_label_local: "\u0645\u0631\u0627\u062D\u064A\u0636 \u0627\u0644\u062A\
      \u0633\u0645\u064A\u062F"
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: MRT-SAN-03
    source_category_code: chasse_d_eau_reliee_a_une_fosse_simple_non_couverte_reliee_a_l_air_libre
    national_label_en: "CHASSE D'EAU / Reli\xE9e \xE0 une fosse simple  non couverte\
      \ + Reli\xE9e \xE0 l'air libre"
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: MRT-SAN-04
    source_category_code: flush_to_somewhere_else
    national_label_en: flush to somewhere else
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: MRT-SAN-05
    source_category_code: chasse_d_eau_reliee_a_systeme_d_egouts
    national_label_en: "CHASSE D'EAU / Reli\xE9e \xE0 syst\xE8me d'\xE9gouts"
    national_label_local: "\u0625\u0644\u0649 \u0646\u0638\u0627\u0645 \u0627\u0644\
      \u0635\u0631\u0641 \u0627\u0644\u0635\u062D\u064A \u0628\u0627\u0644\u0623\u0646\
      \u0627\u0628\u064A\u0628"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: MRT-SAN-06
    source_category_code: flush_to_piped_sewer_system
    national_label_en: flush to piped sewer system
    national_label_local: "\u0625\u0644\u0649 \u0646\u0638\u0627\u0645 \u0627\u0644\
      \u0635\u0631\u0641 \u0627\u0644\u0635\u062D\u064A \u0628\u0627\u0644\u0623\u0646\
      \u0627\u0628\u064A\u0628"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: MRT-SAN-07
    source_category_code: chasse_d_eau_reliee_a_une_fosse_simple_couverte
    national_label_en: "CHASSE D'EAU / Reli\xE9e \xE0 une fosse simple couverte"
    national_label_local: "\u0644\u0644\u062D\u0641\u0631"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: MRT-SAN-08
    source_category_code: flush_to_pit_latrine
    national_label_en: flush to pit latrine
    national_label_local: "\u0644\u0644\u062D\u0641\u0631"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: MRT-SAN-09
    source_category_code: chasse_d_eau_reliee_a_fosse_septique
    national_label_en: "CHASSE D'EAU / Reli\xE9e \xE0 fosse septique"
    national_label_local: "\u0644\u062E\u0632\u0627\u0646 \u0627\u0644\u0635\u0631\
      \u0641 \u0627\u0644\u0635\u062D\u064A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: MRT-SAN-10
    source_category_code: flush_to_septic_tank
    national_label_en: flush to septic tank
    national_label_local: "\u0644\u062E\u0632\u0627\u0646 \u0627\u0644\u0635\u0631\
      \u0641 \u0627\u0644\u0635\u062D\u064A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: MRT-SAN-11
    source_category_code: chasse_d_eau_reliee_a_un_lieu_inconnu
    national_label_en: "CHASSE D'EAU / Reli\xE9e   \xE0 un lieu inconnu"
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u063A\u064A\
      \u0631 \u0645\u0639\u0631\u0648\u0641 / \u0644\u0633\u062A \u0645\u062A\u0623\
      \u0643\u062F\u064B\u0627 / \u0644\u0627 \u0623\u0639\u0631\u0641"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: MRT-SAN-12
    source_category_code: flush_don_t_know_where
    national_label_en: flush, don't know where
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u063A\u064A\
      \u0631 \u0645\u0639\u0631\u0648\u0641 / \u0644\u0633\u062A \u0645\u062A\u0623\
      \u0643\u062F\u064B\u0627 / \u0644\u0627 \u0623\u0639\u0631\u0641"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: MRT-SAN-13
    source_category_code: toilettes_avec_chasse_d_eau
    national_label_en: Toilettes avec chasse d'eau
    national_label_local: "\u062F\u0627\u0641\u0642 \u062E\u0627\u0635 / \u0645\u0631\
      \u062D\u0627\u0636"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: MRT-SAN-14
    source_category_code: toilettes_publiques
    national_label_en: Toilettes publiques
    national_label_local: "\u0639\u0627\u0645 / \u062F\u0627\u0641\u0642 \u0645\u0634\
      \u062A\u0631\u0643 / \u0645\u0631\u062D\u0627\u0636"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: MRT-SAN-15
    source_category_code: bucket_toilet
    national_label_en: bucket toilet
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062F\u0644\u0648"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: MRT-SAN-16
    source_category_code: hanging_toilet_latrine
    national_label_en: hanging toilet/latrine
    national_label_local: "\u062F\u0648\u0631\u0629 \u0645\u064A\u0627\u0647 \u0645\
      \u0639\u0644\u0642\u0629 / \u0645\u0631\u062D\u0627\u0636 \u0645\u0639\u0644\
      \u0642"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: MRT-SAN-17
    source_category_code: toilettes_suspendues_latrines_suspendues
    national_label_en: TOILETTES SUSPENDUES / LATRINES SUSPENDUES
    national_label_local: "\u062F\u0648\u0631\u0629 \u0645\u064A\u0627\u0647 \u0645\
      \u0639\u0644\u0642\u0629 / \u0645\u0631\u062D\u0627\u0636 \u0645\u0639\u0644\
      \u0642"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: MRT-SAN-18
    source_category_code: latrine_a_fosse_latrine_a_fosse_avec_dalle
    national_label_en: "LATRINE A FOSSE/ Latrine \xE0 fosse avec dalle"
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062D\u0641\u0631\u0629\
      \ \u0645\u0639 \u0628\u0644\u0627\u0637\u0629 / \u0645\u0631\u062D\u0627\u0636\
      \ \u0645\u063A\u0637\u0649"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: MRT-SAN-19
    source_category_code: pit_latrine_with_slab
    national_label_en: pit latrine with slab
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062D\u0641\u0631\u0629\
      \ \u0645\u0639 \u0628\u0644\u0627\u0637\u0629 / \u0645\u0631\u062D\u0627\u0636\
      \ \u0645\u063A\u0637\u0649"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: MRT-SAN-20
    source_category_code: latrine_a_fosse_latrine_a_fosse_sans_dalle_fosse_ouverte
    national_label_en: "LATRINE A FOSSE/ Latrine \xE0  fosse sans dalle / fosse ouverte"
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062D\u0641\u0631\u0629\
      \ \u0628\u062F\u0648\u0646 \u0628\u0644\u0627\u0637\u0629 / \u062D\u0641\u0631\
      \u0629 \u0645\u0641\u062A\u0648\u062D\u0629"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: MRT-SAN-21
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: pit latrine without slab/open pit
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062D\u0641\u0631\u0629\
      \ \u0628\u062F\u0648\u0646 \u0628\u0644\u0627\u0637\u0629 / \u062D\u0641\u0631\
      \u0629 \u0645\u0641\u062A\u0648\u062D\u0629"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: MRT-SAN-22
    source_category_code: latrines_avec_fosse_septique
    national_label_en: Latrines avec fosse septique
    national_label_local: "\u0627\u0644\u0645\u0631\u0627\u062D\u064A\u0636 \u0627\
      \u0644\u062A\u0642\u0644\u064A\u062F\u064A\u0629"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MRT-SAN-23
    source_category_code: latrine_a_fosse_latrine_a_fosse_amelioree_ventilee
    national_label_en: "LATRINE A FOSSE/ Latrine \xE0 fosse am\xE9lior\xE9e ventil\xE9\
      e"
    national_label_local: "\u0645\u0631\u0627\u062D\u064A\u0636 \u062D\u0641\u0631\
      \u0629 \u0645\u062D\u0633\u0646\u0629 \u062C\u064A\u062F\u0629 \u0627\u0644\u062A\
      \u0647\u0648\u064A\u0629"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: MRT-SAN-24
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: ventilated improved pit latrine (vip)
    national_label_local: "\u0645\u0631\u0627\u062D\u064A\u0636 \u062D\u0641\u0631\
      \u0629 \u0645\u062D\u0633\u0646\u0629 \u062C\u064A\u062F\u0629 \u0627\u0644\u062A\
      \u0647\u0648\u064A\u0629"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: MRT-SAN-25
    source_category_code: cuvette_seau
    national_label_en: Cuvette/seau
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062F\u0644\u0648"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.private_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 118
  - country_entry_id: MRT-SAN-26
    source_category_code: non_pas_disponible
    national_label_en: Non, pas disponible
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MRT-SAN-27
    source_category_code: pas_de_toilettes
    national_label_en: Pas de toilettes
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MRT-SAN-28
    source_category_code: pas_de_toilettes_nature_champs
    national_label_en: PAS DE TOILETTES / NATURE/ CHAMPS
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MRT-SAN-29
    source_category_code: autre
    national_label_en: Autre
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: MRT-SAN-30
    source_category_code: other_type_of_sanitation
    national_label_en: Other type of sanitation
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MRT_Mauritania_2.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MRT-WAS-01
    source_category_code: eau_de_source_protegee
    national_label_en: Eau de source protegee
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u0627\u0644\u0645\u062D\
      \u0645\u064A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: MRT-WAS-02
    source_category_code: protected_spring
    national_label_en: protected spring
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u0627\u0644\u0645\u062D\
      \u0645\u064A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: MRT-WAS-03
    source_category_code: protected_well
    national_label_en: protected well
    national_label_local: "\u0645\u062D\u0645\u064A \u0628\u0634\u0643\u0644 \u062C\
      \u064A\u062F"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: MRT-WAS-04
    source_category_code: puits_protege
    national_label_en: "Puits prot\xE9g\xE9"
    national_label_local: "\u0645\u062D\u0645\u064A \u0628\u0634\u0643\u0644 \u062C\
      \u064A\u062F"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: MRT-WAS-05
    source_category_code: puits_protegee
    national_label_en: Puits protegee
    national_label_local: "\u0645\u062D\u0645\u064A \u0628\u0634\u0643\u0644 \u062C\
      \u064A\u062F"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: MRT-WAS-06
    source_category_code: puits_sans_pompe
    national_label_en: Puits sans pompe
    national_label_local: "\u0627\u0644\u0622\u0628\u0627\u0631 \u0627\u0644\u062A\
      \u0642\u0644\u064A\u062F\u064A\u0629"
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 62
  - country_entry_id: MRT-WAS-07
    source_category_code: puits_a_pompe_forage
    national_label_en: Puits a pompe, forage
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MRT-WAS-08
    source_category_code: puits_avec_pompe
    national_label_en: Puits avec pompe
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MRT-WAS-09
    source_category_code: puits_tubulaire_ou_forage
    national_label_en: Puits tubulaire ou forage
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MRT-WAS-10
    source_category_code: tube_well_or_borehole
    national_label_en: tube well or borehole
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MRT-WAS-11
    source_category_code: eau_de_source_non_protegee
    national_label_en: Eau de source non protegee
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u063A\u064A\u0631 \u0627\
      \u0644\u0645\u062D\u0645\u064A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: MRT-WAS-12
    source_category_code: eau_source_non_protegee
    national_label_en: Eau source non protegee
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u063A\u064A\u0631 \u0627\
      \u0644\u0645\u062D\u0645\u064A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: MRT-WAS-13
    source_category_code: unprotected_spring
    national_label_en: unprotected spring
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u063A\u064A\u0631 \u0627\
      \u0644\u0645\u062D\u0645\u064A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: MRT-WAS-14
    source_category_code: puits_non_protege
    national_label_en: "Puits non prot\xE9g\xE9"
    national_label_local: "\u0628\u0626\u0631 \u063A\u064A\u0631 \u0645\u062D\u0645\
      \u064A"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MRT-WAS-15
    source_category_code: puits_non_protegee
    national_label_en: Puits non protegee
    national_label_local: "\u0628\u0626\u0631 \u063A\u064A\u0631 \u0645\u062D\u0645\
      \u064A"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MRT-WAS-16
    source_category_code: unprotected_well
    national_label_en: unprotected well
    national_label_local: "\u0628\u0626\u0631 \u063A\u064A\u0631 \u0645\u062D\u0645\
      \u064A"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MRT-WAS-17
    source_category_code: achetee_d_un_chariot_avec_un_petit_ra_servoir_ou_tambour
    national_label_en: "Achetee d'un chariot avec un petit r\xC3\xA9servoir ou tambour"
    national_label_local: "\u0639\u0631\u0628\u0629 \u0645\u0639 \u062E\u0632\u0627\
      \u0646 \u0635\u063A\u064A\u0631 / \u0623\u0633\u0637\u0648\u0627\u0646\u0629"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MRT-WAS-18
    source_category_code: cart_with_small_tank
    national_label_en: cart with small tank
    national_label_local: "\u0639\u0631\u0628\u0629 \u0645\u0639 \u062E\u0632\u0627\
      \u0646 \u0635\u063A\u064A\u0631 / \u0623\u0633\u0637\u0648\u0627\u0646\u0629"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MRT-WAS-19
    source_category_code: charrette_avec_petite_citerne_tonneau
    national_label_en: Charrette avec petite citerne/tonneau
    national_label_local: "\u0639\u0631\u0628\u0629 \u0645\u0639 \u062E\u0632\u0627\
      \u0646 \u0635\u063A\u064A\u0631 / \u0623\u0633\u0637\u0648\u0627\u0646\u0629"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MRT-WAS-20
    source_category_code: revendeur_d_eau
    national_label_en: Revendeur d'eau
    national_label_local: "\u0639\u0631\u0628\u0629 \u0645\u0639 \u062E\u0632\u0627\
      \u0646 \u0635\u063A\u064A\u0631 / \u0623\u0633\u0637\u0648\u0627\u0646\u0629"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MRT-WAS-21
    source_category_code: kiosque_a_eau
    national_label_en: Kiosque a eau
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: MRT-WAS-22
    source_category_code: revendeur_d_eau
    national_label_en: Revendeur d'eau
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: MRT-WAS-23
    source_category_code: achetee_d_une_citerne
    national_label_en: Achetee d'une citerne
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: MRT-WAS-24
    source_category_code: camion_citerne
    national_label_en: Camion-citerne
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: MRT-WAS-25
    source_category_code: citerne
    national_label_en: Citerne
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: MRT-WAS-26
    source_category_code: tanker_truck
    national_label_en: tanker truck
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: MRT-WAS-27
    source_category_code: autre
    national_label_en: Autre
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: MRT-WAS-28
    source_category_code: a_refuse
    national_label_en: A refuse
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MRT-WAS-29
    source_category_code: autre
    national_label_en: Autre
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MRT-WAS-30
    source_category_code: bottled_water
    national_label_en: bottled water
    national_label_local: "\u0645\u064A\u0627\u0647 \u0645\u0639\u0628\u0623\u0629"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: MRT-WAS-31
    source_category_code: eau_en_bouteille
    national_label_en: Eau en bouteille
    national_label_local: "\u0645\u064A\u0627\u0647 \u0645\u0639\u0628\u0623\u0629"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: MRT-WAS-32
    source_category_code: eau_en_sachet
    national_label_en: Eau en sachet
    national_label_local: "\u0643\u064A\u0633 \u0645\u0627\u0621"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: MRT-WAS-33
    source_category_code: mineral_water_in_sachet
    national_label_en: mineral water in sachet
    national_label_local: "\u0643\u064A\u0633 \u0645\u0627\u0621"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: MRT-WAS-34
    source_category_code: collecte_d_eau_de_pluie
    national_label_en: Collecte d'eau de pluie
    national_label_local: "\u062E\u0632\u0627\u0646 / \u062E\u0632\u0627\u0646 \u0645\
      \u063A\u0637\u0649"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: MRT-WAS-35
    source_category_code: eau_de_pluie
    national_label_en: Eau de pluie
    national_label_local: "\u062E\u0632\u0627\u0646 / \u062E\u0632\u0627\u0646 \u0645\
      \u063A\u0637\u0649"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: MRT-WAS-36
    source_category_code: rainwater
    national_label_en: rainwater
    national_label_local: "\u062E\u0632\u0627\u0646 / \u062E\u0632\u0627\u0646 \u0645\
      \u063A\u0637\u0649"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: MRT-WAS-37
    source_category_code: eau_de_surface_riviere_fleuve
    national_label_en: Eau de surface (riviere, fleuve)
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MRT-WAS-38
    source_category_code: eau_de_surface_telle_que_rivia_re_barrage_lac_a_tang_ruisseau_canal_ou_canaux_da_tmirrigation
    national_label_en: "Eau de surface, telle que rivi\xC3\xA8re, barrage, lac, \xC3\
      \xA9tang, ruisseau, canal ou canaux d\xE2\u20AC\u2122irrigation"
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MRT-WAS-39
    source_category_code: fleuve_riviere_lac_ruisseau_source
    national_label_en: "Fleuve,rivi\xE8re,lac,ruisseau,source"
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MRT-WAS-40
    source_category_code: river_dam_lake_ponds_stream_canal_irrigation_channel
    national_label_en: river/dam/lake/ponds/stream/canal/irrigation channel
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MRT-WAS-41
    source_category_code: piped_to_neighbor
    national_label_en: piped to neighbor
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: MRT-WAS-42
    source_category_code: robinet_commun_du_voisin
    national_label_en: Robinet commun /du voisin
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: MRT-WAS-43
    source_category_code: robinet_commun_or_du_voisin
    national_label_en: Robinet commun or du voisin
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: MRT-WAS-44
    source_category_code: robinet_du_voisin
    national_label_en: Robinet du voisin
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: MRT-WAS-45
    source_category_code: piped_into_dwelling
    national_label_en: piped into dwelling
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: MRT-WAS-46
    source_category_code: robinet_dans_la_maison
    national_label_en: Robinet dans la maison
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: MRT-WAS-47
    source_category_code: robinet_dans_le_logement
    national_label_en: Robinet dans le logement
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: MRT-WAS-48
    source_category_code: robinet_interieur
    national_label_en: "Robinet int\xE9rieur"
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: MRT-WAS-49
    source_category_code: piped_to_yard_plot
    national_label_en: piped to yard/plot
    national_label_local: "\u0627\u0644\u0645\u064A\u0627\u0647 \u0627\u0644\u0645\
      \u0646\u0642\u0648\u0644\u0629 \u0628\u0627\u0644\u0623\u0646\u0627\u0628\u064A\
      \u0628 \u0625\u0644\u0649 \u0633\u0627\u062D\u0629 / \u0642\u0637\u0639\u0629\
      \ \u0623\u0631\u0636"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: MRT-WAS-50
    source_category_code: robinet_dans_concession_cour_ou_parcelle
    national_label_en: Robinet dans concession, cour ou parcelle
    national_label_local: "\u0627\u0644\u0645\u064A\u0627\u0647 \u0627\u0644\u0645\
      \u0646\u0642\u0648\u0644\u0629 \u0628\u0627\u0644\u0623\u0646\u0627\u0628\u064A\
      \u0628 \u0625\u0644\u0649 \u0633\u0627\u062D\u0629 / \u0642\u0637\u0639\u0629\
      \ \u0623\u0631\u0636"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: MRT-WAS-51
    source_category_code: robinet_dans_la_cour_dans_la_parcelle_ou_dans_la_concession
    national_label_en: Robinet dans la cour, dans la parcelle, ou dans la concession
    national_label_local: "\u0627\u0644\u0645\u064A\u0627\u0647 \u0627\u0644\u0645\
      \u0646\u0642\u0648\u0644\u0629 \u0628\u0627\u0644\u0623\u0646\u0627\u0628\u064A\
      \u0628 \u0625\u0644\u0649 \u0633\u0627\u062D\u0629 / \u0642\u0637\u0639\u0629\
      \ \u0623\u0631\u0636"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: MRT-WAS-52
    source_category_code: fontaine_publique
    national_label_en: Fontaine publique
    national_label_local: "\u0627\u0644\u062D\u0646\u0641\u064A\u0629 \u0627\u0644\
      \u0639\u0627\u0645\u0629 \u0648\u0627\u0644\u0635\u0646\u0628\u0648\u0631 \u0627\
      \u0644\u0631\u0623\u0633\u064A"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: MRT-WAS-53
    source_category_code: public_tap_standpipe
    national_label_en: public tap/standpipe
    national_label_local: "\u0627\u0644\u062D\u0646\u0641\u064A\u0629 \u0627\u0644\
      \u0639\u0627\u0645\u0629 \u0648\u0627\u0644\u0635\u0646\u0628\u0648\u0631 \u0627\
      \u0644\u0631\u0623\u0633\u064A"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: MRT-WAS-54
    source_category_code: robinet_ou_fontaine_publique
    national_label_en: Robinet ou fontaine publique
    national_label_local: "\u0627\u0644\u062D\u0646\u0641\u064A\u0629 \u0627\u0644\
      \u0639\u0627\u0645\u0629 \u0648\u0627\u0644\u0635\u0646\u0628\u0648\u0631 \u0627\
      \u0644\u0631\u0623\u0633\u064A"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: MRT-WAS-55
    source_category_code: robinet_public_borne_fontaine
    national_label_en: Robinet public/Borne fontaine
    national_label_local: "\u0627\u0644\u062D\u0646\u0641\u064A\u0629 \u0627\u0644\
      \u0639\u0627\u0645\u0629 \u0648\u0627\u0644\u0635\u0646\u0628\u0648\u0631 \u0627\
      \u0644\u0631\u0623\u0633\u064A"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MRT_Mauritania_2.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 2001
  effective_to: null
  selectors: null
  value: 14
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

