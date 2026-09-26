---
country_id: CTY-NER
iso3: NER
schema_version: '0.2'
status: draft
country_name: NER
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: NER-EDU-01
    national_label_en: Préscolaire
    national_label_local: Préscolaire
    entry_age: 5
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: NER-EDU-02
    national_label_en: Enseignement de base, cycle 1
    national_label_local: Enseignement de base, cycle 1
    entry_age: 7
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
  - country_entry_id: NER-EDU-03
    national_label_en: Enseignement de base, cycle 2
    national_label_local: Enseignement de base, cycle 2
    entry_age: 13
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - country_entry_id: NER-EDU-04
    national_label_en: Enseignement professionnel technique 1er cycle
    national_label_local: Enseignement professionnel technique 1er cycle
    entry_age: 13
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
  - country_entry_id: NER-EDU-05
    national_label_en: Enseignement moyen
    national_label_local: Enseignement moyen
    entry_age: 17
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - country_entry_id: NER-EDU-06
    national_label_en: Formation initiale des instituteurs adjoints
    national_label_local: Formation initiale des instituteurs adjoints
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: NER-EDU-07
    national_label_en: Enseignement technique ou professionel 2 e cycle
    national_label_local: Enseignement technique ou professionel 2 e cycle
    entry_age: 17
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
  - country_entry_id: NER-EDU-08
    national_label_en: Enseignement normal, cycle instituteur
    national_label_local: Enseignement normal, cycle instituteur
    entry_age: 20
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - country_entry_id: NER-EDU-09
    national_label_en: Enseignement supérieur professionnel
    national_label_local: Enseignement supérieur professionnel
    entry_age: 20
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - country_entry_id: NER-EDU-10
    national_label_en: Formation des professeurs du cycle de Base 2
    national_label_local: Formation des professeurs du cycle de Base 2
    entry_age: 20
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: NER-EDU-11
    national_label_en: Formation conseiller Pédagogique Base 1
    national_label_local: Formation conseiller Pédagogique Base 1
    entry_age: 21
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: NER-EDU-12
    national_label_en: Études universitaires Technologiques
    national_label_local: Études universitaires Technologiques
    entry_age: 20
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - country_entry_id: NER-EDU-13
    national_label_en: Licence
    national_label_local: Licence
    entry_age: 20
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  - country_entry_id: NER-EDU-14
    national_label_en: License Professionnelle
    national_label_local: License Professionnelle
    entry_age: 20
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
  - country_entry_id: NER-EDU-15
    national_label_en: Etudes des Sciences de la Santé
    national_label_local: Etudes des Sciences de la Santé
    entry_age: 20
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
  - country_entry_id: NER-EDU-16
    national_label_en: Formation conseiller Pédagogique Base 2
    national_label_local: Formation conseiller Pédagogique Base 2
    entry_age: 22
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
  - country_entry_id: NER-EDU-17
    national_label_en: Formation des Inspecteurs
    national_label_local: Formation des Inspecteurs
    entry_age: 23
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
  - country_entry_id: NER-EDU-18
    national_label_en: Etudes Pharmaceutiques
    national_label_local: Etudes Pharmaceutiques
    entry_age: 20
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
  - country_entry_id: NER-EDU-19
    national_label_en: Enseignement supérieur Master I
    national_label_local: Enseignement supérieur Master I
    entry_age: 23
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
  - country_entry_id: NER-EDU-20
    national_label_en: Formation des professeurs du cycle Moyen
    national_label_local: Formation des professeurs du cycle Moyen
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
  - country_entry_id: NER-EDU-21
    national_label_en: Etudes de médecine (médecin)
    national_label_local: Etudes de médecine (médecin)
    entry_age: 20
    duration_years: 7
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
  - country_entry_id: NER-EDU-22
    national_label_en: Enseignement supérieur (DESS)
    national_label_local: Enseignement supérieur (DESS)
    entry_age: 24
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
  - country_entry_id: NER-EDU-23
    national_label_en: Enseignement supérieur (DEA)
    national_label_local: Enseignement supérieur (DEA)
    entry_age: 24
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
  - country_entry_id: NER-EDU-24
    national_label_en: Master
    national_label_local: Master
    entry_age: 24
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
  - country_entry_id: NER-EDU-25
    national_label_en: Enseignement supérieur 3 e cycle
    national_label_local: Enseignement supérieur 3 e cycle
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Niger.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: NER-SUBNAT-01
    survey_labels: 1 - Agadez | 1 - agadez | 1 - gadez
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: NER_2015_GAUL1_2202
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: NER_2015_GAUL1_2202
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2202'
    geo_nvar: ADM1_NAME
    geo_name: Agadez
    source_row: 10725
  - country_entry_id: NER-SUBNAT-02
    survey_labels: 2 - Diffa | 2 - diffa
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: NER_2015_GAUL1_2203
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: NER_2015_GAUL1_2203
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2203'
    geo_nvar: ADM1_NAME
    geo_name: Diffa
    source_row: 10726
  - country_entry_id: NER-SUBNAT-03
    survey_labels: 3 - Dosso | 3 - dosso
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: NER_2015_GAUL1_2204
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: NER_2015_GAUL1_2204
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2204'
    geo_nvar: ADM1_NAME
    geo_name: Dosso
    source_row: 10727
  - country_entry_id: NER-SUBNAT-04
    survey_labels: 4 - Maradi | 4 - maradi
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: NER_2015_GAUL1_2205
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: NER_2015_GAUL1_2205
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2205'
    geo_nvar: ADM1_NAME
    geo_name: Maradi
    source_row: 10728
  - country_entry_id: NER-SUBNAT-05
    survey_labels: 5 - Tahoua | 5 - tahoua
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: NER_2015_GAUL1_2207
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: NER_2015_GAUL1_2207
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2207'
    geo_nvar: ADM1_NAME
    geo_name: Tahoua
    source_row: 10729
  - country_entry_id: NER-SUBNAT-06
    survey_labels: 6 - Tillaberi | 6 - Tillabéri | 6 - Tillab�ri | 6 - tillaberi
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: NER_2015_GAUL1_2208
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: NER_2015_GAUL1_2208
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2208'
    geo_nvar: ADM1_NAME
    geo_name: Tillaberi
    source_row: 10730
  - country_entry_id: NER-SUBNAT-07
    survey_labels: 7 - Zinder | 7 - zinder | 7 -Zinder
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: NER_2015_GAUL1_2209
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: NER_2015_GAUL1_2209
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2209'
    geo_nvar: ADM1_NAME
    geo_name: Zinder
    source_row: 10731
  - country_entry_id: NER-SUBNAT-08
    survey_labels: 8 - Communauté urbaine de Niamey | 8 - Communaut� urbaine de Niamey
      | 8 - Niamey | 8 - niamey
    survey_variables: subnatid | subnatid1 | subnatidsurvey
    gmd_subnatid1: NER_2015_GAUL1_2206
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: NER_2015_GAUL1_2206
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '2206'
    geo_nvar: ADM1_NAME
    geo_name: Niamey
    source_row: 10732
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
  - country_entry_id: NER-SAN-01
    source_category_code: 8_composting
    national_label_en: 8. composting
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: NER-SAN-02
    source_category_code: 8_composting_toilet
    national_label_en: 8. Composting toilet
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: NER-SAN-03
    source_category_code: 9_composting_toilet
    national_label_en: 9. Composting toilet
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: NER-SAN-04
    source_category_code: composage
    national_label_en: composage
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: NER-SAN-05
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: NER-SAN-06
    source_category_code: des_toilettes_a_compostage
    national_label_en: Des toilettes à compostage
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: NER-SAN-07
    source_category_code: latrines_ecosan_dallees_couvertes
    national_label_en: Latrines ECOSAN (dallees, couvertes)
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: NER-SAN-08
    source_category_code: toilettes_a_compostage
    national_label_en: Toilettes à compostage
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: NER-SAN-09
    source_category_code: chasse_eau
    national_label_en: chasse_eau
    national_label_local: شطف وصب دافق
    jmp_classification: Flush and pour flush
    jmp_id: flush_and_pour_flush
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 60
  - country_entry_id: NER-SAN-10
    source_category_code: 3_flush_pour_flush_toilets_connected_to_elsewhere
    national_label_en: '3. Flush/pour flush toilets connected to: Elsewhere'
    national_label_local: إلى مكان آخر
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: NER-SAN-11
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_ailleurs
    national_label_en: Des toilettes à chasse d’eau connectées à ailleurs
    national_label_local: إلى مكان آخر
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: NER-SAN-12
    source_category_code: flushed_toilet_to_elsewhere
    national_label_en: Flushed toilet to elsewhere
    national_label_local: إلى مكان آخر
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: NER-SAN-13
    source_category_code: 1_flush_pour_flush_toilets_connected_to_piped_sewer_system
    national_label_en: '1. Flush/pour flush toilets connected to: Piped sewer system'
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: NER-SAN-14
    source_category_code: chasse_d_eau_evacuation_aux_eaux_usees
    national_label_en: Chasse d'eau evacuation aux eaux usees
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: NER-SAN-15
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_un_systeme_d_egouts
    national_label_en: Des toilettes à chasse d’eau connectées à un système d'égoûts
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: NER-SAN-16
    source_category_code: flush_toilet_to_piped_sewer_system
    national_label_en: Flush toilet to piped sewer system
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: NER-SAN-17
    source_category_code: 13_flush_pour_flush_toilets_connected_to_pit_latrine
    national_label_en: '13. Flush/pour flush toilets connected to: Pit Latrine'
    national_label_local: للحفر
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: NER-SAN-18
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_latrines_a_fosse
    national_label_en: Des toilettes à chasse d’eau connectées à latrines à fosse
    national_label_local: للحفر
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: NER-SAN-19
    source_category_code: flushed_toilet_to_pit_latrine
    national_label_en: Flushed toilet to pit latrine
    national_label_local: للحفر
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: NER-SAN-20
    source_category_code: 2_flush_pour_flush_toilets_connected_to_septic_tank
    national_label_en: '2. Flush/pour flush toilets connected to: Septic tank'
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: NER-SAN-21
    source_category_code: chasse_d_eau_evacuation_en_fosse_septique
    national_label_en: Chasse d'eau evacuation en fosse septique
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: NER-SAN-22
    source_category_code: connecte_a_une_fosse_septique
    national_label_en: Connecte a une fosse septique
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: NER-SAN-23
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_une_fosse_septique
    national_label_en: Des toilettes à chasse d’eau connectées à une fosse septique
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: NER-SAN-24
    source_category_code: flushed_toilet_to_septic_tank
    national_label_en: Flushed toilet to septic tank
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: NER-SAN-25
    source_category_code: 4_flush_pour_flush_toilets_connected_to_unknown_not_sure_do_not_know
    national_label_en: '4. Flush/pour flush toilets connected to: Unknown / Not sure
      / Do not know'
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: NER-SAN-26
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_inconnu_pas_sur_e_ne_sait_pas
    national_label_en: Des toilettes à chasse d’eau connectées à Inconnu / Pas sûr(e)
      / Ne sait pas
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: NER-SAN-27
    source_category_code: chasse_d_eau
    national_label_en: Chasse d'eau
    national_label_local: دافق / مراحيض
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-SAN-28
    source_category_code: chasse_d_eau_avec_egouts_ou_fosse_septiques
    national_label_en: Chasse d'eau avec egouts ou fosse septiques
    national_label_local: دافق / مراحيض
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-SAN-29
    source_category_code: flush_toilet
    national_label_en: Flush toilet
    national_label_local: دافق / مراحيض
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-SAN-30
    source_category_code: w_c_avec_chasse_eau
    national_label_en: W C avec chasse eau
    national_label_local: دافق / مراحيض
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-SAN-31
    source_category_code: w_c_moderne
    national_label_en: w.c. moderne
    national_label_local: دافق / مراحيض
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-SAN-32
    source_category_code: individual_wc
    national_label_en: Individual WC
    national_label_local: دافق خاص / مرحاض
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: NER-SAN-33
    source_category_code: individual_private_wc
    national_label_en: Individual/private WC
    national_label_local: دافق خاص / مرحاض
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: NER-SAN-34
    source_category_code: w_c_int_avec_chasse_d_eau_manuelle_rue_cour_caniveau_nature
    national_label_en: W.C. int. avec chasse d'eau/manuelle Rue/Cour/Caniveau/Nature
      + .
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > Private flush/toilet > to elsewhere
    jmp_id: flush_toilets.private_flush_toilet.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 77
  - country_entry_id: NER-SAN-35
    source_category_code: w_c_int_avec_chasse_d_eau_manuelle_egout
    national_label_en: W.C. int. avec chasse d'eau/manuelle Egout
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - country_entry_id: NER-SAN-36
    source_category_code: w_c_int_avec_chasse_d_eau_manuelle_fosse_etanche_et_sample_et_compost
    national_label_en: W.C. int. avec chasse d'eau/manuelle Fosse etanche et sample
      et compost
    national_label_local: للحفر
    jmp_classification: Flush/toilets > Private flush/toilet > to pit
    jmp_id: flush_toilets.private_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 75
  - country_entry_id: NER-SAN-37
    source_category_code: w_c_int_avec_chasse_d_eau_manuelle_fosse_septique
    national_label_en: W.C. int. avec chasse d'eau/manuelle Fosse septique
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 74
  - country_entry_id: NER-SAN-38
    source_category_code: shared_wc
    national_label_en: Shared WC
    national_label_local: عام / دافق مشترك / مرحاض
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: NER-SAN-39
    source_category_code: w_c_ext_avec_chasse_d_eau_manuelle_rue_cour_caniveau_nature_toilettes_publiques
    national_label_en: W.C. ext. avec chasse d'eau/manuelle Rue/Cour/Caniveau/Nature
      +.+toilettes publiques
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to elsewhere
    jmp_id: flush_toilets.public_shared_flush_toilet.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 83
  - country_entry_id: NER-SAN-40
    source_category_code: w_c_ext_avec_chasse_d_eau_manuelle_egout
    national_label_en: W.C. ext. avec chasse d'eau/manuelle Egout
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - country_entry_id: NER-SAN-41
    source_category_code: w_c_ext_avec_chasse_d_eau_manuelle_fosse_etanche_et_sample_et_compost_toilettes_publiques
    national_label_en: W.C. ext. avec chasse d'eau/manuelle Fosse etanche et sample
      et compost+ toilettes publiques
    national_label_local: للحفر
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to pit
    jmp_id: flush_toilets.public_shared_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 81
  - country_entry_id: NER-SAN-42
    source_category_code: w_c_ext_avec_chasse_d_eau_manuelle_toilettes_publiquesfosse_septique
    national_label_en: W.C. ext. avec chasse d'eau/manuelle + toilettes publiquesFosse
      septique
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 80
  - country_entry_id: NER-SAN-43
    source_category_code: toilettes_publiques
    national_label_en: Toilettes publiques
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to unknown place/
      not sure/DK
    jmp_id: flush_toilets.public_shared_flush_toilet.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 82
  - country_entry_id: NER-SAN-44
    source_category_code: 3_flush_elsewhere
    national_label_en: 3. flush_elsewhere
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: NER-SAN-45
    source_category_code: 4_flush_pour_flush_toilets_connected_to_elsewhere
    national_label_en: '4. Flush/pour flush toilets connected to: Elsewhere'
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: NER-SAN-46
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: NER-SAN-47
    source_category_code: reliee_a_autre_chose
    national_label_en: Reliée à autre chose
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: NER-SAN-48
    source_category_code: 1_flush_pour_flush_toilets_connected_to_piped_sewer_system
    national_label_en: '1. Flush/pour flush toilets connected to: Piped sewer system'
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: NER-SAN-49
    source_category_code: chasse_d_eau_avec_egout
    national_label_en: Chasse d'eau avec égout
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: NER-SAN-50
    source_category_code: connectee_a_un_systeme_d_egout
    national_label_en: Connectée à un système d'égout
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: NER-SAN-51
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: NER-SAN-52
    source_category_code: flush_sewer
    national_label_en: flush_sewer
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: NER-SAN-53
    source_category_code: 13_flushpit
    national_label_en: 13. flushpit
    national_label_local: للحفر
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: NER-SAN-54
    source_category_code: 3_flush_pour_flush_toilets_connected_to_pit_latrine
    national_label_en: '3. Flush/pour flush toilets connected to: Pit Latrine'
    national_label_local: للحفر
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: NER-SAN-55
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit latrine
    national_label_local: للحفر
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: NER-SAN-56
    source_category_code: reliee_a_des_latrines
    national_label_en: Reliée à des latrines
    national_label_local: للحفر
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: NER-SAN-57
    source_category_code: 2_flush_pour_flush_toilets_connected_to_septic_tank
    national_label_en: '2. Flush/pour flush toilets connected to: Septic tank'
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: NER-SAN-58
    source_category_code: 2_flush_septic
    national_label_en: 2. flush_septic
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: NER-SAN-59
    source_category_code: chasse_d_eau_fosse_septique
    national_label_en: Chasse d'eau - fosse septique
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: NER-SAN-60
    source_category_code: connecte_a_une_fosse_septique
    national_label_en: Connecte a une fosse septique
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: NER-SAN-61
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: NER-SAN-62
    source_category_code: 4_flush_unknown
    national_label_en: 4. flush_unknown
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-SAN-63
    source_category_code: 5_flush_pour_flush_toilets_connected_to_unknown_not_sure_do_not_know
    national_label_en: '5. Flush/pour flush toilets connected to: Unknown / Not sure
      / Do not know'
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-SAN-64
    source_category_code: flush_don_t_know_where
    national_label_en: Flush, don't know where
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-SAN-65
    source_category_code: reliee_a_un_endroit_inconnu_ou_nsp
    national_label_en: Reliée à un endroit inconnu ou NSP
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-SAN-66
    source_category_code: 10_bucket
    national_label_en: 10. Bucket
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: NER-SAN-67
    source_category_code: 9_bucket
    national_label_en: 9. Bucket
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: NER-SAN-68
    source_category_code: bucket_toilet
    national_label_en: Bucket toilet
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: NER-SAN-69
    source_category_code: bucket_pot
    national_label_en: Bucket/pot
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: NER-SAN-70
    source_category_code: cuvette_seau
    national_label_en: Cuvette/seau
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: NER-SAN-71
    source_category_code: seau
    national_label_en: seau
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: NER-SAN-72
    source_category_code: un_seau
    national_label_en: Un seau
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: NER-SAN-73
    source_category_code: 10_hanging
    national_label_en: 10. hanging
    national_label_local: دورة مياه معلقة / مرحاض معلق
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: NER-SAN-74
    source_category_code: 10_hanging_toilet_hanging_latrine
    national_label_en: 10. Hanging toilet /Hanging latrine
    national_label_local: دورة مياه معلقة / مرحاض معلق
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: NER-SAN-75
    source_category_code: 11_hanging_toilet_hanging_latrine
    national_label_en: 11. Hanging toilet /Hanging latrine
    national_label_local: دورة مياه معلقة / مرحاض معلق
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: NER-SAN-76
    source_category_code: des_toilettes_ou_des_latrines_suspendues
    national_label_en: Des toilettes ou des latrines suspendues
    national_label_local: دورة مياه معلقة / مرحاض معلق
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: NER-SAN-77
    source_category_code: hanging_toilet_latrine
    national_label_en: Hanging toilet/latrine
    national_label_local: دورة مياه معلقة / مرحاض معلق
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: NER-SAN-78
    source_category_code: toilette_suspendu
    national_label_en: toilette_suspendu
    national_label_local: دورة مياه معلقة / مرحاض معلق
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: NER-SAN-79
    source_category_code: toilettes_latrines_suspendues
    national_label_en: Toilettes/latrines suspendues
    national_label_local: دورة مياه معلقة / مرحاض معلق
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: NER-SAN-80
    source_category_code: autre_a_preciser
    national_label_en: Autre a preciser
    national_label_local: آخر
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: NER-SAN-81
    source_category_code: 6_pit_latrine_with_slab
    national_label_en: 6. Pit latrine with slab
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-82
    source_category_code: 6_pit_with_slab
    national_label_en: 6. pit_with_slab
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-83
    source_category_code: 7_pit_latrine_with_slab
    national_label_en: 7. Pit latrine with slab
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-84
    source_category_code: fosse_latrines_ameliorees
    national_label_en: Fosse/Latrines ameliorees
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-85
    source_category_code: fosse_dalle
    national_label_en: fosse_dalle
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-86
    source_category_code: improved_covered_latrine
    national_label_en: Improved covered latrine
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-87
    source_category_code: latrine_a_fosse_couverte
    national_label_en: Latrine a  fosse couverte
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-88
    source_category_code: latrines_a_fosse_avec_dalle
    national_label_en: Latrines à fosse avec dalle
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-89
    source_category_code: latrines_a_fosses_avec_dalle
    national_label_en: Latrines a fosses avec dalle
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-90
    source_category_code: latrines_ameliorees
    national_label_en: Latrines ameliorees
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-91
    source_category_code: latrines_ameliorees_non_couvertes
    national_label_en: Latrines améliorées non couvertes
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-92
    source_category_code: latrines_couvertes
    national_label_en: Latrines couvertes
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-93
    source_category_code: latrines_dallees_simplement
    national_label_en: Latrines dallees simplement
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-94
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-SAN-95
    source_category_code: 7_pit_latrine_without_slab_open_pit
    national_label_en: 7. Pit latrine without slab  / open pit
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-96
    source_category_code: 7_pit_no_slab
    national_label_en: 7. pit_no_slab
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-97
    source_category_code: 8_pit_latrine_without_slab_open_pit
    national_label_en: 8. Pit latrine without slab  / open pit
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-98
    source_category_code: fosse_rudimentaire_trou_court
    national_label_en: Fosse rudimentaire/trou court
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-99
    source_category_code: fosse_rudimentaire_trou_ouver
    national_label_en: Fosse rudimentaire/trou ouver
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-100
    source_category_code: fosse_sans_dalle
    national_label_en: fosse_sans_dalle
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-101
    source_category_code: latrines_a_fosse_sans_dalle
    national_label_en: Latrines à fosse sans dalle
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-102
    source_category_code: latrines_a_fosses_sans_dalle_trou_ouvert
    national_label_en: Latrines a fosses sans dalle/trou ouvert
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-103
    source_category_code: pit_latrine_without_slab
    national_label_en: Pit latrine without slab
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-104
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-105
    source_category_code: pit_open_hole
    national_label_en: Pit/open hole
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-106
    source_category_code: simple_pit
    national_label_en: Simple Pit
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-107
    source_category_code: trou_ouvert
    national_label_en: Trou ouvert
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: NER-SAN-108
    source_category_code: fosse_latrines_rudimentaires
    national_label_en: Fosse/Latrines rudimentaires
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-SAN-109
    source_category_code: improved_pit
    national_label_en: Improved Pit**
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-SAN-110
    source_category_code: improved_pits
    national_label_en: Improved Pits
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-SAN-111
    source_category_code: latrine
    national_label_en: latrine
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-SAN-112
    source_category_code: latrine_a_fosse_non_couverte
    national_label_en: Latrine a  fosse non couverte
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-SAN-113
    source_category_code: latrines_non_couvertes
    national_label_en: Latrines non couvertes
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-SAN-114
    source_category_code: latrines_sanplat_dallees_non_couvertes
    national_label_en: Latrines SANPLAT (dallees, non couvertes)
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-SAN-115
    source_category_code: latrines_traditionelles
    national_label_en: Latrines traditionelles
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-SAN-116
    source_category_code: uncovered_improved_latrine
    national_label_en: Uncovered improved latrine
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-SAN-117
    source_category_code: 5_ventilated_improved_pit_latrine
    national_label_en: 5. Ventilated improved pit latrine
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-118
    source_category_code: 5_vip
    national_label_en: 5. vip
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-119
    source_category_code: 6_ventilated_improved_pit_latrine
    national_label_en: 6. Ventilated improved pit latrine
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-120
    source_category_code: latrines_ameliorees_vip
    national_label_en: Latrines ameliorees (VIP)
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-121
    source_category_code: latrines_ameliorees_couvertes
    national_label_en: Latrines améliorées couvertes
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-122
    source_category_code: latrines_ameliorees_ventilees
    national_label_en: Latrines améliorées ventilées
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-123
    source_category_code: latrines_ventilees_ameliorees
    national_label_en: Latrines ventilées améliorées
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-124
    source_category_code: latrines_vip_dallees_ventillees
    national_label_en: Latrines VIP (dallees, ventillees)
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-125
    source_category_code: ventilated_improved_pit_vip_latrine
    national_label_en: Ventilated improved pit (VIP) latrine
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-126
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit latrine (VIP)
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: NER-SAN-127
    source_category_code: recipient_seau
    national_label_en: Recipient / Seau
    national_label_local: مرحاض دلو
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Bucket
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 126
  - country_entry_id: NER-SAN-128
    source_category_code: latrines_communautaires
    national_label_en: Latrines communautaires
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 122
  - country_entry_id: NER-SAN-129
    source_category_code: latrines_evacuation
    national_label_en: Latrines evacuation
    national_label_local: إلى مكان غير معروف / لست متأكدًا / لا أعرف
    jmp_classification: Latrines > Pour flush latrines > to unknown place/ not sure/DK
    jmp_id: latrines.pour_flush_latrines.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 89
  - country_entry_id: NER-SAN-130
    source_category_code: 12_bush
    national_label_en: 12. bush
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-131
    source_category_code: 12_no_facility_bush_field
    national_label_en: 12. No facility / bush / field
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-132
    source_category_code: 13_no_facility_bush_field
    national_label_en: 13. No facility / bush / field
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-133
    source_category_code: aucun
    national_label_en: aucun
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-134
    source_category_code: aucun_plein_air
    national_label_en: Aucun (plein air)
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-135
    source_category_code: aucune_toilette_dans_la_nature
    national_label_en: Aucune toilette (dans la nature)
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-136
    source_category_code: brousse
    national_label_en: brousse
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-137
    source_category_code: nature_brousse
    national_label_en: Nature/brousse
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-138
    source_category_code: no_facilities
    national_label_en: No Facilities
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-139
    source_category_code: no_facility_bush_field
    national_label_en: No facility/bush/field
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-140
    source_category_code: no_toilet_outside
    national_label_en: No toilet(outside)
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-141
    source_category_code: no_none_available
    national_label_en: No, none available
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-142
    source_category_code: non_pas_disponible
    national_label_en: Non, pas disponible
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-143
    source_category_code: open_defecation
    national_label_en: Open defecation
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-144
    source_category_code: pas_de_toilettes_buissons_nature
    national_label_en: Pas de toilettes / buissons / nature
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-145
    source_category_code: pas_de_toilettes_ou_brousse_ou_champs
    national_label_en: Pas de toilettes ou brousse ou champs
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-146
    source_category_code: pas_de_toilettes_nature
    national_label_en: Pas de toilettes, nature
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-147
    source_category_code: pas_de_toilettes_nature
    national_label_en: Pas de toilettes/Nature
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-148
    source_category_code: pas_de_toilettes_nature_defecation_a_l_air_libre
    national_label_en: Pas de toilettes/Nature (défécation à l'air libre)
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: NER-SAN-149
    source_category_code: community_latrines
    national_label_en: Community latrines
    national_label_local: آخر
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: NER-SAN-150
    source_category_code: other
    national_label_en: Other
    national_label_local: آخر
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: NER-SAN-151
    source_category_code: latrines_ameliorees
    national_label_en: Latrines améliorées
    national_label_local: آخر
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 133
  - country_entry_id: NER-SAN-152
    source_category_code: latrines_amelora_es
    national_label_en: Latrines amelorÃ©es
    national_label_local: آخر
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 133
  - country_entry_id: NER-SAN-153
    source_category_code: 11_other
    national_label_en: 11. other
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: NER-SAN-154
    source_category_code: 12_other
    national_label_en: 12. Other
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: NER-SAN-155
    source_category_code: autre
    national_label_en: autre
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: NER-SAN-156
    source_category_code: autre_precisez
    national_label_en: Autre, precisez
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: NER-SAN-157
    source_category_code: autres
    national_label_en: Autres
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: NER-SAN-158
    source_category_code: latrines_non_ama_liora_es
    national_label_en: Latrines non amÃ©liorÃ©es
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: NER-SAN-159
    source_category_code: other
    national_label_en: Other
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: NER-SAN-160
    source_category_code: other_type_of_sanitation
    national_label_en: Other type of sanitation
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: NER-SAN-161
    source_category_code: other_not_defined
    national_label_en: Other/Not Defined
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: NER-SAN-162
    source_category_code: other
    national_label_en: Other
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_NER_Niger_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: NER-WAS-01
    source_category_code: source
    national_label_en: Source
    national_label_local: كل الينابيع
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: NER-WAS-02
    source_category_code: private_well
    national_label_en: Private Well
    national_label_local: خاص
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - country_entry_id: NER-WAS-03
    source_category_code: public_well_borehole
    national_label_en: Public Well/Borehole
    national_label_local: عام
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 56
  - country_entry_id: NER-WAS-04
    source_category_code: 7_water_from_spring_protected_spring
    national_label_en: '7. Water from Spring: Protected Spring'
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-05
    source_category_code: eau_de_source_source_protegee
    national_label_en: 'Eau de source : Source protégée'
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-06
    source_category_code: eau_de_source_prota_ga_e
    national_label_en: Eau de source protÃ©gÃ©e
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-07
    source_category_code: eau_de_source_protegee
    national_label_en: Eau de source protégée
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-08
    source_category_code: organized_source
    national_label_en: Organized source
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-09
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-10
    source_category_code: protected_spring_closed
    national_label_en: Protected spring (closed)
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-11
    source_category_code: source_amenage
    national_label_en: Source aménagé
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-12
    source_category_code: source_amenagee
    national_label_en: Source aménagée
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-13
    source_category_code: source_protege
    national_label_en: Source protégé
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: NER-WAS-14
    source_category_code: 5_dug_well_protected_well
    national_label_en: '5. Dug Well: Protected Well'
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-WAS-15
    source_category_code: protected_dug_well_closed_or_with_handpump
    national_label_en: Protected dug well (closed) or with handpump
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-WAS-16
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-WAS-17
    source_category_code: protected_dug_well
    national_label_en: protected_dug_well
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-WAS-18
    source_category_code: puit_protege_couvert
    national_label_en: Puit protégé/couvert
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-WAS-19
    source_category_code: puit_cimente
    national_label_en: puit_cimente
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-WAS-20
    source_category_code: puits_creuse_puits_protege
    national_label_en: 'Puits creusé : puits protégé'
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-WAS-21
    source_category_code: puits_prota_ga
    national_label_en: Puits protÃ©gÃ©
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-WAS-22
    source_category_code: puits_protege
    national_label_en: Puits protégé
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: NER-WAS-23
    source_category_code: protected_well_somewhere_else
    national_label_en: Protected well somewhere else
    national_label_local: آخر
    jmp_classification: Ground water > Protected well > Other
    jmp_id: ground_water.protected_well.other
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: NER-WAS-24
    source_category_code: puit_protege_d_ailleurs
    national_label_en: Puit protégé d'ailleurs
    national_label_local: آخر
    jmp_classification: Ground water > Protected well > Other
    jmp_id: ground_water.protected_well.other
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: NER-WAS-25
    source_category_code: covered_well_in_the_dwelling
    national_label_en: covered well in the dwelling
    national_label_local: خاص
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: NER-WAS-26
    source_category_code: puit_protege_dans_le_logemement_cour
    national_label_en: Puit protégé dans le logemement/cour
    national_label_local: خاص
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: NER-WAS-27
    source_category_code: puits_couvert_dans_la_cour_concession
    national_label_en: Puits couvert dans la cour/Concession
    national_label_local: خاص
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: NER-WAS-28
    source_category_code: covered_well_in_the_courtyard_concession
    national_label_en: covered well in the courtyard/concession
    national_label_local: عام
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 68
  - country_entry_id: NER-WAS-29
    source_category_code: puits_couvert_ailleurs
    national_label_en: Puits couvert ailleurs
    national_label_local: عام
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 68
  - country_entry_id: NER-WAS-30
    source_category_code: forage_puits_source_protege
    national_label_en: Forage/ puits/ source protégé
    national_label_local: آبار أو ينابيع محمية
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: yes
    shared_flag: no
    source_row: 46
  - country_entry_id: NER-WAS-31
    source_category_code: puits
    national_label_en: puits
    national_label_local: الآبار التقليدية
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: NER-WAS-32
    source_category_code: private_well
    national_label_en: Private Well
    national_label_local: خاص
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 63
  - country_entry_id: NER-WAS-33
    source_category_code: public_well
    national_label_en: Public Well
    national_label_local: عام
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 64
  - country_entry_id: NER-WAS-34
    source_category_code: 4_tube_well_or_borehole
    national_label_en: 4. Tube well or borehole
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-35
    source_category_code: borehole
    national_label_en: Borehole
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-36
    source_category_code: borehole_with_handpump_pump
    national_label_en: Borehole (with handpump/pump)
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-37
    source_category_code: forage
    national_label_en: Forage
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-38
    source_category_code: forage_pompe_manuelle
    national_label_en: Forage /pompe manuelle
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-39
    source_category_code: puits_a_pompe_ou_forage
    national_label_en: Puits à pompe ou forage
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-40
    source_category_code: puits_a_pompe_ou_fpmh
    national_label_en: Puits a pompe ou FPMH
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-41
    source_category_code: puits_tubulaire_ou_forage
    national_label_en: Puits tubulaire ou forage
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-42
    source_category_code: tube_well_or_borehole
    national_label_en: Tube well or borehole
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-43
    source_category_code: tubewell
    national_label_en: tubewell
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: NER-WAS-44
    source_category_code: forage_dans_la_concession
    national_label_en: Forage dans la concession
    national_label_local: خاص
    jmp_classification: Ground water > Tubewell, borehole > Private
    jmp_id: ground_water.tubewell_borehole.private
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 59
  - country_entry_id: NER-WAS-45
    source_category_code: forage_ailleurs
    national_label_en: Forage ailleurs
    national_label_local: عام
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 60
  - country_entry_id: NER-WAS-46
    source_category_code: 8_water_from_spring_unprotected_spring
    national_label_en: '8. Water from Spring: Unprotected Spring'
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: NER-WAS-47
    source_category_code: eau_de_source_source_non_protegee
    national_label_en: 'Eau de source : Source non protégée'
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: NER-WAS-48
    source_category_code: eau_de_source_non_prota_ga_e
    national_label_en: Eau de source non protÃ©gÃ©e
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: NER-WAS-49
    source_category_code: eau_de_source_non_protegee
    national_label_en: Eau de source non protégée
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: NER-WAS-50
    source_category_code: non_organized_source
    national_label_en: Non organized source
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: NER-WAS-51
    source_category_code: source_non_amenagee
    national_label_en: Source non aménagée
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: NER-WAS-52
    source_category_code: source_non_protege
    national_label_en: Source non protege
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: NER-WAS-53
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: NER-WAS-54
    source_category_code: unprotected_spring_open
    national_label_en: Unprotected spring (open)
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: NER-WAS-55
    source_category_code: 6_dug_well_unprotected_well
    national_label_en: '6. Dug Well: Unprotected Well'
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-56
    source_category_code: puit_ouvert
    national_label_en: Puit ouvert
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-57
    source_category_code: puit_trad
    national_label_en: puit_trad
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-58
    source_category_code: puits_source
    national_label_en: Puits / source
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-59
    source_category_code: puits_creuse_puits_non_protege
    national_label_en: 'Puits creusé : puits non protégé'
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-60
    source_category_code: puits_non_prota_ga
    national_label_en: Puits non protÃ©gÃ©
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-61
    source_category_code: puits_non_protege
    national_label_en: Puits non protege
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-62
    source_category_code: puits_non_protege_pluie
    national_label_en: Puits non protégé, pluie
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-63
    source_category_code: unprotected_dug_well_open
    national_label_en: Unprotected dug well (open)
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-64
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-65
    source_category_code: unprotected_dug_well
    national_label_en: unprotected_dug_well
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: NER-WAS-66
    source_category_code: open_well_somewhere_else
    national_label_en: open well somewhere else
    national_label_local: آخر
    jmp_classification: Ground water > Unprotected well > Other
    jmp_id: ground_water.unprotected_well.other
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 73
  - country_entry_id: NER-WAS-67
    source_category_code: puit_ouvert_d_ailleurs
    national_label_en: Puit ouvert d'ailleurs
    national_label_local: آخر
    jmp_classification: Ground water > Unprotected well > Other
    jmp_id: ground_water.unprotected_well.other
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 73
  - country_entry_id: NER-WAS-68
    source_category_code: open_well_in_the_dwelling
    national_label_en: open well in the dwelling
    national_label_local: خاص
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: NER-WAS-69
    source_category_code: puit_ouvert_dans_le_logemement_cour
    national_label_en: Puit ouvert dans le logemement / cour
    national_label_local: خاص
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: NER-WAS-70
    source_category_code: puits_ouvert_dans_la_cour_concession
    national_label_en: Puits ouvert dans la cour/Concession
    national_label_local: خاص
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: NER-WAS-71
    source_category_code: open_well_in_the_courtyard_concession
    national_label_en: open well in the courtyard/concession
    national_label_local: عام
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 72
  - country_entry_id: NER-WAS-72
    source_category_code: puits_ouvert_ailleurs
    national_label_en: Puits ouvert ailleurs
    national_label_local: عام
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 72
  - country_entry_id: NER-WAS-73
    source_category_code: puits_source_mare_non_protege
    national_label_en: Puits / source / mare non-protégé
    national_label_local: الآبار أو الينابيع غير المحمية
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 50
  - country_entry_id: NER-WAS-74
    source_category_code: 11_cart_with_small_tank
    national_label_en: 11. Cart with Small Tank
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: NER-WAS-75
    source_category_code: acheta_e_da_tmun_chariot_avec_un_petit_ra_servoir_ou_tambour
    national_label_en: AchetÃ©e dâ€™un chariot avec un petit rÃ©servoir ou tambour
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: NER-WAS-76
    source_category_code: achetee_d_un_chariot_avec_un_petit_reservoir_ou_tambour
    national_label_en: Achetée d’un chariot avec un petit réservoir ou tambour
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: NER-WAS-77
    source_category_code: cart
    national_label_en: cart
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: NER-WAS-78
    source_category_code: cart_with_small_tank
    national_label_en: Cart with small tank
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: NER-WAS-79
    source_category_code: charette_avec_fut
    national_label_en: Charette avec fût
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: NER-WAS-80
    source_category_code: charrette_avec_petite_citerne
    national_label_en: Charrette avec petite citerne
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: NER-WAS-81
    source_category_code: vendeurs_ambulants_garoua
    national_label_en: Vendeurs ambulants (Garoua)
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: NER-WAS-82
    source_category_code: mini_aep
    national_label_en: Mini AEP
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: NER-WAS-83
    source_category_code: vendeur_ambulant
    national_label_en: Vendeur ambulant
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: NER-WAS-84
    source_category_code: source_d_eau_ameliora_e
    national_label_en: Source d'eau ameliorÃ©e
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 104
  - country_entry_id: NER-WAS-85
    source_category_code: source_d_eau_de_boisson_amelioree
    national_label_en: Source d’eau de boisson améliorée
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 104
  - country_entry_id: NER-WAS-86
    source_category_code: achetee_d_une_citerne
    national_label_en: Achetée d’une citerne
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-87
    source_category_code: camion_citerne
    national_label_en: Camion citerne
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-88
    source_category_code: camion_vendeur
    national_label_en: Camion vendeur
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-89
    source_category_code: camion_citerne
    national_label_en: Camion-Citerne
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-90
    source_category_code: citerne_camion_vendeur
    national_label_en: Citerne / camion / vendeur
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-91
    source_category_code: eau_camion
    national_label_en: eau_camion
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-92
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-93
    source_category_code: travelling_vendors_garoua
    national_label_en: Travelling vendors(Garoua)
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-94
    source_category_code: vendeur_camion_citerne
    national_label_en: Vendeur, camion citerne
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-95
    source_category_code: vendor
    national_label_en: Vendor
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-96
    source_category_code: water_selling_cart_or_truck
    national_label_en: Water-selling cart or truck
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: NER-WAS-97
    source_category_code: autre
    national_label_en: autre
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-WAS-98
    source_category_code: autre_a_preciser
    national_label_en: Autre (à préciser)
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-WAS-99
    source_category_code: autres
    national_label_en: Autres
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-WAS-100
    source_category_code: other
    national_label_en: Other
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-WAS-101
    source_category_code: source_d_eau_non_ameliora_e
    national_label_en: Source d'eau non ameliorÃ©e
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: NER-WAS-102
    source_category_code: water_vendor
    national_label_en: Water vendor
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: NER-WAS-103
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: المياه المعبأة
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 89
  - country_entry_id: NER-WAS-104
    source_category_code: 13_bottled_water
    national_label_en: 13. Bottled Water
    national_label_local: مياه معبأة
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: NER-WAS-105
    source_category_code: bottled
    national_label_en: bottled
    national_label_local: مياه معبأة
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: NER-WAS-106
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: مياه معبأة
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: NER-WAS-107
    source_category_code: bouteille_d_eau
    national_label_en: Bouteille d' eau
    national_label_local: مياه معبأة
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: NER-WAS-108
    source_category_code: eau_en_bouiteille
    national_label_en: Eau en Bouiteille
    national_label_local: مياه معبأة
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: NER-WAS-109
    source_category_code: eau_en_bouteille
    national_label_en: Eau en bouteille
    national_label_local: مياه معبأة
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: NER-WAS-110
    source_category_code: 14_sachet_water
    national_label_en: 14. Sachet Water
    national_label_local: كيس ماء
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: NER-WAS-111
    source_category_code: eau_en_sachet
    national_label_en: Eau en sachet
    national_label_local: كيس ماء
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: NER-WAS-112
    source_category_code: sachet
    national_label_en: sachet
    national_label_local: كيس ماء
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: NER-WAS-113
    source_category_code: water_sachets
    national_label_en: Water sachets
    national_label_local: كيس ماء
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: NER-WAS-114
    source_category_code: 9_rainwater
    national_label_en: 9. Rainwater
    national_label_local: مياه الأمطار
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: NER-WAS-115
    source_category_code: 9_rainwater
    national_label_en: 9. Rainwater
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: NER-WAS-116
    source_category_code: collecte_d_eau_de_pluie
    national_label_en: Collecte d’eau de pluie
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: NER-WAS-117
    source_category_code: eau_de_pluie
    national_label_en: Eau de pluie
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: NER-WAS-118
    source_category_code: rain_water
    national_label_en: Rain water
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: NER-WAS-119
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: NER-WAS-120
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: NER-WAS-121
    source_category_code: 12_surface_water
    national_label_en: 12. Surface water
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-122
    source_category_code: eau_de_surface
    national_label_en: Eau de surface
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-123
    source_category_code: eau_de_surface_riviere_barrage_lac_bassin_cours_d_eau_canal_canaux_d_irrigation
    national_label_en: |-
      Eau de surface (rivière / barrage / lac / bassin
      / cours d'eau / canal / canaux d'irrigation)
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-124
    source_category_code: eau_de_surface_riviere_fleuve_barrage_lac_marre_canal_canal_d_irrigati
    national_label_en: Eau de surface (rivière, fleuve, barrage, lac, marre, canal,
      canal d'irrigati
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-125
    source_category_code: eau_de_surface_riviere_barrage_lac_bassin_cours_d_eau_canal_canaux_d_irrigation
    national_label_en: |-
      Eau de surface (rivière/ barrage/ lac/ bassin
      /cours d’eau /canal / canaux d’irrigation)
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-126
    source_category_code: eau_de_surface_telle_que_rivia_re_barrage_lac_a_tang_ruisseau_canal_ou_canaux_da_tmirrigation
    national_label_en: Eau de surface, telle que riviÃ¨re, barrage, lac, Ã©tang, ruisseau,
      canal ou canaux dâ€™irrigation
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-127
    source_category_code: eau_de_surface_telle_que_riviere_barrage_lac_etang_ruisseau_canal_ou_canaux_d_irrigation
    national_label_en: Eau de surface, telle que rivière, barrage, lac, étang, ruisseau,
      canal ou canaux d’irrigation
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-128
    source_category_code: eau_surface
    national_label_en: eau_surface
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-129
    source_category_code: fleuve_riviere_lac_barrage
    national_label_en: Fleuve/Rivière/Lac/Barrage
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-130
    source_category_code: fleuve_riviere_lac_barrage_eau_de_pluie
    national_label_en: Fleuve/Rivière/Lac/Barrage/Eau de pluie
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-131
    source_category_code: fleuve_rivieres
    national_label_en: fleuve/rivieres
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-132
    source_category_code: river_dam_lake_ponds_stream_canal_irrigation_channel
    national_label_en: River/dam/lake/ponds/stream/canal/irrigation channel
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-133
    source_category_code: river_lake_dam
    national_label_en: River/lake/dam
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-134
    source_category_code: riviere_lac_mare
    national_label_en: Rivière, lac, mare
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-135
    source_category_code: riviere_source_lac_reservoir_mare
    national_label_en: Riviere/source + Lac/reservoir/mare
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-136
    source_category_code: spring_river_pond
    national_label_en: Spring/River/Pond
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-137
    source_category_code: surface_water
    national_label_en: Surface Water
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-138
    source_category_code: surface_water_pond_river_stream
    national_label_en: Surface water (pond/river/stream)
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-139
    source_category_code: surface_water
    national_label_en: surface_water
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: NER-WAS-140
    source_category_code: barrage
    national_label_en: Barrage
    national_label_local: سد
    jmp_classification: Surface water > Dam
    jmp_id: surface_water.dam
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 95
  - country_entry_id: NER-WAS-141
    source_category_code: mare_lac
    national_label_en: Mare/Lac
    national_label_local: بحيرة
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 94
  - country_entry_id: NER-WAS-142
    source_category_code: fleuve_rviere
    national_label_en: fleuve/rviere
    national_label_local: نهر
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: NER-WAS-143
    source_category_code: branchement_prive
    national_label_en: branchement_prive
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: NER-WAS-144
    source_category_code: neighbor_s_tap
    national_label_en: Neighbor's tap
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: NER-WAS-145
    source_category_code: piped_to_neighbor
    national_label_en: Piped to neighbor
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: NER-WAS-146
    source_category_code: pompe_eau_electrique
    national_label_en: Pompe eau electrique
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: NER-WAS-147
    source_category_code: robinet_du_voisin
    national_label_en: Robinet du voisin
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: NER-WAS-148
    source_category_code: branch_personnel
    national_label_en: branch. personnel
    national_label_local: اتصالات المنزل
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: NER-WAS-149
    source_category_code: piped_water_system_in_the_psu_ea
    national_label_en: Piped water system in the PSU/EA
    national_label_local: اتصالات المنزل
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: NER-WAS-150
    source_category_code: private_tap
    national_label_en: Private Tap
    national_label_local: اتصالات المنزل
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: NER-WAS-151
    source_category_code: robinet_a_domicile
    national_label_en: Robinet a domicile
    national_label_local: اتصالات المنزل
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: NER-WAS-152
    source_category_code: robinet_dans_le_logement_conc
    national_label_en: Robinet dans le logement/conc.
    national_label_local: اتصالات المنزل
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: NER-WAS-153
    source_category_code: 1_piped_water_piped_into_dwelling_indoor
    national_label_en: '1. Piped Water: Piped into dwelling/indoor'
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-154
    source_category_code: dans_le_logement
    national_label_en: Dans le logement
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-155
    source_category_code: eau_courante
    national_label_en: Eau courante
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-156
    source_category_code: eau_du_robinet_dans_le_logement
    national_label_en: Eau du Robinet dans le logement
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-157
    source_category_code: eau_du_robinet_robinet_dans_le_logement_a_l_interieur
    national_label_en: |-
      Eau du robinet: Robinet dans le logement/à
      l’intérieur
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-158
    source_category_code: inside_the_dwelling
    national_label_en: Inside the dwelling
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-159
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-160
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-161
    source_category_code: piped_indoor
    national_label_en: piped_indoor
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-162
    source_category_code: robinet_dans_la_maison
    national_label_en: Robinet dans la maison
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-163
    source_category_code: robinet_dans_le_logement
    national_label_en: Robinet dans le logement
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: NER-WAS-164
    source_category_code: 2_piped_water_pipe_to_yard_plot
    national_label_en: '2. Piped Water: Pipe to yard/plot'
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-165
    source_category_code: eau_du_robinet_dans_la_cour_concession
    national_label_en: Eau du Robinet dans la cour/concession
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-166
    source_category_code: eau_du_robinet_robinet_sur_la_parcelle_a_l_exterieur
    national_label_en: |-
      Eau du robinet: Robinet sur la parcelle/à
      l’extérieur
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-167
    source_category_code: in_the_courtyard_concession
    national_label_en: In the courtyard/concession
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-168
    source_category_code: piped_to_yard_plot
    national_label_en: Piped to yard/plot
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-169
    source_category_code: piped_water_into_yard
    national_label_en: Piped water into yard
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-170
    source_category_code: piped_yard
    national_label_en: piped_yard
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-171
    source_category_code: raobinet_dans_la_concession_cours_ou_parcelle
    national_label_en: Raobinet dans la concession, cours ou parcelle
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-172
    source_category_code: robinet_dans_la_cour_dans_la_parcelle_ou_dans_la_concession
    national_label_en: Robinet dans la cour, dans la parcelle, ou dans la concession
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-173
    source_category_code: robinet_dans_la_cour_concession
    national_label_en: Robinet dans la cour/Concession
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: NER-WAS-174
    source_category_code: 3_piped_water_public_tap_standpipe
    national_label_en: '3. Piped Water: Public tap/standpipe'
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-175
    source_category_code: borne_fontaine_robinet_public
    national_label_en: Borne fontaine/Robinet public
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-176
    source_category_code: borne_fontaine
    national_label_en: borne_fontaine
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-177
    source_category_code: eau_du_robinet_fontaine_publique
    national_label_en: 'Eau du robinet: Fontaine publique'
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-178
    source_category_code: fontaine
    national_label_en: Fontaine
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-179
    source_category_code: fontaine_pub_forage
    national_label_en: fontaine pub, forage
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-180
    source_category_code: neighborhood_fountain_public_tap
    national_label_en: Neighborhood fountain/public tap
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-181
    source_category_code: piped_public
    national_label_en: piped_public
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-182
    source_category_code: public_tap
    national_label_en: Public Tap
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-183
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-184
    source_category_code: robinet_d_ailleurs
    national_label_en: Robinet d'ailleurs
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-185
    source_category_code: robinet_ou_fontaine_publique
    national_label_en: Robinet ou fontaine publique
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-186
    source_category_code: robinet_public_ext_ou_forage
    national_label_en: Robinet public ext. ou forage
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: NER-WAS-187
    source_category_code: robinet_public_borne_fontaine
    national_label_en: Robinet public/borne fontaine
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_NER_Niger_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

