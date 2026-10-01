---
country_id: CTY-QAT
iso3: QAT
schema_version: '0.2'
status: draft
country_name: QAT
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: QAT-EDU-01
    national_label_en: Nursery
    national_label_local: "\u0627\u0644\u062D\u0636\u0627\u0646\u0629"
    entry_age: 0
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
  - country_entry_id: QAT-EDU-02
    national_label_en: Kindergarten
    national_label_local: "\u0631\u064A\u0627\u0636 \u0627\u0644\u0623\u0637\u0641\
      \u0627\u0644"
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
  - country_entry_id: QAT-EDU-03
    national_label_en: Primary stage
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u0627\u0628\u062A\u062F\u0627\u0626\u064A\u0629"
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
    - QAT-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: QAT-EDU-04
    national_label_en: Primary stage - Adult education
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u0627\u0628\u062A\u062F\u0627\u0626\u064A\u0629 - \u062A\u0639\u0644\u064A\u0645\
      \ \u0627\u0644\u0643\u0628\u0627\u0631"
    entry_age: 12
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - QAT-EDU-04
    cum_years_status: computed
    review_flags: &id002 []
  - country_entry_id: QAT-EDU-05
    national_label_en: Preparatory stage
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u0625\u0639\u062F\u0627\u062F\u064A\u0629"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - QAT-EDU-03
    cum_years_schooling: 9
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: QAT-EDU-06
    national_label_en: Preparatory stage - Adult education
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u0625\u0639\u062F\u0627\u062F\u064A\u0629 - \u062A\u0639\u0644\u064A\u0645\
      \ \u0627\u0644\u0643\u0628\u0627\u0631"
    entry_age: 15
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - QAT-EDU-04
    cum_years_schooling: 7
    cum_years_computation_path:
    - QAT-EDU-04
    - QAT-EDU-06
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: QAT-EDU-07
    national_label_en: Specialized preparatory stage - Science and technology
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u0625\u0639\u062F\u0627\u062F\u064A\u0629 \u0627\u0644\u062A\u062E\u0635\u0635\
      \u064A\u0629 -  \u0627\u0644\u0639\u0644\u0648\u0645 \u0648\u0627\u0644\u062A\
      \u0643\u0646\u0648\u0644\u0648\u062C\u064A\u0627"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - QAT-EDU-03
    cum_years_schooling: 9
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: QAT-EDU-08
    national_label_en: Secondary stage
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A\u0629"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - QAT-EDU-05
    - QAT-EDU-07
    cum_years_schooling: 12
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
  - country_entry_id: QAT-EDU-09
    national_label_en: Secondary stage - Adult education
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A\u0629- \u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0643\u0628\u0627\u0631"
    entry_age: 18
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - QAT-EDU-06
    cum_years_schooling: 10
    cum_years_computation_path:
    - QAT-EDU-04
    - QAT-EDU-06
    - QAT-EDU-09
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: QAT-EDU-10
    national_label_en: Specialized secondary stage - Adult education
    national_label_local: "\u0627\u0644\u0645\u0631\u062D\u0644\u0629 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A\u0629 \u0627\u0644\u062A\u062E\u0635\u0635\u064A\
      \u0629- \u062A\u0639\u0644\u064A\u0645 \u0627\u0644\u0643\u0628\u0627\u0631"
    entry_age: 18
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - QAT-EDU-06
    cum_years_schooling: 10
    cum_years_computation_path:
    - QAT-EDU-04
    - QAT-EDU-06
    - QAT-EDU-10
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: QAT-EDU-11
    national_label_en: Technical secondary
    national_label_local: "\u0627\u0644\u062B\u0627\u0646\u0648\u064A\u0629 \u0627\
      \u0644\u062A\u0642\u0646\u064A\u0629"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 17
    parent_country_entry_ids:
    - QAT-EDU-05
    - QAT-EDU-07
    cum_years_schooling: 12
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
  - country_entry_id: QAT-EDU-12
    national_label_en: Commercial secondary - Banking studies and business administration
    national_label_local: "\u062B\u0627\u0646\u0648\u064A\u0629 \u0627\u0644\u0639\
      \u0644\u0648\u0645 \u0627\u0644\u0645\u0635\u0631\u0641\u064A\u0629 \u0648\u0627\
      \u062F\u0627\u0631\u0629 \u0627\u0644\u0627\u0639\u0645\u0627\u0644"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 18
    parent_country_entry_ids:
    - QAT-EDU-05
    - QAT-EDU-07
    cum_years_schooling: 12
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
  - country_entry_id: QAT-EDU-13
    national_label_en: Science and technology secondary
    national_label_local: "\u062B\u0627\u0646\u0648\u064A\u0629 \u0627\u0644\u0639\
      \u0644\u0648\u0645 \u0648\u0627\u0644\u062A\u0643\u0646\u0648\u0644\u0648\u062C\
      \u064A\u0627"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 19
    parent_country_entry_ids:
    - QAT-EDU-05
    - QAT-EDU-07
    cum_years_schooling: 12
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
  - country_entry_id: QAT-EDU-14
    national_label_en: Foundation programme
    national_label_local: "\u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062C \u0627\
      \u0644\u062A\u0623\u0633\u064A\u0633\u064A"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - QAT-EDU-08
    - QAT-EDU-12
    - QAT-EDU-13
    cum_years_schooling: 13
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    - QAT-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
    - 'minimum parent path selected from: QAT-EDU-08, QAT-EDU-12, QAT-EDU-13'
  - country_entry_id: QAT-EDU-15
    national_label_en: Diploma
    national_label_local: "\u062F\u0628\u0644\u0648\u0645"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - QAT-EDU-08
    - QAT-EDU-12
    - QAT-EDU-13
    cum_years_schooling: 14
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    - QAT-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
    - 'minimum parent path selected from: QAT-EDU-08, QAT-EDU-12, QAT-EDU-13'
  - country_entry_id: QAT-EDU-16
    national_label_en: Diploma
    national_label_local: "\u062F\u0628\u0644\u0648\u0645"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - QAT-EDU-08
    - QAT-EDU-12
    - QAT-EDU-13
    cum_years_schooling: 14
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    - QAT-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
    - 'minimum parent path selected from: QAT-EDU-08, QAT-EDU-12, QAT-EDU-13'
  - country_entry_id: QAT-EDU-17
    national_label_en: Bachelor
    national_label_local: "\u0628\u0643\u0627\u0644\u0648\u0631\u064A\u0648\u0633"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - QAT-EDU-08
    - QAT-EDU-12
    - QAT-EDU-13
    cum_years_schooling: 16
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    - QAT-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
    - 'minimum parent path selected from: QAT-EDU-08, QAT-EDU-12, QAT-EDU-13'
  - country_entry_id: QAT-EDU-18
    national_label_en: Bachelor in pharmacy / architecture / engineering
    national_label_local: "\u0628\u0643\u0627\u0644\u0648\u0631\u064A\u0648\u0633\
      \ \u0641\u064A \u0627\u0644\u0635\u064A\u062F\u0644\u0629 / \u0627\u0644\u0647\
      \u0646\u062F\u0633\u0629 / \u0627\u0644\u0647\u0646\u062F\u0633\u0629 \u0627\
      \u0644\u0645\u0639\u0645\u0627\u0631\u064A\u0629"
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - QAT-EDU-08
    - QAT-EDU-12
    - QAT-EDU-13
    cum_years_schooling: 17
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    - QAT-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
    - 'minimum parent path selected from: QAT-EDU-08, QAT-EDU-12, QAT-EDU-13'
  - country_entry_id: QAT-EDU-19
    national_label_en: Higher diploma
    national_label_local: "\u062F\u0628\u0644\u0648\u0645 \u0639\u0627\u0644\u064A"
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - QAT-EDU-08
    - QAT-EDU-12
    - QAT-EDU-13
    cum_years_schooling: 13
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    - QAT-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
    - 'minimum parent path selected from: QAT-EDU-08, QAT-EDU-12, QAT-EDU-13'
  - country_entry_id: QAT-EDU-20
    national_label_en: Bachelor in medicine
    national_label_local: "\u0628\u0643\u0627\u0644\u0648\u0631\u064A\u0648\u0633\
      \ \u0641\u064A \u0627\u0644\u0637\u0628"
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - QAT-EDU-08
    - QAT-EDU-12
    - QAT-EDU-13
    cum_years_schooling: 18
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    - QAT-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
    - 'minimum parent path selected from: QAT-EDU-08, QAT-EDU-12, QAT-EDU-13'
  - country_entry_id: QAT-EDU-21
    national_label_en: Master
    national_label_local: "\u0627\u0644\u0645\u0627\u062C\u0633\u062A\u064A\u0631"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - QAT-EDU-17
    - QAT-EDU-18
    - QAT-EDU-19
    cum_years_schooling: 15
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    - QAT-EDU-19
    - QAT-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
    - 'minimum parent path selected from: QAT-EDU-08, QAT-EDU-12, QAT-EDU-13'
    - 'minimum parent path selected from: QAT-EDU-17, QAT-EDU-18, QAT-EDU-19'
  - country_entry_id: QAT-EDU-22
    national_label_en: Doctoral
    national_label_local: "\u062F\u0643\u062A\u0648\u0631\u0627\u0647"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - QAT-EDU-20
    - QAT-EDU-21
    cum_years_schooling: 18
    cum_years_computation_path:
    - QAT-EDU-03
    - QAT-EDU-05
    - QAT-EDU-08
    - QAT-EDU-19
    - QAT-EDU-21
    - QAT-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: QAT-EDU-05, QAT-EDU-07'
    - 'minimum parent path selected from: QAT-EDU-08, QAT-EDU-12, QAT-EDU-13'
    - 'minimum parent path selected from: QAT-EDU-17, QAT-EDU-18, QAT-EDU-19'
    - 'minimum parent path selected from: QAT-EDU-20, QAT-EDU-21'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Qatar.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

