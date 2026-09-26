---
country_id: CTY-MAC
iso3: MAC
schema_version: '0.2'
status: draft
country_name: MAC
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: MAC-EDU-01
    national_label_en: Infant education
    national_label_local: |-
      幼兒教育
      Ensino infantil
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: MAC-EDU-02
    national_label_en: Primary education
    national_label_local: |-
      小學教育
      Ensino primário
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
  - country_entry_id: MAC-EDU-03
    national_label_en: Junior secondary education
    national_label_local: |-
      初中教育
      Ensino secundário geral
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - country_entry_id: MAC-EDU-04
    national_label_en: Senior secondary education
    national_label_local: |-
      高中教育
      Ensino secundário complementar
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
  - country_entry_id: MAC-EDU-05
    national_label_en: Senior secondary education (Courses of vocational and technical
      education)
    national_label_local: |-
      高中教育（職業技術教育課程）
      Ensino secundário complementar (cursos do ensino técnico-profissional)
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - country_entry_id: MAC-EDU-06
    national_label_en: Senior secondary education (Courses of vocational and technical
      education)
    national_label_local: |-
      高中教育（職業技術教育課程）
      Ensino secundário complementar (cursos do ensino técnico-profissional)
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: MAC-EDU-07
    national_label_en: Higher education diploma programme (2 years)
    national_label_local: |-
      高等教育文憑
      Diploma de ensino superior
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
  - country_entry_id: MAC-EDU-08
    national_label_en: "Bacharelato \nprogramme (3 years)"
    national_label_local: |-
      高等專科學位
      Bacharelato
    entry_age: 17
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - country_entry_id: MAC-EDU-09
    national_label_en: Bachelor's degree programme (4 years)
    national_label_local: |-
      學士學位
      Licenciatura
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - country_entry_id: MAC-EDU-10
    national_label_en: Bachelor's degree programme  (5 years)
    national_label_local: |-
      學士學位
      Licenciatura
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: MAC-EDU-11
    national_label_en: Master's degree programme
    national_label_local: |-
      碩士學位
      Mestrado
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: MAC-EDU-12
    national_label_en: Postgraduate diploma programme
    national_label_local: |-
      學位後文憑
      Diploma de Pós-Graduação
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - country_entry_id: MAC-EDU-13
    national_label_en: Doctor's degree programme
    national_label_local: |-
      博士學位
      Doutoramente
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_China,
      Macao Special Administrative Region.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

