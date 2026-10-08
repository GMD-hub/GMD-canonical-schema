---
country_id: CTY-ROU
country_name: Romania
iso3: ROU
schema_version: '0.1'
status: draft
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ROU-EDU-01
    national_label_en: Early childhood and development
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt antepre\u0219colar"
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
  - country_entry_id: ROU-EDU-02
    national_label_en: Pre-primary
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt pre\u0219colar"
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
  - country_entry_id: ROU-EDU-03
    national_label_en: Primary
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt primar"
    entry_age: 6
    duration_years: 5
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 5
    cum_years_computation_path:
    - ROU-EDU-03
    cum_years_status: computed
    review_flags: []
  - country_entry_id: ROU-EDU-04
    national_label_en: Second chance - primary
    national_label_local: "Programul \"A doua \u0219ans\u0103 - \xEEnv\u0103\u021B\
      \u0103m\xE2nt primar\""
    entry_age: 10
    duration_years: 2
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 2
    cum_years_computation_path:
    - ROU-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: ROU-EDU-05
    national_label_en: Special primary education
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt primar special"
    entry_age: 6
    duration_years: 5
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 5
    cum_years_computation_path:
    - ROU-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: ROU-EDU-06
    national_label_en: Lower Secondary-gymnazium
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt gimnazial"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - ROU-EDU-03
    - ROU-EDU-04
    - ROU-EDU-05
    cum_years_schooling: 6
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
  - country_entry_id: ROU-EDU-07
    national_label_en: Special Lower Secondary - gymnazium
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt gimnazial special"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - ROU-EDU-03
    - ROU-EDU-04
    - ROU-EDU-05
    cum_years_schooling: 6
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
  - country_entry_id: ROU-EDU-08
    national_label_en: Second chance programme for lower secondary education
    national_label_local: "Programul \"A doua \u0219ans\u0103\" pentru \xEEnv\u0103\
      \u0163\u0103m\xE2ntul secundar inferior"
    entry_age: 14
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - ROU-EDU-03
    - ROU-EDU-04
    - ROU-EDU-05
    cum_years_schooling: 4
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
  - country_entry_id: ROU-EDU-09
    national_label_en: Upper Secondary-high school
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt  liceal (general)"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - ROU-EDU-06
    - ROU-EDU-07
    - ROU-EDU-08
    cum_years_schooling: 8
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
  - country_entry_id: ROU-EDU-10
    national_label_en: Upper Secondary-high school
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt  liceal (tehnologic \u0219\
      i voca\u021Bional)"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - ROU-EDU-06
    - ROU-EDU-07
    - ROU-EDU-08
    cum_years_schooling: 8
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
  - country_entry_id: ROU-EDU-11
    national_label_en: "Upper Secondary-vocational \nschool"
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt  profesional"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - ROU-EDU-06
    - ROU-EDU-07
    - ROU-EDU-08
    cum_years_schooling: 7
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
  - country_entry_id: ROU-EDU-12
    national_label_en: Second chance programme for first cycle upper secondary (vocational
      education included)
    national_label_local: "Programul \"A doua \u0219ans\u0103\" pentru primul ciclu\
      \ de \xEEnv\u0103\u0163\u0103m\xE2nt liceal / \xEEnv\u0103\u0163\u0103m\xE2\
      ntul profesional"
    entry_age: 18
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - ROU-EDU-06
    - ROU-EDU-07
    - ROU-EDU-08
    cum_years_schooling: 6
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
  - country_entry_id: ROU-EDU-13
    national_label_en: "Special Upper Secondary-vocational \nschool"
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt  profesional special"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 17
    parent_country_entry_ids:
    - ROU-EDU-06
    - ROU-EDU-07
    - ROU-EDU-08
    cum_years_schooling: 8
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
  - country_entry_id: ROU-EDU-14
    national_label_en: Post-secondary education non-tertiary
    national_label_local: "\xCEnv\u0103\u021B\u0103m\xE2nt postliceal"
    entry_age: 18
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - ROU-EDU-09
    - ROU-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-09
    - ROU-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
    - 'minimum parent path selected from: ROU-EDU-09, ROU-EDU-10'
  - country_entry_id: ROU-EDU-15
    national_label_en: Higher education. University level accredited first cycle study
      level (bachelor's degree)
    national_label_local: "Studii universitare de licen\u0163\u0103"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - ROU-EDU-09
    - ROU-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-09
    - ROU-EDU-15
    cum_years_status: computed
    review_flags: &id001
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
    - 'minimum parent path selected from: ROU-EDU-09, ROU-EDU-10'
  - country_entry_id: ROU-EDU-16
    national_label_en: Higher education. University level accredited long first degree
      study level (master's equivalent degree)
    national_label_local: "Studii universitare de licen\u0163\u0103 \u0219i master\
      \ integrat/comasat"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - ROU-EDU-15
    cum_years_schooling: 16
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-09
    - ROU-EDU-15
    - ROU-EDU-16
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ROU-EDU-17
    national_label_en: Higher education. University level accredited second cycle
      study level (master's degree).
    national_label_local: Studii universitare de master
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - ROU-EDU-15
    cum_years_schooling: 13
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-09
    - ROU-EDU-15
    - ROU-EDU-17
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: ROU-EDU-18
    national_label_en: Post-graduate studies
    national_label_local: "Studii postuniversitare; cursuri de perfec\u0163ionare\
      \ postuniversitare"
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - ROU-EDU-09
    - ROU-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-09
    - ROU-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
    - 'minimum parent path selected from: ROU-EDU-09, ROU-EDU-10'
  - country_entry_id: ROU-EDU-19
    national_label_en: Higher education / doctorate
    national_label_local: Studii universitare de doctorat
    entry_age: 22
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - ROU-EDU-16
    - ROU-EDU-17
    - ROU-EDU-18
    cum_years_schooling: 12
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-09
    - ROU-EDU-18
    - ROU-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
    - 'minimum parent path selected from: ROU-EDU-09, ROU-EDU-10'
    - 'minimum parent path selected from: ROU-EDU-16, ROU-EDU-17, ROU-EDU-18'
  - country_entry_id: ROU-EDU-20
    national_label_en: Higher education / advanced research postdoctoral training
      programmes
    national_label_local: "Post-doctorat \u0219i cercetare avansat\u0103"
    entry_age: 25
    duration_years: 1
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - ROU-EDU-16
    - ROU-EDU-17
    - ROU-EDU-18
    cum_years_schooling: 10
    cum_years_computation_path:
    - ROU-EDU-04
    - ROU-EDU-08
    - ROU-EDU-09
    - ROU-EDU-18
    - ROU-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: ROU-EDU-03, ROU-EDU-04, ROU-EDU-05'
    - 'minimum parent path selected from: ROU-EDU-06, ROU-EDU-07, ROU-EDU-08'
    - 'minimum parent path selected from: ROU-EDU-09, ROU-EDU-10'
    - 'minimum parent path selected from: ROU-EDU-16, ROU-EDU-17, ROU-EDU-18'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Romania.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: ROU-SUBNAT-01
    survey_labels: "1 \u2013 Macroregion 1 | 1-RO1"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ROU_2021_NUTS1_RO1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ROU_2021_NUTS1_RO1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: RO1
    geo_nvar: NAME_LATN
    geo_name: Macroregiunea Unu
    source_row: 13028
  - country_entry_id: ROU-SUBNAT-02
    survey_labels: "2 \u2013 Macroregion 2 | 2-RO2"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ROU_2021_NUTS1_RO2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ROU_2021_NUTS1_RO2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: RO2
    geo_nvar: NAME_LATN
    geo_name: Macroregiunea Doi
    source_row: 13029
  - country_entry_id: ROU-SUBNAT-03
    survey_labels: "3 \u2013 Macroregion 3 | 3-RO3"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ROU_2021_NUTS1_RO3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ROU_2021_NUTS1_RO3
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: RO3
    geo_nvar: NAME_LATN
    geo_name: Macroregiunea Trei
    source_row: 13030
  - country_entry_id: ROU-SUBNAT-04
    survey_labels: "4 \u2013 Macroregion 4 | 4-RO4"
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: ROU_2021_NUTS1_RO4
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ROU_2021_NUTS1_RO4
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: RO4
    geo_nvar: NAME_LATN
    geo_name: Macroregiunea Patru
    source_row: 13031
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1990
  effective_to: null
  selectors: null
  value: 16
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

No country-specific content has been supplied yet. The regional focal point
must be consulted before harmonization relies on this country layer.
