---
country_id: CTY-DZA
iso3: DZA
schema_version: '0.2'
status: draft
country_name: DZA
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: DZA-EDU-01
    national_label_en: "\xC9ducation  pr\xE9paratoire"
    national_label_local: "\u0627\u0644\u062A\u0631\u0628\u064A\u0629 \u0627\u0644\
      \u062A\u062D\u0636\u064A\u0631\u064A\u0629"
    entry_age: 5
    duration_years: 1
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
  - country_entry_id: DZA-EDU-02
    national_label_en: Enseignement primaire
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0627\u0628\u062A\u062F\u0627\u0626\u064A"
    entry_age: 6
    duration_years: 5
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 5
    cum_years_computation_path:
    - DZA-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: DZA-EDU-03
    national_label_en: Enseignement moyen
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0645\u062A\u0648\u0633\u0637"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - DZA-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: DZA-EDU-04
    national_label_en: "Formation professionnelle sp\xE9cialis\xE9 (CFPS)"
    national_label_local: "\u0627\u0644\u062A\u0643\u0648\u064A\u0646 \u0627\u0644\
      \u0645\u0647\u0646\u064A \u0627\u0644\u0645\u062E\u062A\u0635"
    entry_age: 11
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - DZA-EDU-02
    cum_years_schooling: 6
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: DZA-EDU-05
    national_label_en: Formation d'aptitude professionnelle
    national_label_local: "\u0627\u0644\u062A\u0643\u0648\u064A\u0646 \u0627\u0644\
      \u0645\u0647\u0627\u0631\u0629 \u0627\u0644\u0645\u0647\u0646\u064A\u0629"
    entry_age: 11
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - DZA-EDU-02
    cum_years_schooling: 6
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: DZA-EDU-06
    national_label_en: Formation de maitrise professionnelle
    national_label_local: "\u0627\u0644\u062A\u0643\u0648\u064A\u0646 \u0627\u0644\
      \u062A\u062D\u0643\u0645 \u0627\u0644\u0645\u0647\u0646\u064A"
    entry_age: 16
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - DZA-EDU-02
    cum_years_schooling: 7
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: DZA-EDU-07
    national_label_en: "Enseignement secondaire g\xE9n\xE9ral et technologique"
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A \u0627\u0644\u0639\u0627\u0645 \u0648\u0627\u0644\
      \u062A\u0643\u0646\u0648\u0644\u0648\u062C\u064A"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - DZA-EDU-03
    - DZA-EDU-04
    - DZA-EDU-05
    - DZA-EDU-06
    cum_years_schooling: 9
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
  - country_entry_id: DZA-EDU-08
    national_label_en: Enseignement professionnel
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0645\u0647\u0646\u064A"
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - DZA-EDU-03
    - DZA-EDU-04
    - DZA-EDU-05
    - DZA-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
  - country_entry_id: DZA-EDU-09
    national_label_en: "Brevet de technicien sup\xE9rieur"
    national_label_local: "\u0634\u0647\u0627\u062F\u0629 \u062A\u0642\u0646\u064A\
      \ \u0633\u0627\u0645\u064A"
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-10
    national_label_en: "Formation professeur  \xE0 l'enseignement  primaire"
    national_label_local: "\u062A\u0643\u0648\u064A\u0646 \u0623\u0633\u0627\u062A\
      \u0630\u0629 \u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\u0627\u0628\
      \u062A\u062F\u0627\u0626\u064A"
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-11
    national_label_en: Licence
    national_label_local: "\u0644\u064A\u0633\u0627\u0646\u0633"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-12
    national_label_en: "Formation de professeur \xE0 l'enseignement moyen"
    national_label_local: "\u062A\u0643\u0648\u064A\u0646 \u0623\u0633\u0627\u062A\
      \u0630\u0629 \u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\u0645\u062A\
      \u0648\u0633\u0637"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-13
    national_label_en: "Cycle pr\xE9paratoire"
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u062A\u062D\u0636\u064A\u0631\u064A\u0629"
    entry_age: 18
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 10
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-14
    national_label_en: "Master sp\xE9cialis\xE9"
    national_label_local: "\u0645\u0627\u0633\u062A\u0631 \u0645\u062A\u062E\u0635\
      \u0635"
    entry_age: 20
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - DZA-EDU-11
    - DZA-EDU-12
    cum_years_schooling: 14
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-11
    - DZA-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
    - 'minimum parent path selected from: DZA-EDU-11, DZA-EDU-12'
  - country_entry_id: DZA-EDU-15
    national_label_en: "Formation de professeur \xE0 l'enseignement secondaire"
    national_label_local: "\u062A\u0643\u0648\u064A\u0646 \u0623\u0633\u0627\u062A\
      \u0630\u0629 \u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\u062B\u0627\
      \u0646\u0648\u064A"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-16
    national_label_en: "\xC9tudes sup\xE9rieur sp\xE9cialis\xE9es de 6ans v\xE9t\xE9\
      rinaires, de dentisterie et de pharmacie"
    national_label_local: "\u062F\u0631\u0627\u0633\u0627\u062A \u0637\u0628\u064A\
      \u0629 \u0645\u062A\u062E\u0635\u0635\u0629 (\u0627\u0644\u0628\u064A\u0637\u0631\
      \u0629\u060C \u0637\u0628\u064A\u0628 \u0627\u0644\u0623\u0633\u0646\u0627\u0646\
      \ \u0648\u0627\u0644\u0635\u064A\u062F\u0644\u0629)-6 \u0633\u0646\u0648\u0627\
      \u062A"
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 14
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-17
    national_label_en: "\xC9tudes en m\xE9decine"
    national_label_local: "\u062F\u0631\u0627\u0633\u0627\u062A \u0637\u0628\u064A\
      \u0629"
    entry_age: 18
    duration_years: 7
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 15
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-18
    national_label_en: "Ing\xE9nieur d'\xE9tat"
    national_label_local: "\u0645\u0647\u0646\u062F\u0633 \u062F\u0648\u0644\u0629"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-19
    national_label_en: "\xC9tudes sup\xE9rieur sp\xE9cialis\xE9es v\xE9t\xE9rinaires\
      \ de 5ans, de dentisterie et de pharmacie"
    national_label_local: "\u062F\u0631\u0627\u0633\u0627\u062A \u0637\u0628\u064A\
      \u0629 \u0645\u062A\u062E\u0635\u0635\u0629-5 \u0633\u0646\u0648\u0627\u062A\
      \ (\u0627\u0644\u0628\u064A\u0637\u0631\u0629\u060C \u0637\u0628\u064A\u0628\
      \ \u0627\u0644\u0623\u0633\u0646\u0627\u0646 \u0648\u0627\u0644\u0635\u064A\u062F\
      \u0644\u0629)"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-20
    national_label_en: Master
    national_label_local: "\u0645\u0627\u0633\u062A\u0631"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - DZA-EDU-11
    - DZA-EDU-12
    cum_years_schooling: 13
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-11
    - DZA-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
    - 'minimum parent path selected from: DZA-EDU-11, DZA-EDU-12'
  - country_entry_id: DZA-EDU-21
    national_label_en: "6\xE8me ann\xE9e transitoire en vue de l'obtention du dipl\xF4\
      me de docteur Pharmacien"
    national_label_local: "\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u0633\u0627\
      \u062F\u0633\u0629 \u0627\u0646\u062A\u0642\u0627\u0644\u064A\u0629 \u0644\u0646\
      \u064A\u0644 \u0634\u0647\u0627\u062F\u0629 \u062F\u0643\u062A\u0648\u0631 \u0641\
      \u064A \u0627\u0644\u0635\u064A\u062F\u0644\u0629"
    entry_age: 23
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - DZA-EDU-07
    - DZA-EDU-08
    cum_years_schooling: 9
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
  - country_entry_id: DZA-EDU-22
    national_label_en: Doctorat
    national_label_local: "\u062F\u0643\u062A\u0648\u0631\u0627\u0647"
    entry_age: 23
    duration_years: 5
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - DZA-EDU-13
    - DZA-EDU-14
    - DZA-EDU-15
    - DZA-EDU-16
    - DZA-EDU-17
    - DZA-EDU-18
    - DZA-EDU-19
    - DZA-EDU-20
    - DZA-EDU-21
    cum_years_schooling: 14
    cum_years_computation_path:
    - DZA-EDU-02
    - DZA-EDU-04
    - DZA-EDU-08
    - DZA-EDU-21
    - DZA-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: DZA-EDU-03, DZA-EDU-04, DZA-EDU-05, DZA-EDU-06'
    - 'minimum parent path selected from: DZA-EDU-07, DZA-EDU-08'
    - 'minimum parent path selected from: DZA-EDU-13, DZA-EDU-14, DZA-EDU-15, DZA-EDU-16,
      DZA-EDU-17, DZA-EDU-18, DZA-EDU-19, DZA-EDU-20, DZA-EDU-21'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Algerie.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: DZA-SAN-01
    source_category_code: toilette_a_compostage
    national_label_en: Toilette a compostage
    national_label_local: "\u0645\u0631\u0627\u062D\u064A\u0636 \u0627\u0644\u062A\
      \u0633\u0645\u064A\u062F"
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: DZA-SAN-02
    source_category_code: toilettes_a_compostage
    national_label_en: "Toilettes \xE0 compostage"
    national_label_local: "\u0645\u0631\u0627\u062D\u064A\u0636 \u0627\u0644\u062A\
      \u0633\u0645\u064A\u062F"
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: DZA-SAN-03
    source_category_code: chasse_reliee_a_autre_chose
    national_label_en: "Chasse reli\xE9e \xE0 autre chose"
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: DZA-SAN-04
    source_category_code: reliee_a_autre_chose_a_un_oued_a_l_aire_libre
    national_label_en: "Reli\xE9e a autre chose/ a un oued/ a l'aire libre"
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: DZA-SAN-05
    source_category_code: chasse_connectee_a_systeme_d_egouts
    national_label_en: "Chasse connect\xE9e \xE0 syst\xE8me d'\xE9gouts"
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
  - country_entry_id: DZA-SAN-06
    source_category_code: reliee_a_sisteme_d_egouts
    national_label_en: "Reli\xE9e a sisteme d'egouts"
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
  - country_entry_id: DZA-SAN-07
    source_category_code: chasse_reliee_a_des_latrines
    national_label_en: "Chasse reli\xE9e \xE0 des latrines"
    national_label_local: "\u0644\u0644\u062D\u0641\u0631"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: DZA-SAN-08
    source_category_code: reliee_aux_latrines
    national_label_en: "Reli\xE9e aux latrines"
    national_label_local: "\u0644\u0644\u062D\u0641\u0631"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: DZA-SAN-09
    source_category_code: chasse_connectee_a_fosse_septique
    national_label_en: "Chasse connect\xE9e \xE0 fosse septique"
    national_label_local: "\u0644\u062E\u0632\u0627\u0646 \u0627\u0644\u0635\u0631\
      \u0641 \u0627\u0644\u0635\u062D\u064A"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: DZA-SAN-10
    source_category_code: reliee_a_fosse_septique
    national_label_en: "Reli\xE9e a fosse septique"
    national_label_local: "\u0644\u062E\u0632\u0627\u0646 \u0627\u0644\u0635\u0631\
      \u0641 \u0627\u0644\u0635\u062D\u064A"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: DZA-SAN-11
    source_category_code: chasse_reliee_a_endroit_inconnu_passee_nsp
    national_label_en: "Chasse reli\xE9e \xE0 endroit inconnu / Pass\xE9e / NSP"
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
  - country_entry_id: DZA-SAN-12
    source_category_code: seau
    national_label_en: Seau
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062F\u0644\u0648"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: DZA-SAN-13
    source_category_code: seaux
    national_label_en: Seaux
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062F\u0644\u0648"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: DZA-SAN-14
    source_category_code: toilettes_latrines_suspendues
    national_label_en: Toilettes / Latrines suspendues
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
  - country_entry_id: DZA-SAN-15
    source_category_code: toilettes_suspendues_latrines_suspendues
    national_label_en: Toilettes suspendues/latrines suspendues
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
  - country_entry_id: DZA-SAN-16
    source_category_code: latrine_a_fosse_avec_dalle
    national_label_en: Latrine a fosse avec dalle
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
  - country_entry_id: DZA-SAN-17
    source_category_code: latrines_a_fosse_avec_dalle
    national_label_en: "Latrines \xE0 fosse avec dalle"
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
  - country_entry_id: DZA-SAN-18
    source_category_code: latrine_a_fosse_sans_dalle_fosse_ouverte
    national_label_en: Latrine a fosse sans dalle/fosse ouverte
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
  - country_entry_id: DZA-SAN-19
    source_category_code: latrines_a_fosse_sans_dalle_trou_ouvert
    national_label_en: "Latrines  \xE0 fosse sans dalle / trou ouvert"
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
  - country_entry_id: DZA-SAN-20
    source_category_code: latrine_a_fosse_amelioree_ventilee
    national_label_en: "Latrine a fosse amelior\xE9e ventil\xE9e"
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
  - country_entry_id: DZA-SAN-21
    source_category_code: latrines_ameliorees_ventilees_lav
    national_label_en: "Latrines am\xE9lior\xE9es ventil\xE9es (LAV)"
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
  - country_entry_id: DZA-SAN-22
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
  - country_entry_id: DZA-SAN-23
    source_category_code: pas_de_toilettes_nature_plein_air
    national_label_en: Pas de toilettes/nature/plein air
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: DZA-SAN-24
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
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_DZA_Algeria_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: DZA-WAS-01
    source_category_code: source_protegee
    national_label_en: "Source prot\xE9g\xE9e"
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u0627\u0644\u0645\u062D\
      \u0645\u064A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: DZA-WAS-02
    source_category_code: source_protegee
    national_label_en: "Source:proteg\xE9e"
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u0627\u0644\u0645\u062D\
      \u0645\u064A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: DZA-WAS-03
    source_category_code: puits_creuse_protege
    national_label_en: "Puits creuse: proteg\xE9"
    national_label_local: "\u0645\u062D\u0645\u064A \u0628\u0634\u0643\u0644 \u062C\
      \u064A\u062F"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: DZA-WAS-04
    source_category_code: puits_proteges
    national_label_en: "Puits prot\xE9g\xE9s"
    national_label_local: "\u0645\u062D\u0645\u064A \u0628\u0634\u0643\u0644 \u062C\
      \u064A\u062F"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: DZA-WAS-05
    source_category_code: puits_a_pompe_forage
    national_label_en: "Puits \xE0 pompe, forage"
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: DZA-WAS-06
    source_category_code: puits_a_pompe_forage
    national_label_en: Puits a pompe/forage
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: DZA-WAS-07
    source_category_code: source_non_protegee
    national_label_en: "Source non prot\xE9g\xE9e"
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u063A\u064A\u0631 \u0627\
      \u0644\u0645\u062D\u0645\u064A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: DZA-WAS-08
    source_category_code: source_pas_protegee
    national_label_en: "Source: pas proteg\xE9e"
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u063A\u064A\u0631 \u0627\
      \u0644\u0645\u062D\u0645\u064A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: DZA-WAS-09
    source_category_code: puits_creuse_pas_protege
    national_label_en: "Puits creuse: pas proteg\xE9"
    national_label_local: "\u0628\u0626\u0631 \u063A\u064A\u0631 \u0645\u062D\u0645\
      \u064A"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: DZA-WAS-10
    source_category_code: puits_non_proteges
    national_label_en: "Puits non prot\xE9g\xE9s"
    national_label_local: "\u0628\u0626\u0631 \u063A\u064A\u0631 \u0645\u062D\u0645\
      \u064A"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: DZA-WAS-11
    source_category_code: camion_citerne
    national_label_en: Camion citerne
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: DZA-WAS-12
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
  - country_entry_id: DZA-WAS-13
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
  - country_entry_id: DZA-WAS-14
    source_category_code: eau_conditionee_eau_en_bouteille
    national_label_en: "Eau condition\xE9e: eau en bouteille"
    national_label_local: "\u0645\u064A\u0627\u0647 \u0645\u0639\u0628\u0623\u0629"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: DZA-WAS-15
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
  - country_entry_id: DZA-WAS-16
    source_category_code: eau_en_bouteille
    national_label_en: Eau en bouteille
    national_label_local: "\u0643\u064A\u0633 \u0645\u0627\u0621"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: DZA-WAS-17
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
  - country_entry_id: DZA-WAS-18
    source_category_code: eau_de_surface_oued_lac_barrage
    national_label_en: Eau de surface (oued, lac, barrage)
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: DZA-WAS-19
    source_category_code: eau_de_surface_riviere_fleuve_barrage_lac_mare_canal_canal
    national_label_en: "Eau de surface (rivi\xE8re, fleuve, barrage, lac, mare, canal,\
      \ canal"
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: DZA-WAS-20
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
  - country_entry_id: DZA-WAS-21
    source_category_code: robinet_chez_le_voisin
    national_label_en: 'Robinet: chez le voisin'
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: DZA-WAS-22
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
  - country_entry_id: DZA-WAS-23
    source_category_code: robinet_dans_le_logement
    national_label_en: 'Robinet: dans le logement'
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: DZA-WAS-24
    source_category_code: robinet_dans_quartier_cour_ou_parcelle
    national_label_en: Robinet dans quartier, cour ou parcelle
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
  - country_entry_id: DZA-WAS-25
    source_category_code: robinet_dans_la_cour_jardin_pacelle
    national_label_en: 'Robinet: dans la cour/jardin/pacelle'
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
  - country_entry_id: DZA-WAS-26
    source_category_code: robinet_public_borne_fontaine
    national_label_en: Robinet public / borne fontaine
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
  - country_entry_id: DZA-WAS-27
    source_category_code: robinet_robinet_public_borne_fontaine
    national_label_en: 'Robinet: robinet public/borne fontaine'
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_DZA_Algeria_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

