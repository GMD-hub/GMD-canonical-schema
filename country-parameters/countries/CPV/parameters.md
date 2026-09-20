---
country_id: CTY-CPV
iso3: CPV
schema_version: '0.2'
status: draft
country_name: CPV
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - national_label_en: Pré-scolaire
    national_label_local: Educação Pré-escolar
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - national_label_en: |-
      Enseignement de Base
      (1-6 années)
    national_label_local: |-
      Ensino Básico
      (1-6 anos)
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 8
  - national_label_en: |-
      Enseignement récurrente
      (1-6 années)
    national_label_local: |-
      Ensino recorrente
      (1-6 anos)
    entry_age: 15
    duration_years: 3
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
  - national_label_en: |-
      Enseignement de Base
      (7-8 années)
    national_label_local: |-
      Ensino Básico
      (7-8 anos)
    entry_age: 12
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
  - national_label_en: |-
      Enseignement récurrente
      (7-8 années)
    national_label_local: |-
      Ensino recorrente
      (7-8 anos)
    entry_age: 18
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
  - national_label_en: "Enseignement secondaire \n1-ère cycle \n(via general)\n1-ère
      année"
    national_label_local: "Ensino Secundário \n1º Ciclo (Via Geral)\n1º ano"
    entry_age: 14
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 12
  - national_label_en: "Enseignement récurrente \n(secondaire 1ére cycle)\n(9 année)"
    national_label_local: |-
      Ensino recorrente
      (Secundário - 1º Ciclo)
      (9 ano)
    entry_age: 20
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 13
  - national_label_en: "Enseignement secondaire \n1-ère cycle \n(via general)\n2-ème
      année"
    national_label_local: |-
      Ensino Secundário
      1º Ciclo (Via Geral)
      2o ano
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
  - national_label_en: "Enseignement récurrente \n(secondaire 1ére cycle)\n(10 année)"
    national_label_local: |-
      Ensino recorrente
      (Secundário - 1º Ciclo)
      (10 ano)
    entry_age: 21
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 15
  - national_label_en: Enseignement secondaire 2éme cycle (via générale)
    national_label_local: Ensino Secundário - 2º Ciclo (Via Geral)
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
  - national_label_en: Enseignement secondaire 2e cycle (Via Téchnique)
    national_label_local: Ensino Secundário - 2º Ciclo (Via Técnica)
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 17
  - national_label_en: "Enseignement récurrente \n(secondaire 2éme cycle)\n(11-12
      année)"
    national_label_local: |-
      Ensino recorrente
      (Secundário - 2º Ciclo)
      (11 -12ano)
    entry_age: 22
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 18
  - national_label_en: |-
      Année complémentaire professionnelle
      (ACP)
    national_label_local: |-
      Ano complementar profissionalizante
      (ACP)
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  - national_label_en: Etudes supérieures professionelles
    national_label_local: |-
      Curso de estudos superior e profissionalizante
      (CESP)
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
  - national_label_en: Enseignement supérieur (Licence)
    national_label_local: Ensino Superior (Bacharelato)
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
  - national_label_en: Enseignement supérieur (Master)
    national_label_local: Ensino Superior (Mestrado)
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
  - national_label_en: Enseignement supérieur (Doctorat)
    national_label_local: Ensino Superior (Doutoramento)
    entry_age: 24
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Cabo_Verde.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: 2015
  selectors: ~
  value:
  - survey_labels: 5 - Boa Vista | 5-Boa Vista | Boa Vista
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: CPV_2015_GAUL1_838
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CPV_2015_GAUL1_838
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '838'
    geo_nvar: ADM1_NAME
    geo_name: Boa Vista
    source_row: 3094
  - survey_labels: 9 - Brava | 9-Brava | Brava
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: CPV_2015_GAUL1_839
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CPV_2015_GAUL1_839
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '839'
    geo_nvar: ADM1_NAME
    geo_name: Brava
    source_row: 3095
  - survey_labels: 8 - Fogo | 8-Fogo | Fogo
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: CPV_2015_GAUL1_841
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CPV_2015_GAUL1_841
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '841'
    geo_nvar: ADM1_NAME
    geo_name: Fogo
    source_row: 3096
  - survey_labels: 6 - Maio | 6-Maio | Maio
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: CPV_2015_GAUL1_844
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CPV_2015_GAUL1_844
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '844'
    geo_nvar: ADM1_NAME
    geo_name: Maio
    source_row: 3097
  - survey_labels: 4 - Sal | 4-Sal | Sal
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: CPV_2015_GAUL1_846
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CPV_2015_GAUL1_846
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '846'
    geo_nvar: ADM1_NAME
    geo_name: Sal
    source_row: 3098
  - survey_labels: 7 - Santiago | 7-Santiago | Santiago
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: CPV_2015_GAUL1_848
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CPV_2015_GAUL1_848
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '848'
    geo_nvar: ADM1_NAME
    geo_name: Santiago
    source_row: 3099
  - survey_labels: 1 - Santo Antão | 1-São Antão | Santo Antão
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: CPV_2015_GAUL1_849
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CPV_2015_GAUL1_849
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '849'
    geo_nvar: ADM1_NAME
    geo_name: Santo Antao
    source_row: 3100
  - survey_labels: 3 - São Nicolau | 3- São Nicolau | São Nicolau
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: CPV_2015_GAUL1_850
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CPV_2015_GAUL1_850
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '850'
    geo_nvar: ADM1_NAME
    geo_name: Sao Nicolau
    source_row: 3101
  - survey_labels: 2 - São Vicente | 2-São Vicente | São Vicente
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: CPV_2015_GAUL1_851
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CPV_2015_GAUL1_851
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '851'
    geo_nvar: ADM1_NAME
    geo_name: Sao Vicente
    source_row: 3102
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2022
  effective_to: ~
  selectors: ~
  value:
  - survey_labels: 11 - Ribeira Grande | 11-Ribeira Grande
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.9_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.9_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.9_1
    geo_nvar: NAME_1
    geo_name: Ribeira Grande
    source_row: 3112
  - survey_labels: 12 - Paul | 12-Paúl
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.5_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.5_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.5_1
    geo_nvar: NAME_1
    geo_name: Paúl
    source_row: 3113
  - survey_labels: 13 - Porto Novo | 13-Porto novo
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.6_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.6_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.6_1
    geo_nvar: NAME_1
    geo_name: Porto Novo
    source_row: 3114
  - survey_labels: 21 - São Vicente | 21-São vicente
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.20_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.20_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.20_1
    geo_nvar: NAME_1
    geo_name: São Vicente
    source_row: 3115
  - survey_labels: 31 - Ribeira Brava | 31-Ribeira Brava
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.8_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.8_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.8_1
    geo_nvar: NAME_1
    geo_name: Ribeira Brava
    source_row: 3116
  - survey_labels: 32 - Tarrafal de São Nicolau | 32-Tarrafal de São Nicolau
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.22_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.22_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.22_1
    geo_nvar: NAME_1
    geo_name: Tarrafal de São Nicolau
    source_row: 3117
  - survey_labels: 41 - Sal | 41-Sal
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.11_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.11_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.11_1
    geo_nvar: NAME_1
    geo_name: Sal
    source_row: 3118
  - survey_labels: 51 - Boa Vista | 51-Boavista
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.1_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.1_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.1_1
    geo_nvar: NAME_1
    geo_name: Boa Vista
    source_row: 3119
  - survey_labels: 61 - Maio | 61-Maio
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.3_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.3_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.3_1
    geo_nvar: NAME_1
    geo_name: Maio
    source_row: 3120
  - survey_labels: 71 - Tarrafal de Santiago | 71-Tarrafal
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.21_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.21_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.21_1
    geo_nvar: NAME_1
    geo_name: Tarrafal
    source_row: 3121
  - survey_labels: 72 - Santa Catarina | 72-Santa Catarina
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.12_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.12_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.12_1
    geo_nvar: NAME_1
    geo_name: Santa Catarina
    source_row: 3122
  - survey_labels: 73 - Santa Cruz | 73-Santa Cruz
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.14_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.14_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.14_1
    geo_nvar: NAME_1
    geo_name: Santa Cruz
    source_row: 3123
  - survey_labels: 74 - Praia | 74-Praia
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.7_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.7_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.7_1
    geo_nvar: NAME_1
    geo_name: Praia
    source_row: 3124
  - survey_labels: 75 - São Domingo | 75-São Domingos
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.15_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.15_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.15_1
    geo_nvar: NAME_1
    geo_name: São Domingos
    source_row: 3125
  - survey_labels: 76 - Calheta S. Miguel | 76-São Miguel
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.18_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.18_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.18_1
    geo_nvar: NAME_1
    geo_name: São Miguel
    source_row: 3126
  - survey_labels: 77 - São Lourenço dos Orgãos | 77-São Salvador do Mundo
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.17_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.17_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.17_1
    geo_nvar: NAME_1
    geo_name: São Lourenço dos Órgãos
    source_row: 3127
  - survey_labels: 78 - São Salvador do Mundo | 78-São Lourenço dos Órgãos
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.19_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.19_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.19_1
    geo_nvar: NAME_1
    geo_name: São Salvador do Mundo
    source_row: 3128
  - survey_labels: 79 - Ribeira Gr. de Santiago | 79-Ribeira Grande de Santiago
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.10_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.10_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.10_1
    geo_nvar: NAME_1
    geo_name: Ribeira Grande de Santiago
    source_row: 3129
  - survey_labels: 81 - Mosteiros | 81-Mosteiros
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.4_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.4_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.4_1
    geo_nvar: NAME_1
    geo_name: Mosteiros
    source_row: 3130
  - survey_labels: 82 - São Filipe | 82-São Filipe
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.16_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.16_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.16_1
    geo_nvar: NAME_1
    geo_name: São Filipe
    source_row: 3131
  - survey_labels: 83 - Santa Catarina do Fogo | 83-Santa Catarina do Fogo
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.13_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.13_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.13_1
    geo_nvar: NAME_1
    geo_name: Santa Catarina do Fogo
    source_row: 3132
  - survey_labels: 91 - Brava | 91-Brava
    survey_variables: subnatid2 | subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: CPV_2022_GADM1_CPV.2_1
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: yes
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 2
    gmd_subnatidsurvey: CPV_2022_GADM1_CPV.2_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: CPV.2_1
    geo_nvar: NAME_1
    geo_name: Brava
    source_row: 3133
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
  - source_category_code: nao_nenhum_disponivel
    national_label_en: Não, nenhum disponivel
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: no_none_available
    national_label_en: No, none available
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: sem_instalacao
    national_label_en: Sem Instalacao
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: sem_instalacao_sanitaria
    national_label_en: Sem instalacao sanitaria
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - source_category_code: other_type_of_sanitation
    national_label_en: Other type of sanitation
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - source_category_code: total_do_outras_respostas_nao_se_sabe_o_tipo_de_saneamento
    national_label_en: Total do outras respostas, nao se sabe o tipo de saneamento
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CPV_Cabo_Verde_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - source_category_code: nascente
    national_label_en: Nascente
    national_label_local: All springs
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - source_category_code: poco
    national_label_en: Poço
    national_label_local: All wells
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 54
  - source_category_code: nascente_protegida
    national_label_en: Nascente protegida
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - source_category_code: poco_protegido
    national_label_en: Poço protegido
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - source_category_code: poco
    national_label_en: Poco
    national_label_local: Traditional wells
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - source_category_code: poco_com_tubo_ou_poco
    national_label_en: Poço com  tubo ou poço
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - source_category_code: nascente_desprotegida
    national_label_en: Nascente desprotegida
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - source_category_code: poco_desprotegido
    national_label_en: Poço desprotegido
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - source_category_code: comprado_em_um_carrinho_com_um_pequeno_tanque_ou_tambor
    national_label_en: Comprado em um carrinho com um pequeno tanque ou tambor
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - source_category_code: cisterna_publica
    national_label_en: Cisterna Publica
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - source_category_code: auto_tanque
    national_label_en: Auto-Tanque
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: autotanque
    national_label_en: Autotanque
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: comprado_num_camiao_auto_tanque
    national_label_en: Comprado num camião auto-tanque
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - source_category_code: outro
    national_label_en: Outro
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - source_category_code: nao_sabe
    national_label_en: Não sabe
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - source_category_code: outro
    national_label_en: Outro
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - source_category_code: agua_engarrafada
    national_label_en: Agua engarrafada
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - source_category_code: agua_da_chuva_recolhida
    national_label_en: Água da chuva recolhida
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: cisterna
    national_label_en: Cisterna
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: cisterna_domiciliaria
    national_label_en: Cisterna Domiciliária
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - source_category_code: aguas_superficiais_como_rio_represa_lago_lagoa_ribeira
    national_label_en: Águas superficiais, como rio, represa, lago, lagoa, ribeira
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - source_category_code: levada
    national_label_en: Levada
    national_label_local: Irrigation channel
    jmp_classification: Surface water > Irrigation channel
    jmp_id: surface_water.irrigation_channel
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 98
  - source_category_code: agua_rede_publica_casa_dos_vizinhos
    national_label_en: Agua rede publica casa dos vizinhos
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - source_category_code: agua_canalizada_da_rede_publica
    national_label_en: Agua canalizada da rede publica
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - source_category_code: agua_da_rede_publica
    national_label_en: Água da rede pública
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - source_category_code: agua_canalizada_na_habitacao
    national_label_en: Água canalizada na habitação
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - source_category_code: agua_canalizada_no_quintal_parcela_ou_condominio
    national_label_en: Água canalizada no quintal, parcela ou condominio
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - source_category_code: chafariz
    national_label_en: Chafariz
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CPV_Cabo_Verde_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

