---
country_id: CTY-SMR
iso3: SMR
schema_version: '0.2'
status: draft
country_name: SMR
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SMR-EDU-01
    national_label_en: Early Childhood educational development
    national_label_local: Asilo Nido
    entry_age: 0
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: SMR-EDU-02
    national_label_en: Pre-primary School
    national_label_local: Scuola dell'Infanzia
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: SMR-EDU-03
    national_label_en: Primary School
    national_label_local: Scuola Elementare
    entry_age: 6
    duration_years: 5
    isced_level: '1'
    isced_label: ISCED 1 Primary
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 5
    cum_years_computation_path:
    - SMR-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: SMR-EDU-04
    national_label_en: Lower secondary education
    national_label_local: Scuola Media
    entry_age: 11
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    source_row: 10
    parent_country_entry_ids:
    - SMR-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - SMR-EDU-03
    - SMR-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SMR-EDU-05
    national_label_en: Educational and vocational training
    national_label_local: Centro Formazione Professionale
    entry_age: 14
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    source_row: 11
    parent_country_entry_ids:
    - SMR-EDU-04
    cum_years_schooling: 11
    cum_years_computation_path:
    - SMR-EDU-03
    - SMR-EDU-04
    - SMR-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SMR-EDU-06
    national_label_en: Liceo Education (Classical, Linguistic, Scientific and Economic)
    national_label_local: Liceo (Classico, Linguistico, Scientifico, Economico)
    entry_age: 14
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    source_row: 12
    parent_country_entry_ids:
    - SMR-EDU-04
    cum_years_schooling: 13
    cum_years_computation_path:
    - SMR-EDU-03
    - SMR-EDU-04
    - SMR-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SMR-EDU-07
    national_label_en: Technical Institute
    national_label_local: Istituto Tecnico Industriale
    entry_age: 14
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    source_row: 13
    parent_country_entry_ids:
    - SMR-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - SMR-EDU-03
    - SMR-EDU-04
    - SMR-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SMR-EDU-08
    national_label_en: Bachelor's degree
    national_label_local: Corso di laurea triennale
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    source_row: 14
    parent_country_entry_ids:
    - SMR-EDU-06
    cum_years_schooling: 16
    cum_years_computation_path:
    - SMR-EDU-03
    - SMR-EDU-04
    - SMR-EDU-06
    - SMR-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SMR-EDU-09
    national_label_en: Master I level
    national_label_local: Master I livello
    entry_age: 22
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    source_row: 15
    parent_country_entry_ids:
    - SMR-EDU-08
    - SMR-EDU-09
    cum_years_schooling: 18
    cum_years_computation_path:
    - SMR-EDU-03
    - SMR-EDU-04
    - SMR-EDU-06
    - SMR-EDU-08
    - SMR-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SMR-EDU-08, SMR-EDU-09'
  - country_entry_id: SMR-EDU-10
    national_label_en: Master's degree
    national_label_local: Corso di laurea magistrale
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    source_row: 16
    parent_country_entry_ids:
    - SMR-EDU-08
    - SMR-EDU-09
    cum_years_schooling: 18
    cum_years_computation_path:
    - SMR-EDU-03
    - SMR-EDU-04
    - SMR-EDU-06
    - SMR-EDU-08
    - SMR-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SMR-EDU-08, SMR-EDU-09'
  - country_entry_id: SMR-EDU-11
    national_label_en: Master II level
    national_label_local: Master II livello
    entry_age: 24
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    source_row: 17
    parent_country_entry_ids:
    - SMR-EDU-08
    - SMR-EDU-09
    cum_years_schooling: 17
    cum_years_computation_path:
    - SMR-EDU-03
    - SMR-EDU-04
    - SMR-EDU-06
    - SMR-EDU-08
    - SMR-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SMR-EDU-08, SMR-EDU-09'
  - country_entry_id: SMR-EDU-12
    national_label_en: PhD in Historical Sciences
    national_label_local: Dottorato di ricerca in scienze storiche
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    source_row: 18
    parent_country_entry_ids:
    - SMR-EDU-10
    - SMR-EDU-11
    cum_years_schooling: 20
    cum_years_computation_path:
    - SMR-EDU-03
    - SMR-EDU-04
    - SMR-EDU-06
    - SMR-EDU-08
    - SMR-EDU-11
    - SMR-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SMR-EDU-08, SMR-EDU-09'
    - 'minimum parent path selected from: SMR-EDU-10, SMR-EDU-11'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_San
      Marino.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1995
  effective_to: null
  selectors: null
  value: 16
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

