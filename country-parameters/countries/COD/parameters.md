---
country_id: CTY-COD
iso3: COD
schema_version: '0.2'
status: draft
country_name: COD
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: COD-EDU-01
    national_label_en: Maternelle
    national_label_local: Maternelle
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
  - country_entry_id: COD-EDU-02
    national_label_en: Education de base - Enseignement primaire
    national_label_local: Education de base - Enseignement primaire
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
    - COD-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: COD-EDU-03
    national_label_en: "Education de base- \"7\xE8me et 8\xE8me ann\xE9e \""
    national_label_local: "Education de base- \"7\xE8me et 8\xE8me ann\xE9es \""
    entry_age: 12
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - COD-EDU-02
    cum_years_schooling: 8
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: COD-EDU-04
    national_label_en: Premier cycle du secondaire (professionnel)
    national_label_local: Premier cycle du secondaire (professionnel)
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - COD-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: COD-EDU-05
    national_label_en: "Premier cycle du secondaire (Arts et m\xE9tiers, 1ans)"
    national_label_local: "Premier cycle du secondaire (Arts et m\xE9tiers, 1ans)"
    entry_age: 12
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - COD-EDU-02
    cum_years_schooling: 7
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: COD-EDU-06
    national_label_en: "Premier cycle du secondaire (Arts et m\xE9tiers, 2-3 ans)"
    national_label_local: "Premier cycle du secondaire (Arts et m\xE9tiers, 2-3 ans)"
    entry_age: 12
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - COD-EDU-02
    cum_years_schooling: 8
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: COD-EDU-07
    national_label_en: "Deuxi\xE8me cycle du secondaire (G\xE9n\xE9ral et Normal,\
      \ cycle long)"
    national_label_local: "Deuxi\xE8me cycle du secondaire (G\xE9n\xE9ral et Normal,\
      \ cycle long)"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - COD-EDU-03
    - COD-EDU-04
    - COD-EDU-05
    - COD-EDU-06
    cum_years_schooling: 11
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
  - country_entry_id: COD-EDU-08
    national_label_en: "Deuxi\xE8me cycle professionnel (1 ans)"
    national_label_local: "Deuxi\xE8me cycle professionnel (1 ans)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - COD-EDU-03
    - COD-EDU-04
    - COD-EDU-05
    - COD-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
  - country_entry_id: COD-EDU-09
    national_label_en: "Deuxi\xE8me cycle professionnel (2 ans)"
    national_label_local: "Deuxi\xE8me cycle professionnel (2 ans)"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - COD-EDU-03
    - COD-EDU-04
    - COD-EDU-05
    - COD-EDU-06
    cum_years_schooling: 9
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
  - country_entry_id: COD-EDU-10
    national_label_en: "Deuxi\xE8me cycle du technique secondaire cycle long"
    national_label_local: "Deuxi\xE8me cycle du technique secondaire cycle long"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - COD-EDU-03
    - COD-EDU-04
    - COD-EDU-05
    - COD-EDU-06
    cum_years_schooling: 11
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
  - country_entry_id: COD-EDU-11
    national_label_en: "Secr\xE9taire de direction"
    national_label_local: "Secr\xE9taire de direction"
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-12
    national_label_en: "Enseignement sup\xE9rieur technique, Dipl\xF4me A1"
    national_label_local: "Enseignement sup\xE9rieur technique, Dipl\xF4me A1"
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-13
    national_label_en: "Enseignement sup\xE9rieur, premier cycle, Ann\xE9e pr\xE9\
      paratoire (Ing\xE9niorat)"
    national_label_local: "Enseignement sup\xE9rieur, premier cycle, Ann\xE9e pr\xE9\
      paratoire (Ing\xE9niorat)"
    entry_age: 18
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-14
    national_label_en: "Enseignement sup\xE9rieur, premier cycle, Ann\xE9e pr\xE9\
      paratoire (Ing\xE9niorat technicien)"
    national_label_local: "Enseignement sup\xE9rieur, premier cycle, Ann\xE9e pr\xE9\
      paratoire (Ing\xE9niorat technicien)"
    entry_age: 18
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-15
    national_label_en: "Enseignement sup\xE9rieur, premier cycle"
    national_label_local: "Enseignement sup\xE9rieur, premier cycle"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-16
    national_label_en: "Enseignement sup\xE9rieur, premier cycle (Ing\xE9niorat technicien)"
    national_label_local: "Enseignement sup\xE9rieur, premier cycle (Ing\xE9niorat\
      \ technicien)"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-17
    national_label_en: "Enseignement sup\xE9rieur, premier cycle (Ing\xE9niorat)"
    national_label_local: "Enseignement sup\xE9rieur, premier cycle (Ing\xE9niorat)"
    entry_age: 19
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 13
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-18
    national_label_en: "Enseignement sup\xE9rieur second cycle"
    national_label_local: "Enseignement sup\xE9rieur second cycle"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-19
    national_label_en: "Enseignement sup\xE9rieur second cycle: M\xE9decine humaine\
      \ et v\xE9t\xE9rinaire"
    national_label_local: "Enseignement sup\xE9rieur second cycle: M\xE9decine humaine\
      \ et v\xE9t\xE9rinaire"
    entry_age: 21
    duration_years: 4
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 12
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-20
    national_label_en: "Enseignement sup\xE9rieur, troisi\xE8me cycle (DES)"
    national_label_local: "Enseignement sup\xE9rieur, troisi\xE8me cycle (DES)"
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - COD-EDU-07
    - COD-EDU-08
    - COD-EDU-09
    - COD-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
  - country_entry_id: COD-EDU-21
    national_label_en: "Enseignement sup\xE9rieur, troisi\xE8me cycle (Doctorat)"
    national_label_local: "Enseignement sup\xE9rieur, troisi\xE8me cycle (Doctorat)"
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - COD-EDU-18
    - COD-EDU-19
    - COD-EDU-20
    cum_years_schooling: 13
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-18
    - COD-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
    - 'minimum parent path selected from: COD-EDU-18, COD-EDU-19, COD-EDU-20'
  - country_entry_id: COD-EDU-22
    national_label_en: "Enseignement sup\xE9rieur (Sp\xE9cialisation en m\xE9decine)"
    national_label_local: "Enseignement sup\xE9rieur (Sp\xE9cialisation en m\xE9decine)"
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - COD-EDU-18
    - COD-EDU-19
    - COD-EDU-20
    cum_years_schooling: 13
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-18
    - COD-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
    - 'minimum parent path selected from: COD-EDU-18, COD-EDU-19, COD-EDU-20'
  - country_entry_id: COD-EDU-23
    national_label_en: "Professeur en m\xE9decine: Enseignement sup\xE9rieur (Agr\xE9\
      gation en M\xE9decine)"
    national_label_local: "Professeur en m\xE9decine: Enseignement sup\xE9rieur (Agr\xE9\
      gation en M\xE9decine)"
    entry_age: 28
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - COD-EDU-18
    - COD-EDU-19
    - COD-EDU-20
    cum_years_schooling: 13
    cum_years_computation_path:
    - COD-EDU-02
    - COD-EDU-05
    - COD-EDU-08
    - COD-EDU-18
    - COD-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: COD-EDU-03, COD-EDU-04, COD-EDU-05, COD-EDU-06'
    - 'minimum parent path selected from: COD-EDU-07, COD-EDU-08, COD-EDU-09, COD-EDU-10'
    - 'minimum parent path selected from: COD-EDU-18, COD-EDU-19, COD-EDU-20'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Template
      Fr Republique Democratique Du Congo.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: 2015
  selectors: null
  value:
  - country_entry_id: COD-SUBNAT-01
    survey_labels: 10 - Kinshasa
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1072
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1072
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1072'
    geo_nvar: ADM1_NAME
    geo_name: Kinshasa
    source_row: 2474
  - country_entry_id: COD-SUBNAT-02
    survey_labels: 20 - Bas-Congo
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1067
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1067
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1067'
    geo_nvar: ADM1_NAME
    geo_name: Bas-Congo
    source_row: 2475
  - country_entry_id: COD-SUBNAT-03
    survey_labels: 30 - Bandundu
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1066
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1066
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1066'
    geo_nvar: ADM1_NAME
    geo_name: Bandundu
    source_row: 2476
  - country_entry_id: COD-SUBNAT-04
    survey_labels: 40 - Equateur
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1068
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1068
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1068'
    geo_nvar: ADM1_NAME
    geo_name: Equateur
    source_row: 2477
  - country_entry_id: COD-SUBNAT-05
    survey_labels: 50 - Orientale
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1075
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1075
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1075'
    geo_nvar: ADM1_NAME
    geo_name: Orientale
    source_row: 2478
  - country_entry_id: COD-SUBNAT-06
    survey_labels: 61 - Nord-Kivu
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1074
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1074
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1074'
    geo_nvar: ADM1_NAME
    geo_name: Nord-Kivu
    source_row: 2479
  - country_entry_id: COD-SUBNAT-07
    survey_labels: 62 - Maniema
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1073
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1073
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1073'
    geo_nvar: ADM1_NAME
    geo_name: Maniema
    source_row: 2480
  - country_entry_id: COD-SUBNAT-08
    survey_labels: 63 - Sud-Kivu
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1076
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1076
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1076'
    geo_nvar: ADM1_NAME
    geo_name: Sud-Kivu
    source_row: 2481
  - country_entry_id: COD-SUBNAT-09
    survey_labels: 70 - Katanga
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1071
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1071
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1071'
    geo_nvar: ADM1_NAME
    geo_name: Katanga
    source_row: 2482
  - country_entry_id: COD-SUBNAT-10
    survey_labels: "80 - Kasa\xEF Oriental"
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1070
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1070
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1070'
    geo_nvar: ADM1_NAME
    geo_name: Kasai Oriental
    source_row: 2483
  - country_entry_id: COD-SUBNAT-11
    survey_labels: "90 - Kasa\xEF Occidental"
    survey_variables: subnatid
    gmd_subnatid1: COD_2015_GAUL1_1069
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COD_2015_GAUL1_1069
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1069'
    geo_nvar: ADM1_NAME
    geo_name: Kasai Occidental
    source_row: 2484
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2022
  effective_to: null
  selectors: null
  value:
  - country_entry_id: COD-SUBNAT-01
    survey_labels: 1 - Kinshasa
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.10_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.10_1
    geo_nvar: NAME_1
    geo_name: Kinshasa
    source_row: 2496
  - country_entry_id: COD-SUBNAT-02
    survey_labels: 10 - Tshuapa
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.26_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.26_1
    geo_nvar: NAME_1
    geo_name: Tshuapa
    source_row: 2497
  - country_entry_id: COD-SUBNAT-03
    survey_labels: 11 - Tshopo
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.25_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.25_1
    geo_nvar: NAME_1
    geo_name: Tshopo
    source_row: 2498
  - country_entry_id: COD-SUBNAT-04
    survey_labels: 12 - Bas Uele
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.1_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.1_1
    geo_nvar: NAME_1
    geo_name: Bas-Uele
    source_row: 2499
  - country_entry_id: COD-SUBNAT-05
    survey_labels: 13 - Haut Uele
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.5_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.5_1
    geo_nvar: NAME_1
    geo_name: Haut-Uele
    source_row: 2500
  - country_entry_id: COD-SUBNAT-06
    survey_labels: 14 - Ituri
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.6_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.6_1
    geo_nvar: NAME_1
    geo_name: Ituri
    source_row: 2501
  - country_entry_id: COD-SUBNAT-07
    survey_labels: 15 - Nord Kivu
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.19_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.19_1
    geo_nvar: NAME_1
    geo_name: Nord-Kivu
    source_row: 2502
  - country_entry_id: COD-SUBNAT-08
    survey_labels: 16 - Sud Kivu
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.22_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.22_1
    geo_nvar: NAME_1
    geo_name: Sud-Kivu
    source_row: 2503
  - country_entry_id: COD-SUBNAT-09
    survey_labels: 17 - Maniema
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.17_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.17_1
    geo_nvar: NAME_1
    geo_name: Maniema
    source_row: 2504
  - country_entry_id: COD-SUBNAT-10
    survey_labels: 18 - Haut Katanga
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.3_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.3_1
    geo_nvar: NAME_1
    geo_name: Haut-Katanga
    source_row: 2505
  - country_entry_id: COD-SUBNAT-11
    survey_labels: 19 - Haut Lomami
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.4_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.4_1
    geo_nvar: NAME_1
    geo_name: Haut-Lomami
    source_row: 2506
  - country_entry_id: COD-SUBNAT-12
    survey_labels: 2 - Kongo central
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.11_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.11_1
    geo_nvar: NAME_1
    geo_name: Kongo-Central
    source_row: 2507
  - country_entry_id: COD-SUBNAT-13
    survey_labels: 20 - Lualaba
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.15_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.15_1
    geo_nvar: NAME_1
    geo_name: Lualaba
    source_row: 2508
  - country_entry_id: COD-SUBNAT-14
    survey_labels: 21 - Tanganyka
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.24_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.24_1
    geo_nvar: NAME_1
    geo_name: Tanganyika
    source_row: 2509
  - country_entry_id: COD-SUBNAT-15
    survey_labels: 22 - Lomami
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.14_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.14_1
    geo_nvar: NAME_1
    geo_name: Lomami
    source_row: 2510
  - country_entry_id: COD-SUBNAT-16
    survey_labels: 23 - Sankuru
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.21_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.21_1
    geo_nvar: NAME_1
    geo_name: Sankuru
    source_row: 2511
  - country_entry_id: COD-SUBNAT-17
    survey_labels: 24 - Kasai Oriental
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.8_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.8_1
    geo_nvar: NAME_1
    geo_name: "Kasa\xEF-Oriental"
    source_row: 2512
  - country_entry_id: COD-SUBNAT-18
    survey_labels: 25 - Kasai
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.9_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.9_1
    geo_nvar: NAME_1
    geo_name: "Kasa\xEF"
    source_row: 2513
  - country_entry_id: COD-SUBNAT-19
    survey_labels: 26 - Kasai Central
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.7_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.7_1
    geo_nvar: NAME_1
    geo_name: "Kasa\xEF-Central"
    source_row: 2514
  - country_entry_id: COD-SUBNAT-20
    survey_labels: 3 - Kwango
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.12_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.12_1
    geo_nvar: NAME_1
    geo_name: Kwango
    source_row: 2515
  - country_entry_id: COD-SUBNAT-21
    survey_labels: 4 - Kwilu
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.13_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.13_1
    geo_nvar: NAME_1
    geo_name: Kwilu
    source_row: 2516
  - country_entry_id: COD-SUBNAT-22
    survey_labels: 5 - Maindombe
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.16_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.16_1
    geo_nvar: NAME_1
    geo_name: Mai-Ndombe
    source_row: 2517
  - country_entry_id: COD-SUBNAT-23
    survey_labels: 6 - Equateur
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.2_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.2_1
    geo_nvar: NAME_1
    geo_name: "\xC9quateur"
    source_row: 2518
  - country_entry_id: COD-SUBNAT-24
    survey_labels: 7 - Nord Ubangi
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.20_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.20_1
    geo_nvar: NAME_1
    geo_name: Nord-Ubangi
    source_row: 2519
  - country_entry_id: COD-SUBNAT-25
    survey_labels: 8 - Sud Ubangi
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.23_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.23_1
    geo_nvar: NAME_1
    geo_name: Sud-Ubangi
    source_row: 2520
  - country_entry_id: COD-SUBNAT-26
    survey_labels: 9 - Mongala
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: COD_2022_GADM1_COD.18_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: COD.18_1
    geo_nvar: NAME_1
    geo_name: Mongala
    source_row: 2521
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
  - country_entry_id: COD-SAN-01
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: COD-SAN-02
    source_category_code: toilette_a_compostage
    national_label_en: Toilette a compostage
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: COD-SAN-03
    source_category_code: toilettes_a_compostage
    national_label_en: Toilettes a compostage
    national_label_local: "Toilettes a compostage (priv\xE9es)"
    jmp_classification: Composting toilets > Composting toilet (private)
    jmp_id: composting_toilets.composting_toilet_private
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 129
  - country_entry_id: COD-SAN-04
    source_category_code: chasse_d_eau_reliee_a_l_air_libre
    national_label_en: "Chasse d\u2019eau: reliee a l\u2019air libre"
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: COD-SAN-05
    source_category_code: chasse_d_eau_reliee_a_systeme_d_egouts
    national_label_en: "Chasse d\u2019eau reliee a systeme d\u2019egouts"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: COD-SAN-06
    source_category_code: chasse_d_eau_reliee_aux_latrines
    national_label_en: "Chasse d\u2019eau: reliee aux latrines"
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: COD-SAN-07
    source_category_code: chasse_d_eau_reliee_a_fosse_septique
    national_label_en: "Chasse d\u2019eau reliee a fosse septique"
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: COD-SAN-08
    source_category_code: chasse_d_eau_reliee_a_un_lieu_inconnu
    national_label_en: "Chasse d\u2019eau: reliee a un lieu inconnu"
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: COD-SAN-09
    source_category_code: flush_toilet
    national_label_en: Flush toilet
    national_label_local: "Toilette \xE0 chasse d'eau"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: COD-SAN-10
    source_category_code: interieur_exterieur_prive_avec_chasse_d_eau
    national_label_en: "Int\xE9rieur/Ext\xE9rieur priv\xE9 avec chasse d'eau"
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: COD-SAN-11
    source_category_code: interieur_exterieur_prive_chasse_eau
    national_label_en: "Int\xE9rieur/Ext\xE9rieur priv\xE9 chasse eau"
    national_label_local: "Toilette \xE0 chasse d'eau (priv\xE9e)"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: COD-SAN-12
    source_category_code: commun_a_plusieurs_menages_chasse_eau
    national_label_en: "Commun \xE0 plusieurs m\xE9nages (chasse eau)"
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: COD-SAN-13
    source_category_code: commun_a_plusieurs_menages_avec_chasse_d_eau
    national_label_en: "Commun \xE0 plusieurs m\xE9nages, avec chasse d'eau"
    national_label_local: "Toilette \xE0 chasse d'eau (publique/partag\xE9e)"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: COD-SAN-14
    source_category_code: flush_don_t_know_where
    national_label_en: Flush, don't know where
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: COD-SAN-15
    source_category_code: latrines_avec_chasse_reliees_a_autre_chose
    national_label_en: Latrines avec chasse reliees a autre chose
    national_label_local: "reli\xE9e al'air libre"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: COD-SAN-16
    source_category_code: chasse_connectees_a_systeme_d_egouts
    national_label_en: Chasse connectees a systeme d'egouts
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: COD-SAN-17
    source_category_code: chasse_raccordee_a_l_egout
    national_label_en: "Chasse raccord\xE9e \xE0 l'\xE9gout"
    national_label_local: "reli\xE9e a systeme d'egouts"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: COD-SAN-18
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
  - country_entry_id: COD-SAN-19
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit latrine
    national_label_local: "reli\xE9e aux latrine"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: COD-SAN-20
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
  - country_entry_id: COD-SAN-21
    source_category_code: latrines_avec_chasse_connectees_a_fosse_septique
    national_label_en: Latrines avec chasse connectees a fosse septique
    national_label_local: "reli\xE9e a fosse septique"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: COD-SAN-22
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: "reli\xE9e a autre chose"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: COD-SAN-23
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
  - country_entry_id: COD-SAN-24
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
  - country_entry_id: COD-SAN-25
    source_category_code: hanging_toilet_latrine
    national_label_en: Hanging toilet/latrine
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: COD-SAN-26
    source_category_code: toilettes_suspendues_latrines_suspendues
    national_label_en: Toilettes suspendues/latrines suspendues
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: COD-SAN-27
    source_category_code: latrine_a_fosse_avec_dalle
    national_label_en: 'Latrine a fosse: avec dalle'
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: COD-SAN-28
    source_category_code: latrines_traditionnelle_couverte
    national_label_en: Latrines traditionnelle couverte
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: COD-SAN-29
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
  - country_entry_id: COD-SAN-30
    source_category_code: traditional_pit_toilet_covered
    national_label_en: Traditional pit toilet (covered)
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: COD-SAN-31
    source_category_code: latrine_a_fosse_sans_dalle_trou_ouvert
    national_label_en: Latrine a fosse sans dalle / trou ouvert
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: COD-SAN-32
    source_category_code: latrine_a_fosse_sans_dalle_fosse_ouverte
    national_label_en: 'Latrine a fosse: sans dalle/ fosse ouverte'
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: COD-SAN-33
    source_category_code: latrine_traditionnelle_non_couverte_trou_ouvert
    national_label_en: Latrine traditionnelle non couverte/trou ouvert
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: COD-SAN-34
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
  - country_entry_id: COD-SAN-35
    source_category_code: traditional_pit_toilet_uncovered
    national_label_en: Traditional pit toilet (uncovered)
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: COD-SAN-36
    source_category_code: latrines_a_fosse_avec_dalle
    national_label_en: Latrines a fosse avec dalle
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: COD-SAN-37
    source_category_code: latrines_amenagees_publiques
    national_label_en: "Latrines am\xE9nag\xE9es Publiques"
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: COD-SAN-38
    source_category_code: trou_dans_la_parcelle
    national_label_en: Trou dans la parcelle
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: COD-SAN-39
    source_category_code: latrine_a_fosse_amelioree_ventilee
    national_label_en: 'Latrine a fosse: amelioree ventilee'
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: COD-SAN-40
    source_category_code: latrines_ameliorees_a_ventilation
    national_label_en: "Latrines am\xE9lior\xE9es \xE0 ventilation"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: COD-SAN-41
    source_category_code: latrines_ameliorees_ventilees_lav
    national_label_en: "Latrines am\xE9lior\xE9es ventilees (LAV)"
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: COD-SAN-42
    source_category_code: ventilated_improved_pit_latirine
    national_label_en: Ventilated Improved Pit Latirine
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: COD-SAN-43
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit latrine (VIP)
    national_label_local: "Latrine a fosse amelior\xE9e ventil\xE9e"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: COD-SAN-44
    source_category_code: latrines_amenagees_privees
    national_label_en: "Latrines am\xE9nag\xE9es priv\xE9es"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: COD-SAN-45
    source_category_code: latrines_amenagees_privees
    national_label_en: "Latrines am\xE9nag\xE9es Priv\xE9es"
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 115
  - country_entry_id: COD-SAN-46
    source_category_code: latrines_amenagees_publiques
    national_label_en: "Latrines am\xE9nag\xE9es publiques"
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: COD-SAN-47
    source_category_code: latrine_a_evacuation
    national_label_en: "Latrine \xE0 \xE9vacuation"
    national_label_local: "Latrines \xE0 chasse d'eau"
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 85
  - country_entry_id: COD-SAN-48
    source_category_code: latrines_avec_chasse_connectees_aux_latrines_a_fosse_ou_autres
    national_label_en: Latrines avec chasse connectees aux latrines a fosse ou autres
    national_label_local: "Latrines \xE0 chasse d'eau"
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 85
  - country_entry_id: COD-SAN-49
    source_category_code: defecation_a_l_air_libre_pas_de_toilette_brousse_champ
    national_label_en: Defecation a l'air libre (pas de toilette, brousse, champ)
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: COD-SAN-50
    source_category_code: no_facility_bush_field
    national_label_en: No facility, bush,field
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: COD-SAN-51
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
  - country_entry_id: COD-SAN-52
    source_category_code: pas_de_toilette
    national_label_en: Pas de toilette
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: COD-SAN-53
    source_category_code: pas_de_toilette_brousse_champ
    national_label_en: Pas de toilette/brousse/champ
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: COD-SAN-54
    source_category_code: pas_de_toilettes
    national_label_en: Pas de toilettes
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: COD-SAN-55
    source_category_code: pas_de_toilettes_nature_champs
    national_label_en: Pas de toilettes/ nature/champs
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: COD-SAN-56
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
  - country_entry_id: COD-SAN-57
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
  - country_entry_id: COD-SAN-58
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
  - country_entry_id: COD-SAN-59
    source_category_code: others
    national_label_en: Others
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: COD-SAN-60
    source_category_code: trou_dans_la_parcelle
    national_label_en: Trou dans la parcelle
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_COD_Congo_Democratic_Republic_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: COD-WAS-01
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
  - country_entry_id: COD-WAS-02
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
  - country_entry_id: COD-WAS-03
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
  - country_entry_id: COD-WAS-04
    source_category_code: source_source_protegee
    national_label_en: 'Source: source protegee'
    national_label_local: "Source prot\xE9g\xE9es"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: COD-WAS-05
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
  - country_entry_id: COD-WAS-06
    source_category_code: puit_proteges
    national_label_en: "Puit prot\xE9g\xE9s"
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: COD-WAS-07
    source_category_code: puits_creuse_protege
    national_label_en: 'Puits creuse: protege'
    national_label_local: "Puits proteg\xE9es"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: COD-WAS-08
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
  - country_entry_id: COD-WAS-09
    source_category_code: protected_well_in_dwelling_plot_or_yard
    national_label_en: Protected well in dwelling, plot or yard
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: COD-WAS-10
    source_category_code: protected_public_well
    national_label_en: Protected public well
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 68
  - country_entry_id: COD-WAS-11
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
  - country_entry_id: COD-WAS-12
    source_category_code: puits_a_pompe
    national_label_en: "Puits \xE0 pompe"
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: COD-WAS-13
    source_category_code: puits_a_pompe_forage
    national_label_en: "Puits \xE0 pompe, forage"
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: COD-WAS-14
    source_category_code: puits_a_pompe_forage
    national_label_en: Puits a pompe/forage
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: COD-WAS-15
    source_category_code: tube_well_or_borehole
    national_label_en: Tube well or borehole
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: COD-WAS-16
    source_category_code: tubewell
    national_label_en: Tubewell
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: COD-WAS-17
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
  - country_entry_id: COD-WAS-18
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
  - country_entry_id: COD-WAS-19
    source_category_code: source_source_non_protegee
    national_label_en: 'Source: source non protegee'
    national_label_local: "Source non-prot\xE9g\xE9es"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: COD-WAS-20
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
  - country_entry_id: COD-WAS-21
    source_category_code: puit_non_protege
    national_label_en: "Puit non prot\xE9g\xE9"
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: COD-WAS-22
    source_category_code: puits_creuse_non_protege
    national_label_en: 'Puits creuse: non protege'
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: COD-WAS-23
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
  - country_entry_id: COD-WAS-24
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: "Puits non-proteg\xE9es"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: COD-WAS-25
    source_category_code: open_well_in_dwelling_plot_or_yard
    national_label_en: Open well in dwelling, plot or yard
    national_label_local: "Priv\xE9"
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: COD-WAS-26
    source_category_code: open_public_well
    national_label_en: Open public well
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 72
  - country_entry_id: COD-WAS-27
    source_category_code: bidon_bassin_seau_livre_a_domicile
    national_label_en: Bidon, bassin,seau livre a domicile
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: COD-WAS-28
    source_category_code: camion_citerne
    national_label_en: Camion citerne
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: COD-WAS-29
    source_category_code: cart_with_small_tank
    national_label_en: Cart with small tank
    national_label_local: "Chariot avec petit r\xE9servoir/tambour"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: COD-WAS-30
    source_category_code: kiosque_a_eau
    national_label_en: Kiosque a eau
    national_label_local: Autre
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: COD-WAS-31
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
  - country_entry_id: COD-WAS-32
    source_category_code: charette_avec_petite_citerne_tonneau
    national_label_en: Charette avec petite citerne / tonneau
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: COD-WAS-33
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: COD-WAS-34
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
  - country_entry_id: COD-WAS-35
    source_category_code: autres
    national_label_en: Autres
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: COD-WAS-36
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
  - country_entry_id: COD-WAS-37
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
  - country_entry_id: COD-WAS-38
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "Eau conditionn\xE9e"
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 89
  - country_entry_id: COD-WAS-39
    source_category_code: eau_en_boutille
    national_label_en: Eau en boutille
    national_label_local: "Eau conditionn\xE9e"
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 89
  - country_entry_id: COD-WAS-40
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: COD-WAS-41
    source_category_code: eau_conditionnee_eau_en_bouteille
    national_label_en: 'Eau conditionnee: eau en bouteille'
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: COD-WAS-42
    source_category_code: eau_conditionnee_eau_en_sachet
    national_label_en: 'Eau conditionnee: eau en sachet'
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: COD-WAS-43
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
  - country_entry_id: COD-WAS-44
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
  - country_entry_id: COD-WAS-45
    source_category_code: cours_d_eau
    national_label_en: Cours d'eau
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: COD-WAS-46
    source_category_code: eau_de_surface_riviere_barrage_lac_mare_courant_canal_systeme_d_irrigation
    national_label_en: "Eau de surface (riviere, barrage, lac, mare, courant, canal,\
      \ systeme d\u2019irrigation)"
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: COD-WAS-47
    source_category_code: eua_de_surface
    national_label_en: Eua de surface
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: COD-WAS-48
    source_category_code: mare_ruisseau_fleuve
    national_label_en: Mare/ruisseau/fleuve
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: COD-WAS-49
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
  - country_entry_id: COD-WAS-50
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
  - country_entry_id: COD-WAS-51
    source_category_code: sea_lake
    national_label_en: Sea/Lake
    national_label_local: Lac
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 94
  - country_entry_id: COD-WAS-52
    source_category_code: river_stream
    national_label_en: River/stream
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: COD-WAS-53
    source_category_code: eau_du_robinet_dans_la_parcelle_voisine
    national_label_en: Eau du robinet dans la parcelle voisine
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: COD-WAS-54
    source_category_code: piped_from_the_neighbor
    national_label_en: Piped from the neighbor
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: COD-WAS-55
    source_category_code: robinet_d_un_autre_menage
    national_label_en: "Robinet d'un autre m\xE9nage"
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: COD-WAS-56
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
  - country_entry_id: COD-WAS-57
    source_category_code: robinet_chez_le_voisin
    national_label_en: 'Robinet: chez le voisin'
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: COD-WAS-58
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
  - country_entry_id: COD-WAS-59
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
  - country_entry_id: COD-WAS-60
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
  - country_entry_id: COD-WAS-61
    source_category_code: robinet_interieur
    national_label_en: "Robinet int\xE9rieur"
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: COD-WAS-62
    source_category_code: robinet_dans_le_logement
    national_label_en: 'Robinet: dans le logement'
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: COD-WAS-63
    source_category_code: eau_du_robinet_dans_la_cour_parcelle
    national_label_en: Eau du robinet dans la cour/parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COD-WAS-64
    source_category_code: eau_du_robinet_dans_quartier_cour_ou_parcelle
    national_label_en: Eau du robinet dans quartier, cour ou parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COD-WAS-65
    source_category_code: piped_to_yard_plot
    national_label_en: Piped to yard/plot
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COD-WAS-66
    source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COD-WAS-67
    source_category_code: robinet_exterieur
    national_label_en: "Robinet ext\xE9rieur"
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COD-WAS-68
    source_category_code: robinet_dans_la_concession_jardin_parcelle
    national_label_en: 'Robinet: dans la concession/jardin/ parcelle'
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COD-WAS-69
    source_category_code: borne_fontaine
    national_label_en: Borne fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: COD-WAS-70
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
  - country_entry_id: COD-WAS-71
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: COD-WAS-72
    source_category_code: robinet_public_borne_fontaine
    national_label_en: Robinet public / borne fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: COD-WAS-73
    source_category_code: robinet_robient_public_borne_fontaine
    national_label_en: 'Robinet: robient public/borne fontaine'
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_COD_Congo_Democratic_Republic_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

