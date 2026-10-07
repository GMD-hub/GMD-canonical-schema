---
country_id: CTY-SVN
iso3: SVN
schema_version: '0.2'
status: draft
country_name: SVN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SVN-EDU-01
    national_label_en: Pre-school education (1st age period)
    national_label_local: "Pred\u0161olska vzgoja (1.starostno obdobje)"
    entry_age: 0
    duration_years: 2
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
  - country_entry_id: SVN-EDU-02
    national_label_en: Pre-school education (2nd age period)
    national_label_local: "Pred\u0161olska vzgoja (2. starostno obdobje)"
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
  - country_entry_id: SVN-EDU-03
    national_label_en: Basic education (grades 1-6)
    national_label_local: "Osnovno\u0161olsko izobra\u017Eevanje (1.- 6. razred)"
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
    - SVN-EDU-03
    cum_years_status: computed
    review_flags: []
  - country_entry_id: SVN-EDU-04
    national_label_en: Basic education (grades 1-6), lower educational standard
    national_label_local: "Osnovno\u0161olsko izobra\u017Eevanje (1.-6. razred), ni\u017E\
      ji izobrazbeni standard"
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - SVN-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: SVN-EDU-05
    national_label_en: Special education programme (for special education needs children)
    national_label_local: "Posebni program vzgoje in izobra\u017Eevanja (za otroke\
      \ in mladostnike s posebnimi potrebami)"
    entry_age: 6
    duration_years: 20
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 20
    cum_years_computation_path:
    - SVN-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: SVN-EDU-06
    national_label_en: Basic education (grades  7-9)
    national_label_local: "Osnovno\u0161olsko izobra\u017Eevanje (7.-9. razred)"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - SVN-EDU-03
    - SVN-EDU-04
    - SVN-EDU-05
    cum_years_schooling: 9
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
  - country_entry_id: SVN-EDU-07
    national_label_en: Basic education (grades  7-9); lower educational standard
    national_label_local: "Osnovno\u0161olsko izobra\u017Eevanje (7.-9. razred), ni\u017E\
      ji izobrazbeni standard"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - SVN-EDU-03
    - SVN-EDU-04
    - SVN-EDU-05
    cum_years_schooling: 9
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
  - country_entry_id: SVN-EDU-08
    national_label_en: Short vocational upper secondary education
    national_label_local: "Ni\u017Eje poklicno izobra\u017Eevanje"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - SVN-EDU-06
    - SVN-EDU-07
    cum_years_schooling: 11
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
  - country_entry_id: SVN-EDU-09
    national_label_en: Vocational upper secondary education
    national_label_local: "Srednje poklicno izobra\u017Eevanje"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - SVN-EDU-06
    - SVN-EDU-07
    cum_years_schooling: 12
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
  - country_entry_id: SVN-EDU-10
    national_label_en: Vocational-technical upper secondary education
    national_label_local: "Poklicno-tehni\u0161ko izobra\u017Eevanja"
    entry_age: 18
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - SVN-EDU-06
    - SVN-EDU-07
    cum_years_schooling: 11
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
  - country_entry_id: SVN-EDU-11
    national_label_en: Technical upper secondary education
    national_label_local: "Srednje tehni\u0161ko in drugo strokovno izobra\u017Eevanje"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - SVN-EDU-06
    - SVN-EDU-07
    cum_years_schooling: 13
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
  - country_entry_id: SVN-EDU-12
    national_label_en: 'General upper secondary education (general: gimnazija and
      classical gimnazija; gimnazija with specialization: technical gimnazija, gimnazija
      of economics, gimnazija of art, international gimnazija)'
    national_label_local: "Srednje splo\u0161no izobra\u017Eevanje (splo\u0161na:\
      \ gimnazija in klasi\u010Dna gimnazija; strokovna: ekonomska, tehni\u0161ka,\
      \ umetni\u0161ka, mednarodna gimnazija)"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - SVN-EDU-06
    - SVN-EDU-07
    cum_years_schooling: 13
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
  - country_entry_id: SVN-EDU-13
    national_label_en: Vocational course and vocational matura
    national_label_local: Poklicni tecaj in poklicna matura
    entry_age: 19
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - SVN-EDU-06
    - SVN-EDU-07
    cum_years_schooling: 10
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
  - country_entry_id: SVN-EDU-14
    national_label_en: Matura course and general matura
    national_label_local: "Maturitetni tecaj in splo\u0161na matura"
    entry_age: 19
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - SVN-EDU-06
    - SVN-EDU-07
    cum_years_schooling: 10
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-14
    cum_years_status: computed
    review_flags: &id001
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
  - country_entry_id: SVN-EDU-15
    national_label_en: Short-cycle higher vocational education
    national_label_local: "Vi\u0161je strokovno izobra\u017Eevanje"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - SVN-EDU-14
    cum_years_schooling: 12
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-14
    - SVN-EDU-15
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SVN-EDU-16
    national_label_en: Professional study programmes (first-cycle higher education)
    national_label_local: "Visoko\u0161olsko strokovno izobra\u017Eevanje (1. bolonjska\
      \ stopnja)"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - SVN-EDU-14
    cum_years_schooling: 13
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-14
    - SVN-EDU-16
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SVN-EDU-17
    national_label_en: Academic study programmes (first cycle higher education)
    national_label_local: "Visoko\u0161olsko univerzitetno izobra\u017Eevanje (1.\
      \ bolonjska stopnja)"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - SVN-EDU-14
    cum_years_schooling: 13
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-14
    - SVN-EDU-17
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SVN-EDU-18
    national_label_en: Master's study programmes (second-cycle higher education)
    national_label_local: "Magistrsko izobra\u017Eevanje (2. bolonjska stopnja)"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - SVN-EDU-16
    - SVN-EDU-17
    cum_years_schooling: 14
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-14
    - SVN-EDU-16
    - SVN-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
    - 'minimum parent path selected from: SVN-EDU-16, SVN-EDU-17'
  - country_entry_id: SVN-EDU-19
    national_label_en: Integrated Master's study programmes (second-cycle higher education)
    national_label_local: "Magistrsko izobra\u017Eevanje (2. bolonjska stopnja); enoviti\
      \ programi"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - SVN-EDU-16
    - SVN-EDU-17
    cum_years_schooling: 18
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-14
    - SVN-EDU-16
    - SVN-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
    - 'minimum parent path selected from: SVN-EDU-16, SVN-EDU-17'
  - country_entry_id: SVN-EDU-20
    national_label_en: Doctoral study programmes (third-cycle higher education)
    national_label_local: "Doktorsko izobra\u017Eevanje (3. bolonjska stopnja"
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - SVN-EDU-18
    - SVN-EDU-19
    cum_years_schooling: 17
    cum_years_computation_path:
    - SVN-EDU-03
    - SVN-EDU-06
    - SVN-EDU-14
    - SVN-EDU-16
    - SVN-EDU-18
    - SVN-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SVN-EDU-03, SVN-EDU-04, SVN-EDU-05'
    - 'minimum parent path selected from: SVN-EDU-06, SVN-EDU-07'
    - 'minimum parent path selected from: SVN-EDU-16, SVN-EDU-17'
    - 'minimum parent path selected from: SVN-EDU-18, SVN-EDU-19'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Slovenia.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1992
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

