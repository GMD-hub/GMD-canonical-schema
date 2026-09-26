---
country_id: CTY-BOL
iso3: BOL
schema_version: '0.2'
status: draft
country_name: BOL
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: BOL-EDU-01
    national_label_en: Initial education in community family
    national_label_local: Educación Inicial en Familia Comunitaria
    entry_age: 4
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: BOL-EDU-02
    national_label_en: Vocational community primary education
    national_label_local: Educación Primaria Comunitaria Vocacional
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
  - country_entry_id: BOL-EDU-03
    national_label_en: Productive community secondary education, Stage 1 (Grades 1-2)
    national_label_local: Educación Secundaria Comunitaria Productiva. Primera etapa
      (Grados 1 y 2)
    entry_age: 12
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - country_entry_id: BOL-EDU-04
    national_label_en: Productive community secondary education, Stage 2 (Grades 3-6)
    national_label_local: Educación Secundaria Comunitaria Productiva. Segunda etapa
      (Grados 3 a 6)
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
  - country_entry_id: BOL-EDU-05
    national_label_en: Middle technical and technological training
    national_label_local: Formación Técnica y Tecnológica Media
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 11
  - country_entry_id: BOL-EDU-06
    national_label_en: Higher technical and technological training
    national_label_local: Formación Técnica y Tecnológica Superior
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 12
  - country_entry_id: BOL-EDU-07
    national_label_en: Teachers higher education
    national_label_local: Formación Superior de Maestras y Maestros
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
  - country_entry_id: BOL-EDU-08
    national_label_en: University higher education
    national_label_local: Formación Superior Universitaria
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - country_entry_id: BOL-EDU-09
    national_label_en: Specialization programmes
    national_label_local: Cursos de especialidad
    entry_age: 23
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - country_entry_id: BOL-EDU-10
    national_label_en: Medicine
    national_label_local: Medicina
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: BOL-EDU-11
    national_label_en: Master programmes
    national_label_local: Maestría
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: BOL-EDU-12
    national_label_en: Doctorate programmes
    national_label_local: Doctorado
    entry_age: 25
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Bolivia.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: BOL-SUBNAT-01
    survey_labels: 1 - Chuquisaca | 1-Chuquisaca
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: BOL_2015_GAUL1_40444
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: BOL_2015_GAUL1_40444
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '40444'
    geo_nvar: ADM1_NAME
    geo_name: Chuquisaca
    source_row: 1075
  - country_entry_id: BOL-SUBNAT-02
    survey_labels: 2 - La Paz | 2-La Paz
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: BOL_2015_GAUL1_40446
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: BOL_2015_GAUL1_40446
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '40446'
    geo_nvar: ADM1_NAME
    geo_name: La Paz
    source_row: 1076
  - country_entry_id: BOL-SUBNAT-03
    survey_labels: 3 - Cochabamba | 3-Cochabamba
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: BOL_2015_GAUL1_40445
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: BOL_2015_GAUL1_40445
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '40445'
    geo_nvar: ADM1_NAME
    geo_name: Cochabamba
    source_row: 1077
  - country_entry_id: BOL-SUBNAT-04
    survey_labels: 4 - Oruro | 4-Oruro
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: BOL_2015_GAUL1_40447
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: BOL_2015_GAUL1_40447
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '40447'
    geo_nvar: ADM1_NAME
    geo_name: Oruro
    source_row: 1078
  - country_entry_id: BOL-SUBNAT-05
    survey_labels: 5 - Potosi | 5-Potosi
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: BOL_2015_GAUL1_40448
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: BOL_2015_GAUL1_40448
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '40448'
    geo_nvar: ADM1_NAME
    geo_name: Potosi
    source_row: 1079
  - country_entry_id: BOL-SUBNAT-06
    survey_labels: 6 - Tarija | 6-Tarija
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: BOL_2015_GAUL1_40450
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: BOL_2015_GAUL1_40450
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '40450'
    geo_nvar: ADM1_NAME
    geo_name: Tarija
    source_row: 1080
  - country_entry_id: BOL-SUBNAT-07
    survey_labels: 7 - Santa Cruz | 7-Santa Cruz
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: BOL_2015_GAUL1_40449
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: BOL_2015_GAUL1_40449
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '40449'
    geo_nvar: ADM1_NAME
    geo_name: Santa Cruz
    source_row: 1081
  - country_entry_id: BOL-SUBNAT-08
    survey_labels: 8 - Beni + Pando | 8-Beni + Pando
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: BOL_2015_GAULx_8
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: BOL_2015_GAULx_8
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '8'
    geo_nvar: ADM1_NAME
    geo_name: Beni & Pando
    source_row: 1082
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
  - country_entry_id: BOL-SAN-01
    source_category_code: bano_ecologico_bano_de_compostaje
    national_label_en: Baño ecológico (baño de compostaje)
    national_label_local: Letrinas de compostaje
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: BOL-SAN-02
    source_category_code: arrastre_de_agua_a_la_superficie_calle_quebrada_rio
    national_label_en: Arrastre de agua a la superficie (calle/quebrada/rio)
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: BOL-SAN-03
    source_category_code: bano_o_letrina_con_descarga_de_agua_a_la_superficie_calle_quebrada_rio
    national_label_en: Baño o letrina con descarga de agua a la superficie (calle/quebrada/rio)
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: BOL-SAN-04
    source_category_code: bano_servicio_sanitario_o_letrina_a_la_superficie_calle_quebrada_rio
    national_label_en: 'Baño, servicio sanitario o letrina: a la superficie (calle/quebrada/rio)'
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: BOL-SAN-05
    source_category_code: desague_del_bano_water_o_letrina_superficie_calle_rio
    national_label_en: DESAGÜE DEL BAÑO, WATER O LETRINA Superficie (calle /río)
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: BOL-SAN-06
    source_category_code: alcantarillado
    national_label_en: Alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: BOL-SAN-07
    source_category_code: arrastre_de_agua_a_la_red_de_alcantarillado
    national_label_en: Arrastre de agua a la red de alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: BOL-SAN-08
    source_category_code: bano_o_letrina_con_descarga_de_agua_a_la_red_de_alcantarillado
    national_label_en: Baño o letrina con descarga de agua a la red de alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: BOL-SAN-09
    source_category_code: bano_servicio_sanitario_o_letrina_a_la_red_de_alcantarillado
    national_label_en: 'Baño, servicio sanitario o letrina: a la red de alcantarillado'
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: BOL-SAN-10
    source_category_code: desague_del_bano_water_o_letrina_alcantarillado
    national_label_en: DESAGÜE DEL BAÑO, WATER O LETRINA Alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: BOL-SAN-11
    source_category_code: arrastre_de_agua_a_un_pozo_de_absorcion
    national_label_en: Arrastre de agua a un pozo de absorción
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: BOL-SAN-12
    source_category_code: bano_o_letrina_con_descarga_de_agua_a_un_pozo_de_absorcion
    national_label_en: Baño o letrina con descarga de agua a un pozo de absorción
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: BOL-SAN-13
    source_category_code: bano_servicio_sanitario_o_letrina_a_un_pozo_ciego_absorcion
    national_label_en: 'Baño, servicio sanitario o letrina: a un pozo ciego/absorción'
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: BOL-SAN-14
    source_category_code: arrastre_de_agua_a_una_camara_septica
    national_label_en: Arrastre de agua a una cámara séptica
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: BOL-SAN-15
    source_category_code: bano_o_letrina_con_descarga_de_agua_a_una_camara_septica
    national_label_en: Baño o letrina con descarga de agua a una cámara séptica
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: BOL-SAN-16
    source_category_code: bano_servicio_sanitario_o_letrina_a_una_camara_septica
    national_label_en: 'Baño, servicio sanitario o letrina:  a una cámara séptica'
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: BOL-SAN-17
    source_category_code: camara_septica
    national_label_en: Camara septica
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: BOL-SAN-18
    source_category_code: desague_del_bano_water_o_letrina_camara_septica
    national_label_en: DESAGÜE DEL BAÑO, WATER O LETRINA cámara séptica
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: BOL-SAN-19
    source_category_code: pozo_septico
    national_label_en: Pozo septico
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: BOL-SAN-20
    source_category_code: arrastre_de_agua_a_otro_no_sabe
    national_label_en: Arrastre de agua a otro/no sabe
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: BOL-SAN-21
    source_category_code: bano_o_letrina_con_descarga_de_agua_a_otro_no_sabe
    national_label_en: Baño o letrina con descarga de agua a otro/no sabe
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: BOL-SAN-22
    source_category_code: bano_servicio_sanitario_o_letrina_no_sabe
    national_label_en: 'Baño, servicio sanitario o letrina: no sabe'
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: BOL-SAN-23
    source_category_code: sanitario_con_sistema_de_alcantarillado_o_pozo_septico
    national_label_en: Sanitario con sistema de alcantarillado o pozo septico
    national_label_local: Inodoros de arrastre hidráulico
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: BOL-SAN-24
    source_category_code: private_flush_toilet
    national_label_en: Private flush toilet
    national_label_local: Inodoros de arrastre hidráulico (privado)
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: BOL-SAN-25
    source_category_code: el_bano_water_o_letrina_tiene_desague_a_la_superficie_calle_quebrada_rio_uso_privado
    national_label_en: EL BAÑO, WATER O LETRINA TIENE DESAGUE A la superficie (calle/quebrada/rio)/uso
      privado
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > Private flush/toilet > to elsewhere
    jmp_id: flush_toilets.private_flush_toilet.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 77
  - country_entry_id: BOL-SAN-26
    source_category_code: el_bano_water_o_letrina_tiene_desague_al_alcantarillado_uso_privado
    national_label_en: EL BAÑO, WATER O LETRINA TIENE DESAGUE Al alcantarillado/uso
      privado
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - country_entry_id: BOL-SAN-27
    source_category_code: el_bano_water_o_letrina_tiene_desague_a_una_camara_septica_uso_privado
    national_label_en: EL BAÑO, WATER O LETRINA TIENE DESAGUE A una cámara séptica/uso
      privado
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 74
  - country_entry_id: BOL-SAN-28
    source_category_code: shared_flush_toilet
    national_label_en: Shared flush toilet
    national_label_local: Inodoros de arrastre hidráulico (publico)
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: BOL-SAN-29
    source_category_code: el_bano_water_o_letrina_tiene_desague_a_la_superficie_calle_quebrada_rio_uso_compartido
    national_label_en: EL BAÑO, WATER O LETRINA TIENE DESAGUE A la superficie (calle/quebrada/rio)/uso
      compartido
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to elsewhere
    jmp_id: flush_toilets.public_shared_flush_toilet.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 83
  - country_entry_id: BOL-SAN-30
    source_category_code: el_bano_water_o_letrina_tiene_desague_al_alcantarillado_uso_compartido
    national_label_en: EL BAÑO, WATER O LETRINA TIENE DESAGUE Al alcantarillado/ uso
      compartido
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - country_entry_id: BOL-SAN-31
    source_category_code: el_bano_water_o_letrina_tiene_desague_a_una_camara_septica_uso_compartido
    national_label_en: EL BAÑO, WATER O LETRINA TIENE DESAGUE A una cámara séptica/uso
      compartido
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 80
  - country_entry_id: BOL-SAN-32
    source_category_code: a_la_superficie_calle_quebrada_rio
    national_label_en: a la superficie (calle/quebrada/rio)
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: BOL-SAN-33
    source_category_code: tiene_bano_servicio_sanitario_o_letrina_tiene_desague_a_la_superficie_calle_quebrada_rio
    national_label_en: Tiene baño, servicio sanitario o letrina - Tiene desague a
      la superficie (calle/quebrada/rio)
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: BOL-SAN-34
    source_category_code: al_alcantarillado
    national_label_en: al alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: BOL-SAN-35
    source_category_code: alcantarillado
    national_label_en: Alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: BOL-SAN-36
    source_category_code: domestic_connection
    national_label_en: Domestic connection
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: BOL-SAN-37
    source_category_code: domestic_connection_to_sewage_system
    national_label_en: Domestic connection to sewage system
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: BOL-SAN-38
    source_category_code: tiene_bano_servicio_sanitario_o_letrina_tiene_desague_al_alcantarillado
    national_label_en: Tiene baño, servicio sanitario o letrina - Tiene desague al
      alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: BOL-SAN-39
    source_category_code: a_una_camara_septica
    national_label_en: a una cámara séptica
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: BOL-SAN-40
    source_category_code: camara_septica
    national_label_en: Cámara séptica
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: BOL-SAN-41
    source_category_code: connection_to_septic_tank
    national_label_en: Connection to septic tank
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: BOL-SAN-42
    source_category_code: domestic_connection_to_septic_tank
    national_label_en: Domestic connection to septic tank
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: BOL-SAN-43
    source_category_code: tiene_bano_servicio_sanitario_o_letrina_tiene_desague_a_una_camara_septica
    national_label_en: Tiene baño, servicio sanitario o letrina - Tiene desague a
      una cámara séptica
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: BOL-SAN-44
    source_category_code: superficie_calle_rio
    national_label_en: Superficie (calle/rio)
    national_label_local: Letrina colgante
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: BOL-SAN-45
    source_category_code: bacin
    national_label_en: Bacin
    national_label_local: Otro
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: BOL-SAN-46
    source_category_code: letrina_de_pozo_ciego_con_piso
    national_label_en: Letrina de pozo ciego con piso
    national_label_local: Letrina simple con loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: BOL-SAN-47
    source_category_code: letrina_de_pozo_con_loza
    national_label_en: Letrina de pozo con loza
    national_label_local: Letrina simple con loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: BOL-SAN-48
    source_category_code: pozo_abierto_letrina_de_pozo_sin_loza
    national_label_en: Pozo abierto (letrina de pozo sin loza)
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: BOL-SAN-49
    source_category_code: pozo_abierto_pozo_ciego_sin_piso
    national_label_en: Pozo abierto (pozo ciego sin piso)
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: BOL-SAN-50
    source_category_code: a_un_pozo_ciego
    national_label_en: a un pozo ciego
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: BOL-SAN-51
    source_category_code: desague_del_bano_water_o_letrina_pozo_ciego
    national_label_en: DESAGÜE DEL BAÑO, WATER O LETRINA pozo ciego
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: BOL-SAN-52
    source_category_code: latrine
    national_label_en: Latrine
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: BOL-SAN-53
    source_category_code: latrine_with_soakaway
    national_label_en: Latrine with soakaway
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: BOL-SAN-54
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
  - country_entry_id: BOL-SAN-55
    source_category_code: pozo_ciego
    national_label_en: Pozo ciego
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: BOL-SAN-56
    source_category_code: tiene_bano_servicio_sanitario_o_letrina_tiene_desague_a_un_pozo_ciego
    national_label_en: Tiene baño, servicio sanitario o letrina - Tiene desague a
      un pozo ciego
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: BOL-SAN-57
    source_category_code: letrina_mejorada_ecologica_vip
    national_label_en: Letrina mejorada/ ecologica (VIP)
    national_label_local: Letrina de pozo mejorada ventilada
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: BOL-SAN-58
    source_category_code: el_bano_water_o_letrina_tiene_desague_apozo_ciego_uso_privado
    national_label_en: EL BAÑO, WATER O LETRINA TIENE DESAGUE apozo ciego/uso privado
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: BOL-SAN-59
    source_category_code: private_latrine
    national_label_en: Private latrine
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: BOL-SAN-60
    source_category_code: el_bano_water_o_letrina_tiene_desague_a_pozo_ciego_uso_compartido
    national_label_en: EL BAÑO, WATER O LETRINA TIENE DESAGUE a pozo ciego/uso compartido
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - country_entry_id: BOL-SAN-61
    source_category_code: shared_latrine
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
  - country_entry_id: BOL-SAN-62
    source_category_code: letrina_con_agua_fluida
    national_label_en: Letrina con agua fluida
    national_label_local: Letrinas de arrastre hidráulico
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 85
  - country_entry_id: BOL-SAN-63
    source_category_code: ninguno_arbusto_campo
    national_label_en: Ninguno (Arbusto/Campo)
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-64
    source_category_code: ninguno_arbusto_campo
    national_label_en: Ninguno-Arbusto-Campo
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-65
    source_category_code: no_facility
    national_label_en: No facility
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-66
    source_category_code: no_facility_brushwood_field
    national_label_en: No facility, brushwood, field
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-67
    source_category_code: no_tiene_bano
    national_label_en: No tiene bano
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-68
    source_category_code: no_tiene_bano_servicio_sanitario_o_letrina
    national_label_en: No tiene baño, servicio sanitario o letrina
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-69
    source_category_code: no_tiene_sanitario_o_matorral_o_campo
    national_label_en: No tiene sanitario, o matorral o campo
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-70
    source_category_code: no_tiene_servicio_sanitario
    national_label_en: No tiene servicio sanitario
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-71
    source_category_code: no_tiene_water_letrina_o_sanitario
    national_label_en: No tiene water, letrina o sanitario
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-72
    source_category_code: none
    national_label_en: NONE
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: BOL-SAN-73
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
  - country_entry_id: BOL-SAN-74
    source_category_code: otro
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_BOL_Bolivia_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: BOL-WAS-01
    source_category_code: well
    national_label_en: Well
    national_label_local: Todos los pozos
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 54
  - country_entry_id: BOL-WAS-02
    source_category_code: well_or_cistern
    national_label_en: Well or cistern
    national_label_local: Todos los pozos
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 54
  - country_entry_id: BOL-WAS-03
    source_category_code: well_or_water_wheel
    national_label_en: Well or water-wheel
    national_label_local: Todos los pozos
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 54
  - country_entry_id: BOL-WAS-04
    source_category_code: manantial_o_vertiente_protegido
    national_label_en: Manantial o vertiente protegido
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: BOL-WAS-05
    source_category_code: manantial_protegido
    national_label_en: Manantial protegido
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: BOL-WAS-06
    source_category_code: pozo_excavado_protegido
    national_label_en: Pozo excavado protegido
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: BOL-WAS-07
    source_category_code: pozo_excavado_protegido_con_bomba
    national_label_en: Pozo excavado protegido-con bomba
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: BOL-WAS-08
    source_category_code: pozo_pretegido_o_cunbierto
    national_label_en: Pozo pretegido o cunbierto
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: BOL-WAS-09
    source_category_code: pozo_excavado_cubierto_sin_bomba
    national_label_en: Pozo excavado cubierto sin bomba
    national_label_local: Otro
    jmp_classification: Ground water > Protected well > Other
    jmp_id: ground_water.protected_well.other
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: BOL-WAS-10
    source_category_code: pozo_excavado_cubierto_sin_bomba
    national_label_en: Pozo excavado cubierto, sin bomba
    national_label_local: Otro
    jmp_classification: Ground water > Protected well > Other
    jmp_id: ground_water.protected_well.other
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: BOL-WAS-11
    source_category_code: pozo_escavado_cubierto_con_bomba
    national_label_en: Pozo escavado cubierto, con bomba
    national_label_local: Privado
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: BOL-WAS-12
    source_category_code: pozo_excavado_cubierto_con_bomba
    national_label_en: Pozo excavado cubierto con bomba
    national_label_local: Privado
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: BOL-WAS-13
    source_category_code: pozo_excavado_cubierto_con_bomba
    national_label_en: Pozo excavado cubierto, con bomba
    national_label_local: Privado
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: BOL-WAS-14
    source_category_code: pozo_protegido_con_bomba
    national_label_en: Pozo protegido, con bomba
    national_label_local: Privado
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: BOL-WAS-15
    source_category_code: pozo_o_noria_sin_bomba
    national_label_en: Pozo o noria sin bomba
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: BOL-WAS-16
    source_category_code: pozo_or_noria_sin_bomba
    national_label_en: Pozo or noria sin bomba
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: BOL-WAS-17
    source_category_code: pozo_can_tuberia_o_bomba
    national_label_en: Pozo can tuberia o bomba
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: BOL-WAS-18
    source_category_code: pozo_entubado_o_perforado
    national_label_en: Pozo entubado o perforado
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: BOL-WAS-19
    source_category_code: pozo_entubado_perforado_con_bomba
    national_label_en: Pozo entubado-perforado-con bomba
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: BOL-WAS-20
    source_category_code: pozo_o_noria_con_bomba
    national_label_en: Pozo o noria con bomba
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: BOL-WAS-21
    source_category_code: pozo_or_noria_con_bomba
    national_label_en: Pozo or noria con bomba
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: BOL-WAS-22
    source_category_code: pozo_perforado_o_entubado_con_bomba
    national_label_en: Pozo perforado o entubado, con bomba
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: BOL-WAS-23
    source_category_code: manantial_no_protegido
    national_label_en: Manantial no protegido
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: BOL-WAS-24
    source_category_code: pozo_excavado_no_cubierto
    national_label_en: Pozo excavado no cubierto
    national_label_local: Pozos non protegidos
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: BOL-WAS-25
    source_category_code: pozo_excavado_no_protegido
    national_label_en: Pozo excavado no protegido
    national_label_local: Pozos non protegidos
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: BOL-WAS-26
    source_category_code: pozo_excavado_no_protegido_con_o_sin_bomba
    national_label_en: Pozo excavado no protegido, con o sin bomba
    national_label_local: Pozos non protegidos
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: BOL-WAS-27
    source_category_code: pozo_no_protegido
    national_label_en: Pozo no protegido
    national_label_local: Pozos non protegidos
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: BOL-WAS-28
    source_category_code: pozo_no_protegido_o_sin_bomba
    national_label_en: Pozo no protegido o sin bomba
    national_label_local: Otro
    jmp_classification: Ground water > Unprotected well > Other
    jmp_id: ground_water.unprotected_well.other
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 73
  - country_entry_id: BOL-WAS-29
    source_category_code: carro_repartidor_aguatero
    national_label_en: carro repartidor (aguatero)
    national_label_local: Carro con tanque / tambor pequeño
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: BOL-WAS-30
    source_category_code: carro_repartidor_aguatero_with_piped_connection
    national_label_en: carro repartidor (aguatero) with piped connection
    national_label_local: Otro
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: BOL-WAS-31
    source_category_code: camion_tanque_vendedor
    national_label_en: Camion, tanque, vendedor
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: BOL-WAS-32
    source_category_code: caro_repartidor_aguatero
    national_label_en: Caro repartidor (Aguatero)
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: BOL-WAS-33
    source_category_code: carro_repartidor
    national_label_en: Carro repartidor
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: BOL-WAS-34
    source_category_code: carro_repartidor_aguatero
    national_label_en: Carro repartidor (aguatero)
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: BOL-WAS-35
    source_category_code: truck_distribution
    national_label_en: Truck distribution
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: BOL-WAS-36
    source_category_code: truckborne
    national_label_en: Truckborne
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: BOL-WAS-37
    source_category_code: neighbour_no_specification
    national_label_en: Neighbour (no specification)
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: BOL-WAS-38
    source_category_code: other
    national_label_en: Other
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: BOL-WAS-39
    source_category_code: other_source
    national_label_en: Other source
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: BOL-WAS-40
    source_category_code: otra
    national_label_en: Otra
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: BOL-WAS-41
    source_category_code: otro
    national_label_en: Otro
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: BOL-WAS-42
    source_category_code: otros
    national_label_en: Otros
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: BOL-WAS-43
    source_category_code: agua_del_vecino
    national_label_en: Agua del vecino
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: BOL-WAS-44
    source_category_code: no_se_distribuye_por_caneria_pileta_publica
    national_label_en: No se distribuye por cañería - Pileta pública
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: BOL-WAS-45
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
  - country_entry_id: BOL-WAS-46
    source_category_code: otro_1
    national_label_en: Otro (1)
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: BOL-WAS-47
    source_category_code: agua_embotellada
    national_label_en: Agua embotellada
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: BOL-WAS-48
    source_category_code: agua_de_lluvia
    national_label_en: Agua de lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: BOL-WAS-49
    source_category_code: cosecha_de_agua_de_lluvia
    national_label_en: Cosecha de agua de lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: BOL-WAS-50
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: BOL-WAS-51
    source_category_code: charca_estanque_rio_o_arroyo
    national_label_en: Charca, estanque, rio o arroyo
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: BOL-WAS-52
    source_category_code: rio_acequia_vertiente_no_protegida
    national_label_en: Río-Acequia-Vertiente no protegida
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: BOL-WAS-53
    source_category_code: rio_acequia_vertiente_no_protegida
    national_label_en: Rio/Acequia/Vertiente no protegida
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: BOL-WAS-54
    source_category_code: river_irrigated_channel
    national_label_en: River, irrigated channel
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: BOL-WAS-55
    source_category_code: river_lake_spring_irrigation_channel
    national_label_en: River, lake spring, irrigation channel
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: BOL-WAS-56
    source_category_code: river_lake_spring
    national_label_en: River, lake, spring
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: BOL-WAS-57
    source_category_code: lago_laguna_o_curiche
    national_label_en: Lago, laguna o curiche
    national_label_local: Lago
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 94
  - country_entry_id: BOL-WAS-58
    source_category_code: lago_laguna_curiche
    national_label_en: Lago, laguna, curiche
    national_label_local: Lago
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 94
  - country_entry_id: BOL-WAS-59
    source_category_code: lago_laguna_cariche
    national_label_en: Lago/laguna/cariche
    national_label_local: Lago
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 94
  - country_entry_id: BOL-WAS-60
    source_category_code: lago_laguna_curiche
    national_label_en: Lago/laguna/curiche
    national_label_local: Lago
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 94
  - country_entry_id: BOL-WAS-61
    source_category_code: lago_laguna_curiche
    national_label_en: lago/laguna/curiche
    national_label_local: Estanque
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - country_entry_id: BOL-WAS-62
    source_category_code: rio_vertiente_o_acequia
    national_label_en: Rio, vertiente o acequia
    national_label_local: Río
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: BOL-WAS-63
    source_category_code: rio_vertiente_acequia
    national_label_en: Rio/vertiente/acequía
    national_label_local: Río
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: BOL-WAS-64
    source_category_code: caneria_de_red_por_caneria_fuera_del_lote_o_terreno
    national_label_en: Cañería de red - Por cañería fuera del lote o terreno
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: BOL-WAS-65
    source_category_code: caneria_de_red_otros_medios_no_en_vivienda_o_terreno
    national_label_en: Caneria de red otros medios/no en vivienda o terreno
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: BOL-WAS-66
    source_category_code: neighbour_drinking_water
    national_label_en: Neighbour (drinking water)
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: BOL-WAS-67
    source_category_code: por_caneria_fuera_de_la_vivienda_fuera_del_lote_o_ter
    national_label_en: por cañeria fuera de la vivienda, fuera del lote o ter
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: BOL-WAS-68
    source_category_code: pipeborne_water
    national_label_en: Pipeborne water
    national_label_local: Conexiones domiciliarias
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: BOL-WAS-69
    source_category_code: red_por_caneira
    national_label_en: Red por caneira
    national_label_local: Conexiones domiciliarias
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: BOL-WAS-70
    source_category_code: agua_por_caneria_dentro_de_la_vivienda
    national_label_en: Agua por cañería dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-71
    source_category_code: caneria_de_red
    national_label_en: cañería de red
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-72
    source_category_code: caneria_de_red_por_caneria_dentro_de_la_vivienda
    national_label_en: Cañería de red - Por cañería dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-73
    source_category_code: caneria_de_red_dentro_de_casa
    national_label_en: Cañería de red dentro de casa
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-74
    source_category_code: caneria_de_red_dentro_de_la_vivienda
    national_label_en: Cañería de red dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-75
    source_category_code: domestic_connection
    national_label_en: Domestic connection
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-76
    source_category_code: domestic_connection_within_house
    national_label_en: Domestic connection (within house)
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-77
    source_category_code: por_caneria_dentro_de_la_vivienda
    national_label_en: por cañería dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-78
    source_category_code: red_por_caneria
    national_label_en: Red por cañería
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-79
    source_category_code: tuberia_dentro_de_la_vivienda_patio
    national_label_en: Tuberia dentro de la vivienda/patio
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-80
    source_category_code: tuberia_dentro_le_vivienda
    national_label_en: Tuberia dentro le vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: BOL-WAS-81
    source_category_code: agua_por_caneria_fuera_de_la_vivienda
    national_label_en: Agua por cañería fuera de la vivienda
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-82
    source_category_code: caneria_de_red_por_caneria_fuera_de_la_vivienda_pero_dentro_del_lote_o_terreno
    national_label_en: Cañería de red - Por cañería fuera de la vivienda, pero dentro
      del lote o terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-83
    source_category_code: caneria_de_red_fuera_de_la_vivienda_pero_dentro_del_lote
    national_label_en: Cañería de red fuera de la vivienda, pero dentro del lote
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-84
    source_category_code: caneria_de_red_fuera_de_la_vivienda_pero_dentro_del_lote_o_terreno
    national_label_en: Cañería de red fuera de la vivienda, pero dentro del lote o
      terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-85
    source_category_code: domestic_connection_within_building_or_yard
    national_label_en: Domestic connection (within building or yard)
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-86
    source_category_code: por_caneria_fuera_de_la_en_terreno
    national_label_en: Por cañería fuera de la en terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-87
    source_category_code: por_caneria_fuera_de_la_vivienda_pero_dentro_del_lote_o_terreno
    national_label_en: Por cañeria fuera de la vivienda, pero dentro del lote o terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-88
    source_category_code: por_caneria_pero_dentro_del_lote_o_terreno
    national_label_en: por cañeria pero dentro del lote o terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-89
    source_category_code: tuberia_en_el_patio
    national_label_en: Tuberia en el patio
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-90
    source_category_code: yard_tap
    national_label_en: Yard tap
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: BOL-WAS-91
    source_category_code: agua_por_caneria_fuera_del_lote
    national_label_en: Agua por cañería fuera del lote
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: BOL-WAS-92
    source_category_code: caneria_de_red_pileta_publica
    national_label_en: Cañería de red - Pileta pública
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: BOL-WAS-93
    source_category_code: caneria_de_red_con_pileta_publica
    national_label_en: Cañería de red con pileta pública
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: BOL-WAS-94
    source_category_code: connection_outside
    national_label_en: Connection outside
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: BOL-WAS-95
    source_category_code: llave_publica
    national_label_en: Llave publica
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: BOL-WAS-96
    source_category_code: pileta_publica
    national_label_en: Pileta publica
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: BOL-WAS-97
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
  - country_entry_id: BOL-WAS-98
    source_category_code: tuberia_publica_fuera_de_la_vivienda
    national_label_en: Tuberia publica fuera de la vivienda
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_BOL_Bolivia_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

