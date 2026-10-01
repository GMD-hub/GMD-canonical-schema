---
country_id: CTY-HUN
iso3: HUN
schema_version: '0.2'
status: draft
country_name: HUN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: HUN-EDU-01
    national_label_en: Special education consulting, early development and care
    national_label_local: "Gy\xF3gypedag\xF3giai tan\xE1csad\xE1s, korai fejleszt\xE9\
      s \xE9s gondoz\xE1s"
    entry_age: 0
    duration_years: 0
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
  - country_entry_id: HUN-EDU-02
    national_label_en: Kindergarten (under 3 years)
    national_label_local: "\xD3voda (3 \xE9v alatt)"
    entry_age: 2
    duration_years: 0
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
  - country_entry_id: HUN-EDU-03
    national_label_en: Kindergarten (3 years and older)
    national_label_local: "\xD3voda (3 \xE9ves \xE9s id\u0151sebb)"
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
  - country_entry_id: HUN-EDU-04
    national_label_en: Primary school primary level (Grades 1-4) (full-time education)
    national_label_local: "\xC1ltal\xE1nos iskola  1-4. \xE9vfolyam (nappali rendszer\u0171\
      \ oktat\xE1s)"
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
    - HUN-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: HUN-EDU-05
    national_label_en: Primary school primary level (Grades 1-4) (adult literacy course)
    national_label_local: "\xC1ltal\xE1nos iskola 1-4. \xE9vfolyam (feln\u0151ttoktat\xE1\
      s)"
    entry_age: 16
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
    - HUN-EDU-05
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: HUN-EDU-06
    national_label_en: Programmes for severely disabled children (6-12 years)
    national_label_local: "Fejleszt\u0151 nevel\xE9s-oktat\xE1s (6-12 \xE9vesek)"
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
    - HUN-EDU-06
    cum_years_status: computed
    review_flags: []
  - country_entry_id: HUN-EDU-07
    national_label_en: Primary school lower secondary level (Grades 5-8), and grades
      5-8 of the upper secondary general school (full-time education)
    national_label_local: "\xC1ltal\xE1nos iskola  5-8., illetve gimn\xE1zium 5-8.,\
      \ \xE9vfolyamai (nappali rendszer\u0171 oktat\xE1s)"
    entry_age: 10
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - HUN-EDU-04
    - HUN-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
  - country_entry_id: HUN-EDU-08
    national_label_en: Primary school lower secondary level (Grades 5-8) (adult education)
    national_label_local: "\xC1ltal\xE1nos iskola 5-8. \xE9vfolyam (feln\u0151ttoktat\xE1\
      s)"
    entry_age: 16
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - HUN-EDU-05
    cum_years_schooling: 8
    cum_years_computation_path:
    - HUN-EDU-05
    - HUN-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: HUN-EDU-09
    national_label_en: Programmes for severely disabled children (13-23 years)
    national_label_local: "Fejleszt\u0151 nevel\xE9s-oktat\xE1s (13-23 \xE9vesek)"
    entry_age: 13
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - HUN-EDU-04
    - HUN-EDU-06
    cum_years_schooling: 8
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
  - country_entry_id: HUN-EDU-10
    national_label_en: Upper secondary general school (Grades 9-12(13)) (full-time
      education)
    national_label_local: "Gimn\xE1zium 9-12(13). \xE9vfolyam (nappali rendszer\u0171\
      \ oktat\xE1s)"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 12
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-11
    national_label_en: Upper secondary general school (Grades 9-12(13)) (adult education)
    national_label_local: "Gimn\xE1zium 9-12(13). \xE9vfolyam (feln\u0151ttoktat\xE1\
      s)"
    entry_age: 16
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - HUN-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - HUN-EDU-05
    - HUN-EDU-08
    - HUN-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: HUN-EDU-12
    national_label_en: Special skills development school (full-time education).
    national_label_local: "K\xE9szs\xE9gfejleszt\u0151 iskola (nappali rendszer\u0171\
      \ oktat\xE1s)"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 12
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-13
    national_label_en: Vocational school education for SEN students (full-time education)
    national_label_local: "Szakiskolai oktat\xE1s, k\xE9pz\xE9s (nappali rendszer\u0171\
      \ oktat\xE1s)"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 12
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-14
    national_label_en: Vocational school education for SEN students (adult education)
    national_label_local: "Szakiskolai oktat\xE1s, k\xE9pz\xE9s (feln\u0151ttoktat\xE1\
      s)"
    entry_age: 16
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - HUN-EDU-08
    cum_years_schooling: 12
    cum_years_computation_path:
    - HUN-EDU-05
    - HUN-EDU-08
    - HUN-EDU-14
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: HUN-EDU-15
    national_label_en: "Springboard (Dobbant\xF3) Programme"
    national_label_local: "Dobbant\xF3 Program (el\u0151k\xE9sz\xEDt\u0151 \xE9vfolyam)"
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 9
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-16
    national_label_en: School workshop programme
    national_label_local: "M\u0171helyiskola"
    entry_age: 16
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 8
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-17
    national_label_en: Career orientation development year
    national_label_local: "Orient\xE1ci\xF3s \xE9vfolyam"
    entry_age: 14
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 9
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-18
    national_label_en: Short VET Programme (full-time education)
    national_label_local: "Szakk\xE9pz\u0151 iskolai oktat\xE1s, k\xE9pz\xE9s (nappali\
      \ rendszer\u0171 oktat\xE1s)"
    entry_age: 14
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 11
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-19
    national_label_en: Short VET Programme (part-time education)
    national_label_local: "Szakk\xE9pz\u0151 iskolai oktat\xE1s, k\xE9pz\xE9s (nem\
      \ nappali oktat\xE1s)"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 11
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-20
    national_label_en: Technicum, upper secondary vocational school (Grades 9-13)
      (full-time education)
    national_label_local: "Technikum, szakgimn\xE1zium 9-13. \xE9vfolyam (nappali\
      \ rendszer\u0171 oktat\xE1s)"
    entry_age: 14
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 24
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 13
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-21
    national_label_en: Technicum, upper secondary vocational school (Grades 9-13)
      (part-time education)
    national_label_local: "Technikum, szakgimn\xE1zium 9-13. \xE9vfolyam (nem nappali\
      \ oktat\xE1s)"
    entry_age: 16
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 25
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 13
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-22
    national_label_en: Programmes preparing strictly for final examination at secondary
      level at technicums, upper secondary vocational schools
    national_label_local: "Technikum, szakgimn\xE1zium kiz\xE1r\xF3lag \xE9retts\xE9\
      gi vizsg\xE1ra felk\xE9sz\xEDt\u0151 \xE9vfolyamai"
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 26
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 10
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-23
    national_label_en: Programmes preparing strictly for vocational qualifications
      at upper secondary vocational school (not requiring maturity examination)
    national_label_local: "Szakgimn\xE1zium kiz\xE1r\xF3lag szakk\xE9pes\xEDt\xE9\
      sre felk\xE9sz\xEDt\u0151 \xE9vfolyamai (\xE9retts\xE9git nem ig\xE9nyl\u0151\
      l)"
    entry_age: 14
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 27
    parent_country_entry_ids:
    - HUN-EDU-07
    - HUN-EDU-09
    cum_years_schooling: 11
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
  - country_entry_id: HUN-EDU-24
    national_label_en: Vocational programmes requiring certification of maturity examination
      (full-time education)
    national_label_local: "\xC9retts\xE9gire \xE9p\xFCl\u0151 szakmai k\xE9pz\xE9\
      s (nappali rendszer\u0171 oktat\xE1s)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 9
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-25
    national_label_en: Vocational programmes requiring certification of maturity examination
      (part-time education)
    national_label_local: "\xC9retts\xE9gire \xE9p\xFCl\u0151 szakmai k\xE9pz\xE9\
      s (nem nappali oktat\xE1s)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 9
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-26
    national_label_en: Tertiary vocational programme (full-time education) (short
      cycle)
    national_label_local: "Fels\u0151oktat\xE1si szakk\xE9pz\xE9s (nappali munkarend)"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 10
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-27
    national_label_en: Tertiary vocational programme (part-time education) (short
      cycle)
    national_label_local: "Fels\u0151oktat\xE1si szakk\xE9pz\xE9s (esti, levelez\u0151\
      , t\xE1voktat\xE1s munkarend)"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 10
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-28
    national_label_en: Bachelor programmes (full-time education)
    national_label_local: "Alapk\xE9pz\xE9s (nappali munkarend)"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 11
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-29
    national_label_en: Bachelor programmes (part-time education)
    national_label_local: "Alapk\xE9pz\xE9s (esti, levelez\u0151, t\xE1voktat\xE1\
      s munkarend)"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 11
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-30
    national_label_en: 'Postgraduate specialization programme (full-time education).
      Minimun entry requirements: College or Bachelor degree'
    national_label_local: "Szakir\xE1ny\xFA tov\xE1bbk\xE9pz\xE9s (nappali munkarend).\
      \ Felv\xE9teli felt\xE9tel: f\u0151iskolai diploma vagy alapfokozat"
    entry_age: 21
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 34
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 10
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-31
    national_label_en: 'Postgraduate specialization programme (part-time education).
      Minimun entry requirements: College or Bachelor degree'
    national_label_local: "Szakir\xE1ny\xFA tov\xE1bbk\xE9pz\xE9s (esti, levelez\u0151\
      , t\xE1voktat\xE1s munkarend). Felv\xE9teli felt\xE9tel: f\u0151iskolai diploma\
      \ vagy alapfokozat"
    entry_age: 21
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 35
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 10
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-32
    national_label_en: Master (full-time education)
    national_label_local: "Mesterk\xE9pz\xE9s (nappali munkarend)"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 36
    parent_country_entry_ids:
    - HUN-EDU-28
    - HUN-EDU-29
    - HUN-EDU-30
    - HUN-EDU-31
    cum_years_schooling: 12
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-30
    - HUN-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
    - 'minimum parent path selected from: HUN-EDU-28, HUN-EDU-29, HUN-EDU-30, HUN-EDU-31'
  - country_entry_id: HUN-EDU-33
    national_label_en: Master (part-time education)
    national_label_local: "Mesterk\xE9pz\xE9s (esti, levelez\u0151, t\xE1voktat\xE1\
      s munkarend)"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 37
    parent_country_entry_ids:
    - HUN-EDU-28
    - HUN-EDU-29
    - HUN-EDU-30
    - HUN-EDU-31
    cum_years_schooling: 12
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-30
    - HUN-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
    - 'minimum parent path selected from: HUN-EDU-28, HUN-EDU-29, HUN-EDU-30, HUN-EDU-31'
  - country_entry_id: HUN-EDU-34
    national_label_en: Undivided programmes in universities (full-time education)
    national_label_local: "Osztatlan k\xE9pz\xE9s (nappali munkarend)"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 38
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 13
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-35
    national_label_en: Undivided programmes in universities (part-time education)
    national_label_local: "Osztatlan k\xE9pz\xE9s (esti, levelez\u0151, t\xE1voktat\xE1\
      s munkarend)"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - HUN-EDU-10
    - HUN-EDU-12
    - HUN-EDU-15
    - HUN-EDU-16
    - HUN-EDU-17
    - HUN-EDU-18
    - HUN-EDU-19
    cum_years_schooling: 13
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
  - country_entry_id: HUN-EDU-36
    national_label_en: 'Postgraduate specialization programme (full-time education).
      Minimun entry requirements: University or Master degree'
    national_label_local: "Szakir\xE1ny\xFA tov\xE1bbk\xE9pz\xE9s (nappali munkarend).\
      \ Felv\xE9teli felt\xE9tel: egyetemi diploma vagy mesterfokozat"
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 40
    parent_country_entry_ids:
    - HUN-EDU-28
    - HUN-EDU-29
    - HUN-EDU-30
    - HUN-EDU-31
    cum_years_schooling: 12
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-30
    - HUN-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
    - 'minimum parent path selected from: HUN-EDU-28, HUN-EDU-29, HUN-EDU-30, HUN-EDU-31'
  - country_entry_id: HUN-EDU-37
    national_label_en: 'Postgraduate specialization programme (part-time education).
      Minimun entry requirements: University or Master degree'
    national_label_local: "Szakir\xE1ny\xFA tov\xE1bbk\xE9pz\xE9s (esti, levelez\u0151\
      , t\xE1voktat\xE1s munkarend). Felv\xE9teli felt\xE9tel: egyetemi diploma vagy\
      \ mesterfokozat"
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 41
    parent_country_entry_ids:
    - HUN-EDU-28
    - HUN-EDU-29
    - HUN-EDU-30
    - HUN-EDU-31
    cum_years_schooling: 12
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-30
    - HUN-EDU-37
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
    - 'minimum parent path selected from: HUN-EDU-28, HUN-EDU-29, HUN-EDU-30, HUN-EDU-31'
  - country_entry_id: HUN-EDU-38
    national_label_en: Doctoral programme (full-time education)
    national_label_local: PhD,  DLA (nappali munkarend)
    entry_age: 23
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 42
    parent_country_entry_ids:
    - HUN-EDU-32
    - HUN-EDU-33
    - HUN-EDU-34
    - HUN-EDU-35
    - HUN-EDU-36
    - HUN-EDU-37
    cum_years_schooling: 16
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-30
    - HUN-EDU-32
    - HUN-EDU-38
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
    - 'minimum parent path selected from: HUN-EDU-28, HUN-EDU-29, HUN-EDU-30, HUN-EDU-31'
    - 'minimum parent path selected from: HUN-EDU-32, HUN-EDU-33, HUN-EDU-34, HUN-EDU-35,
      HUN-EDU-36, HUN-EDU-37'
  - country_entry_id: HUN-EDU-39
    national_label_en: Doctoral programme (part-time education)
    national_label_local: "PhD,  DLA (esti, levelez\u0151 munkarend)"
    entry_age: 23
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 43
    parent_country_entry_ids:
    - HUN-EDU-32
    - HUN-EDU-33
    - HUN-EDU-34
    - HUN-EDU-35
    - HUN-EDU-36
    - HUN-EDU-37
    cum_years_schooling: 16
    cum_years_computation_path:
    - HUN-EDU-04
    - HUN-EDU-07
    - HUN-EDU-16
    - HUN-EDU-30
    - HUN-EDU-32
    - HUN-EDU-39
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HUN-EDU-04, HUN-EDU-06'
    - 'minimum parent path selected from: HUN-EDU-07, HUN-EDU-09'
    - 'minimum parent path selected from: HUN-EDU-10, HUN-EDU-12, HUN-EDU-15, HUN-EDU-16,
      HUN-EDU-17, HUN-EDU-18, HUN-EDU-19'
    - 'minimum parent path selected from: HUN-EDU-28, HUN-EDU-29, HUN-EDU-30, HUN-EDU-31'
    - 'minimum parent path selected from: HUN-EDU-32, HUN-EDU-33, HUN-EDU-34, HUN-EDU-35,
      HUN-EDU-36, HUN-EDU-37'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Hungary.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: HUN-SUBNAT-01
    survey_labels: 1-HU1
    survey_variables: subnatid
    gmd_subnatid1: HUN_2021_NUTS1_HU1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: HUN_2021_NUTS1_HU1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: HU1
    geo_nvar: NAME_LATN
    geo_name: "K\xF6z\xE9p-Magyarorsz\xE1g"
    source_row: 6130
  - country_entry_id: HUN-SUBNAT-02
    survey_labels: 2-HU2
    survey_variables: subnatid
    gmd_subnatid1: HUN_2021_NUTS1_HU2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: HUN_2021_NUTS1_HU2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: HU2
    geo_nvar: NAME_LATN
    geo_name: "Dun\xE1nt\xFAl"
    source_row: 6131
  - country_entry_id: HUN-SUBNAT-03
    survey_labels: 3-HU3
    survey_variables: subnatid
    gmd_subnatid1: HUN_2021_NUTS1_HU3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: HUN_2021_NUTS1_HU3
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: HU3
    geo_nvar: NAME_LATN
    geo_name: "Alf\xF6ld \xE9s \xC9szak"
    source_row: 6132
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: HUN-WAS-01
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
  - country_entry_id: HUN-WAS-02
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
  - country_entry_id: HUN-WAS-03
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
  - country_entry_id: HUN-WAS-04
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker-truck, vendor
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: HUN-WAS-05
    source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: HUN-WAS-06
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
  - country_entry_id: HUN-WAS-07
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: HUN-WAS-08
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_HUN_Hungary_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

