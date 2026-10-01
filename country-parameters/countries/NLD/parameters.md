---
country_id: CTY-NLD
iso3: NLD
schema_version: '0.2'
status: draft
country_name: NLD
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: NLD-EDU-01
    national_label_en: Private day-care centres
    national_label_local: Kinderdagverblijven
    entry_age: 3
    duration_years: 1
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
  - country_entry_id: NLD-EDU-02
    national_label_en: Pre-school education in day care centers and play groups
    national_label_local: Voorschools onderwijs
    entry_age: 2
    duration_years: 1
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
  - country_entry_id: NLD-EDU-03
    national_label_en: Pre-primary education in school settings group (class) 1 and
      2
    national_label_local: Basisonderwijs en speciaal basisonderwijs, groep 1 en 2
    entry_age: 4
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
  - country_entry_id: NLD-EDU-04
    national_label_en: Primary education group (class) 3-8
    national_label_local: Basisonderwijs en speciaal basisonderwijs, groep 3 tot en
      met 8
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
    - NLD-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: NLD-EDU-05
    national_label_en: Primary special needs education in Centres of Expertise
    national_label_local: Expertisecentra-basisonderwijs
    entry_age: 4
    duration_years: 8
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 8
    cum_years_computation_path:
    - NLD-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: NLD-EDU-06
    national_label_en: 'Vocational education: training to assistant level; (level
      1); full time school based and dual programmes'
    national_label_local: Entreeopleiding (mbo-1), voltijd bol en bbl
    entry_age: 16
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - NLD-EDU-04
    - NLD-EDU-05
    cum_years_schooling: 7
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
  - country_entry_id: NLD-EDU-07
    national_label_en: Practical  training
    national_label_local: Praktijkonderwijs
    entry_age: 12
    duration_years: 5
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - NLD-EDU-04
    - NLD-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
  - country_entry_id: NLD-EDU-08
    national_label_en: Pre-vocational secondary education (including programmes with
      prevocational content, general content and mixed content)
    national_label_local: Voorbereidend middelbaar beroepsonderwijs (VMBO) (beroepsgerichte,
      gemengde en theoretische leerwegen)
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - NLD-EDU-04
    - NLD-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
  - country_entry_id: NLD-EDU-09
    national_label_en: Junior general secondary education (first three grades of HAVO
      and VWO and combined classes)
    national_label_local: HAVO en VWO klas 1-3, en de gecombineerde AVO klassen 1-3
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - NLD-EDU-04
    - NLD-EDU-05
    cum_years_schooling: 9
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
  - country_entry_id: NLD-EDU-10
    national_label_en: Secondary special needs education in Centres of Expertise
    national_label_local: Expertisecentra-voortgezet onderwijs
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - NLD-EDU-04
    - NLD-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
  - country_entry_id: NLD-EDU-11
    national_label_en: Junior general secondary education for adults
    national_label_local: VAVO-MAVO-niveau
    entry_age: 16
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 15
    parent_country_entry_ids: []
    cum_years_schooling: 1
    cum_years_computation_path:
    - NLD-EDU-11
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: NLD-EDU-12
    national_label_en: Vocational education, basic vocational training  (level 2);
      fulltime school based programmes
    national_label_local: WEB-basisberoepsopleiding, voltijd bol
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 8
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-13
    national_label_en: Vocational education, basic vocational training  (level 2);
      fulltime dual programmes
    national_label_local: WEB-basisberoepsopleiding, voltijd bbl
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 8
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-14
    national_label_en: Vocational education, basic vocational training  (level 2);
      parttime programmes, school based
    national_label_local: WEB-basisberoepsopleiding, deeltijd bol
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 8
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-15
    national_label_en: Vocational education, professional training (level 3); fulltime
      school based programmes
    national_label_local: WEB-vakopleiding, voltijd bol
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-16
    national_label_en: Vocational education, professional training (level 3); fulltime
      dual programmes
    national_label_local: WEB-vakopleiding, voltijd bbl
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-17
    national_label_en: Vocational education, professional training (level 3); parttime
      programmes, school based
    national_label_local: WEB-vakopleiding, deeltijd bol
    entry_age: 18
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-18
    national_label_en: Vocational education, middle-management training (level 4);
      fulltime school based programmes
    national_label_local: WEB-middenkaderopleiding, voltijd bol
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-19
    national_label_en: Vocational education, middle-management training (level 4);
      fulltime dual programmes
    national_label_local: WEB-middenkaderopleiding, voltijd bbl
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-20
    national_label_en: Vocational education, middle-management training (level 4);
      parttime programmes, school based
    national_label_local: WEB-middenkaderopleiding, deeltijd bol
    entry_age: 18
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 24
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-21
    national_label_en: Senior general secondary education
    national_label_local: Klas 4-5 HAVO
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 25
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 9
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-22
    national_label_en: Senior general secondary education
    national_label_local: Klas 4-6 VWO
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 26
    parent_country_entry_ids:
    - NLD-EDU-06
    - NLD-EDU-07
    - NLD-EDU-08
    - NLD-EDU-09
    - NLD-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
  - country_entry_id: NLD-EDU-23
    national_label_en: Senior general secondary education for adults
    national_label_local: VAVO-HAVO
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 27
    parent_country_entry_ids:
    - NLD-EDU-11
    cum_years_schooling: 2
    cum_years_computation_path:
    - NLD-EDU-11
    - NLD-EDU-23
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NLD-EDU-24
    national_label_en: Senior general secondary education for adults
    national_label_local: VAVO-VWO
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 28
    parent_country_entry_ids:
    - NLD-EDU-11
    cum_years_schooling: 2
    cum_years_computation_path:
    - NLD-EDU-11
    - NLD-EDU-24
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NLD-EDU-25
    national_label_en: Associate degree programmes
    national_label_local: Associate degree opleiding
    entry_age: 20
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - NLD-EDU-21
    - NLD-EDU-22
    cum_years_schooling: 11
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-21
    - NLD-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
    - 'minimum parent path selected from: NLD-EDU-21, NLD-EDU-22'
  - country_entry_id: NLD-EDU-26
    national_label_en: Professional bachelor's degree programmes
    national_label_local: HBO bacheloropleiding
    entry_age: 17
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - NLD-EDU-21
    - NLD-EDU-22
    cum_years_schooling: 13
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-21
    - NLD-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
    - 'minimum parent path selected from: NLD-EDU-21, NLD-EDU-22'
  - country_entry_id: NLD-EDU-27
    national_label_en: Academic bachelor's degree programmes
    national_label_local: WO bacheloropleiding
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - NLD-EDU-21
    - NLD-EDU-22
    cum_years_schooling: 12
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-21
    - NLD-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
    - 'minimum parent path selected from: NLD-EDU-21, NLD-EDU-22'
  - country_entry_id: NLD-EDU-28
    national_label_en: Professional master's degree programmes
    national_label_local: HBO masteropleiding
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - NLD-EDU-26
    - NLD-EDU-27
    cum_years_schooling: 13
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-21
    - NLD-EDU-27
    - NLD-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
    - 'minimum parent path selected from: NLD-EDU-21, NLD-EDU-22'
    - 'minimum parent path selected from: NLD-EDU-26, NLD-EDU-27'
  - country_entry_id: NLD-EDU-29
    national_label_en: Academic master's degree programmes
    national_label_local: WO masteropleiding
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - NLD-EDU-26
    - NLD-EDU-27
    cum_years_schooling: 13
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-21
    - NLD-EDU-27
    - NLD-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
    - 'minimum parent path selected from: NLD-EDU-21, NLD-EDU-22'
    - 'minimum parent path selected from: NLD-EDU-26, NLD-EDU-27'
  - country_entry_id: NLD-EDU-30
    national_label_en: Research assistants
    national_label_local: Assistenten in opleiding (aio's)
    entry_age: 0
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 34
    parent_country_entry_ids:
    - NLD-EDU-28
    - NLD-EDU-29
    cum_years_schooling: 17
    cum_years_computation_path:
    - NLD-EDU-04
    - NLD-EDU-06
    - NLD-EDU-21
    - NLD-EDU-27
    - NLD-EDU-28
    - NLD-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NLD-EDU-04, NLD-EDU-05'
    - 'minimum parent path selected from: NLD-EDU-06, NLD-EDU-07, NLD-EDU-08, NLD-EDU-09,
      NLD-EDU-10'
    - 'minimum parent path selected from: NLD-EDU-21, NLD-EDU-22'
    - 'minimum parent path selected from: NLD-EDU-26, NLD-EDU-27'
    - 'minimum parent path selected from: NLD-EDU-28, NLD-EDU-29'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Netherlands.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

