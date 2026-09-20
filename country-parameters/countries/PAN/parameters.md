---
country_id: CTY-PAN
iso3: PAN
schema_version: '0.2'
status: draft
country_name: PAN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - national_label_en: Early childhood education 1 and 2
    national_label_local: Parvularia 1 y 2
    entry_age: 0
    duration_years: 4
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - national_label_en: Early childhood education 3 or "Preschool"
    national_label_local: Parvularia 3 o "Preescolar"
    entry_age: 4
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 8
  - national_label_en: Primary
    national_label_local: Primaria
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
  - national_label_en: Lower secondary
    national_label_local: Premedia
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
  - national_label_en: Upper secondary, academic orientation
    national_label_local: Educación Media Académica
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - national_label_en: Upper secondary, professional and technical orientation
    national_label_local: Educación Media Profesional y Técnica
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - national_label_en: Third level
    national_label_local: Tercer nivel
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
  - national_label_en: Higher education, non-university
    national_label_local: Superior no universitaria
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - national_label_en: Technical diploma
    national_label_local: Técnicos
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - national_label_en: Licentiate
    national_label_local: Licenciaturas
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - national_label_en: Dentistry
    national_label_local: Odontología
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - national_label_en: Veterinary medicine
    national_label_local: Medicina Veterinaria
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - national_label_en: Medicine
    national_label_local: Medicina
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  - national_label_en: Masters
    national_label_local: Maestrías
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
  - national_label_en: Doctorate
    national_label_local: Doctorado
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Panama.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - survey_labels: 1 - Bocas del Toro
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_93668
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_93668
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '93668'
    geo_nvar: ADM1_NAME
    geo_name: Bocas del Toro
    source_row: 11004
  - survey_labels: 2 - Cocle
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_2282
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_2282
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2282'
    geo_nvar: ADM1_NAME
    geo_name: Coclé
    source_row: 11005
  - survey_labels: 3 - Colon
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_2283
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_2283
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2283'
    geo_nvar: ADM1_NAME
    geo_name: Colón
    source_row: 11006
  - survey_labels: 4 - Chiriqui
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_93669
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_93669
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '93669'
    geo_nvar: ADM1_NAME
    geo_name: Chiriquí
    source_row: 11007
  - survey_labels: 5 - Darien
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_93670
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_93670
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '93670'
    geo_nvar: ADM1_NAME
    geo_name: Darién
    source_row: 11008
  - survey_labels: 6 - Herrera
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_2286
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_2286
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2286'
    geo_nvar: ADM1_NAME
    geo_name: Herrera
    source_row: 11009
  - survey_labels: 7 - Los Santos
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_2287
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_2287
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2287'
    geo_nvar: ADM1_NAME
    geo_name: Los Santos
    source_row: 11010
  - survey_labels: 8 - Panama
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_2288
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2288'
    geo_nvar: ADM1_NAME
    geo_name: Panamá
    source_row: 11011
  - survey_labels: 9 - Veraguas
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_93673
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_93673
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '93673'
    geo_nvar: ADM1_NAME
    geo_name: Veraguas
    source_row: 11012
  - survey_labels: 10 - Comarca Kuna Yala
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_2284
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_2284
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2284'
    geo_nvar: ADM1_NAME
    geo_name: Kuna Yala
    source_row: 11014
  - survey_labels: 11 - Comarca Embera
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_93671
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_93671
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '93671'
    geo_nvar: ADM1_NAME
    geo_name: Emberá
    source_row: 11015
  - survey_labels: 12 - Comarca Ngobe-Bugle
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAUL1_93672
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAUL1_93672
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '93672'
    geo_nvar: ADM1_NAME
    geo_name: Ngöbe Buglé
    source_row: 11016
  - survey_labels: 13 - Panama-Oeste
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAULx_13
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAULx_13
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '13'
    geo_nvar: ADM2_NAME
    geo_name: Capira & Chame & San Carlos & Arraiján & La Chorrera
    source_row: 11185
  - survey_labels: 8 - Panama
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PAN_2015_GAULx_8
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PAN_2015_GAULx_8
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '8'
    geo_nvar: ADM2_NAME
    geo_name: Balboa & Chimán & San Miguelito & Taboga & Chepo & Panamá & Kuna de
      Madungandí
    source_row: 11192
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
  - source_category_code: letrina_de_compostaje
    national_label_en: Letrina de compostaje
    national_label_local: Letrinas de compostaje
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - source_category_code: conectado_a_alcantarillado_o_tanque_septico
    national_label_en: Conectado a alcantarillado o tanque séptico
    national_label_local: Descarga/baldeo con agua
    jmp_classification: Flush and pour flush
    jmp_id: flush_and_pour_flush
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 60
  - source_category_code: servicio_con_conexion_al_mar_rio_o_quebrada_u_otro_lugar_circundante
    national_label_en: Servicio con conexión al mar, río o quebrada u otro lugar circundante
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - source_category_code: conectado_a_alcantarillado
    national_label_en: Conectado a alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - source_category_code: servicio_conectado_al_alcantarillado
    national_label_en: Servicio conectado al alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - source_category_code: letrina_de_arrastre
    national_label_en: Letrina de arrastre
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - source_category_code: conectado_a_tanque_septico
    national_label_en: Conectado a tanque septico
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - source_category_code: servicio_conectado_a_tanque_septico_o_a_fosa_septica
    national_label_en: Servicio conectado a tanque séptico o a fosa séptica
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - source_category_code: connection_to_sewer_private
    national_label_en: Connection to sewer, private
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - source_category_code: connection_to_septic_tank_private
    national_label_en: Connection to septic tank, private
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 74
  - source_category_code: connection_to_sewer_shared
    national_label_en: Connection to sewer, shared
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - source_category_code: connection_to_septic_tank_shared
    national_label_en: Connection to septic tank, shared
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 80
  - source_category_code: conectado_a_alcantarillado
    national_label_en: Conectado a alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - source_category_code: conectado_a_alcantarillado_sanitario
    national_label_en: Conectado a alcantarillado sanitario
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - source_category_code: conectado_a_tanque_septico
    national_label_en: Conectado a tanque septico
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - source_category_code: servicio_colgante_sobre_el_rio_o_el_mar
    national_label_en: Servicio colgante sobre el río o el mar
    national_label_local: Letrina colgante
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - source_category_code: letrina_o_servicio_hueco_sin_piso
    national_label_en: Letrina o servicio hueco sin piso
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - source_category_code: de_hueco_o_letrina
    national_label_en: De hueco o letrina
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - source_category_code: hueco_hole_o_letrina
    national_label_en: Hueco {hole} o letrina
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - source_category_code: letrina_o_servicio_de_hueco_sin_ventilacion
    national_label_en: Letrina o servicio de hueco sin ventilación
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - source_category_code: letrina_o_servicio_de_hueco_con_ventilacion
    national_label_en: Letrina o servicio de hueco con ventilación
    national_label_local: Letrina de pozo mejorada ventilada
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - source_category_code: private_latrine
    national_label_en: Private latrine
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - source_category_code: shared_latrine
    national_label_en: Shared latrine
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - source_category_code: no_hay_servicio_sanitario_va_al_monte_campo
    national_label_en: No hay servicio sanitario, va al monte, campo
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: no_tiene
    national_label_en: No tiene
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: no_tiene_no_usa_el_servicio_sanitario_del_vecino
    national_label_en: No tiene/no usa el servicio sanitario del vecino
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: usa_servicio_sanitario_del_vecino
    national_label_en: Usa servicio sanitario del vecino
    national_label_local: Otro
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - source_category_code: otro
    national_label_en: Otro
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_PAN_Panama_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - source_category_code: pozo_privado
    national_label_en: Pozo privado
    national_label_local: Privado
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - source_category_code: pozo_publico
    national_label_en: Pozo Publico
    national_label_local: Publico
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 56
  - source_category_code: manantial_protegido
    national_label_en: Manantial protegido
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - source_category_code: pozo_artesanal_protegido
    national_label_en: Pozo artesanal protegido
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - source_category_code: pozo_brocal_protegido
    national_label_en: Pozo brocal protegido
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - source_category_code: pozo_sanitario
    national_label_en: Pozo sanitario
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - source_category_code: pozo_o_manantial_protegido
    national_label_en: Pozo o manantial protegido
    national_label_local: Pozos o manantiales protegidos
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: yes
    shared_flag: no
    source_row: 46
  - source_category_code: pozo_superficial
    national_label_en: Pozo superficial
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - source_category_code: pozo_brocal_protegido
    national_label_en: Pozo brocal protegido
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: pozo_perforado_o_tubular
    national_label_en: Pozo perforado o tubular
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: manantial_no_protegido
    national_label_en: Manantial no protegido
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - source_category_code: pozo_artesanal_no_protegido
    national_label_en: Pozo artesanal no protegido
    national_label_local: Pozos non protegidos
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - source_category_code: pozo_brocal_no_protegido
    national_label_en: Pozo brocal no protegido
    national_label_local: Pozos non protegidos
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - source_category_code: pozo_o_manantial_no_protegido
    national_label_en: Pozo o manantial no protegido
    national_label_local: Pozos o manantiales non protegidos
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 50
  - source_category_code: carro_con_tanque_o_bidon_pequea_o_camion_cisterna
    national_label_en: Carro con tanque o bidon pequeã‘o / camion cisterna
    national_label_local: Carro con tanque / tambor pequeño
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - source_category_code: carro_cisterna
    national_label_en: Carro cisterna
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: carro_tanque_camion_cisterna
    national_label_en: Carro-tanque / camión cisterna
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: otra
    national_label_en: Otra
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - source_category_code: otro
    national_label_en: Otro
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - source_category_code: agua_embotellada_agua_en_bolsitas_garrafones
    national_label_en: Agua embotellada/agua en bolsitas / garrafones
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - source_category_code: agua_embotellada_envasada
    national_label_en: Agua embotellada/envasada
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - source_category_code: agua_de_lluvia
    national_label_en: Agua de lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: recogen_agua_de_lluvia
    national_label_en: Recogen agua de lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: agua_de_superficie
    national_label_en: Agua de superficie
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: aguas_de_superficie_rio_arroyo_presa_lago_charca_canal_o_acequia
    national_label_en: Aguas de superficie (rio, arroyo, presa, lago, charca, canal
      o acequia)
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: rio_quebrada_o_lago
    national_label_en: Río, quebrada o lago
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: rio_vertiente_o_quebrada
    national_label_en: Rio, vertiente o quebrada
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: rio_vertiente_quebrada_lluvia
    national_label_en: Río, vertiente, quebrada, lluvia
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: acueducto_conexion_o_pluma_del_vecino_llave_o_grifo_publico
    national_label_en: Acueducto conexion o pluma del vecino, llave o grifo publico
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - source_category_code: acueducto_particular
    national_label_en: Acueducto particular
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - source_category_code: acueducto_conexion_o_pluma_del_vecino
    national_label_en: 'Acueducto: Conexion o pluma del vecino'
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - source_category_code: conexion_o_pluma_del_vecino
    national_label_en: Conexion o pluma del vecino
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - source_category_code: acueducto_dentro_de_la_vivienda_o_dentro_del_terreno_patio_o_lote
    national_label_en: 'Acueducto: dentro de la vivienda o dentro del terreno, patio
      o lote'
    national_label_local: Conexiones domiciliarias
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - source_category_code: acqueducto_dentro_la_vivienda_y_el_patio
    national_label_en: Acqueducto dentro la vivienda y el patio
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: acueducto_dentro_de_la_vivienda
    national_label_en: Acueducto dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: acueducto_publico
    national_label_en: Acueducto público
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: acueducto_publico_del_idaan
    national_label_en: Acueducto público del IDAAN
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: acueducto_dentro_de_la_vivienda
    national_label_en: 'Acueducto: Dentro de la vivienda'
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: dentro_de_la_vivienda
    national_label_en: Dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: tuberia_dentro_de_la_vivienda
    national_label_en: Tuberia dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: acqueducto_en_el_patio
    national_label_en: Acqueducto en el patio
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: acueducto_de_la_comunidad
    national_label_en: Acueducto de la comunidad
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: acueducto_en_al_patio_de_la_vivienda
    national_label_en: Acueducto en al patio de la vivienda
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: acueducto_publico_de_la_comunidad
    national_label_en: Acueducto público de la comunidad
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: acueducto_dentro_del_terreno_patio_o_lote
    national_label_en: 'Acueducto: Dentro del terreno, patio o lote'
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: dentro_del_terreno_patio_o_lote
    national_label_en: Dentro del terreno, patio o lote
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: tuberia_dentro_del_terreno_lote
    national_label_en: Tuberia  dentro del terreno/ lote
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: acqueducto_fuera_de_la_vivienda
    national_label_en: Acqueducto fuera de la vivienda
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: acueducto_fuera_de_la_vivienda_y_del_patio
    national_label_en: Acueducto fuera de la vivienda y del patio
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: acueducto_llave_o_grifo_publico
    national_label_en: 'Acueducto: Llave o grifo publico'
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: llave_o_grifo_publico
    national_label_en: Llave o grifo publico
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - source_category_code: llave_grifo_publico
    national_label_en: Llave/grifo publico
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_PAN_Panama_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

