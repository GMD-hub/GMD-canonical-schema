---
country_id: CTY-NRU
iso3: NRU
schema_version: '0.2'
status: draft
country_name: NRU
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: NRU-EDU-01
    national_label_en: Playcentre
    national_label_local: Playcentre
    entry_age: 3
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: NRU-EDU-02
    national_label_en: Pre-School
    national_label_local: Pre-School
    entry_age: 4
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: NRU-EDU-03
    national_label_en: Prep
    national_label_local: Prep
    entry_age: 5
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: NRU-EDU-04
    national_label_en: Primary Y1-Y6
    national_label_local: Primary
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - NRU-EDU-04
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: NRU-EDU-05
    national_label_en: Primary Y7-Y8
    national_label_local: Primary
    entry_age: 12
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    source_row: 11
    parent_country_entry_ids:
    - NRU-EDU-04
    cum_years_schooling: 8
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NRU-EDU-06
    national_label_en: Secondary Y9-Y10
    national_label_local: Secondary
    entry_age: 14
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    source_row: 12
    parent_country_entry_ids:
    - NRU-EDU-04
    cum_years_schooling: 8
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NRU-EDU-07
    national_label_en: Secondary Y11-Y12
    national_label_local: Secondary
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    source_row: 13
    parent_country_entry_ids:
    - NRU-EDU-05
    - NRU-EDU-06
    cum_years_schooling: 10
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-05
    - NRU-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NRU-EDU-05, NRU-EDU-06'
  - country_entry_id: NRU-EDU-08
    national_label_en: Secondary Y11-Y12
    national_label_local: Secondary
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    source_row: 14
    parent_country_entry_ids:
    - NRU-EDU-05
    - NRU-EDU-06
    cum_years_schooling: 10
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-05
    - NRU-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NRU-EDU-05, NRU-EDU-06'
  - country_entry_id: NRU-EDU-09
    national_label_en: TVET
    national_label_local: TVET
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    source_row: 15
    parent_country_entry_ids:
    - NRU-EDU-07
    - NRU-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-05
    - NRU-EDU-07
    - NRU-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NRU-EDU-05, NRU-EDU-06'
    - 'minimum parent path selected from: NRU-EDU-07, NRU-EDU-08'
  - country_entry_id: NRU-EDU-10
    national_label_en: Foundation USP
    national_label_local: Foundation USP
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    source_row: 16
    parent_country_entry_ids:
    - NRU-EDU-07
    - NRU-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-05
    - NRU-EDU-07
    - NRU-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NRU-EDU-05, NRU-EDU-06'
    - 'minimum parent path selected from: NRU-EDU-07, NRU-EDU-08'
  - country_entry_id: NRU-EDU-11
    national_label_en: Cert/Dip USP
    national_label_local: Cert/Dip USP
    entry_age: 19
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    source_row: 17
    parent_country_entry_ids:
    - NRU-EDU-07
    - NRU-EDU-08
    cum_years_schooling: 11
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-05
    - NRU-EDU-07
    - NRU-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NRU-EDU-05, NRU-EDU-06'
    - 'minimum parent path selected from: NRU-EDU-07, NRU-EDU-08'
  - country_entry_id: NRU-EDU-12
    national_label_en: Bachelor
    national_label_local: Bachelor degree + Post-graduate Dip/Cert
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    source_row: 18
    parent_country_entry_ids:
    - NRU-EDU-07
    - NRU-EDU-08
    cum_years_schooling: 13
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-05
    - NRU-EDU-07
    - NRU-EDU-12
    cum_years_status: computed
    review_flags: &id002
    - 'minimum parent path selected from: NRU-EDU-05, NRU-EDU-06'
    - 'minimum parent path selected from: NRU-EDU-07, NRU-EDU-08'
  - country_entry_id: NRU-EDU-13
    national_label_en: Masters
    national_label_local: Masters
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    source_row: 19
    parent_country_entry_ids:
    - NRU-EDU-12
    cum_years_schooling: 15
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-05
    - NRU-EDU-07
    - NRU-EDU-12
    - NRU-EDU-13
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: NRU-EDU-14
    national_label_en: Phd
    national_label_local: Phd
    entry_age: 24
    duration_years: 5
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    source_row: 20
    parent_country_entry_ids:
    - NRU-EDU-13
    cum_years_schooling: 20
    cum_years_computation_path:
    - NRU-EDU-04
    - NRU-EDU-05
    - NRU-EDU-07
    - NRU-EDU-12
    - NRU-EDU-13
    - NRU-EDU-14
    cum_years_status: computed
    review_flags: *id002
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Nauru.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: NRU-SAN-01
    source_category_code: to_open_drain
    national_label_en: to open drain
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: NRU-SAN-02
    source_category_code: to_piped_sewer_system
    national_label_en: to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: NRU-SAN-03
    source_category_code: to_pit
    national_label_en: to pit
    national_label_local: to pit
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: NRU-SAN-04
    source_category_code: to_septic_tank
    national_label_en: to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: NRU-SAN-05
    source_category_code: to_dk_where
    national_label_en: to DK where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: NRU-SAN-06
    source_category_code: bucket
    national_label_en: Bucket
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.private_latrines.bucket_latrine
    improved_flag: false
    shared_flag: false
    source_row: 118
  - country_entry_id: NRU-SAN-07
    source_category_code: pit_latrine_with_slab_covered_latrine
    national_label_en: Pit latrine with slab/covered latrine
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: NRU-SAN-08
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated Improved Pit latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    improved_flag: true
    shared_flag: false
    source_row: 113
  - country_entry_id: NRU-SAN-09
    source_category_code: no_facility_bush_field
    national_label_en: No facility, bush,field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: NRU-SAN-10
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_NRU_Nauru_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: NRU-WAS-01
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: NRU-WAS-02
    source_category_code: tanker_truck_desalination
    national_label_en: Tanker truck/desalination
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: NRU-WAS-03
    source_category_code: community_tank
    national_label_en: Community tank
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    improved_flag: true
    shared_flag: false
    source_row: 104
  - country_entry_id: NRU-WAS-04
    source_category_code: other
    national_label_en: other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: NRU-WAS-05
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: NRU-WAS-06
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: Rainwater
    jmp_classification: Rainwater
    jmp_id: rainwater
    improved_flag: true
    shared_flag: false
    source_row: 86
  - country_entry_id: NRU-WAS-07
    source_category_code: piped_to_neighbour
    national_label_en: Piped to neighbour
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: NRU-WAS-08
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: NRU-WAS-09
    source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    improved_flag: true
    shared_flag: false
    source_row: 40
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_NRU_Nauru_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

