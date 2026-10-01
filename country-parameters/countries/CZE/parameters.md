---
country_id: CTY-CZE
iso3: CZE
schema_version: '0.2'
status: draft
country_name: CZE
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CZE-EDU-01
    national_label_en: Nursery school
    national_label_local: "Mate\u0159sk\xE1 \u0161kola"
    entry_age: 3
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
  - country_entry_id: CZE-EDU-02
    national_label_en: Preparatory classes for socially disadvantaged children
    national_label_local: "P\u0159\xEDpravn\xE9 t\u0159\xEDdy pro d\u011Bti se soci\xE1\
      ln\xEDm znev\xFDhodn\u011Bn\xEDm"
    entry_age: 6
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
  - country_entry_id: CZE-EDU-03
    national_label_en: Preparatory stage of special basic school
    national_label_local: "P\u0159\xEDpravn\xFD stupe\u0148 z\xE1kladn\xED \u0161\
      koly speci\xE1ln\xED"
    entry_age: 6
    duration_years: 3
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
  - country_entry_id: CZE-EDU-04
    national_label_en: "Basic school \u2013 1st stage"
    national_label_local: "Z\xE1kladn\xED \u0161kola \u2013 1. stupe\u0148"
    entry_age: 6
    duration_years: 5
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 5
    cum_years_computation_path:
    - CZE-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: CZE-EDU-05
    national_label_en: "Special basic school \u2013 1st stage"
    national_label_local: "Z\xE1kladn\xED \u0161kola speci\xE1ln\xED \u2013 1. stupe\u0148"
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - CZE-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: CZE-EDU-06
    national_label_en: Basic school - Home schooling (1st stage)
    national_label_local: "Z\xE1kladn\xED \u0161kola - individu\xE1ln\xED vzd\u011B\
      l\xE1v\xE1n\xED (1. stupe\u0148)"
    entry_age: 6
    duration_years: 5
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 5
    cum_years_computation_path:
    - CZE-EDU-06
    cum_years_status: computed
    review_flags: []
  - country_entry_id: CZE-EDU-07
    national_label_en: "Special basic school \u2013 1st stage - education of pupils\
      \ suffering from serious mental disability"
    national_label_local: "Z\xE1kladn\xED \u0161kola - vzd\u011Bl\xE1v\xE1n\xED \u017E\
      \xE1k\u016F s hlubok\xFDm ment\xE1ln\xEDm posti\u017Een\xEDm (1. stupe\u0148\
      )"
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 11
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - CZE-EDU-07
    cum_years_status: computed
    review_flags: []
  - country_entry_id: CZE-EDU-08
    national_label_en: "Basic school \u2013 2nd stage"
    national_label_local: "Z\xE1kladn\xED \u0161kola \u2013 2. stupe\u0148"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - CZE-EDU-04
    - CZE-EDU-05
    - CZE-EDU-06
    - CZE-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
  - country_entry_id: CZE-EDU-09
    national_label_en: 1- or 2-years special vocational school
    national_label_local: "Praktick\xE1 \u0161kola 1-2let\xE1"
    entry_age: 16
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - CZE-EDU-04
    - CZE-EDU-05
    - CZE-EDU-06
    - CZE-EDU-07
    cum_years_schooling: 6
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
  - country_entry_id: CZE-EDU-10
    national_label_en: Courses for completing basic education
    national_label_local: "Kursy pro z\xEDsk\xE1n\xED z\xE1kladn\xEDho vzd\u011Bl\xE1\
      n\xED"
    entry_age: 15
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - CZE-EDU-04
    - CZE-EDU-05
    - CZE-EDU-06
    - CZE-EDU-07
    cum_years_schooling: 6
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
  - country_entry_id: CZE-EDU-11
    national_label_en: "Special basic school \u2013 2nd stage"
    national_label_local: "Z\xE1kladn\xED \u0161kola speci\xE1ln\xED \u2013 2. stupe\u0148"
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - CZE-EDU-04
    - CZE-EDU-05
    - CZE-EDU-06
    - CZE-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
  - country_entry_id: CZE-EDU-12
    national_label_en: '"Gymnasium" - lower stage of 8-years courses (1st to 4th grade)'
    national_label_local: "8let\xE9 gymn\xE1zium - ni\u017E\u0161\xED stupe\u0148\
      \ (1.-4. ro\u010Dn\xEDk)"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - CZE-EDU-04
    - CZE-EDU-05
    - CZE-EDU-06
    - CZE-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
  - country_entry_id: CZE-EDU-13
    national_label_en: '"Gymnasium" - lower stage of 6-years courses (1st and 2nd
      grade)'
    national_label_local: "6let\xE9 gymn\xE1zium - ni\u017E\u0161\xED stupe\u0148\
      \ (1.-2. ro\u010Dn\xEDk)"
    entry_age: 13
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - CZE-EDU-04
    - CZE-EDU-05
    - CZE-EDU-06
    - CZE-EDU-07
    cum_years_schooling: 7
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
  - country_entry_id: CZE-EDU-14
    national_label_en: Conservatoire - lower stage of 8-years courses (1st to 4th
      grade)
    national_label_local: "8let\xFD obor konzervato\u0159e - 1.-4. ro\u010Dn\xEDk"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - CZE-EDU-04
    - CZE-EDU-05
    - CZE-EDU-06
    - CZE-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
  - country_entry_id: CZE-EDU-15
    national_label_en: "Special basic school \u2013 2nd stage - education of pupils\
      \ suffering from serious mental disability"
    national_label_local: "Z\xE1kladn\xED \u0161kola - vzd\u011Bl\xE1v\xE1n\xED \u017E\
      \xE1k\u016F s hlubok\xFDm ment\xE1ln\xEDm posti\u017Een\xEDm (2. stupe\u0148\
      )"
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - CZE-EDU-04
    - CZE-EDU-05
    - CZE-EDU-06
    - CZE-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
  - country_entry_id: CZE-EDU-16
    national_label_en: Basic school - Home schooling (2nd stage)
    national_label_local: "Z\xE1kladn\xED \u0161kola - individu\xE1ln\xED vzd\u011B\
      l\xE1v\xE1n\xED (2. stupe\u0148)"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - CZE-EDU-04
    - CZE-EDU-05
    - CZE-EDU-06
    - CZE-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
  - country_entry_id: CZE-EDU-17
    national_label_en: '"Gymnasium" - upper stage of 8-years courses (5th to 8th grade)'
    national_label_local: "8let\xE9 gymn\xE1zium - vy\u0161\u0161\xED stupe\u0148\
      \ (5.-8. ro\u010Dn\xEDk)"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 10
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-18
    national_label_en: '"Gymnasium" - upper stage fo 6-years courses (3rd to 6th grade)'
    national_label_local: "6let\xE9 gymn\xE1zium - vy\u0161\u0161\xED stupe\u0148\
      \ (3.-6. ro\u010Dn\xEDk)"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 10
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-19
    national_label_en: "\"Gymnasium\" \u2013 4-years courses"
    national_label_local: "4let\xE9 gymn\xE1zium"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 10
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-20
    national_label_en: Study of selected subjects
    national_label_local: "Studium jednotliv\xFDch p\u0159edm\u011Bt\u016F a ucelen\xFD\
      ch \u010D\xE1st\xED u\u010Diva"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 24
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 7
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-21
    national_label_en: Secondary education courses without maturita exam
    national_label_local: "St\u0159edn\xED vzd\u011Bl\xE1n\xED"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 25
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-22
    national_label_en: Secondary education courses with VET certificate
    national_label_local: "St\u0159edn\xED vzd\u011Bl\xE1n\xED s v\xFDu\u010Dn\xED\
      m listem"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 26
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-23
    national_label_en: Secondary technical and vocational courses with maturita exam
    national_label_local: "St\u0159edn\xED vzd\u011Bl\xE1n\xED s maturitn\xED zkou\u0161\
      kou (odborn\xE9)"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 27
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 10
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-24
    national_label_en: "Secondary education courses with VET certificate \u2013 2-years\
      \ courses"
    national_label_local: "St\u0159edn\xED vzd\u011Bl\xE1n\xED s v\xFDu\u010Dn\xED\
      m listem - 2let\xE9 obory"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 28
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 8
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-25
    national_label_en: Conservatoire - middle stage of 8-years courses (5th and 6th
      grade)
    national_label_local: "8let\xFD obor konzervato\u0159e - 5.-6. ro\u010Dn\xEDk"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 29
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 8
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-26
    national_label_en: Conservatoire - lower stage of 6-years courses (1st to 4th
      grade)
    national_label_local: "6let\xFD obor konzervato\u0159e - 1.-4. ro\u010Dn\xEDk"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 30
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 10
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-27
    national_label_en: Lyceum
    national_label_local: Lyceum
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 31
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 10
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-28
    national_label_en: Language schools with certificate of Ministry of Education
      (post-secondary courses)
    national_label_local: "Jazykov\xE1 \u0161kola (pomaturirn\xED studium)"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 8
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-29
    national_label_en: 'Universities: the second qualification for graduates from
      upper secondary education'
    national_label_local: "Dal\u0161\xED vzd\u011Bl\xE1v\xE1n\xED na vysok\xE9 \u0161\
      kole: pro absolventy S\u0160"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 8
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-30
    national_label_en: Follow-up courses (for graduates of secondary education courses
      without maturita exam or secondary education courses with VET certificate)
    national_label_local: "N\xE1stavbov\xE9 studium"
    entry_age: 18
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 34
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 8
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-31
    national_label_en: Shortened courses leading to apprenticeship certificate (second
      qualification for graduates of upper secondary education with VET certificate
      or maturita exam)
    national_label_local: "Zkr\xE1cen\xE9 studium s v\xFDu\u010Dn\xEDm listem"
    entry_age: 19
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 35
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 7
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-32
    national_label_en: Shortened courses leading to maturita exam (second qualification
      for graduates of upper secondary education with maturita exam)
    national_label_local: "Zkr\xE1cen\xE9 studium s maturitn\xED zkou\u0161kou"
    entry_age: 19
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 36
    parent_country_entry_ids:
    - CZE-EDU-08
    - CZE-EDU-09
    - CZE-EDU-10
    - CZE-EDU-11
    - CZE-EDU-12
    - CZE-EDU-13
    - CZE-EDU-14
    - CZE-EDU-15
    - CZE-EDU-16
    cum_years_schooling: 7
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
  - country_entry_id: CZE-EDU-33
    national_label_en: Courses for retraining, vocational type
    national_label_local: "Rekvalifika\u010Dn\xED kursy"
    entry_age: 18
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 37
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 7
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-34
    national_label_en: Courses for retraining, vocational type, with VET certificate
    national_label_local: "Rekvalifika\u010Dn\xED kursy s v\xFDu\u010Dn\xEDm listem"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 38
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 8
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-35
    national_label_en: Post-secondary courses, vocational type
    national_label_local: "Pomaturitn\xED studium"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 8
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-36
    national_label_en: Conservatoire - upper stage of 8-years courses (7th and 8th
      grade)
    national_label_local: "8let\xFD obor konzervato\u0159e - 7.-8. ro\u010Dn\xEDk"
    entry_age: 17
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 40
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-37
    national_label_en: Conservatoire - upper stage of 6-years (5th and 6th grade)
    national_label_local: "6let\xFD obor konzervato\u0159e - 5.-6. ro\u010Dn\xEDk"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 41
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 9
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-37
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-38
    national_label_en: Higher technical school
    national_label_local: "Vy\u0161\u0161\xED odborn\xE1 \u0161kola \u2013 3-and 4-years\
      \ courses"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 42
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 10
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-38
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-39
    national_label_en: Bachelor study
    national_label_local: "Bakal\xE1\u0159sk\xE9 studium"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 43
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 10
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-39
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-40
    national_label_en: Master study (long 5-years programmes)
    national_label_local: "Magistersk\xE9 studium (dlouh\xE9 5\u20136let\xE9 programy)"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 44
    parent_country_entry_ids:
    - CZE-EDU-38
    - CZE-EDU-39
    - CZE-EDU-42
    cum_years_schooling: 15
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-38
    - CZE-EDU-40
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
    - 'minimum parent path selected from: CZE-EDU-38, CZE-EDU-39, CZE-EDU-42'
  - country_entry_id: CZE-EDU-41
    national_label_en: Master study (short 2- to 3-years follow-up programmes)
    national_label_local: "Magistersk\xE9 navazuj\xEDc\xED studium (2\u20133let\xE9\
      )"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 45
    parent_country_entry_ids:
    - CZE-EDU-38
    - CZE-EDU-39
    - CZE-EDU-42
    cum_years_schooling: 12
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-38
    - CZE-EDU-41
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
    - 'minimum parent path selected from: CZE-EDU-38, CZE-EDU-39, CZE-EDU-42'
  - country_entry_id: CZE-EDU-42
    national_label_en: 'Universities: special courses for bachelors and graduates
      of higher technical schools'
    national_label_local: "Dal\u0161\xED vzd\u011Bl\xE1v\xE1n\xED na vysok\xE9 \u0161\
      kole: pro bakal\xE1\u0159e a absolventy VO\u0160"
    entry_age: 21
    duration_years: 6
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 46
    parent_country_entry_ids:
    - CZE-EDU-17
    - CZE-EDU-18
    - CZE-EDU-19
    - CZE-EDU-20
    - CZE-EDU-21
    - CZE-EDU-22
    - CZE-EDU-24
    - CZE-EDU-25
    - CZE-EDU-26
    - CZE-EDU-27
    - CZE-EDU-30
    - CZE-EDU-31
    - CZE-EDU-32
    cum_years_schooling: 13
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-42
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
  - country_entry_id: CZE-EDU-43
    national_label_en: 'Universities: special courses for masters'
    national_label_local: "Dal\u0161\xED vzd\u011Bl\xE1v\xE1n\xED na vysok\xE9 \u0161\
      kole: pro absolventy magistersk\xFDch studijn\xEDch programu."
    entry_age: 24
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 47
    parent_country_entry_ids:
    - CZE-EDU-38
    - CZE-EDU-39
    - CZE-EDU-42
    cum_years_schooling: 16
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-38
    - CZE-EDU-43
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
    - 'minimum parent path selected from: CZE-EDU-38, CZE-EDU-39, CZE-EDU-42'
  - country_entry_id: CZE-EDU-44
    national_label_en: Doctoral study
    national_label_local: "Doktorsk\xE9 studium"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 48
    parent_country_entry_ids:
    - CZE-EDU-40
    - CZE-EDU-41
    - CZE-EDU-43
    cum_years_schooling: 15
    cum_years_computation_path:
    - CZE-EDU-04
    - CZE-EDU-09
    - CZE-EDU-20
    - CZE-EDU-38
    - CZE-EDU-41
    - CZE-EDU-44
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CZE-EDU-04, CZE-EDU-05, CZE-EDU-06, CZE-EDU-07'
    - 'minimum parent path selected from: CZE-EDU-08, CZE-EDU-09, CZE-EDU-10, CZE-EDU-11,
      CZE-EDU-12, CZE-EDU-13, CZE-EDU-14, CZE-EDU-15, CZE-EDU-16'
    - 'minimum parent path selected from: CZE-EDU-17, CZE-EDU-18, CZE-EDU-19, CZE-EDU-20,
      CZE-EDU-21, CZE-EDU-22, CZE-EDU-24, CZE-EDU-25, CZE-EDU-26, CZE-EDU-27, CZE-EDU-30,
      CZE-EDU-31, CZE-EDU-32'
    - 'minimum parent path selected from: CZE-EDU-38, CZE-EDU-39, CZE-EDU-42'
    - 'minimum parent path selected from: CZE-EDU-40, CZE-EDU-41, CZE-EDU-43'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Czechia.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CZE-SUBNAT-01
    survey_labels: 1-CZ01
    survey_variables: subnatid
    gmd_subnatid1: CZE_2021_NUTS2_CZ01
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CZE_2021_NUTS2_CZ01
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CZ01
    geo_nvar: NAME_LATN
    geo_name: Praha
    source_row: 3327
  - country_entry_id: CZE-SUBNAT-02
    survey_labels: 2-CZ02
    survey_variables: subnatid
    gmd_subnatid1: CZE_2021_NUTS2_CZ02
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CZE_2021_NUTS2_CZ02
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CZ02
    geo_nvar: NAME_LATN
    geo_name: "St\u0159edn\xED \u010Cechy"
    source_row: 3328
  - country_entry_id: CZE-SUBNAT-03
    survey_labels: 3-CZ03
    survey_variables: subnatid
    gmd_subnatid1: CZE_2021_NUTS2_CZ03
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CZE_2021_NUTS2_CZ03
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CZ03
    geo_nvar: NAME_LATN
    geo_name: "Jihoz\xE1pad"
    source_row: 3329
  - country_entry_id: CZE-SUBNAT-04
    survey_labels: 4-CZ04
    survey_variables: subnatid
    gmd_subnatid1: CZE_2021_NUTS2_CZ04
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CZE_2021_NUTS2_CZ04
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CZ04
    geo_nvar: NAME_LATN
    geo_name: "Severoz\xE1pad"
    source_row: 3330
  - country_entry_id: CZE-SUBNAT-05
    survey_labels: 5-CZ05
    survey_variables: subnatid
    gmd_subnatid1: CZE_2021_NUTS2_CZ05
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CZE_2021_NUTS2_CZ05
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CZ05
    geo_nvar: NAME_LATN
    geo_name: "Severov\xFDchod"
    source_row: 3331
  - country_entry_id: CZE-SUBNAT-06
    survey_labels: 6-CZ06
    survey_variables: subnatid
    gmd_subnatid1: CZE_2021_NUTS2_CZ06
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CZE_2021_NUTS2_CZ06
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CZ06
    geo_nvar: NAME_LATN
    geo_name: "Jihov\xFDchod"
    source_row: 3332
  - country_entry_id: CZE-SUBNAT-07
    survey_labels: 7-CZ07
    survey_variables: subnatid
    gmd_subnatid1: CZE_2021_NUTS2_CZ07
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CZE_2021_NUTS2_CZ07
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CZ07
    geo_nvar: NAME_LATN
    geo_name: "St\u0159edn\xED Morava"
    source_row: 3333
  - country_entry_id: CZE-SUBNAT-08
    survey_labels: 8-CZ08
    survey_variables: subnatid
    gmd_subnatid1: CZE_2021_NUTS2_CZ08
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CZE_2021_NUTS2_CZ08
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CZ08
    geo_nvar: NAME_LATN
    geo_name: Moravskoslezsko
    source_row: 3334
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
  - country_entry_id: CZE-SAN-01
    source_category_code: flush_to_piped_sewage_system
    national_label_en: Flush to piped sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: CZE-SAN-02
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: CZE-SAN-03
    source_category_code: covered_dry_latrine_with_privacy
    national_label_en: Covered dry latrine (with privacy)
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: CZE-SAN-04
    source_category_code: pour_flush_latrine
    national_label_en: Pour flush latrine
    national_label_local: Pour flush latrines
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 85
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CZE_Czechia_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CZE-WAS-01
    source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: Protected wells or springs
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: true
    shared_flag: false
    source_row: 46
  - country_entry_id: CZE-WAS-02
    source_category_code: protected_tube_well_or_bore_hole
    national_label_en: Protected tube well or bore hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: CZE-WAS-03
    source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: Unprotected wells or springs
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 50
  - country_entry_id: CZE-WAS-04
    source_category_code: water_taken_directly_from_pond_water_or_stream
    national_label_en: Water taken directly from pond-water or stream
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: CZE-WAS-05
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: CZE-WAS-06
    source_category_code: public_standpipe
    national_label_en: Public standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CZE_Czechia_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

