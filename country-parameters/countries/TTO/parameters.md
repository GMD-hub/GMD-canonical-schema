---
country_id: CTY-TTO
iso3: TTO
schema_version: '0.2'
status: draft
country_name: TTO
parameters:
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: TTO-SAN-01
    source_category_code: flush_pour_flush_flush_to_open_drain
    national_label_en: 'flush / pour flush: flush to open drain'
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: TTO-SAN-02
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: TTO-SAN-03
    source_category_code: flush_pour_flush_flush_to_piped_sewer_system
    national_label_en: 'flush / pour flush: flush to piped sewer system'
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: TTO-SAN-04
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: TTO-SAN-05
    source_category_code: flush_pour_flush_flush_to_pit_latrine
    national_label_en: 'flush / pour flush: flush to pit latrine'
    national_label_local: to pit
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: TTO-SAN-06
    source_category_code: flush_pour_flush_flush_to_septic_tank
    national_label_en: 'flush / pour flush: flush to septic tank'
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: TTO-SAN-07
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: TTO-SAN-08
    source_category_code: flush_pour_flush_flush_to_dk_where
    national_label_en: 'flush / pour flush: flush to dk where'
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: TTO-SAN-09
    source_category_code: flush_to_unknown_place_not_sure_dk_where
    national_label_en: Flush to unknown place / Not sure / DK where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: TTO-SAN-10
    source_category_code: flush
    national_label_en: Flush
    national_label_local: Flush/toilets
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: TTO-SAN-11
    source_category_code: flush_toilet
    national_label_en: Flush toilet
    national_label_local: Private flush/toilet
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: TTO-SAN-12
    source_category_code: flush_toilet_shared
    national_label_en: Flush toilet shared
    national_label_local: Public/shared flush/toilet
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: TTO-SAN-13
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: to elsewhere
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: TTO-SAN-14
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: TTO-SAN-15
    source_category_code: wc_linked_to_sewer
    national_label_en: WC linked to sewer
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: TTO-SAN-16
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: TTO-SAN-17
    source_category_code: wc_not_linked_to_sewer
    national_label_en: WC not linked to sewer
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: TTO-SAN-18
    source_category_code: flush_to_unknown_place_not_sure_dk_where
    national_label_en: Flush to unknown place/not sure/DK where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: TTO-SAN-19
    source_category_code: pit_latrine
    national_label_en: Pit latrine
    national_label_local: Dry latrines
    jmp_classification: Latrines > Dry latrines
    jmp_id: latrines.dry_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: no
    shared_flag: no
    source_row: 103
  - country_entry_id: TTO-SAN-20
    source_category_code: bucket
    national_label_en: Bucket
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: TTO-SAN-21
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: TTO-SAN-22
    source_category_code: pit_latrine_with_slab_covered_latrine
    national_label_en: Pit latrine with slab/covered latrine
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: TTO-SAN-23
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab / Open pit
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: TTO-SAN-24
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: TTO-SAN-25
    source_category_code: pit
    national_label_en: Pit
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: TTO-SAN-26
    source_category_code: traditional_pit
    national_label_en: Traditional pit
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: TTO-SAN-27
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated Improved Pit latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: TTO-SAN-28
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit latrine (VIP)
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: TTO-SAN-29
    source_category_code: no_facilities_or_bush_or_field
    national_label_en: No facilities or bush or field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: TTO-SAN-30
    source_category_code: no_facility
    national_label_en: No facility
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: TTO-SAN-31
    source_category_code: no_facility_bush_field
    national_label_en: No facility, Bush, Field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: TTO-SAN-32
    source_category_code: none
    national_label_en: None
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: TTO-SAN-33
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_TTO_Trinidad_and_Tobago_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: TTO-WAS-01
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: TTO-WAS-02
    source_category_code: spring_protected_spring
    national_label_en: 'spring: protected spring'
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: TTO-WAS-03
    source_category_code: protected_dug_well
    national_label_en: Protected dug well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: TTO-WAS-04
    source_category_code: tubewell_borehole_with_pump
    national_label_en: Tubewell/ borehole with pump
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: TTO-WAS-05
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: TTO-WAS-06
    source_category_code: dug_well_unprotected_well
    national_label_en: 'dug well: unprotected well'
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: TTO-WAS-07
    source_category_code: well_w_o_handpump
    national_label_en: Well w/o handpump
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: TTO-WAS-08
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank / drum
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: TTO-WAS-09
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank/drum
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: TTO-WAS-10
    source_category_code: other_improved_bottled
    national_label_en: Other improved (bottled)
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: TTO-WAS-11
    source_category_code: tanker_truck_provided
    national_label_en: Tanker truck provided
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: TTO-WAS-12
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker truck, vendor
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: TTO-WAS-13
    source_category_code: tanker_truck
    national_label_en: Tanker-truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: TTO-WAS-14
    source_category_code: truck_borne
    national_label_en: Truck borne
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: TTO-WAS-15
    source_category_code: truckborne_and_not_piped_into_dwelling
    national_label_en: TRUCKBORNE (AND NOT PIPED INTO DWELLING)
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: TTO-WAS-16
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: TTO-WAS-17
    source_category_code: private_catchment
    national_label_en: Private/catchment
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: TTO-WAS-18
    source_category_code: spring_river_well_pond
    national_label_en: SPRING/RIVER/WELL/POND
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: TTO-WAS-19
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: TTO-WAS-20
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: TTO-WAS-21
    source_category_code: packaged_water_bottled_water
    national_label_en: 'packaged water: bottled water'
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: TTO-WAS-22
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: Rainwater
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: TTO-WAS-23
    source_category_code: private_catchment_not_piped
    national_label_en: PRIVATE CATCHMENT, NOT PIPED
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: TTO-WAS-24
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: TTO-WAS-25
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: TTO-WAS-26
    source_category_code: river_spring_water
    national_label_en: River/ spring water
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: TTO-WAS-27
    source_category_code: spring_river
    national_label_en: Spring/ river
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: TTO-WAS-28
    source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: TTO-WAS-29
    source_category_code: surface_water_river_stream_dam_lake_pond_canal_irrigation_channel
    national_label_en: Surface water (river, stream, dam, lake, pond, canal, irrigation
      channel)
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: TTO-WAS-30
    source_category_code: piped_to_neighbour
    national_label_en: Piped to neighbour
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: TTO-WAS-31
    source_category_code: piped_water_piped_to_neighbour
    national_label_en: 'piped water: piped to neighbour'
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: TTO-WAS-32
    source_category_code: private_piped_into_dwelling
    national_label_en: PRIVATE PIPED INTO DWELLING
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: TTO-WAS-33
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: TTO-WAS-34
    source_category_code: piped_into_residence
    national_label_en: Piped into residence
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: TTO-WAS-35
    source_category_code: piped_water_piped_into_dwelling
    national_label_en: 'piped water: piped into dwelling'
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: TTO-WAS-36
    source_category_code: public_piped_into_dwelling
    national_label_en: PUBLIC PIPED  INTO DWELLING
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: TTO-WAS-37
    source_category_code: piped_into_compound_yard_or_plot
    national_label_en: Piped into compound, yard or plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: TTO-WAS-38
    source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: TTO-WAS-39
    source_category_code: piped_into_yard_plot
    national_label_en: Piped into yard/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: TTO-WAS-40
    source_category_code: piped_water_piped_to_yard_plot
    national_label_en: 'piped water: piped to yard / plot'
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: TTO-WAS-41
    source_category_code: public_piped_into_yard
    national_label_en: PUBLIC PIPED INTO YARD
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: TTO-WAS-42
    source_category_code: piped_water_public_tap_standpipe
    national_label_en: 'piped water: public tap / standpipe'
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: TTO-WAS-43
    source_category_code: public_standpipe
    national_label_en: PUBLIC STANDPIPE
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: TTO-WAS-44
    source_category_code: public_tap
    national_label_en: Public tap
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: TTO-WAS-45
    source_category_code: public_tap_standpipe
    national_label_en: Public tap / standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: TTO-WAS-46
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_TTO_Trinidad_and_Tobago_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

