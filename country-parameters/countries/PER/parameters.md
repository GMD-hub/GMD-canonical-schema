---
country_id: CTY-PER
country_name: Peru
iso3: PER
schema_version: '0.1'
status: draft
parameters:
- parameter_id: PARAM-EDU-YEARS-BY-LEVEL
  effective_from: 1980
  effective_to: 1999
  value:
    primary: 6
    lower_secondary: 3
    upper_secondary: 2
  provenance:
    source: PLACEHOLDER, NOT VERIFIED. Must be confirmed against the UNESCO ISCED
      mapping and national curriculum documentation before any use in production.
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-EDU-YEARS-BY-LEVEL
  effective_from: 2000
  effective_to: ~
  value:
    primary: 7
    lower_secondary: 3
    upper_secondary: 2
  provenance:
    source: PLACEHOLDER, NOT VERIFIED.
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-DEM-MIN-MARRIAGE-AGE
  effective_from: ~
  effective_to: ~
  value: 18
  provenance:
    source: PLACEHOLDER, NOT VERIFIED. Must be confirmed against national legislation.
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: PER-EDU-01
    national_label_en: 'Early childhood education: cycle I'
    national_label_local: 'Educación Inicial: Ciclo I'
    entry_age: 0
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: PER-EDU-02
    national_label_en: 'Early childhood education: cycle II'
    national_label_local: 'Educación Inicial: Ciclo II'
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 8
  - country_entry_id: PER-EDU-03
    national_label_en: Primary education
    national_label_local: Educación Primaria
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
  - country_entry_id: PER-EDU-04
    national_label_en: Alternative basic education - Initial and intermediate cycles
    national_label_local: Educación Básica Alternativa-Ciclos Inicial e Intermedio
    entry_age: 14
    duration_years: 5
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 10
  - country_entry_id: PER-EDU-05
    national_label_en: Secondary education, Grades 1 to 3
    national_label_local: Educación Secundaria. Del 1ero. al 3er. grados.
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
  - country_entry_id: PER-EDU-06
    national_label_en: Alternative basic education - Advanced cycle (grades 1 and
      2)
    national_label_local: Educación Básica Alternativa-Ciclo Avanzado. Grados 1er.
      y 2o.
    entry_age: 19
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 12
  - country_entry_id: PER-EDU-07
    national_label_en: Technical productive education - Middle cycle
    national_label_local: Educación Técnico Productiva-Ciclo Medio
    entry_age: 14
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 13
  - country_entry_id: PER-EDU-08
    national_label_en: Alternative basic education - Advanced cycle (grades 3 and
      4)
    national_label_local: Educación Básica Alternativa-Ciclo Avanzado. Grados 3er.
      y 4o.
    entry_age: 21
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
  - country_entry_id: PER-EDU-09
    national_label_en: Secondary education. Grades 4 to 5.
    national_label_local: Educación Secundaria. Del 4to. al 5to. grados.
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
  - country_entry_id: PER-EDU-10
    national_label_en: Non-university higher education (technical training)
    national_label_local: Educación Superior No Universitaria (Técnica)
    entry_age: 17
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: PER-EDU-11
    national_label_en: Non-university higher technological education
    national_label_local: Educación Superior Tecnológica No Universitaria
    entry_age: 17
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: PER-EDU-12
    national_label_en: Non-university higher education; pedagogical and artistic training
    national_label_local: Educación Superior No Universitaria Pedagógica y Artística
    entry_age: 17
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - country_entry_id: PER-EDU-13
    national_label_en: University higher education
    national_label_local: Pregrado universitario
    entry_age: 17
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  - country_entry_id: PER-EDU-14
    national_label_en: Postgraduate
    national_label_local: Diplomado
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
  - country_entry_id: PER-EDU-15
    national_label_en: Bachelor in Law
    national_label_local: Pregrado en Derecho
    entry_age: 17
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
  - country_entry_id: PER-EDU-16
    national_label_en: Bachelor in Medicine
    national_label_local: Pregrado en Medicina
    entry_age: 17
    duration_years: 7
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
  - country_entry_id: PER-EDU-17
    national_label_en: Second Professsional Specialization
    national_label_local: Segunda Especialidad Profesional
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
  - country_entry_id: PER-EDU-18
    national_label_en: Master
    national_label_local: Maestría
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
  - country_entry_id: PER-EDU-19
    national_label_en: Doctorate
    national_label_local: Doctorado
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Peru.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: PER-SUBNAT-01
    survey_labels: 1 - Amazonas | 1-Amazonas
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2328
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2328
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2328'
    geo_nvar: ADM1_NAME
    geo_name: Amazonas
    source_row: 11285
  - country_entry_id: PER-SUBNAT-02
    survey_labels: 10 - Huanuco | 10-Huanuco
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2337
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2337
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2337'
    geo_nvar: ADM1_NAME
    geo_name: Huánuco
    source_row: 11286
  - country_entry_id: PER-SUBNAT-03
    survey_labels: 11 - Ica | 11-Ica
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2338
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2338
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2338'
    geo_nvar: ADM1_NAME
    geo_name: Ica
    source_row: 11287
  - country_entry_id: PER-SUBNAT-04
    survey_labels: 12 - Junin | 12-Junin
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2339
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2339
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2339'
    geo_nvar: ADM1_NAME
    geo_name: Junín
    source_row: 11288
  - country_entry_id: PER-SUBNAT-05
    survey_labels: 13 - La Libertad | 13-La Libertad
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2340
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2340
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2340'
    geo_nvar: ADM1_NAME
    geo_name: La Libertad
    source_row: 11289
  - country_entry_id: PER-SUBNAT-06
    survey_labels: 14 - Lambayeque | 14-Lambayeque
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2341
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2341
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2341'
    geo_nvar: ADM1_NAME
    geo_name: Lambayeque
    source_row: 11290
  - country_entry_id: PER-SUBNAT-07
    survey_labels: 15 - Lima | 15-Lima
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2342
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2342
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2342'
    geo_nvar: ADM1_NAME
    geo_name: Lima
    source_row: 11291
  - country_entry_id: PER-SUBNAT-08
    survey_labels: 16 - Loreto | 16-Loreto
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2343
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2343
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2343'
    geo_nvar: ADM1_NAME
    geo_name: Loreto
    source_row: 11292
  - country_entry_id: PER-SUBNAT-09
    survey_labels: 17 - Madre de Dios | 17-Madre de Dios
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2344
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2344
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2344'
    geo_nvar: ADM1_NAME
    geo_name: Madre de Dios
    source_row: 11293
  - country_entry_id: PER-SUBNAT-10
    survey_labels: 18 - Moquegua | 18-Moquegua
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2345
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2345
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2345'
    geo_nvar: ADM1_NAME
    geo_name: Moquegua
    source_row: 11294
  - country_entry_id: PER-SUBNAT-11
    survey_labels: 19 - Pasco | 19-Pasco
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2346
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2346
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2346'
    geo_nvar: ADM1_NAME
    geo_name: Pasco
    source_row: 11295
  - country_entry_id: PER-SUBNAT-12
    survey_labels: 2 - Ancash | 2-Ancash
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2329
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2329
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2329'
    geo_nvar: ADM1_NAME
    geo_name: Ancash
    source_row: 11296
  - country_entry_id: PER-SUBNAT-13
    survey_labels: 20 - Piura | 20-Piura
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2347
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2347
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2347'
    geo_nvar: ADM1_NAME
    geo_name: Piura
    source_row: 11297
  - country_entry_id: PER-SUBNAT-14
    survey_labels: 21 - Puno | 21-Puno
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2348
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2348
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2348'
    geo_nvar: ADM1_NAME
    geo_name: Puno
    source_row: 11298
  - country_entry_id: PER-SUBNAT-15
    survey_labels: 22 - San Mart�n | 22-San Mart�n
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2349
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2349
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2349'
    geo_nvar: ADM1_NAME
    geo_name: San Martín
    source_row: 11299
  - country_entry_id: PER-SUBNAT-16
    survey_labels: 23 - Tacna | 23-Tacna
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2350
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2350
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2350'
    geo_nvar: ADM1_NAME
    geo_name: Tacna
    source_row: 11300
  - country_entry_id: PER-SUBNAT-17
    survey_labels: 24 - Tumbes | 24-Tumbes
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2351
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2351
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2351'
    geo_nvar: ADM1_NAME
    geo_name: Tumbes
    source_row: 11301
  - country_entry_id: PER-SUBNAT-18
    survey_labels: 25 - Ucayali | 25-Ucayali
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2352
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2352
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2352'
    geo_nvar: ADM1_NAME
    geo_name: Ucayali
    source_row: 11302
  - country_entry_id: PER-SUBNAT-19
    survey_labels: 3 - Apurimac | 3-Apurimac
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2330
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2330
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2330'
    geo_nvar: ADM1_NAME
    geo_name: Apurímac
    source_row: 11303
  - country_entry_id: PER-SUBNAT-20
    survey_labels: 4 - Arequipa | 4-Arequipa
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2331
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2331
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2331'
    geo_nvar: ADM1_NAME
    geo_name: Arequipa
    source_row: 11304
  - country_entry_id: PER-SUBNAT-21
    survey_labels: 5 - Ayacucho | 5-Ayacucho
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2332
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2332
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2332'
    geo_nvar: ADM1_NAME
    geo_name: Ayacucho
    source_row: 11305
  - country_entry_id: PER-SUBNAT-22
    survey_labels: 6 - Cajamarca | 6-Cajamarca
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2333
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2333
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2333'
    geo_nvar: ADM1_NAME
    geo_name: Cajamarca
    source_row: 11306
  - country_entry_id: PER-SUBNAT-23
    survey_labels: 7 - Callao | 7-Callao
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2334
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2334
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2334'
    geo_nvar: ADM1_NAME
    geo_name: Callao
    source_row: 11307
  - country_entry_id: PER-SUBNAT-24
    survey_labels: 8 - Cuzco | 8-Cuzco
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2335
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2335
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2335'
    geo_nvar: ADM1_NAME
    geo_name: Cusco
    source_row: 11308
  - country_entry_id: PER-SUBNAT-25
    survey_labels: 9 - Huancavelica | 9-Huancavelica
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: PER_2015_GAUL1_2336
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: PER_2015_GAUL1_2336
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2336'
    geo_nvar: ADM1_NAME
    geo_name: Huancavelica
    source_row: 11309
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
  - country_entry_id: PER-SAN-01
    source_category_code: a_rio_acequi_etc
    national_label_en: A río, acequi, etc.
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: PER-SAN-02
    source_category_code: rio_o_canal
    national_label_en: Río o canal
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: PER-SAN-03
    source_category_code: rio_acequia_o_canal
    national_label_en: Río, acequia o canal
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: PER-SAN-04
    source_category_code: rio_acequia_canal
    national_label_en: Rio, acequia, canal
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: PER-SAN-05
    source_category_code: rio_acequia_canal_o_similar
    national_label_en: Río, acequia, canal o similar
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: PER-SAN-06
    source_category_code: r_o_acequia_o_canal
    national_label_en: R¡o, acequia o canal
    national_label_local: a drenaje abierto
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: PER-SAN-07
    source_category_code: conectado_a_red_publica_de_desague
    national_label_en: Conectado a red pública de desague
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: PER-SAN-08
    source_category_code: conectado_a_red_publica_de_desague_dentro_de_la_vivienda_fuera_de_la_vivienda_pero_dentro_del_edificio
    national_label_en: Conectado a red pública de desague ( Dentro de la vivienda
      + Fuera de la vivienda, pero dentro del edificio )
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: PER-SAN-09
    source_category_code: red_publica
    national_label_en: Red pública
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: PER-SAN-10
    source_category_code: red_publica_de_desague_dentro_de_la_vivienda_de_desague_fuera_de_la_vivienda_pero_dentro_de_la_edificacion
    national_label_en: Red pública (de desagüe dentro de la vivienda + de desagüe
      fuera de la vivienda pero dentro de la edificación)
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: PER-SAN-11
    source_category_code: red_publica_de_desague_dentro_de_la_vivienda_de_desague_fuera_de_la_vivienda_pero_dentro_del_edificio
    national_label_en: Red pública (de desagüe dentro de la vivienda + de desagüe
      fuera de la vivienda pero dentro del edificio)
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: PER-SAN-12
    source_category_code: red_publica_dentro_o_fuera_de_la_vivienda
    national_label_en: Red pública dentro o fuera de la vivienda
    national_label_local: al alcantarillado
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: PER-SAN-13
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
  - country_entry_id: PER-SAN-14
    source_category_code: pozo_septico_con_o_sin_observacion_directa
    national_label_en: Pozo séptico (con o sin observacion directa)
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: PER-SAN-15
    source_category_code: pozo_septico_tanque_septico
    national_label_en: Pozo septico / tanque septico
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: PER-SAN-16
    source_category_code: pozo_septico_tanque_septico_o_biodigesto
    national_label_en: Pozo séptico, tanque séptico o biodigesto
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: PER-SAN-17
    source_category_code: pozo_septico_tanque_septico_o_biodigesto_con_o_sin_observacion_directa
    national_label_en: Pozo séptico, tanque séptico o biodigesto (con o sin observacion
      directa)
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: PER-SAN-18
    source_category_code: pozo_septico_tanque_septico_o_biodigestor
    national_label_en: Pozo séptico, tanque septico o biodigestor
    national_label_local: a pozo septico
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: PER-SAN-19
    source_category_code: inodoro_exclusivo
    national_label_en: Inodoro exclusivo
    national_label_local: Inodoros de arrastre hidráulico (privado)
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: PER-SAN-20
    source_category_code: private_toilet
    national_label_en: Private toilet
    national_label_local: Inodoros de arrastre hidráulico (privado)
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: PER-SAN-21
    source_category_code: domestic_connection_to_system
    national_label_en: Domestic connection to system
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - country_entry_id: PER-SAN-22
    source_category_code: public_network_connection_inside_house
    national_label_en: PUBLIC NETWORK CONNECTION INSIDE HOUSE
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - country_entry_id: PER-SAN-23
    source_category_code: inodoro_fuera_la_vivienda
    national_label_en: Inodoro fuera la vivienda
    national_label_local: no sabe donde
    jmp_classification: Flush/toilets > Private flush/toilet > to unknown place/ not
      sure/DK
    jmp_id: flush_toilets.private_flush_toilet.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 76
  - country_entry_id: PER-SAN-24
    source_category_code: inodoro_comun
    national_label_en: Inodoro comun
    national_label_local: Inodoros de arrastre hidráulico (publico)
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: PER-SAN-25
    source_category_code: shared_toilet
    national_label_en: Shared toilet
    national_label_local: Inodoros de arrastre hidráulico (publico)
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: PER-SAN-26
    source_category_code: public_network_connection_outside_house
    national_label_en: PUBLIC NETWORK CONNECTION OUTSIDE HOUSE
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - country_entry_id: PER-SAN-27
    source_category_code: water_closet_excusado
    national_label_en: Water closet (Excusado)
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - country_entry_id: PER-SAN-28
    source_category_code: a_rio_acequi_etc
    national_label_en: A río, acequi, etc.
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: PER-SAN-29
    source_category_code: sewer_or_canal
    national_label_en: SEWER OR CANAL
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: PER-SAN-30
    source_category_code: red_publica_dentro_o_fuera_de_la_vivienda
    national_label_en: Red pública dentro o fuera de la vivienda
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: PER-SAN-31
    source_category_code: sanitario_connectado_a_red_publica_fuera_o_dentro_de_la_casa
    national_label_en: Sanitario connectado a red publica fuera o dentro de la casa
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: PER-SAN-32
    source_category_code: wc_inside_dwelling
    national_label_en: WC inside dwelling
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: PER-SAN-33
    source_category_code: pozo_septico
    national_label_en: Pozo séptico
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: PER-SAN-34
    source_category_code: sanitaria_connectado_a_septic_well
    national_label_en: Sanitaria connectado a septic well
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: PER-SAN-35
    source_category_code: septic_tank
    national_label_en: SEPTIC TANK
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: PER-SAN-36
    source_category_code: wc_septic_well
    national_label_en: WC septic well
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: PER-SAN-37
    source_category_code: turkish_chair_silla_turca
    national_label_en: '"Turkish chair" (Silla turca)'
    national_label_local: no sabe donde
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: PER-SAN-38
    source_category_code: inodoro_dentro_la_vivienda
    national_label_en: Inodoro dentro la vivienda
    national_label_local: no sabe donde
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: PER-SAN-39
    source_category_code: latrina_mejorada_colgante_flotante
    national_label_en: 'Latrina: Mejorada colgante / flotante'
    national_label_local: Letrina colgante
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: PER-SAN-40
    source_category_code: latrine_over_river_lake
    national_label_en: Latrine over river/lake
    national_label_local: Letrina colgante
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: PER-SAN-41
    source_category_code: mejorada_colgante_flotante
    national_label_en: Mejorada colgante / flotante
    national_label_local: Letrina colgante
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: PER-SAN-42
    source_category_code: rio_acequia_o_canal
    national_label_en: Río, acequia o canal
    national_label_local: Letrina colgante
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: PER-SAN-43
    source_category_code: river_canal
    national_label_en: River, canal
    national_label_local: Otro
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: PER-SAN-44
    source_category_code: pozo_ciego_o_negro
    national_label_en: Pozo ciego o negro
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: PER-SAN-45
    source_category_code: pozo_ciego_o_negro_con_o_sin_observacion_directa
    national_label_en: Pozo ciego o negro (con o sin observacion directa)
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: PER-SAN-46
    source_category_code: pozo_ciego_o_negro_letrina
    national_label_en: Pozo ciego o negro/letrina
    national_label_local: Letrina simple sin loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: PER-SAN-47
    source_category_code: latrina_pozo_ciego_o_negro
    national_label_en: 'Latrina: Pozo ciego o negro'
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-SAN-48
    source_category_code: latrine_ciego_o_negro
    national_label_en: Latrine (ciego o negro)
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-SAN-49
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
  - country_entry_id: PER-SAN-50
    source_category_code: letrina_con_o_sin_observacion_directa
    national_label_en: Letrina (con o sin observacion directa)
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-SAN-51
    source_category_code: letrina_con_tratamiento
    national_label_en: Letrina (con tratamiento)
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-SAN-52
    source_category_code: letrina_pozo_ciego_o_negro
    national_label_en: Letrina (pozo ciego o negro)
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-SAN-53
    source_category_code: pit_latrine
    national_label_en: PIT LATRINE
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-SAN-54
    source_category_code: pozo_ciego_o_negro_con_o_sin_observacion_directa
    national_label_en: Pozo ciego o negro (con o sin observacion directa)
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-SAN-55
    source_category_code: pozo_ciego_o_negro_letrina
    national_label_en: Pozo ciego o negro / letrina
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-SAN-56
    source_category_code: pozo_ciego_o_negro_letrina
    national_label_en: Pozo ciego o negro/letrina
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-SAN-57
    source_category_code: latrina_mejorada_ventilada
    national_label_en: 'Latrina: Mejorada ventilada'
    national_label_local: Letrina de pozo mejorada ventilada
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: PER-SAN-58
    source_category_code: mejorada_ventilada
    national_label_en: Mejorada ventilada
    national_label_local: Letrina de pozo mejorada ventilada
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: PER-SAN-59
    source_category_code: ventilated_latrine
    national_label_en: Ventilated latrine
    national_label_local: Letrina de pozo mejorada ventilada
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: PER-SAN-60
    source_category_code: letrina_exclusiva
    national_label_en: Letrina exclusiva
    national_label_local: Letrina privada
    jmp_classification: Latrines > Dry latrines > Private Latrines
    jmp_id: latrines.dry_latrines.private_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: no
    shared_flag: no
    source_row: 112
  - country_entry_id: PER-SAN-61
    source_category_code: letrina_exclusiva
    national_label_en: Letrina exclusiva
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: PER-SAN-62
    source_category_code: letrina_exclusiva_fuera_de_la_vivienda
    national_label_en: Letrina exclusiva (fuera de la vivienda)
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: PER-SAN-63
    source_category_code: pozo_ciego_o_negro
    national_label_en: Pozo ciego o negro
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: PER-SAN-64
    source_category_code: simple_pit_private
    national_label_en: Simple pit (private)
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: PER-SAN-65
    source_category_code: letrina_comun
    national_label_en: Letrina comun
    national_label_local: Letrina publica/compartida
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines
    jmp_id: latrines.dry_latrines.public_shared_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: no
    shared_flag: yes
    source_row: 120
  - country_entry_id: PER-SAN-66
    source_category_code: letrina_commun
    national_label_en: Letrina commun
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - country_entry_id: PER-SAN-67
    source_category_code: letrina_comun
    national_label_en: Letrina común
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - country_entry_id: PER-SAN-68
    source_category_code: letrina_comun_fuera_de_la_vivienda
    national_label_en: Letrina comun (fuera de la vivienda)
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - country_entry_id: PER-SAN-69
    source_category_code: simple_pit_shared
    national_label_en: Simple pit (shared)
    national_label_local: Letrina tradicional
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - country_entry_id: PER-SAN-70
    source_category_code: pour_flush_private
    national_label_en: Pour-flush (private)
    national_label_local: Letrinas de arrastre hidráulico (privado)
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 91
  - country_entry_id: PER-SAN-71
    source_category_code: pour_flush_shared
    national_label_en: Pour-flush (shared)
    national_label_local: Letrinas de arrastre hidráulico (publico)
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 97
  - country_entry_id: PER-SAN-72
    source_category_code: wc_outside_dwelling
    national_label_en: WC outside dwelling
    national_label_local: al alcantarillado
    jmp_classification: Latrines > Pour flush latrines > to piped sewer system
    jmp_id: latrines.pour_flush_latrines.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: PER-SAN-73
    source_category_code: blind_well_soakaway
    national_label_en: Blind well (soakaway)
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Latrines > Pour flush latrines > to pit
    jmp_id: latrines.pour_flush_latrines.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 88
  - country_entry_id: PER-SAN-74
    source_category_code: pour_flush_botadero
    national_label_en: Pour-flush (Botadero)
    national_label_local: a pozo septico
    jmp_classification: Latrines > Pour flush latrines > to septic tank
    jmp_id: latrines.pour_flush_latrines.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: PER-SAN-75
    source_category_code: bush_river_irrigation_ditch_canal
    national_label_en: Bush / River, irrigation ditch, canal
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: PER-SAN-76
    source_category_code: campo_abierto_o_al_aire_libre
    national_label_en: Campo abierto o al aire libre
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: PER-SAN-77
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
  - country_entry_id: PER-SAN-78
    source_category_code: no_hay_servicio
    national_label_en: No hay servicio
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: PER-SAN-79
    source_category_code: no_hay_servicio_matorral_campo
    national_label_en: No hay servicio (matorral / campo)
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: PER-SAN-80
    source_category_code: no_sanitation_facilities
    national_label_en: NO SANITATION FACILITIES
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: PER-SAN-81
    source_category_code: no_service
    national_label_en: No service
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: PER-SAN-82
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
  - country_entry_id: PER-SAN-83
    source_category_code: sin_servicio_matorral_campo
    national_label_en: Sin servicio (matorral/campo)
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: PER-SAN-84
    source_category_code: servicio_de_alcantarillado_y_letrinas
    national_label_en: Servicio de alcantarillado y letrinas
    national_label_local: Otro
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: PER-SAN-85
    source_category_code: letrina_con_o_sin_observacion_directa
    national_label_en: Letrina (con o sin observacion directa)
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: PER-SAN-86
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
  - country_entry_id: PER-SAN-87
    source_category_code: otra
    national_label_en: Otra
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: PER-SAN-88
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
  - country_entry_id: PER-SAN-89
    source_category_code: outro
    national_label_en: Outro
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: PER-SAN-90
    source_category_code: rio_acequia_o_canal
    national_label_en: Río, acequia o canal
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_PER_Peru_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: PER-WAS-01
    source_category_code: manantial
    national_label_en: Manantial
    national_label_local: Todos los manantiales
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: PER-WAS-02
    source_category_code: manantial_puquio
    national_label_en: Manantial (Puquio)
    national_label_local: Todos los manantiales
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: PER-WAS-03
    source_category_code: manantial_o_puquio
    national_label_en: Manantial o puquio
    national_label_local: Todos los manantiales
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: PER-WAS-04
    source_category_code: spring
    national_label_en: Spring
    national_label_local: Todos los manantiales
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: PER-WAS-05
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
  - country_entry_id: PER-WAS-06
    source_category_code: pozo_agua_subterranea
    national_label_en: Pozo (agua subterranea)
    national_label_local: Todos los pozos
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 54
  - country_entry_id: PER-WAS-07
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
  - country_entry_id: PER-WAS-08
    source_category_code: pozo_en_la_casa_patio
    national_label_en: Pozo en la casa /patio
    national_label_local: Privado
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - country_entry_id: PER-WAS-09
    source_category_code: pozo_en_la_casa_patio
    national_label_en: Pozo en la casa/patio
    national_label_local: Privado
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - country_entry_id: PER-WAS-10
    source_category_code: private_well
    national_label_en: Private well
    national_label_local: Privado
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - country_entry_id: PER-WAS-11
    source_category_code: well_in_house_or_yard
    national_label_en: Well in house or yard
    national_label_local: Privado
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - country_entry_id: PER-WAS-12
    source_category_code: well_inside_dwelling
    national_label_en: Well inside dwelling
    national_label_local: Privado
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - country_entry_id: PER-WAS-13
    source_category_code: pozo_publico
    national_label_en: Pozo publico
    national_label_local: Publico
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 56
  - country_entry_id: PER-WAS-14
    source_category_code: public_well
    national_label_en: Public well
    national_label_local: Publico
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 56
  - country_entry_id: PER-WAS-15
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
  - country_entry_id: PER-WAS-16
    source_category_code: well
    national_label_en: WELL
    national_label_local: Pozos tradicionales
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: PER-WAS-17
    source_category_code: pozo_en_la_casa_patio
    national_label_en: Pozo en la casa/patio
    national_label_local: Privado
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 63
  - country_entry_id: PER-WAS-18
    source_category_code: pozo_en_la_casa_patio_lote
    national_label_en: Pozo en la casa/patio/lote
    national_label_local: Privado
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 63
  - country_entry_id: PER-WAS-19
    source_category_code: pozo_en_la_vivineda_patio_lote
    national_label_en: Pozo en la vivineda/patio/lote
    national_label_local: Privado
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 63
  - country_entry_id: PER-WAS-20
    source_category_code: pozo_publico
    national_label_en: Pozo publico
    national_label_local: Publico
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 64
  - country_entry_id: PER-WAS-21
    source_category_code: pump
    national_label_en: PUMP
    national_label_local: Pozos entubados o de sondeo
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: PER-WAS-22
    source_category_code: camion_cisterna_u_otro_similar
    national_label_en: Camion - cisterna u otro similar
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: PER-WAS-23
    source_category_code: camion_cisterna
    national_label_en: Camion cisterna
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: PER-WAS-24
    source_category_code: camion_tanque
    national_label_en: Camion tanque
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: PER-WAS-25
    source_category_code: camion_tanque_aguatero
    national_label_en: Camion tanque/aguatero
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: PER-WAS-26
    source_category_code: camion_cisterna_u_otro_similar
    national_label_en: Camión-cisterna u otro similar
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: PER-WAS-27
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: PER-WAS-28
    source_category_code: water_tank_or_seller
    national_label_en: WATER TANK OR SELLER
    national_label_local: Agua distribuida en camiones cisterna
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: PER-WAS-29
    source_category_code: other
    national_label_en: other
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: PER-WAS-30
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
  - country_entry_id: PER-WAS-31
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
  - country_entry_id: PER-WAS-32
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
  - country_entry_id: PER-WAS-33
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
  - country_entry_id: PER-WAS-34
    source_category_code: otro
    national_label_en: Otro
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: PER-WAS-35
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
  - country_entry_id: PER-WAS-36
    source_category_code: bw_with_improved_source
    national_label_en: BW with improved source
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: PER-WAS-37
    source_category_code: bw_with_improved_sources
    national_label_en: BW with improved sources
    national_label_local: Agua embotellada
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: PER-WAS-38
    source_category_code: bw_with_unimproved_source
    national_label_en: BW with unimproved source
    national_label_local: Agua en bolsita
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: PER-WAS-39
    source_category_code: bw_with_unimproved_sources
    national_label_en: BW with unimproved sources
    national_label_local: Agua en bolsita
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: PER-WAS-40
    source_category_code: agua_de_lluivia
    national_label_en: Agua de lluivia
    national_label_local: Cisterna/tanque cubierto
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: PER-WAS-41
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
  - country_entry_id: PER-WAS-42
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
  - country_entry_id: PER-WAS-43
    source_category_code: rio_acequia_lago_laguna
    national_label_en: Río, acequia, lago, laguna
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-44
    source_category_code: rio_acequia_manantial_o_similar
    national_label_en: Rio, acequia, manantial o similar
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-45
    source_category_code: rio_acequia_manantial_o_similar
    national_label_en: Río, acequia.manantial o similar
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-46
    source_category_code: rio_acequia
    national_label_en: Río/ acequia
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-47
    source_category_code: rio_acequia_laguna
    national_label_en: Río/ acequia / Laguna
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-48
    source_category_code: rio_acequia
    national_label_en: Rio/acequia
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-49
    source_category_code: river_irrigation_channel
    national_label_en: River, irrigation channel
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-50
    source_category_code: river_irrigation_channel
    national_label_en: River/ irrigation channel
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-51
    source_category_code: river_dam_lake_ponds_stream_canal_irirgation_channel
    national_label_en: River/dam/lake/ponds/stream/canal/irirgation channel
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-52
    source_category_code: river_dam_lake_ponds_stream_canal_irrigation_channel
    national_label_en: River/dam/lake/ponds/stream/canal/irrigation channel
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: PER-WAS-53
    source_category_code: rio_acequia
    national_label_en: Río/ acequia
    national_label_local: Río
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: PER-WAS-54
    source_category_code: river_or_stream
    national_label_en: RIVER OR STREAM
    national_label_local: Río
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: PER-WAS-55
    source_category_code: connection_outdoors
    national_label_en: Connection outdoors
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: PER-WAS-56
    source_category_code: household_connection_neighbour_s
    national_label_en: Household connection (neighbour's)
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: PER-WAS-57
    source_category_code: household_connection
    national_label_en: Household connection
    national_label_local: Conexiones domiciliarias
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: PER-WAS-58
    source_category_code: red_publica_dentro_de_la_vivienda_fuera_de_la_vivienda_y_pilon_de_uso_publico
    national_label_en: Red pública dentro de la vivienda, fuera de la vivienda y pilón
      de uso público
    national_label_local: Conexiones domiciliarias
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: PER-WAS-59
    source_category_code: household_connection_to_system
    national_label_en: Household connection to system
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: PER-WAS-60
    source_category_code: inside_the_house
    national_label_en: INSIDE THE HOUSE
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: PER-WAS-61
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
  - country_entry_id: PER-WAS-62
    source_category_code: red_publica_dentro_de_la_viv
    national_label_en: Red pública Dentro de la viv.
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: PER-WAS-63
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
  - country_entry_id: PER-WAS-64
    source_category_code: red_publica_dentro_de_la_vivienda
    national_label_en: Red publica, dentro de la vivienda
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: PER-WAS-65
    source_category_code: building_connection_to_system
    national_label_en: Building connection to system
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: PER-WAS-66
    source_category_code: outside_the_house_but_inside_the_compound
    national_label_en: OUTSIDE THE HOUSE, BUT INSIDE THE COMPOUND.
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: PER-WAS-67
    source_category_code: piped_outside_dwelling_but_within_buikding
    national_label_en: Piped outside dwelling but within buikding
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: PER-WAS-68
    source_category_code: red_publica_fuera_de_la_vivienda
    national_label_en: Red Pública Fuera de la vivienda
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: PER-WAS-69
    source_category_code: red_publica_fuera_de_la_vivienda_pero_dentro_del_edificio
    national_label_en: Red publica fuera de la vivienda pero dentro del edificio
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: PER-WAS-70
    source_category_code: red_publica_fuera_de_la_vivienda_pero_dentro_de_la_edificacion
    national_label_en: Red pública fuera de la vivienda, pero dentro de la edificación
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: PER-WAS-71
    source_category_code: red_publica_fuera_de_la_vivienda_pero_dentro_del_edificio
    national_label_en: Red publica, fuera de la vivienda pero dentro del edificio
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: PER-WAS-72
    source_category_code: pilon_grifo_publico
    national_label_en: Pilon /grifo publico/
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: PER-WAS-73
    source_category_code: pilon_de_uso_publico
    national_label_en: Pilón de uso público
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: PER-WAS-74
    source_category_code: pilon_o_pileta_de_uso_publico
    national_label_en: Pilón o pileta de uso público
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: PER-WAS-75
    source_category_code: pilon_grifo_publico
    national_label_en: Pilon/Grifo publico
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: PER-WAS-76
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
  - country_entry_id: PER-WAS-77
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: Fuentes públicas
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_PER_Peru_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---









## Country notes

Every value in this file is an illustrative placeholder. None is a verified
fact about Peru, and none may be used in production before human review.

## Parameter notes

### PARAM-EDU-YEARS-BY-LEVEL

The two illustrative records demonstrate effective dating. The first closes
in 1999 and the second begins in 2000, so exactly one record is selected for
any covered survey ID year. The apparent change from 1999 to 2000 is a
structural example only and does not assert a real education reform.

### PARAM-DEM-MIN-MARRIAGE-AGE

The open-ended illustrative record demonstrates a validation parameter. The
value is not verified against Peruvian legislation.

## Verification status

All records have `human_reviewed: false`. Their provenance labels them as
placeholders, and production use is prohibited pending source verification and
GPID Team approval.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-07-28 | 0.1 | Initial illustrative draft | GPID Team |
