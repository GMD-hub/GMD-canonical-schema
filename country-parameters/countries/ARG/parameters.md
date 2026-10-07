---
country_id: CTY-ARG
iso3: ARG
schema_version: '0.2'
status: draft
country_name: ARG
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ARG-EDU-01
    national_label_en: Early childhood educational development
    national_label_local: Jardin maternal
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
  - country_entry_id: ARG-EDU-02
    national_label_en: Kindergarden - Pre-primary
    national_label_local: "Jard\xEDn de Infantes"
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
  - country_entry_id: ARG-EDU-03
    national_label_en: Primary education
    national_label_local: "Educaci\xF3n Primaria"
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - ARG-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: ARG-EDU-04
    national_label_en: Adults primary education
    national_label_local: Primaria de Adultos
    entry_age: 15
    duration_years: 3
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 3
    cum_years_computation_path:
    - ARG-EDU-04
    cum_years_status: computed
    review_flags: &id002 []
  - country_entry_id: ARG-EDU-05
    national_label_en: Basic cycle. Secondary education
    national_label_local: "Ciclo B\xE1sico Educaci\xF3n Secundaria"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - ARG-EDU-03
    cum_years_schooling: 9
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-06
    national_label_en: Basic cycle. Adults secondary education
    national_label_local: "Ciclo B\xE1sico Secundaria de Adultos"
    entry_age: 18
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - ARG-EDU-04
    cum_years_schooling: 5
    cum_years_computation_path:
    - ARG-EDU-04
    - ARG-EDU-06
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: ARG-EDU-07
    national_label_en: Secondary education - oriented cycle
    national_label_local: "Educaci\xF3n secundaria - ciclo orientado."
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - ARG-EDU-05
    cum_years_schooling: 12
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-08
    national_label_en: Oriented cycle. Adults secondary education
    national_label_local: Ciclo Orientado Secundaria de Adultos
    entry_age: 18
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - ARG-EDU-06
    cum_years_schooling: 7
    cum_years_computation_path:
    - ARG-EDU-04
    - ARG-EDU-06
    - ARG-EDU-08
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: ARG-EDU-09
    national_label_en: Short cycle higher non-university education
    national_label_local: Superior no Universitario de ciclo corto
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 14
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-10
    national_label_en: Short cycle higher university education
    national_label_local: Superior Universitario - de Ciclo Corto
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 15
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-11
    national_label_en: Higher non-university education  (teacher training)
    national_label_local: "Superior no Universitario (Formaci\xF3n pedag\xF3gica)"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 16
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-12
    national_label_en: Higher university education - Bachelor
    national_label_local: Superior Universitario
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 17
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-13
    national_label_en: University programme in law
    national_label_local: "Abogac\xEDa"
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 17
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-13
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-14
    national_label_en: University programme in engineering
    national_label_local: Ingeniero
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 17
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-14
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-15
    national_label_en: University programme in architecture
    national_label_local: Arquitectura
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 17
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-15
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-16
    national_label_en: University complementation cycle
    national_label_local: "Ciclo de complementaci\xF3n universitaria"
    entry_age: 22
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 14
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-16
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-17
    national_label_en: Dentistry
    national_label_local: "Odontolog\xEDa"
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 18
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-17
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-18
    national_label_en: Medicine
    national_label_local: Medicina
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 18
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-18
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-19
    national_label_en: Post degree - Specialization
    national_label_local: "Formaci\xF3n de Posgrado (Especialidad)"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - ARG-EDU-07
    cum_years_schooling: 14
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-19
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ARG-EDU-20
    national_label_en: Post degree - Master
    national_label_local: "Formaci\xF3n de Posgrado (Maestr\xEDa)"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - ARG-EDU-11
    - ARG-EDU-12
    - ARG-EDU-13
    - ARG-EDU-14
    - ARG-EDU-15
    - ARG-EDU-16
    cum_years_schooling: 16
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-16
    - ARG-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ARG-EDU-11, ARG-EDU-12, ARG-EDU-13, ARG-EDU-14,
      ARG-EDU-15, ARG-EDU-16'
  - country_entry_id: ARG-EDU-21
    national_label_en: Post degree - Doctorate
    national_label_local: "Formaci\xF3n de Posgrado (Doctorado)"
    entry_age: 22
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - ARG-EDU-17
    - ARG-EDU-18
    - ARG-EDU-19
    - ARG-EDU-20
    cum_years_schooling: 18
    cum_years_computation_path:
    - ARG-EDU-03
    - ARG-EDU-05
    - ARG-EDU-07
    - ARG-EDU-19
    - ARG-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ARG-EDU-17, ARG-EDU-18, ARG-EDU-19, ARG-EDU-20'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Argentina.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ARG-SUBNAT-01
    survey_labels: 1 - Gran Buenos Aires
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ARG_2015_GAULx_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARG_2015_GAULx_1
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '1'
    geo_nvar: ADM1_NAME
    geo_name: Buenos Aires D.f. & Entre Rios
    source_row: 141
  - country_entry_id: ARG-SUBNAT-02
    survey_labels: 2 - Pampeana
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ARG_2015_GAULx_2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARG_2015_GAULx_2
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '2'
    geo_nvar: ADM1_NAME
    geo_name: Buenos Aires & Cordoba & Entre Rios & La Pampa & Santa Fe
    source_row: 142
  - country_entry_id: ARG-SUBNAT-03
    survey_labels: 3 - Cuyo
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ARG_2015_GAULx_3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARG_2015_GAULx_3
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '3'
    geo_nvar: ADM1_NAME
    geo_name: Mendoza & San Juan & San Luis
    source_row: 143
  - country_entry_id: ARG-SUBNAT-04
    survey_labels: 4 - Noroeste Argentino
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ARG_2015_GAULx_4
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARG_2015_GAULx_4
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '4'
    geo_nvar: ADM1_NAME
    geo_name: Catamarca & Jujuy & La Rioja & Salta & Santiago Del Estero & Tucuman
    source_row: 144
  - country_entry_id: ARG-SUBNAT-05
    survey_labels: 5 - Patagonia
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ARG_2015_GAULx_5
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARG_2015_GAULx_5
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '5'
    geo_nvar: ADM1_NAME
    geo_name: Chubut & Neuquen & Rio Negro & Santa Cruz & Tierra Del Fuego
    source_row: 145
  - country_entry_id: ARG-SUBNAT-06
    survey_labels: 6 - Noreste Argentino
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ARG_2015_GAULx_6
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ARG_2015_GAULx_6
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '6'
    geo_nvar: ADM1_NAME
    geo_name: Chaco & Corrientes & Formosa & Misiones
    source_row: 146
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ARG-SAN-01
    source_category_code: inodoro_de_compostaje
    national_label_en: Inodoro De Compostaje
    national_label_local: Letrinas de compostaje
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: ARG-SAN-02
    source_category_code: bano_o_letrina_con_desague_a_hoyo_excavaciion_en_la_tierra_etc
    national_label_en: "Bano o letrina con desague a hoyo, excavaci\xEFon en la tierra,\
      \ etc"
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: ARG-SAN-03
    source_category_code: descarga_drenaje_abierto_excavacion_en_la_tierra
    national_label_en: "Descarga: Drenaje Abierto, Excavaci\xF3n En La Tierra"
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: ARG-SAN-04
    source_category_code: bano_o_letrina_con_desague_a_red_publica_cloaca
    national_label_en: Bano o letrina con desague a red publica (cloaca)
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: ARG-SAN-05
    source_category_code: descarga_red_publica
    national_label_en: "Descarga: Red P\xFAblica"
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: ARG-SAN-06
    source_category_code: bano_o_letrina_con_desague_solo_a_pozo_ciego
    national_label_en: Bano o letrina con desague solo a pozo ciego
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: ARG-SAN-07
    source_category_code: descarga_pozo_ciego
    national_label_en: 'Descarga: Pozo Ciego'
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: ARG-SAN-08
    source_category_code: bano_o_letrina_con_desague_a_camara_septica_y_pozo_ciego
    national_label_en: Bano o letrina con desague a camara septica y pozo ciego
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: ARG-SAN-09
    source_category_code: descarga_camara_septica
    national_label_en: "Descarga: C\xE1mara S\xE9ptica"
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: ARG-SAN-10
    source_category_code: bano_o_letrina_con_desague_a_nr
    national_label_en: Bano o letrina con desague a NR
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: ARG-SAN-11
    source_category_code: descarga_no_sabe_donde
    national_label_en: "Descarga: No Sabe D\xF3nde"
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: ARG-SAN-12
    source_category_code: has_flush_toilet
    national_label_en: Has flush toilet
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: ARG-SAN-13
    source_category_code: inodoro_a_hoyo_excavacion_en_tierra
    national_label_en: "Inodoro a hoyo, excavaci\xF3n en tierra"
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: ARG-SAN-14
    source_category_code: inodoro_con_boton_mochila_cadena_y_arrastre_de_agua_a_hoyo_excavacion_en_tierra
    national_label_en: "Inodoro con bot\xF3n/mochila/cadena y arrastre de agua a hoyo,\
      \ excavaci\xF3n en tierra"
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: ARG-SAN-15
    source_category_code: inodoro_con_boton_mochila_cadena_y_arrastre_de_agua_solo_a_otros
    national_label_en: "Inodoro con bot\xF3n/mochila/cadena y arrastre de agua s\xF3\
      lo a otros"
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: ARG-SAN-16
    source_category_code: inodoro_con_boton_mochila_cadena_y_arrastre_de_agua_a_red_publica
    national_label_en: "Inodoro con bot\xF3n/mochila/cadena y arrastre de agua a red\
      \ publica"
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: ARG-SAN-17
    source_category_code: inodoro_con_boton_mochila_cadena_y_arrastre_de_agua_a_red_publica_cloaca
    national_label_en: "Inodoro con bot\xF3n/mochila/cadena y arrastre de agua a red\
      \ p\xFAblica (cloaca)"
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: ARG-SAN-18
    source_category_code: inodoro_con_desague_a_red_publica_cloaca
    national_label_en: "Inodoro con desague a red p\xFAblica(cloaca)"
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: ARG-SAN-19
    source_category_code: inodoro_con_boton_mochila_cadena_y_arrastre_de_agua_solo_a_pozo_ciego
    national_label_en: "Inodoro con bot\xF3n/mochila/cadena y arrastre de agua s\xF3\
      lo a pozo ciego"
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: ARG-SAN-20
    source_category_code: inodoro_con_desague_solo_a_pozo_ciego
    national_label_en: "Inodoro con desague s\xF3lo a pozo ciego"
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: ARG-SAN-21
    source_category_code: inodoro_con_boton_mochila_cadena_y_arrastre_de_agua_a_camara_septica_y_pozo_ciego
    national_label_en: "Inodoro con bot\xF3n/mochila/cadena y arrastre de agua a c\xE1\
      mara s\xE9ptica y pozo ciego"
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: ARG-SAN-22
    source_category_code: inodoro_con_desague_a_camara_septica_y_pozo_ciego
    national_label_en: "Inodoro con desague a c\xE1mara s\xE9ptica y pozo ciego"
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: ARG-SAN-23
    source_category_code: inodoro_con_boton_mochila_cadena_y_arrastre_de_agua_ns_nr
    national_label_en: "Inodoro con bot\xF3n/mochila/cadena y arrastre de agua Ns/nr"
    national_label_local: no sabe donde
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: ARG-SAN-24
    source_category_code: inodoro_con_desague_a_ns_nr
    national_label_en: Inodoro con desague a Ns/Nr
    national_label_local: no sabe donde
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: ARG-SAN-25
    source_category_code: letrina_con_losa
    national_label_en: 'Letrina: Con Losa'
    national_label_local: Letrina simple con loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: ARG-SAN-26
    source_category_code: letrina_sin_arrastre_de_agua_solo_a_pozo_ciego
    national_label_en: Letrina (sin arrastre de agua) solo a pozo ciego
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: ARG-SAN-27
    source_category_code: letrina_sin_losa_pozo_abierto
    national_label_en: 'Letrina: Sin Losa/Pozo Abierto'
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: ARG-SAN-28
    source_category_code: letrina_sin_arrastre_de_agua_a_hoyo_excavacion_en_tierra
    national_label_en: "Letrina (sin arrastre de agua) a hoyo/excavaci\xF3n en tierra"
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARG-SAN-29
    source_category_code: letrina_sin_arrastre_de_agua
    national_label_en: Letrina sin arrastre de agua
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARG-SAN-30
    source_category_code: no_tiene_bano_equipado_con_inodoro_con_arrastre_de_agua
    national_label_en: No tiene bano equipado con inodoro con arrastre de agua
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARG-SAN-31
    source_category_code: inodoro_sin_boton_cadena_y_con_arrastre_de_agua_a_balde_a_hoyo_excavacion_en_tierra
    national_label_en: "Inodoro sin bot\xF3n/cadena y con arrastre de agua (a balde)\
      \ a hoyo, excavaci\xF3n en tierra"
    national_label_local: a drenaje abierto
    jmp_classification: Latrines > Pour flush latrines > to elsewhere
    jmp_id: latrines.pour_flush_latrines.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 90
  - country_entry_id: ARG-SAN-32
    source_category_code: inodoro_sin_boton_mochila_cadena_y_arrastre_de_agua_a_hoyo_excavacion_en_la_tierra_etc
    national_label_en: "Inodoro sin bot\xF3n/mochila/cadena y arrastre de agua/a hoyo,\
      \ excavaci\xF3n en la tierra, etc."
    national_label_local: a drenaje abierto
    jmp_classification: Latrines > Pour flush latrines > to elsewhere
    jmp_id: latrines.pour_flush_latrines.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 90
  - country_entry_id: ARG-SAN-33
    source_category_code: inodoro_sin_boton_cadena_y_con_arrastre_de_agua_a_balde_a_red_publica_cloaca
    national_label_en: "Inodoro sin bot\xF3n/cadena y con arrastre de agua (a balde)\
      \ a red p\xFAblica (cloaca)"
    national_label_local: al alcantarillado
    jmp_classification: Latrines > Pour flush latrines > to piped sewer system
    jmp_id: latrines.pour_flush_latrines.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 86
  - country_entry_id: ARG-SAN-34
    source_category_code: inodoro_sin_boton_mochila_cadena_y_arrastre_de_agua_a_red_publica_cloaca
    national_label_en: "Inodoro sin bot\xF3n/mochila/cadena y arrastre de agua/a red\
      \ p\xFAblica (cloaca)"
    national_label_local: al alcantarillado
    jmp_classification: Latrines > Pour flush latrines > to piped sewer system
    jmp_id: latrines.pour_flush_latrines.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 86
  - country_entry_id: ARG-SAN-35
    source_category_code: inodoro_sin_boton_cadena_y_con_arrastre_de_agua_a_balde_solo_a_pozo_ciego
    national_label_en: "Inodoro sin bot\xF3n/cadena y con arrastre de agua (a balde)\
      \ s\xF3lo a pozo ciego"
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Latrines > Pour flush latrines > to pit
    jmp_id: latrines.pour_flush_latrines.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 88
  - country_entry_id: ARG-SAN-36
    source_category_code: inodoro_sin_boton_cadena_y_con_arrastre_de_agua_a_balde_solo_a_pozo_ciego
    national_label_en: "Inodoro sin bot\xF3n/cadena y con arrastre de agua (a balde)s\xF3\
      lo a pozo ciego"
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Latrines > Pour flush latrines > to pit
    jmp_id: latrines.pour_flush_latrines.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 88
  - country_entry_id: ARG-SAN-37
    source_category_code: inodoro_sin_boton_mochila_cadena_y_arrastre_de_agua_a_solo_a_pozo_ciego
    national_label_en: "Inodoro sin bot\xF3n/mochila/cadena y arrastre de agua/a s\xF3\
      lo a pozo ciego"
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Latrines > Pour flush latrines > to pit
    jmp_id: latrines.pour_flush_latrines.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 88
  - country_entry_id: ARG-SAN-38
    source_category_code: inodoro_sin_boton_cadena_y_con_arrastre_de_agua_a_balde_a_camara_septica_y_pozo_ciego
    national_label_en: "Inodoro sin bot\xF3n/cadena y con arrastre de agua (a balde)\
      \ a c\xE1mara s\xE9ptica y pozo ciego"
    national_label_local: a pozo septico
    jmp_classification: Latrines > Pour flush latrines > to septic tank
    jmp_id: latrines.pour_flush_latrines.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: ARG-SAN-39
    source_category_code: inodoro_sin_boton_mochila_cadena_y_arrastre_de_agua_a_camara_septica_y_pozo_ciego
    national_label_en: "Inodoro sin bot\xF3n/mochila/cadena y arrastre de agua/a c\xE1\
      mara s\xE9ptica y pozo ciego"
    national_label_local: a pozo septico
    jmp_classification: Latrines > Pour flush latrines > to septic tank
    jmp_id: latrines.pour_flush_latrines.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: ARG-SAN-40
    source_category_code: inodoro_sin_boton_cadena_y_con_arrastre_de_agua_a_balde_ns_nr
    national_label_en: "Inodoro sin bot\xF3n/cadena y con arrastre de agua (a balde)\
      \ Ns/nr"
    national_label_local: no sabe donde
    jmp_classification: Latrines > Pour flush latrines > to unknown place/ not sure/DK
    jmp_id: latrines.pour_flush_latrines.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 89
  - country_entry_id: ARG-SAN-41
    source_category_code: no_hay_instalacion_sanitaria_monte_campo
    national_label_en: "No Hay Instalaci\xF3n Sanitaria / Monte / Campo"
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: ARG-SAN-42
    source_category_code: no_tiene_bano
    national_label_en: No tiene bano
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: ARG-SAN-43
    source_category_code: no_tiene_bano_o_letrina
    national_label_en: "No tiene ba\xF1o o letrina"
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: ARG-SAN-44
    source_category_code: no_tiene_letrina_o_bano
    national_label_en: No tiene letrina o bano
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: ARG-SAN-45
    source_category_code: no_flush_toilet
    national_label_en: No flush toilet
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: ARG-SAN-46
    source_category_code: otro_especifique
    national_label_en: Otro (Especifique)
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_ARG_Argentina_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ARG-WAS-01
    source_category_code: aljibe_o_pozo_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: Aljibe o pozo fuera de la vivienda pero dentro del terreno
    national_label_local: Otro
    jmp_classification: Ground water > All springs > Other
    jmp_id: ground_water.all_springs.other
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 77
  - country_entry_id: ARG-WAS-02
    source_category_code: pozo_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: Pozo fuera de la vivienda pero dentro del terreno
    national_label_local: Otro
    jmp_classification: Ground water > All springs > Other
    jmp_id: ground_water.all_springs.other
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 77
  - country_entry_id: ARG-WAS-03
    source_category_code: aljibe_o_pozo_por_caneria_dentro_de_la_vivienda
    national_label_en: "Aljibe o pozo por ca\xF1er\xEDa dentro de la vivienda"
    national_label_local: Privado
    jmp_classification: Ground water > All springs > Private
    jmp_id: ground_water.all_springs.private
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 75
  - country_entry_id: ARG-WAS-04
    source_category_code: pozo_por_caneria_dentro_de_la_vivienda
    national_label_en: "Pozo por ca\xF1er\xEDa dentro de la vivienda"
    national_label_local: Privado
    jmp_classification: Ground water > All springs > Private
    jmp_id: ground_water.all_springs.private
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 75
  - country_entry_id: ARG-WAS-05
    source_category_code: aljibe_o_pozo_fuera_del_terreno
    national_label_en: Aljibe o pozo fuera del terreno
    national_label_local: Publico
    jmp_classification: Ground water > All springs > Public
    jmp_id: ground_water.all_springs.public
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: true
    source_row: 76
  - country_entry_id: ARG-WAS-06
    source_category_code: pozo_fuera_del_terreno
    national_label_en: Pozo fuera del terreno
    national_label_local: Publico
    jmp_classification: Ground water > All springs > Public
    jmp_id: ground_water.all_springs.public
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: true
    source_row: 76
  - country_entry_id: ARG-WAS-07
    source_category_code: pozo_protegido
    national_label_en: Pozo Protegido
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: ARG-WAS-08
    source_category_code: perforacion_con_bomba_manual_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: "Perforaci\xF3n con bomba manual fuera de la vivienda pero\
      \ dentro del terreno"
    national_label_local: Otro
    jmp_classification: Ground water > Protected well > Other
    jmp_id: ground_water.protected_well.other
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: ARG-WAS-09
    source_category_code: perforacion_con_bomba_manual_por_caneria_dentro_de_la_vivienda
    national_label_en: "Perforaci\xF3n con bomba manual por ca\xF1er\xEDa dentro de\
      \ la vivienda"
    national_label_local: Privado
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: ARG-WAS-10
    source_category_code: perforacion_con_bomba_manual_fuera_del_terreno
    national_label_en: "Perforaci\xF3n con bomba manual fuera del terreno"
    national_label_local: Publico
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 68
  - country_entry_id: ARG-WAS-11
    source_category_code: pozo_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: Pozo fuera de la vivienda pero dentro del terreno
    national_label_local: Otro
    jmp_classification: Ground water > Traditional wells > Other
    jmp_id: ground_water.traditional_wells.other
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: ARG-WAS-12
    source_category_code: pozo_por_caneria_dentro_de_la_vivienda
    national_label_en: "Pozo por ca\xF1er\xEDa dentro de la vivienda"
    national_label_local: Privado
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 63
  - country_entry_id: ARG-WAS-13
    source_category_code: pozo_fuera_del_terreno
    national_label_en: Pozo fuera del terreno
    national_label_local: Publico
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 64
  - country_entry_id: ARG-WAS-14
    source_category_code: pozo_con_tuberia
    national_label_en: "Pozo Con Tuber\xEDa"
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: ARG-WAS-15
    source_category_code: perforacion_con_bomba_a_motor_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: "Perforaci\xF3n con bomba a motor fuera de la vivienda pero\
      \ dentro del terreno"
    national_label_local: Otro
    jmp_classification: Ground water > Tubewell, borehole > Other
    jmp_id: ground_water.tubewell_borehole.other
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: ARG-WAS-16
    source_category_code: perforacion_con_bomba_a_motor_por_caneria_dentro_de_la_vivienda
    national_label_en: "Perforaci\xF3n con bomba a motor por ca\xF1er\xEDa dentro\
      \ de la vivienda"
    national_label_local: Privado
    jmp_classification: Ground water > Tubewell, borehole > Private
    jmp_id: ground_water.tubewell_borehole.private
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 59
  - country_entry_id: ARG-WAS-17
    source_category_code: perforacion_con_bomba_a_motor_fuera_del_terreno
    national_label_en: "Perforaci\xF3n con bomba a motor fuera del terreno"
    national_label_local: Publico
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 60
  - country_entry_id: ARG-WAS-18
    source_category_code: pozo_no_protegido
    national_label_en: Pozo No Protegido
    national_label_local: Pozos non protegidos
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: ARG-WAS-19
    source_category_code: otras_fuentes_por_caneria_dentro_de_la_vivienda
    national_label_en: "otras fuentes por ca\xF1er\xEDa dentro de la vivienda"
    national_label_local: Otro
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: ARG-WAS-20
    source_category_code: camion_cisterna
    national_label_en: "Cami\xF3n Cisterna"
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: ARG-WAS-21
    source_category_code: transporte_por_cisterna
    national_label_en: Transporte por cisterna
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: ARG-WAS-22
    source_category_code: otras_fuentes_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: otras fuentes fuera de la vivienda, pero dentro del terreno
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: ARG-WAS-23
    source_category_code: otras_fuentes_por_caneria_dentro_de_la_vivienda
    national_label_en: "Otras fuentes por ca\xF1er\xEDa dentro de la vivienda"
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: ARG-WAS-24
    source_category_code: otro_especifique
    national_label_en: Otro (Especifique)
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: ARG-WAS-25
    source_category_code: otro_por_caneria_dentro_de_la_vivienda_o_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: "Otro por ca\xF1er\xEDa dentro de la vivienda o fuera de la\
      \ vivienda pero dentro del terreno"
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: ARG-WAS-26
    source_category_code: otras
    national_label_en: Otras
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARG-WAS-27
    source_category_code: otras_fuentes_fuera_de_la_vivienda_o_del_terreno
    national_label_en: Otras fuentes fuera de la vivienda o del terreno
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARG-WAS-28
    source_category_code: otras_fuentes_fuera_del_terreno
    national_label_en: otras fuentes fuera del terreno
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: ARG-WAS-29
    source_category_code: agua_embotellada
    national_label_en: Agua Embotellada
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: ARG-WAS-30
    source_category_code: bolsa_de_agua
    national_label_en: Bolsa De Agua
    national_label_local: Agua en bolsita
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: ARG-WAS-31
    source_category_code: agua_de_lluvia
    national_label_en: Agua De Lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: ARG-WAS-32
    source_category_code: agua_de_lluvia_rio_canal_arroyo
    national_label_en: Agua de lluvia, rio, canal, arroyo
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: ARG-WAS-33
    source_category_code: agua_de_lluvia_rio_canal_arroyo_o_acequia
    national_label_en: "Agua de lluvia, r\xEDo, canal, arroyo o acequia"
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: ARG-WAS-34
    source_category_code: agua_de_superficie_rio_represa_lago_estanque_arroyo_canal
    national_label_en: "Agua De Superficie (R\xEDo, Represa, Lago, Estanque, Arroyo,\
      \ Canal)"
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: ARG-WAS-35
    source_category_code: caneria_conectada_al_vecino
    national_label_en: "Ca\xF1er\xEDa Conectada Al Vecino"
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: ARG-WAS-36
    source_category_code: agua_de_red_publica_por_caneria_dentro_de_la_vivienda
    national_label_en: "Agua de red p\xFAblica, por ca\xF1er\xEDa dentro de la vivienda"
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: ARG-WAS-37
    source_category_code: caneria_dentro_de_la_vivienda
    national_label_en: "Ca\xF1er\xEDa Dentro De La Vivienda"
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: ARG-WAS-38
    source_category_code: red_publica_agua_corriente_por_caneria_dentro_de_la_vivienda
    national_label_en: "Red p\xFAblica (agua corriente) por ca\xF1er\xEDa dentro de\
      \ la vivienda"
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: ARG-WAS-39
    source_category_code: agua_de_red_publica_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: "Agua de red p\xFAblica, fuera de la vivienda pero dentro del\
      \ terreno"
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: ARG-WAS-40
    source_category_code: caneria_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: "Ca\xF1er\xEDa Fuera De La Vivienda, Pero Dentro Del Terreno"
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: ARG-WAS-41
    source_category_code: red_publica_agua_corriente_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: "Red p\xFAblica (agua corriente) fuera de la vivienda pero\
      \ dentro del terreno"
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: ARG-WAS-42
    source_category_code: agua_de_red_publica_fuera_del_terreno
    national_label_en: "Agua de red p\xFAblica, fuera del terreno"
    national_label_local: "Fuentes p\xFAblicas"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: ARG-WAS-43
    source_category_code: canilla_grifo_publico
    national_label_en: "Canilla/Grifo P\xFAblico"
    national_label_local: "Fuentes p\xFAblicas"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: ARG-WAS-44
    source_category_code: red_publica_agua_corriente_fuera_del_terreno
    national_label_en: "Red p\xFAblica (agua corriente) fuera del terreno"
    national_label_local: "Fuentes p\xFAblicas"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_ARG_Argentina_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1996
  effective_to: null
  selectors: null
  value: 14
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

