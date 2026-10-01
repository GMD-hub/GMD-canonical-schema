---
country_id: CTY-IRQ
iso3: IRQ
schema_version: '0.2'
status: draft
country_name: IRQ
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: IRQ-EDU-01
    national_label_en: Kindergarten
    national_label_local: "\u0631\u064A\u0627\u0636 \u0627\u0644\u0623\u0637\u0641\
      \u0627\u0644"
    entry_age: 4
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
  - country_entry_id: IRQ-EDU-02
    national_label_en: Primary education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0627\u0628\u062A\u062F\u0627\u0626\u064A"
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
    - IRQ-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: IRQ-EDU-03
    national_label_en: Adult primary education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0627\u0628\u062A\u062F\u0627\u0626\u064A \u0644\u0644\u0643\u0628\u0627\u0631"
    entry_age: 10
    duration_years: 3
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 3
    cum_years_computation_path:
    - IRQ-EDU-03
    cum_years_status: computed
    review_flags: []
  - country_entry_id: IRQ-EDU-04
    national_label_en: Intermediate education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0645\u062A\u0648\u0633\u0637"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - IRQ-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRQ-EDU-05
    national_label_en: Preparatory education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0625\u0639\u062F\u0627\u062F\u064A"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - IRQ-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRQ-EDU-06
    national_label_en: Vocational education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0645\u0647\u0646\u064A"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - IRQ-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRQ-EDU-07
    national_label_en: Fine Arts Institutes Programs (First to third year)
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0645\u0639\u0627\u0647\
      \u062F \u0627\u0644\u0641\u0646\u0648\u0646 \u0627\u0644\u062C\u0645\u064A\u0644\
      \u0629 (\u0633\u0646\u0629 \u0623\u0648\u0644\u0649 \u0625\u0644\u0649 \u062B\
      \u0627\u0644\u062B\u0629)"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - IRQ-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: IRQ-EDU-08
    national_label_en: Fine Arts Institutes Programs (Fourth and fifth Years)
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0645\u0639\u0627\u0647\
      \u062F \u0627\u0644\u0641\u0646\u0648\u0646 \u0627\u0644\u062C\u0645\u064A\u0644\
      \u0629 (\u0633\u0646\u0629 \u0631\u0627\u0628\u0639\u0629 \u0648\u062E\u0627\
      \u0645\u0633\u0629)"
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - IRQ-EDU-05
    - IRQ-EDU-07
    cum_years_schooling: 14
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-05
    - IRQ-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRQ-EDU-05, IRQ-EDU-07'
  - country_entry_id: IRQ-EDU-09
    national_label_en: Technical diploma
    national_label_local: "\u062F\u0628\u0644\u0648\u0645 \u062A\u0642\u0646\u064A"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - IRQ-EDU-05
    - IRQ-EDU-07
    cum_years_schooling: 14
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-05
    - IRQ-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRQ-EDU-05, IRQ-EDU-07'
  - country_entry_id: IRQ-EDU-10
    national_label_en: 4 years Bachelor's programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0628\u0643\u0627\u0644\
      \u0648\u0631\u064A\u0648\u0633 4 \u0633\u0646\u0648\u0627\u062A"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - IRQ-EDU-05
    - IRQ-EDU-07
    cum_years_schooling: 16
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-05
    - IRQ-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRQ-EDU-05, IRQ-EDU-07'
  - country_entry_id: IRQ-EDU-11
    national_label_en: 5 years Bachelor's programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0628\u0643\u0627\u0644\
      \u0648\u0631\u064A\u0648\u0633 5 \u0633\u0646\u0648\u0627\u062A"
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - IRQ-EDU-05
    - IRQ-EDU-07
    cum_years_schooling: 17
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-05
    - IRQ-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRQ-EDU-05, IRQ-EDU-07'
  - country_entry_id: IRQ-EDU-12
    national_label_en: High diploma
    national_label_local: "\u062F\u0628\u0644\u0648\u0645 \u0639\u0627\u0644\u064A"
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - IRQ-EDU-05
    - IRQ-EDU-07
    cum_years_schooling: 13
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-05
    - IRQ-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRQ-EDU-05, IRQ-EDU-07'
  - country_entry_id: IRQ-EDU-13
    national_label_en: Bachelor's in medicine
    national_label_local: "\u0628\u0643\u0627\u0644\u0648\u0631\u064A\u0648\u0633\
      \ \u0627\u0644\u0637\u0628"
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - IRQ-EDU-05
    - IRQ-EDU-07
    cum_years_schooling: 18
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-05
    - IRQ-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRQ-EDU-05, IRQ-EDU-07'
  - country_entry_id: IRQ-EDU-14
    national_label_en: Master's programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0645\u0627\
      \u062C\u0633\u062A\u064A\u0631"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - IRQ-EDU-10
    - IRQ-EDU-11
    - IRQ-EDU-12
    cum_years_schooling: 15
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-05
    - IRQ-EDU-12
    - IRQ-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRQ-EDU-05, IRQ-EDU-07'
    - 'minimum parent path selected from: IRQ-EDU-10, IRQ-EDU-11, IRQ-EDU-12'
  - country_entry_id: IRQ-EDU-15
    national_label_en: Doctoral programme
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u062F\u0643\
      \u062A\u0648\u0631\u0627\u0647"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - IRQ-EDU-13
    - IRQ-EDU-14
    cum_years_schooling: 18
    cum_years_computation_path:
    - IRQ-EDU-02
    - IRQ-EDU-04
    - IRQ-EDU-05
    - IRQ-EDU-12
    - IRQ-EDU-14
    - IRQ-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: IRQ-EDU-05, IRQ-EDU-07'
    - 'minimum parent path selected from: IRQ-EDU-10, IRQ-EDU-11, IRQ-EDU-12'
    - 'minimum parent path selected from: IRQ-EDU-13, IRQ-EDU-14'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Iraq.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: IRQ-SUBNAT-01
    survey_labels: 11 - DUHOK | 11 - Duhouk
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1574
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-02
    survey_labels: 12 - NINEVEH | 12 - Nineveh
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1578
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-03
    survey_labels: 13 - SULAYMANIYAH | 13 - Suleimaniya
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1580
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-04
    survey_labels: 14 - KIRKUK | 14 - Karkouk
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1570
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-05
    survey_labels: 15 - ERBIL | 15 - Erbil
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1569
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-06
    survey_labels: 21 - DIYALA | 21 - Diala
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1575
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-07
    survey_labels: 22 - AL-ANBAR | 22 - Al-Anbar
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1564
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-08
    survey_labels: 23 - BAGHDAD | 23 - Baghdad
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1572
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-09
    survey_labels: 24 - BABYLON | 24 - Babil
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1571
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-10
    survey_labels: 25 - KARBALA | 25 - Kerbala
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1576
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-11
    survey_labels: 26 - WASIT | 26 - Wasit
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1581
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-12
    survey_labels: 27 - SALAH AL-DIN | 27 - Salahuddin
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1579
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-13
    survey_labels: 28 - Al-Najaf | 28 - NAJAF
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1568
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-14
    survey_labels: 31 - AL-QADISIYAH | 31 - Al-Qadisiya
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1567
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-15
    survey_labels: 32 - Al-Muthanna | 32 - MUTHANNA
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1566
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-16
    survey_labels: 33 - DHI QAR | 33 - Thi-Qar
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1573
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-17
    survey_labels: 34 - MAYSAN | 34 - Missan
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1577
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
  - country_entry_id: IRQ-SUBNAT-18
    survey_labels: 35 - BASRA | 35 - Basrah
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: IRQ_2015_GAUL1_1565
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
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
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: IRQ-SAN-01
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: "\u0645\u0631\u0627\u062D\u064A\u0636 \u0627\u0644\u062A\
      \u0633\u0645\u064A\u062F"
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: IRQ-SAN-02
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u0633\u0645\u0627\u062F\
      \ (\u062E\u0627\u0635)"
    jmp_classification: Composting toilets > Composting toilet (private)
    jmp_id: composting_toilets.composting_toilet_private
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 129
  - country_entry_id: IRQ-SAN-03
    source_category_code: flush_pour_flush_to_somewhere_else
    national_label_en: Flush/pour flush to somewhere else
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: IRQ-SAN-04
    source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
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
  - country_entry_id: IRQ-SAN-05
    source_category_code: public_network_covered_drain
    national_label_en: Public network+covered drain
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
  - country_entry_id: IRQ-SAN-06
    source_category_code: flush_pour_flush_to_pit_latrine
    national_label_en: Flush/pour flush to pit latrine
    national_label_local: "\u0644\u0644\u062D\u0641\u0631"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: IRQ-SAN-07
    source_category_code: flush_pour_flush_to_septic_tank
    national_label_en: Flush/pour flush to septic tank
    national_label_local: "\u0644\u062E\u0632\u0627\u0646 \u0627\u0644\u0635\u0631\
      \u0641 \u0627\u0644\u0635\u062D\u064A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: IRQ-SAN-08
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
  - country_entry_id: IRQ-SAN-09
    source_category_code: flush_to_unknown_place_not_sure_dk_where
    national_label_en: Flush to unknown place/not sure/DK where
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
  - country_entry_id: IRQ-SAN-10
    source_category_code: flush_to_sewage_system_septic_tank
    national_label_en: Flush to sewage system/septic tank
    national_label_local: "\u062F\u0627\u0641\u0642 / \u0645\u0631\u0627\u062D\u064A\
      \u0636"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: IRQ-SAN-11
    source_category_code: flush_toilet_inside_outside_dwelling_exclusive_use_of_the_household
    national_label_en: Flush toilet, inside/outside dwelling exclusive use of the
      household
    national_label_local: "\u0625\u0644\u0649 \u0646\u0638\u0627\u0645 \u0627\u0644\
      \u0635\u0631\u0641 \u0627\u0644\u0635\u062D\u064A \u0628\u0627\u0644\u0623\u0646\
      \u0627\u0628\u064A\u0628"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: IRQ-SAN-12
    source_category_code: flushed_toilet_inside_outside_dwelling_and_shared
    national_label_en: flushed toilet inside/outside dwelling and shared
    national_label_local: "\u0625\u0644\u0649 \u0646\u0638\u0627\u0645 \u0627\u0644\
      \u0635\u0631\u0641 \u0627\u0644\u0635\u062D\u064A \u0628\u0627\u0644\u0623\u0646\
      \u0627\u0628\u064A\u0628"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: IRQ-SAN-13
    source_category_code: flush_to_open_drain
    national_label_en: Flush to open drain
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: IRQ-SAN-14
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: IRQ-SAN-15
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: "\u0625\u0644\u0649 \u0646\u0638\u0627\u0645 \u0627\u0644\
      \u0635\u0631\u0641 \u0627\u0644\u0635\u062D\u064A \u0628\u0627\u0644\u0623\u0646\
      \u0627\u0628\u064A\u0628"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: IRQ-SAN-16
    source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
    national_label_local: "\u0625\u0644\u0649 \u0646\u0638\u0627\u0645 \u0627\u0644\
      \u0635\u0631\u0641 \u0627\u0644\u0635\u062D\u064A \u0628\u0627\u0644\u0623\u0646\
      \u0627\u0628\u064A\u0628"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: IRQ-SAN-17
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit (latrine)
    national_label_local: "\u0644\u0644\u062D\u0641\u0631"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: IRQ-SAN-18
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: "\u0644\u062E\u0632\u0627\u0646 \u0627\u0644\u0635\u0631\
      \u0641 \u0627\u0644\u0635\u062D\u064A"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: IRQ-SAN-19
    source_category_code: flush_pour_flush_to_pit_latrine_septic_tank
    national_label_en: Flush/pour flush to pit latrine (septic tank)
    national_label_local: "\u0644\u062E\u0632\u0627\u0646 \u0627\u0644\u0635\u0631\
      \u0641 \u0627\u0644\u0635\u062D\u064A"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: IRQ-SAN-20
    source_category_code: flush_to_unknown_place_not_sure_dk_where
    national_label_en: Flush to unknown place/not sure/DK where
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u063A\u064A\
      \u0631 \u0645\u0639\u0631\u0648\u0641 / \u0644\u0633\u062A \u0645\u062A\u0623\
      \u0643\u062F\u064B\u0627 / \u0644\u0627 \u0623\u0639\u0631\u0641"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: IRQ-SAN-21
    source_category_code: flush_pour_flush_to_don_t_know_where
    national_label_en: Flush/pour flush to don't know where
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u063A\u064A\
      \u0631 \u0645\u0639\u0631\u0648\u0641 / \u0644\u0633\u062A \u0645\u062A\u0623\
      \u0643\u062F\u064B\u0627 / \u0644\u0627 \u0623\u0639\u0631\u0641"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: IRQ-SAN-22
    source_category_code: bucket
    national_label_en: Bucket
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062F\u0644\u0648"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: IRQ-SAN-23
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet/hanging latrine
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
  - country_entry_id: IRQ-SAN-24
    source_category_code: improved_pit_latrine
    national_label_en: Improved pit latrine
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
  - country_entry_id: IRQ-SAN-25
    source_category_code: pit_latirne_with_slab
    national_label_en: Pit latirne with slab
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
  - country_entry_id: IRQ-SAN-26
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
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
  - country_entry_id: IRQ-SAN-27
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated improved pit latrine
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
  - country_entry_id: IRQ-SAN-28
    source_category_code: open_pit
    national_label_en: Open pit
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
  - country_entry_id: IRQ-SAN-29
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
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
  - country_entry_id: IRQ-SAN-30
    source_category_code: traditional_pit_latrine
    national_label_en: Traditional pit latrine*
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
  - country_entry_id: IRQ-SAN-31
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
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
  - country_entry_id: IRQ-SAN-32
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit latrine (VIP)
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
  - country_entry_id: IRQ-SAN-33
    source_category_code: non_flush_toilet_inside_outside_dwelling_exclusive_use_of_the_household
    national_label_en: non Flush toilet, inside/outside dwelling exclusive use of
      the household
    national_label_local: "\u0627\u0644\u0645\u0631\u0627\u062D\u064A\u0636 \u0627\
      \u0644\u062A\u0642\u0644\u064A\u062F\u064A\u0629"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 115
  - country_entry_id: IRQ-SAN-34
    source_category_code: non_flush_toilet_inside_outside_dwelling_exclusive_and_shared
    national_label_en: non Flush toilet, inside/outside dwelling exclusive and shared
    national_label_local: "\u0627\u0644\u0645\u0631\u0627\u062D\u064A\u0636 \u0627\
      \u0644\u062A\u0642\u0644\u064A\u062F\u064A\u0629"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: true
    source_row: 123
  - country_entry_id: IRQ-SAN-35
    source_category_code: pour_flush_latrine
    national_label_en: Pour flush latrine
    national_label_local: "\u0635\u0628 \u0627\u0644\u0645\u0631\u0627\u062D\u064A\
      \u0636 \u0627\u0644\u0645\u062A\u062F\u0641\u0642\u0629"
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 85
  - country_entry_id: IRQ-SAN-36
    source_category_code: no_facilities_or_bush_or_field
    national_label_en: No facilities or bush or field
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: IRQ-SAN-37
    source_category_code: no_facilities_bush_field
    national_label_en: No facilities/bush field
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: IRQ-SAN-38
    source_category_code: no_toilet
    national_label_en: No toilet
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: IRQ-SAN-39
    source_category_code: open_defecation_no_facility_bush_field
    national_label_en: Open defecation (no facility, bush, field)
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: IRQ-SAN-40
    source_category_code: other
    national_label_en: other
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: IRQ-SAN-41
    source_category_code: use_of_other_facility
    national_label_en: Use of other facility
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: IRQ-SAN-42
    source_category_code: other
    national_label_en: other
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_IRQ_Iraq_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: IRQ-WAS-01
    source_category_code: spring
    national_label_en: Spring
    national_label_local: "\u0643\u0644 \u0627\u0644\u064A\u0646\u0627\u0628\u064A\
      \u0639"
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 74
  - country_entry_id: IRQ-WAS-02
    source_category_code: kehriz_man_built_spring
    national_label_en: Kehriz (man built spring)
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Ground water > All springs > Other
    jmp_id: ground_water.all_springs.other
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 77
  - country_entry_id: IRQ-WAS-03
    source_category_code: open_well_covered_well
    national_label_en: open well / covered well
    national_label_local: "\u0643\u0644 \u0627\u0644\u0622\u0628\u0627\u0631"
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 54
  - country_entry_id: IRQ-WAS-04
    source_category_code: open_well_covered_well
    national_label_en: Open well/Covered well
    national_label_local: "\u0643\u0644 \u0627\u0644\u0622\u0628\u0627\u0631"
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 54
  - country_entry_id: IRQ-WAS-05
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
  - country_entry_id: IRQ-WAS-06
    source_category_code: protected_dug_well
    national_label_en: Protected dug well
    national_label_local: "\u0645\u062D\u0645\u064A \u0628\u0634\u0643\u0644 \u062C\
      \u064A\u062F"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: IRQ-WAS-07
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
  - country_entry_id: IRQ-WAS-08
    source_category_code: tube_well_bore_hole
    national_label_en: Tube well / bore-hole
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: IRQ-WAS-09
    source_category_code: tube_well_borehole_with_pump
    national_label_en: Tube well/Borehole with pump
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: IRQ-WAS-10
    source_category_code: tubewell_borehole
    national_label_en: Tubewell, borehole
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: IRQ-WAS-11
    source_category_code: tubewell_borehole
    national_label_en: Tubewell/borehole
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: IRQ-WAS-12
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
  - country_entry_id: IRQ-WAS-13
    source_category_code: unprotected_dug_well
    national_label_en: unprotected dug well
    national_label_local: "\u0628\u0626\u0631 \u063A\u064A\u0631 \u0645\u062D\u0645\
      \u064A"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: IRQ-WAS-14
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
  - country_entry_id: IRQ-WAS-15
    source_category_code: cart_with_small_tank
    national_label_en: Cart with small tank
    national_label_local: "\u0639\u0631\u0628\u0629 \u0645\u0639 \u062E\u0632\u0627\
      \u0646 \u0635\u063A\u064A\u0631 / \u0623\u0633\u0637\u0648\u0627\u0646\u0629"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: IRQ-WAS-16
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank/drum
    national_label_local: "\u0639\u0631\u0628\u0629 \u0645\u0639 \u062E\u0632\u0627\
      \u0646 \u0635\u063A\u064A\u0631 / \u0623\u0633\u0637\u0648\u0627\u0646\u0629"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: IRQ-WAS-17
    source_category_code: cart_with_tank_drum
    national_label_en: Cart with tank / drum
    national_label_local: "\u0639\u0631\u0628\u0629 \u0645\u0639 \u062E\u0632\u0627\
      \u0646 \u0635\u063A\u064A\u0631 / \u0623\u0633\u0637\u0648\u0627\u0646\u0629"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: IRQ-WAS-18
    source_category_code: reverse_osmosis
    national_label_en: Reverse Osmosis
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: IRQ-WAS-19
    source_category_code: water_kiosk
    national_label_en: Water kiosk
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: IRQ-WAS-20
    source_category_code: desalinized_water_and_sterilized_water
    national_label_en: Desalinized water and sterilized water
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 104
  - country_entry_id: IRQ-WAS-21
    source_category_code: tanker
    national_label_en: Tanker
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: IRQ-WAS-22
    source_category_code: tanker_truck
    national_label_en: Tanker Truck
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: IRQ-WAS-23
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker truck, vendor
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: IRQ-WAS-24
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
  - country_entry_id: IRQ-WAS-25
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
  - country_entry_id: IRQ-WAS-26
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
  - country_entry_id: IRQ-WAS-27
    source_category_code: bottled_water_big_small
    national_label_en: Bottled water (big/small)
    national_label_local: "\u0645\u064A\u0627\u0647 \u0645\u0639\u0628\u0623\u0629"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: IRQ-WAS-28
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "\u0643\u064A\u0633 \u0645\u0627\u0621"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: IRQ-WAS-29
    source_category_code: bottled_water_without_other_improved
    national_label_en: Bottled Water (without other improved)
    national_label_local: "\u0643\u064A\u0633 \u0645\u0627\u0621"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: IRQ-WAS-30
    source_category_code: rain_water_collection
    national_label_en: Rain water collection
    national_label_local: "\u062E\u0632\u0627\u0646 / \u062E\u0632\u0627\u0646 \u0645\
      \u063A\u0637\u0649"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: IRQ-WAS-31
    source_category_code: rain_water
    national_label_en: Rain-water
    national_label_local: "\u062E\u0632\u0627\u0646 / \u062E\u0632\u0627\u0646 \u0645\
      \u063A\u0637\u0649"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: IRQ-WAS-32
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: "\u062E\u0632\u0627\u0646 / \u062E\u0632\u0627\u0646 \u0645\
      \u063A\u0637\u0649"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: IRQ-WAS-33
    source_category_code: pond_river_or_stream
    national_label_en: Pond, river, or stream
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: IRQ-WAS-34
    source_category_code: river_canal_creek_wheel
    national_label_en: river/canal/creek/ wheel
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: IRQ-WAS-35
    source_category_code: river_canal_creek_wheel
    national_label_en: River/Canal/creek/Wheel
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: IRQ-WAS-36
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
  - country_entry_id: IRQ-WAS-37
    source_category_code: pond_lake
    national_label_en: Pond/lake
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Surface water > Other
    jmp_id: surface_water.other
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 99
  - country_entry_id: IRQ-WAS-38
    source_category_code: piped_to_neigbhour
    national_label_en: Piped to neigbhour
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: IRQ-WAS-39
    source_category_code: piped_water_to_neighbour
    national_label_en: Piped water to neighbour
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: IRQ-WAS-40
    source_category_code: hh_directly_linked_to_the_water_network
    national_label_en: HH directly linked to the water network
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: IRQ-WAS-41
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
  - country_entry_id: IRQ-WAS-42
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: IRQ-WAS-43
    source_category_code: public_network_housing_unit_connected
    national_label_en: 'Public network: housing unit connected'
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: IRQ-WAS-44
    source_category_code: piped_into_the_yard_or_plot
    national_label_en: Piped into the yard or plot
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
  - country_entry_id: IRQ-WAS-45
    source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
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
  - country_entry_id: IRQ-WAS-46
    source_category_code: piped_water_into_yard_plot
    national_label_en: Piped water into yard/plot
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
  - country_entry_id: IRQ-WAS-47
    source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
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
  - country_entry_id: IRQ-WAS-48
    source_category_code: public_network_tap
    national_label_en: Public network tap
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
  - country_entry_id: IRQ-WAS-49
    source_category_code: pubic_network_tap
    national_label_en: pubic network tap
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
  - country_entry_id: IRQ-WAS-50
    source_category_code: public_tap
    national_label_en: Public tap
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
  - country_entry_id: IRQ-WAS-51
    source_category_code: public_tap_stand_pipe
    national_label_en: Public tap / stand-pipe
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
  - country_entry_id: IRQ-WAS-52
    source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
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
  - country_entry_id: IRQ-WAS-53
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_IRQ_Iraq_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

