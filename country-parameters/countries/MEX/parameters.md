---
country_id: CTY-MEX
iso3: MEX
schema_version: '0.2'
status: draft
country_name: MEX
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: MEX-EDU-01
    national_label_en: Pre-primary Education
    national_label_local: Educación Preescolar
    entry_age: 3
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 6
  - country_entry_id: MEX-EDU-02
    national_label_en: Primary Education
    national_label_local: Educación Primaria
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 7
  - country_entry_id: MEX-EDU-03
    national_label_en: Lower Secondary Education
    national_label_local: Educación Secundaria
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 8
  - country_entry_id: MEX-EDU-04
    national_label_en: Job Training
    national_label_local: Capacitación para el Trabajo
    entry_age: 15
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 9
  - country_entry_id: MEX-EDU-05
    national_label_en: Upper Secondary Education (General Programs)
    national_label_local: Bachillerato General, Bachillerato por Cooperación, Bachillerato
      Pedagógico, Bachillerato de Arte
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 10
  - country_entry_id: MEX-EDU-06
    national_label_en: Upper Secondary (combined General and Technical Programs)
    national_label_local: Bachillerato Tecnológico, Profesional Técnico Bachiller
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 11
  - country_entry_id: MEX-EDU-07
    national_label_en: Upper Secondary (Vocational or Technical Programs)
    national_label_local: Profesional Técnico
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 12
  - country_entry_id: MEX-EDU-08
    national_label_en: Technical Professional Education (Technological Institute Program)
    national_label_local: Técnico Superior
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
  - country_entry_id: MEX-EDU-09
    national_label_en: Teacher's College (Bachelor´s Degree Program)
    national_label_local: Educación Normal Licenciatura
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - country_entry_id: MEX-EDU-10
    national_label_en: Master´s Degree Program (Postgraduate Studies) (long)
    national_label_local: Maestría
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: MEX-EDU-11
    national_label_en: Specialisation Program (Postgraduate Studies) (short)
    national_label_local: Especialización
    entry_age: 23
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Mexico.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: MEX-SUBNAT-01
    survey_labels: '2028'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2028'
    geo_nvar: ADM1_NAME
    geo_name: Aguascalientes
    source_row: 9456
  - country_entry_id: MEX-SUBNAT-02
    survey_labels: '2029'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2029'
    geo_nvar: ADM1_NAME
    geo_name: Baja California
    source_row: 9457
  - country_entry_id: MEX-SUBNAT-03
    survey_labels: '2030'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2030'
    geo_nvar: ADM1_NAME
    geo_name: Baja California Sur
    source_row: 9458
  - country_entry_id: MEX-SUBNAT-04
    survey_labels: '2031'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2031'
    geo_nvar: ADM1_NAME
    geo_name: Campeche
    source_row: 9459
  - country_entry_id: MEX-SUBNAT-05
    survey_labels: '2032'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2032'
    geo_nvar: ADM1_NAME
    geo_name: Chiapas
    source_row: 9460
  - country_entry_id: MEX-SUBNAT-06
    survey_labels: '2033'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2033'
    geo_nvar: ADM1_NAME
    geo_name: Chihuahua
    source_row: 9461
  - country_entry_id: MEX-SUBNAT-07
    survey_labels: '2034'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2034'
    geo_nvar: ADM1_NAME
    geo_name: Coahuila
    source_row: 9462
  - country_entry_id: MEX-SUBNAT-08
    survey_labels: '2035'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2035'
    geo_nvar: ADM1_NAME
    geo_name: Colima
    source_row: 9463
  - country_entry_id: MEX-SUBNAT-09
    survey_labels: '2036'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2036'
    geo_nvar: ADM1_NAME
    geo_name: Distrito Federal
    source_row: 9464
  - country_entry_id: MEX-SUBNAT-10
    survey_labels: '2037'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2037'
    geo_nvar: ADM1_NAME
    geo_name: Durango
    source_row: 9465
  - country_entry_id: MEX-SUBNAT-11
    survey_labels: '2038'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2038'
    geo_nvar: ADM1_NAME
    geo_name: Guanajuato
    source_row: 9466
  - country_entry_id: MEX-SUBNAT-12
    survey_labels: '2039'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2039'
    geo_nvar: ADM1_NAME
    geo_name: Guerrero
    source_row: 9467
  - country_entry_id: MEX-SUBNAT-13
    survey_labels: '2040'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2040'
    geo_nvar: ADM1_NAME
    geo_name: Hidalgo
    source_row: 9468
  - country_entry_id: MEX-SUBNAT-14
    survey_labels: '2041'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2041'
    geo_nvar: ADM1_NAME
    geo_name: Jalisco
    source_row: 9469
  - country_entry_id: MEX-SUBNAT-15
    survey_labels: '2042'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2042'
    geo_nvar: ADM1_NAME
    geo_name: Mexico
    source_row: 9470
  - country_entry_id: MEX-SUBNAT-16
    survey_labels: '2043'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2043'
    geo_nvar: ADM1_NAME
    geo_name: Michoacan
    source_row: 9471
  - country_entry_id: MEX-SUBNAT-17
    survey_labels: '2044'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2044'
    geo_nvar: ADM1_NAME
    geo_name: Morelos
    source_row: 9472
  - country_entry_id: MEX-SUBNAT-18
    survey_labels: '2045'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2045'
    geo_nvar: ADM1_NAME
    geo_name: Nayarit
    source_row: 9473
  - country_entry_id: MEX-SUBNAT-19
    survey_labels: '2046'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2046'
    geo_nvar: ADM1_NAME
    geo_name: Nuevo Leon
    source_row: 9474
  - country_entry_id: MEX-SUBNAT-20
    survey_labels: '2047'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2047'
    geo_nvar: ADM1_NAME
    geo_name: Oaxaca
    source_row: 9475
  - country_entry_id: MEX-SUBNAT-21
    survey_labels: '2048'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2048'
    geo_nvar: ADM1_NAME
    geo_name: Puebla
    source_row: 9476
  - country_entry_id: MEX-SUBNAT-22
    survey_labels: '2049'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2049'
    geo_nvar: ADM1_NAME
    geo_name: Queretaro
    source_row: 9477
  - country_entry_id: MEX-SUBNAT-23
    survey_labels: '2050'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2050'
    geo_nvar: ADM1_NAME
    geo_name: Quintana Roo
    source_row: 9478
  - country_entry_id: MEX-SUBNAT-24
    survey_labels: '2051'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2051'
    geo_nvar: ADM1_NAME
    geo_name: San Luis Potosi
    source_row: 9479
  - country_entry_id: MEX-SUBNAT-25
    survey_labels: '2052'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2052'
    geo_nvar: ADM1_NAME
    geo_name: Sinaloa
    source_row: 9480
  - country_entry_id: MEX-SUBNAT-26
    survey_labels: '2053'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2053'
    geo_nvar: ADM1_NAME
    geo_name: Sonora
    source_row: 9481
  - country_entry_id: MEX-SUBNAT-27
    survey_labels: '2054'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2054'
    geo_nvar: ADM1_NAME
    geo_name: Tabasco
    source_row: 9482
  - country_entry_id: MEX-SUBNAT-28
    survey_labels: '2055'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2055'
    geo_nvar: ADM1_NAME
    geo_name: Tamaulipas
    source_row: 9483
  - country_entry_id: MEX-SUBNAT-29
    survey_labels: '2056'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2056'
    geo_nvar: ADM1_NAME
    geo_name: Tlaxcala
    source_row: 9484
  - country_entry_id: MEX-SUBNAT-30
    survey_labels: '2057'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2057'
    geo_nvar: ADM1_NAME
    geo_name: Veracruz
    source_row: 9485
  - country_entry_id: MEX-SUBNAT-31
    survey_labels: '2058'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2058'
    geo_nvar: ADM1_NAME
    geo_name: Yucatan
    source_row: 9486
  - country_entry_id: MEX-SUBNAT-32
    survey_labels: '2059'
    survey_variables: gaul_adm1_code
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2059'
    geo_nvar: ADM1_NAME
    geo_name: Zacatecas
    source_row: 9487
  - country_entry_id: MEX-SUBNAT-33
    survey_labels: 1 - Aguascalientes
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2028
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
    geo_id: '2028'
    geo_nvar: ADM1_NAME
    geo_name: Aguascalientes
    source_row: 9904
  - country_entry_id: MEX-SUBNAT-34
    survey_labels: 10 - Durango
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2037
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
    geo_id: '2037'
    geo_nvar: ADM1_NAME
    geo_name: Durango
    source_row: 9905
  - country_entry_id: MEX-SUBNAT-35
    survey_labels: 11 - Guanjuato
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2038
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
    geo_id: '2038'
    geo_nvar: ADM1_NAME
    geo_name: Guanajuato
    source_row: 9906
  - country_entry_id: MEX-SUBNAT-36
    survey_labels: 12 - Guerrero
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2039
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
    geo_id: '2039'
    geo_nvar: ADM1_NAME
    geo_name: Guerrero
    source_row: 9907
  - country_entry_id: MEX-SUBNAT-37
    survey_labels: 13 - Hidalgo
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2040
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
    geo_id: '2040'
    geo_nvar: ADM1_NAME
    geo_name: Hidalgo
    source_row: 9908
  - country_entry_id: MEX-SUBNAT-38
    survey_labels: 14 - Jalisco
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2041
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
    geo_id: '2041'
    geo_nvar: ADM1_NAME
    geo_name: Jalisco
    source_row: 9909
  - country_entry_id: MEX-SUBNAT-39
    survey_labels: 15 - Mexico
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2042
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
    geo_id: '2042'
    geo_nvar: ADM1_NAME
    geo_name: Mexico
    source_row: 9910
  - country_entry_id: MEX-SUBNAT-40
    survey_labels: 16 - Michoacan
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2043
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
    geo_id: '2043'
    geo_nvar: ADM1_NAME
    geo_name: Michoacan
    source_row: 9911
  - country_entry_id: MEX-SUBNAT-41
    survey_labels: 17 - Morelos
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2044
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
    geo_id: '2044'
    geo_nvar: ADM1_NAME
    geo_name: Morelos
    source_row: 9912
  - country_entry_id: MEX-SUBNAT-42
    survey_labels: 18 - Nayarit
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2045
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
    geo_id: '2045'
    geo_nvar: ADM1_NAME
    geo_name: Nayarit
    source_row: 9913
  - country_entry_id: MEX-SUBNAT-43
    survey_labels: 19 - Nuevo Leon
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2046
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
    geo_id: '2046'
    geo_nvar: ADM1_NAME
    geo_name: Nuevo Leon
    source_row: 9914
  - country_entry_id: MEX-SUBNAT-44
    survey_labels: 2 - Baja California
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2029
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
    geo_id: '2029'
    geo_nvar: ADM1_NAME
    geo_name: Baja California
    source_row: 9915
  - country_entry_id: MEX-SUBNAT-45
    survey_labels: 20 - Oaxaca
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2047
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
    geo_id: '2047'
    geo_nvar: ADM1_NAME
    geo_name: Oaxaca
    source_row: 9916
  - country_entry_id: MEX-SUBNAT-46
    survey_labels: 21 - Puebla
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2048
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
    geo_id: '2048'
    geo_nvar: ADM1_NAME
    geo_name: Puebla
    source_row: 9917
  - country_entry_id: MEX-SUBNAT-47
    survey_labels: 22 - Queretaro de Arteaga
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2049
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
    geo_id: '2049'
    geo_nvar: ADM1_NAME
    geo_name: Queretaro
    source_row: 9918
  - country_entry_id: MEX-SUBNAT-48
    survey_labels: 23 - Quintana Roo
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2050
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
    geo_id: '2050'
    geo_nvar: ADM1_NAME
    geo_name: Quintana Roo
    source_row: 9919
  - country_entry_id: MEX-SUBNAT-49
    survey_labels: 24 - San Luis Potosi
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2051
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
    geo_id: '2051'
    geo_nvar: ADM1_NAME
    geo_name: San Luis Potosi
    source_row: 9920
  - country_entry_id: MEX-SUBNAT-50
    survey_labels: 25 - Sinaloa
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2052
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
    geo_id: '2052'
    geo_nvar: ADM1_NAME
    geo_name: Sinaloa
    source_row: 9921
  - country_entry_id: MEX-SUBNAT-51
    survey_labels: 26 - Sonora
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2053
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
    geo_id: '2053'
    geo_nvar: ADM1_NAME
    geo_name: Sonora
    source_row: 9922
  - country_entry_id: MEX-SUBNAT-52
    survey_labels: 27 - Tabasco
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2054
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
    geo_id: '2054'
    geo_nvar: ADM1_NAME
    geo_name: Tabasco
    source_row: 9923
  - country_entry_id: MEX-SUBNAT-53
    survey_labels: 28 - Tamaulipas
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2055
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
    geo_id: '2055'
    geo_nvar: ADM1_NAME
    geo_name: Tamaulipas
    source_row: 9924
  - country_entry_id: MEX-SUBNAT-54
    survey_labels: 29 - Tlaxcala
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2056
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
    geo_id: '2056'
    geo_nvar: ADM1_NAME
    geo_name: Tlaxcala
    source_row: 9925
  - country_entry_id: MEX-SUBNAT-55
    survey_labels: 3 - Baja California Sur
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2030
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
    geo_id: '2030'
    geo_nvar: ADM1_NAME
    geo_name: Baja California Sur
    source_row: 9926
  - country_entry_id: MEX-SUBNAT-56
    survey_labels: 30 - Veracruz-Llave
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2057
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
    geo_id: '2057'
    geo_nvar: ADM1_NAME
    geo_name: Veracruz
    source_row: 9927
  - country_entry_id: MEX-SUBNAT-57
    survey_labels: 31 - Yucatan
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2058
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
    geo_id: '2058'
    geo_nvar: ADM1_NAME
    geo_name: Yucatan
    source_row: 9928
  - country_entry_id: MEX-SUBNAT-58
    survey_labels: 32 - Zacatecas
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2059
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
    geo_id: '2059'
    geo_nvar: ADM1_NAME
    geo_name: Zacatecas
    source_row: 9929
  - country_entry_id: MEX-SUBNAT-59
    survey_labels: 4 - Campeche
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2031
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
    geo_id: '2031'
    geo_nvar: ADM1_NAME
    geo_name: Campeche
    source_row: 9930
  - country_entry_id: MEX-SUBNAT-60
    survey_labels: 5 - Cohauila
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2034
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
    geo_id: '2034'
    geo_nvar: ADM1_NAME
    geo_name: Coahuila
    source_row: 9931
  - country_entry_id: MEX-SUBNAT-61
    survey_labels: 6 - Colima
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2035
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
    geo_id: '2035'
    geo_nvar: ADM1_NAME
    geo_name: Colima
    source_row: 9932
  - country_entry_id: MEX-SUBNAT-62
    survey_labels: 7 - Chiapas
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2032
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
    geo_id: '2032'
    geo_nvar: ADM1_NAME
    geo_name: Chiapas
    source_row: 9933
  - country_entry_id: MEX-SUBNAT-63
    survey_labels: 8 - Chihuahua
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2033
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
    geo_id: '2033'
    geo_nvar: ADM1_NAME
    geo_name: Chihuahua
    source_row: 9934
  - country_entry_id: MEX-SUBNAT-64
    survey_labels: 9 - Distrito Federal
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: MEX_2015_GAUL1_2036
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
    geo_id: '2036'
    geo_nvar: ADM1_NAME
    geo_name: Distrito Federal
    source_row: 9935
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
  - country_entry_id: MEX-SAN-01
    source_category_code: composting_toilet
    national_label_en: composting toilet
    national_label_local: Letrinas de compostaje
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: MEX-SAN-02
    source_category_code: excusado_de_compostaje
    national_label_en: Excusado de compostaje
    national_label_local: Letrinas de compostaje
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: MEX-SAN-03
    source_category_code: composting_toilet_not_shared
    national_label_en: composting toilet - not shared
    national_label_local: Letrinas de compostaje (privado)
    jmp_classification: Composting toilets > Composting toilet (private)
    jmp_id: composting_toilets.composting_toilet_private
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 129
  - country_entry_id: MEX-SAN-04
    source_category_code: conectado_a_una_tuberia_que_va_a_dar_a_un_rio_lago_o_mar_connectado_a_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta
    national_label_en: Conectado a una tubería que va a dar a un río, lago o mar +
      Connectado a una tubería que va a dar a una barranca o grieta
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-05
    source_category_code: conectado_a_una_tuberia_que_va_dar_a_un_rio_lago_o_mar
    national_label_en: conectado a una tuberia que va dar a un rio, lago o mar
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-06
    source_category_code: connected_to_pipes_that_go_into_a_ravine_or_creek_pipes_that_go_into_a_river_lake_or_sea
    national_label_en: Connected to pipes that go into a ravine or creek + Pipes that
      go into a river, lake or sea
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-07
    source_category_code: descarga_a_otra_parte
    national_label_en: Descarga a otra parte
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-08
    source_category_code: descarga_a_tuberia_que_va_a_dar_a_una_barranca_o_grieta_rio_lago_o_mar
    national_label_en: Descarga a tubería que va a dar a una barranca o grieta/río,
      lago o mar
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-09
    source_category_code: excusado_conectado_a_una_tuberia_que_va_dar_a_un_rio_lago_o_mar
    national_label_en: Excusado conectado a una tuberia que va dar a un rio, lago
      o mar
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-10
    source_category_code: excusado_retrete_o_sanita_con_descarga_a_una_tuberia_que_va_a_dar_a_un_rio_lago_o_mar
    national_label_en: Excusado, retrete o sanita con descarga a una tubería que va
      a dar a un río, lago o mar
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-11
    source_category_code: excusado_letrina_conectado_a_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_un_rio_lago_o_mar
    national_label_en: 'Excusado/letrina: conectado a una tuberia que va a dar a una
      barranca o grieta, un rio, lago o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-12
    source_category_code: excusado_retrete_sanitario_letrina_u_hoyo_negro_conectado_a_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_o_un_rio_lago_o_mar
    national_label_en: 'Excusado/retrete/sanitario(letrina u hoyo negro): Conectado
      a una tubería que va a dar a una barranca o grieta o un rio, lago o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-13
    source_category_code: flush_pour_to_other_location
    national_label_en: flush/pour to other location
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-14
    source_category_code: taza_de_bano_excusado_sanitario_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_rio_o_mar
    national_label_en: 'Taza de baño (excusado, sanitario): una tubería que va a dar
      a una barranca o grieta +, río o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-15
    source_category_code: taza_de_bano_excusado_sanitario_una_tuberia_que_va_a_dar_a_una_barranca_grieta_rio_o_mar
    national_label_en: 'Taza de baño (excusado, sanitario): una tubería que va a dar
      a una barranca, grieta, río o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-16
    source_category_code: taza_de_bano_excusado_sanitario_una_tuberia_que_va_a_dar_a_una_barranca_grieta_rio_o_mar_una_tuberia_que_va_a_dar_a_un_rio_lago_o_mar
    national_label_en: 'Taza de baño (excusado, sanitario): una tubería que va a dar
      a una barranca, grieta, río o mar + una tubería que va a dar a un río, lago
      o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-17
    source_category_code: tiene_conexion_de_agua
    national_label_en: tiene conexión de agua
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-18
    source_category_code: tiene_servicio_sanitario_a_una_tuberia_que_va_a_dar_a_una_barranca_o_grietaa_o_rio_lago_o_mar
    national_label_en: 'Tiene servicio sanitario: a una tubería que va a dar a una
      barranca o grietaa o río, lago o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: MEX-SAN-19
    source_category_code: conectado_a_la_red_publica
    national_label_en: Conectado a la red pública
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-20
    source_category_code: drainage_or_sewage_connected_to_the_public_system
    national_label_en: Drainage or sewage connected to the public system
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-21
    source_category_code: excusado_conectado_a_la_red_publica
    national_label_en: Excusado conectado a la red publica
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-22
    source_category_code: excusado_conectado_al_alcantarillado
    national_label_en: Excusado conectado al alcantarillado
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-23
    source_category_code: excusado_retrete_o_sanita_con_descarga_a_la_red_publica
    national_label_en: Excusado, retrete o sanita con descarga a la red publica
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-24
    source_category_code: excusado_letrina_conectado_a_la_red_publica
    national_label_en: 'Excusado/letrina: conectado a la red publica'
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-25
    source_category_code: excusado_retrete_sanitario_letrina_u_hoyo_negro_conectado_a_la_red_publica
    national_label_en: 'Excusado/retrete/sanitario(letrina u hoyo negro): Conectado
      a la red pública'
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-26
    source_category_code: flush_pour_to_piped_sewage_system
    national_label_en: flush/pour to piped sewage system
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-27
    source_category_code: red_publica
    national_label_en: Red publica
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-28
    source_category_code: taza_de_bano_excusado_sanitario_la_red_publica
    national_label_en: 'Taza de baño (excusado, sanitario): la red pública'
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-29
    source_category_code: tiene_servicio_sanitario_a_la_red_publica
    national_label_en: 'Tiene servicio sanitario: a la red publica'
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: MEX-SAN-30
    source_category_code: flush_pour_to_pit_latrine
    national_label_en: flush/pour to pit latrine
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: MEX-SAN-31
    source_category_code: letrina_pozo_negro_hoyo
    national_label_en: Letrina (pozo negro, hoyo)
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: MEX-SAN-32
    source_category_code: conectado_a_una_fosa_septica
    national_label_en: Conectado a una fosa séptica
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-33
    source_category_code: conectado_a_una_fosa_septica_o_tanque_septico_biodigestor
    national_label_en: conectado a una fosa septica o tanque septico (biodigestor)
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-34
    source_category_code: connected_to_a_septic_tank
    national_label_en: Connected to a septic tank
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-35
    source_category_code: excusado_conectado_a_tanque_septico
    national_label_en: Excusado conectado a tanque septico
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-36
    source_category_code: excusado_conectado_a_una_fosa_septica
    national_label_en: Excusado conectado a una fosa septica
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-37
    source_category_code: excusado_retrete_o_sanita_con_descarga_a_fosa_septica
    national_label_en: Excusado, retrete o sanita con descarga a fosa septica
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-38
    source_category_code: excusado_letrina_conectado_a_una_fosa_septica
    national_label_en: 'Excusado/letrina: conectado a una fosa septica'
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-39
    source_category_code: excusado_retrete_sanitario_letrina_u_hoyo_negro_conectado_a_una_fosa_septica_biodigestor
    national_label_en: 'Excusado/retrete/sanitario(letrina u hoyo negro): Conectado
      a una fosa séptica (biodigestor)'
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-40
    source_category_code: flush_pour_to_septic_tank
    national_label_en: flush/pour to septic tank
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-41
    source_category_code: fosa_septica
    national_label_en: Fosa septica
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-42
    source_category_code: taza_de_bano_excusado_sanitario_una_fosa_septica
    national_label_en: 'Taza de baño (excusado, sanitario): una fosa séptica'
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-43
    source_category_code: tiene_servicio_sanitario_una_fosa_septica_o_tanque_septico_biodigestor
    national_label_en: 'Tiene servicio sanitario: una fosa séptica o tanque séptico
      (biodigestor)'
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-SAN-44
    source_category_code: descarga_a_sitio_desconocido_no_esta_seguro_donde_ns_donde
    national_label_en: Descarga a sitio desconocido / no esta seguro donde / NS donde
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: MEX-SAN-45
    source_category_code: excusado_retrete_o_sanita_con_descarga_a_ns
    national_label_en: Excusado, retrete o sanita con descarga a  NS
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: MEX-SAN-46
    source_category_code: excusado_retrete_sanitario_letrina_u_hoyo_negro_no_especificado
    national_label_en: Excusado/retrete/sanitario(letrina u hoyo negro) no especificado
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: MEX-SAN-47
    source_category_code: flush_pour_to_unknown
    national_label_en: flush/pour to unknown
    national_label_local: no sabe donde
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: MEX-SAN-48
    source_category_code: excusado
    national_label_en: Excusado
    national_label_local: Inodoros de arrastre hidráulico
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: MEX-SAN-49
    source_category_code: conectado_a_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_o_un_rio_lago_o_mar
    national_label_en: Conectado a una tubería que va a dar a una barranca o grieta
      o un rio lago o mar
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: MEX-SAN-50
    source_category_code: excusado_letrina_conectado_a_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_o_un_rio_lago_o_mar
    national_label_en: 'Excusado/letrina: Conectado a una tubería que va a dar a una
      barranca o grieta o un rio lago o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: MEX-SAN-51
    source_category_code: taza_de_bano_excusado_sanitario_a_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_o_a_un_rio_lago_o_mar
    national_label_en: 'Taza de bano (excusado, sanitario): a una tuberia que va a
      dar a una barranca o grieta o a un rio lago o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: MEX-SAN-52
    source_category_code: una_tuberia_que_va_a_dar_a_un_rio_lago_o_mar
    national_label_en: Una tubería que va a dar a un río, lago o mar
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: MEX-SAN-53
    source_category_code: una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_rio_lago_etc
    national_label_en: Una tubería que va a dar a una barranca o grieta/rio,lago etc.
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: MEX-SAN-54
    source_category_code: conectado_a_la_red_publica
    national_label_en: Conectado a la red pública
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: MEX-SAN-55
    source_category_code: drainage_to_sewer_system
    national_label_en: DRAINAGE TO SEWER SYSTEM
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: MEX-SAN-56
    source_category_code: excusado_letrina_conectado_a_la_red_publica
    national_label_en: 'Excusado/letrina: Conectado a la red pública'
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: MEX-SAN-57
    source_category_code: flush_to_piped_sewage_system
    national_label_en: Flush to piped sewage system
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: MEX-SAN-58
    source_category_code: la_red_publica
    national_label_en: La red pública
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: MEX-SAN-59
    source_category_code: taza_de_bano_excusado_sanitario_a_red_publica
    national_label_en: 'Taza de bano (excusado, sanitario): a red publica'
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: MEX-SAN-60
    source_category_code: taza_de_bano_excusado_sanitario_no_tiene_drenaje
    national_label_en: 'Taza de bano (excusado, sanitario): no tiene drenaje'
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: MEX-SAN-61
    source_category_code: conecatdo_a_una_fosa_septica
    national_label_en: Conecatdo a una fosa séptica
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: MEX-SAN-62
    source_category_code: drainage_to_septic_tank
    national_label_en: DRAINAGE TO SEPTIC TANK
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: MEX-SAN-63
    source_category_code: excusado_letrina_conectado_a_una_fosa_septica
    national_label_en: 'Excusado/letrina: Conectado a una fosa séptica'
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: MEX-SAN-64
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: MEX-SAN-65
    source_category_code: taza_de_bano_excusado_sanitario_una_fosa_septica_o_tanque_septico_biodigestor
    national_label_en: 'Taza de bano (excusado, sanitario): una fosa septica o tanque
      septico (biodigestor)'
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: MEX-SAN-66
    source_category_code: una_fosa_septica
    national_label_en: Una fosa séptica
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: MEX-SAN-67
    source_category_code: taza_de_bano_excusado_sanitario_no_especificado
    national_label_en: 'Taza de bano (excusado, sanitario): no especificado'
    national_label_local: no sabe donde
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: MEX-SAN-68
    source_category_code: una_tuberia_que_va_a_dar_a_una_barranca_o_grieta
    national_label_en: Una tubería que va a dar a una barranca o grieta
    national_label_local: no sabe donde
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: MEX-SAN-69
    source_category_code: bucket
    national_label_en: bucket
    national_label_local: Letrina de cubeta
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: MEX-SAN-70
    source_category_code: bucket_latrine_excrements_are_manually_removed
    national_label_en: BUCKET LATRINE (EXCREMENTS ARE MANUALLY REMOVED)
    national_label_local: Letrina de cubeta
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: MEX-SAN-71
    source_category_code: bucket_latrine_where_fresh_excreta_are_manually_removed
    national_label_en: Bucket latrine (where fresh excreta are manually removed)
    national_label_local: Letrina de cubeta
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: MEX-SAN-72
    source_category_code: excusado_colgante_letrina_colgante
    national_label_en: Excusado colgante, Letrina colgante
    national_label_local: Letrina colgante
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: MEX-SAN-73
    source_category_code: hanging_toilet_latrine
    national_label_en: hanging toilet/latrine
    national_label_local: Letrina colgante
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: MEX-SAN-74
    source_category_code: hoyo_negro_o_pozo
    national_label_en: Hoyo negro o pozo
    national_label_local: Otro
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: MEX-SAN-75
    source_category_code: hoyo_negro_o_pozo_ciego
    national_label_en: Hoyo negro o pozo ciego
    national_label_local: Otro
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: MEX-SAN-76
    source_category_code: covered_dry_latrine_with_privacy
    national_label_en: Covered dry latrine (with privacy)
    national_label_local: Letrina simple con loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-SAN-77
    source_category_code: letrina_de_fosa_con_losa
    national_label_en: Letrina de fosa con losa
    national_label_local: Letrina simple con loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-SAN-78
    source_category_code: pit_with_slab
    national_label_en: pit with slab
    national_label_local: Letrina simple con loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-SAN-79
    source_category_code: letrina_de_fosa_sin_losa_foso_abierto
    national_label_en: Letrina de fosa sin losa/Foso abierto
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: MEX-SAN-80
    source_category_code: pit_witout_slap_open
    national_label_en: pit witout slap/open
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: MEX-SAN-81
    source_category_code: uncovered_dry_latrine_without_privacy
    national_label_en: Uncovered dry latrine (without privacy)
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: MEX-SAN-82
    source_category_code: excusado_retrete_o_sanita_sin_descarga
    national_label_en: Excusado, retrete o sanita sin descarga
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-83
    source_category_code: excusado_no_tiene_drenaje
    national_label_en: Excusado/ no tiene drenaje
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-84
    source_category_code: excusado_letrina_no_tiene_drenaje
    national_label_en: 'Excusado/letrina: No tiene drenaje'
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-85
    source_category_code: excusado_retrete_sanitario_letrina_u_hoyo_negro_no_tiene_drenaje
    national_label_en: Excusado/retrete/sanitario(letrina u hoyo negro) no tiene drenaje
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-86
    source_category_code: letrina
    national_label_en: Letrina
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-87
    source_category_code: letrina_hoyo_negro_no_tiene_drenaje
    national_label_en: 'Letrina (hoyo negro): no tiene drenaje'
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-88
    source_category_code: letrina_pozo_o_hoyo_no_tiene_drenaje
    national_label_en: 'Letrina (pozo o hoyo): no tiene drenaje'
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-89
    source_category_code: no_se_le_echa_agua
    national_label_en: no se le echa agua
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-90
    source_category_code: no_tiene_drenaje
    national_label_en: No tiene drenaje
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-91
    source_category_code: no_tiene_drenaje_no_tiene_excusado
    national_label_en: No tiene drenaje &  no tiene excusado
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-92
    source_category_code: there_is_no_drainage_system
    national_label_en: There is no drainage system
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-93
    source_category_code: tiene_servicio_sanitario_no_tiene_drenaje
    national_label_en: 'Tiene servicio sanitario: no tiene drenaje'
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-SAN-94
    source_category_code: letrina_de_fosa_mejorada_con_ventilacion
    national_label_en: Letrina de fosa mejorada con ventilacion
    national_label_local: Letrina de pozo mejorada ventilada
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: MEX-SAN-95
    source_category_code: ventilation_improved_pit_latrine
    national_label_en: ventilation improved pit latrine
    national_label_local: Letrina de pozo mejorada ventilada
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: MEX-SAN-96
    source_category_code: pour_flush_latrine
    national_label_en: Pour flush latrine
    national_label_local: Letrinas de arrastre hidráulico
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 85
  - country_entry_id: MEX-SAN-97
    source_category_code: latrine_with_drainage_connected_to_river_lake_gorge
    national_label_en: LATRINE WITH DRAINAGE - Connected to RIVER/LAKE/GORGE
    national_label_local: a drenaje abierto
    jmp_classification: Latrines > Pour flush latrines > to elsewhere
    jmp_id: latrines.pour_flush_latrines.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-SAN-98
    source_category_code: le_echan_agua_con_cubeta
    national_label_en: le echan agua con cubeta
    national_label_local: a drenaje abierto
    jmp_classification: Latrines > Pour flush latrines > to elsewhere
    jmp_id: latrines.pour_flush_latrines.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-SAN-99
    source_category_code: letrina_hoyo_negro_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta
    national_label_en: 'Letrina (hoyo negro): una tubería que va a dar a una barranca
      o grieta'
    national_label_local: a drenaje abierto
    jmp_classification: Latrines > Pour flush latrines > to elsewhere
    jmp_id: latrines.pour_flush_latrines.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-SAN-100
    source_category_code: letrina_hoyo_negro_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_lago_o_mar
    national_label_en: 'Letrina (hoyo negro): una tubería que va a dar a una barranca
      o grieta + lago o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Latrines > Pour flush latrines > to elsewhere
    jmp_id: latrines.pour_flush_latrines.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-SAN-101
    source_category_code: letrina_hoyo_negro_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_una_tuberia_que_va_a_dar_a_un_rio_lago_o_mar
    national_label_en: 'Letrina (hoyo negro): una tubería que va a dar a una barranca
      o grieta + una tubería que va a dar a un río, lago o mar'
    national_label_local: a drenaje abierto
    jmp_classification: Latrines > Pour flush latrines > to elsewhere
    jmp_id: latrines.pour_flush_latrines.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-SAN-102
    source_category_code: letrina_pozo_hoyo_a_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta_o_a_un_rio_lago_o_mar
    national_label_en: Letrina (pozo, hoyo) a una tuberia que va a dar a una barranca
      o grieta o a un rio lago o mar
    national_label_local: a drenaje abierto
    jmp_classification: Latrines > Pour flush latrines > to elsewhere
    jmp_id: latrines.pour_flush_latrines.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-SAN-103
    source_category_code: drenaje
    national_label_en: Drenaje
    national_label_local: al alcantarillado
    jmp_classification: Latrines > Pour flush latrines > to piped sewer system
    jmp_id: latrines.pour_flush_latrines.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: MEX-SAN-104
    source_category_code: latrine_with_drainage_connected_to_grid
    national_label_en: LATRINE WITH DRAINAGE - Connected to GRID
    national_label_local: al alcantarillado
    jmp_classification: Latrines > Pour flush latrines > to piped sewer system
    jmp_id: latrines.pour_flush_latrines.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: MEX-SAN-105
    source_category_code: letrina_hoyo_negro_la_red_publica
    national_label_en: 'Letrina (hoyo negro): la red pública'
    national_label_local: al alcantarillado
    jmp_classification: Latrines > Pour flush latrines > to piped sewer system
    jmp_id: latrines.pour_flush_latrines.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: MEX-SAN-106
    source_category_code: letrina_pozo_o_hoyo_a_red_publica
    national_label_en: 'Letrina (pozo o hoyo): a red publica'
    national_label_local: al alcantarillado
    jmp_classification: Latrines > Pour flush latrines > to piped sewer system
    jmp_id: latrines.pour_flush_latrines.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: MEX-SAN-107
    source_category_code: latrine_without_drainage
    national_label_en: LATRINE WITHOUT DRAINAGE
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Latrines > Pour flush latrines > to pit
    jmp_id: latrines.pour_flush_latrines.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 88
  - country_entry_id: MEX-SAN-108
    source_category_code: fosa_septica
    national_label_en: fosa septica
    national_label_local: a pozo septico
    jmp_classification: Latrines > Pour flush latrines > to septic tank
    jmp_id: latrines.pour_flush_latrines.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-SAN-109
    source_category_code: latrine_with_drainage_connected_to_septic_tank
    national_label_en: LATRINE WITH DRAINAGE - Connected to SEPTIC TANK
    national_label_local: a pozo septico
    jmp_classification: Latrines > Pour flush latrines > to septic tank
    jmp_id: latrines.pour_flush_latrines.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-SAN-110
    source_category_code: letrina_hoyo_negro_una_fosa_septica
    national_label_en: 'Letrina (hoyo negro): una fosa séptica'
    national_label_local: a pozo septico
    jmp_classification: Latrines > Pour flush latrines > to septic tank
    jmp_id: latrines.pour_flush_latrines.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-SAN-111
    source_category_code: letrina_pozo_o_hoyo_una_fosa_septica_o_tanque_septico_biodigestor
    national_label_en: 'Letrina (pozo o hoyo): una fosa septica o tanque septico (biodigestor)'
    national_label_local: a pozo septico
    jmp_classification: Latrines > Pour flush latrines > to septic tank
    jmp_id: latrines.pour_flush_latrines.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-SAN-112
    source_category_code: latrine_with_drainage_connected_to_don_t_know
    national_label_en: LATRINE WITH DRAINAGE - Connected to DON'T KNOW
    national_label_local: no sabe donde
    jmp_classification: Latrines > Pour flush latrines > to unknown place/ not sure/DK
    jmp_id: latrines.pour_flush_latrines.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 89
  - country_entry_id: MEX-SAN-113
    source_category_code: letrina_pozo_o_hoyo_no_especificado
    national_label_en: 'Letrina (pozo o hoyo): no especificado'
    national_label_local: no sabe donde
    jmp_classification: Latrines > Pour flush latrines > to unknown place/ not sure/DK
    jmp_id: latrines.pour_flush_latrines.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 89
  - country_entry_id: MEX-SAN-114
    source_category_code: no_dispone_de_servicio_sanitario
    national_label_en: No dispone de servicio sanitario
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-115
    source_category_code: no_facilities_bush_field
    national_label_en: no facilities (bush, field)
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-116
    source_category_code: no_facilities_open_defecation
    national_label_en: No facilities (open defecation)
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-117
    source_category_code: no_hay_instalacion_sanitaria_va_al_monte_campo
    national_label_en: No hay instalacion sanitaria, va al monte, campo
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-118
    source_category_code: no_sanitation_facilities_defecation_in_the_open_air
    national_label_en: NO SANITATION FACILITIES (DEFECATION IN THE OPEN AIR)
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-119
    source_category_code: no_tiene
    national_label_en: No tiene
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-120
    source_category_code: no_tiene_el_servicio_sanitario
    national_label_en: No tiene el servicio sanitario
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-121
    source_category_code: no_tiene_excusado
    national_label_en: No tiene excusado
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-122
    source_category_code: no_tiene_excusado_o_letrina
    national_label_en: No tiene excusado o letrina
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-123
    source_category_code: no_tiene_excusado_retrete_sanitario_letrina_u_hoyo_negro
    national_label_en: No tiene excusado, retrete, sanitario, letrina u hoyo negro
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-124
    source_category_code: no_tiene_excusado_letrina
    national_label_en: No tiene excusado/letrina
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-125
    source_category_code: no_tiene_excusado_retrete_sanitario_letrina_u_hoyo_negro
    national_label_en: No tiene excusado/retrete/sanitario(letrina u hoyo negro)
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-126
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
  - country_entry_id: MEX-SAN-127
    source_category_code: no_tiene_taza_de_bano_ni_letrina
    national_label_en: No tiene taza de baño ni letrina
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-128
    source_category_code: none
    national_label_en: None
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: MEX-SAN-129
    source_category_code: conectado_a_una_tuberia_que_va_dar_a_una_barranca_o_grieta
    national_label_en: conectado a una tuberia que va dar a una barranca o grieta
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: MEX-SAN-130
    source_category_code: excusado_conectado_a_una_tuberia_que_va_dar_a_una_barranca_o_grieta
    national_label_en: Excusado conectado a una tuberia que va dar a una barranca
      o grieta
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: MEX-SAN-131
    source_category_code: excusado_retrete_o_sanita_con_descarga_a_una_tuberia_que_va_a_dar_a_una_barranca_o_grieta
    national_label_en: Excusado, retrete o sanita con descarga a una tubería que va
      a dar a una barranca o grieta
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: MEX-SAN-132
    source_category_code: no_tiene_drenaje
    national_label_en: No tiene drenaje
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: MEX-SAN-133
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
  - country_entry_id: MEX-SAN-134
    source_category_code: other_specify
    national_label_en: other, specify
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: MEX-SAN-135
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
  - country_entry_id: MEX-SAN-136
    source_category_code: otros
    national_label_en: Otros
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: MEX-SAN-137
    source_category_code: taza_de_bano_excusado_sanitario_no_tiene_drenaje
    national_label_en: 'Taza de baño (excusado, sanitario): no tiene drenaje'
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: MEX-SAN-138
    source_category_code: albaal
    national_label_en: albaal
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MEX_Mexico_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: MEX-WAS-01
    source_category_code: agua_de_pipa
    national_label_en: Agua de pipa
    national_label_local: Todos los manantiales
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: MEX-WAS-02
    source_category_code: de_una_pipa
    national_label_en: De una pipa
    national_label_local: Todos los manantiales
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: MEX-WAS-03
    source_category_code: pozo
    national_label_en: Pozo
    national_label_local: Todos los pozos
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 54
  - country_entry_id: MEX-WAS-04
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
  - country_entry_id: MEX-WAS-05
    source_category_code: protected_spring
    national_label_en: protected spring
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: MEX-WAS-06
    source_category_code: protected_underground_well_or_protected_spring
    national_label_en: PROTECTED UNDERGROUND WELL OR PROTECTED SPRING
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: MEX-WAS-07
    source_category_code: pozo_protegido
    national_label_en: Pozo protegido
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: MEX-WAS-08
    source_category_code: protected_dug_well
    national_label_en: protected dug well
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: MEX-WAS-09
    source_category_code: protected_well_or_hole_drilled_in_the_ground
    national_label_en: PROTECTED WELL OR HOLE DRILLED IN THE GROUND
    national_label_local: Pozos protegidos
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: MEX-WAS-10
    source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: Pozos o manantiales protegidos
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: yes
    shared_flag: no
    source_row: 46
  - country_entry_id: MEX-WAS-11
    source_category_code: agua_de_un_pozo
    national_label_en: Agua de un pozo
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-WAS-12
    source_category_code: de_un_pozo
    national_label_en: De un pozo
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-WAS-13
    source_category_code: la_sacan_y_acarrean_de_un_pozo
    national_label_en: la sacan y acarrean de un pozo
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-WAS-14
    source_category_code: pozo
    national_label_en: Pozo
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-WAS-15
    source_category_code: sacan_o_acarrean_de_un_pozo
    national_label_en: sacan o acarrean de un pozo
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-WAS-16
    source_category_code: tiene_agua_de_un_pozo
    national_label_en: Tiene agua de un pozo
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-WAS-17
    source_category_code: un_pozo
    national_label_en: un pozo
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: MEX-WAS-18
    source_category_code: pozo_con_tuberia
    national_label_en: Pozo con tuberia
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: MEX-WAS-19
    source_category_code: protected_tube_well_or_bore_hole
    national_label_en: Protected tube well or bore hole
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: MEX-WAS-20
    source_category_code: tubewell_borehole
    national_label_en: tubewell/borehole
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: MEX-WAS-21
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
  - country_entry_id: MEX-WAS-22
    source_category_code: unprotected_spring
    national_label_en: unprotected spring
    national_label_local: Manantiales protegidos
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: MEX-WAS-23
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
  - country_entry_id: MEX-WAS-24
    source_category_code: unprotected_dug_well
    national_label_en: unprotected dug well
    national_label_local: Pozos non protegidos
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: MEX-WAS-25
    source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: Pozos o manantiales non protegidos
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 50
  - country_entry_id: MEX-WAS-26
    source_category_code: unprotected_underground_well_or_unprotected_spring
    national_label_en: UNPROTECTED UNDERGROUND WELL OR UNPROTECTED SPRING
    national_label_local: Pozos o manantiales non protegidos
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 50
  - country_entry_id: MEX-WAS-27
    source_category_code: carreta_con_tanque_tambor_pequeno
    national_label_en: Carreta con tanque / tambor pequeno
    national_label_local: Carro con tanque / tambor pequeño
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: MEX-WAS-28
    source_category_code: small_scale_vendor
    national_label_en: small scale vendor
    national_label_local: Carro con tanque / tambor pequeño
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: MEX-WAS-29
    source_category_code: de_pipa_o_entubada_de_llave_publica_o_hidrante_o_entubada_fuera_de_la_vivienda
    national_label_en: De pipa o entubada de llave publica o hidrante o entubada fuera
      de la vivienda
    national_label_local: Otro
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: MEX-WAS-30
    source_category_code: small_scale_vendor
    national_label_en: small scale vendor
    national_label_local: Otro
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: MEX-WAS-31
    source_category_code: acarreo
    national_label_en: Acarreo
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-32
    source_category_code: agua_de_pipa
    national_label_en: Agua de pipa
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-33
    source_category_code: agua_de_una_pipa
    national_label_en: Agua de una pipa
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-34
    source_category_code: carro_tanque_camion_cisterna
    national_label_en: Carro-tanque / camion cisterna
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-35
    source_category_code: la_trae_una_pipa
    national_label_en: la trae una pipa
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-36
    source_category_code: pipa
    national_label_en: Pipa
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-37
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker-truck, vendor
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-38
    source_category_code: tanker_truck_lorry
    national_label_en: tanker-truck/lorry
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-39
    source_category_code: tiene_agua_de_una_pipa
    national_label_en: Tiene agua de una pipa
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-40
    source_category_code: trae_una_pipa
    national_label_en: Trae una pipa
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-41
    source_category_code: una_pipa
    national_label_en: una pipa
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-42
    source_category_code: water_from_a_tanker_truck
    national_label_en: WATER FROM A TANKER TRUCK
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-43
    source_category_code: water_from_a_truck
    national_label_en: Water from a truck
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: MEX-WAS-44
    source_category_code: agua_de_pozo_rio_lago_arroyo_u_otra
    national_label_en: Agua de pozo, río, lago, arroyo u otra
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-45
    source_category_code: agua_de_un_pozo_rio_arroyo_lago_u_otro
    national_label_en: Agua de un pozo, río, arroyo, lago u otro
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-46
    source_category_code: agua_de_un_pozo_rio_lago_arroyo_u_otra
    national_label_en: Agua de un pozo, rio, lago arroyo u otra
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-47
    source_category_code: agua_de_un_pozo_rio_lago_arroyo_u_otra
    national_label_en: agua de un pozo, rio, lago, arroyo u otra
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-48
    source_category_code: agua_entubada_no_tiene
    national_label_en: Agua entubada No tiene
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-49
    source_category_code: no_tiene_agua
    national_label_en: No tiene agua
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-50
    source_category_code: no_tiene_agua_entubada
    national_label_en: no tiene agua entubada .
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-51
    source_category_code: no_tienen_agua_entubada_en_la_vivienda
    national_label_en: No tienen agua entubada en la vivienda
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-52
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
  - country_entry_id: MEX-WAS-53
    source_category_code: other_specify
    national_label_en: other, specify
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-54
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
  - country_entry_id: MEX-WAS-55
    source_category_code: otra_no_entubada_pipa_pozo_rio_otro
    national_label_en: Otra no entubada (pipa, pozo, río, otro)
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-56
    source_category_code: otrps
    national_label_en: Otrps
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-57
    source_category_code: water_from_a_well_river_lake_gully_or_other
    national_label_en: Water from a well, river, lake, gully or other
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: MEX-WAS-58
    source_category_code: acarreo
    national_label_en: Acarreo
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-WAS-59
    source_category_code: agua_de_un_pozo_rio_lago_arroyo_u_otra
    national_label_en: Agua de un pozo, río, lago, arroyo u otra
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-WAS-60
    source_category_code: rio_arroyo_lago_o_manantial
    national_label_en: Rio, arroyo, lago o manantial
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: MEX-WAS-61
    source_category_code: agua_embotellada_envasada
    national_label_en: Agua embotellada/envasada
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-WAS-62
    source_category_code: bottled_water
    national_label_en: bottled water
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-WAS-63
    source_category_code: bottled_water_with_other_improved
    national_label_en: Bottled water - with other improved
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-WAS-64
    source_category_code: garrafon_with_other_improved
    national_label_en: Garrafon - with other improved
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-WAS-65
    source_category_code: garrafon_o_botella
    national_label_en: Garrafon o botella
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: MEX-WAS-66
    source_category_code: bottled_water_without_other_improved
    national_label_en: Bottled water - without other improved
    national_label_local: Agua en bolsita
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: MEX-WAS-67
    source_category_code: garrafon_without_other_imprvoed
    national_label_en: Garrafon - without other imprvoed
    national_label_local: Agua en bolsita
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: MEX-WAS-68
    source_category_code: acceso_al_agua_a_traves_de_captadores_de_agua_de_lluvia
    national_label_en: Acceso al agua, a través de captadores de agua de lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-WAS-69
    source_category_code: captadores_de_agua_de_lluvia
    national_label_en: captadores de agua de lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-WAS-70
    source_category_code: captan_de_la_lluvia
    national_label_en: Captan de la lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-WAS-71
    source_category_code: la_captan_de_la_lluvia
    national_label_en: la captan de la lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-WAS-72
    source_category_code: rainwater_in_tank_or_cistern
    national_label_en: RAINWATER (IN TANK OR CISTERN)
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-WAS-73
    source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-WAS-74
    source_category_code: rainwater_collection
    national_label_en: rainwater collection
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-WAS-75
    source_category_code: recogen_agua_de_lluvia
    national_label_en: Recogen agua de lluvia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: MEX-WAS-76
    source_category_code: agua_de_rio_arroyo_lago_u_otro
    national_label_en: Agua de río, arroyo, lago u otro
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-77
    source_category_code: agua_de_superficie_rio_arroyo_represa_lago_estanque_canal_canal_de_irrigacion
    national_label_en: Agua de superficie (rio, arroyo, represa, lago, estanque, canal,
      canal de irrigacion)
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-78
    source_category_code: agua_de_un_rio_arroyo_lago_u_otro
    national_label_en: Agua de un río, arroyo, lago u otro
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-79
    source_category_code: de_un_rio_arroyo_lago_u_otro
    national_label_en: De un río, arroyo, lago u otro
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-80
    source_category_code: la_acarrean_de_un_ra_o_arroyo_o_lago
    national_label_en: la acarrean de un rÃ­o, arroyo o lago
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-81
    source_category_code: rio_arroyo_o_lago
    national_label_en: Rio arroyo o lago
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-82
    source_category_code: rio_arroyo_lago_u_otro
    national_label_en: Rio, arroyo, lago u otro
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-83
    source_category_code: surface_water_river_lake_etc
    national_label_en: surface water (river, lake, etc)
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-84
    source_category_code: tiene_agua_de_un_rio_arroyo_lago_u_otro
    national_label_en: Tiene agua de un rio, arroyo, lago u otro
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-85
    source_category_code: un_rio_arroyo_lago_u_otro
    national_label_en: un río, arroyo, lago u otro
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-86
    source_category_code: water_taken_directly_from_pond_water_or_stream
    national_label_en: Water taken directly from pond-water or stream
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: MEX-WAS-87
    source_category_code: water_collected_directly_from_a_pond_or_creek
    national_label_en: WATER COLLECTED DIRECTLY FROM A POND OR CREEK
    national_label_local: Estanque
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - country_entry_id: MEX-WAS-88
    source_category_code: agua_de_otra_vivienda
    national_label_en: Agua de otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-89
    source_category_code: agua_entubada_que_acarrea_de_otra_vivienda
    national_label_en: Agua entubada que acarrea de otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-90
    source_category_code: agua_entubada_que_acarrean_de_otra_vivienda
    national_label_en: Agua entubada que acarrean de otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-91
    source_category_code: de_la_red_publica_de_otra_vivienda
    national_label_en: De la red pública de otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-92
    source_category_code: la_traen_de_otra_vivienda
    national_label_en: la traen de otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-93
    source_category_code: otra_agua_entubada
    national_label_en: Otra agua entubada
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-94
    source_category_code: otra_vivienda
    national_label_en: otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-95
    source_category_code: piped_water_that_is_transported_from_another_housing_unit
    national_label_en: Piped water that is transported from another housing unit
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-96
    source_category_code: piped_water_with_a_connection_in_the_house_or_lawn_dk_if_reached_interior_of_the_house
    national_label_en: PIPED WATER WITH A CONNECTION IN THE HOUSE OR LAWN - DK if
      reached interior of the house.
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-97
    source_category_code: red_publica_de_otra_vivienda
    national_label_en: Red publica de otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-98
    source_category_code: tiene_agua_de_la_red_publica_de_otra_vivienda
    national_label_en: Tiene agua de la red publica de otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-99
    source_category_code: tiene_agua_de_otra_vivienda
    national_label_en: Tiene agua  de otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-100
    source_category_code: traen_de_otra_vivienda
    national_label_en: traen de otra vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-101
    source_category_code: tubera_a_del_vecino
    national_label_en: TuberÃ­a del vecino
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: MEX-WAS-102
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Conexiones domiciliarias
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: MEX-WAS-103
    source_category_code: agua_de_la_llave_dentro_de_la_vivienda
    national_label_en: Agua de la llave dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-104
    source_category_code: agua_entubada_dentro_de_la_vivienda
    national_label_en: Agua entubada dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-105
    source_category_code: agua_entubada_si_dentro_de_la_vivienda
    national_label_en: Agua entubada Si, dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-106
    source_category_code: agua_entubada_dentro_de_la_vivienda
    national_label_en: 'agua entubada: dentro de la vivienda'
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-107
    source_category_code: agua_entubada_dentro_de_la_vivienda
    national_label_en: 'agua entubada: dentro de la vivienda .'
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-108
    source_category_code: de_la_red_publica
    national_label_en: De la red pública
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-109
    source_category_code: de_la_red_publica_dentro_de_la_vivienda
    national_label_en: de la red pública dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-110
    source_category_code: piped_private
    national_label_en: piped private
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-111
    source_category_code: piped_water_inside_the_housing_unit
    national_label_en: Piped water inside the housing unit
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-112
    source_category_code: piped_water_with_a_connection_in_the_house_or_lawn_reaches_interior_of_the_house
    national_label_en: PIPED WATER WITH A CONNECTION IN THE HOUSE OR LAWN - reaches
      interior of the house.
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-113
    source_category_code: red_publica_dentro_de_la_vivienda
    national_label_en: Red publica dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-114
    source_category_code: tiene_agua_de_la_red_publica_dentro_de_la_vivienda
    national_label_en: Tiene agua de la red pública dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-115
    source_category_code: tuberia_dentro_de_la_vivienda
    national_label_en: Tuberia dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: MEX-WAS-116
    source_category_code: agua_de_la_llave_fuera_de_la_vivienda
    national_label_en: Agua de la llave fuera de la vivienda
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-117
    source_category_code: agua_entubada_en_el_patio_o_terreno
    national_label_en: Agua entubada en el patio o terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-118
    source_category_code: agua_entubada_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: Agua entubada fuera de la vivienda, pero dentro del terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-119
    source_category_code: agua_entubada_solo_en_el_patio_o_terreno
    national_label_en: Agua entubada solo en el patio o terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-120
    source_category_code: agua_entubada_solo_en_el_terreno
    national_label_en: Agua entubada solo en el terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-121
    source_category_code: agua_entubada_solo_en_el_patio_o_terreno
    national_label_en: 'agua entubada: solo en el patio o terreno'
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-122
    source_category_code: agua_entubada_solo_en_el_terreno
    national_label_en: 'agua entubada: solo en el terreno .'
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-123
    source_category_code: de_la_red_publica_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: De la red pública fuera de la vivienda pero dentro del terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-124
    source_category_code: piped_to_yard_plot
    national_label_en: piped to yard/plot
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-125
    source_category_code: piped_water_outside_the_housing_unit_but_on_the_property
    national_label_en: Piped water outside the housing unit but on the property
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-126
    source_category_code: piped_water_with_a_connection_in_the_house_or_lawn_not_reach_interior_of_the_house
    national_label_en: PIPED WATER WITH A CONNECTION IN THE HOUSE OR LAWN - Not reach
      interior of the house.
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-127
    source_category_code: red_publica_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: red pública fuera de la vivienda, pero dentro del terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-128
    source_category_code: tiene_agua_de_la_red_publica_fuera_de_la_vivienda_pero_dentro_del_terreno
    national_label_en: Tiene agua de la red pública fuera de la vivienda, pero dentro
      del terreno
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-129
    source_category_code: tuberia_dentro_del_terreno_patio_o_lote
    national_label_en: Tuberia dentro del terreno, patio o lote
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: MEX-WAS-130
    source_category_code: acarrean_de_una_toma_o_llave_comunitaria
    national_label_en: acarrean de una toma o llave comunitaria
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-131
    source_category_code: agua_de_pipa
    national_label_en: Agua de pipa
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-132
    source_category_code: agua_entubada_de_llave_publica_o_hidrante
    national_label_en: agua entubada de llave publica (o hidrante)
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-133
    source_category_code: agua_entubada_de_llave_publica_o_hidrante
    national_label_en: Agua entubada de llave pública(o hidrante)
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-134
    source_category_code: agua_entubada_si_fuera_de_la_vivienda
    national_label_en: Agua entubada Si, fuera de la vivienda
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-135
    source_category_code: de_una_llave_publica_o_hidratante
    national_label_en: de una llave pública (o hidratante)
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-136
    source_category_code: de_una_llave_publica_o_hidrante
    national_label_en: De una llave pública o hidrante
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-137
    source_category_code: la_acarrean_de_una_toma_o_llave_comunitaria
    national_label_en: la acarrean de una toma o llave comunitaria
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-138
    source_category_code: llave_comunitaria
    national_label_en: Llave comunitaria
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-139
    source_category_code: llave_publica_o_hidrante
    national_label_en: Llave publica o hidrante
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-140
    source_category_code: llave_grifo_paoblico
    national_label_en: Llave/grifo pÃºblico
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-141
    source_category_code: piped_water_from_a_public_tap_or_hydrant
    national_label_en: Piped water from a public tap (or hydrant)
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-142
    source_category_code: public_standpipe
    national_label_en: Public standpipe
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-143
    source_category_code: public_tap_standpipe
    national_label_en: public tap/standpipe
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-144
    source_category_code: tiene_agua_de_una_llave_publica_o_hidrante
    national_label_en: Tiene agua de una llave pública o hidrante
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: MEX-WAS-145
    source_category_code: vertical_public_pipe
    national_label_en: VERTICAL PUBLIC PIPE
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_MEX_Mexico_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

