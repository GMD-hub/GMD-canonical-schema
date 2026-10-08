---
country_id: CTY-LBN
iso3: LBN
schema_version: '0.2'
status: draft
country_name: LBN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: LBN-EDU-01
    national_label_en: "Pr\xE9 primaire"
    national_label_local: "\u0645\u0627 \u0642\u0628\u0644 \u0627\u0644\u0627\u0628\
      \u062A\u062F\u0627\u0626\u064A"
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
  - country_entry_id: LBN-EDU-02
    national_label_en: "Cycle primaire (1er et 2\xE8me cycles de l'enseignement principal)"
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u0627\u0628\u062A\u062F\u0627\u0626\u064A\u0629 (\u0627\u0644\u062D\u0644\u0642\
      \u062A\u064A\u0646 \u0627\u0644\u0623\u0648\u0644\u0649 \u0648\u0627\u0644\u062B\
      \u0627\u0646\u064A\u0629 \u0645\u0646 \u0627\u0644\u062A\u0639\u0644\u064A\u0645\
      \ \u0627\u0644\u0623\u0633\u0627\u0633\u064A)"
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - LBN-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: LBN-EDU-03
    national_label_en: "Cycle moyen (3\xE8me cycle de l'enseignement principal)"
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u0645\u062A\u0648\u0633\u0637\u0629 (\u0627\u0644\u062D\u0644\u0642\u0629 \u0627\
      \u0644\u062B\u0627\u0644\u062B\u0629 \u0645\u0646 \u0627\u0644\u062A\u0639\u0644\
      \u064A\u0645 \u0627\u0644\u0623\u0633\u0627\u0633\u064A)"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - LBN-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBN-EDU-04
    national_label_en: Aptitude professionnelle
    national_label_local: "\u0627\u0644\u0643\u0641\u0627\u0621\u0629 \u0627\u0644\
      \u0645\u0647\u0646\u064A\u0629"
    entry_age: 13
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - LBN-EDU-02
    cum_years_schooling: 8
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBN-EDU-05
    national_label_en: Brevet professionnel (B.P.)
    national_label_local: "\u0627\u0644\u062A\u0643\u0645\u064A\u0644\u064A\u0629\
      \ \u0627\u0644\u0645\u0647\u0646\u064A\u0629"
    entry_age: 14
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - LBN-EDU-02
    cum_years_schooling: 8
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBN-EDU-06
    national_label_en: "Secondaire g\xE9n\xE9rale"
    national_label_local: "\u0627\u0644\u062B\u0627\u0646\u0648\u064A\u0629 \u0627\
      \u0644\u0639\u0627\u0645\u0629"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - LBN-EDU-03
    - LBN-EDU-04
    - LBN-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
  - country_entry_id: LBN-EDU-07
    national_label_en: Secondaire professionnelle
    national_label_local: "\u0627\u0644\u062B\u0627\u0646\u0648\u064A\u0629  \u0627\
      \u0644\u0645\u0647\u0646\u064A\u0629"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - LBN-EDU-03
    - LBN-EDU-04
    - LBN-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
  - country_entry_id: LBN-EDU-08
    national_label_en: Secondaire technique
    national_label_local: "\u0627\u0644\u062B\u0627\u0646\u0648\u064A\u0629 \u0627\
      \u0644\u0641\u0646\u064A\u0629"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - LBN-EDU-03
    - LBN-EDU-04
    - LBN-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
  - country_entry_id: LBN-EDU-09
    national_label_en: "Dipl\xF4me Universitaire - 1 an"
    national_label_local: "\u062F\u0628\u0644\u0648\u0645 \u062C\u0627\u0645\u0639\
      \u064A- \u0633\u0646\u0629 \u0648\u0627\u062D\u062F\u0629"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-10
    national_label_en: "Dipl\xF4me Universitaire"
    national_label_local: "\u062F\u0628\u0644\u0648\u0645 \u062C\u0627\u0645\u0639\
      \u064A"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-11
    national_label_en: "Technique sup\xE9rieur (TS)"
    national_label_local: "\u0627\u0645\u062A\u064A\u0627\u0632 \u0641\u0646\u064A"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-12
    national_label_en: Licence technique
    national_label_local: "\u0627\u0644\u0625\u062C\u0627\u0632\u0629 \u0627\u0644\
      \u0641\u0646\u064A\u0629"
    entry_age: 20
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-13
    national_label_en: Licence
    national_label_local: "\u0625\u062C\u0627\u0632\u0629"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 14
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-14
    national_label_en: "Ma\xEEtrise"
    national_label_local: "\u062C\u062F\u0627\u0631\u0629"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 15
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-15
    national_label_en: "Etude de m\xE9decine"
    national_label_local: "\u062F\u0631\u0627\u0633\u0629  \u0627\u0644\u0637\u0628"
    entry_age: 18
    duration_years: 7
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 18
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-16
    national_label_en: "Magist\xE8re"
    national_label_local: "\u0645\u0627\u062C\u0633\u062A\u064A\u0631"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-17
    national_label_en: "Dipl\xF4me d'\xE9tudes sup\xE9rieures (D.E.S.)"
    national_label_local: "\u062F\u0628\u0644\u0648\u0645 \u062F\u0631\u0627\u0633\
      \u0627\u062A \u0639\u0644\u064A\u0627"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-18
    national_label_en: "Dipl\xF4me d'\xE9tudes approfondies (D.E.A.)"
    national_label_local: "\u062F\u0628\u0644\u0648\u0645 \u062F\u0631\u0627\u0633\
      \u0627\u062A \u0645\u0639\u0645\u0642\u0629"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-19
    national_label_en: "\xC9tudes sup\xE9rieures sp\xE9cialis\xE9es"
    national_label_local: "\u062F\u0631\u0627\u0633\u0627\u062A \u0639\u0644\u064A\
      \u0627 \u0645\u062A\u062E\u0635\u0635\u0629"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - LBN-EDU-06
    - LBN-EDU-07
    - LBN-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
  - country_entry_id: LBN-EDU-20
    national_label_en: Doctorat
    national_label_local: "\u062F\u0643\u062A\u0648\u0631\u0627\u0647"
    entry_age: 23
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - LBN-EDU-15
    - LBN-EDU-16
    - LBN-EDU-17
    - LBN-EDU-18
    - LBN-EDU-19
    cum_years_schooling: 15
    cum_years_computation_path:
    - LBN-EDU-02
    - LBN-EDU-04
    - LBN-EDU-06
    - LBN-EDU-18
    - LBN-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBN-EDU-03, LBN-EDU-04, LBN-EDU-05'
    - 'minimum parent path selected from: LBN-EDU-06, LBN-EDU-07, LBN-EDU-08'
    - 'minimum parent path selected from: LBN-EDU-15, LBN-EDU-16, LBN-EDU-17, LBN-EDU-18,
      LBN-EDU-19'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Lebanon.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: LBN-SUBNAT-01
    survey_labels: 1 - Beirut | 1-Beirut
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: LBN_2015_GAUL1_1798
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: LBN_2015_GAUL1_1798
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1798'
    geo_nvar: ADM1_NAME
    geo_name: Beirut
    source_row: 8975
  - country_entry_id: LBN-SUBNAT-02
    survey_labels: 2 - Mount Lebanon | 2-Mount Lebanon
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: LBN_2015_GAUL1_1801
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: LBN_2015_GAUL1_1801
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1801'
    geo_nvar: ADM1_NAME
    geo_name: Mount Lebanon
    source_row: 8976
  - country_entry_id: LBN-SUBNAT-03
    survey_labels: 3 - North
    survey_variables: subnatid
    gmd_subnatid1: LBN_2015_GAUL1_1799
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: LBN_2015_GAUL1_1799
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1799'
    geo_nvar: ADM1_NAME
    geo_name: North
    source_row: 8977
  - country_entry_id: LBN-SUBNAT-04
    survey_labels: 5 - Bekaa | 5-Bekaa
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: LBN_2015_GAUL1_1797
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: LBN_2015_GAUL1_1797
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1797'
    geo_nvar: ADM1_NAME
    geo_name: Bekaa
    source_row: 8978
  - country_entry_id: LBN-SUBNAT-05
    survey_labels: 6 - South
    survey_variables: subnatid
    gmd_subnatid1: LBN_2015_GAUL1_1800
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: LBN_2015_GAUL1_1800
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1800'
    geo_nvar: ADM1_NAME
    geo_name: South
    source_row: 8979
  - country_entry_id: LBN-SUBNAT-06
    survey_labels: 7 - Nabatieh
    survey_variables: subnatid
    gmd_subnatid1: LBN_2015_GAUL1_1802
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: LBN_2015_GAUL1_1802
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1802'
    geo_nvar: ADM1_NAME
    geo_name: Nabatiye
    source_row: 8980
  - country_entry_id: LBN-SUBNAT-07
    survey_labels: 3-North
    survey_variables: subnatid1
    gmd_subnatid1: LBN_2015_GAULx_3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '3'
    geo_nvar: ADM1_NAME
    geo_name: North
    source_row: 8983
  - country_entry_id: LBN-SUBNAT-08
    survey_labels: 4-Akkar
    survey_variables: subnatid1
    gmd_subnatid1: LBN_2015_GAUL2_18797
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '2'
    geo_idvar: ADM2_CODE
    geo_id: '18797'
    geo_nvar: ADM2_NAME
    geo_name: Akkar
    source_row: 8984
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
  - country_entry_id: LBN-SAN-01
    source_category_code: open_sewage_system
    national_label_en: Open sewage system
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: LBN-SAN-02
    source_category_code: public_sewage_system
    national_label_en: Public sewage system
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
  - country_entry_id: LBN-SAN-03
    source_category_code: septic_tank
    national_label_en: Septic tank
    national_label_local: "\u0644\u062E\u0632\u0627\u0646 \u0627\u0644\u0635\u0631\
      \u0641 \u0627\u0644\u0635\u062D\u064A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: LBN-SAN-04
    source_category_code: no_facility
    national_label_en: No facility
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: LBN-SAN-05
    source_category_code: other_source
    national_label_en: Other source
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_LBN_Lebanon_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: LBN-WAS-01
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u0627\u0644\u0645\u062D\
      \u0645\u064A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: LBN-WAS-02
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: "\u0645\u062D\u0645\u064A \u0628\u0634\u0643\u0644 \u062C\
      \u064A\u062F"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: LBN-WAS-03
    source_category_code: protected_wells_or_springs
    national_label_en: Protected wells or springs
    national_label_local: "\u0622\u0628\u0627\u0631 \u0623\u0648 \u064A\u0646\u0627\
      \u0628\u064A\u0639 \u0645\u062D\u0645\u064A\u0629"
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: true
    shared_flag: false
    source_row: 46
  - country_entry_id: LBN-WAS-04
    source_category_code: boreholes_tubewells
    national_label_en: Boreholes/Tubewells
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: LBN-WAS-05
    source_category_code: tube_well_borehole
    national_label_en: Tube well, Borehole
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: LBN-WAS-06
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u063A\u064A\u0631 \u0627\
      \u0644\u0645\u062D\u0645\u064A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: LBN-WAS-07
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: "\u0628\u0626\u0631 \u063A\u064A\u0631 \u0645\u062D\u0645\
      \u064A"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: LBN-WAS-08
    source_category_code: unprotected_wells_or_springs
    national_label_en: Unprotected wells or springs
    national_label_local: "\u0627\u0644\u0622\u0628\u0627\u0631 \u0623\u0648 \u0627\
      \u0644\u064A\u0646\u0627\u0628\u064A\u0639 \u063A\u064A\u0631 \u0627\u0644\u0645\
      \u062D\u0645\u064A\u0629"
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 50
  - country_entry_id: LBN-WAS-09
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank / drum
    national_label_local: "\u0639\u0631\u0628\u0629 \u0645\u0639 \u062E\u0632\u0627\
      \u0646 \u0635\u063A\u064A\u0631 / \u0623\u0633\u0637\u0648\u0627\u0646\u0629"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: LBN-WAS-10
    source_category_code: delivered_water_tanker_trucks
    national_label_en: Delivered water (tanker trucks)
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: LBN-WAS-11
    source_category_code: tanker_truck
    national_label_en: Tanker-truck
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: LBN-WAS-12
    source_category_code: other
    national_label_en: other
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: LBN-WAS-13
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "\u0645\u064A\u0627\u0647 \u0645\u0639\u0628\u0623\u0629"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: LBN-WAS-14
    source_category_code: packed_water_bottled
    national_label_en: Packed water (bottled)
    national_label_local: "\u0645\u064A\u0627\u0647 \u0645\u0639\u0628\u0623\u0629"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: LBN-WAS-15
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: "\u0645\u064A\u0627\u0647 \u0627\u0644\u0623\u0645\u0637\
      \u0627\u0631"
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 86
  - country_entry_id: LBN-WAS-16
    source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: LBN-WAS-17
    source_category_code: surface_water_river_stream_dam_lake_pond_canal_irrigation_channel
    national_label_en: Surface water (river, stream, dam, lake, pond, canal, irrigation
      channel)
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: LBN-WAS-18
    source_category_code: piped_to_neighbour
    national_label_en: Piped to neighbour
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: LBN-WAS-19
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: LBN-WAS-20
    source_category_code: tap_water_into_dwelling
    national_label_en: Tap water into dwelling
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: LBN-WAS-21
    source_category_code: piped_into_compound_yard_or_plot
    national_label_en: Piped into compound, yard or plot
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
  - country_entry_id: LBN-WAS-22
    source_category_code: public_stanposts
    national_label_en: Public stanposts
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
  - country_entry_id: LBN-WAS-23
    source_category_code: public_tap_standpipe
    national_label_en: Public tap / standpipe
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_LBN_Lebanon_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 2003
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

