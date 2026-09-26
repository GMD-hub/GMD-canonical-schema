---
country_id: CTY-COM
iso3: COM
schema_version: '0.2'
status: draft
country_name: COM
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: COM-EDU-01
    national_label_en: Enseignement préscolaire
    national_label_local: Enseignement préscolaire
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: COM-EDU-02
    national_label_en: Enseignement primaire
    national_label_local: Enseignement primaire
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
  - country_entry_id: COM-EDU-03
    national_label_en: "Enseignement secondaire \n(1 er cycle)"
    national_label_local: "Enseignement secondaire \n(1 er  cycle)"
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - country_entry_id: COM-EDU-04
    national_label_en: 'Enseignement technique secondaire

      (1er cycle)'
    national_label_local: "Enseignement technique secondaire \n(1er cycle)"
    entry_age: 15
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
  - country_entry_id: COM-EDU-05
    national_label_en: "Enseignement secondaire \n(2 ème cycle)"
    national_label_local: "Enseignement secondaire \n(2 ème cycle)"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - country_entry_id: COM-EDU-06
    national_label_en: Enseignement secondaire technique et professionnel
    national_label_local: Enseignement secondaire technique et professionnel
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: COM-EDU-07
    national_label_en: 'Enseignement secondaire technique

      (2 e cycle)'
    national_label_local: 'Enseignement secondaire technique

      (2 ème cycle)'
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
  - country_entry_id: COM-EDU-08
    national_label_en: "Enseignement \npost -secondaire"
    national_label_local: "Enseignement \npost -secondaire"
    entry_age: 19
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - country_entry_id: COM-EDU-09
    national_label_en: Enseignement supérieur technique
    national_label_local: Enseignement supérieur technique
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - country_entry_id: COM-EDU-10
    national_label_en: Enseignement supérieur de formation des instituteurs
    national_label_local: Enseignement supérieur de formation des instituteurs
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: COM-EDU-11
    national_label_en: Enseignement supérieur professionnel
    national_label_local: Enseignement supérieur professsionnel
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: COM-EDU-12
    national_label_en: Enseignement supérieur (Licence)
    national_label_local: Enseignement supérieur (Licence)
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - country_entry_id: COM-EDU-13
    national_label_en: Enseignement supérieur (Master)
    national_label_local: Enseignement supérieur (Master)
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Comoros.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: COM-SUBNAT-01
    survey_labels: 1 - Mwali | 4 - Mwali
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: COM_2015_GAUL1_968
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COM_2015_GAUL1_968
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '968'
    geo_nvar: ADM1_NAME
    geo_name: Moheli
    source_row: 3064
  - country_entry_id: COM-SUBNAT-02
    survey_labels: 2 - Ndzouani | 3 - Ndzouani | 3 - Ndzuwani
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: COM_2015_GAUL1_967
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COM_2015_GAUL1_967
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '967'
    geo_nvar: ADM1_NAME
    geo_name: Anjouan
    source_row: 3065
  - country_entry_id: COM-SUBNAT-03
    survey_labels: 1 - Moroni | 3 - Ngazidja
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: COM_2015_GAUL1_969
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: COM_2015_GAUL1_969
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '969'
    geo_nvar: ADM1_NAME
    geo_name: Ngazidja
    source_row: 3066
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: null
  effective_to: 2014
  selectors:
    geo_year: unknown
  value:
  - country_entry_id: COM-SUBNAT-01
    survey_labels: 11 - FOMBONI | 12 - NIOUMACHOUA | 13 - DJANDO | 21 - MUTSAMUDU
      | 22 - OUANI | 23 - DOMONI | 24 - MREMANI | 25 - SIMA | 26 - MOYA | 31 - MORONI-BAMBAO
      | 32 - HAMBOU | 33 - MBADJINI OUEST | 34 - MBADJINI EST | 35 - OICHILI-DIMANI
      | 36 - HAMAHAMET-MBOINKOU | 37 - MITSAMIOULI | 38 - MBOUDE | 39 - ITSANDRA-HAMANVOU
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
    gmd_subnatidsurvey: ''
    geo_year: ''
    geo_source: ''
    geo_level: ''
    geo_idvar: ''
    geo_id: ''
    geo_nvar: ''
    geo_name: ''
    source_row: 3073
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: COM-WAS-01
    source_category_code: well
    national_label_en: Well
    national_label_local: Tous les puits
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 54
  - country_entry_id: COM-WAS-02
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: COM-WAS-03
    source_category_code: protected_dug_well
    national_label_en: Protected dug well
    national_label_local: Puits protegées
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: COM-WAS-04
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: Puits protegées
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: COM-WAS-05
    source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: Puits ou sources protégées
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: true
    shared_flag: false
    source_row: 46
  - country_entry_id: COM-WAS-06
    source_category_code: protected_tube_well_or_bore_hole
    national_label_en: Protected tube well or bore hole
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: COM-WAS-07
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
  - country_entry_id: COM-WAS-08
    source_category_code: tubewell_borehole_with_pump
    national_label_en: Tubewell/borehole with pump
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: COM-WAS-09
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: COM-WAS-10
    source_category_code: unprotected_dug_well
    national_label_en: Unprotected dug well
    national_label_local: Puits non-protegées
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: COM-WAS-11
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: Puits non-protegées
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: COM-WAS-12
    source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: Puits ou sources non protégées
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 50
  - country_entry_id: COM-WAS-13
    source_category_code: cart_with_small_tank
    national_label_en: Cart with small tank
    national_label_local: Chariot avec petit réservoir/tambour
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: COM-WAS-14
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
  - country_entry_id: COM-WAS-15
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker truck vendor
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: COM-WAS-16
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker-truck, vendor
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: COM-WAS-17
    source_category_code: autre_source
    national_label_en: Autre source
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: COM-WAS-18
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
  - country_entry_id: COM-WAS-19
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Eau conditionnée
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 89
  - country_entry_id: COM-WAS-20
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: COM-WAS-21
    source_category_code: eau_de_pluie
    national_label_en: Eau de pluie
    national_label_local: Citerne/réservoir couvert
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: COM-WAS-22
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: Citerne/réservoir couvert
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: COM-WAS-23
    source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: Citerne/réservoir couvert
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: COM-WAS-24
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: Citerne/réservoir couvert
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: COM-WAS-25
    source_category_code: tank_citerne
    national_label_en: Tank (citerne)
    national_label_local: Citerne/réservoir couvert
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: COM-WAS-26
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
  - country_entry_id: COM-WAS-27
    source_category_code: surface_water
    national_label_en: Surface Water
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: COM-WAS-28
    source_category_code: pond_river_or_stream
    national_label_en: Pond river or stream
    national_label_local: Étang
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 96
  - country_entry_id: COM-WAS-29
    source_category_code: water_taken_directly_from_pond_water_or_stream
    national_label_en: Water taken directly from pond-water or stream
    national_label_local: Étang
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 96
  - country_entry_id: COM-WAS-30
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: COM-WAS-31
    source_category_code: tap_in_house_yard
    national_label_en: Tap in House/Yard
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: COM-WAS-32
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
  - country_entry_id: COM-WAS-33
    source_category_code: robinet_logt_ou_cour
    national_label_en: Robinet logt ou cour
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: COM-WAS-34
    source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: COM-WAS-35
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
  - country_entry_id: COM-WAS-36
    source_category_code: public_standpipe
    national_label_en: Public standpipe
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: COM-WAS-37
    source_category_code: public_tap
    national_label_en: Public Tap
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: COM-WAS-38
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
  - country_entry_id: COM-WAS-39
    source_category_code: robinet_exterieur
    national_label_en: Robinet extérieur
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_COM_Comoros_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---
