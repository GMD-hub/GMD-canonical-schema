---
country_id: CTY-DJI
iso3: DJI
schema_version: '0.2'
status: draft
country_name: DJI
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: DJI-EDU-01
    national_label_en: Enseignement préscolaire (privé)
    national_label_local: Enseignement préscolaire (privé)
    entry_age: 4
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: DJI-EDU-02
    national_label_en: Enseignement préscolaire (public)
    national_label_local: Enseignement préscolaire (public)
    entry_age: 5
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 8
  - country_entry_id: DJI-EDU-03
    national_label_en: 'Enseignement fondamental: enseignement de base'
    national_label_local: 'Enseignement fondamental: enseignement de base'
    entry_age: 6
    duration_years: 5
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 9
  - country_entry_id: DJI-EDU-04
    national_label_en: 'Enseignement fondamental: enseignement moyen général'
    national_label_local: 'Enseignement fondamental: enseignement moyen général'
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
  - country_entry_id: DJI-EDU-05
    national_label_en: Enseignement secondaire général
    national_label_local: Enseignement secondaire général
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - country_entry_id: DJI-EDU-06
    national_label_en: Enseignement secondaire technique
    national_label_local: Enseignement secondaire technique
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: DJI-EDU-07
    national_label_en: Enseignement technique et formation professionnelle court,
      2ans
    national_label_local: Enseignement technique et formation professionnelle court,
      2ans
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
  - country_entry_id: DJI-EDU-08
    national_label_en: Enseignement technique et formation professionnelle long ,
      3ans
    national_label_local: Enseignement technique et formation professionnelle long
      , 3ans
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
  - country_entry_id: DJI-EDU-09
    national_label_en: Brevet de technicien
    national_label_local: Brevet de technicien
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - country_entry_id: DJI-EDU-10
    national_label_en: Enseignement supérieur cycle long
    national_label_local: Enseignement supérieur cycle long
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Djibouti.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2022
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: DJI-SUBNAT-01
    survey_labels: 1 - Djibouti | 10 - Djibouti
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: DJI_2022_GADM1_DJI.3_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: DJI_2022_GADM1_DJI.3_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: DJI.3_1
    geo_nvar: NAME_1
    geo_name: Djiboutii
    source_row: 3695
  - country_entry_id: DJI-SUBNAT-02
    survey_labels: 2 - Ali Sabieh | 20 - Ali Sabieh
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: DJI_2022_GADM1_DJI.1_2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: DJI_2022_GADM1_DJI.1_2
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: DJI.1_2
    geo_nvar: NAME_1
    geo_name: Ali Sabieh
    source_row: 3696
  - country_entry_id: DJI-SUBNAT-03
    survey_labels: 3 - Dikhil | 30 - Dikhil
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: DJI_2022_GADM1_DJI.2_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: DJI_2022_GADM1_DJI.2_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: DJI.2_1
    geo_nvar: NAME_1
    geo_name: Dikhil
    source_row: 3697
  - country_entry_id: DJI-SUBNAT-04
    survey_labels: 4 - Tadjourah | 40 - Tadjourah
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: DJI_2022_GADM1_DJI.5_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: DJI_2022_GADM1_DJI.5_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: DJI.5_1
    geo_nvar: NAME_1
    geo_name: Tadjoura
    source_row: 3698
  - country_entry_id: DJI-SUBNAT-05
    survey_labels: 5 - Obock | 50 - Obock
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: DJI_2022_GADM1_DJI.4_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: DJI_2022_GADM1_DJI.4_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: DJI.4_1
    geo_nvar: NAME_1
    geo_name: Obock
    source_row: 3699
  - country_entry_id: DJI-SUBNAT-06
    survey_labels: 6 - Arta | 60 - Arta
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: DJI_2022_GADM1_DJI.6_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: DJI_2022_GADM1_DJI.6_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: DJI.6_1
    geo_nvar: NAME_1
    geo_name: Arta
    source_row: 3700
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
  - country_entry_id: DJI-SAN-01
    source_category_code: toilettes_a_compostage
    national_label_en: Toilettes a compostage
    national_label_local: مراحيض التسميد
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: DJI-SAN-02
    source_category_code: wc_avec_chasse_d_eau
    national_label_en: WC avec chasse d'eau
    national_label_local: دافق / مراحيض
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: DJI-SAN-03
    source_category_code: wc_turc_avec_eau
    national_label_en: WC turc avec eau
    national_label_local: دافق / مراحيض
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: DJI-SAN-04
    source_category_code: chasse_branchee_a_autre_chose
    national_label_en: Chasse branchee a autre chose
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: DJI-SAN-05
    source_category_code: chasse_d_eau_vers_des_fosses_ouverts
    national_label_en: Chasse d'eau vers des fossés ouverts
    national_label_local: إلى مكان آخر
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: DJI-SAN-06
    source_category_code: chasse_branchee_a_l_egout
    national_label_en: Chasse branchee a l'egout
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: DJI-SAN-07
    source_category_code: chasse_d_eau_vers_un_reseau_d_egout
    national_label_en: Chasse d'eau vers un réseau d'égout
    national_label_local: إلى نظام الصرف الصحي بالأنابيب
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: DJI-SAN-08
    source_category_code: chasse_branchee_a_latrines
    national_label_en: Chasse branchee a latrines
    national_label_local: للحفر
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: DJI-SAN-09
    source_category_code: chasse_d_eau_vers_une_latrine_a_fosse
    national_label_en: Chasse d'eau vers une latrine à fosse
    national_label_local: للحفر
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: DJI-SAN-10
    source_category_code: chasse_branchee_a_fosse_septique
    national_label_en: Chasse branchee a fosse septique
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: DJI-SAN-11
    source_category_code: chasse_d_eau_vers_une_fosse_septique
    national_label_en: Chasse d'eau vers une fosse septique
    national_label_local: لخزان الصرف الصحي
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: DJI-SAN-12
    source_category_code: toilette_suspendues_latrines_suspendues
    national_label_en: Toilette suspendues/latrines suspendues
    national_label_local: دورة مياه معلقة / مرحاض معلق
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: DJI-SAN-13
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
  - country_entry_id: DJI-SAN-14
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
  - country_entry_id: DJI-SAN-15
    source_category_code: wc_turc_sans_eau
    national_label_en: WC turc sans eau
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: DJI-SAN-16
    source_category_code: latrines_a_fosse_sans_dalle_fosse_ouverte
    national_label_en: Latrines à fosse sans dalle/fosse ouverte
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: DJI-SAN-17
    source_category_code: latrines_a_fosses_trou_ouvert
    national_label_en: Latrines a fosses/trou ouvert
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: DJI-SAN-18
    source_category_code: wc_cuve_sans_eau
    national_label_en: WC cuve sans eau
    national_label_local: مرحاض حفرة بدون بلاطة / حفرة مفتوحة
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: DJI-SAN-19
    source_category_code: latrines_a_fosse_seche
    national_label_en: Latrines à fosse sèche
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: DJI-SAN-20
    source_category_code: latrines_ameliorees_auto_aerees_laa
    national_label_en: Latrines ameliorees auto aerees (LAA)
    national_label_local: مراحيض حفرة محسنة جيدة التهوية
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: DJI-SAN-21
    source_category_code: latrine_simple_fosse_simple_avec_dalle_en_beton_ou_materiau
    national_label_en: Latrine simple (fosse simple avec dalle en béton/ou matériau)
    national_label_local: مرحاض حفرة مع بلاطة / مرحاض مغطى
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 114
  - country_entry_id: DJI-SAN-22
    source_category_code: trou_dans_le_sol_avec_cloture_rudimentaire
    national_label_en: Trou dans le sol avec clôture rudimentaire
    national_label_local: المراحيض التقليدية
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: DJI-SAN-23
    source_category_code: wc_cuve_avec_eau
    national_label_en: WC cuve avec eau
    national_label_local: صب المراحيض المتدفقة
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 85
  - country_entry_id: DJI-SAN-24
    source_category_code: autre
    national_label_en: Autre
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: DJI-SAN-25
    source_category_code: dans_la_nature
    national_label_en: Dans la nature
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: DJI-SAN-26
    source_category_code: pas_de_toilettes_ou_brousse_ou_champ
    national_label_en: Pas de toilettes ou brousse ou champ
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: DJI-SAN-27
    source_category_code: ucun_buisson_espace_ouvert_dans_la_nature
    national_label_en: ucun / buisson / espace ouvert / dans la nature
    national_label_local: لا توجد منشأة ، شجيرة ، حقل
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: DJI-SAN-28
    source_category_code: wc_sans_chasse_d_eau
    national_label_en: WC sans chasse d'eau
    national_label_local: آخر
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: DJI-SAN-29
    source_category_code: autre
    national_label_en: Autre
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: DJI-SAN-30
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
  - country_entry_id: DJI-SAN-31
    source_category_code: inconnu
    national_label_en: Inconnu
    national_label_local: آخر
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_DJI_Djibouti_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: DJI-WAS-01
    source_category_code: source_protegee
    national_label_en: Source protegee
    national_label_local: ينبوع المحمي
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: DJI-WAS-02
    source_category_code: puits_amenages_sans_pompe
    national_label_en: Puits aménagés sans pompe
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: DJI-WAS-03
    source_category_code: puits_protege
    national_label_en: Puits protege
    national_label_local: محمي بشكل جيد
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: DJI-WAS-04
    source_category_code: puits_traditionnel
    national_label_en: Puits traditionnel
    national_label_local: الآبار التقليدية
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: DJI-WAS-05
    source_category_code: puit_traditionnel
    national_label_en: Puit traditionnel
    national_label_local: آخر
    jmp_classification: Ground water > Traditional wells > Other
    jmp_id: ground_water.traditional_wells.other
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: DJI-WAS-06
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
  - country_entry_id: DJI-WAS-07
    source_category_code: forage_puis_avec_pompe
    national_label_en: Forage (puis avec pompe)
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: DJI-WAS-08
    source_category_code: forage_ou_puits_tubulaire
    national_label_en: Forage ou puits tubulaire
    national_label_local: بئر أنبوبي ، بئر
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: DJI-WAS-09
    source_category_code: source_non_protegee
    national_label_en: Source non protegee
    national_label_local: ينبوع غير المحمي
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: DJI-WAS-10
    source_category_code: puit
    national_label_en: Puit
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: DJI-WAS-11
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
  - country_entry_id: DJI-WAS-12
    source_category_code: puits_traditionnels
    national_label_en: Puits traditionnels
    national_label_local: بئر غير محمي
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: DJI-WAS-13
    source_category_code: charrette_avec_petite_citerne_tonneau
    national_label_en: Charrette avec petite citerne/tonneau
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: DJI-WAS-14
    source_category_code: vendeur
    national_label_en: Vendeur
    national_label_local: عربة مع خزان صغير / أسطوانة
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: DJI-WAS-15
    source_category_code: eau_courante
    national_label_en: Eau courante
    national_label_local: آخر
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: DJI-WAS-16
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
  - country_entry_id: DJI-WAS-17
    source_category_code: camion_citerne
    national_label_en: Camion-citerne
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: DJI-WAS-18
    source_category_code: vendeur
    national_label_en: Vendeur
    national_label_local: يتم توفير شاحنة صهريج
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: DJI-WAS-19
    source_category_code: autre
    national_label_en: Autre
    national_label_local: آخر
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: DJI-WAS-20
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
  - country_entry_id: DJI-WAS-21
    source_category_code: collecte_des_eaux_de_pluie
    national_label_en: Collecte des eaux de pluie
    national_label_local: خزان / خزان مغطى
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: DJI-WAS-22
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
  - country_entry_id: DJI-WAS-23
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
  - country_entry_id: DJI-WAS-24
    source_category_code: eau_de_surface_retenue_citerne_enterree_oued_en_crue
    national_label_en: Eau de surface (Retenue, Citerne enterrée, Oued en crue)
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: DJI-WAS-25
    source_category_code: riviere_cours_d_eau_eau_de_pluie_retenu_d_eau_citerne_enter
    national_label_en: Rivière/cours d'eau/eau de pluie/retenu d'eau/ citerne enter
    national_label_local: سطح الماء
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: DJI-WAS-26
    source_category_code: riviere
    national_label_en: Riviere
    national_label_local: نهر
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: DJI-WAS-27
    source_category_code: branchem_exterieur
    national_label_en: Branchem. exterieur
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: DJI-WAS-28
    source_category_code: branchement_direct_a_partir_d_un_forage
    national_label_en: Branchement direct à partir d'un forage
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: DJI-WAS-29
    source_category_code: branchement_exterieur
    national_label_en: Branchement Exterieur
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: DJI-WAS-30
    source_category_code: branchements_chez_le_voisin
    national_label_en: Branchements chez le voisin
    national_label_local: آخر
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: DJI-WAS-31
    source_category_code: branchem_interieur
    national_label_en: Branchem. interieur
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: DJI-WAS-32
    source_category_code: branchements_dans_le_lotissement_dans_la_cour_ou_sur_la_parcelle
    national_label_en: Branchements dans le lotissement, dans la cour ou sur la parcelle
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: DJI-WAS-33
    source_category_code: eau_courante
    national_label_en: Eau Courante
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: DJI-WAS-34
    source_category_code: eau_courante_branchement_interieur_onead
    national_label_en: Eau courante (branchement intérieur ONEAD)
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: DJI-WAS-35
    source_category_code: eau_de_robinet_dans_le_logement
    national_label_en: Eau de robinet dans le logement
    national_label_local: الماء بالأنابيب في المسكن
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: DJI-WAS-36
    source_category_code: branchement_exterieur_onead_par_tuyau
    national_label_en: Branchement extérieur ONEAD, par tuyau
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: DJI-WAS-37
    source_category_code: dans_la_cour_parcelle
    national_label_en: Dans la cour/parcelle
    national_label_local: المياه المنقولة بالأنابيب إلى ساحة / قطعة أرض
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: DJI-WAS-38
    source_category_code: borne_publique
    national_label_en: Borne publique
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: DJI-WAS-39
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
  - country_entry_id: DJI-WAS-40
    source_category_code: fontaine_publique
    national_label_en: Fontaine publique
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: DJI-WAS-41
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
  - country_entry_id: DJI-WAS-42
    source_category_code: robinet_public_borne_fontaine
    national_label_en: Robinet public/borne-fontaine
    national_label_local: الحنفية العامة والصنبور الرأسي
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_DJI_Djibouti_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

