---
country_id: CTY-VEN
iso3: VEN
schema_version: '0.2'
status: draft
country_name: VEN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: VEN-EDU-01
    national_label_en: Early childhood education
    national_label_local: "Educaci\xF3n Inicial - Maternal"
    entry_age: 0
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
  - country_entry_id: VEN-EDU-02
    national_label_en: Special early childhood education
    national_label_local: "Educaci\xF3n Especial Inicial - Maternal"
    entry_age: 1
    duration_years: 2
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
  - country_entry_id: VEN-EDU-03
    national_label_en: Pre-school education
    national_label_local: "Educaci\xF3n Inicial - Preescolar"
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: VEN-EDU-04
    national_label_en: Special pre-school education
    national_label_local: "Educaci\xF3n Especial Inicial - Preescolar"
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: VEN-EDU-05
    national_label_en: Primary education
    national_label_local: "Educaci\xF3n Primaria"
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 11
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - VEN-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: VEN-EDU-06
    national_label_en: Special education - Primary
    national_label_local: "Educaci\xF3n Especial - Primaria"
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 12
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - VEN-EDU-06
    cum_years_status: computed
    review_flags: []
  - country_entry_id: VEN-EDU-07
    national_label_en: Adult and youth primary education
    national_label_local: "Educaci\xF3n Primaria para j\xF3venes y adultos"
    entry_age: 15
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 13
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - VEN-EDU-07
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: VEN-EDU-08
    national_label_en: Lower-middle general  education
    national_label_local: "Educaci\xF3n Media General Baja"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - VEN-EDU-05
    - VEN-EDU-06
    cum_years_schooling: 9
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
  - country_entry_id: VEN-EDU-09
    national_label_en: Lower-middle technical education
    national_label_local: "Educaci\xF3n Media T\xE9cnica Baja"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - VEN-EDU-05
    - VEN-EDU-06
    cum_years_schooling: 9
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
  - country_entry_id: VEN-EDU-10
    national_label_en: Special lower-middle general  education
    national_label_local: "Educaci\xF3n Especial Media General Baja"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - VEN-EDU-05
    - VEN-EDU-06
    cum_years_schooling: 9
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
  - country_entry_id: VEN-EDU-11
    national_label_en: Youth and adult lower-middle general  education
    national_label_local: "Educaci\xF3n Media General Baja para J\xF3venes y Adultos"
    entry_age: 15
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 17
    parent_country_entry_ids:
    - VEN-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - VEN-EDU-07
    - VEN-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: VEN-EDU-12
    national_label_en: Upper-middle general education
    national_label_local: "Educaci\xF3n Media General Alta"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 18
    parent_country_entry_ids:
    - VEN-EDU-08
    - VEN-EDU-09
    - VEN-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    - VEN-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
    - 'minimum parent path selected from: VEN-EDU-08, VEN-EDU-09, VEN-EDU-10'
  - country_entry_id: VEN-EDU-13
    national_label_en: Upper-middle technical education
    national_label_local: "Educaci\xF3n Media T\xE9cnica Alta"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 19
    parent_country_entry_ids:
    - VEN-EDU-08
    - VEN-EDU-09
    - VEN-EDU-10
    cum_years_schooling: 12
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    - VEN-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
    - 'minimum parent path selected from: VEN-EDU-08, VEN-EDU-09, VEN-EDU-10'
  - country_entry_id: VEN-EDU-14
    national_label_en: Special upper-middle  general education
    national_label_local: "Educaci\xF3n Especial Media General Alta"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 20
    parent_country_entry_ids:
    - VEN-EDU-08
    - VEN-EDU-09
    - VEN-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    - VEN-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
    - 'minimum parent path selected from: VEN-EDU-08, VEN-EDU-09, VEN-EDU-10'
  - country_entry_id: VEN-EDU-15
    national_label_en: Youth and adult upper-middle general education
    national_label_local: "Educaci\xF3n Media General Alta para J\xF3venes y Adultos"
    entry_age: 18
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 21
    parent_country_entry_ids:
    - VEN-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - VEN-EDU-07
    - VEN-EDU-11
    - VEN-EDU-15
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: VEN-EDU-16
    national_label_en: University higher technical education
    national_label_local: "T\xE9cnico Superior Universitario"
    entry_age: 17
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - VEN-EDU-12
    - VEN-EDU-14
    cum_years_schooling: 14
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    - VEN-EDU-12
    - VEN-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
    - 'minimum parent path selected from: VEN-EDU-08, VEN-EDU-09, VEN-EDU-10'
    - 'minimum parent path selected from: VEN-EDU-12, VEN-EDU-14'
  - country_entry_id: VEN-EDU-17
    national_label_en: Technical specialization
    national_label_local: "Especializaci\xF3n T\xE9cnica"
    entry_age: 20
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - VEN-EDU-12
    - VEN-EDU-14
    cum_years_schooling: 12
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    - VEN-EDU-12
    - VEN-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
    - 'minimum parent path selected from: VEN-EDU-08, VEN-EDU-09, VEN-EDU-10'
    - 'minimum parent path selected from: VEN-EDU-12, VEN-EDU-14'
  - country_entry_id: VEN-EDU-18
    national_label_en: Bachelor programmes
    national_label_local: Licenciaturas
    entry_age: 17
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - VEN-EDU-12
    - VEN-EDU-14
    cum_years_schooling: 16
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    - VEN-EDU-12
    - VEN-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
    - 'minimum parent path selected from: VEN-EDU-08, VEN-EDU-09, VEN-EDU-10'
    - 'minimum parent path selected from: VEN-EDU-12, VEN-EDU-14'
  - country_entry_id: VEN-EDU-19
    national_label_en: Specialization
    national_label_local: "Especializaci\xF3n"
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - VEN-EDU-12
    - VEN-EDU-14
    cum_years_schooling: 12
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    - VEN-EDU-12
    - VEN-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
    - 'minimum parent path selected from: VEN-EDU-08, VEN-EDU-09, VEN-EDU-10'
    - 'minimum parent path selected from: VEN-EDU-12, VEN-EDU-14'
  - country_entry_id: VEN-EDU-20
    national_label_en: Master's programmes
    national_label_local: "Maestr\xEDa"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - VEN-EDU-17
    - VEN-EDU-18
    - VEN-EDU-19
    cum_years_schooling: 14
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    - VEN-EDU-12
    - VEN-EDU-17
    - VEN-EDU-20
    cum_years_status: computed
    review_flags: &id002
    - 'minimum parent path selected from: VEN-EDU-05, VEN-EDU-06'
    - 'minimum parent path selected from: VEN-EDU-08, VEN-EDU-09, VEN-EDU-10'
    - 'minimum parent path selected from: VEN-EDU-12, VEN-EDU-14'
    - 'minimum parent path selected from: VEN-EDU-17, VEN-EDU-18, VEN-EDU-19'
  - country_entry_id: VEN-EDU-21
    national_label_en: Doctorate
    national_label_local: Doctorado
    entry_age: 22
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - VEN-EDU-20
    cum_years_schooling: 17
    cum_years_computation_path:
    - VEN-EDU-05
    - VEN-EDU-08
    - VEN-EDU-12
    - VEN-EDU-17
    - VEN-EDU-20
    - VEN-EDU-21
    cum_years_status: computed
    review_flags: *id002
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Venezuela
      Bolivarian Republic of.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: VEN-WAS-01
    source_category_code: manantial_protegido
    national_label_en: Manantial protegido
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: VEN-WAS-02
    source_category_code: pozo_protegido_cubierto
    national_label_en: Pozo protegido/cubierto
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: VEN-WAS-03
    source_category_code: pozo_con_tuberia_con_bomba
    national_label_en: Pozo con tuberia/ con bomba
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: VEN-WAS-04
    source_category_code: manantial_no_protegido
    national_label_en: Manantial no protegido
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: VEN-WAS-05
    source_category_code: pozo_no_protegide_sin_cubierto
    national_label_en: Pozo no protegide/sin cubierto
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: VEN-WAS-06
    source_category_code: camiontanque_vendedor
    national_label_en: Camiontanque, vendedor
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: VEN-WAS-07
    source_category_code: otra
    national_label_en: Otra
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: VEN-WAS-08
    source_category_code: agua_embotellada
    national_label_en: Agua embotellada
    national_label_local: Sachet water
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: VEN-WAS-09
    source_category_code: agua_lluvia
    national_label_en: Agua lluvia
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: VEN-WAS-10
    source_category_code: charca_estanque_rio_o_arroyo
    national_label_en: Charca/estanque, rio o arroyo
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: VEN-WAS-11
    source_category_code: tuberia_dentro_de_vivienda
    national_label_en: Tuberia dentro de vivienda
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: VEN-WAS-12
    source_category_code: tuberia_en_el_patio
    national_label_en: Tuberia en el patio
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: VEN-WAS-13
    source_category_code: llave_publica
    national_label_en: Llave publica
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_VEN_Venezuela_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1990
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

