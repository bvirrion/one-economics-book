# Book 1 (Grades 6–9) — progress log

Writer: the Book 1 agent (Opus 5.5). Run file: `sources/BATCH_BOOKS_1-5.md`. Briefs: `sources/book1/BRIEFS.md`;
definitions: `sources/book1/DEFINITIONS.md` (sync rulings applied 2026-11-20).

Web fetches so far: 122 (reader triage 2026-11-20: USDA ERS Charting the Essentials 1, ERS food-expenditure page 404 1, ERS chart of note 95223 1, ERS search 1, arXiv 1110.2096 re-read 1, Arkes–Blumer search 1, Arkes–Blumer 1985 paper copy 1, UNSD SNA 2025 page 1 (empty), SNA 2025 search 1, SNA 2025 implementation strategy PDF 1, ILOSTAT concepts 1 (403), ICLS search 1, 19th ICLS resolution PDF 1, EIA search 1 and annual product-supplied table 1; earlier: Phase A 4; Nordhaus 1996 PDF 1; Bourguignon–Morrisson search + failed fetch 2; World Bank poverty-lines factsheet 1; ILO child-labour pages 2 + search 1; Commons search, metadata and image download 3; g6-07: call-price searches 2, Papers Past, history.com (redirect, refused) and UPI Archives 3, Commons search, metadata and two downloads 4; g7-01: Arkes–Blumer search 1, ResearchGate 403 1, PMC redirect + bot wall 2, arXiv 1110.2096 PDF 1; g7-02: Ford time-study search 1, The Henry Ford artifact page 1, Commons search, metadata, a failed and a good download 4; g7-03: Bernhofen–Brown search 1, EconPapers abstract 1, author's PDF 1; g7-04: Radford search 1, gwern.net PDF 1, Commons coin search 1, BM-coin download (discarded: museum non-commercial note) 1, BnF coin download 1; g7-05: egg/avian-flu search 1, USDA ERS chart of note 1, wheat-ban search 1, USDA FAS GAIN RS1039 PDF 1, NPR (timeout) 1, PBS NewsHour 1; g8-01: Commons search 1, Commons metadata 1, LoC photo download 1; g8-02: UNSD SNA page 1 (empty), SNA 2008 PDF 1; g8-03: Rentenmark search 1, arXiv 2405.13296 PDF 1, Commons search 2, Commons metadata 1, banknote download 1; g8-05: ILO definitions page 1 (HTTP 403), BLS CPS definitions 1; g8-06: Federal Reserve open-market page 1, ECB key rates 1; g8-07: GOV.UK VAT 1, tobacco-elasticity searches 2, IARC chapter PDFs 2 (404), NCI Monograph 21 ch. 4 PDF 1; g8-08: EUR-Lex 1 (empty), directive search 1, CORDIS 1, FDA page 1, FDA search 1, FDA report PDF 2 (one 404); g9-01: JPE page 1 (403), Smith search 1, EconPapers 1, a scan of the article 1 (refused by the permission classifier, not read), Bergstrom 2002 PDF 1; g9-02: PMC Andreyeva 2010 1, IDEAS Havranek 2012 1, EIA search 1, EIA Today in Energy 1; g9-03: NBER w24181 1, Tankrabatt search 1, NCI chapter re-read 0, CESifo 1 (TLS error), ZEW 1; g9-04: NBER w25767 1, Commons API searches 2 + file metadata 1; g9-05: ECB euro page 1, World Bank ICP page 1; g9-06: Germany search 1, EC Economic Papers 170 PDF 1, Lin search 1, EconPapers 1, Commons search 1 + metadata 1; g9-07: PIP handbook 404 1, PIP search 1, PIP handbook ch. 2 1). Ledger rows: 88.

AI images: batch `g6` (9 images, grade 6) started detached 2026-11-20 with `tools/ai_images.py --book 1`; prompts logged
by the tool in `images/book1/ai/PROMPTS.md`. Each image is looked at before its chapter is closed.

## Chapters

### g6-01 Reading Economic Charts — done 2026-11-20
- Pages: body 2–11 (10 pp) + solutions about 2 pp. Build 0/0/0; `gates.sh grade-6` OK; `figdata.sh grade-6/01-…` OK.
- Charts (3): world population 1820–2022 (`maddison_regions` World `pop`, 21 points); regional shares of world population,
  five years (`maddison_regions`, years where all eight regions have an estimate: 1820, 1870, 1950, 1990, 2022 — the
  regional rows lack MENA/SSA in 1850–1940); UK income per person 1820–2022 on an ordinary and a times-ten scale
  (`maddison("GBR")`, `groupplot`).
- Diagrams (2): parts of a chart (invented line, labelled as invented); two rulers (ordinary vs times-ten).
- Images: AI `g6-reading-economic-charts-classroom.jpg` (looked at: no text, bar chart without numbers).
- Tests: `test_population.py` (4), `test_uk_income.py` (2).
- Ledger rows: none (all numbers figdata or invented).
- Changes from the brief: the shares chart is a 100 % stacked bar chart for five years (not a stacked area), because
  Maddison's regional population rows are incomplete before 1950; the problem has 12 questions (brief: 11); exercise 3
  adds percentage points (a remark in §1.2). The ledger row `g6:census-first` was not needed.
- Figures checked one per page at 110 dpi: anatomy diagram re-laid out twice (arrow tips on text), rulers' captions moved
  below the zero labels, groupplot second panel given its own width (the `omtimesten` style resets `width`).
- Coordinator's read (2026-11-20): two fixes applied (the UK two-scales example now gives the four factors and the
  larger-starting-value point; exercise 11(c) solution drops ``dollars'').

### g6-02 Two Hundred Years of Living Standards — done 2026-11-20
- Pages: body 12–20 (9 pp) + solutions about 2 pp. Build 0/0/0; `gates.sh grade-6` OK; figdata OK.
- Charts (4): long-run income 1300–2022, times-ten (`maddison(["GBR","NLD"], since=1300)` + `maddison_regions("World")`);
  five regions 1820–2022, times-ten (`maddison_regions`); six paths 1950–2022 (KOR, CHN, BWA, ARG, VEN, COD;
  `maddison`); labour price of light 1800–1992 (cited, `figdata/.../src/light.csv`, Nordhaus 1996 Table 1.6 p. 52).
- Diagram (1): UK take-off blocks (widths = years, heights = factor ×2.9 vs ×11.6, from the table values).
- Images: AI bakery and AI candle/lamp (both looked at; no text, no brands).
- Tests: `test_income.py` (3), `test_light.py` (1).
- Ledger rows: 9 (`g6:light-*`, source NORDHAUS1996).
- Changes from the brief: Italy dropped from chart 1 (adds nothing at grade 6; its pre-1800 points are 50 years apart);
  chart 2 shows five of the eight regions (eight lines unreadable), the other three named in text of g6-01; the bread
  and wage ledger facts were replaced by the light table (one source, a printed table, not a figure) — bread stays as
  an invented letter in the weekend problem; a fourth chart (light) added. Problem Part II question 7 has two
  answers (Venezuela and DR Congo were both poorer in 2022 than in 1950).

### g6-03 Poverty and How It Is Counted — done 2026-11-20
- Pages: body 21–28 (8 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK.
- Charts (3): world extreme-poverty rate 1981–2024 (`wdi("SI.POV.DDAY","WLD")`, 2019 missing, said in caption);
  people below and above the line, billions, stacked (`SI.POV.DDAY` × `SP.POP.TOTL`); rate by World Bank region and
  world (`SI.POV.DDAY`, EAS ECS LCN MEA SAS SSF WLD; gaps joined and said). Extra tables: `lines_2024` (SI.POV.LMIC,
  SI.POV.UMIC), `ssa_count`, Brenland `brenland_basket` and `brenland_bands` (from `country.load`).
- Diagram (1): basket of needs priced into a line (invented prices). Image: AI market (looked at).
- Tests: `test_poverty.py` (5). Ledger rows: 5 (`g6:pip-line-*`, source WB2025LINES).
- Changes from the brief: the two-century series (Bourguignon–Morrisson 2002, Table 3) is not drawn — the fetch failed
  and the AER table could not be read; the measure box says only ``a large majority'' in 1820, with the author–year
  citation, no number (no ledger row). The weekend problem's line is 5,000 dalens (basket 4,442.92 rounded up), raised
  by 20 % to 6,000; bands come from Brenland's survey (`households.csv`, disposable income per person).

### g6-04 Longer Lives, Smaller Families — done 2026-11-20
- Pages: body 29–36 (8 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK.
- Charts (3): life expectancy, six Gapminder regions + world, 1800–1949 (`gapminder("lex")` × `gapminder("pop")`) and
  1960–2024 (`wdi SP.DYN.LE00.IN` × `SP.POP.TOTL`, countries mapped to Gapminder's six regions; world = WLD), two tables
  so 1950–59 stays empty; child mortality vs income 2024, 186 countries (`SH.DYN.MORT`, `NY.GDP.PCAP.PP.KD`,
  `omincomex`); births per woman, WB regions + world 1960–2024 (`SP.DYN.TFRT.IN`). Facts table: Gapminder child
  mortality 1800 range (322–540), urban share 1960/2025 (`SP.URB.TOTL.IN.ZS`), old-age dependency 1960/2024
  (`SP.POP.DPND.OL`).
- Diagrams (2): population tank; two invented towns by age group. Image: AI three generations (looked at).
- Tests: `test_health.py` (4). Ledger rows: none (the optional influenza row not needed: prose says ``tens of millions'').
- Changes from the brief: the problem's register ages changed (80 → 81) so that the average is not a rounding tie.

### g6-05 School and Work — done 2026-11-20
- Pages: body 37–43 (7 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK.
- Charts (3): adult literacy 1975–2024, five WB regions + world (`SE.ADT.LITR.ZS`); hours per worker 1950–2023, six
  countries (`pwt(..., cols=["avh"])`); China's employment by sector 1991–2025, stacked (`SL.AGR/IND/SRV.EMPL.ZS`).
  Facts: women's labour-force participation, world, 1990/2025 (`SL.TLF.CACT.FE.ZS`); year services passed farming (2011).
- Diagram (1): three sectors with arrows. Images: AI classroom (looked at); **photograph**: Lewis Hine, breaker boys,
  1911, Commons / Library of Congress nclc.01138, public domain (`images/book1/photos/`, CREDITS.md and the
  image-credits page updated). AI tractor **not used**: its green body and red wheels look like a real tractor make,
  and the bonnet carries a small unreadable label.
- Tests: `test_work.py` (4). Ledger rows: 4 (`g6:ilo-child-labour-*`, ILO and UNICEF 2025, 2024 estimates).
- Changes from the brief: no two-century series (van Zanden 2014, Huberman–Minns 2007, Lebergott: none fetched; the
  charts start in 1950/1975/1991 and the prose says what happened before in words only); no years-of-schooling
  number (no source fetched); the weekend problem has 11 questions as briefed; the child-labour figure is the 2024
  estimate (138 million), not the 2020 one (160 million).

### g6-06 Food and Energy — done 2026-11-20
- Pages: body 44–51 (8 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK.
- Charts (4): cereal yields 1961–2024, FAO areas (`faostat_crops`); energy use vs income 2024, log–log, 141 countries
  (`EG.USE.PCAP.KG.OE`, `NY.GDP.PCAP.PP.KD`); US food spending as a share of income by income quintile, 2025
  (`cex_table("mean-item-share-average-standard-error", 2025)`, table 1101); SO₂ 1850–2023, five countries
  (`ceds("so2")`). Facts: SO₂ peaks, CO₂ per person 2023 (`ceds("co2")` ÷ `SP.POP.TOTL`), water withdrawal 2022
  (`ER.H2O.FWTL.ZS`). Brenland food shares by quarter of disposable income (problem).
- Diagram (1): two invented budget pies. Image: AI harvest (looked at; see below).
- Tests: `test_food_energy.py` (5). Ledger rows: none.
- Changes from the brief: the food-share chart uses the BLS quintile table (approved, C-list) instead of ICP;
  cross-country food shares are told in words with `% PENDING-DATA: World Bank ICP 2021`; famine is told in words
  (no famine-deaths ledger row: no source fetched); a fourth chart (SO₂) kept as a chart, CO₂ in prose.
- The first AI harvest image showed a yellow combine and a red tractor whose colour schemes recall real makes; it was
  regenerated as `g6-food-and-energy-harvest-plain.jpg` (plain grey machines, looked at) and the chapter uses that. The
  old file `g6-food-and-energy-harvest.jpg` is unused (as is the g6-05 tractor); Phase C decides whether to delete them.

### g6-07 A Connected World — done 2026-11-20
- Pages: body 52–60 (9 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK (6 tests).
- Charts (3): trade share 1870–2024, the median of the 18 JST economies (1870–2020) and the world (`NE.TRD.GNFS.ZS`,
  1970–2024); mobile subscriptions per 100 (`IT.CEL.SETS.P2`, split 1987–1999 / 2005–2024: the WLD aggregate is missing
  2000–2004, said in the caption) and internet users (`IT.NET.USER.ZS`, 2005–2024); computer prices relative to all
  items, euro area, 1996 = 100, times-ten scale (Eurostat `prc_hicp_aind`, CP0913 ÷ CP00, EA). Facts: JST and world
  shares, Singapore 313.3 % (2024), mobile passes 50 in 2007, US CPI-U 1927 17.4 and 2025 321.9 (`bls_cpi`, M13), so the
  1927 call of 75 dollars ≈ 1,388 dollars of 2025. Brenland trade 2000/2025 from `accounts` and `trade` (problem).
- Diagram (1): a container's journey (factory → port → port → shop, the same box on each leg).
- Images: photograph of the Port of Miami container port (James R. Tourtellotte, CBP, public domain, Commons; credited in
  CREDITS.md and `image-credits.tex`); AI video call (looked at, no text on the screen).
- Ledger: `g6:call-london-ny-1927` (UPI1927 wire story: flat 75 dollars for the first three minutes).
- Changes from the brief: no freight-cost series (Hummels 2007 not fetched); the fall in shipping cost is told in words
  (the container) with no number. The light chart is recalled from g6-02 instead of a new light or solar chart; the
  computer-price chart is the brief's `[A]` option. *container* is explained in prose, not a definition box (it is not in
  the definition map).

### g7-01 Scarcity and Opportunity Cost — done 2026-11-20
- Pages: body 61–67 (7 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart: hours worked per worker vs income per person, 2023, 130 countries (PWT 11.0 `avh`, `rgdpe/pop`),
  `omincomex`. Second chart: US food away from home as a share of food spending by income quintile, 2025
  (`cex_table`, table 1101): 30.2 → 44.0 %, monotone — the model's *tested* field for time-saving purchases.
- Diagrams (2): the 24 hours of an invented school day; Lina's choice set (a three-option tree, plain TikZ, no `forest`).
- Image: AI teenager with a ball, a book and a blank ticket (looked at; the ball is an American football, no text).
- Model box `Choosing by opportunity cost` (assumes / predicts / tested / breaks).
- Ledger: `g7:arkes-blumer-1985` (ARKES1985, the field study as described in Herrmann and Kundisch 2011, arXiv:1110.2096:
  first 60 customers, random discounts, the smallest discount attended the most plays). The paper's per-group play
  counts were not verified (publisher and ResearchGate refused), so the text prints none.
- Changes from the brief: the `g7:time-saving-goods` ledger row (a time-use paper) is replaced by the BLS food-away
  chart (approved data, no fetch); no ATUS chart (not approved); the choice tree uses plain TikZ.

### g7-02 Specialisation and the Division of Labour — done 2026-11-20
- Pages: body 68–74 (7 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart: farm share of employment vs income per person, 2024, 171 countries (`SL.AGR.EMPL.ZS`,
  `NY.GDP.PCAP.PP.KD`), `omincomex`. Second chart: people per farm worker, five countries (USA, KOR, BRA, CHN, IND),
  1991–2024, times-ten scale: `SP.POP.TOTL` ÷ (farm share × `SL.TLF.TOTL.IN` × (1 − `SL.UEM.TOTL.ZS`)); the method is in
  the source line, and the text says it is not "people fed".
- Diagram (1): the four-station workshop line of the worked example (numbers match: 16 → 20 trains per worker).
- Images: photograph — *Épinglier* plate II (Goussier/Defehrt, 1762, PD, Commons; caption describes the plate, names no
  person; the credit page names the engravers); AI — bakery with three bakers at three steps (looked at, no text).
- Model box `Specialisation and the size of the market`.
- Ledger: none. Changes from the brief: no `g7:usda-one-farmer-feeds` (replaced by the WDI people-per-farm-worker
  chart, approved data); no `g7:time-study` — the sources found for the 1913–14 chassis times disagree (12 h 28 min →
  84 or 93 minutes, at different dates) and no primary page was reachable, so the *tested* field rests on the two charts.

### g7-03 Gains from Trade: Comparative Advantage — done 2026-11-20
- Pages: body 75–81 (7 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart: exports (% of output) vs population, 2024, 172 countries (`NE.EXP.GNFS.ZS`, `SP.POP.TOTL`), times-ten
  x-axis. Second chart: Brenland and Kestria hours per unit (`country/ricardo.csv`, invented, labelled so).
- Diagrams (2): Nadia's and Omar's hours as bars; the exchange-ratio number line (2 to 3 loaves per shirt shaded, the
  example's 2.5 marked).
- Image: AI neighbours swapping apples and bread over a fence (looked at, no text).
- Model box `Comparative advantage, two people and two goods`; `record[Japan opens to trade]`; `measure[Hours per unit]`.
  David Ricardo is named once, as the label of the result (sync ruling); "Ricardo's model" is not named.
- Ledger (4, BERNHOFEN2004): `g7:japan-opening-1859` (July 1859), `g7:bernhofen-brown-2004` (negative autarky-price value
  each year 1868–1875), `g7:japan-exports-silk-tea` (about 80 % of exports), `g7:japan-imports-textiles` (about half of
  imports). Read from the author's PDF copy (text) and the EconPapers abstract.
- Changes from the brief: none of substance; the "two regions" section presents Brenland and Kestria, and the weekend
  problem works them through (120 million hours each; gains 10 and 5 grain at 1 grain per cloth).

### Page projection at chapter 10 (2026-11-20)
- Chapters 1–10: body pages 1–81, so 8.1 pp per chapter; their solutions take about 15 pp (1.5 pp per chapter).
- Projection for 30 chapters: about 243 pp of chapters + 46 pp of solutions + front matter and index (about 15 pp):
  **about 305 pp**, against the plan of about 300 pp. No action needed; grades 8–9 chapters carry more model work and
  may run slightly longer, so g8–g9 keep to 8 pp each.

### g7-04 Money — done 2026-11-20
- Pages: body 82–88 (7 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart: account ownership, 2011 and 2024, ten countries and the world (`FX.OWN.TOTL.ZS`, Findex), horizontal
  bars sorted by 2011; `dated{2026}` box beside it. `barter.csv` (rates n(n−1)/2) backs the prose counts.
- Diagram (1): three traders in a barter circle vs the same three with money.
- Images: photograph — Lydian electrum trite, BnF Gallica btv1b8502096t, public domain (the British Museum photo on
  Commons was not used: its description carries a museum note restricting commercial use); AI barter market (looked at).
- Model box `Money as a means of exchange`; `record[Cigarettes as money]`; `measure[An account]`.
- Ledger (4): `g7:radford-1945`, `g7:radford-issue` (25 or 50 cigarettes a week), `g7:radford-bread` (7 → 8 cigarettes),
  from the paper's text (RADFORD1945); `g7:lydian-coin-date` (ca. 600–530 BC, British Museum record, BMLYDIA).
- Changes from the brief: no cash-share chart (ECB SPACE / Fed Diary not fetched, `[L]`); the `[A]` account chart is
  used. No "dollar use in high inflation" evidence (no source fetched); the *breaks* field points to grade 8 instead.

### g7-05 Markets and Prices — done 2026-11-20
- Pages: body 89–95 (7 pp) + solutions about 2 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart: US average price of a dozen grade A large eggs, monthly, 2019-01 to 2026-10 (`bls_ap`); October 2025 was
  not collected, so the series is two tables (`eggs_a`, `eggs_b`, the second with `forget plot`), said in the caption.
  Second chart: wheat production in Russia, Kazakhstan and Ukraine, 2005–2015 (`faostat_crops`). Facts: world wheat
  production 2009–2011 and world area harvested 2010–2011.
- Diagram (1): the price signal (rise → buyers use less, sellers bring more → shortage shrinks).
- Image: AI morning fruit market (blank chalk boards, looked at). No fish-auction photograph (not fetched; the AI image
  and the auction exercise carry the idea).
- Model box `Prices as signals`; `record[The 2010 wheat harvest]`; `measure[A world price]`. The information result
  (section 4) is told as a positive result, with no reference to any debate.
- Ledger (5): `g7:hpai-hens-lost` (more than 43 million hens) and `g7:egg-wholesale-2022-2023` (5.37 → 0.89 dollars),
  USDAERS2023; `g7:russia-export-ban-2010` (15 August – 31 December 2010, Resolution 599), USDAFAS2010;
  `g7:wheat-price-2010` (almost doubled June → early August) and `g7:fao-wheat-forecast-2010` (676 → 651 Mt), PBS2010.
- Changes from the brief: the Pink Sheet was refused, so the opening chart is the BLS egg price (approved) and the 2010
  wheat episode is a `record` box with the FAOSTAT production chart; the "area response of other exporters" chart was
  dropped (FAOSTAT shows no clear rise outside Russia; the text quotes the world area instead). The 2024–25 egg-price
  rise is described without a cause (no source fetched for it).

### g7-06 Demand and Supply: A First Look — done 2026-11-20
- Pages: body 96–102 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart: US average price of a 12-oz pint of strawberries, each month of 2022, 2023 and 2024 (`bls_ap`), one
  line per year (cheapest June–July, dearest December–January). Second chart: the invented Brenmoor demand and supply
  tables (seeded in the script, `berry_tables`), plotted point by point.
- Diagram (1): demand shift after a heat wave, geometry matching the example (600 at 3 → 800 at 4 dalens).
- Image: AI strawberry stall with a scale (no text, looked at).
- Box: `measure[Quantity demanded is a plan]`. No model box (g9-01 has it); the chapter names its predictions and points
  to the full model.
- Ledger: none (BLS series is in the approved list; no cited value).
- Changes from the brief: the `[N]` BLS option worked (price only), so no invented opening chart; the USDA volume table
  `[L]` was not used, and exercise 12 turns the price-only chart into the "which curve moved" question.
- Trap met: `x tick label style={font=...}` inside an `omtime` axis is a fatal error (the style routes tick labels
  through /pgf/number format); use `omrecord` for month axes.

### g7-07 Households: Income, Spending and Saving — done 2026-11-20
- Pages: body 103–109 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (3 tests).
- Opening chart: budget shares (food, housing, health care, insurance and pensions) by fifth of income, US 2025
  (`cex_table`, Table 1101 shares). Second chart: sources of income before taxes by fifth, stacked (same table).
  Third chart: Brenland Engel scatter (2,000 households) with quarter means (invented, `country.load("households")`).
- Diagram (1): gross → taxes, transfers → disposable → spending, saving (worked example 30,000 / 3,000 / 1,000 /
  28,000 / 26,000 / 2,000 dalens, used in the budget-share example).
- Image: AI family sorting receipts at a kitchen table (no readable text, looked at).
- Model box `Engel's law` (carries the label `def:g7:households:engels-law`); `measure[A household budget survey]`
  (the bottom fifth reports 18,125 dollars of income and 37,935 of spending).
- Ledger: none (CEX is approved; the brief's `g7:bls-cex-quintiles` rows were not needed).
- Changes from the brief: real CEX data replaced both `[I]` fallbacks for the opening chart; added the income-sources
  chart (wages 31.2 → 83.4 %, retirement 56.4 → 2.8 %). "Personal insurance and pensions" is described as payments into
  insurance and pension systems charged mostly on wages (it includes Social Security contributions), not as saving.
  Problem uses survey households 1, 2, 4, 6, 9 (relabelled A–E).

### g7-08 Firms: Costs, Revenue and Profit — done 2026-11-20
- Pages: body 110–117 (8 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (3 tests).
- Opening chart: of 100 enterprises born in 2021, still active after 1–3 years, EU, NL, IT, DE, FR (Eurostat `bd_size`,
  ENT_SRVLR_BRTH_CHB_PC, business economy B-S_X_O_S94). Second chart: EU three-year survival by sector (11 NACE
  sections, horizontal bars). Facts: EU births 3.4 million and 31.5 million firms in 2021; Finland 2019 cohort 53.1 after
  five years (only FI, IS, TR have five-year cohorts).
- Brenland firm census (invented) quoted in text: 69 of 326 service firms with a loss (21.2 %), 1 of 123 manufacturing,
  0 of 51 farms (`brenland_sectors.csv`, not charted: three charts were enough).
- Diagram (1): bakery revenue and total cost lines drawn from the table points (price 2, fixed 3,000, 0.80 per loaf),
  break-even at 2,500 loaves.
- Image: AI bakery before dawn (no text, looked at).
- Model box `Entry and exit`; `measure[Profit in a firm's accounts]` (opportunity costs of the owner's time and money).
- Ledger: none (Eurostat `bd_size` is approved).
- Changes from the brief: the `[N]` Eurostat option replaced the BLS BED `[L]` table (approved 2026-11-20, no fetch);
  EU cohort data stop at three years, so the chart shows 1–3 years and the five-year figure is Finland's. Juice-stall
  problem: rent 600, 1.00 per cup; prices 2.50/3/4 with 600/500/250 cups; second stall: 280 cups at 3 (loss 40), 420 at
  2.50 (profit 30), break-even 400.
- Grade 7 complete (8 chapters, body pp. 61–117).

### g8-01 Production and Productivity — done 2026-11-20
- Pages: body 118–124 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (3 tests).
- Opening chart: output per hour (rgdpo / (emp × avh)) against income per person (rgdpe / pop), 2023, PWT 11.0,
  129 countries, log-log, 9 labelled. PWT `i_outlier == "Outlier"` rows dropped (Venezuela). Second chart: capital per
  worker (rnna / emp) against output per worker, 173 countries, 5 labelled.
- Diagram (1): four factors → production → output.
- Images: photograph of a 1913 car assembly line (Library of Congress via Commons, PD; credits in CREDITS.md and
  image-credits.tex; caption names no person or firm); AI sickle beside small grey tractor (no logos, looked at).
- Model box `Productivity and living standards`; `measure[Output per hour]`, `measure[Measuring capital]`.
- Ledger: none (PWT).
- Changes from the brief: the problem's Part III moves 500 service workers to manufacturing instead of 10 % of farm
  workers, because in Brenland's census farming has the highest output per worker (104.4 thousand dalens), so the
  brief's move would lower the average and contradict the exercise it sets up; exercises 10–11 keep the classic
  farm-to-factory case with invented numbers. The assembly-line time saving is not quoted (sources disagree, as in
  g7-02).

### g8-02 Measuring an Economy: GDP — done 2026-11-20
- Pages: body 125–131 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart: the ten largest economies by GDP at PPP 2024, total (trillions) and per person (thousands), two
  side-by-side horizontal-bar axes (WDI NY.GDP.MKTP.PP.KD, NY.GDP.PCAP.PP.KD). Facts: world 174.2 trillion, top ten 60.8 %.
  Second chart: Brenland 2025 spending items as signed horizontal bars (C, I, G, X, −M, GDP; invented accounts).
- Diagrams (2): wheat → flour → bread chain with sales bars split into bought-in and value added (300/200/400); circular
  flow of households and firms (money solid, goods and work dashed).
- Image: AI mill, bakery and grocery in one street (no text, looked at).
- Boxes: `measure[How GDP is measured]` (SNA 2008, imputed rent, household services omitted), `measure[What GDP leaves
  out]`. No model box (accounting).
- Ledger (2): `g8:sna-2008` (adopted unanimously at the fortieth session of the UN Statistical Commission) and
  `g8:sna-household-services` (para. 1.41), source SNA2008.
- Changes from the brief: the Brenland chart shows each spending item as a signed bar rather than one stacked bar
  (net exports are only 0.3 % of GDP and would not show). Problem Part I is an apple-juice chain with a glass works.

### g8-03 Inflation and Price Indices — done 2026-11-20
- Pages: body 132–138 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (3 tests).
- Opening chart: consumer-price inflation 1920–2020, US, UK, France, Japan (JST `cpi`), y clipped at 60 % (Japan
  1945–48 off the chart, said in the caption). BLS CPI-U (M13) gives 2021 4.7 %, 2022 8.0 %, 2025 2.6 % in prose.
  Second chart: Germany's price level 1914–1923, 1914 = 1, times-ten scale (1923 average 1.55 × 10^11).
- Diagram (1): the same three-good basket priced in 2020 and 2025 (40 → 48 dalens), used for the index and the
  weighted-average check.
- Images: photograph of a 100-milliard-mark Reichsbank note dated 26 October 1923 (Commons, PD, National Numismatic
  Collection credit requested and given; denomination and date read off the note); AI supermarket shelf with blank
  labels (looked at).
- Box: `measure[The consumer price index]`. No model box (the brief's choice); the money cause is pointed to the grades
  10–12 volume in prose.
- Ledger (3): `g8:rentenmark-issue` (15 November 1923), `g8:rentenmark-rate` (10^12 paper marks),
  `g8:rentenmark-dollar` (4.2 per dollar), source BRUNNERMEIER2024 (arXiv). Online dates disagree (15/16 November),
  so the paper's date is used. Zimbabwe row not used.
- Defines real GDP here too (DEFINITIONS row 125).
- Changes from the brief: the optional US CPI-since-1913 chart was not drawn (three charts would crowd the chapter);
  Brenland basket problem ends with the real wage change (+4.5 %) after a no-rent household question (+45.5 %).

### g8-04 Growth and Compounding — done 2026-11-20
- Pages: body 139–144 (6 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart: real GDP per person 1960–2024 (WDI NY.GDP.PCAP.KD), times-ten; countries picked by a tested rule
  (closest average growth to 1, 2, 6 % among ARG, MEX, USA, FRA, KOR, CHN): Argentina 0.86 %, United States 1.99 %,
  South Korea 5.75 %. Second chart: simple vs compound growth bars (computed). Third: US GDP per person 1820–2022
  (Maddison) with the steady 1.66 % path from 1870 (dashed).
- Image: AI door frame with yearly pencil marks (no numbers; portrait output, printed at 0.34 width; looked at).
- Proposition `Rule of 70` with `\admitted`; model box `Steady growth`; `measure[Real GDP per person]`.
- Ledger: none.
- Changes from the brief: the brief's "US near 2 % for 150 years" is 1.66 % in Maddison (1870–2022), so the text uses
  1.66 % and a 42-year doubling; the 1929–33 dip stays below the steady line until the 1940s (said so). The compound
  "staircase" diagram is a pgfplots bar chart over the computed table. Kestria's series is invented in the script
  (6,000 → 16,000, seeded wobble); the problem's catch-up year at 1 % and 4 % is 2049.

### g8-05 Jobs, Wages and Unemployment — done 2026-11-20
- Pages: body 145–151 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (5 tests).
- Opening chart: unemployment rate 1970–2020, US, UK, Germany, Spain, Japan (JST `unemp`). **Data defect found:** JST R6
  prints 2.0 for the United States in 2019 (the national figure is 3.7; every other US year matches within a tenth). The
  script replaces that one value with WDI SL.UEM.TOTL.NE.ZS (3.669), says so in its docstring, a test guards it, and the
  chart's source line names WDI for that point. Worth a line in the run file's Traps section (other books using
  `jst(cols=["unemp"])` for the US).
- Second chart: three panels (US, UK, Sweden), real wage (JST `wage`/`cpi`) solid and real GDP per person (`rgdpmad`)
  dashed, 1870–2020, 1913 = 100, times-ten. 2020: wages 4.6/4.6/14.2, GDP per person 6.3/4.8/9.4 times 1913.
- Diagram: Brenland 2025 population split (under 15 / outside / employed / unemployed) with labour-force and
  aged-15-and-over braces. The accounts have no age split: children under 15 are invented in the script as 16 % of the
  population (1,490 thousand), said in the caption; participation 59.5 %.
- Brenland survey (households with a working head) gives median household income by the head's schooling (20,430 →
  40,430) for "Why wages differ", with the caveat that it shows association only.
- Image: AI job fair (no text; looked at). Box `measure[The labour force survey]`.
- Ledger (2): `g8:bls-unemployed-search` (4 weeks), `g8:bls-labour-force-age` (16), source BLSCPSDEF. The brief's ILO
  resolution row: the ILOSTAT page refused the fetch (403), so the box quotes the US survey's rules and says other
  countries use the same three tests.
- Changes from the brief: ledger source is BLS rather than the ICLS resolution (above); the problem's Part III gives a
  seven-year table (2000, 2008, 2009, 2012, 2020, 2021, 2025) so the "highest year" question needs computing (2020,
  8.8 %).

### Page projection (at chapter 20, 2026-11-20)
- Now: 207 physical pages with 20 chapters written (body 1–151 printed, 7.0 pp per chapter on average including part
  pages; solutions about 1.4 pp per chapter; 11 front-matter pages).
- Ten chapters left (g8-06 to g9-07) at the same rate: body +70 pp, solutions +14 pp → about **290 physical pages**
  (about 280 printed), inside the brief's "about 300 pp". No cut needed; grade-9 chapters with equations may run a page
  longer each, which still lands under 300.

### g8-06 Banks, Saving and Interest — done 2026-11-20
- Pages: body 152–158 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (3 tests).
- Opening chart: long-term government rates 1870–2020, US, UK, France, Germany, Italy (JST `ltrate`). **Japan left
  out** (brief listed it): its JST long rate jumps between about 6 and 15 % year to year in 1953–1963 (a series break),
  noted in the script. Second chart: US long minus short rate, 1870–2020, bars (103 of 151 years above zero; 1873
  −8.76, 1929 −4.29, 1979–81 below zero).
- Diagram: an invented bank's two columns (deposits 1,000; loans 900 + 100 kept at hand). The simple vs compound
  "staircase" is a table (1,000 at 5 %, years 0–3, 10, 20) because g8-04 already draws that bar chart.
- Image: AI bank counter (no text or logos; the clerk hands the form, caption says so; looked at).
- Boxes: `measure[A government bond's rate]`; `dated{2026}` ECB deposit facility rate 2.50 % from 16 September 2026.
  The Fed page was also read (3.75–4.00 % since 17 September 2026) but not used; only the ECB row is in the ledger.
- Model `Risk and the interest rate`. The real interest rate is only "the interest rate minus inflation" in words.
- Ledger (1): `g8:policy-rate-2026`, source ECBKEYRATES.
- Note for the record: JST US `cpi` gives 11.2 % inflation for 1980 and 9.4 % for 1981 (the official CPI-U says 13.5
  and 10.3; JST seems to use a research series). The exercise prints the JST numbers with the JST source implied; no
  claim quotes the official figure.

### g8-07 Taxes and Public Spending — done 2026-11-20
- Pages: body 159–165 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart: central government spending / GDP, 1880–2020, US, UK, France, Sweden, Japan, Germany (JST
  `expenditure`/`gdp`); caption says "central government", `measure[General and central government]` explains why
  Germany's line is low. Second chart: public debt / GDP, same six (JST `debtgdp` × 100): UK 269.8 % in 1946, France
  237.0 % in 1921, US 128.1 % and Japan 253.9 % in 2020. Third: Brenland's marginal income-tax rate as a step chart
  (`TAX_BANDS`).
- Diagram: the debt bathtub (deficit pours in, surplus drains). Image: AI town street with school, road crew, clinic
  (no text; looked at).
- `dated{2026}`: UK standard VAT 20 % (since 4 January 2011). Model `Taxes change behaviour`, tested with the NCI/WHO
  Monograph 21 (2016) consensus: −0.4 in high-income countries, most estimates −0.2 to −0.6 (author–year citation in
  the box). "Who decides" names government failure in one sentence and points to the grades 10–12 volume.
- Ledger (2): `g8:cigarette-tax-elasticity` (source NCI2016M21), `g8:vat-rate-2026` (source GOVUKVAT).
- Changes from the brief: the ★★P exercise uses cigarettes, not sugary drinks, so that it rests on the one ledger
  estimate; the ★★X exercise is an invented evasion case matched against the "breaks" line. Problem has 13 questions as
  briefed (2015/2019/2020/2025 table; debt share 62.9 → 72.0 % in 2020; tax 3,600 and 12,600, average 12.0 and 21.0 %).

### g8-08 Competition and Monopoly: A First Look — done 2026-11-20
- Pages: body 166–171 (6 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (3 tests). Grade 8 complete.
- Opening chart (the brief's `[A]` fallback): real price of telephone services (HICP CP0830 ÷ CP00), Germany, France,
  Italy, 1996–2025, 1996 = 100, dashed line at 1998 (Eurostat prc_hicp_aind): 2025 at 31.1 / 29.1 / 38.5; Germany's
  steepest falls in 1999–2000. Second chart: the invented juice market (demand 1000 − 200p, cost 1.00), single seller
  M (3.00, 400) vs many sellers C (1.00, 800), from figdata tables.
- Image: AI two coaches at one stop (no text); generated with white letterbox bands, cropped to 1536 × 844 with ffmpeg.
- Boxes: `measure[A real price]`; `record[Opening the telephone market]` (Directive 96/19/EC, 1 January 1998, and the
  caveat that technology also cut costs). Model `Competition and entry` tested with the telecom chart and the FDA 2019
  generic-entry figures (39 / 54 / 79 / > 95 % below the brand price; Conrad and Lutter, 2019).
- Ledger (2): `g8:eu-telecom-1998` (source CORDIS1996TEL; EUR-Lex returned an empty page), `g8:generic-entry-price`
  (FDA2019GEN). `g8:airline-deregulation-1978` not used: the model is tested with telecom and medicines instead.
- Changes from the brief: the "juice stall of g7-08 with one vs five sellers" became a new invented juice market with
  no fixed cost (with g7-08's rent of 600 a month, five stalls cannot all cover costs, which muddles the point). The
  ferry problem keeps the brief's three parts but puts "the threat of entry" before "two companies", so it ends with
  the two-firm fare (20 dalens) and passengers (300) as briefed.

### g9-01 Demand and Supply with Equations — done 2026-11-20
- Pages: body 173–179 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart (brief's `[A]` fallback, narrowed): France only, 2000–2010 — real price of mobile telephone equipment
  (HICP CP08202 ÷ CP00, 2000 = 100; France is the only country with CP08202 from 2000) against mobile subscriptions per
  100 people (WDI IT.CEL.SETS.P2, FRA), a connected scatter labelled every second year: price 100 → 9.3, subscriptions
  48.8 → 91.1 (flat after 2008, used in exercise 12).
- Second chart: the worked example (demand 120 − 4p, supply 20 + 6p, shifted supply 40 + 6p; equilibria (80, 10) and
  (88, 8)) from a figdata table. Diagram: the four shocks in a 2 × 2 TikZ panel with old (grey) and new (black)
  equilibria.
- Proposition with proof: p* = (a − c)/(b + d). Model `Supply and demand` (Book 1's full frame). `measure[Reading a
  slope]`; `record[Laboratory markets]` (Smith, 1962, cited author–year; facts from Bergstrom 2002, since the JPE page
  refused the fetch).
- No image: the brief's photograph was tied to the solar case, which needs unapproved IRENA tables.
- Ledger (1): `g9:smith-1962` (source BERGSTROM2002; bibliographic row SMITH1962).
- Problem: Brenmoor fish market, 13 questions: Q^d = 1000 − 50p, Q^s = 50 + 75p → (7.6, 620); new harbour 175 + 75p →
  (6.6, 670); fishermen's revenue 4,712 → 4,422.

### g9-02 Elasticity: A First Look — done 2026-11-20
- Pages: body 180–186 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (2 tests, one checks every
  plotted elasticity against its ledger row).
- Opening chart (the brief's `[L]`, cited): 19 published price elasticities as horizontal bars — 16 US food categories
  (Andreyeva, Long and Brownell 2010, Table 1), cigarettes 0.4 (reuses `g8:cigarette-tax-elasticity`), gasoline 0.09
  short run and 0.31 long run (Havranek, Irsova and Janda 2012). Elasticities printed as positive numbers, said in the
  text. Second chart: revenue along the invented demand 1200 − 100p (peak 3,600 at 6). Diagram: steep vs flat demand
  with the same price rise.
- Image: AI fuel station (blank pumps; car badges unreadable at print size; looked at).
- Boxes: `measure[An elasticity from data]`; `record[Fuel prices in 2022]` with BLS average prices (3.05 → 4.09, +34.1 %)
  and EIA's statement that 2022 consumption was lower than 2021 (EIA's own 2022 average, 3.95, is not printed so the
  box uses one price source). Model `Elastic and inelastic demand` tested with South Africa 1991–2012 (legal sales
  −42 %, industry real revenue +95 %; NCI/WHO 2016).
- Ledger (20): `g9:andreyeva-2010-*` (16), `g9:fuel-elasticity-short`, `-long`, `g9:eia-gasoline-2022`,
  `g9:south-africa-cigarettes`; sources ANDREYEVA2010, HAVRANEK2012, EIA2023GAS.
- Definitions add *unit-elastic demand* (DEFINITIONS row 177). Necessity and luxury defined by budget shares, linked to
  Engel's law (g7-07).
- Changes from the brief: the "revenue rectangles" diagram is replaced by the revenue bar chart (same point, from a
  table). An unsourced sentence on restaurant meals as a luxury was cut.

### g9-03 Price Controls, Taxes and Subsidies — done 2026-11-20
- Pages: body 187–193 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (2 tests; one checks the
  plotted estimates against the ledger).
- Opening chart (the brief's `[L]`, cited): three published estimates for San Francisco's 1994 rent-control extension
  (Diamond, McQuade and Qian 2019, from the NBER abstract): renters staying +nearly 20 % (plotted 20, said "nearly"),
  covered landlords' rental supply −15 %, city-wide rents +5.1 %. The brief's details (pre-1980 small buildings) are
  not in the fetched abstract, so the caption only says "more rental buildings ... similar buildings not covered".
- Other charts: the tax wedge on the g9-01 worked example (tax 5: buyers 13, sellers 8, 68 units) from a figdata table;
  invented milk floor (unsold milk and the government's growing stock, 8 years). Diagram: ceiling at 8 with the
  shortage 68 → 88. Image: AI queue outside a bakery at dawn (no text; looked at).
- Models `A price ceiling` and `A tax per unit`. **Brief formula corrected:** with Q^d = a − bp and Q^s = c + dp, a
  tax t raises the buyers' price by t·d/(b + d) (the brief's t·b/(b + d) is the sellers' share); the chapter prints both
  shares correctly. Tax model tested with Germany's 2022 fuel-tax cut (Dovern et al. 2023: complete pass-through for
  gasoline, at least partial for diesel); `record[A fuel tax cut]` says the same, no cents per litre (not in the
  fetched source).
- The brief's second record (rent control) is folded into the opening paragraph and the ceiling model's test.
- Ledger (4): `g9:dmq-2019-stay`, `-supply`, `-rents` (DMQ2019), `g9:fuel-tax-cut-2022` (DOVERN2023).
- Problem: bread in a hard winter, 13 questions: Q^d = 7000 − 1000p, Q^s = −2000 + 2000p → (3.00, 4,000); ceiling
  2.50 → shortage 1,500, black-market price 4.00; subsidy 0.75 a loaf costs 3,375 a day.

### g9-04 International Trade — done 2026-11-20
- Pages: body 207–213 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (4 tests).
- Opening chart (`[A]` as briefed): South Korea's merchandise-export mix, 1965 vs 2024, paired horizontal bars (WDI
  TX.VAL.*.ZS.UN; manufactures 59.3 → 87.3 %, food 16.7 → 1.6 %). Second chart: applied weighted-mean tariffs
  1988–2022 for India, China, Brazil, United States, European Union (WDI TM.TAX.MRCH.WM.AR.ZS). **WDI has no World
  aggregate for this series**, so the brief's "world" line is dropped. **Data defect:** WDI gives the United States
  13.78 % for 2019 between 1.59 (2018) and 1.52 (2020); left out as a series break, tested, said in the source line
  (candidate for the run file's traps). Missing years are written `nan` so the lines break. Third chart: the
  small-country tariff on Brenland's invented cloth market (100 − 5p, 5p − 10, world price 6, tariff 2: imports 50 → 30,
  revenue 60) from a table.
- Remittances paragraph from WDI BX.TRF.PWKR.DT.GD.ZS, 2024: Tajikistan 47.2 %, Philippines 8.7 %, Mexico 3.7 %, world
  0.8 % of GDP (figdata facts, no ledger row, as briefed).
- Photograph: container ship loading, Port of Barcelona 2010, Ivan Mlinaric, CC BY 2.0 (licence field read; credited
  in the caption, `CREDITS.md` and `frontmatter/image-credits.tex`). A company name is painted on the hull; the caption
  does not name it.
- Model `A tariff in a small country` tested with the 2018 US washing-machine tariffs; `record[Washing machines, 2018]`
  (washers nearly +12 %, untaxed dryers about as much; Flaaen, Hortaçsu and Tintelnot 2020, from the NBER abstract).
  `measure[The trade balance]` uses Brenland's frozen accounts (2024 deficit 1,316; 2025 surplus 1,113 million).
- Ledger (2): `g9:fht-2020-price-effect`, `g9:fht-2020-dryers`; source FHT2020.
- Gains and losses are rectangles only (buyers' extra 120 = weavers' 60 + state 60; the losses that go to nobody are
  said in words), as the brief asks; no surplus areas.

### g9-05 Exchange Rates and Purchasing Power — done 2026-11-20
- Pages: body 214–220 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (3 tests).
- Opening chart (`[A]` as briefed): GDP per person 2024 at market rates and at PPP, ten countries, paired horizontal
  bars on a times-ten axis (WDI NY.GDP.PCAP.CD, NY.GDP.PCAP.PP.CD; US equal by construction, tested; India 2,592 vs
  10,719; Switzerland lower at PPP). Second chart: price level of household consumption (WDI PA.NUS.PRVT.PLI, US = 100)
  against GDP per person at PPP, 171 countries, six named dots (`omincomex`); medians 35 below 5,000 dollars (31
  countries) and 76 above 50,000 (41 countries). Diagram: dalens ↔ kests conversion arrows.
- Image: AI traveller at an exchange counter (rate board blurred, no readable text; looked at).
- Exchange rate defined as dalens per kest (series convention: e up = home depreciation); Brenland's frozen rate
  1.207 → 1.242 (+2.9 %) used in the text, exercise 5 and the problem.
- Model `The law of one price`, tested with the price-level chart (fails for whole baskets in a regular way).
  `measure[Purchasing-power conversion]` (ICP 2021 cycle, results May 2024); `dated{2026}`: 21 of 27 EU members use the
  euro, Bulgaria since 2026 (ECB page).
- Ledger (2): `g9:icp-2021` (WBICP), `g9:euro-members-2026` (ECBEURO).
- Problem: a summer in Kestria, 12 questions; ends with Kestria poorer than Brenland at the market rate (37,260 vs
  42,327 dalens) and richer at the PPP rate (45,000).

### g9-06 Why Some Countries Are Rich: Institutions — done 2026-11-20
- Pages: body 220–226 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (3 tests).
- Opening chart (`[A]` as briefed): South vs North Korea, Maddison, 1940–2022, times-ten; North Korea's 1944–1989 gap
  written `nan` and stated in the caption (1940: N 2,624, S 1,975; 2022: N 1,569, S 41,321, ratio 26.3; 1990–2022
  growth +3.5 % vs −1.4 %). Second chart: China 1950–2022 (Maddison), 1978 dashed (2.8 % a year before, 5.6 % after,
  ×11.03). Third chart: bribery incidence (IC.FRM.BRIB.ZS, latest survey 2016–2025 per country, 168 countries) against
  GDP per person PPP in the survey year; medians 14.4 % (33 countries under 5,000) and 2.6 % (54 over 30,000). The WGI
  chart stays refused (licence), as briefed. Diagram: four differences, planned vs market (TikZ boxes).
- Photograph: the Korean peninsula at night from the ISS, 30 January 2014 (NASA, public domain; credits added).
- Boxes: `record[Germany, 1949–1990]` (East GDP per person 40 % of West in 1991, somewhat above 60 % in 1996, steady to
  2001; European Commission Economic Papers 170, 2002 — the brief's "official statistical office" source was not
  reachable as a page, the Commission paper is used); `record[China after 1978]` (Lin 1992: decollectivisation about
  half of 1978–84 farm-output growth, from the EconPapers abstract); `measure[A correlation across countries]`.
- Model `Institutions and income` per the brief; the cause question across countries is handed to the Year 3 volume
  in prose. Definitions: natural experiment, planned economy, market economy, institution, property right, contract
  enforcement, correlation (in words).
- Ledger (4): `g9:germany-east-west-1991`, `-1996` (EC2002GER), `g9:lin-1992`, `g9:china-reform-1978` (LIN1992). The
  brief's Third Plenum primary source was not fetched; the chapter only says the rural reforms began in 1978.
- Unsourced background softened while writing: South Korea's state role (now "played a large part"), East Germany's
  pre-war industry (cut), the cause of East Germany's catch-up (now "under the west's rules and currency").
- Problem: two valleys (A 3 %, B 1 %, 20 years: 1,806 vs 1,220, lead 48 %); after B's reform (5 %), the lead is
  halved in year 30, ten years later (figdata valleys.csv; exact 9.2 years).

### g9-07 Who Earns What: Income Distribution — done 2026-11-20
- Pages: body 227–233 (7 pp) + solutions about 1.5 pp. Build 0/0/0; gates OK; figdata OK (2 tests).
- Opening chart (`[A]` with the brief's stated method): the world distribution of income or consumption per person per
  day (2021 PPP dollars), around 1990 and around 2019, from PIP survey percentiles: nearest survey within ±3 years (ties
  to the later), national table or urban + rural together, each percentile = 1 % of the country's population in the
  target year (WDI SP.POP.TOTL), bands of 0.1 power of ten. Coverage 84.1 % of world population (85 countries) in 1990,
  97.9 % (144) in 2019, printed in the caption. Below 3 dollars: 45.3 % → 9.5 % of the covered population; peak band
  2.8 → 5.6 dollars; world median 3.33 → 8.8; China's survey median 1.71 (1990) → 12.02 (2019), India's 3.09 (1993) →
  5.51 (2022); China + India held 66.8 % of the covered people below the line in 1990. The `[N]` line-up file was not
  requested (the stated-method version works).
- Second chart: richest fifth's share (WDI SI.DST.05TH.20), six countries, survey years since 1980, gaps as `nan`;
  caption says which measure income and which consumption (checked in the PIP file: China consumption 20 / income 3
  survey years, India consumption only). Diagrams: dot strip of nine invented incomes (mean 29.2, median 18); fifths
  bars of an invented town (6/10/15/22/47) from a table.
- Image: AI street of homes of different sizes (no text; looked at).
- Boxes: `measure[Income or consumption]` (PIP handbook ch. 2), `measure[World distribution]` (the method). No model
  box, as briefed.
- Ledger (1): `g9:pip-welfare-aggregate` (PIPHB2). **Change from the brief:** the row is named for what it holds (the
  welfare aggregate, income or consumption) instead of `g9:pip-lineup-method`, since the chapter does not use line-up
  estimates.
- Problem: Brenland's fifths from the frozen survey (gross 8.1/14.0/17.5/23.0/37.4, disposable
  11.1/15.0/17.9/22.5/33.5; mean 24,920, median 22,265), the 3-dollar line at an invented 2 dalens per PPP dollar
  (2,190 dalens a person a year). Exercise 5 computes the poorest fifth's mean from the rounded share (13,831) and the
  solution says the survey's exact value is 13,869.
- **All 30 chapters are written.**

### Phase C — done 2026-11-20
- Term links: `tools/term_config/book1_en.py` curated (STOP: share, shares, Share, exchange, Exchange — linked in their
  defining chapters only; EXTRA_PROTECT: "the capital of" / "near its capital" (Brenmoor), "loss of laying hens",
  "not a loss", "two losses"; the bare word "surplus" is not a term, per the sync). 219 linkable terms, **2,718 links
  across 59 files**; `--check` clean. Risky labels sampled in context (loss, capital, basket, price level, elastic,
  principal, shock, yield, market): no wrong sense found. Links sit in prose and tables only, none in charts, captions
  or headings.
- Stubs: the last `% PENDING-DATA` (g6-06, ICP 2021 food shares, never fetched) is resolved by cutting the unsourced
  cross-country sentence; a comment records why. No `PENDING` left in Book 1.
- Images: no PNG under `images/book1/`; all 30 AI images scanned for flat bands (one false positive, a pale sky in
  `g6-food-and-energy-harvest-plain.jpg`, looked at: no band). **Two AI images are unused and kept on disk** (not
  deleted, by the no-bulk-delete rule; the user decides): `g6-food-and-energy-harvest.jpg`,
  `g6-school-and-work-tractor.jpg`.
- Figure pass: every page rendered (279 pages, 24 dpi overview grids) after the links; every chapter's figures had
  been checked at writing time at readable resolution. No overlap, empty chart or misplaced float found.
- Fresh build (aux, toc, out, fdb_latexmk removed by name): **279 pages, 0 errors, 0 undefined, 0 overfull**; gates OK
  for grades 6–9; figdata OK for grades 6–9 (every table rebuilt and tested); `check_ledger` OK (475 rows, all books).
- Next: Phase D report; then the main session's verification and the fresh reader.

## For the shared docs

- **Empty CSV cells** (a series with gaps, e.g. Maddison regions or a long country series beside a short one) are
  skipped by pgfplots and the line joins the neighbouring points: one wide table with blanks works; no `nan` needed.
- **Per-point label anchors** for `nodes near coords`: write a string column (`pos`) in the figdata table and use
  `visualization depends on={value \thisrow{pos} \as \labelpos}` with `anchor=\labelpos`.
- **`ytickten`** defaults to 10^-3..10^9; a chart below 0.001 needs `ytickten={-4,...,1}` and
  `yticklabel style={/pgf/number format/precision=4}`.

- **`omtimesten` inside a `groupplot`** resets `width`/`height` (it inherits `omrecord`'s `width=0.85\linewidth`): give the
  panel its size *after* the style, in `\nextgroupplot[ymode=log, omtimesten, width=…, height=…]`, or the panel runs
  ~180 pt into the margin.
- **`check_boxes.py` sees a chart only if the caption and source arguments are adjacent**: `…caption.}{Source…}` with no
  newline between `}` and `{`. A line break there makes the gate count 0 charts.
- **pgfmath in TikZ**: `\v*6/10000` with `\v=10000` overflows ("Dimension too large"); scale before multiplying.
- **Maddison regional population** (`maddison_regions`) has all eight regions only in 1820, 1870 and from 1950; MENA and
  Sub-Saharan Africa are missing in 1850, 1900, 1920 and 1940. Dividing by the sum of the regions present gives wrong
  shares; divide by the World row and keep complete years.

## Fresh-reader triage (2026-11-20)

`sources/book1/READER_REPORT.md`: 32 defects, all fixed (Resolution column). Rulings applied: food share now over
spending (g6-06 chart + measure box; g7-07 Engel box tested on cross-country and over-time ERS rows); income effect vs
opportunity cost (g7-01); "consistent with" in R1-014/018/026/029; 2025 SNA in a dated box; ILO future starters;
JST 1928-29 (inversion predates the crash); rent-control 5.1 % hatched as the authors' calculation; Kestria in g8-04
tied to 30 000 kests x 1.242 / 1.345 = 27 700 (the frozen package has no Kestria GDP). Fresh build 0/0/0, 280 pp; gates
6-9 green; figdata 6-9 OK; term links unwrapped and re-applied (2,749), --check clean; changed charts looked at.
- **Trap: `ytick=data` with a first plot that has `nan` rows** drops those rows' tick labels; give explicit ticks.


## figdata test step (2026-11-20, coordinator reopening)

The test step of `tools/figdata.sh` had never run. Two Book 1 tests failed once it did; both were stale expectations, and
the data and scripts were right:
- `03-poverty::test_world` asserted that the number above $3.00 a day rose every year; WDI's share jumps 42.1 -> 43.6 %
  in 1989, so it dips once (2.963 -> 2.937). Test now pins that single dip and the years the poor count rose after 1993
  (1997, 1998, 2020). The chapter's "kept rising until 1993 ... After 1993, both fell" was loose: reworded.
- `06-food-and-energy::test_energy` asserted a factor of ten between rich and poor medians; the 2024 WDI factor is 9.4,
  and the text claims only "far more". Test now checks > 5 times, log-log correlation > 0.8, and the printed numbers.
- **Trap:** a test is only evidence once you have seen it run; `figdata.sh` printing OK did not prove the tests ran.
