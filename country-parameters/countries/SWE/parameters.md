---
country_id: CTY-SWE
iso3: SWE
schema_version: '0.2'
status: draft
country_name: SWE
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SWE-EDU-01
    national_label_en: Pre-school, for children younger than 3 years
    national_label_local: "F\xF6rskola f\xF6r barn under 3 \xE5r"
    entry_age: 1
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
  - country_entry_id: SWE-EDU-02
    national_label_en: Pre-school classes
    national_label_local: "F\xF6rskoleklass"
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
  - country_entry_id: SWE-EDU-03
    national_label_en: Pre-school, for children 3 years of age or older
    national_label_local: "F\xF6rskola f\xF6r barn 3 \xE5r eller \xE4ldre"
    entry_age: 3
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
  - country_entry_id: SWE-EDU-04
    national_label_en: Compulsory school, grades 1-6.
    national_label_local: "Grundskolan, skol\xE5r 1-6."
    entry_age: 7
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
    - SWE-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: SWE-EDU-05
    national_label_en: Special school for the intellectually disabled, grades 1-6.
    national_label_local: "Grunds\xE4rskola, skol\xE5r 1-6."
    entry_age: 7
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
    - SWE-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: SWE-EDU-06
    national_label_en: Special school for pupils with impaired vision, hearing or
      speech defects, grades 1-6.
    national_label_local: "Specialskolan, skol\xE5r 1-6"
    entry_age: 7
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - SWE-EDU-06
    cum_years_status: computed
    review_flags: []
  - country_entry_id: SWE-EDU-07
    national_label_en: Swedish for immigrants
    national_label_local: "Svenskundervisning f\xF6r invandrare (SFI)"
    entry_age: 16
    duration_years: 0
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 11
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path:
    - SWE-EDU-07
    cum_years_status: computed
    review_flags: []
  - country_entry_id: SWE-EDU-08
    national_label_en: Adult education - basic adult education in reading and writing
    national_label_local: "Grundl\xE4ggande vuxenutbildning - l\xE4s- och skrivinl\xE4\
      rning (Komvux)"
    entry_age: 16
    duration_years: 0
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 12
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path:
    - SWE-EDU-08
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: SWE-EDU-09
    national_label_en: Compulsory school, grades 7-9.
    national_label_local: "Grundskolan, skol\xE5r 7-9."
    entry_age: 13
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - SWE-EDU-04
    - SWE-EDU-05
    - SWE-EDU-06
    - SWE-EDU-07
    cum_years_schooling: 3
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
  - country_entry_id: SWE-EDU-10
    national_label_en: Special school for the intellectually disabled, grades 7-9.
    national_label_local: "Grunds\xE4rskola, skol\xE5r 7-9."
    entry_age: 13
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - SWE-EDU-04
    - SWE-EDU-05
    - SWE-EDU-06
    - SWE-EDU-07
    cum_years_schooling: 3
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
  - country_entry_id: SWE-EDU-11
    national_label_en: Special school for pupils with impaired vision, hearing or
      speech defects, grades 7-10.
    national_label_local: "Specialskolan, skol\xE5r 7-10"
    entry_age: 13
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - SWE-EDU-04
    - SWE-EDU-05
    - SWE-EDU-06
    - SWE-EDU-07
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
  - country_entry_id: SWE-EDU-12
    national_label_en: Adult education - basic adult education
    national_label_local: "Grundl\xE4ggande vuxenutbildning (Komvux)"
    entry_age: 20
    duration_years: 0
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - SWE-EDU-08
    cum_years_schooling: 0
    cum_years_computation_path:
    - SWE-EDU-08
    - SWE-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SWE-EDU-13
    national_label_en: Adult education for people with intellectually disabilities,
      primary level schooling and training in sensory development, social and practical
      skills.
    national_label_local: "S\xE4rvux, grunds\xE4rskoleniv\xE5, tr\xE4ningsskoleniv\xE5"
    entry_age: 20
    duration_years: 0
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - SWE-EDU-08
    cum_years_schooling: 0
    cum_years_computation_path:
    - SWE-EDU-08
    - SWE-EDU-13
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: SWE-EDU-14
    national_label_en: Adult education for people with intellectually disabilities,  upper
      secondary level school.
    national_label_local: "S\xE4rvux,  gymnasies\xE4rskoleniv\xE5"
    entry_age: 20
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - SWE-EDU-12
    - SWE-EDU-13
    cum_years_schooling: 0
    cum_years_computation_path:
    - SWE-EDU-08
    - SWE-EDU-12
    - SWE-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-12, SWE-EDU-13'
  - country_entry_id: SWE-EDU-15
    national_label_en: Folk high school, general
    national_label_local: "Folkh\xF6gskola allm\xE4nna kurser"
    entry_age: 18
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - SWE-EDU-09
    - SWE-EDU-10
    - SWE-EDU-11
    cum_years_schooling: 3
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
  - country_entry_id: SWE-EDU-16
    national_label_en: Adult education - upper secondary vocational training programmes
    national_label_local: Vuxenutbildning - Yrkesvux (Komvux)
    entry_age: 20
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - SWE-EDU-12
    - SWE-EDU-13
    cum_years_schooling: 0
    cum_years_computation_path:
    - SWE-EDU-08
    - SWE-EDU-12
    - SWE-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-12, SWE-EDU-13'
  - country_entry_id: SWE-EDU-17
    national_label_en: Upper secondary school , introduction programs
    national_label_local: Gymnasieskolan, introduktionsprogram
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - SWE-EDU-09
    - SWE-EDU-10
    - SWE-EDU-11
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
  - country_entry_id: SWE-EDU-18
    national_label_en: Upper secondary school (vocational)
    national_label_local: Gymnasieskolan, yrkesprogram
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - SWE-EDU-09
    - SWE-EDU-10
    - SWE-EDU-11
    cum_years_schooling: 6
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
  - country_entry_id: SWE-EDU-19
    national_label_en: Upper secondary school (vocational) -apprenticeship
    national_label_local: "Gymnasieskolan, yrkesprogram - l\xE4rling"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - SWE-EDU-09
    - SWE-EDU-10
    - SWE-EDU-11
    cum_years_schooling: 6
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
  - country_entry_id: SWE-EDU-20
    national_label_en: Upper secondary school , introduction programs
    national_label_local: Gymnasieskolan, introduktionsprogram
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 24
    parent_country_entry_ids:
    - SWE-EDU-09
    - SWE-EDU-10
    - SWE-EDU-11
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
  - country_entry_id: SWE-EDU-21
    national_label_en: Upper secondary school (general)
    national_label_local: "Gymnasieskolan, h\xF6gskolef\xF6rberedande program"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 25
    parent_country_entry_ids:
    - SWE-EDU-09
    - SWE-EDU-10
    - SWE-EDU-11
    cum_years_schooling: 6
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
  - country_entry_id: SWE-EDU-22
    national_label_en: Upper secondary education for pupils with intellectually disabilities
      - national and individual programmes
    national_label_local: "Gymnasies\xE4rskolan - nationella och individuella program"
    entry_age: 16
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 26
    parent_country_entry_ids:
    - SWE-EDU-09
    - SWE-EDU-10
    - SWE-EDU-11
    cum_years_schooling: 7
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
  - country_entry_id: SWE-EDU-23
    national_label_en: Adult education - upper secondary adult education, vocational
      courses
    national_label_local: Gymnasial vuxenutbildning (Komvux), yrkeskurser
    entry_age: 20
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 27
    parent_country_entry_ids:
    - SWE-EDU-12
    - SWE-EDU-13
    cum_years_schooling: 0
    cum_years_computation_path:
    - SWE-EDU-08
    - SWE-EDU-12
    - SWE-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-12, SWE-EDU-13'
  - country_entry_id: SWE-EDU-24
    national_label_en: Adult education - upper secondary adult education, general
      courses
    national_label_local: "Gymnasial vuxenutbildning (Komvux), allm\xE4nna kurser"
    entry_age: 20
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 28
    parent_country_entry_ids:
    - SWE-EDU-12
    - SWE-EDU-13
    cum_years_schooling: 0
    cum_years_computation_path:
    - SWE-EDU-08
    - SWE-EDU-12
    - SWE-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-12, SWE-EDU-13'
  - country_entry_id: SWE-EDU-25
    national_label_en: Technical colleague, upper secondary additional technical year
    national_label_local: "Gymnasieskolan, tekniskt 4 \xE5r"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-26
    national_label_en: Arts and culture courses- short general
    national_label_local: Konst och kulturutbildningar, kort och generell
    entry_age: 19
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 3
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-27
    national_label_en: Arts and culture courses- short vocational
    national_label_local: Konst och kulturutbildningar, kort och yrkes
    entry_age: 19
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 3
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-28
    national_label_en: Other general education in universities and university colleges.
    national_label_local: "\xD6vrig generell h\xF6gskoleutbildning < 2 \xE5r"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-29
    national_label_en: Programme for Vocational Education Teacher , Programme for
      Folk High School Education Teacher
    national_label_local: "Korta l\xE4rarprogram p\xE5 grundniv\xE5"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-30
    national_label_en: Higher Vocational Education, <2 yrs
    national_label_local: "YH-utbildning, <2 \xE5r"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 34
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-31
    national_label_en: Higher Vocational education, > 2 yrs
    national_label_local: "YH-utbildning, >2 \xE5r"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 35
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 5
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-32
    national_label_en: Tertiary education 2 yrs, fine arts
    national_label_local: "H\xF6gskoleutbildning 2 \xE5r, konstn\xE4rligt h\xF6gskoleexamensprogram"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 36
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 5
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-33
    national_label_en: Tertiary education 2 yrs, general
    national_label_local: "H\xF6gskoleutbildning 2 \xE5r, generellt h\xF6gskoleexamensprogram"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 37
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 5
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-34
    national_label_en: Tertiary education 2- <3 yrs, professional
    national_label_local: "H\xF6gskoleutbildning 2-< 3 \xE5r, yrkesexamensprogram"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 38
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 5
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-35
    national_label_en: Arts and culture courses- long general
    national_label_local: "Konst och kulturutbildningar, l\xE5ng och generell"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 5
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-36
    national_label_en: Arts and culture courses- long vocational
    national_label_local: "Konst och kulturutbildningar, l\xE5ng och yrkes"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 40
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 5
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-37
    national_label_en: Tertiary education 3 yrs, Bachelor program in fine arts
    national_label_local: "H\xF6gskoleutbildning 3 \xE5r, konstn\xE4rligt kandidatexamensprogram"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 41
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 6
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-37
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-38
    national_label_en: Bachelor program 3 yrs, general
    national_label_local: "H\xF6gskoleutbildning 3 \xE5r, generellt kandidatexamensprogram"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 42
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 6
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-38
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-39
    national_label_en: Tertiary education 3-3,5 yrs, professional and academic
    national_label_local: "H\xF6gskoleutbildning 3-3,5 \xE5r, yrkesexamensprogram"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 43
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 6
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-39
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-40
    national_label_en: Tertiary education freestanding courses in first cycle
    national_label_local: "H\xF6gskoleutbildning frist\xE5ende kurser p\xE5 grundniv\xE5"
    entry_age: 19
    duration_years: 0
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 44
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 3
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-40
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-41
    national_label_en: Tertiary education 5 yrs and more, professional and academic
    national_label_local: "H\xF6gskoleutbildning 5 \xE5r och mer, yrkesexamensprogram"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 45
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 8
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-41
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-42
    national_label_en: Tertiary education, 2nd cycle, 1-1,25 yrs, professional
    national_label_local: "H\xF6gskoleutbildning, p\xE5byggnad, 1-1,25 \xE5r, yrkesexamensprogram"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 46
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-42
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-43
    national_label_en: Tertiary education, 2nd cycle, 1,5 yrs, professional
    national_label_local: "H\xF6gskoleutbildning, p\xE5byggnad, 1,5 \xE5r, yrkesexamensprogram"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 47
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-43
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-44
    national_label_en: Tertiary education, 2nd cycle, master 1 yr, general
    national_label_local: "H\xF6gskoleutbildning, 1 \xE5r, generellt magisterexamensprogram"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 48
    parent_country_entry_ids:
    - SWE-EDU-37
    - SWE-EDU-38
    - SWE-EDU-39
    - SWE-EDU-40
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-40
    - SWE-EDU-44
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
    - 'minimum parent path selected from: SWE-EDU-37, SWE-EDU-38, SWE-EDU-39, SWE-EDU-40'
  - country_entry_id: SWE-EDU-45
    national_label_en: Tertiary education, 2nd cycle, master 2 yrs, general
    national_label_local: "H\xF6gskoleutbildning, 2 \xE5r, generellt masterexamensprogram"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 49
    parent_country_entry_ids:
    - SWE-EDU-37
    - SWE-EDU-38
    - SWE-EDU-39
    - SWE-EDU-40
    cum_years_schooling: 5
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-40
    - SWE-EDU-45
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
    - 'minimum parent path selected from: SWE-EDU-37, SWE-EDU-38, SWE-EDU-39, SWE-EDU-40'
  - country_entry_id: SWE-EDU-46
    national_label_en: Tertiary education, 2nd cycle, masterprogram 1 yr, fine arts
    national_label_local: "H\xF6gskoleutbildning, 1 \xE5r, konstn\xE4rligt magisterexamensprogram."
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 50
    parent_country_entry_ids:
    - SWE-EDU-37
    - SWE-EDU-38
    - SWE-EDU-39
    - SWE-EDU-40
    cum_years_schooling: 4
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-40
    - SWE-EDU-46
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
    - 'minimum parent path selected from: SWE-EDU-37, SWE-EDU-38, SWE-EDU-39, SWE-EDU-40'
  - country_entry_id: SWE-EDU-47
    national_label_en: Tertiary education, 2nd cycle, masterprogram 2 yrs, fine arts
    national_label_local: "H\xF6gskoleutbildning, 2 \xE5r, konstn\xE4rligt masterexamensprogram"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 51
    parent_country_entry_ids:
    - SWE-EDU-37
    - SWE-EDU-38
    - SWE-EDU-39
    - SWE-EDU-40
    cum_years_schooling: 5
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-40
    - SWE-EDU-47
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
    - 'minimum parent path selected from: SWE-EDU-37, SWE-EDU-38, SWE-EDU-39, SWE-EDU-40'
  - country_entry_id: SWE-EDU-48
    national_label_en: Tertiary education 4-4,5 yrs, professional and academic
    national_label_local: "H\xF6gskoleutbildning 4-4,5 \xE5r, yrkesexamensprogram"
    entry_age: 19
    duration_years: 4
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 52
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 7
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-48
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-49
    national_label_en: Tertiary education freestanding courses in second cycle
    national_label_local: "H\xF6gskoleutbildning frist\xE5ende kurser p\xE5 avancerad\
      \ niv\xE5"
    entry_age: 22
    duration_years: 0
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 53
    parent_country_entry_ids:
    - SWE-EDU-15
    - SWE-EDU-17
    - SWE-EDU-20
    - SWE-EDU-21
    - SWE-EDU-22
    cum_years_schooling: 3
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-49
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
  - country_entry_id: SWE-EDU-50
    national_label_en: Tertiary education, 3rd cycle, general
    national_label_local: "Utbildning p\xE5 forskarniv\xE5, generell"
    entry_age: 24
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 54
    parent_country_entry_ids:
    - SWE-EDU-41
    - SWE-EDU-42
    - SWE-EDU-43
    - SWE-EDU-44
    - SWE-EDU-45
    - SWE-EDU-46
    - SWE-EDU-47
    - SWE-EDU-48
    - SWE-EDU-49
    cum_years_schooling: 7
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-49
    - SWE-EDU-50
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
    - 'minimum parent path selected from: SWE-EDU-41, SWE-EDU-42, SWE-EDU-43, SWE-EDU-44,
      SWE-EDU-45, SWE-EDU-46, SWE-EDU-47, SWE-EDU-48, SWE-EDU-49'
  - country_entry_id: SWE-EDU-51
    national_label_en: Tertiary education, 3rd cycle, fine arts
    national_label_local: "Konstn\xE4rlig utbildning p\xE5 forskarniv\xE5"
    entry_age: 24
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 55
    parent_country_entry_ids:
    - SWE-EDU-41
    - SWE-EDU-42
    - SWE-EDU-43
    - SWE-EDU-44
    - SWE-EDU-45
    - SWE-EDU-46
    - SWE-EDU-47
    - SWE-EDU-48
    - SWE-EDU-49
    cum_years_schooling: 7
    cum_years_computation_path:
    - SWE-EDU-07
    - SWE-EDU-09
    - SWE-EDU-15
    - SWE-EDU-49
    - SWE-EDU-51
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: SWE-EDU-04, SWE-EDU-05, SWE-EDU-06, SWE-EDU-07'
    - 'minimum parent path selected from: SWE-EDU-09, SWE-EDU-10, SWE-EDU-11'
    - 'minimum parent path selected from: SWE-EDU-15, SWE-EDU-17, SWE-EDU-20, SWE-EDU-21,
      SWE-EDU-22'
    - 'minimum parent path selected from: SWE-EDU-41, SWE-EDU-42, SWE-EDU-43, SWE-EDU-44,
      SWE-EDU-45, SWE-EDU-46, SWE-EDU-47, SWE-EDU-48, SWE-EDU-49'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Sweden.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: SWE-SUBNAT-01
    survey_labels: 1-SE1
    survey_variables: subnatid
    gmd_subnatid1: SWE_2021_NUTS1_SE1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SWE_2021_NUTS1_SE1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: SE1
    geo_nvar: NAME_LATN
    geo_name: "\xD6stra Sverige"
    source_row: 15035
  - country_entry_id: SWE-SUBNAT-02
    survey_labels: 2-SE2
    survey_variables: subnatid
    gmd_subnatid1: SWE_2021_NUTS1_SE2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SWE_2021_NUTS1_SE2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: SE2
    geo_nvar: NAME_LATN
    geo_name: "S\xF6dra Sverige"
    source_row: 15036
  - country_entry_id: SWE-SUBNAT-03
    survey_labels: 3-SE3
    survey_variables: subnatid
    gmd_subnatid1: SWE_2021_NUTS1_SE3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: SWE_2021_NUTS1_SE3
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: SE3
    geo_nvar: NAME_LATN
    geo_name: Norra Sverige
    source_row: 15037
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1990
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

