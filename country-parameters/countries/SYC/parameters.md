---
country_id: CTY-SYC
iso3: SYC
schema_version: '0.2'
status: draft
country_name: SYC
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - national_label_en: Creche
    national_label_local: Creche
    entry_age: 4
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - national_label_en: Primary
    national_label_local: Primary
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 8
  - national_label_en: Secondary 1 to 3
    national_label_local: Secondary 1 to 3
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - national_label_en: Secondary 4 to 5
    national_label_local: Secondary 4 to 5
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
  - national_label_en: Apprenticeship programmes
    national_label_local: Apprenticeship programmes
    entry_age: 16
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
  - national_label_en: Advanced Certificate (Cambridge A levels)
    national_label_local: Advanced Certificate (Cambridge A levels)
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - national_label_en: Certificate Programmes
    national_label_local: Certificate Programmes
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
  - national_label_en: Diploma Programmes
    national_label_local: Diploma Programmes
    entry_age: 18
    duration_years: 3
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - national_label_en: Advanced Diploma Programmes
    national_label_local: Advanced Diploma Programmes
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - national_label_en: Primary Teacher Training
    national_label_local: Primary Teacher Training
    entry_age: 17
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - national_label_en: Secondary Teacher Training
    national_label_local: Secondary Teacher Training
    entry_age: 19
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - national_label_en: Bachelor's degree
    national_label_local: Bachelor's degree
    entry_age: 19
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - national_label_en: Bachelor's degree
    national_label_local: Bachelor's degree
    entry_age: 19
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  - national_label_en: Post Graduate Certificate in Education
    national_label_local: Post Graduate Certificate in Education
    entry_age: 23
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
  - national_label_en: Master's Programme
    national_label_local: Master's Programme
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Seychelles.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2010
  effective_to: 2010
  selectors: ~
  value:
  - survey_labels: 1 – Central 1
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: SYC_2010_UN2_SC11
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: SYC_2010_UN2_SC11
    geo_year: '2010'
    geo_source: UN
    geo_level: '2'
    geo_idvar: ADM2_PCODE
    geo_id: SC11
    geo_nvar: ADM2_EN
    geo_name: Central 1 Mahe
    source_row: 15104
  - survey_labels: 2 – Central 2
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: SYC_2010_UN2_SC12
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: SYC_2010_UN2_SC12
    geo_year: '2010'
    geo_source: UN
    geo_level: '2'
    geo_idvar: ADM2_PCODE
    geo_id: SC12
    geo_nvar: ADM2_EN
    geo_name: Central 2 Mahe
    source_row: 15105
  - survey_labels: 3 – East/South Mahe
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: SYC_2010_UN2_SC13
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: SYC_2010_UN2_SC13
    geo_year: '2010'
    geo_source: UN
    geo_level: '2'
    geo_idvar: ADM2_PCODE
    geo_id: SC13
    geo_nvar: ADM2_EN
    geo_name: East Mahe
    source_row: 15106
  - survey_labels: 4 – West Mahe
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: SYC_2010_UN2_SC14
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: SYC_2010_UN2_SC14
    geo_year: '2010'
    geo_source: UN
    geo_level: '2'
    geo_idvar: ADM2_PCODE
    geo_id: SC14
    geo_nvar: ADM2_EN
    geo_name: West Mahe
    source_row: 15107
  - survey_labels: 5 – North Mahe
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: SYC_2010_UN2_SC15
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: SYC_2010_UN2_SC15
    geo_year: '2010'
    geo_source: UN
    geo_level: '2'
    geo_idvar: ADM2_PCODE
    geo_id: SC15
    geo_nvar: ADM2_EN
    geo_name: North Mahe
    source_row: 15108
  - survey_labels: 6 – Praslin/La Digue
    survey_variables: subnatid | subnatidsurvey
    gmd_subnatid1: SYC_2010_UNx_6
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: SYC_2010_UNx_6
    geo_year: '2010'
    geo_source: UN
    geo_level: x
    geo_idvar: sample
    geo_id: '6'
    geo_nvar: ADM2_EN
    geo_name: Praslin & La Digue
    source_row: 15109
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: ~
  selectors: ~
  value:
  - survey_labels: 1 - English River
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: SYC_2015_GAUL1_61164
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
    geo_id: '61164'
    geo_nvar: ADM1_NAME
    geo_name: English River
    source_row: 15098
  - survey_labels: 2 - Mont Buxton
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: SYC_2015_GAUL1_61183
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
    geo_id: '61183'
    geo_nvar: ADM1_NAME
    geo_name: Mont Buxton
    source_row: 15099
  - survey_labels: 3 - St Louis
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: SYC_2015_GAUL1_61200
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
    geo_id: '61200'
    geo_nvar: ADM1_NAME
    geo_name: St Louis
    source_row: 15100
  - survey_labels: 4 - Bel Air
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: SYC_2015_GAUL1_61147
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
    geo_id: '61147'
    geo_nvar: ADM1_NAME
    geo_name: Bel Air
    source_row: 15101
  - survey_labels: 5 - Mont Fleuri
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: SYC_2015_GAUL1_61184
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
    geo_id: '61184'
    geo_nvar: ADM1_NAME
    geo_name: Mont Fleuri
    source_row: 15102
  - survey_labels: 6 - Plaisance
    survey_variables: subnatid2
    gmd_subnatid1: ''
    gmd_subnatid2: SYC_2015_GAUL1_61188
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
    geo_id: '61188'
    geo_nvar: ADM1_NAME
    geo_name: Plaisance
    source_row: 15103
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

