---
country_id: CTY-KIR
iso3: KIR
schema_version: '0.2'
status: draft
country_name: KIR
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: KIR-EDU-01
    national_label_en: Preschool
    national_label_local: Preschool
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: KIR-EDU-02
    national_label_en: Primary
    national_label_local: Primary Education (years 1-6)
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
  - country_entry_id: KIR-EDU-03
    national_label_en: Junior Secondary (Year 7 to 9)
    national_label_local: Junior Secondary (Year 7 to 9)
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - country_entry_id: KIR-EDU-04
    national_label_en: Senior Secondary (Year 10 and 11)
    national_label_local: Senior Secondary (Year 10 and 11)
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 10
  - country_entry_id: KIR-EDU-05
    national_label_en: Senior Secondary Year 12
    national_label_local: Senior Secondary Year 12
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 11
  - country_entry_id: KIR-EDU-06
    national_label_en: Senior Secondary Year 13 (SPBEA)
    national_label_local: Senior Secondary Year 13 (SPBEA)
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: KIR-EDU-07
    national_label_en: Senior Secondary Year 13 Foundation (USP)
    national_label_local: Senior Secondary Year 13 Foundation (USP)
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
  - country_entry_id: KIR-EDU-08
    national_label_en: Technical, Colleges and Vocational (TVET)
    national_label_local: Technical, Colleges and Vocational (TVET)
    entry_age: 17
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
  - country_entry_id: KIR-EDU-09
    national_label_en: Pastoral/Theological Institutes
    national_label_local: Pastoral/Theological Institutes
    entry_age: 17
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
  - country_entry_id: KIR-EDU-10
    national_label_en: University of South Pacific Bachelor degree
    national_label_local: University of South Pacific Bachelor degree
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Kiribati.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2024
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: KIR-SUBNAT-01
    survey_labels: 1-South Tarawa
    survey_variables: subnatid1
    gmd_subnatid1: KIR_2024_GAUL1_4002
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: gaul1_code
    geo_id: '4002'
    geo_nvar: gaul1_name
    geo_name: South Tarawa
    source_row: 8897
  - country_entry_id: KIR-SUBNAT-02
    survey_labels: 2-Northern
    survey_variables: subnatid1
    gmd_subnatid1: KIR_2024_GAUL1_4001
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: gaul1_code
    geo_id: '4001'
    geo_nvar: gaul1_name
    geo_name: Northern
    source_row: 8898
  - country_entry_id: KIR-SUBNAT-03
    survey_labels: 3-Central
    survey_variables: subnatid1
    gmd_subnatid1: KIR_2024_GAUL1_3999
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: gaul1_code
    geo_id: '3999'
    geo_nvar: gaul1_name
    geo_name: Central
    source_row: 8899
  - country_entry_id: KIR-SUBNAT-04
    survey_labels: 4-Southern
    survey_variables: subnatid1
    gmd_subnatid1: KIR_2024_GAUL1_4003
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: gaul1_code
    geo_id: '4003'
    geo_nvar: gaul1_name
    geo_name: Southern
    source_row: 8900
  - country_entry_id: KIR-SUBNAT-05
    survey_labels: 5-Linix
    survey_variables: subnatid1
    gmd_subnatid1: KIR_2024_GAUL1_4000
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: gaul1_code
    geo_id: '4000'
    geo_nvar: gaul1_name
    geo_name: Line Is. & Phoenix
    source_row: 8901
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: KIR-SAN-01
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: KIR-SAN-02
    source_category_code: to_open_drain
    national_label_en: to open drain
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: KIR-SAN-03
    source_category_code: to_piped_sewer_system
    national_label_en: to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: KIR-SAN-04
    source_category_code: to_pit
    national_label_en: to pit
    national_label_local: to pit
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: KIR-SAN-05
    source_category_code: to_septic_tank
    national_label_en: to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: KIR-SAN-06
    source_category_code: to_do_not_know_where
    national_label_en: to do not know where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: KIR-SAN-07
    source_category_code: own_flush_septic_tank
    national_label_en: Own flush septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 74
  - country_entry_id: KIR-SAN-08
    source_category_code: shared_flush_toilet
    national_label_en: Shared flush toilet
    national_label_local: Public/shared flush/toilet
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: KIR-SAN-09
    source_category_code: public_sewege_system
    national_label_en: Public sewege system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: KIR-SAN-10
    source_category_code: closet_over_sea_or_water_long_drop
    national_label_en: Closet over sea or water (long drop)
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: KIR-SAN-11
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet/hanging latrine
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: KIR-SAN-12
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
  - country_entry_id: KIR-SAN-13
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
  - country_entry_id: KIR-SAN-14
    source_category_code: household_pit
    national_label_en: Household pit
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: KIR-SAN-15
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
  - country_entry_id: KIR-SAN-16
    source_category_code: no_facility_bush_field_beach
    national_label_en: No facility/bush/field/beach
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: KIR-SAN-17
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
  - country_entry_id: KIR-SAN-18
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_KIR_Kiribati_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: KIR-WAS-01
    source_category_code: well_in_yard
    national_label_en: Well in yard
    national_label_local: Private
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - country_entry_id: KIR-WAS-02
    source_category_code: public_well
    national_label_en: Public well
    national_label_local: Public
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 56
  - country_entry_id: KIR-WAS-03
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: KIR-WAS-04
    source_category_code: tubewell_borehole
    national_label_en: Tubewell, borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: KIR-WAS-05
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: KIR-WAS-06
    source_category_code: cart_with_small_tank
    national_label_en: Cart with small tank
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: KIR-WAS-07
    source_category_code: water_kiosk
    national_label_en: Water kiosk
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: KIR-WAS-08
    source_category_code: desalination_plant_water
    national_label_en: Desalination plant water
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 104
  - country_entry_id: KIR-WAS-09
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: KIR-WAS-10
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
  - country_entry_id: KIR-WAS-11
    source_category_code: other_including_tanker_truck
    national_label_en: Other (including tanker truck)
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: KIR-WAS-12
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
  - country_entry_id: KIR-WAS-13
    source_category_code: rain_water_tank
    national_label_en: Rain water tank
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: KIR-WAS-14
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
  - country_entry_id: KIR-WAS-15
    source_category_code: piped_into_neighbourhood_or_outside_neighbourhood
    national_label_en: Piped into neighbourhood or outside neighbourhood
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: KIR-WAS-16
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
  - country_entry_id: KIR-WAS-17
    source_category_code: piped_into_household_yard
    national_label_en: Piped into household/yard
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: KIR-WAS-18
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: KIR-WAS-19
    source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: KIR-WAS-20
    source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_KIR_Kiribati_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

