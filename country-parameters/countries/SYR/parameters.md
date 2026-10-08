---
country_id: CTY-SYR
iso3: SYR
schema_version: '0.2'
status: draft
country_name: SYR
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SYR-EDU-01
    national_label_en: Early childhood education
    national_label_local: "\u0631\u064A\u0627\u0636 \u0627\u0644\u0623\u0637\u0641\
      \u0627\u0644"
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
  - country_entry_id: SYR-EDU-02
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
    - SYR-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: SYR-EDU-03
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
    source_row: 9
    parent_country_entry_ids:
    - SYR-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-04
    national_label_en: General secondary education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A \u0627\u0644\u0639\u0627\u0645"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - SYR-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-05
    national_label_en: Vocational secondary education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A \u0627\u0644\u0645\u0647\u0646\u064A"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - SYR-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-06
    national_label_en: Technical institute programmes /  Certified Assistant
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0645\u0639\
      \u0627\u0647\u062F \u0627\u0644\u0641\u0646\u064A\u0651\u0629 / \u0645\u0633\
      \u0627\u0639\u062F \u0645\u062C\u0627\u0632"
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 12
    parent_country_entry_ids:
    - SYR-EDU-04
    cum_years_schooling: 14
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-07
    national_label_en: Technical Institutes programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0645\u0639\
      \u0627\u0647\u062F \u0627\u0644\u062A\u0642\u0646\u064A\u0629"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
    parent_country_entry_ids:
    - SYR-EDU-04
    cum_years_schooling: 14
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-08
    national_label_en: Bachelor's programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0628\u0643\
      \u0627\u0644\u0648\u0631\u064A\u0648\u0633"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - SYR-EDU-04
    cum_years_schooling: 16
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-09
    national_label_en: Higher Institute of Business Administration Programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0645\u0639\
      \u0647\u062F \u0627\u0644\u0639\u0627\u0644\u064A \u0644\u0625\u062F\u0627\u0631\
      \u0629 \u0627\u0644\u0623\u0639\u0645\u0627\u0644"
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - SYR-EDU-04
    cum_years_schooling: 17
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-10
    national_label_en: Engineering Sciences and Medical Sciences (Dentistry, Pharmacy)
      programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0639\u0644\
      \u0648\u0645 \u0627\u0644\u0647\u0646\u062F\u0633\u064A\u0629 \u0648\u0627\u0644\
      \u0639\u0644\u0648\u0645 \u0627\u0644\u0637\u0628\u064A\u0629 (\u0637\u0628\
      \ \u0627\u0644\u0623\u0633\u0646\u0627\u0646 - \u0627\u0644\u0635\u064A\u062F\
      \u0644\u0629)"
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - SYR-EDU-04
    cum_years_schooling: 17
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-11
    national_label_en: Education Qualification Programme
    national_label_local: "\u0628\u0631\u0646\u0627\u0645\u062C \u0627\u0644\u062A\
      \u0623\u0647\u064A\u0644 \u0627\u0644\u062A\u0631\u0628\u0648\u064A"
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - SYR-EDU-04
    cum_years_schooling: 13
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-12
    national_label_en: Human Medicine Programme
    national_label_local: "\u0628\u0631\u0646\u0627\u0645\u062C \u0627\u0644\u0637\
      \u0628 \u0627\u0644\u0628\u0634\u0631\u064A"
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - SYR-EDU-04
    cum_years_schooling: 18
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-13
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
    source_row: 19
    parent_country_entry_ids:
    - SYR-EDU-08
    - SYR-EDU-09
    - SYR-EDU-10
    - SYR-EDU-11
    cum_years_schooling: 15
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-11
    - SYR-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SYR-EDU-08, SYR-EDU-09, SYR-EDU-10, SYR-EDU-11'
  - country_entry_id: SYR-EDU-14
    national_label_en: Qualification and Specialization Programme
    national_label_local: "\u0628\u0631\u0646\u0627\u0645\u062C  \u0627\u0644\u062A\
      \u0623\u0647\u064A\u0644 \u0648\u0627\u0644\u062A\u062E\u0635\u0635"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - SYR-EDU-04
    cum_years_schooling: 14
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-14
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SYR-EDU-15
    national_label_en: Doctorate programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u062F\u0643\
      \u062A\u0648\u0631\u0627\u0647"
    entry_age: 24
    duration_years: 2
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - SYR-EDU-12
    - SYR-EDU-13
    - SYR-EDU-14
    cum_years_schooling: 16
    cum_years_computation_path:
    - SYR-EDU-02
    - SYR-EDU-03
    - SYR-EDU-04
    - SYR-EDU-14
    - SYR-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SYR-EDU-12, SYR-EDU-13, SYR-EDU-14'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Template
      En Syrian Arab Republic.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SYR-SAN-01
    source_category_code: surface_run_off
    national_label_en: Surface run-off
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: SYR-SAN-02
    source_category_code: connection_to_sewer_network
    national_label_en: Connection to sewer network
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
  - country_entry_id: SYR-SAN-03
    source_category_code: connection_to_hh_septic_tank_or_cesspit
    national_label_en: Connection to HH septic tank or cesspit
    national_label_local: "\u0644\u062E\u0632\u0627\u0646 \u0627\u0644\u0635\u0631\
      \u0641 \u0627\u0644\u0635\u062D\u064A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: SYR-SAN-04
    source_category_code: flush_toilet_not_connected
    national_label_en: Flush toilet not connected
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u0622\u062E\
      \u0631"
    jmp_classification: Flush/toilets > Private flush/toilet > to elsewhere
    jmp_id: flush_toilets.private_flush_toilet.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 77
  - country_entry_id: SYR-SAN-05
    source_category_code: flush_toilet_connected
    national_label_en: Flush toilet connected
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
  - country_entry_id: SYR-SAN-06
    source_category_code: toilet_connected
    national_label_en: Toilet connected
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
  - country_entry_id: SYR-SAN-07
    source_category_code: toilet_connected_to_closed_pit
    national_label_en: Toilet connected to closed pit
    national_label_local: "\u0644\u0644\u062D\u0641\u0631"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to pit
    jmp_id: flush_toilets.public_shared_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 81
  - country_entry_id: SYR-SAN-08
    source_category_code: public_toilet
    national_label_en: Public toilet
    national_label_local: "\u0625\u0644\u0649 \u0645\u0643\u0627\u0646 \u063A\u064A\
      \u0631 \u0645\u0639\u0631\u0648\u0641 / \u0644\u0633\u062A \u0645\u062A\u0623\
      \u0643\u062F\u064B\u0627 / \u0644\u0627 \u0623\u0639\u0631\u0641"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to unknown place/
      not sure/DK
    jmp_id: flush_toilets.public_shared_flush_toilet.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: true
    source_row: 82
  - country_entry_id: SYR-SAN-09
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
  - country_entry_id: SYR-SAN-10
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
  - country_entry_id: SYR-SAN-11
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
  - country_entry_id: SYR-SAN-12
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
  - country_entry_id: SYR-SAN-13
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
  - country_entry_id: SYR-SAN-14
    source_category_code: open_air
    national_label_en: Open air
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: SYR-SAN-15
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_SYR_Syria_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SYR-WAS-01
    source_category_code: springs
    national_label_en: Springs
    national_label_local: "\u0643\u0644 \u0627\u0644\u064A\u0646\u0627\u0628\u064A\
      \u0639"
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 74
  - country_entry_id: SYR-WAS-02
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
  - country_entry_id: SYR-WAS-03
    source_category_code: supervised_spring
    national_label_en: Supervised spring
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u0627\u0644\u0645\u062D\
      \u0645\u064A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: SYR-WAS-04
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
  - country_entry_id: SYR-WAS-05
    source_category_code: closed_well_individual_household
    national_label_en: Closed well (Individual Household)
    national_label_local: "\u062E\u0627\u0635"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SYR-WAS-06
    source_category_code: closed_well_individual
    national_label_en: Closed well individual
    national_label_local: "\u062E\u0627\u0635"
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: SYR-WAS-07
    source_category_code: closed_well_network
    national_label_en: Closed well (Network)
    national_label_local: "\u0639\u0627\u0645"
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 68
  - country_entry_id: SYR-WAS-08
    source_category_code: closed_well_network
    national_label_en: Closed well network
    national_label_local: "\u0639\u0627\u0645"
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 68
  - country_entry_id: SYR-WAS-09
    source_category_code: regular_well
    national_label_en: Regular well
    national_label_local: "\u0627\u0644\u0622\u0628\u0627\u0631 \u0627\u0644\u062A\
      \u0642\u0644\u064A\u062F\u064A\u0629"
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 62
  - country_entry_id: SYR-WAS-10
    source_category_code: artesian_well
    national_label_en: Artesian well
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: SYR-WAS-11
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
  - country_entry_id: SYR-WAS-12
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
  - country_entry_id: SYR-WAS-13
    source_category_code: unsupervised_spring
    national_label_en: Unsupervised spring
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u063A\u064A\u0631 \u0627\
      \u0644\u0645\u062D\u0645\u064A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: SYR-WAS-14
    source_category_code: open_well
    national_label_en: Open well
    national_label_local: "\u0628\u0626\u0631 \u063A\u064A\u0631 \u0645\u062D\u0645\
      \u064A"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: SYR-WAS-15
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
  - country_entry_id: SYR-WAS-16
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
  - country_entry_id: SYR-WAS-17
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SYR-WAS-18
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
  - country_entry_id: SYR-WAS-19
    source_category_code: water_trucking
    national_label_en: Water trucking
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: SYR-WAS-20
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: SYR-WAS-21
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
  - country_entry_id: SYR-WAS-22
    source_category_code: rain_water
    national_label_en: Rain water
    national_label_local: "\u0645\u064A\u0627\u0647 \u0627\u0644\u0623\u0645\u0637\
      \u0627\u0631"
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 86
  - country_entry_id: SYR-WAS-23
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
  - country_entry_id: SYR-WAS-24
    source_category_code: river_lake
    national_label_en: River/lake
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: SYR-WAS-25
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
  - country_entry_id: SYR-WAS-26
    source_category_code: lake
    national_label_en: Lake
    national_label_local: "\u0628\u062D\u064A\u0631\u0629"
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 94
  - country_entry_id: SYR-WAS-27
    source_category_code: river
    national_label_en: River
    national_label_local: "\u0646\u0647\u0631"
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: SYR-WAS-28
    source_category_code: network
    national_label_en: Network
    national_label_local: "\u0627\u062A\u0635\u0627\u0644\u0627\u062A \u0627\u0644\
      \u0645\u0646\u0632\u0644"
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: SYR-WAS-29
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
  - country_entry_id: SYR-WAS-30
    source_category_code: piped_supply
    national_label_en: Piped supply
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: SYR-WAS-31
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
  - country_entry_id: SYR-WAS-32
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
  - country_entry_id: SYR-WAS-33
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_SYR_Syria_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 2001
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

