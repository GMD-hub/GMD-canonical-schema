---
country_id: CTY-TKM
iso3: TKM
schema_version: '0.2'
status: draft
country_name: TKM
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: TKM-EDU-01
    national_label_en: Pre-primary education for young children
    national_label_local: ''
    entry_age: 1
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
  - country_entry_id: TKM-EDU-02
    national_label_en: Pre-primary education
    national_label_local: ''
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
  - country_entry_id: TKM-EDU-03
    national_label_en: Primary education
    national_label_local: ''
    entry_age: 6
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - TKM-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: TKM-EDU-04
    national_label_en: "General basic education \n(1st stage)"
    national_label_local: ''
    entry_age: 10
    duration_years: 6
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - TKM-EDU-03
    cum_years_schooling: 10
    cum_years_computation_path:
    - TKM-EDU-03
    - TKM-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TKM-EDU-05
    national_label_en: "General secondary education \n(2nd stage)"
    national_label_local: ''
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - TKM-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - TKM-EDU-03
    - TKM-EDU-04
    - TKM-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TKM-EDU-06
    national_label_en: Basic vocational education
    national_label_local: ''
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 12
    parent_country_entry_ids:
    - TKM-EDU-05
    cum_years_schooling: 13
    cum_years_computation_path:
    - TKM-EDU-03
    - TKM-EDU-04
    - TKM-EDU-05
    - TKM-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TKM-EDU-07
    national_label_en: Secondary vocational education
    national_label_local: ''
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
    parent_country_entry_ids:
    - TKM-EDU-05
    cum_years_schooling: 15
    cum_years_computation_path:
    - TKM-EDU-03
    - TKM-EDU-04
    - TKM-EDU-05
    - TKM-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TKM-EDU-08
    national_label_en: Bachelor
    national_label_local: ''
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - TKM-EDU-05
    cum_years_schooling: 16
    cum_years_computation_path:
    - TKM-EDU-03
    - TKM-EDU-04
    - TKM-EDU-05
    - TKM-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TKM-EDU-09
    national_label_en: "Higher professional education \n(Specialist)"
    national_label_local: ''
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - TKM-EDU-05
    cum_years_schooling: 17
    cum_years_computation_path:
    - TKM-EDU-03
    - TKM-EDU-04
    - TKM-EDU-05
    - TKM-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TKM-EDU-10
    national_label_en: Master
    national_label_local: ''
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - TKM-EDU-08
    cum_years_schooling: 18
    cum_years_computation_path:
    - TKM-EDU-03
    - TKM-EDU-04
    - TKM-EDU-05
    - TKM-EDU-08
    - TKM-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: TKM-EDU-11
    national_label_en: Aspirantura
    national_label_local: ''
    entry_age: 28
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - TKM-EDU-09
    - TKM-EDU-10
    cum_years_schooling: 20
    cum_years_computation_path:
    - TKM-EDU-03
    - TKM-EDU-04
    - TKM-EDU-05
    - TKM-EDU-09
    - TKM-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: TKM-EDU-09, TKM-EDU-10'
  - country_entry_id: TKM-EDU-12
    national_label_en: Doctorantura
    national_label_local: ''
    entry_age: 31
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - TKM-EDU-09
    - TKM-EDU-10
    cum_years_schooling: 20
    cum_years_computation_path:
    - TKM-EDU-03
    - TKM-EDU-04
    - TKM-EDU-05
    - TKM-EDU-09
    - TKM-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: TKM-EDU-09, TKM-EDU-10'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Turkmenistan.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: TKM-SAN-01
    source_category_code: to_open_drain
    national_label_en: to open drain
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: TKM-SAN-02
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: TKM-SAN-03
    source_category_code: to_piped_sewer_system
    national_label_en: to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: TKM-SAN-04
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit (latrine)
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: TKM-SAN-05
    source_category_code: to_pit
    national_label_en: to pit
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: TKM-SAN-06
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: TKM-SAN-07
    source_category_code: to_septic_tank
    national_label_en: to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: TKM-SAN-08
    source_category_code: to_don_t_know_where
    national_label_en: to don't know where
    national_label_local: "\u0432 \u043D\u0435\u0438\u0437\u0432\u0435\u0441\u0442\
      \u043D\u043E\u0435 \u043C\u0435\u0441\u0442\u043E/\u043D\u0435 \u0437\u043D\u0430\
      \u044E/\u043D\u0435 \u0443\u0432\u0435\u0440\u0435\u043D(\u0430)"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: TKM-SAN-09
    source_category_code: flush_to_piped_sewer_system_private
    national_label_en: Flush to piped sewer system - private
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: TKM-SAN-10
    source_category_code: flush_to_pit_latrine_private
    national_label_en: Flush to pit (latrine) - private
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > Private flush/toilet > to pit
    jmp_id: flush_toilets.private_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 75
  - country_entry_id: TKM-SAN-11
    source_category_code: flush_to_septic_tank_private
    national_label_en: Flush to septic tank - private
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: TKM-SAN-12
    source_category_code: flush_to_piped_sewer_system_shared
    national_label_en: Flush to piped sewer system - shared
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: TKM-SAN-13
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: TKM-SAN-14
    source_category_code: pit_latrine_with_slab_covered_latrine
    national_label_en: Pit latrine with slab/covered latrine
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: TKM-SAN-15
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0431\
      \u0435\u0437 \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\
      \u0438\u0442\u044B/\u0441 \u043E\u0442\u043A\u0440\u044B\u0442\u043E\u0439 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: TKM-SAN-16
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated Improved Pit latrine
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: TKM-SAN-17
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit latrine (VIP)
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: TKM-SAN-18
    source_category_code: pit_latrine_with_slab_private
    national_label_en: Pit latrine with slab - private
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: TKM-SAN-19
    source_category_code: ventilated_improved_pit_latrine_vip_private
    national_label_en: Ventilated Improved Pit latrine (VIP) - private
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 113
  - country_entry_id: TKM-SAN-20
    source_category_code: pit_latrine_with_slab_shared
    national_label_en: Pit latrine with slab - shared
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: TKM-SAN-21
    source_category_code: ventilated_improved_pit_latrine_vip_shared
    national_label_en: Ventilated Improved Pit latrine (VIP) - shared
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Ventilated
      Improved Pit latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 121
  - country_entry_id: TKM-SAN-22
    source_category_code: no_facilities_or_bush_or_field
    national_label_en: No facilities or bush or field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: TKM-SAN-23
    source_category_code: no_facility_bush_field
    national_label_en: No facility, bush, field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: TKM-SAN-24
    source_category_code: open_defecation_no_facility_bush_field
    national_label_en: Open defecation (no facility, bush, field)
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_TKM_Turkmenistan_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: TKM-WAS-01
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: "\u0417\u0430\u0449\u0438\u0449\u0451\u043D\u043D\u044B\u0439\
      \ \u0440\u043E\u0434\u043D\u0438\u043A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: TKM-WAS-02
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: "\u0417\u0430\u0449\u0438\u0449\u0451\u043D\u043D\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: TKM-WAS-03
    source_category_code: tubewell_borehole
    national_label_en: Tubewell, borehole
    national_label_local: "\u0422\u0440\u0443\u0431\u0447\u0430\u0442\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446, \u0441\u043A\u0432\u0430\u0436\
      \u0438\u043D\u0430"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: TKM-WAS-04
    source_category_code: tubewell_borehole
    national_label_en: Tubewell/borehole
    national_label_local: "\u0422\u0440\u0443\u0431\u0447\u0430\u0442\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446, \u0441\u043A\u0432\u0430\u0436\
      \u0438\u043D\u0430"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: TKM-WAS-05
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0439 \u0440\u043E\u0434\u043D\u0438\u043A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: TKM-WAS-06
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0439 \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: TKM-WAS-07
    source_category_code: cart_with_small_tank
    national_label_en: Cart with small tank
    national_label_local: "\u0422\u0435\u043B\u0435\u0436\u043A\u0430 \u0441 \u043D\
      \u0435\u0431\u043E\u043B\u044C\u0448\u0438\u043C \u0431\u0430\u043A\u043E\u043C\
      /\u0431\u043E\u0447\u043A\u043E\u0439"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: TKM-WAS-08
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank/drum
    national_label_local: "\u0422\u0435\u043B\u0435\u0436\u043A\u0430 \u0441 \u043D\
      \u0435\u0431\u043E\u043B\u044C\u0448\u0438\u043C \u0431\u0430\u043A\u043E\u043C\
      /\u0431\u043E\u0447\u043A\u043E\u0439"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: TKM-WAS-09
    source_category_code: cart_with_tank_drum
    national_label_en: cart with tank/drum
    national_label_local: "\u0422\u0435\u043B\u0435\u0436\u043A\u0430 \u0441 \u043D\
      \u0435\u0431\u043E\u043B\u044C\u0448\u0438\u043C \u0431\u0430\u043A\u043E\u043C\
      /\u0431\u043E\u0447\u043A\u043E\u0439"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: TKM-WAS-10
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: TKM-WAS-11
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: TKM-WAS-12
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "\u0411\u0443\u0442\u0438\u043B\u0438\u0440\u043E\u0432\u0430\
      \u043D\u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: TKM-WAS-13
    source_category_code: rain_water
    national_label_en: Rain water
    national_label_local: "\u041A\u0440\u044B\u0442\u0430\u044F \u0446\u0438\u0441\
      \u0442\u0435\u0440\u043D\u0430/\u0440\u0435\u0437\u0435\u0440\u0432\u0443\u0430\
      \u0440"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: TKM-WAS-14
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: "\u041A\u0440\u044B\u0442\u0430\u044F \u0446\u0438\u0441\
      \u0442\u0435\u0440\u043D\u0430/\u0440\u0435\u0437\u0435\u0440\u0432\u0443\u0430\
      \u0440"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: TKM-WAS-15
    source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: TKM-WAS-16
    source_category_code: surface_water_used_for_the_estimates
    national_label_en: Surface water used for the estimates
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: TKM-WAS-17
    source_category_code: piped_to_neighbour
    national_label_en: Piped to neighbour
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: TKM-WAS-18
    source_category_code: to_neighbour
    national_label_en: to neighbour
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: TKM-WAS-19
    source_category_code: into_dwelling
    national_label_en: into dwelling
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: TKM-WAS-20
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: TKM-WAS-21
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: TKM-WAS-22
    source_category_code: into_yard_plot
    national_label_en: into yard/plot
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: TKM-WAS-23
    source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: TKM-WAS-24
    source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: TKM-WAS-25
    source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: TKM-WAS-26
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_TKM_Turkmenistan_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 2012
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

