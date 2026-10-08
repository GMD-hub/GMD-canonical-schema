---
country_id: CTY-AUT
iso3: AUT
schema_version: '0.2'
status: draft
country_name: AUT
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: AUT-EDU-01
    national_label_en: Kindergarten
    national_label_local: Kindergarten
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
  - country_entry_id: AUT-EDU-02
    national_label_en: Pre-primary stage (of primary school)
    national_label_local: Vorschulstufe
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
  - country_entry_id: AUT-EDU-03
    national_label_en: "Cr\xE8che"
    national_label_local: Kinderkrippe
    entry_age: 0
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
  - country_entry_id: AUT-EDU-04
    national_label_en: Primary school
    national_label_local: Volksschule, 1.-4. Schulstufe
    entry_age: 6
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - AUT-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: AUT-EDU-05
    national_label_en: Special school, stages 1-4
    national_label_local: "Sonderschule (inkl. Heilst\xE4ttenschulen), 1.-4. Schulstufe"
    entry_age: 6
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - AUT-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: AUT-EDU-06
    national_label_en: General school of own statutory right (incl. international
      schools), stages 1-4
    national_label_local: Allgemein bildende Statutschule (inkl. internationale Schulen),
      1.-4. Schulstufe
    entry_age: 6
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - AUT-EDU-06
    cum_years_status: computed
    review_flags: []
  - country_entry_id: AUT-EDU-07
    national_label_en: Primary school, stages 5-8
    national_label_local: Volksschule, Oberstufe
    entry_age: 10
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - AUT-EDU-04
    - AUT-EDU-05
    - AUT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
  - country_entry_id: AUT-EDU-08
    national_label_en: Academic secondary school, junior stage
    national_label_local: "Allgemein bildende h\xF6here Schule, Unterstufe (inkl.\
      \ \xDCbergangsstufe)"
    entry_age: 10
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - AUT-EDU-04
    - AUT-EDU-05
    - AUT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
  - country_entry_id: AUT-EDU-09
    national_label_en: Special school, stages 5-8
    national_label_local: "Sonderschule (inkl. Heilst\xE4ttenschulen), 5.-8. Schulstufe"
    entry_age: 10
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - AUT-EDU-04
    - AUT-EDU-05
    - AUT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
  - country_entry_id: AUT-EDU-10
    national_label_en: General school of own statutory right (incl. international
      schools), stages 5-8
    national_label_local: Allgemein bildende Statutschule (inkl. internationale Schulen),
      5.-8. Schulstufe
    entry_age: 10
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - AUT-EDU-04
    - AUT-EDU-05
    - AUT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
  - country_entry_id: AUT-EDU-11
    national_label_en: New secondary school
    national_label_local: Neue Mittelschule
    entry_age: 10
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - AUT-EDU-04
    - AUT-EDU-05
    - AUT-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
  - country_entry_id: AUT-EDU-12
    national_label_en: Academic secondary school, senior stage
    national_label_local: "Allgemeinbildende h\xF6here Schule, Oberstufe"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-13
    national_label_en: Academic secondary school for adults
    national_label_local: "Allgemein bildende h\xF6here Schule f\xFCr Berufst\xE4\
      tige"
    entry_age: 17
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - AUT-EDU-13
    cum_years_status: computed
    review_flags: []
  - country_entry_id: AUT-EDU-14
    national_label_en: General school of own statutory right (incl. international
      schools), stages 9 and higher
    national_label_local: "Allgemein bildende Statutschule (inkl. internationale Schulen),\
      \ 9. Schulstufe und h\xF6her"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-15
    national_label_en: Higher technical and vocational college, grades 1-3
    national_label_local: "Berufsbildende h\xF6here Schule, Jahrgang 1-3"
    entry_age: 14
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-16
    national_label_en: Intermediate technical and vocational school
    national_label_local: Berufsbildende mittlere Schule
    entry_age: 14
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-17
    national_label_en: Vocational school for agriculture and forestry
    national_label_local: Land- und forstwirtschaftliche mittlere Schule
    entry_age: 14
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 11
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-18
    national_label_en: Apprenticeship
    national_label_local: Lehre (Duale Ausbildung)
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-19
    national_label_en: One-year and two-year home-economic school and other short
      courses
    national_label_local: Haushaltungs-, Hauswirtschaftsschule und andere kurze Ausbildungen
    entry_age: 14
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 9
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-20
    national_label_en: Pre-vocational school
    national_label_local: Polytechnische Schule
    entry_age: 14
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 24
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 9
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-21
    national_label_en: Course for assistent nursing
    national_label_local: Pflegeassistenz-Ausbildung
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 25
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 9
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-22
    national_label_en: Training of physical educators
    national_label_local: Ausbildung von Leibeserziehern und Sportlehrern
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 26
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-23
    national_label_en: Private school of own statutory right (as not allocated otherwise)
    national_label_local: Berufsbildende Statutschule (soweit nicht anders zugeordnet)
    entry_age: 14
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 27
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-24
    national_label_en: Advanced training of emergency medical technicians
    national_label_local: "Notfallsanit\xE4terausbildung"
    entry_age: 17
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 28
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-25
    national_label_en: Professional module for emergency medical technicians
    national_label_local: "Santit\xE4ter: Berufsmodul"
    entry_age: 18
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 29
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-26
    national_label_en: Massage therapists, basic modules (medical masseur)
    national_label_local: "Ausbildung f\xFCr medizinische Masseure"
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 30
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 9
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-27
    national_label_en: Massage therapists, advanced course (therapeutic masseur)
    national_label_local: "Ausbildung f\xFCr Heilmasseure"
    entry_age: 18
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 31
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-28
    national_label_en: Course for medical assistant professions
    national_label_local: "Ausbildung f\xFCr medizinische Assistenzberufe"
    entry_age: 15
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 32
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-29
    national_label_en: School for qualified medical assistants
    national_label_local: "Ausbildung f\xFCr medizinische Fachassistenz"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 33
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-30
    national_label_en: School for qualified assistant nursing
    national_label_local: Ausbildung in der Pflegefachassistenz
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 34
    parent_country_entry_ids:
    - AUT-EDU-07
    - AUT-EDU-08
    - AUT-EDU-09
    - AUT-EDU-10
    - AUT-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
  - country_entry_id: AUT-EDU-31
    national_label_en: School for qualified nursing care
    national_label_local: "Schule f\xFCr Gesundheits- und Krankenpflege"
    entry_age: 16
    duration_years: 3
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 35
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 11
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-32
    national_label_en: Specific training in the field of nursing
    national_label_local: "Sonderausbildung im gehobenen Dienst f\xFCr Gesundheits-\
      \ und Krankenpflege"
    entry_age: 19
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 36
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-33
    national_label_en: Private school of own statutory right, courses, (as not allocated
      otherwise)
    national_label_local: "Berufsbildende Statutschule und Lehrg\xE4nge (soweit nicht\
      \ anders zugeordnet)"
    entry_age: 18
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 37
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 8
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-34
    national_label_en: School for master craftsmen
    national_label_local: Meisterschule
    entry_age: 18
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 38
    parent_country_entry_ids:
    - AUT-EDU-39
    cum_years_schooling: 12
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-39
    - AUT-EDU-34
    cum_years_status: computed
    review_flags: &id001
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-35
    national_label_en: School for foremen and building workers
    national_label_local: Werkmeister- und Bauhandwerkerschule
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-36
    national_label_en: Post-secondary course in TVE (Technical and Vocational Education)
    national_label_local: Kolleg
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 40
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-37
    national_label_en: University course (for upper secondary graduates)
    national_label_local: "Universit\xE4rer Lehrgang (Maturaniveau)"
    entry_age: 18
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 41
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 9
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-37
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-38
    national_label_en: Post-secondary college
    national_label_local: Akademie, Erstausbildung
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 42
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 11
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-38
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-39
    national_label_en: Bachelor programme
    national_label_local: Bachelorstudium
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 43
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 11
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-39
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AUT-EDU-40
    national_label_en: Master programme
    national_label_local: Masterstudium
    entry_age: 21
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 44
    parent_country_entry_ids:
    - AUT-EDU-39
    cum_years_schooling: 12
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-39
    - AUT-EDU-40
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: AUT-EDU-41
    national_label_en: Diploma programme
    national_label_local: Diplomstudium
    entry_age: 18
    duration_years: 4
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 45
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 12
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-41
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-42
    national_label_en: University course (at post-graduate level)
    national_label_local: "Universit\xE4rer Lehrgang (postgradual)"
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 46
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-42
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-43
    national_label_en: Add-on course
    national_label_local: Aufbaulehrgang
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 47
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-43
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-44
    national_label_en: Higher technical and vocational college for working people
    national_label_local: "Berufsbildende h\xF6here Schule f\xFCr Berufst\xE4tige"
    entry_age: 17
    duration_years: 4
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 48
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 12
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-44
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-45
    national_label_en: Higher technical and vocational college, grades 4-5
    national_label_local: "Berufsbildende h\xF6here Schule, Jahrgang 4-5"
    entry_age: 17
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 49
    parent_country_entry_ids:
    - AUT-EDU-12
    - AUT-EDU-14
    - AUT-EDU-18
    - AUT-EDU-19
    - AUT-EDU-21
    - AUT-EDU-22
    - AUT-EDU-23
    - AUT-EDU-24
    - AUT-EDU-25
    - AUT-EDU-26
    - AUT-EDU-27
    - AUT-EDU-28
    - AUT-EDU-29
    - AUT-EDU-30
    cum_years_schooling: 10
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-45
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
  - country_entry_id: AUT-EDU-46
    national_label_en: Doctorate
    national_label_local: Doktoratstudium (postgradual)
    entry_age: 23
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 50
    parent_country_entry_ids:
    - AUT-EDU-40
    - AUT-EDU-41
    - AUT-EDU-42
    cum_years_schooling: 13
    cum_years_computation_path:
    - AUT-EDU-04
    - AUT-EDU-07
    - AUT-EDU-24
    - AUT-EDU-42
    - AUT-EDU-46
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: AUT-EDU-04, AUT-EDU-05, AUT-EDU-06'
    - 'minimum parent path selected from: AUT-EDU-07, AUT-EDU-08, AUT-EDU-09, AUT-EDU-10,
      AUT-EDU-11'
    - 'minimum parent path selected from: AUT-EDU-12, AUT-EDU-14, AUT-EDU-18, AUT-EDU-19,
      AUT-EDU-21, AUT-EDU-22, AUT-EDU-23, AUT-EDU-24, AUT-EDU-25, AUT-EDU-26, AUT-EDU-27,
      AUT-EDU-28, AUT-EDU-29, AUT-EDU-30'
    - 'minimum parent path selected from: AUT-EDU-40, AUT-EDU-41, AUT-EDU-42'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Austria.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: AUT-SUBNAT-01
    survey_labels: 1-AT1
    survey_variables: subnatid
    gmd_subnatid1: AUT_2021_NUTS1_AT1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AUT_2021_NUTS1_AT1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: AT1
    geo_nvar: NAME_LATN
    geo_name: "Ost\xF6sterreich"
    source_row: 448
  - country_entry_id: AUT-SUBNAT-02
    survey_labels: 2-AT2
    survey_variables: subnatid
    gmd_subnatid1: AUT_2021_NUTS1_AT2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AUT_2021_NUTS1_AT2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: AT2
    geo_nvar: NAME_LATN
    geo_name: "S\xFCd\xF6sterreich"
    source_row: 449
  - country_entry_id: AUT-SUBNAT-03
    survey_labels: 3-AT3
    survey_variables: subnatid
    gmd_subnatid1: AUT_2021_NUTS1_AT3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: AUT_2021_NUTS1_AT3
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: AT3
    geo_nvar: NAME_LATN
    geo_name: "West\xF6sterreich"
    source_row: 450
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 2000
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

