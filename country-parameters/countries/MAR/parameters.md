---
country_id: CTY-MAR
country_name: Morocco
iso3: MAR
schema_version: '0.1'
status: draft
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MAR-EDU-01
    national_label_en: "\xC9ducation de la petite enfance"
    national_label_local: "\u062A\u0646\u0645\u064A\u0629 \u0627\u0644\u0637\u0641\
      \u0648\u0644\u0629 \u0627\u0644\u0645\u0628\u0643\u0631\u0629"
    entry_age: 1
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
  - country_entry_id: MAR-EDU-02
    national_label_en: "Enseignement pr\xE9scolaire"
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0642\u0628\
      \u0644 \u0627\u0644\u0645\u062F\u0631\u0633\u064A"
    entry_age: 4
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
  - country_entry_id: MAR-EDU-03
    national_label_en: Enseignement primaire
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0627\u0628\u062A\u062F\u0627\u0626\u064A"
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
    - MAR-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: MAR-EDU-04
    national_label_en: "Enseignement secondaire coll\xE9gial"
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A \u0627\u0644\u0625\u0639\u062F\u0627\u062F\u064A"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - MAR-EDU-03
    cum_years_schooling: 9
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAR-EDU-05
    national_label_en: "Formation professionnelle / Sp\xE9cialisation"
    national_label_local: "\u0627\u0644\u062A\u0643\u0648\u064A\u0646 \u0627\u0644\
      \u0645\u0647\u0646\u064A: \u0645\u0633\u062A\u0648\u0649 \u0627\u0644\u062A\u062E\
      \u0635\u0635"
    entry_age: 15
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - MAR-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MAR-EDU-06
    national_label_en: "Secondaire qualifiant g\xE9n\xE9ral"
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A \u0627\u0644\u062A\u0623\u0647\u064A\u0644\u064A"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - MAR-EDU-04
    - MAR-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
  - country_entry_id: MAR-EDU-07
    national_label_en: Formation professionnelle / Qualification
    national_label_local: "\u0627\u0644\u062A\u0643\u0648\u064A\u0646 \u0627\u0644\
      \u0645\u0647\u0646\u064A- \u0645\u0633\u062A\u0648\u0649 \u0627\u0644\u062A\u0623\
      \u0647\u064A\u0644"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - MAR-EDU-04
    - MAR-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
  - country_entry_id: MAR-EDU-08
    national_label_en: Enseignement technique et professionnel
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u062A\u0642\u0646\u064A \u0648\u0627\u0644\u0645\u0647\u0646\u064A"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - MAR-EDU-04
    - MAR-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
  - country_entry_id: MAR-EDU-09
    national_label_en: Formation professionnelle / Technicien
    national_label_local: "\u0627\u0644\u062A\u0643\u0648\u064A\u0646 \u0627\u0644\
      \u0645\u0647\u0646\u064A - \u0645\u0633\u062A\u0648\u0649 \u0641\u0646\u064A"
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-10
    national_label_en: "Formation professionnelle / Technicien sup\xE9rieur"
    national_label_local: "\u0627\u0644\u062A\u0643\u0648\u064A\u0646 \u0627\u0644\
      \u0645\u0647\u0646\u064A - \u0645\u0633\u062A\u0648\u0649 \u0627\u0644\u062A\
      \u0642\u0646\u064A \u0627\u0644\u0639\u0627\u0644\u064A"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-11
    national_label_en: "Formation professionnelle / Technicien sp\xE9cialis\xE9"
    national_label_local: "\u0645\u0633\u062A\u0648\u0649 \u0627\u0644\u062A\u0642\
      \u0646\u064A \u0627\u0644\u0645\u062A\u062E\u0635\u0635"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-12
    national_label_en: "Dipl\xF4me Universitaire de Technologie"
    national_label_local: "\u0627\u0644\u062F\u0628\u0644\u0648\u0645 \u0627\u0644\
      \u062C\u0627\u0645\u0639\u064A \u0641\u064A \u0627\u0644\u062A\u0643\u0646\u0648\
      \u0644\u0648\u062C\u064A\u0627"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-13
    national_label_en: Licence professionnelle (LP)
    national_label_local: "\u0627\u0644\u0625\u062C\u0627\u0632\u0629 \u0627\u0644\
      \u0645\u0647\u0646\u064A\u0629"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-14
    national_label_en: Licence sciences et technique (LST)
    national_label_local: "\u0625\u062C\u0627\u0632\u0629 \u0627\u0644\u0639\u0644\
      \u0648\u0645 \u0648 \u0627\u0644\u062A\u0642\u0646\u064A\u0629"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-15
    national_label_en: "Licence d'\xE9tudes fondamentales (LEF)"
    national_label_local: "\u0625\u062C\u0627\u0632\u0629 \u0627\u0644\u062F\u0631\
      \u0627\u0633\u0627\u062A \u0627\u0644\u0623\u0633\u0627\u0633\u064A\u0629"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-16
    national_label_en: Formation des instituteurs du primaire
    national_label_local: "\u062A\u0643\u0648\u064A\u0646 \u0623\u0633\u0627\u062A\
      \u0630\u0629 \u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\u0627\u0628\
      \u062A\u062F\u0627\u0626\u064A"
    entry_age: 21
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-17
    national_label_en: "Formation des enseignants du secondaire coll\xE9gial"
    national_label_local: "\u062A\u0643\u0648\u064A\u0646 \u0623\u0633\u0627\u062A\
      \u0630\u0629 \u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\u062B\u0627\
      \u0646\u0648\u064A \u0627\u0644\u0625\u0639\u062F\u0627\u062F\u064A"
    entry_age: 21
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-18
    national_label_en: Formation des enseignants du secondaire
    national_label_local: "\u062A\u0643\u0648\u064A\u0646 \u0623\u0633\u0627\u062A\
      \u0630\u0629 \u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\u062B\u0627\
      \u0646\u0648\u064A"
    entry_age: 21
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-19
    national_label_en: "M\xE9decine dentaire"
    national_label_local: "\u0637\u0628 \u0627\u0644\u0623\u0633\u0646\u0627\u0646"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 15
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-20
    national_label_en: "Sciences de l'ing\xE9nieur"
    national_label_local: "\u0639\u0644\u0648\u0645 \u0627\u0644\u0645\u0647\u0646\
      \u062F\u0633"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 15
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-21
    national_label_en: Pharmacie
    national_label_local: "\u0627\u0644\u0635\u064A\u062F\u0644\u0629"
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 16
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-22
    national_label_en: "M\xE9decine"
    national_label_local: "\u0627\u0644\u0637\u0628"
    entry_age: 18
    duration_years: 7
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 17
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-23
    national_label_en: Programmes de master
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0645\u0627\
      \u0633\u062A\u0631"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - MAR-EDU-13
    - MAR-EDU-14
    - MAR-EDU-15
    - MAR-EDU-16
    - MAR-EDU-17
    - MAR-EDU-18
    cum_years_schooling: 13
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-16
    - MAR-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
    - 'minimum parent path selected from: MAR-EDU-13, MAR-EDU-14, MAR-EDU-15, MAR-EDU-16,
      MAR-EDU-17, MAR-EDU-18'
  - country_entry_id: MAR-EDU-24
    national_label_en: "Interpr\xE8te"
    national_label_local: "\u0627\u0644\u062A\u0631\u062C\u0645\u0629"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - MAR-EDU-06
    - MAR-EDU-07
    - MAR-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
  - country_entry_id: MAR-EDU-25
    national_label_en: "Sp\xE9cialit\xE9 en M\xE9decine Dentaire"
    national_label_local: "\u0627\u0644\u062A\u062E\u0635\u0635 \u0641\u064A \u0637\
      \u0628 \u0627\u0644\u0623\u0633\u0646\u0627\u0646"
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - MAR-EDU-19
    - MAR-EDU-20
    - MAR-EDU-21
    - MAR-EDU-22
    - MAR-EDU-23
    - MAR-EDU-24
    cum_years_schooling: 15
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-24
    - MAR-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
    - 'minimum parent path selected from: MAR-EDU-19, MAR-EDU-20, MAR-EDU-21, MAR-EDU-22,
      MAR-EDU-23, MAR-EDU-24'
  - country_entry_id: MAR-EDU-26
    national_label_en: "Sp\xE9cialit\xE9 en M\xE9decine"
    national_label_local: "\u0627\u0644\u062A\u062E\u0635\u0635 \u0641\u064A \u0627\
      \u0644\u0637\u0628"
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - MAR-EDU-19
    - MAR-EDU-20
    - MAR-EDU-21
    - MAR-EDU-22
    - MAR-EDU-23
    - MAR-EDU-24
    cum_years_schooling: 15
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-24
    - MAR-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
    - 'minimum parent path selected from: MAR-EDU-19, MAR-EDU-20, MAR-EDU-21, MAR-EDU-22,
      MAR-EDU-23, MAR-EDU-24'
  - country_entry_id: MAR-EDU-27
    national_label_en: "\xC9tude de Doctorat"
    national_label_local: "\u062F\u0631\u0627\u0633\u0627\u062A \u0627\u0644\u062F\
      \u0643\u062A\u0648\u0631\u0627\u0647"
    entry_age: 23
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - MAR-EDU-19
    - MAR-EDU-20
    - MAR-EDU-21
    - MAR-EDU-22
    - MAR-EDU-23
    - MAR-EDU-24
    cum_years_schooling: 15
    cum_years_computation_path:
    - MAR-EDU-03
    - MAR-EDU-05
    - MAR-EDU-07
    - MAR-EDU-24
    - MAR-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MAR-EDU-04, MAR-EDU-05'
    - 'minimum parent path selected from: MAR-EDU-06, MAR-EDU-07, MAR-EDU-08'
    - 'minimum parent path selected from: MAR-EDU-19, MAR-EDU-20, MAR-EDU-21, MAR-EDU-22,
      MAR-EDU-23, MAR-EDU-24'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Morocco.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: 2015
  selectors: null
  value:
  - country_entry_id: MAR-SUBNAT-01
    survey_labels: 1 - Regions sahariennes
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAULx_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAULx_1
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '1'
    geo_nvar: ADM1_NAME
    geo_name: "Guelmim - Es-Semara & La\xE2youne - Boujdour - Sakia El Hamra"
    source_row: 9231
  - country_entry_id: MAR-SUBNAT-02
    survey_labels: 10 - Tadla-Azilal
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_147336
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_147336
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147336'
    geo_nvar: ADM1_NAME
    geo_name: Tadla - Azilal
    source_row: 9232
  - country_entry_id: MAR-SUBNAT-03
    survey_labels: 11 - Meknes-Tafilalet
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_2107
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_2107
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2107'
    geo_nvar: ADM1_NAME
    geo_name: "Mekn\xE8s - Tafilalet"
    source_row: 9233
  - country_entry_id: MAR-SUBNAT-04
    survey_labels: 12 - Fes-Boulemane-Taounate
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAULx_12
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAULx_12
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '12'
    geo_nvar: ADM1_NAME
    geo_name: "F\xE8s - Boulemane & Taounate"
    source_row: 9234
  - country_entry_id: MAR-SUBNAT-05
    survey_labels: 13 - Taza-Hoceima
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAULx_13
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAULx_13
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '13'
    geo_nvar: ADM2_NAME
    geo_name: Taza & Al Hoceima
    source_row: 9235
  - country_entry_id: MAR-SUBNAT-06
    survey_labels: 14 - Tanger-Tetouan
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_147337
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_147337
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147337'
    geo_nvar: ADM1_NAME
    geo_name: "Tanger - T\xE9touan"
    source_row: 9236
  - country_entry_id: MAR-SUBNAT-07
    survey_labels: 2 - Souss- Massa-Draa
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_147335
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_147335
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147335'
    geo_nvar: ADM1_NAME
    geo_name: "Souss - Massa - Dra\xE2"
    source_row: 9237
  - country_entry_id: MAR-SUBNAT-08
    survey_labels: 3 - Gharb-Chrarda-Beni Hssen
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_147329
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_147329
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147329'
    geo_nvar: ADM1_NAME
    geo_name: "Gharb - Chrarda - B\xE9ni Hssen"
    source_row: 9238
  - country_entry_id: MAR-SUBNAT-09
    survey_labels: 4 - Chaouia-Ouardigha
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_147326
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_147326
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147326'
    geo_nvar: ADM1_NAME
    geo_name: Chaouia - Ouardigha
    source_row: 9239
  - country_entry_id: MAR-SUBNAT-10
    survey_labels: 5 - Marrakech-Tensift-Haouz
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_147333
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_147333
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147333'
    geo_nvar: ADM1_NAME
    geo_name: Marrakech - Tensift - Al Haouz
    source_row: 9240
  - country_entry_id: MAR-SUBNAT-11
    survey_labels: 6 - Oriental
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_2109
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_2109
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2109'
    geo_nvar: ADM1_NAME
    geo_name: Oriental
    source_row: 9241
  - country_entry_id: MAR-SUBNAT-12
    survey_labels: 7 - Grand Casablanca
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_147330
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_147330
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147330'
    geo_nvar: ADM1_NAME
    geo_name: Grand Casablanca
    source_row: 9242
  - country_entry_id: MAR-SUBNAT-13
    survey_labels: 8 -Rabat-Sale-Zemmour-Zaer
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_147334
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_147334
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147334'
    geo_nvar: ADM1_NAME
    geo_name: "Rabat - Sal\xE9 - Zemmour - Zaer"
    source_row: 9243
  - country_entry_id: MAR-SUBNAT-14
    survey_labels: 9 - Doukkala-Abda
    survey_variables: subnatid
    gmd_subnatid1: MAR_2015_GAUL1_147327
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2015_GAUL1_147327
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147327'
    geo_nvar: ADM1_NAME
    geo_name: Doukkala - Abda
    source_row: 9244
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2023
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MAR-SUBNAT-01
    survey_labels: 1 - Tanger-Tetouan-Al Hoceima
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA010
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA010
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA010
    geo_nvar: ADM1_FR
    geo_name: "Tanger-T\xE9touan-Al Hoceima"
    source_row: 9259
  - country_entry_id: MAR-SUBNAT-02
    survey_labels: 10 - Guelmim-Oued Noun
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA005
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA005
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA005
    geo_nvar: ADM1_FR
    geo_name: Guelmim-Oued Noun
    source_row: 9260
  - country_entry_id: MAR-SUBNAT-03
    survey_labels: 2 - Oriental
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA007
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA007
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA007
    geo_nvar: ADM1_FR
    geo_name: Oriental
    source_row: 9261
  - country_entry_id: MAR-SUBNAT-04
    survey_labels: "3 - Fes-M\xE9kn\xE8s"
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA004
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA004
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA004
    geo_nvar: ADM1_FR
    geo_name: "F\xE8s-Mekn\xE8s"
    source_row: 9262
  - country_entry_id: MAR-SUBNAT-05
    survey_labels: "4 - Rabat-Sal\xE9-Kenitra"
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA008
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA008
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA008
    geo_nvar: ADM1_FR
    geo_name: "Rabat-Sal\xE9-K\xE9nitra"
    source_row: 9263
  - country_entry_id: MAR-SUBNAT-06
    survey_labels: 5 - Beni Mellal-Khenifra
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA001
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA001
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA001
    geo_nvar: ADM1_FR
    geo_name: "B\xE9ni Mellal-Kh\xE9nifra"
    source_row: 9264
  - country_entry_id: MAR-SUBNAT-07
    survey_labels: 6 - Grand Casablanca
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA002
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA002
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA002
    geo_nvar: ADM1_FR
    geo_name: Grand Casablanca-Settat
    source_row: 9265
  - country_entry_id: MAR-SUBNAT-08
    survey_labels: 7 - Marrakech-Safi
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA006
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA006
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA006
    geo_nvar: ADM1_FR
    geo_name: Marrakech-Safi
    source_row: 9266
  - country_entry_id: MAR-SUBNAT-09
    survey_labels: 8 - Draa-Tafilalet
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA003
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA003
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA003
    geo_nvar: ADM1_FR
    geo_name: "Dr\xE2a-Tafilalet"
    source_row: 9267
  - country_entry_id: MAR-SUBNAT-10
    survey_labels: 9 - Souss-Massa
    survey_variables: subnatid
    gmd_subnatid1: MAR_2023_UN1_MA009
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MAR_2023_UN1_MA009
    geo_year: '2023'
    geo_source: UN
    geo_level: '1'
    geo_idvar: ADM1_PCODE
    geo_id: MA009
    geo_nvar: ADM1_FR
    geo_name: Souss-Massa
    source_row: 9268
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
  - country_entry_id: MAR-SAN-01
    source_category_code: chasse_branchee_a_d_autres_moyens
    national_label_en: "Chasse branche\u0301e a\u0300 d\u2019autres moyens"
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: MAR-SAN-02
    source_category_code: chasse_branchee_a_l_egout
    national_label_en: "Chasse branche\u0301e a\u0300 l'e\u0301gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: MAR-SAN-03
    source_category_code: toilette_avec_siphon_reliee_aux_egouts
    national_label_en: Toilette avec siphon reliee aux egouts
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: MAR-SAN-04
    source_category_code: chasse_branchee_a_latrine
    national_label_en: "Chasse branche\u0301e a\u0300 latrine"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: MAR-SAN-05
    source_category_code: toilette_avec_siphon_non_reliee_aux_egouts
    national_label_en: Toilette avec siphon non reliee aux egouts
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: MAR-SAN-06
    source_category_code: private_flush
    national_label_en: Private flush
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: MAR-SAN-07
    source_category_code: private_flush_inside
    national_label_en: Private flush inside
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: MAR-SAN-08
    source_category_code: toilette_a_l_interieur
    national_label_en: "Toilette \xE0 l'int\xE9rieur"
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: MAR-SAN-09
    source_category_code: wc_a_l_interieur_et_exterieur_prive
    national_label_en: "WC \xE0 l'int\xE9rieur et ext\xE9rieur priv\xE9"
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: MAR-SAN-10
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
  - country_entry_id: MAR-SAN-11
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
  - country_entry_id: MAR-SAN-12
    source_category_code: outdoor_collective_wc
    national_label_en: Outdoor Collective WC
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: MAR-SAN-13
    source_category_code: shared_flush
    national_label_en: Shared flush
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: MAR-SAN-14
    source_category_code: shared_flush_inside
    national_label_en: Shared flush inside
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: MAR-SAN-15
    source_category_code: toilette_publique
    national_label_en: Toilette publique
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: MAR-SAN-16
    source_category_code: toilettes_a_l_exterieur
    national_label_en: "Toilettes \xE0 l'ext\xE9rieur"
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: MAR-SAN-17
    source_category_code: wc_a_l_interieur_et_exterieur_collectif
    national_label_en: "WC \xE0 l'int\xE9rieur et ext\xE9rieur collectif"
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: MAR-SAN-18
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
  - country_entry_id: MAR-SAN-19
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
  - country_entry_id: MAR-SAN-20
    source_category_code: egout
    national_label_en: Egout
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: MAR-SAN-21
    source_category_code: toilette_branchee_aux_egouts
    national_label_en: "Toilette branch\xE9e aux \xE9gouts"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: MAR-SAN-22
    source_category_code: toilette_avec_siphone_non_branchee_aux_egouts
    national_label_en: "Toilette avec siphone non branch\xE9e aux \xE9gouts"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: MAR-SAN-23
    source_category_code: fosse_septique
    national_label_en: Fosse septique
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: MAR-SAN-24
    source_category_code: toilette_branchee_a_une_fosse_septique
    national_label_en: "Toilette branch\xE9e \xE0 une fosse s\xE9ptique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: MAR-SAN-25
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
  - country_entry_id: MAR-SAN-26
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
  - country_entry_id: MAR-SAN-27
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
  - country_entry_id: MAR-SAN-28
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
  - country_entry_id: MAR-SAN-29
    source_category_code: fosse_d_aisance_ou_latrine
    national_label_en: Fosse d aisance ou latrine
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MAR-SAN-30
    source_category_code: fosse_somaire
    national_label_en: Fosse somaire
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MAR-SAN-31
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
  - country_entry_id: MAR-SAN-32
    source_category_code: latrines
    national_label_en: Latrines
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MAR-SAN-33
    source_category_code: simple_pit
    national_label_en: Simple Pit*
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MAR-SAN-34
    source_category_code: fosse_amelioree_et_ventilee
    national_label_en: "Fosse amelior\xE9e et ventil\xE9e"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: MAR-SAN-35
    source_category_code: improved_pit
    national_label_en: Improved Pit
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: MAR-SAN-36
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
  - country_entry_id: MAR-SAN-37
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
  - country_entry_id: MAR-SAN-38
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
  - country_entry_id: MAR-SAN-39
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
  - country_entry_id: MAR-SAN-40
    source_category_code: dans_la_nature_pas_de_toilette
    national_label_en: Dans la nature pas de toilette
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MAR-SAN-41
    source_category_code: en_plein_air
    national_label_en: En plein air
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MAR-SAN-42
    source_category_code: jetees_dans_la_nature
    national_label_en: "Jet\xE9es dans la nature"
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MAR-SAN-43
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
  - country_entry_id: MAR-SAN-44
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
  - country_entry_id: MAR-SAN-45
    source_category_code: no_none_available
    national_label_en: No, none available
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MAR-SAN-46
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
  - country_entry_id: MAR-SAN-47
    source_category_code: pas_de_toilet_dans_la_nature
    national_label_en: Pas de toilet dans la nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MAR-SAN-48
    source_category_code: pas_de_toilettes_dans_la_brousse_ou_dans_des_champs
    national_label_en: Pas de toilettes dans la brousse ou dans des champs
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MAR-SAN-49
    source_category_code: plein_air
    national_label_en: Plein air
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MAR-SAN-50
    source_category_code: autres_installations_d_assainissement_ameliorees
    national_label_en: "Autres (Installations d'assainissement ame\u0301liore\u0301\
      es)"
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: MAR-SAN-51
    source_category_code: toilette_sans_siphon_reliee_aux_egouts
    national_label_en: Toilette sans siphon reliee aux egouts
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: MAR-SAN-52
    source_category_code: toilette_sans_siphone_branchee_aux_egouts
    national_label_en: "Toilette sans siphone branch\xE9e aux \xE9gouts"
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: MAR-SAN-53
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
  - country_entry_id: MAR-SAN-54
    source_category_code: autres_installations_d_assainissement_non_ameliorees
    national_label_en: "Autres (Installations d'assainissement non ame\u0301liore\u0301\
      es)"
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: MAR-SAN-55
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
  - country_entry_id: MAR-SAN-56
    source_category_code: other_not_defined
    national_label_en: Other (Not Defined)
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: MAR-SAN-57
    source_category_code: other_type_of_sanitation
    national_label_en: Other type of sanitation
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MAR_Morocco.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MAR-WAS-01
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
  - country_entry_id: MAR-WAS-02
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
  - country_entry_id: MAR-WAS-03
    source_category_code: well
    national_label_en: Well
    national_label_local: Tous les puits
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 54
  - country_entry_id: MAR-WAS-04
    source_category_code: well_in_yard
    national_label_en: Well in yard
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 55
  - country_entry_id: MAR-WAS-05
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
  - country_entry_id: MAR-WAS-06
    source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: MAR-WAS-07
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: MAR-WAS-08
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
  - country_entry_id: MAR-WAS-09
    source_category_code: source_surveillee
    national_label_en: "Source surv\xE9ill\xE9e"
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: MAR-WAS-10
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: MAR-WAS-11
    source_category_code: puits_proteges
    national_label_en: "Puits prote\u0301ge\u0301s"
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: MAR-WAS-12
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
  - country_entry_id: MAR-WAS-13
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
  - country_entry_id: MAR-WAS-14
    source_category_code: eua_de_puits
    national_label_en: Eua de puits
    national_label_local: Puits traditionnels
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 62
  - country_entry_id: MAR-WAS-15
    source_category_code: puits_non_equipe_d_une_pompe
    national_label_en: "Puits non \xE9quip\xE9 d'une pompe"
    national_label_local: Puits traditionnels
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 62
  - country_entry_id: MAR-WAS-16
    source_category_code: puits_sans_pompe
    national_label_en: Puits sans pompe
    national_label_local: Puits traditionnels
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 62
  - country_entry_id: MAR-WAS-17
    source_category_code: puits_source_metfia_oued
    national_label_en: Puits, source metfia, oued
    national_label_local: Autre
    jmp_classification: Ground water > Traditional wells > Other
    jmp_id: ground_water.traditional_wells.other
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: MAR-WAS-18
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
  - country_entry_id: MAR-WAS-19
    source_category_code: puits_avec_pompe
    national_label_en: Puits avec pompe
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MAR-WAS-20
    source_category_code: puits_equipe_d_une_pompe
    national_label_en: "Puits \xE9quip\xE9 d'une pompe"
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MAR-WAS-21
    source_category_code: tubewell_or_borehole
    national_label_en: Tubewell or borehole
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MAR-WAS-22
    source_category_code: source_non_protege
    national_label_en: "Source non prote\u0301ge\u0301"
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: MAR-WAS-23
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
  - country_entry_id: MAR-WAS-24
    source_category_code: source_non_surveillee
    national_label_en: "Source non surv\xE9ill\xE9e"
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: MAR-WAS-25
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: MAR-WAS-26
    source_category_code: puits_non_proteges
    national_label_en: "Puits non prote\u0301ge\u0301s"
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MAR-WAS-27
    source_category_code: unprotected_dug_well
    national_label_en: Unprotected dug well
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MAR-WAS-28
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
  - country_entry_id: MAR-WAS-29
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
  - country_entry_id: MAR-WAS-30
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
  - country_entry_id: MAR-WAS-31
    source_category_code: purchased_from_a_cart_with_a_small_tank_or_drum
    national_label_en: Purchased from a cart with a small tank or drum
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MAR-WAS-32
    source_category_code: autres_sources_ameliorees
    national_label_en: "Autres (Sources ame\u0301liore\u0301es)"
    national_label_local: Autre
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: MAR-WAS-33
    source_category_code: camion_cisterne
    national_label_en: Camion cisterne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: MAR-WAS-34
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
  - country_entry_id: MAR-WAS-35
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
  - country_entry_id: MAR-WAS-36
    source_category_code: purchased_from_a_tanker_truck
    national_label_en: Purchased from a tanker truck
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: MAR-WAS-37
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
  - country_entry_id: MAR-WAS-38
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
  - country_entry_id: MAR-WAS-39
    source_category_code: vehicule_equipe_d_un_reservoir_d_eau
    national_label_en: "V\xE9hicule \xE9quip\xE9 d'un r\xE9servoir d'eau"
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: MAR-WAS-40
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
  - country_entry_id: MAR-WAS-41
    source_category_code: autres_sources_non_ameliorees
    national_label_en: "Autres(Sources non ame\u0301liore\u0301es)"
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: MAR-WAS-42
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
  - country_entry_id: MAR-WAS-43
    source_category_code: vendeur
    national_label_en: Vendeur
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: MAR-WAS-44
    source_category_code: autres
    national_label_en: Autres
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MAR-WAS-45
    source_category_code: eau_en_bouteille
    national_label_en: Eau en bouteille
    national_label_local: "Eau conditionn\xE9e"
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 89
  - country_entry_id: MAR-WAS-46
    source_category_code: eau_en_buiteille
    national_label_en: Eau en buiteille
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: MAR-WAS-47
    source_category_code: eau_minerale_en_bouteille
    national_label_en: Eau minerale en bouteille
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: MAR-WAS-48
    source_category_code: l_eau_minerale_en_verre_ou_en_plastique
    national_label_en: L'eau minerale en verre ou en plastique
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: MAR-WAS-49
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
  - country_entry_id: MAR-WAS-50
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
  - country_entry_id: MAR-WAS-51
    source_category_code: eau_des_pluies
    national_label_en: Eau des pluies
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: MAR-WAS-52
    source_category_code: rain_water
    national_label_en: Rain Water
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: MAR-WAS-53
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
  - country_entry_id: MAR-WAS-54
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: MAR-WAS-55
    source_category_code: source_riviere_barrage_lac
    national_label_en: "Source, rivi\xE8re, barrage, lac"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MAR-WAS-56
    source_category_code: surface_water_like_a_river_dam_lake_pond_stream_canal_or_irrigation_channel
    national_label_en: Surface water, like a river, dam, lake, pond, stream, canal
      or irrigation channel
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MAR-WAS-57
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
  - country_entry_id: MAR-WAS-58
    source_category_code: barrage
    national_label_en: Barrage
    national_label_local: Endiguer
    jmp_classification: Surface water > Dam
    jmp_id: surface_water.dam
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 95
  - country_entry_id: MAR-WAS-59
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
  - country_entry_id: MAR-WAS-60
    source_category_code: etang_lac
    national_label_en: Etang / Lac
    national_label_local: Lac
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 94
  - country_entry_id: MAR-WAS-61
    source_category_code: lac
    national_label_en: Lac
    national_label_local: Lac
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 94
  - country_entry_id: MAR-WAS-62
    source_category_code: pond
    national_label_en: Pond
    national_label_local: "\xC9tang"
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 96
  - country_entry_id: MAR-WAS-63
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
  - country_entry_id: MAR-WAS-64
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
  - country_entry_id: MAR-WAS-65
    source_category_code: riviere_cours_d_eau
    national_label_en: Riviere / Cours d'eau
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: MAR-WAS-66
    source_category_code: riviere_fleuve_ruisseau
    national_label_en: Riviere, Fleuve, Ruisseau
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: MAR-WAS-67
    source_category_code: riviere_ruisseau
    national_label_en: "Rivi\xE8re/ruisseau"
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: MAR-WAS-68
    source_category_code: eau_du_robinet
    national_label_en: Eau du robinet
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: MAR-WAS-69
    source_category_code: piped_water
    national_label_en: Piped water
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: MAR-WAS-70
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
  - country_entry_id: MAR-WAS-71
    source_category_code: private_tap
    national_label_en: Private Tap
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: MAR-WAS-72
    source_category_code: reseau_public
    national_label_en: "R\xE9seau public"
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: MAR-WAS-73
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
  - country_entry_id: MAR-WAS-74
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: MAR-WAS-75
    source_category_code: reseau_public
    national_label_en: Reseau public
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: MAR-WAS-76
    source_category_code: eau_du_robinet_dans_la_cour
    national_label_en: Eau du robinet dans la cour
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: MAR-WAS-77
    source_category_code: piped_water_into_yard_plot_or_compound
    national_label_en: Piped water into yard, plot or compound
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: MAR-WAS-78
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
  - country_entry_id: MAR-WAS-79
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
  - country_entry_id: MAR-WAS-80
    source_category_code: public_tap_or_standpipe
    national_label_en: Public tap or standpipe
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: MAR-WAS-81
    source_category_code: robinet_public_borne_fontaine
    national_label_en: Robinet public/ borne fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: MAR-WAS-82
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MAR_Morocco.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

No country-specific content has been supplied yet. The regional focal point
must be consulted before harmonization relies on this country layer.
