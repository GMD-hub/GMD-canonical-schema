---
country_id: CTY-GRC
iso3: GRC
schema_version: '0.2'
status: draft
country_name: GRC
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: GRC-EDU-01
    national_label_en: Pre-primary
    national_label_local: Nipiagogio
    entry_age: 4
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
  - country_entry_id: GRC-EDU-02
    national_label_en: Special Pre-primary school
    national_label_local: Eidiko Nipiagogio
    entry_age: 4
    duration_years: 1
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
  - country_entry_id: GRC-EDU-03
    national_label_en: Elementary school (Primary)
    national_label_local: Dimotiko Scholeio
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
    - GRC-EDU-03
    cum_years_status: computed
    review_flags: []
  - country_entry_id: GRC-EDU-04
    national_label_en: Special primary school
    national_label_local: Eidiko Dimotiko Scholeio
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
    - GRC-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: GRC-EDU-05
    national_label_en: 'Gymnasium

      (Lower secondary education)'
    national_label_local: Gymnasio
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - GRC-EDU-03
    - GRC-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-05
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
  - country_entry_id: GRC-EDU-06
    national_label_en: 'Special Gymnasium

      (Lower secondary special education)'
    national_label_local: Eidiko Gymnasio
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - GRC-EDU-03
    - GRC-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
  - country_entry_id: GRC-EDU-07
    national_label_en: 'Ecclesiastical Gymnasium

      (Lower secondary education)'
    national_label_local: Ecclesiastical Gymnasio
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - GRC-EDU-03
    - GRC-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
  - country_entry_id: GRC-EDU-08
    national_label_en: Second Chance School Gymnasio
    national_label_local: Scholio Defteris Efkerias -Gymnasio
    entry_age: 18
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - GRC-EDU-03
    - GRC-EDU-04
    cum_years_schooling: 8
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
  - country_entry_id: GRC-EDU-09
    national_label_en: "Labs of Special vocational education and of special vocational\
      \ training (\u0395\u03C1\u03B3\u03B1\u03C3\u03C4\u03AE\u03C1\u03B9\u03B1 \u0395\
      \u03B9\u03B4\u03B9\u03BA\u03AE\u03C2 \u0395\u03C0\u03B1\u03B3\u03B3\u03B5\u03BB\
      \u03BC\u03B1\u03C4\u03B9\u03BA\u03AE\u03C2 \u0395\u03BA\u03C0\u03B1\u03AF\u03B4\
      \u03B5\u03C5\u03C3\u03B7\u03C2 \u03BA\u03B1\u03B9 \u039A\u03B1\u03C4\u03AC\u03C1\
      \u03C4\u03B9\u03C3\u03B7\u03C2) \n(Lower secondary special - vocational education)"
    national_label_local: "\u0395.\u0395.\u0395.\u0395.\u039A."
    entry_age: 12
    duration_years: 6
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - GRC-EDU-03
    - GRC-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
  - country_entry_id: GRC-EDU-10
    national_label_en: "SPECIAL VOCATIONAL GYMNASIUM,  PREVIOUSLY KNOWN AS T.E.E.\
      \ 1st level AND IN GREEK:TEE A \u0392\u0391\u0398\u039C\u0399\u0394\u0391\u03A3"
    national_label_local: "EIDIKO EPAGGELMATIKO GYMNASIO (previously known as \u03A4\
      \u0395\u0395 OF 1ST LEVEL) has been united with special vocational luceums and\
      \ the joint institution is called eidiko-epaggelmatiko gymnasio-lyceio"
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - GRC-EDU-03
    - GRC-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
  - country_entry_id: GRC-EDU-11
    national_label_en: 'Unified Lyceum

      (Upper secondary education)'
    national_label_local: Geniko Lykio **
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - GRC-EDU-05
    - GRC-EDU-06
    - GRC-EDU-07
    - GRC-EDU-08
    - GRC-EDU-09
    - GRC-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
  - country_entry_id: GRC-EDU-12
    national_label_en: Special Lyceum for students with SEN (Upper secondary education)
    national_label_local: Eidiko Lykio
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - GRC-EDU-05
    - GRC-EDU-06
    - GRC-EDU-07
    - GRC-EDU-08
    - GRC-EDU-09
    - GRC-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
  - country_entry_id: GRC-EDU-13
    national_label_en: 'Ecclesiastical Lyceum

      (Lower secondary education)'
    national_label_local: Ecclesiastical Lykeio
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - GRC-EDU-05
    - GRC-EDU-06
    - GRC-EDU-07
    - GRC-EDU-08
    - GRC-EDU-09
    - GRC-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
  - country_entry_id: GRC-EDU-14
    national_label_en: Technical Vocational Schools (Upper secondary education)
    national_label_local: Epagelmatiki Sxoli (EPAS)
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - GRC-EDU-05
    - GRC-EDU-06
    - GRC-EDU-07
    - GRC-EDU-08
    - GRC-EDU-09
    - GRC-EDU-10
    cum_years_schooling: 10
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
  - country_entry_id: GRC-EDU-15
    national_label_en: Special Vocational Lyceum
    national_label_local: Eidiko Epaggelmatiko Lykio
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - GRC-EDU-05
    - GRC-EDU-06
    - GRC-EDU-07
    - GRC-EDU-08
    - GRC-EDU-09
    - GRC-EDU-10
    cum_years_schooling: 12
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
  - country_entry_id: GRC-EDU-16
    national_label_en: Technical-Vocational Lyceum
    national_label_local: Epagelmatiko Lykeio (EPAL) **
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - GRC-EDU-05
    - GRC-EDU-06
    - GRC-EDU-07
    - GRC-EDU-08
    - GRC-EDU-09
    - GRC-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
  - country_entry_id: GRC-EDU-17
    national_label_en: Greek Open University (University Sector)
    national_label_local: Elliniko Anoikto Panepistimio (EAP)
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - GRC-EDU-11
    - GRC-EDU-12
    - GRC-EDU-13
    cum_years_schooling: 14
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
  - country_entry_id: GRC-EDU-18
    national_label_en: a. University (belong to university sector)
    national_label_local: a. Panepistimio
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - GRC-EDU-11
    - GRC-EDU-12
    - GRC-EDU-13
    cum_years_schooling: 15
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
  - country_entry_id: GRC-EDU-19
    national_label_en: University (belong to university sector)
    national_label_local: b. Medical schools Panepistimio University
    entry_age: 18
    duration_years: 6
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - GRC-EDU-11
    - GRC-EDU-12
    - GRC-EDU-13
    cum_years_schooling: 17
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
  - country_entry_id: GRC-EDU-20
    national_label_en: University (belong to university sector)
    national_label_local: C. VETERINARY SCIENCE -DENTISTRY, PHARMACEUTICAL schools,
      Agricultural schools,  Polytechneio
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - GRC-EDU-11
    - GRC-EDU-12
    - GRC-EDU-13
    cum_years_schooling: 16
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
  - country_entry_id: GRC-EDU-21
    national_label_en: Technological Education Institutions                                 (Technological
      Sector in Tertiary Education)
    national_label_local: Technologika Ekpedeftika Idrymata (T.E.I. ) (1) see below
      the definition of tertiary vocational education as appears in the law 4485/2017
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - GRC-EDU-11
    - GRC-EDU-12
    - GRC-EDU-13
    cum_years_schooling: 15
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
  - country_entry_id: GRC-EDU-22
    national_label_en: Higher School of Pedagogical and Technological Education
    national_label_local: ASPETE  the definition of tertiary vocational education
      as appears in the law 4485/2017
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - GRC-EDU-11
    - GRC-EDU-12
    - GRC-EDU-13
    cum_years_schooling: 16
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
  - country_entry_id: GRC-EDU-23
    national_label_en: Sxoles anoteris epaggelmatikis ekpaidefsis (AEN- Tertiary schools
      of commercial marine & schools of tourism & ekklesiastical schools)                                               Tertiary
      Education
    national_label_local: Sxoles anoteris epaggelmatikis ekpaidefsis (AEN- Tertiary
      schools of commercial marine & schools of tourism & ekklesiastical schools)
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - GRC-EDU-11
    - GRC-EDU-12
    - GRC-EDU-13
    cum_years_schooling: 14
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
  - country_entry_id: GRC-EDU-24
    national_label_en: Higher professional education - Art schools   -Not classifiable
      by level -
    national_label_local: Higher professional education - Art schools
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - GRC-EDU-11
    - GRC-EDU-12
    - GRC-EDU-13
    cum_years_schooling: 14
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
  - country_entry_id: GRC-EDU-25
    national_label_en: Greek Open University (University sector) (post-graduate studies,
      Master)
    national_label_local: Elliniko Anoikto Panepistimio (EAP)
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - GRC-EDU-17
    - GRC-EDU-18
    - GRC-EDU-19
    - GRC-EDU-20
    - GRC-EDU-21
    - GRC-EDU-22
    - GRC-EDU-23
    - GRC-EDU-24
    cum_years_schooling: 16
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
  - country_entry_id: GRC-EDU-26
    national_label_en: International Hellenic University (for post-graduate studies
      only, Master)
    national_label_local: Ellhniko Diethnes Panepistimio
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - GRC-EDU-17
    - GRC-EDU-18
    - GRC-EDU-19
    - GRC-EDU-20
    - GRC-EDU-21
    - GRC-EDU-22
    - GRC-EDU-23
    - GRC-EDU-24
    cum_years_schooling: 15
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
  - country_entry_id: GRC-EDU-27
    national_label_en: "University sector\n (post-graduate studies, Master)"
    national_label_local: a. Panepistimio
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 34
    parent_country_entry_ids:
    - GRC-EDU-17
    - GRC-EDU-18
    - GRC-EDU-19
    - GRC-EDU-20
    - GRC-EDU-21
    - GRC-EDU-22
    - GRC-EDU-23
    - GRC-EDU-24
    cum_years_schooling: 15
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
  - country_entry_id: GRC-EDU-28
    national_label_en: "University sector\n (post-graduate studies, Master)"
    national_label_local: b. Medical schools Panepistimio University
    entry_age: 24
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 35
    parent_country_entry_ids:
    - GRC-EDU-17
    - GRC-EDU-18
    - GRC-EDU-19
    - GRC-EDU-20
    - GRC-EDU-21
    - GRC-EDU-22
    - GRC-EDU-23
    - GRC-EDU-24
    cum_years_schooling: 16
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
  - country_entry_id: GRC-EDU-29
    national_label_en: 'University sector

      (post-graduate studies, Master)'
    national_label_local: C. VETERINARY SCIENCE -DENTISTRY, PHARMACEUTICAL schools,
      Agricultural schools, Polytechneio
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 36
    parent_country_entry_ids:
    - GRC-EDU-17
    - GRC-EDU-18
    - GRC-EDU-19
    - GRC-EDU-20
    - GRC-EDU-21
    - GRC-EDU-22
    - GRC-EDU-23
    - GRC-EDU-24
    cum_years_schooling: 16
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
  - country_entry_id: GRC-EDU-30
    national_label_en: 'Greek Open University

      (DOCTORAL PROGRAMME)'
    national_label_local: Elliniko Anoikto Panepistimio (EAP)
    entry_age: 0
    duration_years: 0
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 37
    parent_country_entry_ids:
    - GRC-EDU-25
    - GRC-EDU-26
    - GRC-EDU-27
    - GRC-EDU-28
    - GRC-EDU-29
    cum_years_schooling: 15
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-26
    - GRC-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
    - 'minimum parent path selected from: GRC-EDU-25, GRC-EDU-26, GRC-EDU-27, GRC-EDU-28,
      GRC-EDU-29'
  - country_entry_id: GRC-EDU-31
    national_label_en: International Hellenic University (DOCTORAL PROGRAMME)
    national_label_local: Ellhniko Diethnes Panepistimio
    entry_age: 22
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 38
    parent_country_entry_ids:
    - GRC-EDU-25
    - GRC-EDU-26
    - GRC-EDU-27
    - GRC-EDU-28
    - GRC-EDU-29
    cum_years_schooling: 18
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-26
    - GRC-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
    - 'minimum parent path selected from: GRC-EDU-25, GRC-EDU-26, GRC-EDU-27, GRC-EDU-28,
      GRC-EDU-29'
  - country_entry_id: GRC-EDU-32
    national_label_en: 'University sector

      (DOCTORAL PROGRAMME)'
    national_label_local: a. Panepistimio
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - GRC-EDU-25
    - GRC-EDU-26
    - GRC-EDU-27
    - GRC-EDU-28
    - GRC-EDU-29
    cum_years_schooling: 18
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-26
    - GRC-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
    - 'minimum parent path selected from: GRC-EDU-25, GRC-EDU-26, GRC-EDU-27, GRC-EDU-28,
      GRC-EDU-29'
  - country_entry_id: GRC-EDU-33
    national_label_en: 'University sector

      (DOCTORAL PROGRAMME)'
    national_label_local: b. Medical schools Panepistimio University
    entry_age: 6
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 40
    parent_country_entry_ids:
    - GRC-EDU-25
    - GRC-EDU-26
    - GRC-EDU-27
    - GRC-EDU-28
    - GRC-EDU-29
    cum_years_schooling: 18
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-26
    - GRC-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
    - 'minimum parent path selected from: GRC-EDU-25, GRC-EDU-26, GRC-EDU-27, GRC-EDU-28,
      GRC-EDU-29'
  - country_entry_id: GRC-EDU-34
    national_label_en: 'University sector

      (DOCTORAL PROGRAMME)'
    national_label_local: C. VETERINARY SCIENCE -DENTISTRY, PHARMACEUTICAL schools,
      Agricultural schools, Polytechneio
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 41
    parent_country_entry_ids:
    - GRC-EDU-25
    - GRC-EDU-26
    - GRC-EDU-27
    - GRC-EDU-28
    - GRC-EDU-29
    cum_years_schooling: 18
    cum_years_computation_path:
    - GRC-EDU-03
    - GRC-EDU-08
    - GRC-EDU-11
    - GRC-EDU-17
    - GRC-EDU-26
    - GRC-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: GRC-EDU-03, GRC-EDU-04'
    - 'minimum parent path selected from: GRC-EDU-05, GRC-EDU-06, GRC-EDU-07, GRC-EDU-08,
      GRC-EDU-09, GRC-EDU-10'
    - 'minimum parent path selected from: GRC-EDU-11, GRC-EDU-12, GRC-EDU-13'
    - 'minimum parent path selected from: GRC-EDU-17, GRC-EDU-18, GRC-EDU-19, GRC-EDU-20,
      GRC-EDU-21, GRC-EDU-22, GRC-EDU-23, GRC-EDU-24'
    - 'minimum parent path selected from: GRC-EDU-25, GRC-EDU-26, GRC-EDU-27, GRC-EDU-28,
      GRC-EDU-29'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Greece.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: GRC-SUBNAT-01
    survey_labels: 1-EL3
    survey_variables: subnatid
    gmd_subnatid1: GRC_2021_NUTS1_EL3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: GRC_2021_NUTS1_EL3
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: EL3
    geo_nvar: NAME_LATN
    geo_name: Attiki
    source_row: 5825
  - country_entry_id: GRC-SUBNAT-02
    survey_labels: 2-EL4
    survey_variables: subnatid
    gmd_subnatid1: GRC_2021_NUTS1_EL4
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: GRC_2021_NUTS1_EL4
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: EL4
    geo_nvar: NAME_LATN
    geo_name: Nisia Aigaiou, Kriti
    source_row: 5826
  - country_entry_id: GRC-SUBNAT-03
    survey_labels: 3-EL5
    survey_variables: subnatid
    gmd_subnatid1: GRC_2021_NUTS1_EL5
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: GRC_2021_NUTS1_EL5
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: EL5
    geo_nvar: NAME_LATN
    geo_name: "Voreia Ell\xE1da"
    source_row: 5827
  - country_entry_id: GRC-SUBNAT-04
    survey_labels: 4-EL6
    survey_variables: subnatid
    gmd_subnatid1: GRC_2021_NUTS1_EL6
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: GRC_2021_NUTS1_EL6
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: EL6
    geo_nvar: NAME_LATN
    geo_name: "Kentriki Ell\xE1da"
    source_row: 5828
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

