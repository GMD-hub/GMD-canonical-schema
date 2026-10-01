---
country_id: CTY-MLI
iso3: MLI
schema_version: '0.2'
status: draft
country_name: MLI
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MLI-EDU-01
    national_label_en: "Education pr\xE9scolaire"
    national_label_local: "Education pr\xE9scolaire"
    entry_age: 4
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
  - country_entry_id: MLI-EDU-02
    national_label_en: Premier cycle fondamental
    national_label_local: Premier cycle fondamental
    entry_age: 7
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
    - MLI-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: MLI-EDU-03
    national_label_en: "Deuxi\xE8me cycle fondamental"
    national_label_local: "Deuxi\xE8me cycle fondamental"
    entry_age: 13
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - MLI-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLI-EDU-04
    national_label_en: "Enseignement secondaire g\xE9n\xE9ral"
    national_label_local: "Enseignement secondaire g\xE9n\xE9ral"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - MLI-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLI-EDU-05
    national_label_en: Enseignement professionnel
    national_label_local: Enseignement professionnel
    entry_age: 19
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - MLI-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLI-EDU-06
    national_label_en: Enseignement professionnel
    national_label_local: Enseignement professionnel
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - MLI-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLI-EDU-07
    national_label_en: "Techniciens du premier cycle de sant\xE9"
    national_label_local: "Techniciens du premier cycle de sant\xE9"
    entry_age: 17
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - MLI-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLI-EDU-08
    national_label_en: "Formation des \xE9ducateurs du pr\xE9scolaire"
    national_label_local: "Formation des \xE9ducateurs du pr\xE9scolaire"
    entry_age: 19
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - MLI-EDU-03
    cum_years_schooling: 13
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLI-EDU-09
    national_label_en: "Formation des ma\xEEtres  (Apr\xE8s DEF)"
    national_label_local: "Formation des ma\xEEtres (Apr\xE8s DEF)"
    entry_age: 19
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - MLI-EDU-03
    cum_years_schooling: 13
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLI-EDU-10
    national_label_en: Enseignement technique
    national_label_local: Enseignement technique
    entry_age: 17
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - MLI-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MLI-EDU-11
    national_label_en: "Formation des ma\xEEtres  (Apr\xE8s baccalaur\xE9at)"
    national_label_local: "Formation des ma\xEEtres (Apr\xE8s baccalaur\xE9at)"
    entry_age: 19
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 13
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-12
    national_label_en: "Enseignement sup\xE9rieur (DUTS)"
    national_label_local: "Enseignement sup\xE9rieur (DUTS)"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 13
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-13
    national_label_en: "Enseignement sup\xE9rieur (BTS)"
    national_label_local: "Enseignement sup\xE9rieur (BTS)"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 13
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-14
    national_label_en: "Enseignement sup\xE9rieur (DTSS)"
    national_label_local: "Enseignement sup\xE9rieur (DTSS)"
    entry_age: 19
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 14
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-15
    national_label_en: "Enseignement sup\xE9rieur (DEUG / DUEL)"
    national_label_local: "Enseignement sup\xE9rieur (DEUG / DUEL)"
    entry_age: 19
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 13
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-16
    national_label_en: "Enseignement sup\xE9rieur (Licence)"
    national_label_local: "Enseignement sup\xE9rieur (Licence)"
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 12
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-17
    national_label_en: "Enseignement sup\xE9rieur (Maitrise)"
    national_label_local: "Enseignement sup\xE9rieur (Maitrise)"
    entry_age: 23
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 12
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-18
    national_label_en: "Enseignement sup\xE9rieur (Ingenieur)"
    national_label_local: "Enseignement sup\xE9rieur (Ingenieur)"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 16
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-19
    national_label_en: "M\xE9decine et pharmacie"
    national_label_local: "M\xE9decine et pharmacie"
    entry_age: 19
    duration_years: 7
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 18
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-20
    national_label_en: Formation des professeurs du secondaire
    national_label_local: Formation des professeurs du secondaire
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 13
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-21
    national_label_en: "Enseignement sup\xE9rieur (DEA)"
    national_label_local: "Enseignement sup\xE9rieur (DEA)"
    entry_age: 24
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 12
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-22
    national_label_en: "Enseignement sup\xE9rieur  (Ingenieur apr\xE8s licence)"
    national_label_local: "Enseignement sup\xE9rieur (Ingenieur apr\xE8s licence)"
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - MLI-EDU-04
    - MLI-EDU-05
    - MLI-EDU-06
    - MLI-EDU-07
    - MLI-EDU-08
    - MLI-EDU-09
    - MLI-EDU-10
    cum_years_schooling: 13
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
  - country_entry_id: MLI-EDU-23
    national_label_en: "Enseignement sup\xE9rieur (Master)"
    national_label_local: "Enseignement sup\xE9rieur (Master)"
    entry_age: 23
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - MLI-EDU-15
    - MLI-EDU-16
    - MLI-EDU-17
    cum_years_schooling: 13
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-16
    - MLI-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
    - 'minimum parent path selected from: MLI-EDU-15, MLI-EDU-16, MLI-EDU-17'
  - country_entry_id: MLI-EDU-24
    national_label_en: "Enseignement sup\xE9rieur  (Doctorat)"
    national_label_local: "Enseignement sup\xE9rieur (Doctorat)"
    entry_age: 25
    duration_years: 2
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - MLI-EDU-18
    - MLI-EDU-19
    - MLI-EDU-20
    - MLI-EDU-21
    - MLI-EDU-22
    - MLI-EDU-23
    cum_years_schooling: 14
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-21
    - MLI-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
    - 'minimum parent path selected from: MLI-EDU-18, MLI-EDU-19, MLI-EDU-20, MLI-EDU-21,
      MLI-EDU-22, MLI-EDU-23'
  - country_entry_id: MLI-EDU-25
    national_label_en: "Enseignement sup\xE9rieur (Medecine)"
    national_label_local: "Enseignement sup\xE9rieur (Medecine)"
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - MLI-EDU-18
    - MLI-EDU-19
    - MLI-EDU-20
    - MLI-EDU-21
    - MLI-EDU-22
    - MLI-EDU-23
    cum_years_schooling: 15
    cum_years_computation_path:
    - MLI-EDU-02
    - MLI-EDU-03
    - MLI-EDU-05
    - MLI-EDU-21
    - MLI-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MLI-EDU-04, MLI-EDU-05, MLI-EDU-06, MLI-EDU-07,
      MLI-EDU-08, MLI-EDU-09, MLI-EDU-10'
    - 'minimum parent path selected from: MLI-EDU-18, MLI-EDU-19, MLI-EDU-20, MLI-EDU-21,
      MLI-EDU-22, MLI-EDU-23'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Mali.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MLI-SUBNAT-01
    survey_labels: "1 - Kayes | 1 \u2013 Kayes"
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: MLI_2015_GAUL1_1928
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL1_1928
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1928'
    geo_nvar: ADM1_NAME
    geo_name: Kayes
    source_row: 10106
  - country_entry_id: MLI-SUBNAT-02
    survey_labels: "2 - Koulikoro | 2 \u2013 Koulikoro"
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: MLI_2015_GAUL1_1930
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL1_1930
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1930'
    geo_nvar: ADM1_NAME
    geo_name: Koulikoro
    source_row: 10107
  - country_entry_id: MLI-SUBNAT-03
    survey_labels: "3 - Sikasso | 3 \u2013 Sikasso"
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: MLI_2015_GAUL1_1933
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL1_1933
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1933'
    geo_nvar: ADM1_NAME
    geo_name: Sikasso
    source_row: 10108
  - country_entry_id: MLI-SUBNAT-04
    survey_labels: "4 - Segou | 4 - S\uFFFDgou | 4 \u2013 S\xE9gou"
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: MLI_2015_GAUL1_1932
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL1_1932
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1932'
    geo_nvar: ADM1_NAME
    geo_name: Segou
    source_row: 10109
  - country_entry_id: MLI-SUBNAT-05
    survey_labels: "5 - Mopti | 5 \u2013 Mopti"
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: MLI_2015_GAUL1_1931
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL1_1931
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1931'
    geo_nvar: ADM1_NAME
    geo_name: Mopti
    source_row: 10110
  - country_entry_id: MLI-SUBNAT-06
    survey_labels: "6 - Tombouctou | 6 \u2013 Tombouctou"
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: MLI_2015_GAUL1_1934
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL1_1934
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1934'
    geo_nvar: ADM1_NAME
    geo_name: Tombouctou
    source_row: 10111
  - country_entry_id: MLI-SUBNAT-07
    survey_labels: "7 - Gao | 7 \u2013 Gao"
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: MLI_2015_GAUL1_1927
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL1_1927
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1927'
    geo_nvar: ADM1_NAME
    geo_name: Gao
    source_row: 10112
  - country_entry_id: MLI-SUBNAT-08
    survey_labels: "8 - Kidal | 8 \u2013 Kidal"
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: MLI_2015_GAUL1_1929
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL1_1929
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1929'
    geo_nvar: ADM1_NAME
    geo_name: Kidal
    source_row: 10113
  - country_entry_id: MLI-SUBNAT-09
    survey_labels: "9 - Bamako | 9 \u2013 Bamako"
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: MLI_2015_GAUL1_1926
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL1_1926
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1926'
    geo_nvar: ADM1_NAME
    geo_name: Bamako
    source_row: 10114
  - country_entry_id: MLI-SUBNAT-10
    survey_labels: 11 - Menaka
    survey_variables: subnatid
    gmd_subnatid1: MLI_2015_GAUL2_19375
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAUL2_19375
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '2'
    geo_idvar: ADM2_CODE
    geo_id: '19375'
    geo_nvar: ADM2_NAME
    geo_name: Menaka
    source_row: 10125
  - country_entry_id: MLI-SUBNAT-11
    survey_labels: 7 - Gao
    survey_variables: subnatid
    gmd_subnatid1: MLI_2015_GAULx_1927
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: MLI_2015_GAULx_1927
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: ADM1_CODE
    geo_id: '1927'
    geo_nvar: ADM1_NAME
    geo_name: Gao
    source_row: 10131
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
  - country_entry_id: MLI-SAN-01
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
  - country_entry_id: MLI-SAN-02
    source_category_code: toilettes_a_compostage
    national_label_en: "Toilettes \xE0 compostage"
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: MLI-SAN-03
    source_category_code: toilettes_a_compostage
    national_label_en: "Toilettes \xE0 compostage"
    national_label_local: "Toilettes a compostage (priv\xE9es)"
    jmp_classification: Composting toilets > Composting toilet (private)
    jmp_id: composting_toilets.composting_toilet_private
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 129
  - country_entry_id: MLI-SAN-04
    source_category_code: toilettes_a_compostage
    national_label_en: "Toilettes \xE0 compostage"
    national_label_local: Toilettes a compostage (publiques)
    jmp_classification: Composting toilets > Composting toilet (shared)
    jmp_id: composting_toilets.composting_toilet_shared
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 130
  - country_entry_id: MLI-SAN-05
    source_category_code: chasse_branchee_a_autre_chose
    national_label_en: "Chasse branch\xE9e \xE0 autre chose"
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: MLI-SAN-06
    source_category_code: chasse_branchee_ailleurs
    national_label_en: "Chasse branch\xE9e ailleurs"
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: MLI-SAN-07
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: MLI-SAN-08
    source_category_code: flushed_toilet_to_elsewhere
    national_label_en: Flushed toilet to elsewhere
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: MLI-SAN-09
    source_category_code: chasse_branchee_a_l_egout
    national_label_en: "Chasse branch\xE9e \xE0 l'\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: MLI-SAN-10
    source_category_code: chasse_d_eau_manuelle_branchee_a_l_egout
    national_label_en: "Chasse d'eau/manuelle branch\xE9e \xE0 l'\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: MLI-SAN-11
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: MLI-SAN-12
    source_category_code: flush_toilet_to_piped_sewer_system
    national_label_en: Flush toilet to piped sewer system
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: MLI-SAN-13
    source_category_code: chasse_branchee_a_latrines
    national_label_en: "Chasse branch\xE9e \xE0 latrines"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: MLI-SAN-14
    source_category_code: chasse_d_eau_manuelle_branchee_a_latrines
    national_label_en: "Chasse d'eau/manuelle branch\xE9e \xE0 latrines"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: MLI-SAN-15
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit latrine
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: MLI-SAN-16
    source_category_code: flushed_toilet_to_pit_latrine
    national_label_en: Flushed toilet to pit latrine
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: MLI-SAN-17
    source_category_code: chasse_branchee_a_fosse_septique
    national_label_en: "Chasse branch\xE9e \xE0 fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: MLI-SAN-18
    source_category_code: chasse_d_eau_manuelle_branchee_a_fosse_septique
    national_label_en: "Chasse d'eau/manuelle branch\xE9e \xE0 fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: MLI-SAN-19
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: MLI-SAN-20
    source_category_code: flushed_toilet_to_septic_tank
    national_label_en: Flushed toilet to septic tank
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: MLI-SAN-21
    source_category_code: chasse_branchee_a_un_endroit_inconnu_pas_sur
    national_label_en: "Chasse branch\xE9e \xE0 un endroit inconnu/pas s\xFBr"
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: MLI-SAN-22
    source_category_code: chasse_d_eau_manuelle_branchee_a_un_endroit_inconnu_pas_sur
    national_label_en: "Chasse d'eau/manuelle branch\xE9e \xE0 un endroit inconnu/pas\
      \ s\xFBr"
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: MLI-SAN-23
    source_category_code: flush_don_t_know_where
    national_label_en: Flush, don't know where
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: MLI-SAN-24
    source_category_code: chasse_d_eau_avec_evacuation
    national_label_en: "Chasse d'eau avec \xE9vacuation"
    national_label_local: "Toilette \xE0 chasse d'eau"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: MLI-SAN-25
    source_category_code: flush_toilet
    national_label_en: flush toilet
    national_label_local: "Toilette \xE0 chasse d'eau"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: MLI-SAN-26
    source_category_code: w_c_interieur_exterieur_avec_chasse_eau
    national_label_en: "W.C. int\xE9rieur/ext\xE9rieur avec chasse eau"
    national_label_local: "Toilette \xE0 chasse d'eau"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: MLI-SAN-27
    source_category_code: wc_flush
    national_label_en: WC / Flush
    national_label_local: "Toilette \xE0 chasse d'eau"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: MLI-SAN-28
    source_category_code: chasse_d_eau_interieure_ou_exterieure_privee
    national_label_en: "Chasse d'eau int\xE9rieure ou ext\xE9rieure priv\xE9e"
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: MLI-SAN-29
    source_category_code: w_c_int
    national_label_en: W.C. int
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: MLI-SAN-30
    source_category_code: chasse_d_eau_chasse_manuelle_non_reliee_aux_egouts_fosse
    national_label_en: "Chasse d\u2019eau/chasse manuelle non reli\xE9e aux \xE9gouts/fosse"
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush/toilets > Private flush/toilet > to elsewhere
    jmp_id: flush_toilets.private_flush_toilet.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 77
  - country_entry_id: MLI-SAN-31
    source_category_code: chasse_d_eau_chasse_manuelle_connectee_a_un_systeme_d_egout
    national_label_en: "Chasse d\u2019eau/chasse manuelle connect\xE9e \xE0 un syst\xE8\
      me d\u2019\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: MLI-SAN-32
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
  - country_entry_id: MLI-SAN-33
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_septique
    national_label_en: "Chasse d\u2019eau/chasse manuelle reli\xE9e \xE0 une fosse\
      \ septique"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > Private flush/toilet > to pit
    jmp_id: flush_toilets.private_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 75
  - country_entry_id: MLI-SAN-34
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_d_aisances
    national_label_en: "Chasse d\u2019eau/chasse manuelle reli\xE9e \xE0 une fosse\
      \ d\u2019aisances"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: MLI-SAN-35
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
  - country_entry_id: MLI-SAN-36
    source_category_code: prive_avec_chasse_eau
    national_label_en: "Priv\xE9 avec chasse eau"
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush/toilets > Private flush/toilet > to unknown place/ not
      sure/DK
    jmp_id: flush_toilets.private_flush_toilet.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 76
  - country_entry_id: MLI-SAN-37
    source_category_code: chasse_d_eau_a_plusieurs_menages
    national_label_en: "Chasse d'eau \xE0 plusieurs m\xE9nages"
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: MLI-SAN-38
    source_category_code: w_c_ext
    national_label_en: W.C. ext
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: MLI-SAN-39
    source_category_code: chasse_d_eau_chasse_manuelle_connectee_a_un_systeme_d_egout
    national_label_en: "Chasse d\u2019eau/chasse manuelle connect\xE9e \xE0 un syst\xE8\
      me d\u2019\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: MLI-SAN-40
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
  - country_entry_id: MLI-SAN-41
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_septique
    national_label_en: "Chasse d\u2019eau/chasse manuelle reli\xE9e \xE0 une fosse\
      \ septique"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to pit
    jmp_id: flush_toilets.public_shared_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 81
  - country_entry_id: MLI-SAN-42
    source_category_code: chasse_d_eau_chasse_manuelle_reliee_a_une_fosse_d_aisances
    national_label_en: "Chasse d\u2019eau/chasse manuelle reli\xE9e \xE0 une fosse\
      \ d\u2019aisances"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 80
  - country_entry_id: MLI-SAN-43
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
  - country_entry_id: MLI-SAN-44
    source_category_code: commun_a_plusieurs_menages_avec_chasse_eau
    national_label_en: "Commun \xE0 plusieurs m\xE9nages avec chasse eau"
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to unknown place/
      not sure/DK
    jmp_id: flush_toilets.public_shared_flush_toilet.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 82
  - country_entry_id: MLI-SAN-45
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
  - country_entry_id: MLI-SAN-46
    source_category_code: flush_to_piped_sewer_system
    national_label_en: flush to piped sewer system
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: MLI-SAN-47
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
  - country_entry_id: MLI-SAN-48
    source_category_code: flush_to_septic_tank
    national_label_en: flush to septic tank
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: MLI-SAN-49
    source_category_code: chasse_d_eau_chasse_manuelle_non_reliee_aux_egouts_fosse
    national_label_en: "Chasse d\u2019eau/chasse manuelle non reli\xE9e aux \xE9gouts/fosse"
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MLI-SAN-50
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
  - country_entry_id: MLI-SAN-51
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
  - country_entry_id: MLI-SAN-52
    source_category_code: bucket_toilet
    national_label_en: Bucket toilet
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: MLI-SAN-53
    source_category_code: seaux_tinettes
    national_label_en: Seaux/tinettes
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: MLI-SAN-54
    source_category_code: hanging_toilet
    national_label_en: Hanging toilet
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: MLI-SAN-55
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
  - country_entry_id: MLI-SAN-56
    source_category_code: toilette_suspendues_latrines_suspendues
    national_label_en: Toilette suspendues/latrines suspendues
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: MLI-SAN-57
    source_category_code: toilettes_suspendues
    national_label_en: Toilettes suspendues
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: MLI-SAN-58
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
  - country_entry_id: MLI-SAN-59
    source_category_code: improved_latrine_pit
    national_label_en: Improved Latrine/Pit
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: MLI-SAN-60
    source_category_code: latrines_a_fosse_avec_dalle
    national_label_en: "Latrines \xE0 fosse avec dalle"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: MLI-SAN-61
    source_category_code: latrines_ameliorees
    national_label_en: "Latrines am\xE9lior\xE9es"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: MLI-SAN-62
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
  - country_entry_id: MLI-SAN-63
    source_category_code: pit_latrine_with_slab
    national_label_en: pit latrine with slab
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: MLI-SAN-64
    source_category_code: fosse_rudimentaire_trou_court
    national_label_en: Fosse rudimentaire/trou court
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: MLI-SAN-65
    source_category_code: fosse_rudimentaire_trou_ouvert
    national_label_en: Fosse rudimentaire/trou ouvert
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: MLI-SAN-66
    source_category_code: latrines_a_fosses_sans_dalle
    national_label_en: "Latrines \xE0 fosses sans dalle"
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: MLI-SAN-67
    source_category_code: latrines_a_fosses_sans_dalle_trou_ouvert
    national_label_en: "Latrines \xE0 fosses sans dalle/trou ouvert"
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: MLI-SAN-68
    source_category_code: pit_latrine_without_slab
    national_label_en: Pit latrine without slab
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: MLI-SAN-69
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: MLI-SAN-70
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
  - country_entry_id: MLI-SAN-71
    source_category_code: fosse_latrines_en_plein_air
    national_label_en: Fosse/latrines en plein air
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MLI-SAN-72
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
  - country_entry_id: MLI-SAN-73
    source_category_code: simple_latrine_pit
    national_label_en: Simple Latrine/Pit
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MLI-SAN-74
    source_category_code: traditional_pit_toilet
    national_label_en: traditional pit toilet
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: MLI-SAN-75
    source_category_code: latrines_ameliorees_ventilees
    national_label_en: "Latrines amelior\xE9es ventil\xE9es"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: MLI-SAN-76
    source_category_code: latrines_ameliorees_ventilees_lav
    national_label_en: "Latrines amelior\xE9es ventil\xE9es (LAV)"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: MLI-SAN-77
    source_category_code: ventilated_improved_pit_vip_latrine
    national_label_en: Ventilated improved pit (VIP) latrine
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: MLI-SAN-78
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: ventilated improved pit latrine
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: MLI-SAN-79
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: ventilated improved pit latrine (vip)
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: MLI-SAN-80
    source_category_code: latrines_privees
    national_label_en: "Latrines priv\xE9es"
    national_label_local: "Latrines priv\xE9es"
    jmp_classification: Latrines > Dry latrines > Private Latrines
    jmp_id: latrines.dry_latrines.private_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: false
    shared_flag: false
    source_row: 112
  - country_entry_id: MLI-SAN-81
    source_category_code: fosse_d_aisances_avec_dalle
    national_label_en: "Fosse d\u2019aisances avec dalle"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: MLI-SAN-82
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
  - country_entry_id: MLI-SAN-83
    source_category_code: latrines_privees
    national_label_en: "Latrines priv\xE9es"
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 115
  - country_entry_id: MLI-SAN-84
    source_category_code: fosse_d_aisances_amelioree_auto_aeree
    national_label_en: "Fosse d\u2019aisances am\xE9lior\xE9e auto-a\xE9r\xE9e"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 113
  - country_entry_id: MLI-SAN-85
    source_category_code: latrines_a_plusieurs_menages
    national_label_en: "Latrines \xE0 plusieurs m\xE9nages"
    national_label_local: "Latrines publiques/partag\xE9es"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines
    jmp_id: latrines.dry_latrines.public_shared_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: false
    shared_flag: true
    source_row: 120
  - country_entry_id: MLI-SAN-86
    source_category_code: bucket_toilet
    national_label_en: bucket toilet
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Bucket
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 126
  - country_entry_id: MLI-SAN-87
    source_category_code: hanging_toilet_latrine
    national_label_en: hanging toilet/latrine
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Hanging
      toilet/hanging latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 125
  - country_entry_id: MLI-SAN-88
    source_category_code: fosse_d_aisances_avec_dalle
    national_label_en: "Fosse d\u2019aisances avec dalle"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: MLI-SAN-89
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
  - country_entry_id: MLI-SAN-90
    source_category_code: latrines_communes_a_plusieurs_menages
    national_label_en: "Latrines communes \xE0 plusieurs m\xE9nages"
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: true
    source_row: 123
  - country_entry_id: MLI-SAN-91
    source_category_code: fosse_d_aisances_amelioree_auto_aeree
    national_label_en: "Fosse d\u2019aisances am\xE9lior\xE9e auto-a\xE9r\xE9e"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Ventilated
      Improved Pit latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 121
  - country_entry_id: MLI-SAN-92
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
  - country_entry_id: MLI-SAN-93
    source_category_code: private_pour_flush
    national_label_en: Private Pour-Flush
    national_label_local: "Latrines \xE0 chasse d'eau (priv\xE9es)"
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 91
  - country_entry_id: MLI-SAN-94
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
  - country_entry_id: MLI-SAN-95
    source_category_code: shared_pour_flush
    national_label_en: Shared Pour-Flush
    national_label_local: "Latrines \xE0 chasse d'eau (publiques/partag\xE9es)"
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 97
  - country_entry_id: MLI-SAN-96
    source_category_code: aucune_toilette_dans_la_nature
    national_label_en: Aucune toilette (dans la nature)
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MLI-SAN-97
    source_category_code: autre
    national_label_en: Autre
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MLI-SAN-98
    source_category_code: dans_la_nature
    national_label_en: Dans la nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MLI-SAN-99
    source_category_code: nature_pas_de_toilette
    national_label_en: Nature/Pas de toilette
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MLI-SAN-100
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
  - country_entry_id: MLI-SAN-101
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
  - country_entry_id: MLI-SAN-102
    source_category_code: no_facility_bush_field
    national_label_en: no facility, bush, field
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MLI-SAN-103
    source_category_code: no_facility_bush_field
    national_label_en: no facility/bush/field
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MLI-SAN-104
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
  - country_entry_id: MLI-SAN-105
    source_category_code: open_defecation
    national_label_en: Open defecation
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MLI-SAN-106
    source_category_code: pas_de_toilettes_nature
    national_label_en: Pas de toilettes , nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: MLI-SAN-107
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
  - country_entry_id: MLI-SAN-108
    source_category_code: community_latrines
    national_label_en: Community latrines
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: MLI-SAN-109
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
  - country_entry_id: MLI-SAN-110
    source_category_code: autre_non_determine
    national_label_en: "Autre/Non d\xE9termin\xE9"
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: MLI-SAN-111
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
  - country_entry_id: MLI-SAN-112
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
  - country_entry_id: MLI-SAN-113
    source_category_code: other_not_defined
    national_label_en: Other/Not Defined
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MLI_Mali_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MLI-WAS-01
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
  - country_entry_id: MLI-WAS-02
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
  - country_entry_id: MLI-WAS-03
    source_category_code: protected_spring_closed
    national_label_en: Protected spring (closed)
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: MLI-WAS-04
    source_category_code: source_amenagee
    national_label_en: "Source am\xE9nag\xE9e"
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: MLI-WAS-05
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
  - country_entry_id: MLI-WAS-06
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
  - country_entry_id: MLI-WAS-07
    source_category_code: protected_dug_well_closed_or_with_handpump
    national_label_en: Protected dug well (closed) or with handpump
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: MLI-WAS-08
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
  - country_entry_id: MLI-WAS-09
    source_category_code: puits_amenage
    national_label_en: "Puits am\xE9nag\xE9"
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: MLI-WAS-10
    source_category_code: puits_amenages
    national_label_en: "Puits am\xE9nag\xE9s"
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: MLI-WAS-11
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
  - country_entry_id: MLI-WAS-12
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
  - country_entry_id: MLI-WAS-13
    source_category_code: puits_a_pompe_equipe_de_pmh
    national_label_en: "Puits \xE0 pompe/\xE9quip\xE9 de PMH"
    national_label_local: Autre
    jmp_classification: Ground water > Protected well > Other
    jmp_id: ground_water.protected_well.other
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: MLI-WAS-14
    source_category_code: puits_couvert_dans_la_cour_concession
    national_label_en: Puits couvert dans la cour/concession
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: MLI-WAS-15
    source_category_code: puits_moderne_protege
    national_label_en: "Puits moderne prot\xE9g\xE9"
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: MLI-WAS-16
    source_category_code: puits_protege_dans_logement_cour
    national_label_en: "Puits prot\xE9g\xE9 dans logement/cour"
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: MLI-WAS-17
    source_category_code: puits_couvert_ailleurs
    national_label_en: Puits couvert ailleurs
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 68
  - country_entry_id: MLI-WAS-18
    source_category_code: puits_creuse_protege
    national_label_en: "Puits creus\xE9 prot\xE9g\xE9"
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 68
  - country_entry_id: MLI-WAS-19
    source_category_code: puits_protege_public
    national_label_en: "Puits prot\xE9g\xE9 public"
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 68
  - country_entry_id: MLI-WAS-20
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
  - country_entry_id: MLI-WAS-21
    source_category_code: private_well_in_house_yard
    national_label_en: Private Well (In house/Yard)
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 63
  - country_entry_id: MLI-WAS-22
    source_category_code: well_private
    national_label_en: Well (Private)
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 63
  - country_entry_id: MLI-WAS-23
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
  - country_entry_id: MLI-WAS-24
    source_category_code: well_public
    national_label_en: Well  (public)
    national_label_local: Public
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 64
  - country_entry_id: MLI-WAS-25
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
  - country_entry_id: MLI-WAS-26
    source_category_code: borehole_with_handpump_pump
    national_label_en: Borehole (with handpump/pump)
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MLI-WAS-27
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
  - country_entry_id: MLI-WAS-28
    source_category_code: forage_pompe
    national_label_en: Forage/Pompe
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MLI-WAS-29
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
  - country_entry_id: MLI-WAS-30
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
  - country_entry_id: MLI-WAS-31
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
  - country_entry_id: MLI-WAS-32
    source_category_code: pump
    national_label_en: Pump
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: MLI-WAS-33
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
  - country_entry_id: MLI-WAS-34
    source_category_code: forage_dans_la_concession
    national_label_en: Forage dans la concession
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Tubewell, borehole > Private
    jmp_id: ground_water.tubewell_borehole.private
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 59
  - country_entry_id: MLI-WAS-35
    source_category_code: forage_ailleurs
    national_label_en: Forage ailleurs
    national_label_local: Public
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 60
  - country_entry_id: MLI-WAS-36
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
  - country_entry_id: MLI-WAS-37
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
  - country_entry_id: MLI-WAS-38
    source_category_code: source_non_amenagee
    national_label_en: "Source non am\xE9nag\xE9e"
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: MLI-WAS-39
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
  - country_entry_id: MLI-WAS-40
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
  - country_entry_id: MLI-WAS-41
    source_category_code: unprotected_spring_open
    national_label_en: Unprotected spring (open)
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: MLI-WAS-42
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
  - country_entry_id: MLI-WAS-43
    source_category_code: puits_moderne_non_protege
    national_label_en: "Puits moderne non prot\xE9g\xE9"
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MLI-WAS-44
    source_category_code: puits_non_amenages
    national_label_en: "Puits non am\xE9nag\xE9s"
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MLI-WAS-45
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
  - country_entry_id: MLI-WAS-46
    source_category_code: puits_non_amenages
    national_label_en: "Puits non-am\xE9nag\xE9s"
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MLI-WAS-47
    source_category_code: unprotected_dug_well_open
    national_label_en: Unprotected dug well (open)
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: MLI-WAS-48
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
  - country_entry_id: MLI-WAS-49
    source_category_code: puits_ouvert_dans_la_cour_concession
    national_label_en: Puits ouvert dans la cour/concession
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: MLI-WAS-50
    source_category_code: puits_ouvert_dans_logement_cour
    national_label_en: Puits ouvert dans logement/cour
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: MLI-WAS-51
    source_category_code: puits_creuse_non_protege
    national_label_en: "Puits creus\xE9 non prot\xE9g\xE9"
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 72
  - country_entry_id: MLI-WAS-52
    source_category_code: puits_ouvert_ailleurs
    national_label_en: Puits ouvert ailleurs
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 72
  - country_entry_id: MLI-WAS-53
    source_category_code: puits_ouvert_public
    national_label_en: Puits ouvert public
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 72
  - country_entry_id: MLI-WAS-54
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
  - country_entry_id: MLI-WAS-55
    source_category_code: achat_au_revendeurs
    national_label_en: Achat au revendeurs
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MLI-WAS-56
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
  - country_entry_id: MLI-WAS-57
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
  - country_entry_id: MLI-WAS-58
    source_category_code: chariot_avec_un_petit_reservoir_ou_tambour
    national_label_en: chariot avec un petit reservoir ou tambour
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MLI-WAS-59
    source_category_code: charrette_avec_petite_citerne
    national_label_en: charrette avec petite citerne
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MLI-WAS-60
    source_category_code: charrette_avec_petite_citerne_tonneau
    national_label_en: Charrette avec petite citerne / tonneau
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: MLI-WAS-61
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
  - country_entry_id: MLI-WAS-62
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
  - country_entry_id: MLI-WAS-63
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
  - country_entry_id: MLI-WAS-64
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
  - country_entry_id: MLI-WAS-65
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
  - country_entry_id: MLI-WAS-66
    source_category_code: water_selling_cart_or_truck
    national_label_en: Water-selling cart or truck
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: MLI-WAS-67
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
  - country_entry_id: MLI-WAS-68
    source_category_code: autre_non_determine
    national_label_en: "Autre/Non d\xE9termin\xE9"
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: MLI-WAS-69
    source_category_code: other
    national_label_en: other
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: MLI-WAS-70
    source_category_code: other_private_public
    national_label_en: Other private & public
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: MLI-WAS-71
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
  - country_entry_id: MLI-WAS-72
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
  - country_entry_id: MLI-WAS-73
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
  - country_entry_id: MLI-WAS-74
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
  - country_entry_id: MLI-WAS-75
    source_category_code: bag_water
    national_label_en: bag water
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: MLI-WAS-76
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
  - country_entry_id: MLI-WAS-77
    source_category_code: sachet_water
    national_label_en: sachet water
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: MLI-WAS-78
    source_category_code: collecte_d_eau_de_pluie
    national_label_en: Collecte d'eau de pluie
    national_label_local: "Citerne/r\xE9servoir couvert"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: MLI-WAS-79
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
  - country_entry_id: MLI-WAS-80
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
  - country_entry_id: MLI-WAS-81
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
  - country_entry_id: MLI-WAS-82
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
  - country_entry_id: MLI-WAS-83
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
  - country_entry_id: MLI-WAS-84
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
  - country_entry_id: MLI-WAS-85
    source_category_code: eau_de_surface_riviere_fleuve_barrage_lac_mare_canal_canal_d_irrigation
    national_label_en: "Eau de surface (rivi\xE8re, fleuve, barrage, lac, mare, canal,\
      \ canal d\u2019irrigation)"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MLI-WAS-86
    source_category_code: eau_de_surface_telle_que_rivia_re_barrage_lac_a_tang_ruisseau_canal_ou_canaux_da_tmirrigation
    national_label_en: "Eau de surface, telle que rivi\xC3\xA8re, barrage, lac, \xC3\
      \xA9tang, ruisseau, canal ou canaux d\xE2\u20AC\u2122irrigation"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MLI-WAS-87
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
  - country_entry_id: MLI-WAS-88
    source_category_code: eaux_de_surface
    national_label_en: Eaux de surface
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MLI-WAS-89
    source_category_code: fleuve_riviere_lac
    national_label_en: "Fleuve, rivi\xE8re, lac"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MLI-WAS-90
    source_category_code: fleuve_riviere_lac_barrage_eau_de_pluie
    national_label_en: "Fleuve/Rivi\xE8re/Lac/Barrage/Eau de pluie"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MLI-WAS-91
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
  - country_entry_id: MLI-WAS-92
    source_category_code: river_dam_lake_ponds_stream_canal_irrigation_channel
    national_label_en: river/dam/lake/ponds/stream/canal/irrigation channel
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MLI-WAS-93
    source_category_code: river_surface_water
    national_label_en: River/Surface Water
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MLI-WAS-94
    source_category_code: surface_water_pond_river_stream
    national_label_en: Surface water (pond/river/stream)
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: MLI-WAS-95
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
  - country_entry_id: MLI-WAS-96
    source_category_code: lakes_creeks
    national_label_en: Lakes/Creeks
    national_label_local: Lac
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 94
  - country_entry_id: MLI-WAS-97
    source_category_code: mare_lac
    national_label_en: Mare/Lac
    national_label_local: Lac
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 94
  - country_entry_id: MLI-WAS-98
    source_category_code: fleuve_riviere
    national_label_en: "Fleuve/Rivi\xE8re"
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: MLI-WAS-99
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
  - country_entry_id: MLI-WAS-100
    source_category_code: piped_from_the_neighbor
    national_label_en: piped from the neighbor
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: MLI-WAS-101
    source_category_code: piped_to_neighbor
    national_label_en: Piped to neighbor
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: MLI-WAS-102
    source_category_code: robinet_chez_les_voisins
    national_label_en: Robinet chez les voisins
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: MLI-WAS-103
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
  - country_entry_id: MLI-WAS-104
    source_category_code: dans_le_logement_la_cour
    national_label_en: Dans le logement/la cour
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: MLI-WAS-105
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
  - country_entry_id: MLI-WAS-106
    source_category_code: private_tap_house_yard
    national_label_en: Private Tap (house/yard)
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: MLI-WAS-107
    source_category_code: robinet
    national_label_en: Robinet
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: MLI-WAS-108
    source_category_code: running_water
    national_label_en: Running Water
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: MLI-WAS-109
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
  - country_entry_id: MLI-WAS-110
    source_category_code: piped_into_dwelling
    national_label_en: piped into dwelling
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: MLI-WAS-111
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
  - country_entry_id: MLI-WAS-112
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
  - country_entry_id: MLI-WAS-113
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
  - country_entry_id: MLI-WAS-114
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
  - country_entry_id: MLI-WAS-115
    source_category_code: robinet_du_menage
    national_label_en: "Robinet du m\xE9nage"
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: MLI-WAS-116
    source_category_code: robinet_prive
    national_label_en: "Robinet priv\xE9"
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: MLI-WAS-117
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
  - country_entry_id: MLI-WAS-118
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
  - country_entry_id: MLI-WAS-119
    source_category_code: piped_water_into_yard
    national_label_en: Piped water into yard
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: MLI-WAS-120
    source_category_code: robinet_dans_concession_cour_ou_parcelle
    national_label_en: Robinet dans concession, cour ou parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: MLI-WAS-121
    source_category_code: robinet_dans_cour_jardin
    national_label_en: Robinet dans cour/jardin
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: MLI-WAS-122
    source_category_code: robinet_dans_la_concession_cour_parcelle
    national_label_en: Robinet dans la concession/cour/parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: MLI-WAS-123
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
  - country_entry_id: MLI-WAS-124
    source_category_code: borne_fontaine_robinet_public
    national_label_en: Borne fontaine/Robinet public
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: MLI-WAS-125
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
  - country_entry_id: MLI-WAS-126
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
  - country_entry_id: MLI-WAS-127
    source_category_code: public_tap
    national_label_en: Public Tap
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: MLI-WAS-128
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
  - country_entry_id: MLI-WAS-129
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
  - country_entry_id: MLI-WAS-130
    source_category_code: robinet_public
    national_label_en: Robinet public
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: MLI-WAS-131
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
  - country_entry_id: MLI-WAS-132
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
  - country_entry_id: MLI-WAS-133
    source_category_code: spring
    national_label_en: Spring
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MLI_Mali_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

