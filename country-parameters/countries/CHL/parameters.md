---
country_id: CTY-CHL
iso3: CHL
schema_version: '0.2'
status: draft
country_name: CHL
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CHL-EDU-01
    national_label_en: Early Childhood Education (Day Care and Lower Middle Level)
    national_label_local: "Educaci\xF3n Parvularia (Sala Cuna y Nivel Medio Menor)"
    entry_age: 0
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 5
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: CHL-EDU-02
    national_label_en: Pre-primary Education (Upper Middle Level, 1st Transition Level
      and 2nd Transition Level)
    national_label_local: "Educaci\xF3n Parvularia (Nivel Medio Mayor, Nivel de Transici\xF3\
      n 1 y Nivel de Transici\xF3n 2)"
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 6
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: CHL-EDU-03
    national_label_en: Primary Education
    national_label_local: "Ense\xF1anza B\xE1sica (grados 1\xB0 al 6\xB0)"
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - CHL-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: CHL-EDU-04
    national_label_en: Lower Secondary Education
    national_label_local: "Ense\xF1anza B\xE1sica (grados 7\xB0 y 8\xB0)"
    entry_age: 12
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 8
    parent_country_entry_ids:
    - CHL-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHL-EDU-05
    national_label_en: General Upper Secondary Education
    national_label_local: "Ciclo General de Ense\xF1anza Media"
    entry_age: 14
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 9
    parent_country_entry_ids:
    - CHL-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHL-EDU-06
    national_label_en: Sciences and Humanities Upper Secondary Education
    national_label_local: "Ciclo Diferenciado de Ense\xF1anza Media Humanista-Cient\xED\
      fico"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - CHL-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHL-EDU-07
    national_label_en: Technical Upper Secondary Education
    national_label_local: "Ciclo Diferenciado de Ense\xF1anza Media T\xE9cnico-Profesional"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - CHL-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHL-EDU-08
    national_label_en: Technical Upper Secondary Education
    national_label_local: "Ciclo Diferenciado de Ense\xF1anza Media T\xE9cnico-Profesional"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - CHL-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHL-EDU-09
    national_label_en: Artistic Upper Secondary Education
    national_label_local: "Ciclo Diferenciado de Ense\xF1anza Media Art\xEDstica"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - CHL-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHL-EDU-10
    national_label_en: Special Upper Secondary education with Trade Training
    national_label_local: "Ense\xF1anza Media Especial con Formaci\xF3n de Oficios"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - CHL-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: CHL-EDU-11
    national_label_en: Higher Technical Education
    national_label_local: "Educaci\xF3n T\xE9cnica de Nivel Superior"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - CHL-EDU-05
    - CHL-EDU-06
    - CHL-EDU-09
    - CHL-EDU-10
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-05
    - CHL-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHL-EDU-05, CHL-EDU-06, CHL-EDU-09, CHL-EDU-10'
  - country_entry_id: CHL-EDU-12
    national_label_en: General Short-Cycle Programme
    national_label_local: Bachillerato
    entry_age: 18
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - CHL-EDU-05
    - CHL-EDU-06
    - CHL-EDU-09
    - CHL-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-05
    - CHL-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHL-EDU-05, CHL-EDU-06, CHL-EDU-09, CHL-EDU-10'
  - country_entry_id: CHL-EDU-13
    national_label_en: Post-Title Graduate Certificate
    national_label_local: "Post\xEDtulo"
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - CHL-EDU-05
    - CHL-EDU-06
    - CHL-EDU-09
    - CHL-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-05
    - CHL-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHL-EDU-05, CHL-EDU-06, CHL-EDU-09, CHL-EDU-10'
  - country_entry_id: CHL-EDU-14
    national_label_en: Medical or Dental Graduate Specialization Programme
    national_label_local: "Especialidad M\xE9dica u Odontol\xF3gica"
    entry_age: 24
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - CHL-EDU-05
    - CHL-EDU-06
    - CHL-EDU-09
    - CHL-EDU-10
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-05
    - CHL-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHL-EDU-05, CHL-EDU-06, CHL-EDU-09, CHL-EDU-10'
  - country_entry_id: CHL-EDU-15
    national_label_en: Doctorate Programme
    national_label_local: Doctorado
    entry_age: 22
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - CHL-EDU-13
    - CHL-EDU-14
    cum_years_schooling: 14
    cum_years_computation_path:
    - CHL-EDU-03
    - CHL-EDU-04
    - CHL-EDU-05
    - CHL-EDU-13
    - CHL-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHL-EDU-05, CHL-EDU-06, CHL-EDU-09, CHL-EDU-10'
    - 'minimum parent path selected from: CHL-EDU-13, CHL-EDU-14'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Chile.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CHL-SUBNAT-01
    survey_labels: "1 -    I Region de Tarapaca | 1 - Arica y Parinacota y Tarapac\xE1"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAULx_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAULx_1
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '1'
    geo_nvar: ADM1_NAME
    geo_name: Arica y Painacota & Tarapaca
    source_row: 2183
  - country_entry_id: CHL-SUBNAT-02
    survey_labels: "10 -    X Region de Los Lagos | 10 - Los R\xEDos y Los Lagos"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAULx_10
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAULx_10
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '10'
    geo_nvar: ADM1_NAME
    geo_name: Los Rios & Los Lagos
    source_row: 2184
  - country_entry_id: CHL-SUBNAT-03
    survey_labels: "11 -   XI Region de Aysen del Gral. Carlos Iba\xF1ez | 11 -  \
      \ XI Region de Aysen del Gral. Carlos Iba\uFFFDez | 11 - Ays\xE9n | 11 - XI\
      \ Region de Aysen del Gral. Carlos Iba\xF1ez"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_886
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_886
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '886'
    geo_nvar: ADM1_NAME
    geo_name: "Aisen del Gral. Carlos Iba\xF1ez del Campo"
    source_row: 2185
  - country_entry_id: CHL-SUBNAT-04
    survey_labels: "12 -  XII Region de Magallanes y de la Antartica | 12 - Magallanes\
      \ y La Ant\xE1rtica Chilena | 12 - XII Region de Magallanes y de la Antartica"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_891
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_891
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '891'
    geo_nvar: ADM1_NAME
    geo_name: Magallanes y Antartica chilena
    source_row: 2186
  - country_entry_id: CHL-SUBNAT-05
    survey_labels: "13 - Regi\xF3n Metropolitana | 13 - XIII Region Metropolitana\
      \ de Santiago"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_893
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_893
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '893'
    geo_nvar: ADM1_NAME
    geo_name: Metropolitana
    source_row: 2187
  - country_entry_id: CHL-SUBNAT-06
    survey_labels: 2 -   II Region de Antofagasta | 2 - Antofagasta | 2 - II Region
      de Antofagasta
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_883
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_883
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '883'
    geo_nvar: ADM1_NAME
    geo_name: Antofagasta
    source_row: 2188
  - country_entry_id: CHL-SUBNAT-07
    survey_labels: 3 -  III Region de Atacama | 3 - Atacama | 3 - III Region de Atacama
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_885
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_885
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '885'
    geo_nvar: ADM1_NAME
    geo_name: Atacama
    source_row: 2189
  - country_entry_id: CHL-SUBNAT-08
    survey_labels: 4 -   IV Region de Coquimbo | 4 - Coquimbo | 4 - IV Region de Coquimbo
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_888
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_888
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '888'
    geo_nvar: ADM1_NAME
    geo_name: Coquimbo
    source_row: 2190
  - country_entry_id: CHL-SUBNAT-09
    survey_labels: "5 -    V Region de Valparaiso | 5 - V Region de Valparaiso | 5\
      \ - Valpara\xEDso"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_149630
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_149630
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '149630'
    geo_nvar: ADM1_NAME
    geo_name: Valparaiso
    source_row: 2191
  - country_entry_id: CHL-SUBNAT-10
    survey_labels: 6 -   VI Region del Libertador Gral. B. O'Higgins | 6 - Libertador
      Bernardo O'Higgins | 6 - VI Region del Libertador Gral. B. O'Higgins
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_889
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_889
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '889'
    geo_nvar: ADM1_NAME
    geo_name: Libertador Gral. Bernardo O'Higgins
    source_row: 2192
  - country_entry_id: CHL-SUBNAT-11
    survey_labels: 7 -  VII Region del Maule | 7 - Maule | 7 - VII Region del Maule
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_892
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_892
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '892'
    geo_nvar: ADM1_NAME
    geo_name: Maule
    source_row: 2193
  - country_entry_id: CHL-SUBNAT-12
    survey_labels: "8 - B\xEDo B\xEDo | 8 - VIII Region del BioBio"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_887
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_887
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '887'
    geo_nvar: ADM1_NAME
    geo_name: Biobio
    source_row: 2194
  - country_entry_id: CHL-SUBNAT-13
    survey_labels: "9 -   IX Region de la Araucania | 9 - IX Region de la Araucania\
      \ | 9 - La Araucan\xEDa"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_884
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_884
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '884'
    geo_nvar: ADM1_NAME
    geo_name: Araucania
    source_row: 2195
  - country_entry_id: CHL-SUBNAT-14
    survey_labels: 1 -    I Region de Tarapaca | 1 - I Region de Tarapaca
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_91502
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_91502
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '91502'
    geo_nvar: ADM1_NAME
    geo_name: Tarapaca
    source_row: 2209
  - country_entry_id: CHL-SUBNAT-15
    survey_labels: 10 -    X Region de Los Lagos | 10 - X Region de Los Lagos
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_91501
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_91501
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '91501'
    geo_nvar: ADM1_NAME
    geo_name: Los Lagos
    source_row: 2210
  - country_entry_id: CHL-SUBNAT-16
    survey_labels: 14 -  XIV Region de Los Rios | 14 - XIV Region de Los Rios
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_91504
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_91504
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '91504'
    geo_nvar: ADM1_NAME
    geo_name: Los Rios
    source_row: 2214
  - country_entry_id: CHL-SUBNAT-17
    survey_labels: 15 -   XV Region de Arica y Parinacota | 15 - XV Region de Arica
      y Parinacota
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL1_91503
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL1_91503
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '91503'
    geo_nvar: ADM1_NAME
    geo_name: Arica y Painacota
    source_row: 2215
  - country_entry_id: CHL-SUBNAT-18
    survey_labels: 8 - VIII Region del BioBio
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAULx_8
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAULx_8
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '8'
    geo_nvar: ADM1_NAME
    geo_name: Biobio
    source_row: 2267
  - country_entry_id: CHL-SUBNAT-19
    survey_labels: "16 -  XVI Region del \xD1uble | 16 - XVI Region del \xD1uble"
    survey_variables: subnatid1 | subnatidsurvey
    gmd_subnatid1: CHL_2015_GAUL2_12947
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHL_2015_GAUL2_12947
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '2'
    geo_idvar: ADM2_CODE
    geo_id: '12947'
    geo_nvar: ADM2_NAME
    geo_name: "\xD1uble"
    source_row: 2276
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
  - country_entry_id: CHL-SAN-01
    source_category_code: si_con_cajon_sobre_acequia_o_canal
    national_label_en: "s\xED, con caj\xF3n sobre acequia o canal"
    national_label_local: a drenaje abierto
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: CHL-SAN-02
    source_category_code: si_con_wc_conectado_al_alcantarillado
    national_label_en: "S\xED, con WC conectado al alcantarillado"
    national_label_local: al alcantarillado
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: CHL-SAN-03
    source_category_code: si_con_letrina_sanitaria_conectada_a_pozo_negro
    national_label_en: "S\xED, con letrina sanitaria conectada a pozo negro"
    national_label_local: a letrina con cierre hidraulico
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: CHL-SAN-04
    source_category_code: si_con_wc_conectado_a_fosa_septica
    national_label_en: "S\xED, con WC conectado a fosa s\xE9ptica"
    national_label_local: a pozo septico
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: CHL-SAN-05
    source_category_code: si_con_cajon_sobre_pozo_negro
    national_label_en: "S\xED, con caj\xF3n sobre pozo negro"
    national_label_local: Letrina simple con loza
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: CHL-SAN-06
    source_category_code: no_dispone_de_sistema
    national_label_en: no dispone de sistema
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: CHL-SAN-07
    source_category_code: no_tiene
    national_label_en: No tiene
    national_label_local: No hay installacion sanitaria
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: CHL-SAN-08
    source_category_code: si_con_bano_quimico_dentro_del_sitio
    national_label_en: "s\xED, con ba\xF1o qu\xEDmico dentro del sitio"
    national_label_local: Otro
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: CHL-SAN-09
    source_category_code: si_con_cajon_conectado_a_otro_sistema
    national_label_en: "s\xED, con caj\xF3n conectado a otro sistema"
    national_label_local: Otro
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 133
  - country_entry_id: CHL-SAN-10
    source_category_code: si_otra
    national_label_en: Si, otra
    national_label_local: Otro
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CHL_Chile_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CHL-WAS-01
    source_category_code: pozo_o_noria
    national_label_en: Pozo o noria
    national_label_local: Todos los pozos
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 54
  - country_entry_id: CHL-WAS-02
    source_category_code: camion_aljibe
    national_label_en: "Cami\xF3n aljibe"
    national_label_local: "Carro con tanque / tambor peque\xF1o"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: CHL-WAS-03
    source_category_code: otra_fuente
    national_label_en: Otra fuente
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: CHL-WAS-04
    source_category_code: otra_fuente_por_acarreo
    national_label_en: Otra fuente por acarreo
    national_label_local: Otro
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: CHL-WAS-05
    source_category_code: rio_vertiente_lago_o_estero
    national_label_en: "R\xEDo, vertiente, lago o estero"
    national_label_local: Agua superficial
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: CHL-WAS-06
    source_category_code: otra_fuente_con_llave_dentro_de_la_vivienda
    national_label_en: Otra fuente con llave dentro de la vivienda
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: CHL-WAS-07
    source_category_code: red_publica_no_sabe
    national_label_en: "Red p\xFAblica No sabe"
    national_label_local: Otro
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: CHL-WAS-08
    source_category_code: red_publica_con_llave_dentro_de_la_vivienda
    national_label_en: "Red p\xFAblica con llave dentro de la vivienda"
    national_label_local: Agua entubada en la vivienda
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: CHL-WAS-09
    source_category_code: red_publica_con_llave_dentro_del_sitio_pero_fuera_de_la_vivienda
    national_label_en: "Red p\xFAblica con llave dentro del sitio, pero fuera de la\
      \ vivienda"
    national_label_local: Agua corriente al patio/parcela
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: CHL-WAS-10
    source_category_code: red_publica_no_tiene_sistema_la_acarrea
    national_label_en: "Red p\xFAblica No tiene sistema, la acarrea"
    national_label_local: "Fuentes p\xFAblicas"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: CHL-WAS-11
    source_category_code: red_publica_por_acarreo
    national_label_en: "Red p\xFAblica por acarreo"
    national_label_local: "Fuentes p\xFAblicas"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CHL_Chile_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1999
  effective_to: null
  selectors: null
  value: 15
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

