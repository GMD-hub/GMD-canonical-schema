---
country_id: CTY-OMN
iso3: OMN
schema_version: '0.2'
status: draft
country_name: OMN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: OMN-EDU-01
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
  - country_entry_id: OMN-EDU-02
    national_label_en: Kindergarten
    national_label_local: "\u0631\u064A\u0627\u0636 \u0627\u0644\u0623\u0637\u0641\
      \u0627\u0644"
    entry_age: 3
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
  - country_entry_id: OMN-EDU-03
    national_label_en: Grades 1-4 of basic education
    national_label_local: "\u0627\u0644\u0635\u0641\u0648\u0641 1-4 \u0645\u0646 \u0627\
      \u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\u0623\u0633\u0627\u0633\u064A"
    entry_age: 6
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - OMN-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: OMN-EDU-04
    national_label_en: Grades 5-10 of basic education
    national_label_local: "\u0627\u0644\u0635\u0641\u0648\u0641 5-10 \u0645\u0646\
      \ \u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\u0623\u0633\u0627\u0633\
      \u064A"
    entry_age: 10
    duration_years: 6
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - OMN-EDU-03
    cum_years_schooling: 10
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: OMN-EDU-05
    national_label_en: "Grades 7-10 \nRoyal Guard of Oman Technical College"
    national_label_local: "\u0627\u0644\u0635\u0641\u0648\u0641 7-10 \n\u0643\u0644\
      \u064A\u0629 \u0627\u0644\u062D\u0631\u0633 \u0627\u0644\u0633\u0644\u0637\u0627\
      \u0646\u064A \u0627\u0644\u0639\u0645\u0627\u0646\u064A \u0627\u0644\u062A\u0642\
      \u0646\u064A\u0629"
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - OMN-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: OMN-EDU-06
    national_label_en: Grades 11-12 after basic education
    national_label_local: "\u0627\u0644\u0635\u0641\u0627\u064611-12 \u0645\u0646\
      \ \u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0628\u0639\u062F \u0627\u0644\
      \u0623\u0633\u0627\u0633\u064A"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - OMN-EDU-04
    - OMN-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    cum_years_status: computed
    review_flags: &id002
    - 'minimum parent path selected from: OMN-EDU-04, OMN-EDU-05'
  - country_entry_id: OMN-EDU-07
    national_label_en: Vocational and Technical Education
    national_label_local: "\u0646\u0638\u0627\u0645 \u0627\u0644\u062A\u0639\u0644\
      \u064A\u0645 \u0627\u0644\u0645\u0647\u0646\u064A \u0648\u0627\u0644\u062A\u0642\
      \u0646\u064A"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - OMN-EDU-04
    - OMN-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: OMN-EDU-04, OMN-EDU-05'
  - country_entry_id: OMN-EDU-08
    national_label_en: 'Vocational education (1): Apprenticeship + short courses'
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0645\u0647\u0646\u064A (1) : \u0627\u0644\u062A\u0644\u0645\u0630\u0629 \u0627\
      \u0644\u0645\u0647\u0646\u064A\u0629 +\u0627\u0644\u062F\u0648\u0631\u0627\u062A\
      \ \u0627\u0644\u062A\u062F\u0631\u064A\u0628\u064A\u0629 \u0627\u0644\u0645\u0647\
      \u0646\u064A\u0629"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - OMN-EDU-04
    - OMN-EDU-05
    cum_years_schooling: 9
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: OMN-EDU-04, OMN-EDU-05'
  - country_entry_id: OMN-EDU-09
    national_label_en: 'Vocational education (2): Apprenticeship + short courses'
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0645\u0647\u0646\u064A (2) : \u0627\u0644\u062A\u0644\u0645\u0630\u0629 \u0627\
      \u0644\u0645\u0647\u0646\u064A\u0629 +\u0627\u0644\u062F\u0648\u0631\u0627\u062A\
      \ \u0627\u0644\u062A\u062F\u0631\u064A\u0628\u064A\u0629 \u0627\u0644\u0645\u0647\
      \u0646\u064A\u0629"
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - OMN-EDU-04
    - OMN-EDU-05
    cum_years_schooling: 9
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: OMN-EDU-04, OMN-EDU-05'
  - country_entry_id: OMN-EDU-10
    national_label_en: "Grades 11-12 \nRoyal Guard of Oman Technical College"
    national_label_local: "\u0627\u0644\u0635\u0641\u0627\u0646 (11-12) \u0643\u0644\
      \u064A\u0629 \u0627\u0644\u062D\u0631\u0633 \u0627\u0644\u0633\u0644\u0637\u0627\
      \u0646\u064A \u0627\u0644\u0639\u0645\u0627\u0646\u064A \u0627\u0644\u062A\u0642\
      \u0646\u064A\u0629"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - OMN-EDU-04
    - OMN-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: OMN-EDU-04, OMN-EDU-05'
  - country_entry_id: OMN-EDU-11
    national_label_en: Diploma programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u062F\u0628\
      \u0644\u0648\u0645"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - OMN-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-11
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: OMN-EDU-12
    national_label_en: Vocational diploma programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u062F\u0628\
      \u0644\u0648\u0645 \u0627\u0644\u0645\u0647\u0646\u064A"
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - OMN-EDU-06
    cum_years_schooling: 13
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-12
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: OMN-EDU-13
    national_label_en: Bachelor's  programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0628\u0643\
      \u0627\u0644\u0648\u0631\u064A\u0648\u0633"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - OMN-EDU-06
    cum_years_schooling: 14
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-13
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: OMN-EDU-14
    national_label_en: Legal Accounting certificate
    national_label_local: "\u0634\u0647\u0627\u062F\u0629 \u0627\u0644\u0645\u062D\
      \u0627\u0633\u0628\u0629 \u0627\u0644\u0642\u0627\u0646\u0648\u0646\u064A\u0629"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - OMN-EDU-06
    cum_years_schooling: 13
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-14
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: OMN-EDU-15
    national_label_en: Bachelor's programmes in engineering
    national_label_local: "\u0628\u0631\u0646\u0627\u0645\u062C \u0628\u0643\u0627\
      \u0644\u0648\u0631\u064A\u0648\u0633 \u0641\u064A \u0627\u0644\u0647\u0646\u062F\
      \u0633\u0629"
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - OMN-EDU-06
    cum_years_schooling: 15
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-15
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: OMN-EDU-16
    national_label_en: Higher diploma program
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u062F\u0628\
      \u0644\u0648\u0645 \u0627\u0644\u0639\u0627\u0644\u064A"
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - OMN-EDU-06
    cum_years_schooling: 11
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-16
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: OMN-EDU-17
    national_label_en: Diploma in Educational  Qualification
    national_label_local: "\u062F\u0628\u0644\u0648\u0645 \u0627\u0644\u062A\u0623\
      \u0647\u064A\u0644 \u0627\u0644\u062A\u0631\u0628\u0648\u064A"
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - OMN-EDU-06
    cum_years_schooling: 11
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-17
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: OMN-EDU-18
    national_label_en: Bachelor's program in medicine
    national_label_local: "\u0628\u0631\u0646\u0627\u0645\u062C \u0627\u0644\u0628\
      \u0643\u0627\u0644\u0648\u0631\u064A\u0648\u0633 \u0641\u064A \u0627\u0644\u0637\
      \u0628"
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - OMN-EDU-06
    cum_years_schooling: 16
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-18
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: OMN-EDU-19
    national_label_en: Master's  programs
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0645\u0627\
      \u062C\u0633\u062A\u064A\u0631"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - OMN-EDU-13
    - OMN-EDU-14
    - OMN-EDU-15
    - OMN-EDU-16
    - OMN-EDU-17
    cum_years_schooling: 13
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-16
    - OMN-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: OMN-EDU-04, OMN-EDU-05'
    - 'minimum parent path selected from: OMN-EDU-13, OMN-EDU-14, OMN-EDU-15, OMN-EDU-16,
      OMN-EDU-17'
  - country_entry_id: OMN-EDU-20
    national_label_en: Doctoral programs
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u062F\u0643\
      \u062A\u0648\u0631\u0627\u0647"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - OMN-EDU-18
    - OMN-EDU-19
    cum_years_schooling: 16
    cum_years_computation_path:
    - OMN-EDU-03
    - OMN-EDU-05
    - OMN-EDU-06
    - OMN-EDU-16
    - OMN-EDU-19
    - OMN-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: OMN-EDU-04, OMN-EDU-05'
    - 'minimum parent path selected from: OMN-EDU-13, OMN-EDU-14, OMN-EDU-15, OMN-EDU-16,
      OMN-EDU-17'
    - 'minimum parent path selected from: OMN-EDU-18, OMN-EDU-19'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Oman.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 2005
  effective_to: null
  selectors: null
  value: 15
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

