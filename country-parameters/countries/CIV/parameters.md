---
country_id: CTY-CIV
iso3: CIV
schema_version: '0.2'
status: draft
country_name: CIV
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: CIV-EDU-01
    national_label_en: Pré-scolaire
    national_label_local: Pré-scolaire
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: CIV-EDU-02
    national_label_en: Primaire
    national_label_local: Primaire
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 8
  - country_entry_id: CIV-EDU-03
    national_label_en: 'Enseignement secondaire: 1er cycle'
    national_label_local: 'Enseignement secondaire: 1er cycle'
    entry_age: 12
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - country_entry_id: CIV-EDU-04
    national_label_en: Enseignement secondaire technique et professionnel:1er cycle
      (CQP)
    national_label_local: Enseignement secondaire technique et professionnel:1er cycle
      (CQP)
    entry_age: 12
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
  - country_entry_id: CIV-EDU-05
    national_label_en: Enseignement secondaire technique et professionnel:1er cycle
      (CAP)
    national_label_local: Enseignement secondaire technique et professionnel:1er cycle
      (CAP)
    entry_age: 14
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
  - country_entry_id: CIV-EDU-06
    national_label_en: 'Enseignement secondaire général: 2ème cycle'
    national_label_local: 'Enseignement secondaire général: 2ème cycle'
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: CIV-EDU-07
    national_label_en: 'Enseignement secondaire technique: 2ème cycle'
    national_label_local: 'Enseignement secondaire technique: 2ème cycle'
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
  - country_entry_id: CIV-EDU-08
    national_label_en: Formation des instituteurs adjoint
    national_label_local: Formation des instituteurs adjoint
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
  - country_entry_id: CIV-EDU-09
    national_label_en: 'Enseignement secondaire technique: 2ème cycle'
    national_label_local: 'Enseignement secondaire technique: 2ème cycle'
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
  - country_entry_id: CIV-EDU-10
    national_label_en: Enseignement pré-universitaire
    national_label_local: Enseignement pré-universitaire
    entry_age: 19
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: CIV-EDU-11
    national_label_en: Enseignement supérieur technique et professionnel (cycle court,
      DUT, CAP-CM)
    national_label_local: Enseignement supérieur technique et professionnel (cycle
      court, DUT, CAP-CM)
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: CIV-EDU-12
    national_label_en: Enseignement supérieur technique et professionnel (cycle court,
      BTS)
    national_label_local: Enseignement supérieur technique et professionnel (cycle
      court, BTS)
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - country_entry_id: CIV-EDU-13
    national_label_en: 'Enseignement universitaire général: 1er cycle'
    national_label_local: 'Enseignement universitaire général: 1er cycle'
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  - country_entry_id: CIV-EDU-14
    national_label_en: Formation des enseignants (Ecole normale supérieure)
    national_label_local: Formation des enseignants (Ecole normale supérieure)
    entry_age: 21
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
  - country_entry_id: CIV-EDU-15
    national_label_en: Formation des cadres d'administration publique (Ecole normale
      d'administration)
    national_label_local: Formation des cadres d'administration publique (Ecole normale
      d'administration)
    entry_age: 21
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
  - country_entry_id: CIV-EDU-16
    national_label_en: 'Enseignement universitaire général: 1er cycle (Licence)'
    national_label_local: 'Enseignement universitaire général: 1er cycle (Licence)'
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
  - country_entry_id: CIV-EDU-17
    national_label_en: Formation des enseignants (Ecole normale supérieur)
    national_label_local: Formation des enseignants (Ecole normale supérieur)
    entry_age: 19
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
  - country_entry_id: CIV-EDU-18
    national_label_en: Enseignement supérieur technique et professionnel (cycle long,
      DESCOM)
    national_label_local: Enseignement supérieur technique et professionnel (cycle
      long, DESCOM)
    entry_age: 19
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
  - country_entry_id: CIV-EDU-19
    national_label_en: "Enseignement supérieur technique et professionnel \n(Cycle
      long, Ingénieur)"
    national_label_local: "Enseignement supérieur technique et professionnel \n(Cycle
      long, Ingénieur)"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
  - country_entry_id: CIV-EDU-20
    national_label_en: Officier supérieur de la marine marchande, officier mécanicien
      1ère classe et 2è classe
    national_label_local: Officier supérieur de la marine marchande, officier mécanicien
      1ère classe et 2è classe
    entry_age: 19
    duration_years: 6
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
  - country_entry_id: CIV-EDU-21
    national_label_en: 'Enseignement universitaire général: 2ème cycle (Master)'
    national_label_local: 'Enseignement universitaire général: 2ème cycle (Master)'
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
  - country_entry_id: CIV-EDU-22
    national_label_en: 'Enseignement universitaire général: 3ème cycle (DESS)'
    national_label_local: 'Enseignement universitaire général: 3ème cycle (DESS)'
    entry_age: 23
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
  - country_entry_id: CIV-EDU-23
    national_label_en: Formation des cadres d'administration publique (Ecole normale
      d'administration)
    national_label_local: Formation des cadres d'administration publique (Ecole normale
      d'administration)
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
  - country_entry_id: CIV-EDU-24
    national_label_en: Formation des enseignants (Ecole normale supérieur)
    national_label_local: Formation des enseignants (Ecole normale supérieur)
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
  - country_entry_id: CIV-EDU-25
    national_label_en: 'Enseignement universitaire général: 3ème cycle (DEA)'
    national_label_local: 'Enseignement universitaire général: 3ème cycle (DEA)'
    entry_age: 23
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
  - country_entry_id: CIV-EDU-26
    national_label_en: 'Enseignement universitaire général: 3ème cycle (Doctorat thèse
      unique)'
    national_label_local: 'Enseignement universitaire général: 3ème cycle (Doctorat
      thèse unique)'
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
  - country_entry_id: CIV-EDU-27
    national_label_en: 'Enseignement universitaire général: 3ème cycle (Doctorat (LMD))'
    national_label_local: 'Enseignement universitaire général: 3ème cycle (Doctorat
      (LMD))'
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Template
      Fr Cote Divoire.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2005
  effective_to: 2005
  selectors: ~
  value:
  - country_entry_id: CIV-SUBNAT-01
    survey_labels: 0 – Ville d'Abidjan
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_11
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_11
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '11'
    geo_nvar: DHSREGFR
    geo_name: Ville D'Abidjan
    source_row: 2362
  - country_entry_id: CIV-SUBNAT-02
    survey_labels: 1 – Centre-Nord
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_3
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '3'
    geo_nvar: DHSREGFR
    geo_name: Centre-Nord
    source_row: 2363
  - country_entry_id: CIV-SUBNAT-03
    survey_labels: 10 – Nord-Ouest
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_7
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_7
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '7'
    geo_nvar: DHSREGFR
    geo_name: Nord-Ouest
    source_row: 2364
  - country_entry_id: CIV-SUBNAT-04
    survey_labels: 2 – Centre-Ouest
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_4
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_4
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '4'
    geo_nvar: DHSREGFR
    geo_name: Centre-Ouest
    source_row: 2365
  - country_entry_id: CIV-SUBNAT-05
    survey_labels: 3 – Nord-Est
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_6
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_6
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '6'
    geo_nvar: DHSREGFR
    geo_name: Nord-Est
    source_row: 2366
  - country_entry_id: CIV-SUBNAT-06
    survey_labels: 4 – Nord
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_5
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_5
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '5'
    geo_nvar: DHSREGFR
    geo_name: Nord
    source_row: 2367
  - country_entry_id: CIV-SUBNAT-07
    survey_labels: 5 – Ouest
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_8
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_8
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '8'
    geo_nvar: DHSREGFR
    geo_name: Ouest
    source_row: 2368
  - country_entry_id: CIV-SUBNAT-08
    survey_labels: 6 – Sud
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_9
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_9
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '9'
    geo_nvar: DHSREGFR
    geo_name: Sud
    source_row: 2369
  - country_entry_id: CIV-SUBNAT-09
    survey_labels: 7 – Sud-Ouest
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_10
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_10
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '10'
    geo_nvar: DHSREGFR
    geo_name: Sud-Ouest
    source_row: 2370
  - country_entry_id: CIV-SUBNAT-10
    survey_labels: 8 – Centre
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_1
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '1'
    geo_nvar: DHSREGFR
    geo_name: Centre
    source_row: 2371
  - country_entry_id: CIV-SUBNAT-11
    survey_labels: 9 – Centre-Est
    survey_variables: subnatid
    gmd_subnatid1: CIV_2005_DHS1_2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: CIV_2005_DHS1_2
    geo_year: '2005'
    geo_source: DHS
    geo_level: '1'
    geo_idvar: REGCODE
    geo_id: '2'
    geo_nvar: DHSREGFR
    geo_name: Centre-Est
    source_row: 2372
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2007
  effective_to: 2007
  selectors: ~
  value:
  - country_entry_id: CIV-SUBNAT-01
    survey_labels: 1 - Agn�by
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '1'
    geo_nvar: ADM1
    geo_name: Agneby
    source_row: 2373
  - country_entry_id: CIV-SUBNAT-02
    survey_labels: 10 - Marahou�
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_10
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '10'
    geo_nvar: ADM1
    geo_name: Marahoue
    source_row: 2374
  - country_entry_id: CIV-SUBNAT-03
    survey_labels: 11 - Moyen-Cavally
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_11
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '11'
    geo_nvar: ADM1
    geo_name: Moyen Comoe
    source_row: 2375
  - country_entry_id: CIV-SUBNAT-04
    survey_labels: 12 - Moyen-Como�
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_12
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '12'
    geo_nvar: ADM1
    geo_name: Moyen-Cavally
    source_row: 2376
  - country_entry_id: CIV-SUBNAT-05
    survey_labels: 13 - N'zi-Como�
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_13
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '13'
    geo_nvar: ADM1
    geo_name: N'Zi Comoe
    source_row: 2377
  - country_entry_id: CIV-SUBNAT-06
    survey_labels: 14 - Savanes
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_14
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '14'
    geo_nvar: ADM1
    geo_name: Savanes
    source_row: 2378
  - country_entry_id: CIV-SUBNAT-07
    survey_labels: 15 - Sud-Bandama
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_15
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '15'
    geo_nvar: ADM1
    geo_name: Sud-Bandama
    source_row: 2379
  - country_entry_id: CIV-SUBNAT-08
    survey_labels: 16 - Sud-Como�
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_16
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '16'
    geo_nvar: ADM1
    geo_name: Sud-Comoe
    source_row: 2380
  - country_entry_id: CIV-SUBNAT-09
    survey_labels: 17 - Vall�e du Bandama
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_17
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '17'
    geo_nvar: ADM1
    geo_name: Vallee Du Bandama
    source_row: 2381
  - country_entry_id: CIV-SUBNAT-10
    survey_labels: 18 - Worodougou
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_18
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '18'
    geo_nvar: ADM1
    geo_name: Worodougou
    source_row: 2382
  - country_entry_id: CIV-SUBNAT-11
    survey_labels: 19 - Zanzan
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_19
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '19'
    geo_nvar: ADM1
    geo_name: Zanzan
    source_row: 2383
  - country_entry_id: CIV-SUBNAT-12
    survey_labels: 2 - Bafing
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '2'
    geo_nvar: ADM1
    geo_name: Bafing
    source_row: 2384
  - country_entry_id: CIV-SUBNAT-13
    survey_labels: 3 - Bas-Sassandra
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '3'
    geo_nvar: ADM1
    geo_name: Bas-Sassandra
    source_row: 2385
  - country_entry_id: CIV-SUBNAT-14
    survey_labels: 4 - Dengu�l�
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_4
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '4'
    geo_nvar: ADM1
    geo_name: Denguele
    source_row: 2386
  - country_entry_id: CIV-SUBNAT-15
    survey_labels: 5 - Dix-Huit Montagnes
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_5
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '5'
    geo_nvar: ADM1
    geo_name: Dix-Huit Montangnes
    source_row: 2387
  - country_entry_id: CIV-SUBNAT-16
    survey_labels: 6 - Fromager
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_6
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '6'
    geo_nvar: ADM1
    geo_name: Fromager
    source_row: 2388
  - country_entry_id: CIV-SUBNAT-17
    survey_labels: 7 - Haut-Sassandra
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_7
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '7'
    geo_nvar: ADM1
    geo_name: Haut-Sassandra
    source_row: 2389
  - country_entry_id: CIV-SUBNAT-18
    survey_labels: 8 - Lacs
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_8
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '8'
    geo_nvar: ADM1
    geo_name: Lacs
    source_row: 2390
  - country_entry_id: CIV-SUBNAT-19
    survey_labels: 9 - Lagunes
    survey_variables: subnatid1
    gmd_subnatid1: CIV_2007_NSO1_9
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2007'
    geo_source: NSO
    geo_level: '1'
    geo_idvar: ADM1_ID
    geo_id: '9'
    geo_nvar: ADM1
    geo_name: Lagunes
    source_row: 2391
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
  - country_entry_id: CIV-SUBNAT-01
    survey_labels: Bere
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '16845'
    geo_nvar: ADM1_NAME
    geo_name: Woroba
    source_row: 2392
  - country_entry_id: CIV-SUBNAT-02
    survey_labels: Bounkani
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1053'
    geo_nvar: ADM1_NAME
    geo_name: Zanzan
    source_row: 2393
  - country_entry_id: CIV-SUBNAT-03
    survey_labels: District autonome D'abidjan
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '16838'
    geo_nvar: ADM1_NAME
    geo_name: District autonome de Abidjan
    source_row: 2394
  - country_entry_id: CIV-SUBNAT-04
    survey_labels: District autonome de Yamoussou | District autonome de Yamoussoukro
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '16839'
    geo_nvar: ADM1_NAME
    geo_name: District autonome de Yamoussoukro
    source_row: 2395
  - country_entry_id: CIV-SUBNAT-05
    survey_labels: Folon
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1041'
    geo_nvar: ADM1_NAME
    geo_name: Denguele
    source_row: 2396
  - country_entry_id: CIV-SUBNAT-06
    survey_labels: Goh
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '16840'
    geo_nvar: ADM1_NAME
    geo_name: Gôh-Djiboua
    source_row: 2397
  - country_entry_id: CIV-SUBNAT-07
    survey_labels: Guemon
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '16843'
    geo_nvar: ADM1_NAME
    geo_name: Montagnes
    source_row: 2398
  - country_entry_id: CIV-SUBNAT-08
    survey_labels: Hambol
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1051'
    geo_nvar: ADM1_NAME
    geo_name: Vallee Du Bandama
    source_row: 2399
  - country_entry_id: CIV-SUBNAT-09
    survey_labels: La Me
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '16842'
    geo_nvar: ADM1_NAME
    geo_name: Lagunes
    source_row: 2400
  - country_entry_id: CIV-SUBNAT-10
    survey_labels: Marahoue
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '16844'
    geo_nvar: ADM1_NAME
    geo_name: Sassandra-Marahoue
    source_row: 2401
  - country_entry_id: CIV-SUBNAT-11
    survey_labels: Moronou
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '16841'
    geo_nvar: ADM1_NAME
    geo_name: Lacs
    source_row: 2402
  - country_entry_id: CIV-SUBNAT-12
    survey_labels: Nawa
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '190430'
    geo_nvar: ADM1_NAME
    geo_name: Bas Sassandra
    source_row: 2403
  - country_entry_id: CIV-SUBNAT-13
    survey_labels: Sud-Comoe
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '16837'
    geo_nvar: ADM1_NAME
    geo_name: Comoe
    source_row: 2404
  - country_entry_id: CIV-SUBNAT-14
    survey_labels: Tchologo
    survey_variables: gaul_adm1 | gaul_adm1_str
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1048'
    geo_nvar: ADM1_NAME
    geo_name: Savanes
    source_row: 2405
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
  - country_entry_id: CIV-SAN-01
    source_category_code: 8_composting_toilet
    national_label_en: 8. Composting toilet
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: CIV-SAN-02
    source_category_code: 9_composting_toilet
    national_label_en: 9. Composting toilet
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: CIV-SAN-03
    source_category_code: composting_toilet
    national_label_en: COMPOSTING TOILET
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: CIV-SAN-04
    source_category_code: des_toilettes_a_compostage
    national_label_en: Des toilettes à compostage
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: CIV-SAN-05
    source_category_code: latrines_ecosan_dallees_couvertes
    national_label_en: Latrines ECOSAN (dallees, couvertes)
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: CIV-SAN-06
    source_category_code: toilettes_a_compostage
    national_label_en: Toilettes a compostage
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: CIV-SAN-07
    source_category_code: toilettes_a_compostage_ecosan
    national_label_en: Toilettes a compostage / EcoSan
    national_label_local: Toilettes a compostage
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: CIV-SAN-08
    source_category_code: flush_toilet
    national_label_en: FLUSH TOILET
    national_label_local: Chasse d'eau
    jmp_classification: Flush and pour flush
    jmp_id: flush_and_pour_flush
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 60
  - country_entry_id: CIV-SAN-09
    source_category_code: 3_flush_pour_flush_toilets_connected_to_elsewhere
    national_label_en: '3. Flush/pour flush toilets connected to: Elsewhere'
    national_label_local: reliée al'air libre
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: CIV-SAN-10
    source_category_code: 4_flush_pour_flush_toilets_connected_to_elsewhere
    national_label_en: '4. Flush/pour flush toilets connected to: Elsewhere'
    national_label_local: reliée al'air libre
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: CIV-SAN-11
    source_category_code: chasse_reliee_a_autre_chose
    national_label_en: Chasse reliee a autre chose
    national_label_local: reliée al'air libre
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: CIV-SAN-12
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_ailleurs
    national_label_en: Des toilettes à chasse d’eau connectées à ailleurs
    national_label_local: reliée al'air libre
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: CIV-SAN-13
    source_category_code: 1_flush_pour_flush_toilets_connected_to_piped_sewer_system
    national_label_en: '1. Flush/pour flush toilets connected to: Piped sewer system'
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: CIV-SAN-14
    source_category_code: chasse_connectee_a_systeme_d_egouts
    national_label_en: Chasse connectee a systeme d'egouts
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: CIV-SAN-15
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_un_systeme_d_egouts
    national_label_en: Des toilettes à chasse d’eau connectées à un système d'égoûts
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: CIV-SAN-16
    source_category_code: 13_flush_pour_flush_toilets_connected_to_pit_latrine
    national_label_en: '13. Flush/pour flush toilets connected to: Pit Latrine'
    national_label_local: reliée aux latrine
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: CIV-SAN-17
    source_category_code: 3_flush_pour_flush_toilets_connected_to_pit_latrine
    national_label_en: '3. Flush/pour flush toilets connected to: Pit Latrine'
    national_label_local: reliée aux latrine
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: CIV-SAN-18
    source_category_code: chasse_reliee_a_des_latrines
    national_label_en: Chasse reliee a des latrines
    national_label_local: reliée aux latrine
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: CIV-SAN-19
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_latrines_a_fosse
    national_label_en: Des toilettes à chasse d’eau connectées à latrines à fosse
    national_label_local: reliée aux latrine
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: CIV-SAN-20
    source_category_code: 2_flush_pour_flush_toilets_connected_to_septic_tank
    national_label_en: '2. Flush/pour flush toilets connected to: Septic tank'
    national_label_local: reliée a fosse septique
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: CIV-SAN-21
    source_category_code: chasse_connectee_a_fosse_septique
    national_label_en: Chasse connectee a fosse septique
    national_label_local: reliée a fosse septique
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: CIV-SAN-22
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_une_fosse_septique
    national_label_en: Des toilettes à chasse d’eau connectées à une fosse septique
    national_label_local: reliée a fosse septique
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: CIV-SAN-23
    source_category_code: 4_flush_pour_flush_toilets_connected_to_unknown_not_sure_do_not_know
    national_label_en: '4. Flush/pour flush toilets connected to: Unknown / Not sure
      / Do not know'
    national_label_local: reliée a autre chose
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: CIV-SAN-24
    source_category_code: 5_flush_pour_flush_toilets_connected_to_unknown_not_sure_do_not_know
    national_label_en: '5. Flush/pour flush toilets connected to: Unknown / Not sure
      / Do not know'
    national_label_local: reliée a autre chose
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: CIV-SAN-25
    source_category_code: chasse_reliee_a_endroit_inconnu_ne_sait_pas_ou
    national_label_en: Chasse reliee a endroit inconnu / Ne sait pas ou
    national_label_local: reliée a autre chose
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: CIV-SAN-26
    source_category_code: des_toilettes_a_chasse_d_eau_connectees_a_inconnu_pas_sur_e_ne_sait_pas
    national_label_en: Des toilettes à chasse d’eau connectées à Inconnu / Pas sûr(e)
      / Ne sait pas
    national_label_local: reliée a autre chose
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: CIV-SAN-27
    source_category_code: chasse_d_eau
    national_label_en: Chasse d eau
    national_label_local: Toilette à chasse d'eau
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: CIV-SAN-28
    source_category_code: chasse_d_eau
    national_label_en: Chasse d'eau
    national_label_local: Toilette à chasse d'eau
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: CIV-SAN-29
    source_category_code: flush_to_sewage_system_septic_tank
    national_label_en: Flush to sewage system/septic tank*
    national_label_local: Toilette à chasse d'eau
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: CIV-SAN-30
    source_category_code: chasse_d_eau_personnelle
    national_label_en: Chasse d'eau personnelle
    national_label_local: Toilette à chasse d'eau (privée)
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: CIV-SAN-31
    source_category_code: chasse_d_eau_privee
    national_label_en: Chasse d'eau privée
    national_label_local: Toilette à chasse d'eau (privée)
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: CIV-SAN-32
    source_category_code: w_c_int_avec_chasse_d_eau_manuelle_rue_cour_caniveau_nature
    national_label_en: W.C. int. avec chasse d'eau/manuelle Rue/Cour/Caniveau/Nature
      + .
    national_label_local: reliée al'air libre
    jmp_classification: Flush/toilets > Private flush/toilet > to elsewhere
    jmp_id: flush_toilets.private_flush_toilet.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 77
  - country_entry_id: CIV-SAN-33
    source_category_code: private_chasse_deau_manuelles_connectee_ss
    national_label_en: Private Chasse deau manuelles/connectée SS
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - country_entry_id: CIV-SAN-34
    source_category_code: private_domestic_connection_to_sewage_system
    national_label_en: Private domestic connection to sewage system
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - country_entry_id: CIV-SAN-35
    source_category_code: w_c_int_avec_chasse_d_eau_manuelle_egout
    national_label_en: W.C. int. avec chasse d'eau/manuelle Egout
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 73
  - country_entry_id: CIV-SAN-36
    source_category_code: private_chasse_deau_manuelles_connectee_fosse_d_aisances
    national_label_en: Private Chasse deau manuelles/connectée Fosse d'aisances
    national_label_local: reliée aux latrine
    jmp_classification: Flush/toilets > Private flush/toilet > to pit
    jmp_id: flush_toilets.private_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 75
  - country_entry_id: CIV-SAN-37
    source_category_code: w_c_int_avec_chasse_d_eau_manuelle_fosse_etanche_et_sample_et_compost
    national_label_en: W.C. int. avec chasse d'eau/manuelle Fosse etanche et sample
      et compost
    national_label_local: reliée aux latrine
    jmp_classification: Flush/toilets > Private flush/toilet > to pit
    jmp_id: flush_toilets.private_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 75
  - country_entry_id: CIV-SAN-38
    source_category_code: private_chasse_deau_manuelles_connectee_st
    national_label_en: Private Chasse deau manuelles/connectée ST
    national_label_local: reliée a fosse septique
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 74
  - country_entry_id: CIV-SAN-39
    source_category_code: private_flush_to_septic_tank
    national_label_en: Private flush to septic tank
    national_label_local: reliée a fosse septique
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 74
  - country_entry_id: CIV-SAN-40
    source_category_code: w_c_int_avec_chasse_d_eau_manuelle_fosse_septique
    national_label_en: W.C. int. avec chasse d'eau/manuelle Fosse septique
    national_label_local: reliée a fosse septique
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 74
  - country_entry_id: CIV-SAN-41
    source_category_code: chasse_d_eau_commune
    national_label_en: Chasse d'eau commune
    national_label_local: Toilette à chasse d'eau (publique/partagée)
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: CIV-SAN-42
    source_category_code: chasse_d_eau_partagee
    national_label_en: Chasse d'eau partagée
    national_label_local: Toilette à chasse d'eau (publique/partagée)
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: CIV-SAN-43
    source_category_code: w_c_ext_avec_chasse_d_eau_manuelle_rue_cour_caniveau_nature_toilettes_publiques
    national_label_en: W.C. ext. avec chasse d'eau/manuelle Rue/Cour/Caniveau/Nature
      +.+toilettes publiques
    national_label_local: reliée al'air libre
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to elsewhere
    jmp_id: flush_toilets.public_shared_flush_toilet.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 83
  - country_entry_id: CIV-SAN-44
    source_category_code: partagees_chasse_deau_manuelles_connectee_ss
    national_label_en: Partagées Chasse deau manuelles/connectée SS
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - country_entry_id: CIV-SAN-45
    source_category_code: shared_domestic_connection_to_sewage_system
    national_label_en: Shared domestic connection to sewage system
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - country_entry_id: CIV-SAN-46
    source_category_code: w_c_ext_avec_chasse_d_eau_manuelle_egout
    national_label_en: W.C. ext. avec chasse d'eau/manuelle Egout
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 79
  - country_entry_id: CIV-SAN-47
    source_category_code: partagees_chasse_deau_manuelles_connectee_fosse_d_aisances
    national_label_en: Partagées Chasse deau manuelles/connectée Fosse d'aisances
    national_label_local: reliée aux latrine
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to pit
    jmp_id: flush_toilets.public_shared_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 81
  - country_entry_id: CIV-SAN-48
    source_category_code: w_c_ext_avec_chasse_d_eau_manuelle_fosse_etanche_et_sample_et_compost_toilettes_publiques
    national_label_en: W.C. ext. avec chasse d'eau/manuelle Fosse etanche et sample
      et compost+ toilettes publiques
    national_label_local: reliée aux latrine
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to pit
    jmp_id: flush_toilets.public_shared_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 81
  - country_entry_id: CIV-SAN-49
    source_category_code: partagees_chasse_deau_manuelles_connectee_st
    national_label_en: Partagées Chasse deau manuelles/connectée ST
    national_label_local: reliée a fosse septique
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 80
  - country_entry_id: CIV-SAN-50
    source_category_code: shared_flush_to_septic_tank
    national_label_en: Shared flush to septic tank
    national_label_local: reliée a fosse septique
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 80
  - country_entry_id: CIV-SAN-51
    source_category_code: w_c_ext_avec_chasse_d_eau_manuelle_toilettes_publiquesfosse_septique
    national_label_en: W.C. ext. avec chasse d'eau/manuelle + toilettes publiquesFosse
      septique
    national_label_local: reliée a fosse septique
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 80
  - country_entry_id: CIV-SAN-52
    source_category_code: toilettes_publiques
    national_label_en: Toilettes publiques
    national_label_local: reliée a autre chose
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to unknown place/
      not sure/DK
    jmp_id: flush_toilets.public_shared_flush_toilet.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 82
  - country_entry_id: CIV-SAN-53
    source_category_code: chasse_branchee_a_autre_chose
    national_label_en: Chasse branchée a autre chose
    national_label_local: reliée al'air libre
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: CIV-SAN-54
    source_category_code: chasse_branchee_a_l_egout
    national_label_en: Chasse branchée a l'égoût
    national_label_local: reliée a systeme d'egouts
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: CIV-SAN-55
    source_category_code: chasse_branchee_a_puits_perdu
    national_label_en: Chasse branchée a puits perdu
    national_label_local: reliée aux latrine
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: CIV-SAN-56
    source_category_code: chasse_branchee_a_fosse_septique
    national_label_en: Chasse branchée a fosse septique
    national_label_local: reliée a fosse septique
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: CIV-SAN-57
    source_category_code: chasse_branchee_a_endroit_inconnu_pas_sure
    national_label_en: Chasse branchée a endroit inconnu/pas sûre
    national_label_local: reliée a autre chose
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: CIV-SAN-58
    source_category_code: 10_bucket
    national_label_en: 10. Bucket
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: CIV-SAN-59
    source_category_code: 9_bucket
    national_label_en: 9. Bucket
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: CIV-SAN-60
    source_category_code: bucket_latrine_where_fresh_excreta_are_manually_removed
    national_label_en: Bucket latrine (where fresh excreta are manually removed)
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: CIV-SAN-61
    source_category_code: bucket_toilet
    national_label_en: BUCKET TOILET
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: CIV-SAN-62
    source_category_code: latrine_bucket
    national_label_en: Latrine Bucket
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: CIV-SAN-63
    source_category_code: seaux
    national_label_en: Seaux
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: CIV-SAN-64
    source_category_code: seaux_tinettes
    national_label_en: Seaux/tinettes
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: CIV-SAN-65
    source_category_code: un_seau
    national_label_en: Un seau
    national_label_local: Seau
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: CIV-SAN-66
    source_category_code: 10_hanging_toilet_hanging_latrine
    national_label_en: 10. Hanging toilet /Hanging latrine
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: CIV-SAN-67
    source_category_code: 11_hanging_toilet_hanging_latrine
    national_label_en: 11. Hanging toilet /Hanging latrine
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: CIV-SAN-68
    source_category_code: des_toilettes_ou_des_latrines_suspendues
    national_label_en: Des toilettes ou des latrines suspendues
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: CIV-SAN-69
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: HANGING TOILET/ HANGING LATRINE
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: CIV-SAN-70
    source_category_code: toilette_suspendues_latrines_suspendues
    national_label_en: Toilette suspendues/latrines suspendues
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: CIV-SAN-71
    source_category_code: toilettes_latrines_suspendues
    national_label_en: Toilettes / Latrines suspendues
    national_label_local: Toilette sospendues
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: CIV-SAN-72
    source_category_code: 11_other
    national_label_en: 11. Other
    national_label_local: Autre
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: CIV-SAN-73
    source_category_code: autre_a_preciser
    national_label_en: Autre a preciser
    national_label_local: Autre
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: CIV-SAN-74
    source_category_code: 6_pit_latrine_with_slab
    national_label_en: 6. Pit latrine with slab
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: CIV-SAN-75
    source_category_code: 7_pit_latrine_with_slab
    national_label_en: 7. Pit latrine with slab
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: CIV-SAN-76
    source_category_code: latrines_a_fosse_avec_dalle
    national_label_en: Latrines a fosse avec dalle
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: CIV-SAN-77
    source_category_code: latrines_dallees_simplement_et_latrines_sanplat_dallees_non_couvertes
    national_label_en: Latrines dallees simplement et Latrines SANPLAT (dallees, non
      couvertes)
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: CIV-SAN-78
    source_category_code: pit_latrine_with_slab
    national_label_en: PIT LATRINE WITH SLAB
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: CIV-SAN-79
    source_category_code: 7_pit_latrine_without_slab_open_pit
    national_label_en: 7. Pit latrine without slab  / open pit
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-80
    source_category_code: 8_pit_latrine_without_slab_open_pit
    national_label_en: 8. Pit latrine without slab  / open pit
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-81
    source_category_code: fosse_rudimentaire_trou_ouver
    national_label_en: Fosse rudimentaire/trou ouver
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-82
    source_category_code: latrines_a_fosse_sans_dalle
    national_label_en: Latrines à fosse sans dalle
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-83
    source_category_code: latrines_a_fosse_sans_dalle_trou_ouvert
    national_label_en: Latrines a fosse sans dalle / trou ouvert
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-84
    source_category_code: latrines_a_trou_ouvert_tranchee
    national_label_en: Latrines a trou ouvert (tranchée)
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-85
    source_category_code: latrines_a_trou_sans_dalle_trou_ouvert
    national_label_en: Latrines à trou sans dalle / trou ouvert
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-86
    source_category_code: open_pit
    national_label_en: Open pit
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-87
    source_category_code: pit_latrine_without_slab_open
    national_label_en: PIT LATRINE WITHOUT SLAB/OPEN
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-88
    source_category_code: uncovered_dry_latrine_without_privacy
    national_label_en: Uncovered dry latrine (without privacy)
    national_label_local: Latrine a fosse sans dalle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: CIV-SAN-89
    source_category_code: latrine_a_fosse
    national_label_en: Latrine a fosse
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: CIV-SAN-90
    source_category_code: latrine_rudimentaires
    national_label_en: Latrine rudimentaires
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: CIV-SAN-91
    source_category_code: latrine_sommaires
    national_label_en: Latrine sommaires
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: CIV-SAN-92
    source_category_code: latrines_traditionnelles
    national_label_en: Latrines traditionnelles
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: CIV-SAN-93
    source_category_code: simple_pit
    national_label_en: Simple Pit*
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: CIV-SAN-94
    source_category_code: traditional_pit_latrine
    national_label_en: Traditional pit latrine
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: CIV-SAN-95
    source_category_code: 5_ventilated_improved_pit_latrine
    national_label_en: 5. Ventilated improved pit latrine
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-96
    source_category_code: 6_ventilated_improved_pit_latrine
    national_label_en: 6. Ventilated improved pit latrine
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-97
    source_category_code: fosse_latrines_ameliorees
    national_label_en: Fosse/Latrines ameliorees
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-98
    source_category_code: improved_pit
    national_label_en: Improved Pit
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-99
    source_category_code: latrines_ameliorees
    national_label_en: Latrines ameliorees
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-100
    source_category_code: latrines_ameliorees_ventilees_lav
    national_label_en: Latrines ameliorees ventilees (LAV)
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-101
    source_category_code: latrines_ameliorees_ventillees
    national_label_en: Latrines améliorées ventillées
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-102
    source_category_code: latrines_ventilees_ameliorees
    national_label_en: Latrines ventilées améliorées
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-103
    source_category_code: latrines_vip_dallees_ventillees
    national_label_en: Latrines VIP (dallees, ventillees)
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-104
    source_category_code: pit_latrine_ventilated
    national_label_en: PIT LATRINE VENTILATED
    national_label_local: Latrine a fosse ameliorée ventilée
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: CIV-SAN-105
    source_category_code: latrines_a_fosse_avec_dalle_prive
    national_label_en: Latrines à fosse avec dalle (privé)
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 114
  - country_entry_id: CIV-SAN-106
    source_category_code: private_covered_dry_latrine_with_privacy
    national_label_en: Private covered dry latrine (with privacy)
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 114
  - country_entry_id: CIV-SAN-107
    source_category_code: latrine_a_fosse_privee
    national_label_en: Latrine à fosse privée
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: CIV-SAN-108
    source_category_code: latrines_a_fosse_avec_dalle_public
    national_label_en: Latrines à fosse avec dalle (public)
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 122
  - country_entry_id: CIV-SAN-109
    source_category_code: shared_covered_dry_latrine_with_privacy
    national_label_en: Shared covered dry latrine (with privacy)
    national_label_local: Latrine a fosse avec dalle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 122
  - country_entry_id: CIV-SAN-110
    source_category_code: latrine_a_fosse_partagee
    national_label_en: Latrine à fosse partagée
    national_label_local: Latrine traditionelle
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - country_entry_id: CIV-SAN-111
    source_category_code: pour_flush_latrine
    national_label_en: Pour flush latrine
    national_label_local: Latrines à chasse d'eau
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 85
  - country_entry_id: CIV-SAN-112
    source_category_code: private_pour_flush_latrine
    national_label_en: Private pour flush latrine
    national_label_local: Latrines à chasse d'eau (privées)
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 91
  - country_entry_id: CIV-SAN-113
    source_category_code: shared_pour_flush_latrine
    national_label_en: Shared pour flush latrine
    national_label_local: Latrines à chasse d'eau (publiques/partagées)
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 97
  - country_entry_id: CIV-SAN-114
    source_category_code: 12_no_facility_bush_field
    national_label_en: 12. No facility / bush / field
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-115
    source_category_code: 13_no_facility_bush_field
    national_label_en: 13. No facility / bush / field
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-116
    source_category_code: aucune_toilette_dans_la_nature
    national_label_en: Aucune toilette (dans la nature)
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-117
    source_category_code: no_faciliity_bush_field
    national_label_en: NO FACILIITY/BUSH/FIELD
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-118
    source_category_code: no_facilities
    national_label_en: No Facilities
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-119
    source_category_code: no_facilities_open_defecation
    national_label_en: No facilities (open defecation)
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-120
    source_category_code: no_facilities_bush_field
    national_label_en: No facilities/bush/field
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-121
    source_category_code: non_pas_disponible
    national_label_en: Non, pas disponible
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-122
    source_category_code: pas_de_toilet_dans_la_nature
    national_label_en: Pas de toilet dans la nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-123
    source_category_code: pas_de_toilettes_buissons_nature
    national_label_en: Pas de toilettes / buissons / nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-124
    source_category_code: pas_de_toilettes_nature
    national_label_en: Pas de toilettes,nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-125
    source_category_code: pas_de_toilettes_dans_la_nature
    national_label_en: Pas de toilettes/dans la nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-126
    source_category_code: pas_de_toilettes_nature
    national_label_en: Pas de toilettes/nature
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-127
    source_category_code: pas_de_wc
    national_label_en: Pas de WC
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: CIV-SAN-128
    source_category_code: 12_other
    national_label_en: 12. Other
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: CIV-SAN-129
    source_category_code: autre
    national_label_en: Autre
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: CIV-SAN-130
    source_category_code: autres
    national_label_en: Autres
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: CIV-SAN-131
    source_category_code: other
    national_label_en: Other
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: CIV-SAN-132
    source_category_code: other_type_of_sanitation
    national_label_en: Other type of sanitation
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: CIV-SAN-133
    source_category_code: autre
    national_label_en: Autre
    national_label_local: Autre
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CIV_Cote_dIvoire_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: CIV-WAS-01
    source_category_code: source
    national_label_en: Source
    national_label_local: Toutes les sources
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: CIV-WAS-02
    source_category_code: spring
    national_label_en: Spring
    national_label_local: Toutes les sources
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: CIV-WAS-03
    source_category_code: private_well
    national_label_en: Private Well
    national_label_local: Privé
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - country_entry_id: CIV-WAS-04
    source_category_code: puits_dans_le_logement_cour_parcelle
    national_label_en: Puits dans le logement/cour/parcelle
    national_label_local: Privé
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 55
  - country_entry_id: CIV-WAS-05
    source_category_code: public_well
    national_label_en: Public Well
    national_label_local: Public
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 56
  - country_entry_id: CIV-WAS-06
    source_category_code: puits_public
    national_label_en: Puits public
    national_label_local: Public
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 56
  - country_entry_id: CIV-WAS-07
    source_category_code: 7_water_from_spring_protected_spring
    national_label_en: '7. Water from Spring: Protected Spring'
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: CIV-WAS-08
    source_category_code: eau_de_source_source_protegee
    national_label_en: 'Eau de source : Source protégée'
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: CIV-WAS-09
    source_category_code: eau_de_source_prota_ga_e
    national_label_en: Eau de source protÃ©gÃ©e
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: CIV-WAS-10
    source_category_code: eau_de_source_protegee
    national_label_en: Eau de source protégée
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: CIV-WAS-11
    source_category_code: source_amenage
    national_label_en: Source aménagé
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: CIV-WAS-12
    source_category_code: source_amenagee
    national_label_en: Source aménagée
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: CIV-WAS-13
    source_category_code: source_d_eau_protegee
    national_label_en: Source d eau protegée
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: CIV-WAS-14
    source_category_code: source_protege
    national_label_en: Source protégé
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: CIV-WAS-15
    source_category_code: source_protegee
    national_label_en: Source protégée
    national_label_local: Source protégées
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: CIV-WAS-16
    source_category_code: 5_dug_well_protected_well
    national_label_en: '5. Dug Well: Protected Well'
    national_label_local: Puits protegées
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: CIV-WAS-17
    source_category_code: protected_dug_well
    national_label_en: PROTECTED DUG WELL
    national_label_local: Puits protegées
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: CIV-WAS-18
    source_category_code: puits_creuse_puits_protege
    national_label_en: 'Puits creusé : puits protégé'
    national_label_local: Puits protegées
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: CIV-WAS-19
    source_category_code: puits_creuse_protege
    national_label_en: Puits creusé protegé
    national_label_local: Puits protegées
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: CIV-WAS-20
    source_category_code: puits_prota_ga
    national_label_en: Puits protÃ©gÃ©
    national_label_local: Puits protegées
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: CIV-WAS-21
    source_category_code: puits_protege
    national_label_en: Puits protégé
    national_label_local: Puits protegées
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: CIV-WAS-22
    source_category_code: puits_couvert_dans_la_cour_concession
    national_label_en: Puits couvert dans la cour/Concession
    national_label_local: Privé
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: CIV-WAS-23
    source_category_code: puits_protege_dans_le_logement_cour_parcelle
    national_label_en: Puits protégé dans le logement/cour/parcelle
    national_label_local: Privé
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: CIV-WAS-24
    source_category_code: puits_couvert_ailleurs
    national_label_en: Puits couvert ailleurs
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 68
  - country_entry_id: CIV-WAS-25
    source_category_code: puits_public_protege
    national_label_en: Puits public protégé
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 68
  - country_entry_id: CIV-WAS-26
    source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: Puits ou sources protégées
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: yes
    shared_flag: no
    source_row: 46
  - country_entry_id: CIV-WAS-27
    source_category_code: puits
    national_label_en: PUITS
    national_label_local: Puits traditionnels
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: CIV-WAS-28
    source_category_code: puits_sans_pompe
    national_label_en: Puits sans pompe
    national_label_local: Puits traditionnels
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: CIV-WAS-29
    source_category_code: 4_tube_well_or_borehole
    national_label_en: 4. Tube well or borehole
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: CIV-WAS-30
    source_category_code: protected_tube_well_or_bore_hole
    national_label_en: Protected tube well or bore hole
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: CIV-WAS-31
    source_category_code: puits_a_pompe_ou_forage
    national_label_en: Puits à pompe ou forage
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: CIV-WAS-32
    source_category_code: puits_a_pompe_forage
    national_label_en: Puits a pompe/forage
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: CIV-WAS-33
    source_category_code: puits_avec_pompe
    national_label_en: Puits avec pompe
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: CIV-WAS-34
    source_category_code: puits_tubulaire_ou_forage
    national_label_en: Puits tubulaire ou forage
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: CIV-WAS-35
    source_category_code: puits_forage_a_pompe
    national_label_en: Puits/forage a pompe
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: CIV-WAS-36
    source_category_code: tube_well
    national_label_en: TUBE WELL
    national_label_local: Puits tubulaire, forage
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: CIV-WAS-37
    source_category_code: forage_dans_la_concession
    national_label_en: Forage dans la concession
    national_label_local: Privé
    jmp_classification: Ground water > Tubewell, borehole > Private
    jmp_id: ground_water.tubewell_borehole.private
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 59
  - country_entry_id: CIV-WAS-38
    source_category_code: forage_ailleurs
    national_label_en: Forage ailleurs
    national_label_local: Public
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 60
  - country_entry_id: CIV-WAS-39
    source_category_code: pompe_publique
    national_label_en: POMPE PUBLIQUE
    national_label_local: Public
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 60
  - country_entry_id: CIV-WAS-40
    source_category_code: 8_water_from_spring_unprotected_spring
    national_label_en: '8. Water from Spring: Unprotected Spring'
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: CIV-WAS-41
    source_category_code: eau_de_source_source_non_protegee
    national_label_en: 'Eau de source : Source non protégée'
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: CIV-WAS-42
    source_category_code: eau_de_source_non_prota_ga_e
    national_label_en: Eau de source non protÃ©gÃ©e
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: CIV-WAS-43
    source_category_code: eau_de_source_non_protegee
    national_label_en: Eau de source non protégée
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: CIV-WAS-44
    source_category_code: source_d_eau_non_protegee
    national_label_en: Source d eau non protegée
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: CIV-WAS-45
    source_category_code: source_non_amenagee
    national_label_en: Source non aménagée
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: CIV-WAS-46
    source_category_code: source_non_protege
    national_label_en: Source non protégé
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: CIV-WAS-47
    source_category_code: source_non_protegee
    national_label_en: Source non protégée
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: CIV-WAS-48
    source_category_code: water_from_spring
    national_label_en: WATER FROM SPRING
    national_label_local: Source non-protégées
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: CIV-WAS-49
    source_category_code: 6_dug_well_unprotected_well
    national_label_en: '6. Dug Well: Unprotected Well'
    national_label_local: Puits non-protegées
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: CIV-WAS-50
    source_category_code: puits_creuse_puits_non_protege
    national_label_en: 'Puits creusé : puits non protégé'
    national_label_local: Puits non-protegées
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: CIV-WAS-51
    source_category_code: puits_creuse_non_protege
    national_label_en: Puits creusé non protegé
    national_label_local: Puits non-protegées
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: CIV-WAS-52
    source_category_code: puits_non_prota_ga
    national_label_en: Puits non protÃ©gÃ©
    national_label_local: Puits non-protegées
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: CIV-WAS-53
    source_category_code: puits_non_protege
    national_label_en: Puits non protégé
    national_label_local: Puits non-protegées
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: CIV-WAS-54
    source_category_code: unprotected_dug_well
    national_label_en: UNPROTECTED DUG WELL
    national_label_local: Puits non-protegées
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: CIV-WAS-55
    source_category_code: puits_ouvert_dans_la_cour_concession
    national_label_en: Puits ouvert dans la cour/Concession
    national_label_local: Privé
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: CIV-WAS-56
    source_category_code: puits_ouverts_dans_le_logement_cour
    national_label_en: Puits ouverts dans le logement / cour
    national_label_local: Privé
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: CIV-WAS-57
    source_category_code: puits_ouvert_ailleurs
    national_label_en: Puits ouvert ailleurs
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 72
  - country_entry_id: CIV-WAS-58
    source_category_code: puits_public_ouvert
    national_label_en: Puits public ouvert
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 72
  - country_entry_id: CIV-WAS-59
    source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: Puits ou sources non protégées
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 50
  - country_entry_id: CIV-WAS-60
    source_category_code: 11_cart_with_small_tank
    national_label_en: 11. Cart with Small Tank
    national_label_local: Chariot avec petit réservoir/tambour
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: CIV-WAS-61
    source_category_code: acheta_e_da_tmun_chariot_avec_un_petit_ra_servoir_ou_tambour
    national_label_en: AchetÃ©e dâ€™un chariot avec un petit rÃ©servoir ou tambour
    national_label_local: Chariot avec petit réservoir/tambour
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: CIV-WAS-62
    source_category_code: achetee_d_un_chariot_avec_un_petit_reservoir_ou_tambour
    national_label_en: Achetée d’un chariot avec un petit réservoir ou tambour
    national_label_local: Chariot avec petit réservoir/tambour
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: CIV-WAS-63
    source_category_code: cart_with_small_tank
    national_label_en: CART WITH SMALL TANK
    national_label_local: Chariot avec petit réservoir/tambour
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: CIV-WAS-64
    source_category_code: charrette_avec_petite_citerne
    national_label_en: Charrette avec petite citerne
    national_label_local: Chariot avec petit réservoir/tambour
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: CIV-WAS-65
    source_category_code: charrette_avec_petite_citerne_tonneau
    national_label_en: Charrette avec petite citerne / tonneau
    national_label_local: Chariot avec petit réservoir/tambour
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: CIV-WAS-66
    source_category_code: charrette_avec_petite_citerne_tonneau
    national_label_en: Charrette avec petite citerne/tonneau
    national_label_local: Chariot avec petit réservoir/tambour
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: CIV-WAS-67
    source_category_code: hydraulique_villageoise_amelioree_hva
    national_label_en: Hydraulique Villageoise Améliorée - HVA
    national_label_local: Autre
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: CIV-WAS-68
    source_category_code: vendeur_ambulant
    national_label_en: Vendeur ambulant
    national_label_local: Autre
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: CIV-WAS-69
    source_category_code: 10_tanker_truck
    national_label_en: 10. Tanker Truck
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: CIV-WAS-70
    source_category_code: acheta_e_da_tmune_citerne
    national_label_en: AchetÃ©e dâ€™une citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: CIV-WAS-71
    source_category_code: achetee_d_une_citerne
    national_label_en: Achetée d’une citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: CIV-WAS-72
    source_category_code: camion_citerne_vendeur_d_eau
    national_label_en: Camion citerne/vendeur d'eau
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: CIV-WAS-73
    source_category_code: camion_citerne
    national_label_en: Camion, citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: CIV-WAS-74
    source_category_code: camion_citerne
    national_label_en: Camion-citerne
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: CIV-WAS-75
    source_category_code: revendeur
    national_label_en: Revendeur
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: CIV-WAS-76
    source_category_code: tanker_water
    national_label_en: TANKER WATER
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: CIV-WAS-77
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker-truck, vendor
    national_label_local: Camion-citerne
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: CIV-WAS-78
    source_category_code: autre
    national_label_en: Autre
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: CIV-WAS-79
    source_category_code: autre_a_preciser
    national_label_en: Autre (à préciser)
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: CIV-WAS-80
    source_category_code: autres
    national_label_en: Autres
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: CIV-WAS-81
    source_category_code: other
    national_label_en: Other
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: CIV-WAS-82
    source_category_code: 13_bottled_water
    national_label_en: 13. Bottled Water
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: CIV-WAS-83
    source_category_code: bottled_water
    national_label_en: BOTTLED WATER
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: CIV-WAS-84
    source_category_code: eau_en_bouteille
    national_label_en: Eau en bouteille
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: CIV-WAS-85
    source_category_code: 14_sachet_water
    national_label_en: 14. Sachet Water
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: CIV-WAS-86
    source_category_code: bagged_water
    national_label_en: BAGGED WATER
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: CIV-WAS-87
    source_category_code: eau_en_bouteille
    national_label_en: Eau en bouteille
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: CIV-WAS-88
    source_category_code: eau_en_bouteille_autre
    national_label_en: Eau en bouteille/autre
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: CIV-WAS-89
    source_category_code: eau_en_bouteille_minerale
    national_label_en: Eau en bouteille/minerale
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: CIV-WAS-90
    source_category_code: eau_en_sachet
    national_label_en: Eau en sachet
    national_label_local: Sachet d'eau
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: CIV-WAS-91
    source_category_code: 9_rainwater
    national_label_en: 9. Rainwater
    national_label_local: Eau de pluie
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: CIV-WAS-92
    source_category_code: rainwater
    national_label_en: RAINWATER
    national_label_local: Eau de pluie
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: CIV-WAS-93
    source_category_code: collecte_d_eau_de_pluie
    national_label_en: Collecte d’eau de pluie
    national_label_local: Citerne/réservoir couvert
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: CIV-WAS-94
    source_category_code: eau_de_pluie
    national_label_en: Eau de pluie
    national_label_local: Citerne/réservoir couvert
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: CIV-WAS-95
    source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: Citerne/réservoir couvert
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: CIV-WAS-96
    source_category_code: 12_surface_water
    national_label_en: 12. Surface water
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-97
    source_category_code: eau_de_surface
    national_label_en: Eau de surface
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-98
    source_category_code: eau_de_surface_riviere_barrage_lac_bassin_cours_d_eau_canal_canaux_d_irrigation
    national_label_en: |-
      Eau de surface (rivière / barrage / lac / bassin
      / cours d'eau / canal / canaux d'irrigation)
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-99
    source_category_code: eau_de_surface_riviere_fleuve_barrage_lac_mare_canal_canal_d_irrigation
    national_label_en: Eau de surface (rivière, fleuve, barrage, lac, mare, canal,
      canal d'irrigation)
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-100
    source_category_code: eau_de_surface_telle_que_rivia_re_barrage_lac_a_tang_ruisseau_canal_ou_canaux_da_tmirrigation
    national_label_en: Eau de surface, telle que riviÃ¨re, barrage, lac, Ã©tang, ruisseau,
      canal ou canaux dâ€™irrigation
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-101
    source_category_code: eau_de_surface_telle_que_riviere_barrage_lac_etang_ruisseau_canal_ou_canaux_d_irrigation
    national_label_en: Eau de surface, telle que rivière, barrage, lac, étang, ruisseau,
      canal ou canaux d’irrigation
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-102
    source_category_code: fleuve_riviere_lac_barrage
    national_label_en: Fleuve/Rivière/Lac/Barrage
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-103
    source_category_code: mare_rivere_ruisseau
    national_label_en: Mare, rivere, ruisseau
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-104
    source_category_code: riviere_lac_source_ou_marigot
    national_label_en: RIVIERE, LAC, SOURCE OU MARIGOT
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-105
    source_category_code: riviere_lac_source_marigot
    national_label_en: Rivière, lac, source, marigot
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-106
    source_category_code: riviere_fleuve_mare_lac
    national_label_en: Rivière/fleuve/mare/lac
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-107
    source_category_code: surface_water_river_dam_lake_pond_stream_irrigation_canal
    national_label_en: SURFACE WATER(RIVER/DAM/LAKE/POND/STREAM/IRRIGATION CANAL)
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-108
    source_category_code: water_taken_directly_from_pond_water_or_stream
    national_label_en: Water taken directly from pond-water or stream
    national_label_local: Eau de surface
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: CIV-WAS-109
    source_category_code: lake_pond_dam
    national_label_en: Lake/Pond/Dam
    national_label_local: Lac
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 94
  - country_entry_id: CIV-WAS-110
    source_category_code: mare_lac_barrage
    national_label_en: Mare/lac/barrage
    national_label_local: Étang
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - country_entry_id: CIV-WAS-111
    source_category_code: river
    national_label_en: River
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: CIV-WAS-112
    source_category_code: riviere_ruisseau
    national_label_en: Rivière/ruisseau
    national_label_local: Fleuve
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: CIV-WAS-113
    source_category_code: revendeur_d_eau
    national_label_en: Revendeur d'eau
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: CIV-WAS-114
    source_category_code: robinet_du_voisin
    national_label_en: Robinet du voisin
    national_label_local: Autre
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: CIV-WAS-115
    source_category_code: piped_water
    national_label_en: PIPED WATER
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: CIV-WAS-116
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: CIV-WAS-117
    source_category_code: private_tap
    national_label_en: Private Tap
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: CIV-WAS-118
    source_category_code: robinet_dans_le_logement_cour_parcelle
    national_label_en: Robinet dans le logement/cour/parcelle
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: CIV-WAS-119
    source_category_code: 1_piped_water_piped_into_dwelling_indoor
    national_label_en: '1. Piped Water: Piped into dwelling/indoor'
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: CIV-WAS-120
    source_category_code: eau_de_robinet_dans_le_logement
    national_label_en: Eau de robinet dans le logement
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: CIV-WAS-121
    source_category_code: eau_du_robinet_robinet_dans_le_logement_a_l_interieur
    national_label_en: |-
      Eau du robinet: Robinet dans le logement/à
      l’intérieur
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: CIV-WAS-122
    source_category_code: robinet_dans_la_maison
    national_label_en: Robinet dans la maison
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: CIV-WAS-123
    source_category_code: robinet_dans_le_logement
    national_label_en: Robinet dans le logement
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: CIV-WAS-124
    source_category_code: robinet_dans_le_logement_cour_parcelle
    national_label_en: Robinet dans le logement/cour/parcelle
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: CIV-WAS-125
    source_category_code: robinet_dans_logement_cour_concession
    national_label_en: Robinet dans logement/cour/concession
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: CIV-WAS-126
    source_category_code: robinet_dedans
    national_label_en: Robinet dedans
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: CIV-WAS-127
    source_category_code: robinet_prive
    national_label_en: ROBINET PRIVÉ
    national_label_local: Eau courante dans le logement
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: CIV-WAS-128
    source_category_code: 2_piped_water_pipe_to_yard_plot
    national_label_en: '2. Piped Water: Pipe to yard/plot'
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: CIV-WAS-129
    source_category_code: dans_la_cour_parcelle
    national_label_en: Dans la cour/parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: CIV-WAS-130
    source_category_code: eau_du_robinet_robinet_sur_la_parcelle_a_l_exterieur
    national_label_en: |-
      Eau du robinet: Robinet sur la parcelle/à
      l’extérieur
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: CIV-WAS-131
    source_category_code: robinet_commun
    national_label_en: ROBINET COMMUN
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: CIV-WAS-132
    source_category_code: robinet_dans_la_cour
    national_label_en: Robinet dans la cour
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: CIV-WAS-133
    source_category_code: robinet_dans_la_cour_dans_la_parcelle_ou_dans_la_concession
    national_label_en: Robinet dans la cour, dans la parcelle, ou dans la concession
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: CIV-WAS-134
    source_category_code: robinet_dans_la_cour_concession
    national_label_en: Robinet dans la cour/concession
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: CIV-WAS-135
    source_category_code: robinet_dans_quartier_cour_ou_parcelle
    national_label_en: Robinet dans quartier, cour ou parcelle
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: CIV-WAS-136
    source_category_code: robinet_dehors
    national_label_en: Robinet dehors
    national_label_local: Eau courante dans la cour ou sur le terrain
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: CIV-WAS-137
    source_category_code: 3_piped_water_public_tap_standpipe
    national_label_en: '3. Piped Water: Public tap/standpipe'
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-138
    source_category_code: borne_fontaine
    national_label_en: Borne fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-139
    source_category_code: borne_fontaine_robinet_public
    national_label_en: Borne fontaine/Robinet public
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-140
    source_category_code: eau_du_robinet_fontaine_publique
    national_label_en: 'Eau du robinet: Fontaine publique'
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-141
    source_category_code: fontaine_public
    national_label_en: Fontaine public
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-142
    source_category_code: public_standpipe
    national_label_en: Public standpipe
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-143
    source_category_code: public_tap
    national_label_en: Public Tap
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-144
    source_category_code: robinet_ou_fontaine_publique
    national_label_en: Robinet ou fontaine publique
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-145
    source_category_code: robinet_public
    national_label_en: Robinet public
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-146
    source_category_code: robinet_public_fontaine
    national_label_en: Robinet public /fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: CIV-WAS-147
    source_category_code: robinet_public_borne_fontaine
    national_label_en: Robinet public/borne fontaine
    national_label_local: Fontaine publique
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_CIV_Cote_dIvoire_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

