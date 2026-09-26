---
country_id: CTY-GNQ
iso3: GNQ
schema_version: '0.2'
status: draft
country_name: GNQ
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: GNQ-EDU-01
    national_label_en: Garderie
    national_label_local: Pre-escolar 1
    entry_age: 1
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: GNQ-EDU-02
    national_label_en: Pre-primaire
    national_label_local: Pre-escolar 2
    entry_age: 4
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 8
  - country_entry_id: GNQ-EDU-03
    national_label_en: Primaire
    national_label_local: Primaria
    entry_age: 7
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
  - country_entry_id: GNQ-EDU-04
    national_label_en: Enseignement secondaire de base
    national_label_local: Educación Secundaria Básica
    entry_age: 13
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
  - country_entry_id: GNQ-EDU-05
    national_label_en: Baccalauréat
    national_label_local: Educación Secundaria Bachillerato
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - country_entry_id: GNQ-EDU-06
    national_label_en: Formation professionnelle (niveau moyen)
    national_label_local: Educación Sec. Formación Profesional 1  (Técnico Medio)
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: GNQ-EDU-07
    national_label_en: Formation professionnelle (niveau supérieur)
    national_label_local: |-
      Educación Sec. Formación Profesional 2
      (Técnico Superior)
    entry_age: 19
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
  - country_entry_id: GNQ-EDU-08
    national_label_en: Diplôme universitaire court
    national_label_local: Educación Terciaria Grado Corto
    entry_age: 19
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - country_entry_id: GNQ-EDU-09
    national_label_en: Licence
    national_label_local: Graduado en Eduacación Terciaria (Licenciado)
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - country_entry_id: GNQ-EDU-10
    national_label_en: Licence
    national_label_local: Graduado en Eduacación Terciaria (Licenciado)
    entry_age: 21
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: GNQ-EDU-11
    national_label_en: Master
    national_label_local: Master, Especialización o equivalente
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: GNQ-EDU-12
    national_label_en: Doctorat
    national_label_local: Doctor o equivalente
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Equatorial
      Guinea.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: GNQ-SUBNAT-01
    survey_labels: 1 - AnnobóN
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: GNQ_2015_GAUL1_1198
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1198'
    geo_nvar: ADM1_NAME
    geo_name: Annobon
    source_row: 5818
  - country_entry_id: GNQ-SUBNAT-02
    survey_labels: 2 - Bioko Norte
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: GNQ_2015_GAUL1_1199
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1199'
    geo_nvar: ADM1_NAME
    geo_name: Bioko Norte
    source_row: 5819
  - country_entry_id: GNQ-SUBNAT-03
    survey_labels: 3 - Bioko Sur
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: GNQ_2015_GAUL1_1200
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1200'
    geo_nvar: ADM1_NAME
    geo_name: Bioko Sur
    source_row: 5820
  - country_entry_id: GNQ-SUBNAT-04
    survey_labels: 4 - Centro Sur
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: GNQ_2015_GAUL1_1201
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1201'
    geo_nvar: ADM1_NAME
    geo_name: Centro Sur
    source_row: 5821
  - country_entry_id: GNQ-SUBNAT-05
    survey_labels: 6 - Kie Ntem
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: GNQ_2015_GAUL1_1202
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1202'
    geo_nvar: ADM1_NAME
    geo_name: Kientem
    source_row: 5822
  - country_entry_id: GNQ-SUBNAT-06
    survey_labels: 7 - Litoral
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: GNQ_2015_GAUL1_1203
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1203'
    geo_nvar: ADM1_NAME
    geo_name: Litoral
    source_row: 5823
  - country_entry_id: GNQ-SUBNAT-07
    survey_labels: 8 - Wele Nzas
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: GNQ_2015_GAUL1_1204
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1204'
    geo_nvar: ADM1_NAME
    geo_name: Welenzas
    source_row: 5824
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
  - country_entry_id: GNQ-SAN-01
    source_category_code: sanitario_con_sistema_de_alcantarillado_pozo_negro_o_fosa
    national_label_en: Sanitario con sistema de alcantarillado, pozo negro o fosa
    national_label_local: Inodoros de arrastre hidráulico
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: GNQ-SAN-02
    source_category_code: letrina_mejorada_ventilada
    national_label_en: Letrina mejorada/ventilada
    national_label_local: Letrina simple con loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: GNQ-SAN-03
    source_category_code: letrina_tradicional
    national_label_en: Letrina tradicional
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: GNQ-SAN-04
    source_category_code: no_tiene_sanitario
    national_label_en: No tiene sanitario
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: GNQ-SAN-05
    source_category_code: other
    national_label_en: Other
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_GNQ_Equatorial_Guinea_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: GNQ-WAS-01
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: GNQ-WAS-02
    source_category_code: protected_dug_well
    national_label_en: Protected dug well
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: GNQ-WAS-03
    source_category_code: tubewell_borehole_with_pump
    national_label_en: Tubewell/borehole with pump
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: GNQ-WAS-04
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: GNQ-WAS-05
    source_category_code: unprotected_dug_well
    national_label_en: Unprotected dug well
    national_label_local: Pozos non protegidos
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: GNQ-WAS-06
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker truck vendor
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: GNQ-WAS-07
    source_category_code: other
    national_label_en: Other
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: GNQ-WAS-08
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Agua en bolsita
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: GNQ-WAS-09
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: GNQ-WAS-10
    source_category_code: pond_river_or_stream
    national_label_en: Pond, river or stream
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: GNQ-WAS-11
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: GNQ-WAS-12
    source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: GNQ-WAS-13
    source_category_code: public_tap
    national_label_en: Public tap
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_GNQ_Equatorial_Guinea_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

