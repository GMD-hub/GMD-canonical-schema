# Promotion Checklist - Country Parameters

Date: 2026-09-19
Branch: feat/country-schema-v0.2
Source root: extraction/20_drafts/runs/country-parameters/

## Snapshot

- Total YAML draft files (excluding contracts): 623
- ISO3 folders with at least one draft file: 206
- PARAM-EDU-LEVEL-CROSSWALK.yaml: 183
- PARAM-WASH-SANITATION-CROSSWALK.yaml: 146
- PARAM-WASH-WATER-CROSSWALK.yaml: 150
- PARAM-GEO-GMD-CROSSWALK.yaml: 144

## Run Status Notes

- Full forced extraction command used for refresh:
	- .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli extract --force
- GEO all-country rerun result:
	- extraction/20_drafts/runs/geo_all_run_summary.json => ok=true, success=144/144
- For JMP gaps, check per-file status in:
	- extraction/20_drafts/runs/extract_force_all_result.json
	- Fields: water/sanitation (written, unchanged, no_rows, error, invalid_iso3)

Interpretation rule:

- Missing JMP draft does not always mean missing source workbook.
- It can be a file-level extraction error (for example locked workbook), no_rows after transform, or unchanged skip in non-force runs.

## Review Checklist

| ISO3 | EDU | WASH_SAN | WASH_WATER | GEO | Reviewer | Decision | Notes |
|---|---|---|---|---|---|---|---|
| ABW | Y |  |  |  |  | pending |  |
| AFG | Y | Y | Y |  |  | pending |  |
| AGO | Y | Y | Y | Y |  | pending |  |
| AIA | Y |  |  |  |  | pending |  |
| ALB | Y | Y | Y | Y |  | pending |  |
| AND | Y |  |  |  |  | pending |  |
| ARE | Y | Y | Y |  |  | pending |  |
| ARG | Y | Y | Y | Y |  | pending |  |
| ARM | Y | Y | Y | Y |  | pending |  |
| ATG | Y |  |  |  |  | pending |  |
| AUS | Y |  |  | Y |  | pending |  |
| AUT | Y |  |  | Y |  | pending |  |
| AZE | Y | Y | Y | Y |  | pending |  |
| BDI | Y | Y | Y | Y |  | pending |  |
| BEL | Y |  |  | Y |  | pending |  |
| BEN | Y | Y | Y | Y |  | pending |  |
| BFA | Y | Y | Y | Y |  | pending |  |
| BGD | Y | Y | Y | Y |  | pending |  |
| BGR | Y | Y | Y | Y |  | pending |  |
| BHR | Y |  |  |  |  | pending |  |
| BHS | Y | Y | Y |  |  | pending |  |
| BIH | Y | Y | Y | Y |  | pending |  |
| BLR | Y | Y | Y | Y |  | pending |  |
| BLZ | Y | Y | Y | Y |  | pending |  |
| BMU | Y |  |  |  |  | pending |  |
| BOL | Y | Y | Y | Y |  | pending |  |
| BRA |  | Y | Y | Y |  | pending |  |
| BRB | Y | Y | Y | Y |  | pending |  |
| BRN | Y |  |  |  |  | pending |  |
| BTN | Y | Y | Y | Y |  | pending |  |
| BWA |  | Y | Y | Y |  | pending |  |
| CAF | Y | Y | Y | Y |  | pending |  |
| CAN | Y | Y | Y | Y |  | pending |  |
| CHE | Y |  |  | Y |  | pending |  |
| CHL | Y | Y | Y | Y |  | pending |  |
| CHN | Y | Y | Y | Y |  | pending |  |
| CIV | Y | Y | Y | Y |  | pending |  |
| CMR | Y | Y | Y | Y |  | pending |  |
| COD | Y | Y | Y | Y |  | pending |  |
| COG | Y | Y | Y | Y |  | pending |  |
| COK | Y |  |  |  |  | pending |  |
| COL | Y | Y | Y | Y |  | pending |  |
| COM | Y |  | Y | Y |  | pending |  |
| CPV | Y | Y | Y | Y |  | pending |  |
| CRI | Y | Y | Y | Y |  | pending |  |
| CUB | Y | Y | Y |  |  | pending |  |
| CUW | Y |  |  |  |  | pending |  |
| CYM | Y |  |  |  |  | pending |  |
| CZE | Y | Y | Y | Y |  | pending |  |
| DEU | Y |  |  | Y |  | pending |  |
| DJI | Y | Y | Y | Y |  | pending |  |
| DMA |  |  | Y |  |  | pending |  |
| DNK | Y |  |  |  |  | pending |  |
| DOM | Y | Y | Y | Y |  | pending |  |
| DZA | Y | Y | Y |  |  | pending |  |
| ECU | Y | Y | Y | Y |  | pending |  |
| EGY | Y | Y | Y | Y |  | pending |  |
| ERI | Y | Y | Y |  |  | pending |  |
| ESP | Y | Y | Y | Y |  | pending |  |
| EST | Y | Y | Y |  |  | pending |  |
| ETH | Y | Y | Y | Y |  | pending |  |
| FIN | Y |  |  | Y |  | pending |  |
| FJI | Y | Y | Y | Y |  | pending |  |
| FRA | Y |  |  | Y |  | pending |  |
| FSM | Y |  |  |  |  | pending |  |
| GAB | Y | Y | Y | Y |  | pending |  |
| GBR | Y |  |  | Y |  | pending |  |
| GEO | Y | Y | Y | Y |  | pending |  |
| GHA | Y | Y | Y | Y |  | pending |  |
| GIB | Y |  |  |  |  | pending |  |
| GIN | Y | Y | Y | Y |  | pending |  |
| GMB |  | Y | Y | Y |  | pending |  |
| GNB | Y | Y | Y | Y |  | pending |  |
| GNQ | Y | Y | Y | Y |  | pending |  |
| GRC | Y |  |  | Y |  | pending |  |
| GRD | Y |  |  |  |  | pending |  |
| GTM | Y | Y | Y | Y |  | pending |  |
| GUY | Y | Y | Y |  |  | pending |  |
| HKG | Y |  |  |  |  | pending |  |
| HND | Y | Y | Y | Y |  | pending |  |
| HRV | Y | Y | Y | Y |  | pending |  |
| HTI |  | Y | Y | Y |  | pending |  |
| HUN | Y |  | Y | Y |  | pending |  |
| IDN | Y | Y | Y | Y |  | pending |  |
| IND | Y | Y | Y | Y |  | pending |  |
| IRL | Y |  |  |  |  | pending |  |
| IRN | Y |  |  | Y |  | pending |  |
| IRQ | Y | Y | Y | Y |  | pending |  |
| ISL | Y |  |  |  |  | pending |  |
| ISR | Y |  |  | Y |  | pending |  |
| ITA | Y | Y | Y | Y |  | pending |  |
| JAM | Y | Y | Y | Y |  | pending |  |
| JOR | Y | Y | Y | Y |  | pending |  |
| JPN | Y |  |  | Y |  | pending |  |
| KAZ | Y | Y | Y | Y |  | pending |  |
| KEN | Y | Y | Y | Y |  | pending |  |
| KGZ | Y | Y | Y | Y |  | pending |  |
| KHM | Y | Y | Y |  |  | pending |  |
| KIR | Y | Y | Y | Y |  | pending |  |
| KWT | Y |  |  |  |  | pending |  |
| LAO | Y | Y | Y | Y |  | pending |  |
| LBN | Y | Y | Y | Y |  | pending |  |
| LBR |  | Y | Y | Y |  | pending |  |
| LBY | Y | Y | Y |  |  | pending |  |
| LCA | Y | Y | Y |  |  | pending |  |
| LIE | Y |  |  |  |  | pending |  |
| LKA | Y | Y | Y | Y |  | pending |  |
| LSO |  | Y | Y | Y |  | pending |  |
| LTU | Y |  |  |  |  | pending |  |
| LUX | Y |  |  |  |  | pending |  |
| LVA | Y | Y | Y |  |  | pending |  |
| MAC | Y |  |  |  |  | pending |  |
| MAR | Y | Y | Y | Y |  | pending |  |
| MCO | Y |  |  |  |  | pending |  |
| MDA | Y | Y | Y | Y |  | pending |  |
| MDG | Y | Y | Y | Y |  | pending |  |
| MDV |  | Y | Y | Y |  | pending |  |
| MEX | Y | Y | Y | Y |  | pending |  |
| MHL | Y | Y | Y |  |  | pending |  |
| MKD | Y | Y | Y | Y |  | pending |  |
| MLI | Y | Y | Y | Y |  | pending |  |
| MLT | Y |  |  |  |  | pending |  |
| MMR |  | Y | Y | Y |  | pending |  |
| MNE | Y | Y | Y | Y |  | pending |  |
| MNG | Y | Y | Y | Y |  | pending |  |
| MOZ |  | Y | Y | Y |  | pending |  |
| MRT | Y | Y | Y | Y |  | pending |  |
| MSR | Y |  |  |  |  | pending |  |
| MUS | Y | Y | Y | Y |  | pending |  |
| MWI | Y | Y | Y | Y |  | pending |  |
| MYS | Y | Y | Y | Y |  | pending |  |
| NAM |  | Y | Y | Y |  | pending |  |
| NER | Y | Y | Y | Y |  | pending |  |
| NGA | Y | Y | Y | Y |  | pending |  |
| NIU | Y |  |  |  |  | pending |  |
| NLD | Y |  |  |  |  | pending |  |
| NOR | Y |  |  |  |  | pending |  |
| NPL | Y | Y | Y | Y |  | pending |  |
| NRU | Y | Y | Y |  |  | pending |  |
| NZL | Y |  |  |  |  | pending |  |
| OMN | Y |  |  |  |  | pending |  |
| PAK | Y | Y | Y | Y |  | pending |  |
| PAN | Y | Y | Y | Y |  | pending |  |
| PER | Y | Y | Y | Y |  | pending |  |
| PHL | Y | Y | Y | Y |  | pending |  |
| PNG | Y | Y | Y | Y |  | pending |  |
| POL | Y |  |  | Y |  | pending |  |
| PRI |  | Y | Y |  |  | pending |  |
| PRT | Y |  |  | Y |  | pending |  |
| PRY |  | Y | Y | Y |  | pending |  |
| PSE | Y | Y | Y | Y |  | pending |  |
| PYF |  | Y | Y |  |  | pending |  |
| QAT | Y | Y | Y |  |  | pending |  |
| ROU | Y |  |  | Y |  | pending |  |
| RUS | Y |  |  | Y |  | pending |  |
| RWA | Y |  |  | Y |  | pending |  |
| SDN | Y |  |  | Y |  | pending |  |
| SEN | Y |  |  | Y |  | pending |  |
| SGP | Y |  |  |  |  | pending |  |
| SLE | Y |  |  | Y |  | pending |  |
| SLV | Y |  |  | Y |  | pending |  |
| SMR | Y |  |  |  |  | pending |  |
| SOM | Y |  |  |  |  | pending |  |
| SRB | Y |  |  | Y |  | pending |  |
| SUR | Y |  |  | Y |  | pending |  |
| SVK | Y |  |  |  |  | pending |  |
| SVN | Y |  |  |  |  | pending |  |
| SWE | Y |  |  | Y |  | pending |  |
| SYC | Y |  |  | Y |  | pending |  |
| SYR | Y |  |  |  |  | pending |  |
| TCA | Y |  |  |  |  | pending |  |
| TCD | Y |  |  | Y |  | pending |  |
| TGO | Y |  |  | Y |  | pending |  |
| THA | Y |  |  | Y |  | pending |  |
| TJK | Y |  |  | Y |  | pending |  |
| TKL | Y |  |  |  |  | pending |  |
| TKM | Y |  |  |  |  | pending |  |
| TLS | Y |  |  | Y |  | pending |  |
| TON | Y |  |  | Y |  | pending |  |
| TUN | Y |  |  | Y |  | pending |  |
| TUR | Y |  |  | Y |  | pending |  |
| TUV | Y |  |  |  |  | pending |  |
| TZA | Y |  |  | Y |  | pending |  |
| UGA | Y |  |  | Y |  | pending |  |
| UKR | Y |  |  | Y |  | pending |  |
| URY | Y |  |  | Y |  | pending |  |
| USA | Y |  |  | Y |  | pending |  |
| UZB | Y |  |  | Y |  | pending |  |
| VCT | Y |  |  |  |  | pending |  |
| VEN | Y |  |  |  |  | pending |  |
| VGB | Y |  |  |  |  | pending |  |
| VNM | Y | Y | Y | Y |  | pending |  |
| VUT | Y |  |  | Y |  | pending |  |
| WSM | Y |  |  | Y |  | pending |  |
| YEM | Y |  |  | Y |  | pending |  |
| ZAF | Y |  |  | Y |  | pending |  |
| ZWE | Y |  |  | Y |  | pending |  |

## Promotion Rule

- Promote only after human review approval.
- Keep EDU effective_from as null unless clear educational era evidence exists.
- Validate after promotion: .\\.venv\\Scripts\\python.exe validation/validate_country_layer.py
