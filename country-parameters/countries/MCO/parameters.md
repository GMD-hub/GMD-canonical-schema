---
country_id: CTY-MCO
iso3: MCO
schema_version: '0.2'
status: draft
country_name: MCO
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: MCO-EDU-01
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
  - country_entry_id: MCO-EDU-02
    national_label_en: "\xC9l\xE9mentaire"
    national_label_local: "\xC9l\xE9mentaire"
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
    - MCO-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: MCO-EDU-03
    national_label_en: "Coll\xE8ge"
    national_label_local: "Coll\xE8ge"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - MCO-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MCO-EDU-04
    national_label_en: "Section d'enseignement g\xE9n\xE9ral et professionnel adapt\xE9\
      \ (SEGPA)"
    national_label_local: "Section d'enseignement g\xE9n\xE9ral et professionnel adapt\xE9\
      \ (SEGPA)"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - MCO-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: MCO-EDU-05
    national_label_en: "Lyc\xE9e"
    national_label_local: "Lyc\xE9e"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - MCO-EDU-03
    - MCO-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-05
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
  - country_entry_id: MCO-EDU-06
    national_label_en: "Lyc\xE9e professionnel"
    national_label_local: "Lyc\xE9e professionnel"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - MCO-EDU-03
    - MCO-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
  - country_entry_id: MCO-EDU-07
    national_label_en: "Dipl\xF4me d'\xC9tat d'Aide-Soignant"
    national_label_local: "Dipl\xF4me d'\xC9tat d'Aide-Soignant"
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - MCO-EDU-03
    - MCO-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
  - country_entry_id: MCO-EDU-08
    national_label_en: Certificat d'aptitude professionnelle (CAP)
    national_label_local: Certificat d'aptitude professionnelle (CAP)
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - MCO-EDU-03
    - MCO-EDU-04
    cum_years_schooling: 11
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
  - country_entry_id: MCO-EDU-09
    national_label_en: "Mise \xE0 Niveau en H\xF4tellerie"
    national_label_local: "Mise \xE0 Niveau en H\xF4tellerie"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - MCO-EDU-05
    - MCO-EDU-06
    - MCO-EDU-07
    - MCO-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    - MCO-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
    - 'minimum parent path selected from: MCO-EDU-05, MCO-EDU-06, MCO-EDU-07, MCO-EDU-08'
  - country_entry_id: MCO-EDU-10
    national_label_en: "Brevet de Technicien Sup\xE9rieur (BTS)"
    national_label_local: "Brevet de Technicien Sup\xE9rieur (BTS)"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - MCO-EDU-05
    - MCO-EDU-06
    - MCO-EDU-07
    - MCO-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    - MCO-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
    - 'minimum parent path selected from: MCO-EDU-05, MCO-EDU-06, MCO-EDU-07, MCO-EDU-08'
  - country_entry_id: MCO-EDU-11
    national_label_en: "Dipl\xF4me d'\xC9tat Infirmier"
    national_label_local: "Dipl\xF4me d'\xC9tat Infirmier"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - MCO-EDU-05
    - MCO-EDU-06
    - MCO-EDU-07
    - MCO-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    - MCO-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
    - 'minimum parent path selected from: MCO-EDU-05, MCO-EDU-06, MCO-EDU-07, MCO-EDU-08'
  - country_entry_id: MCO-EDU-12
    national_label_en: "Enseignement Sup\xE9rieur Artistique (Bac+3)"
    national_label_local: "Enseignement Sup\xE9rieur Artistique (Bac+3)"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - MCO-EDU-05
    - MCO-EDU-06
    - MCO-EDU-07
    - MCO-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    - MCO-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
    - 'minimum parent path selected from: MCO-EDU-05, MCO-EDU-06, MCO-EDU-07, MCO-EDU-08'
  - country_entry_id: MCO-EDU-13
    national_label_en: "Licence \n(POST-BAC)"
    national_label_local: "Licence \n(POST-BAC)"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - MCO-EDU-05
    - MCO-EDU-06
    - MCO-EDU-07
    - MCO-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    - MCO-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
    - 'minimum parent path selected from: MCO-EDU-05, MCO-EDU-06, MCO-EDU-07, MCO-EDU-08'
  - country_entry_id: MCO-EDU-14
    national_label_en: "Dipl\xF4me de Comptabilit\xE9 et Gestion (DCG)"
    national_label_local: "Dipl\xF4me de Comptabilit\xE9 et Gestion (DCG)"
    entry_age: 20
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - MCO-EDU-05
    - MCO-EDU-06
    - MCO-EDU-07
    - MCO-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    - MCO-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
    - 'minimum parent path selected from: MCO-EDU-05, MCO-EDU-06, MCO-EDU-07, MCO-EDU-08'
  - country_entry_id: MCO-EDU-15
    national_label_en: Master
    national_label_local: Master
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - MCO-EDU-11
    - MCO-EDU-12
    - MCO-EDU-13
    - MCO-EDU-14
    cum_years_schooling: 14
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    - MCO-EDU-14
    - MCO-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
    - 'minimum parent path selected from: MCO-EDU-05, MCO-EDU-06, MCO-EDU-07, MCO-EDU-08'
    - 'minimum parent path selected from: MCO-EDU-11, MCO-EDU-12, MCO-EDU-13, MCO-EDU-14'
  - country_entry_id: MCO-EDU-16
    national_label_en: "Enseignement Sup\xE9rieur Artistique (Bac+5)"
    national_label_local: "Enseignement Sup\xE9rieur Artistique (Bac+5)"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - MCO-EDU-05
    - MCO-EDU-06
    - MCO-EDU-07
    - MCO-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    - MCO-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
    - 'minimum parent path selected from: MCO-EDU-05, MCO-EDU-06, MCO-EDU-07, MCO-EDU-08'
  - country_entry_id: MCO-EDU-17
    national_label_en: Doctorat en administration des affaires
    national_label_local: Doctorat en administration des affaires
    entry_age: 23
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - MCO-EDU-15
    - MCO-EDU-16
    cum_years_schooling: 15
    cum_years_computation_path:
    - MCO-EDU-02
    - MCO-EDU-03
    - MCO-EDU-07
    - MCO-EDU-16
    - MCO-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: MCO-EDU-03, MCO-EDU-04'
    - 'minimum parent path selected from: MCO-EDU-05, MCO-EDU-06, MCO-EDU-07, MCO-EDU-08'
    - 'minimum parent path selected from: MCO-EDU-15, MCO-EDU-16'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Monaco.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

