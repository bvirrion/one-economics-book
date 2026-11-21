# Data sources to approve (licences checked 2026-11-20)

Under the workspace rule, nothing here has been downloaded, probed or mirrored. Six `web-fetch` passes read the
hosts' **HTML terms pages only**. Every licence below was read on that page unless a row says otherwise.

**Proposed storage.** Raw files go in `data/raw/<source>/`. They are gitignored, and `data/MANIFEST.md` records each
one's URL, date, size, sha256 and licence. The small derived tables that the charts read go in `data/derived/`,
which is versioned. Each derived table is written by a tested script.

**Credits.** Each chart's source line gives the provider. The data ledger and the book's colophon give the full
citation the provider asks for.

## A. Proposed for download (licence verified)

| # | Dataset | Host and URL | Contents and size | Licence (as read) | Conditions | Used for |
|---|---|---|---|---|---|---|
| 1 | Maddison Project Database 2023 | dataverse.nl, `https://dataverse.nl/api/access/datafile/421302` (Excel); DOI 10.34894/INZBF2 | GDP per capita and population, year 1 to 2022, 169 countries; a few MB | CC BY 4.0 (rug.nl release page) | Cite Bolt and van Zanden (2024). For charts, also cite the original papers listed in the file's source sheet | g6 living standards; growth chapters in every book |
| 2 | Penn World Table 11.0 | dataverse.nl, `https://dataverse.nl/api/access/datafile/554105` (Excel); DOI 10.34894/FABVLR | 185 countries 1950–2023: PPP GDP, capital, hours, TFP, labour share; ~30 MB | CC BY 4.0 (rug.nl PWT page) | Cite Feenstra, Inklaar and Timmer (2015, AER), version 11.0 | growth accounting, Solow, productivity, PPP |
| 3 | World Development Indicators | datacatalogfiles.worldbank.org, `.../0037712/DR0095335/WDI_CSV_2026_11_11.zip` | ~1,500 indicators since 1960, which include population, fertility, life expectancy and child mortality (UN- and UN IGME-based), poverty headcounts (PIP), employment by sector (ILO modelled), trade share, inflation, government finance and energy; **269 MB zip** (Excel version 78 MB) | CC BY 4.0, plus World Bank dataset terms (datacatalog page and WB Dataset Terms) | Cite "The World Bank: World Development Indicators: <source>". Indicators whose metadata names a third-party restriction are left out (checked in `WDISeries.csv` after download) | most charts since 1960; replaces UN WPP, ILOSTAT and PIP country series |
| 4 | Poverty and Inequality Platform: Percentiles | datacatalogfiles.worldbank.org, `.../0063646/DR0090357/world_100bin.csv` (2021 PPP) | world income distribution in 100 bins by country and year; ~20 MB | CC BY 4.0 (datacatalog page) | Attribution | g9 income distribution, g11 inequality, the world distribution |
| 5 | Jordà–Schularick–Taylor Macrohistory Database R6 | macrohistory.net, `https://www.macrohistory.net/app/download/9834512569/JSTdatasetR6.xlsx` | 18 economies since 1870: GDP, prices, rates, credit, crises, returns, public debt, revenue and spending, exports and imports; a few MB | **CC BY-NC-SA 4.0** (licence-terms page), the same licence as the books | Cite Jordà, Schularick and Taylor (2017), plus the subset paper where one applies; give the consultation date; non-commercial only | long-run inflation, interest rates, debt, crises; trade share since 1870 (replaces Federico–Tena) |
| 6 | Gapminder Fast Track / Systema Globalis (named indicator files only) | github.com/open-numbers, `ddf--gapminder--fasttrack` and `ddf--gapminder--systema_globalis` (exact file paths read from the repo's HTML listing at download time) | life expectancy, child mortality, fertility and population before 1950; GDP per capita long series; a few CSVs of under 5 MB each | CC BY 4.0 (gapminder.org/free-material) | Credit "Based on free material from GAPMINDER.ORG, CC-BY LICENSE". **Used only for the years before 1950**, where Gapminder's own compilation is the source. From 1950 the underlying data is IHME's and the UN's, so WDI is used instead | g6 health and population, the 1800–1950 parts |
| 7 | Eurostat (a few datasets: HICP, unemployment, government deficit and debt, GDP) | ec.europa.eu/eurostat bulk download (`/en/data/bulkdownload`), e.g. `prc_hicp_aind`, `une_rt_a`, `gov_10dd_edpt1`, `nama_10_gdp` | European series; < 20 MB | CC BY 4.0 (copyright notice page) | Cite the dataset DOI and the access date; state any changes | European record boxes (2021–23 inflation, the euro area) |
| 8 | BLS flat files (CPI-U; labour-force series and gross flows) | `https://download.bls.gov/pub/time.series/cu/` and `.../ln/` (named files only) | US CPI since 1913, unemployment, participation and flows; < 50 MB | Public domain (BLS copyright page) | Cite BLS; no emblem. If the server refuses scripted downloads, the row is dropped | price indices, unemployment flows, the Phillips record |
| 9 | CEDS v_2025_03_18 aggregate | zenodo.org, `https://zenodo.org/records/15059443/files/CEDS_v_2025_03_18_aggregate.zip?download=1` | CO₂, SO₂ and other emissions by country and sector since 1750; 62.7 MB | CC BY 4.0 (Zenodo record) | Cite the DOI 10.5281/zenodo.15059443. The README is read for any IEA-derived column, and such columns are left out | g6 food and energy, externalities, environment; replaces the Global Carbon Budget |
| 10 | EIA international energy data (bulk) | eia.gov/opendata bulk page (`INTL.zip`, confirmed on the HTML bulk page before download) | energy consumption and production by country since 1980; ~100 MB | Public domain (EIA copyrights and reuse page) | Acknowledge EIA with the date. If the bulk file needs an API key (and so an e-mail), the row is dropped | energy use per person against income |
| 11 | FAOSTAT Crops and livestock products (bulk, normalised) | fao.org bulk download for the QCL domain (the URL is read from the FAOSTAT bulk page) | crop yields by country since 1961; ~30 MB zip | CC BY 4.0 (FAO database terms) | Use FAO's citation format. FAO's clause on translation and adaptation is to be confirmed before a translated edition | g6 cereal yields, food chapters |
| 12 | CEPII Gravity V202211 | `https://www.cepii.fr/DATA_DOWNLOAD/gravity/data/Gravity_csv_V202211.zip` | bilateral trade flows, distance, borders and language, 1948–2020; a few hundred MB | Licence Ouverte / Etalab 2.0 (stated on the CEPII page). **The licence text itself could not be fetched.** From knowledge, it allows reuse and adaptation with credit to the source and its date | Cite Conte, Cotterlaz and Mayer (2022) | Y3 gravity chapter |
| 13 | Dehejia–Wahba NSW (LaLonde) samples | `http://www.nber.org/~rdehejia/data/nsw_dw.dta`, plus the CPS and PSID comparison files | 445 treated and control men and the comparison groups; < 5 MB | CC BY-NC 2.0 (the page) | Cite the three papers; link the page; keep the data's own NC terms | Y3 matching and treatment effects |

**Bundled, no download:** the datasets that ship inside `statsmodels`, e.g. `macrodata`, US quarterly data
1959–2009. They arrive with the package install, which is not a data download. This is the same footing as
scikit-learn's bundled tables.

## B. Not proposed (dropped, with what replaces each)

| Source | Why | Replacement |
|---|---|---|
| Our World in Data | Most of its series are third-party, and it produces little itself | Not downloaded. Used to find each series' original source, which is then taken from row A or cited |
| UN World Population Prospects | Its terms pages are unreadable (404 or 403), so the licence could not be confirmed | WDI (row 3) carries WPP-based population, fertility and life expectancy; Gapminder covers before 1950 |
| ILOSTAT | 403 | WDI's ILO-modelled employment by sector, if its metadata allows |
| OECD data | 403 on every terms page | Eurostat, WDI, JST; OECD figures cited through the ledger |
| BIS statistics | 403 | JST rates; recent policy rates as cited facts |
| IMF (WEO, debt databases) | The terms forbid automated bulk download without permission, and the WEO page 404s | JST debt, revenue and spending since 1870; WDI. You may download a WEO file by hand if you want one |
| Bank of England Millennium dataset | No open licence; reuse needs a permission form | Cited facts through the ledger |
| Worldwide Governance Indicators | Third-party clause forbids republishing the values | Institutions chapters use cited study results, not a WGI chart |
| BEA | No reuse statement found; the API needs an e-mail | PWT, WDI, JST for national accounts |
| Census microdata (CPS, ACS) | The API key is requested by e-mail | Simulated data calibrated on published moments |
| World Inequality Database | No licence stated | PIP percentiles (row 4); top shares cited through the ledger |
| Barro–Lee | "All rights reserved" | WDI education series; cited facts |
| Federico–Tena trade database | Its pages are unreachable | JST exports and imports since 1870; pre-1870 numbers cited |
| Fraser economic freedom | 403 | Results cited from published studies |
| World Happiness Report | Data page 404; the Gallup survey is proprietary | A few country averages cited from the report through the ledger |
| Global Carbon Budget | No licence stated | CEDS (row 9) |
| Card–Krueger and the Angrist archive | No licence (copyright notice only, or "use with attribution") | Simulated data calibrated on the published tables, stated as such |

## C. Total

About 750 MB of raw files, almost all of it the WDI zip and CEPII Gravity. The derived tables should come to a few
MB.

## C. Second request, after the writers' Phase A (2026-11-20)

The licences were checked on each publisher's own pages; no data file was fetched. The same safety rules as section A
apply to every download: official hosts only, HTTPS, every redirect checked, macros and executables rejected, archives
listed before extraction, and a Defender scan afterwards.

| # | Dataset | Host and files | Licence as read | Used by | Verdict |
|---|---|---|---|---|---|
| C1 | Eurostat, seven more tables: `jvs_q_nace2` (vacancies), `une_rt_q`, `ilc_di12`, `ilc_di12b`, `ilc_di12c` (Gini before and after transfers), `ilc_pw01` (life satisfaction), `bd_size` (business demography) | ec.europa.eu, `api/dissemination/files` (gz TSV), the host already approved | Eurostat copyright notice: re-use with acknowledgement, including commercial | Book 4 Beveridge curve; Book 2 inequality and wellbeing; Book 1 firm survival; Book 5 wellbeing | OK |
| C2 | BLS: Average Price data `ap.*` (~24 MB), JOLTS `jt.*` (~100 MB), Consumer Expenditure tables by income fifth (xlsx) | download.bls.gov, bls.gov/cex | BLS copyright page: public domain, cite BLS | Book 1 retail prices; Book 3 budget shares; Book 4 vacancies (US) | OK |
| C3 | Federal Reserve Board H.15 (federal funds rate) and H.4.1 (balance sheet) | federalreserve.gov Data Download Program (CSV) | Board disclaimer: public domain unless indicated; cite the Board | Books 2, 3, 5: policy rate to 2025, balance sheets | OK |
| C4 | USGS Data Series 140, mineral prices (about 12 workbooks: copper, tin, nickel, tungsten, chromium, aluminium…) | usgs.gov National Minerals Information Center | USGS policy: USGS data are U.S. public domain; credit USGS | Book 5 resources chapter | OK |
| C5 | World Bank ICP 2021 (expenditure shares, price levels) | datacatalog.worldbank.org dataset 0066092 | Dataset page: CC BY 4.0 | Book 1 food share against income | OK |
| C6 | ECB balance-sheet total assets (weekly statement) | ECB Data Portal | ESCB reuse policy: free with source credited; derived numbers stated as ours | Book 5 central banking | OK, with conditions |
| C7 | World Bank Commodity Price Data (Pink Sheet), monthly and annual xlsx | thedocs.worldbank.org, linked from worldbank.org commodity-markets | No licence on the file's page; the World Bank's data catalogue says CC BY 4.0 is the default for World Bank datasets | Books 1–2: oil, maize, rice, soybean prices (six charts) | Probably OK (inferred) |
| C8 | FAOSTAT Producer Prices (PP) | FAO bulk download, the host already approved | FAO database terms: CC BY 4.0 unless the metadata says otherwise (the metadata page could not be read) | Book 3: crop prices | Probably OK (inferred) |

**Not proposed:**
- the Philadelphia Fed real-time data and Survey of Professional Forecasters ("All rights reserved"; educational use only, with permission needed to republish);
- the PIP global distribution file (771 MB, above the 400 MB cap; the nearest-survey method is used instead);
- the USITC tariff table (a PDF: its numbers can go through the ledger as cited values).

**Within the existing approval (row 8):** the BLS labour-force file `ln.data.1.AllData` (about 393 MB, under the cap), which
I left out at first only for its size. Book 3 needs it for job-finding and separation flows and the monthly unemployment
rate.
