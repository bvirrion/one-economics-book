# Book 1 (Grades 6–9) — chapter briefs (Phase A, 2026-11-20)

Writer: the Book 1 agent. Binding inputs: `sources/BATCH_BOOKS_1-5.md`, `OUTLINE.md` (Book 1 and the ownership maps),
`../economics_series.md`, `sources/SERIES_DEFINITIONS.md`, `sources/data_ledger.md`. Definitions with labels are in
`sources/book1/DEFINITIONS.md`. Nothing here is printed.

## Conventions used in these briefs

- **Exercise kinds**: R = read a chart or a table; C = compute; P = use a model to predict a direction and a size;
  X = say what observation would contradict the model (in grade 6, which has no model: what observation would contradict
  the chart's claim, or what the chart cannot show). Stars run 4 × ★, 5 × ★★, 3 × ★★★ in every chapter (12 in all,
  never decreasing).
- **Weekend problem**: 10–14 questions, Parts I–III, story-driven, a quantified result at the end.
- **Data tags**: `[A]` = drawn from an approved dataset through `econdata` now; `[L]` = needs the *ledger-table* mechanism
  requested at the sync (a small table of values transcribed from a published paper or an agency's published table, each
  value with a ledger row); `[N]` = needs a new dataset (see the report's "Data to approve"); `[I]` = invented
  (Brenland/Kestria or a seeded chapter script). Where the outline's chart needs `[L]` or `[N]`, the brief gives the
  `[A]` fallback that will be drawn if the sync says no.
- **Level guard** (one-math-book): g6 has percentages, decimals and proportionality but **no negative numbers** (they come
  in g7): a fall is written "a fall of 3 %", never "−3 %". g7: negative numbers, literal expressions. g8: powers,
  one-unknown equations, weighted averages. g9: affine functions, mean and median.
- Ledger ids carry the year prefix (`g6:`, `g7:`…) and live in `sources/ledger/book1.md`.
- Photographs: Wikimedia Commons or an institution, licence page read, logged in `images/book1/CREDITS.md`. AI images:
  grades 6–9 everyday scenes only, no text, brands, flags, banknote designs, real people.

---

# Grade 6 — The world in twenty-one charts

No model box, no opening chart, three or more `omchart`s per chapter, no `\cref` forward needed. Each chapter: for every
chart, a `measure` box on how the number is made, a paragraph "what the chart shows" and one "what it cannot show".
Every chapter ends with a short section "What the charts do not say" (description is not cause).

## g6-01 Reading Economic Charts — `reading-economic-charts`

Coverage (outline): a quantity over time; a total and the same total per person; a share in percent; a rate of change;
the times-ten scale; the source line; a chart shows what happened, not why. All covered.

- **Sections**: 1 A quantity followed over time (axes, units, the source line). 2 Totals, per person, and shares.
  3 Rates of change (a rise or fall in percent between two dates, a yearly rate in words). 4 The times-ten scale (each
  gridline ten times the one below; equal steps are equal ratios). 5 What a chart cannot tell (what happened, not why;
  the averages hide differences).
- **Definitions**: time series; source line; total value; per-person value; share; rate of change; times-ten scale.
- **Recall**: percentages and reading a chart (mathematics, grade 6, in prose).
- **Charts** (3, all `[A]`):
  1. `world_population.csv` — world population, 1820–2022 (21 dated points, drawn with marks): `maddison_regions("World")`,
     column `pop`. Ordinary scale. Shows: about 1 billion in 1820, 8 billion in 2022.
  2. `population_shares.csv` — shares of world population by Maddison's eight regions, 1820–2022 (stacked area to 100 %):
     `maddison_regions(REGIONS)`, `pop` divided by the World row. Shows: Asia's share falls then rises; Africa's share
     rises after 1950; Western Europe's share falls.
  3. `uk_income_two_scales.csv` — income per person in the United Kingdom, 1820–2022, drawn twice side by side: ordinary
     scale and times-ten scale: `maddison("GBR", since=1820)`, `gdppc` (2011 international dollars). Shows: the ordinary
     scale makes early growth look flat; the times-ten scale shows near-steady growth.
- **Diagrams** (TikZ): anatomy of a chart (title, axes, units, legend, source line, labelled); a "ruler" of the times-ten
  scale (1, 10, 100, 1,000 with equal steps) beside an ordinary ruler.
- **Images**: AI — a classroom wall with a hand-drawn bar chart, no readable text (`g6-reading-economic-charts-classroom.jpg`).
- **Boxes**: `measure[Counting people]` (censuses, estimates before censuses; Maddison's population before 1950 is an
  estimate); `measure[Per person]`.
- **Exercises**: ★ R read population in 1900 and 2000 from chart 1; ★ C a per-person value from a total (invented town);
  ★ R which region's share fell most (chart 2); ★ C a share in percent from two counts; ★★ C rate of change between two
  dates (UK income 1950–2000, figdata); ★★ R read a times-ten chart (between which gridlines); ★★ C equal steps on the
  times-ten scale (×10 each gridline: how many times larger?); ★★ X "a chart that shows population growing proves that
  food got cheaper": what is missing; ★★ R spot the missing source line and the misleading axis in an invented chart;
  ★★★ C total vs per person: two invented countries, the larger total and the smaller per-person value; ★★★ R/C redraw
  three values on a times-ten scale by placing them between gridlines; ★★★ X what chart would show that a fall in a share
  is not a fall in the number (shares vs counts).
- **Weekend problem** — *The census of Brenmoor* (11 questions): Part I counting the town and its districts (totals,
  shares); Part II per-person income of the districts (invented `[I]` seeded table); Part III growth over 50 years on two
  scales, ending with "how many times larger" read off the times-ten scale and the rate of change in percent.
- **Ledger**: `g6:census-first` (date of the first modern censuses, e.g. a national statistical office's page), optional.

## g6-02 Two Hundred Years of Living Standards — `living-standards`

Coverage: income per person flat for centuries then a take-off; who took off first, who caught up, who has not; what an
hour of work buys then and now; an average hides differences inside a country. All covered.

- **Sections**: 1 Income per person, and what it measures (told: a dollar of fixed purchasing power, explained in grade 9).
  2 Centuries of almost nothing, then a take-off. 3 First, later, not yet: the regions since 1820. 4 Catching up since
  1950: six paths. 5 What an hour of work buys (bread, light). 6 What an average hides.
- **Definitions**: income per person; living standard; take-off (sustained growth of income per person); catch-up.
- **Recall**: per-person value, times-ten scale (g6-01, `\cref`).
- **Charts** (3, `[A]`):
  1. `long_run_income.csv` — income per person, times-ten scale: United Kingdom from 1300, the Netherlands from 1348,
     Italy and the World (Maddison's own estimate) from 1820: `maddison(["GBR","NLD","ITA"])`, `maddison_regions("World")`.
     Shows: under 3,000 dollars for centuries, then a rise above 30,000. Caption names the 2011-dollar base.
  2. `income_by_region.csv` — income per person by Maddison's eight regions, 1820–2022, times-ten scale:
     `maddison_regions(REGIONS)`. Shows: Western Offshoots and Western Europe first; East Asia late and fast;
     Sub-Saharan Africa still lowest.
  3. `six_paths.csv` — income per person since 1950: South Korea, China, Botswana (caught up a lot), Argentina, Venezuela,
     DR Congo (did not, or fell back): `maddison([...], since=1950)`, times-ten scale.
- **Diagrams**: a timeline bar of 1,000 years with the take-off marked (TikZ; geometry from table values).
- **Images**: AI — a family buying bread at a bakery counter (no text); AI — a room lit by a candle beside the same room
  lit by an electric lamp. Photograph: none.
- **Boxes**: `measure[Income per person over centuries]` (how Maddison's early numbers are built: wages, prices, output
  estimates; uncertain); `measure[What an hour of work buys]` (hours of work for a loaf or for an hour of light).
- **Exercises**: ★ R UK income in 1700 and 2000; ★ R which region was richest in 1820, which in 2022; ★ C how many times
  richer (2022 / 1820) for the World; ★ R the year South Korea passed Argentina (`six_paths`); ★★ C rate of change of
  Botswana 1950–2022; ★★ C hours of work for a loaf then and now (ledger numbers); ★★ R times-ten: gap between DR Congo
  and South Korea in 2022 in "times"; ★★ X what observation would contradict "the take-off began in Western Europe";
  ★★ R an average and two districts (invented) — what the average hides; ★★★ C the world in 1820 at 1 % a year
  (step-by-step multiplication over 10 years only: no powers yet); ★★★ R/C Venezuela's fall since its peak, in percent;
  ★★★ X what chart would show that a rise in income per person left most people no better off.
- **Weekend problem** — *A letter from 1820* (12 questions): Part I a family budget in 1820 vs today (ledger: bread and
  wage); Part II the six countries (read and compare); Part III a classroom "catch-up race" with invented growth rates,
  ending with the year one country passes another (table by multiplication).
- **Ledger**: `g6:light-labour-price-1800`, `g6:light-labour-price-today` (Nordhaus 1996, *The Economics of New Goods*,
  table of the labour price of light); `g6:bread-wage-1820`, `g6:bread-wage-today` (a published wage-and-price study,
  e.g. Allen 2001, *EEH* 38(4), or a statistical office's average price and wage page). `[L]` would let chart 3's
  companion "hours of work per 1,000 lumen-hours" be drawn; otherwise a small printed table.

## g6-03 Poverty and How It Is Counted — `poverty`

Coverage: a poverty line as the cost of a basket of needs; the extreme line for world comparisons and higher national
lines; the share and the number, which can move apart; where the poorest live. All covered; "over two centuries" needs
`[L]`/`[N]`.

- **Sections**: 1 What a poverty line is (a basket of needs priced). 2 The extreme-poverty line and the higher lines.
  3 The share and the number. 4 Where the poorest live now. 5 What a poverty count leaves out.
- **Definitions**: poverty line; extreme poverty; poverty rate; national poverty line.
- **Recall**: per-person value, share (g6-01); income per person (g6-02).
- **Charts** (3):
  1. `poverty_share_world.csv` — share of the world below \$3.00 a day (2021 PPP), 1981–2024: `wdi("SI.POV.DDAY",
     isos="WLD")` `[A]`. Shows 47.1 % (1981) to 10.1 % (2024); 2019 missing in WDI (line drawn through, stated).
     **Outline wants two centuries** `[L]`: Bourguignon and Morrisson (2002, *AER* 92(4), Table 3) 1820–1992, drawn as a
     second, separately labelled series (different line, 1985 PPP) — or Moatsos (2021) `[N]`.
  2. `poverty_count_world.csv` — number of people below and above the line, billions, 1981–2024: `SI.POV.DDAY` ×
     `SP.POP.TOTL`, both `WLD` `[A]`, stacked area. Shows 2.13 bn poor in 1981, 2.34 bn at the 1993 peak, 0.82 bn in 2024,
     while the number above the line grew.
  3. `poverty_by_region.csv` — poverty rate by World Bank region (EAS, ECS, LCN, MEA, SAS, SSF) and the world, 1990–2024:
     `wdi("SI.POV.DDAY", isos=[...])` `[A]`. Shows East Asia's collapse and Sub-Saharan Africa's slow fall: most of the
     extreme poor now live there (uncomfortable fact kept).
- **Diagrams**: a basket of needs (food, shelter, clothing) priced into a line (TikZ boxes with invented prices).
- **Images**: AI — a market scene where a family counts coins for staples (no text).
- **Boxes**: `measure[The extreme-poverty line]` (national lines of the poorest countries, converted at purchasing-power
  rates; the line moved from \$2.15 to \$3.00 when prices were re-based to 2021; ledger); `measure[A household survey]`.
  `dated{2026}` for the current line value.
- **Exercises**: ★ R the share in 1990 and 2024; ★ R which region had the highest rate in 2024; ★ C share × population
  = number (invented country); ★ C a basket priced into a daily line (invented prices); ★★ C number poor in 1990 and
  2024 (figdata); ★★ R the year the number of poor peaked; ★★ X "fewer poor people means the poor got richer": what the
  count cannot show; ★★ C a household above or below three lines; ★★ R the share above \$8.30 a day (figdata number in
  text); ★★★ C why the share can fall while the number rises (invented two-date example); ★★★ R/C Sub-Saharan Africa's
  share of the world's extreme poor in 1990 and 2024 (needs `SSF` count; figdata); ★★★ X what data would show that a
  fall in the poverty rate came from a change of line, not of lives.
- **Weekend problem** — *Pricing a basket in Brenland* (12 questions): Part I price a basket of needs from Brenland's
  `basket.csv` and set a line; Part II apply it to Brenland's `households.csv` (share below, number below); Part III
  move the line up 20 % and count again, ending on the number and share of households below each line.
- **Ledger**: `g6:pip-line-3-00` (World Bank PIP page: the \$3.00 line, 2021 PPP); `g6:pip-line-2-15` (the previous
  line); `g6:bourguignon-morrisson-1820` (share in extreme poverty in 1820, *AER* 2002, Table 3) — prose even without `[L]`.

## g6-04 Longer Lives, Smaller Families — `health-and-population`

Coverage: life expectancy and what it averages; child mortality; births per woman; why population grew fast and why its
growth slows; ageing. All covered. Programme note: urbanisation (geography course) added as a short prose paragraph with a
figdata number (`SP.URB.TOTL.IN.ZS`, world, 1960 and 2025).

- **Sections**: 1 Life expectancy at birth (an average over a whole life table). 2 Child mortality. 3 Births per woman.
  4 Why population grew fast, and why its growth is slowing (births minus deaths, told). 5 An ageing population.
- **Definitions**: life expectancy at birth; child mortality rate; births per woman (fertility rate); old-age dependency
  ratio.
- **Recall**: per person, shares, times-ten scale (g6-01); income per person (g6-02).
- **Charts** (3, `[A]`):
  1. `life_expectancy_regions.csv` — life expectancy by region (Gapminder's six regions) and the world, 1800–2024:
     1800–1949 `gapminder("lex")` weighted by `gapminder("pop")`; 1960–2024 `wdi("SP.DYN.LE00.IN", countries_only=True)`
     weighted by `SP.POP.TOTL`, countries mapped to the same six regions by iso3; gap 1950–1959 left blank and stated in
     the source line ("Gapminder before 1950; World Bank WDI from 1960"). Shows about 30 years everywhere in 1800; above 70
     in most regions today; the fall in South Asia around 1918 (pandemic) visible.
  2. `child_mortality_income.csv` — deaths before age 5 per 1,000 births against income per person (2021 PPP), latest
     year with ≥ 120 countries (2024): `wdi("SH.DYN.MORT", countries_only=True)`, `wdi("NY.GDP.PCAP.PP.KD",
     countries_only=True)`; `omincomex` (times-ten x-axis). Shows a strong fall with income, and a wide spread at the same
     income.
  3. `fertility_regions.csv` — births per woman by World Bank region and the world, 1960–2024: `wdi("SP.DYN.TFRT.IN",
     isos=[WLD, EAS, ECS, LCN, MEA, NAC, SAS, SSF])`. Outline says "since 1950": WDI starts in 1960. Shows the world from
     about 5 to about 2.2; Sub-Saharan Africa still above 4.
- **Diagrams**: a population "tank" with births flowing in and deaths flowing out (TikZ, invented numbers); two age
  pyramids drawn as bars (invented young and ageing towns).
- **Images**: AI — a grandmother, parents and a child at a kitchen table (no text).
- **Boxes**: `measure[Life expectancy at birth]` (period life table; an average, so child deaths pull it down);
  `measure[Births per woman]`.
- **Exercises**: ★ R world life expectancy in 1900 and 2024; ★ R region with the lowest fertility; ★ C deaths per 1,000
  into a percentage; ★ R child mortality at two income levels; ★★ C why an average of 30 years does not mean people died
  at 30 (invented 10-person table); ★★ C old-age dependency from invented counts; ★★ R the year the world fell below 3
  births per woman; ★★ X what observation would contradict "richer countries always have lower child mortality";
  ★★ C births minus deaths into population growth (invented town over 3 years); ★★★ R/C two countries at the same income
  with different child mortality (figdata); ★★★ C the ageing town in 20 years (invented, by steps); ★★★ X what a chart of
  averages cannot say about who lives longer inside a country.
- **Weekend problem** — *The village register* (12 questions): Part I an invented parish register (births, deaths by age)
  → child mortality and life expectancy by hand; Part II population over 30 years (births minus deaths); Part III the
  dependency ratio now and later, ending with the number of workers per retired person.
- **Ledger**: `g6:influenza-1918` (dates of the 1918–1919 pandemic, a public-health agency page), optional.

## g6-05 School and Work — `school-and-work`

Coverage: literacy and years of schooling; hours worked in a year; farms to factories to services; women in paid work;
child labour then and now. Years of schooling: WDI holds no schooling-years series (`SE.SCH.LIFE` absent; Barro–Lee
refused) — **gap**: years of schooling are given in prose from a ledger row (no chart).

- **Sections**: 1 Reading and writing. 2 How long people work. 3 Farms, factories, services. 4 Women in paid work.
  5 Children at work, then and now.
- **Definitions**: literacy rate; hours worked per year; sector of employment (farming, industry, services); child labour.
- **Recall**: shares, rates of change (g6-01); income per person (g6-02).
- **Charts** (3):
  1. `literacy.csv` — adult literacy rate, world and regions, 1975–2024: `wdi("SE.ADT.LITR.ZS", isos=[WLD, SAS, SSF, MEA,
     EAS, LCN])` `[A]`. Shows 65.4 % (1975) to 87.7 % (2024). **Outline wants two centuries** `[L]`: van Zanden et al.
     (2014, *How Was Life?*, OECD, literacy chapter table), 1820–2000, separately labelled.
  2. `hours_worked.csv` — average yearly hours per worker, 1950–2023: `pwt(["USA","GBR","FRA","DEU","JPN","KOR"],
     cols=["avh"])` `[A]`. Shows a fall of several hundred hours in rich countries; South Korea high then falling.
     **Outline wants 1870** `[L]`: Huberman and Minns (2007, *EEH* 44(4), Table 1) 1870–2000.
  3. `sectors_china.csv` — shares of employment in agriculture, industry and services in China, 1991–2025: WDI
     `SL.AGR.EMPL.ZS`, `SL.IND.EMPL.ZS`, `SL.SRV.EMPL.ZS` (modelled ILO estimates) `[A]`, stacked area. Shows farming from
     about 60 % to under 25 % in one generation. **Outline wants one country over two centuries** `[L]`: the United States
     (Lebergott 1966 / *Historical Statistics of the United States*, public domain) 1800–2000.
- **Diagrams**: three boxes (farm, factory, office) with arrows of people moving (TikZ).
- **Images**: AI — a field with a tractor; AI — a classroom with children writing. Photograph (PD): a historic photo of
  child workers (e.g. a Library of Congress National Child Labor Committee photograph, PD) — check licence page.
- **Boxes**: `measure[Hours worked per year]` (hours actually worked, not contract hours); `measure[Who counts as
  literate]` (self-reported, censuses).
- **Exercises**: ★ R literacy in 1975 and 2024; ★ R which country worked most hours in 2023; ★ C hours per week from
  hours per year; ★ R China's farm share in 2000; ★★ C the fall of hours in percent (figdata); ★★ C a share of workers
  into a number (invented country); ★★ R the year services passed farming in China; ★★ X what observation would
  contradict "people work less as countries get richer"; ★★ C women's share of the workforce from counts (invented);
  ★★★ R/C women in paid work: two figdata values (`SL.TLF.CACT.FE.ZS`, world 1990 and 2025) and the change; ★★★ C the
  number of farm workers falling while total employment rises (invented); ★★★ X what this chart cannot say about
  whether the work became better.
- **Weekend problem** — *Three generations at work* (11 questions): Part I a family's yearly hours (grandparent, parent,
  child) from invented diaries; Part II their sectors and the shares; Part III what an hour of work buys for each
  generation, ending with the hours needed to buy the same bicycle (invented prices and wages).
- **Ledger**: `g6:hours-1870` (Huberman–Minns 2007, Table 1); `g6:us-farm-share-1800` (Historical Statistics / Lebergott);
  `g6:schooling-years-world` (a published world figure for average years of schooling, e.g. a UNESCO page); `g6:ilo-child-labour`
  (ILO–UNICEF 2021 child-labour estimate, 160 million).

## g6-06 Food and Energy — `food-and-energy`

Coverage: crop yields; the decline of famine; the food share of spending falls as income rises; energy per person against
income; air pollution and CO₂ as countries get richer. The food-share chart has **no approved data** (see the report).
Programme note: water as a resource (geography course) gets one prose paragraph with `ER.H2O.FWTL.ZS` (approved).

- **Sections**: 1 More grain from each field. 2 Famine. 3 How much of a budget goes to food. 4 Energy and income.
  5 Smoke and carbon dioxide as countries get richer.
- **Definitions**: crop yield; famine; food share of spending; energy use per person; air pollutant.
- **Recall**: per person, times-ten scale (g6-01); income per person (g6-02).
- **Charts** (3, `[A]`, with one `[N]` alternative):
  1. `cereal_yields.csv` — cereal yield in tonnes per hectare, 1961–2024: `faostat_crops("Cereals, primary", "Yield")`,
     World, Africa, Asia, Europe, Northern America, South America. Shows world yields more than doubled; Africa's rose
     least. **Outline says since 1900** `[L]`: US corn yields (USDA NASS, public domain) as a published table.
  2. `energy_income.csv` — energy use per person (kg of oil equivalent) against income per person (2021 PPP), latest
     year ≥ 120 countries (2022 or later), both axes times-ten (`loglogaxis` with `omrecord`): `wdi("EG.USE.PCAP.KG.OE",
     countries_only=True)`, `NY.GDP.PCAP.PP.KD`.
  3. `so2_rise_and_fall.csv` — sulphur dioxide emissions (kilotonnes), United Kingdom, United States, Germany, China,
     India, 1850–2023: `ceds("so2")`. Shows the rise and fall in rich countries, the later rise and recent fall in China,
     the rise in India. CO₂ per person against income is quoted in prose from a figdata table (`ceds("co2")` ÷
     `SP.POP.TOTL`).
  - **`[N]` alternative**: `food_share_income.csv` — food share of household consumption against income per person, from
    the World Bank ICP 2021 results (see "Data to approve"). If approved it becomes the third chart and SO₂ moves to prose;
    without it, food shares are a printed table of six countries with ledger rows (USDA ERS published table).
- **Diagrams**: a household budget pie at two incomes (invented numbers, TikZ).
- **Images**: AI — a wheat field at harvest with a combine (no brand). Photograph: none.
- **Boxes**: `measure[Yield]` (production ÷ area harvested); `measure[Energy use per person]` (oil-equivalent units).
- **Exercises**: ★ R world yield in 1961 and 2024; ★ C a yield from production and area (invented farm); ★ R which
  country uses most energy per person among five; ★ C food share of an invented family's spending; ★★ C how many times
  world yields rose; ★★ R the year UK SO₂ peaked; ★★ C two families' food shares and the rule they suggest; ★★ X what
  observation would contradict "richer countries always emit more"; ★★ R energy use of two countries with equal income;
  ★★★ C feeding a growing village with rising yields (invented, by steps); ★★★ R/C China's SO₂ peak and its fall in
  percent (figdata); ★★★ X what this chart cannot say about why SO₂ fell.
- **Weekend problem** — *The harbour town's year* (12 questions): Part I a farm's yield and harvest; Part II Brenland
  households' food shares by income group (`households.csv`: food ÷ consumption by quartile of disposable income);
  Part III the town's energy use and smoke, ending with the food share of the poorest and richest quarters.
- **Ledger**: `g6:famine-deaths-decades` (deaths in famines by decade, a published compilation, e.g. Hasell and Roser
  from the World Peace Foundation's famine list — cite the primary list); `g6:food-share-usda-<iso>` (six rows, USDA ERS
  published table, if `[N]` is refused).

## g6-07 A Connected World — `a-connected-world`

Coverage: trade as a share of world output and its two waves; the falling cost of moving goods and information; goods
that became thousands of times cheaper (light, computing, a solar panel); prices over time, first look. Freight and call
costs, the price of light and the solar panel need `[L]`.

- **Sections**: 1 Selling to and buying from other countries. 2 Two waves of trade. 3 Moving goods and words.
  4 Thousands of times cheaper. 5 Prices over time, a first look (pointer to grade 8).
- **Definitions**: export; import; trade share (exports plus imports as a share of output); container (shipping).
  (See the report: *export*/*import* are in the map under g9; proposed to move them here.)
- **Recall**: share, times-ten scale (g6-01); income per person (g6-02).
- **Charts** (3):
  1. `trade_share.csv` — exports plus imports as a share of GDP: median over the 17 JST economies with data, 1870–2020
     (`jst(cols=["exports","imports","gdp"])`) and the world, 1970–2024 (`wdi("NE.TRD.GNFS.ZS", isos="WLD")`; 2025 dropped,
     coverage incomplete) `[A]`. Two labelled lines, different coverage, stated. Shows the first wave to 1913, the fall to
     the 1930s–1940s, the second wave.
  2. `connections.csv` — mobile phone subscriptions per 100 people and internet users (% of population), world, 1990–2024:
     `IT.CEL.SETS.P2`, `IT.NET.USER.ZS` (`WLD`) `[A]`. **Outline wants freight and call costs over a century** `[L]`:
     Hummels (2007, *JEP* 21(3), Figure 1 data) and a published price of a London–New York call (telecoms regulator or
     operator history page).
  3. `cost_of_computing.csv` — price of computers relative to all consumer prices in the euro area, 1996–2025, times-ten
     scale: `eurostat("prc_hicp_aind")`, coicop `CP0913` ÷ `CP00`, geo `EA` `[A]`. Shows a fall of more than ten times.
     **Outline prefers light (centuries)** `[L]`: Nordhaus (1996, Table 1.6) or Fouquet and Pearson (2006, *Energy Journal*
     27(1)); solar module price `[L]` (IRENA, *Renewable Power Generation Costs*).
- **Diagrams**: a world map-free schematic of a container ship's route with ports as nodes (TikZ, no map data).
- **Images**: Photograph — a container port (Commons, CC BY or PD); AI — a family video call on a phone held at a table
  (screen shows shapes only, no text).
- **Boxes**: `measure[Trade as a share of output]` (why it can exceed 100 %: Singapore); `measure[A price index]`
  (first look, pointer to grade 8).
- **Exercises**: ★ R trade share in 1913 and 1938; ★ R world trade share in 1970 and 2008; ★ C exports + imports ÷ output
  (invented island); ★ R internet users in 2000 and 2024; ★★ C how many times computers got cheaper; ★★ C a share above
  100 % (invented port city); ★★ R the year mobile subscriptions passed 50 per 100; ★★ X what would contradict "trade
  always rises"; ★★ R the 2009 dip and what it marks (figdata); ★★★ C a price that halves every 5 years for 20 years
  (repeated halving); ★★★ R/C the second wave's rise in percentage points since 1950 (JST median); ★★★ X what this chart
  cannot say about who gains from trade.
- **Weekend problem** — *A container from Kestria* (12 questions): Part I Brenland's trade with Kestria (`trade.csv`:
  exports, imports, the share of GDP from `accounts.csv`); Part II the cost of shipping (invented freight rates) and of a
  phone call over time (invented); Part III the falling price of a gadget on a times-ten scale, ending on how many times
  cheaper it became.
- **Ledger**: `g6:call-london-ny-1927` (price of a 3-minute transatlantic call); `g6:hummels-freight` (Hummels 2007);
  `g6:singapore-trade-share` is figdata, no row.

---

# Grade 7 — Choice, exchange and prices

From grade 7: one `openingchart` before the first section, explained in the chapter; 2–4 charts in all; the `model` frame
in plain words.

## g7-01 Scarcity and Opportunity Cost — `scarcity-and-opportunity-cost`

Coverage: wants exceed means; to choose is to give up; opportunity cost = best alternative given up; costs that are not
money; sunk costs; the same reasoning for a person, a firm, a country. All covered.

- **Sections**: 1 Wants and means (time, money, resources). 2 To choose is to give up. 3 Opportunity cost (incl. time).
  4 A cost already paid. 5 Persons, firms, countries.
- **Definitions**: scarcity; choice set (the options one can afford); opportunity cost; sunk cost.
- **Models**: `model{Choosing by opportunity cost}` — assumes: a person compares options and picks the one whose value
  beats the best alternative; predicts: when the value of time rises (higher wage), people buy time-saving goods and
  services; tested: richer countries work fewer hours per worker (opening chart) and buy more time-saving goods (ledger:
  a time-use study); breaks: habits, sunk-cost behaviour in experiments (ledger: Arkes and Blumer 1985, *OBHDP* 35).
- **Recall**: hours worked per year (g6-05); income per person (g6-02).
- **Opening chart** `[A]`: `hours_vs_income.csv` — yearly hours per worker against income per person, 2023, PWT
  (`avh`, `rgdpe/pop`), `omincomex`. Outline wanted "the 24 hours of a day in several countries" (OECD time use: refused
  host; BLS ATUS published table would be `[L]`). The chart answers "how do people spend scarce time?".
- **Other charts**: `time_use_us.csv` `[L]` (BLS ATUS published table, hours per day by activity) — optional.
- **Diagrams**: a choice tree (TikZ `forest`) for a Saturday: three options with values; an hourglass/budget bar of 24
  hours.
- **Images**: AI — a teenager at a table choosing between a ball, a book and a ticket (no text).
- **Boxes**: `measure[Valuing time]` (an hour's wage as a first estimate of an hour's value). No `record` box: no dated
  episode tests this model here.
- **Exercises**: ★ R hours worked in two countries; ★ C opportunity cost of an evening in a table; ★ C cost in money and
  in time of two trips; ★ R the best alternative in a list; ★★ C a sunk cost left out of a decision (invented concert);
  ★★ C a firm's opportunity cost of using its own building; ★★ P a wage rise: what happens to buying ready meals, and
  roughly how much (stated ratio); ★★ R/C hours vs income: two countries' gap; ★★ X observation that would contradict
  the model (people ignoring a cheaper, equal option); ★★★ C a country's land: wheat or houses (two-option table);
  ★★★ P a free entry ticket: is the cost zero?; ★★★ X a sunk-cost experiment outcome that contradicts the model.
- **Weekend problem** — *A Saturday in Brenmoor* (11 questions): Part I listing options and costs (money and hours);
  Part II the best choice and its opportunity cost; Part III a change (bus fare rises, a ticket already bought), ending
  with the new best choice and its opportunity cost in dalens.
- **Ledger**: `g7:arkes-blumer-1985`; `g7:time-saving-goods` (a time-use study, e.g. Hamermesh, published paper).

## g7-02 Specialisation and the Division of Labour — `specialisation`

Coverage: doing everything vs one thing well; splitting a task into steps raises output per worker; practice, tools,
saved time; specialisation needs exchange; a larger market allows finer specialisation. All covered.

- **Sections**: 1 Doing everything yourself. 2 Splitting the task (workshop numbers). 3 Why it works: practice, tools,
  saved time. 4 Specialists need to exchange. 5 Bigger markets, finer jobs.
- **Definitions**: specialisation; division of labour; output per worker; exchange.
- **Models**: `model{Specialisation and the size of the market}` — assumes: tasks can be split, workers learn by
  repetition, goods can be traded; predicts: output per worker rises with the division of labour; larger markets have more
  distinct jobs; tested: workshop time studies (ledger) and the fall of the farm share as countries grow richer (opening
  chart); breaks: tasks that cannot be split, repetitive work that lowers quality, markets cut off by transport costs.
- **Recall**: sectors of employment (g6-05); trade share (g6-07).
- **Opening chart** `[A]`: `farm_share_income.csv` — share of employment in agriculture against income per person, 2025,
  WDI `SL.AGR.EMPL.ZS`, `NY.GDP.PCAP.PP.KD`, `omincomex`. Outline: "farm share over two centuries, with the number of
  people one farmer feeds" `[L]` (US Historical Statistics; USDA ERS "one farmer feeds" figure).
- **Other charts** `[A]`: `people_per_farm_worker.csv` — people in the population per farm worker, five countries,
  1991–2025: `SP.POP.TOTL` ÷ (`SL.AGR.EMPL.ZS` × employment from `SL.EMP.TOTL.SP.ZS` × working-age population) — or the
  simpler `SL.TLF.TOTL.IN` × (1 − `SL.UEM.TOTL.ZS`); the method is stated.
- **Diagrams**: a workshop line with four stations and timed steps (TikZ, numbers match the worked example).
- **Images**: Photograph — a plate of pin-making from the 18th-century *Encyclopédie* (PD; caption describes the plate
  only, names no person); AI — a bakery workshop with three workers at different steps.
- **Boxes**: `measure[Output per worker]`.
- **Exercises**: ★ R farm share at two income levels; ★ C output per worker for one and for four workers; ★ C time saved
  by not switching tasks; ★ R people per farm worker in two countries; ★★ C a workshop's daily output after splitting
  (invented times); ★★ C how many specialists a village of 200 can support (invented); ★★ P the market doubles: direction
  and rough size of the number of distinct jobs; ★★ R/C farm share fall in percentage points; ★★ X what would contradict
  the model (a split that lowers output); ★★★ C a bottleneck station and the line's output; ★★★ P transport cost rises:
  what happens to specialisation; ★★★ X a country with a low farm share and low income — what it shows.
- **Weekend problem** — *The bicycle workshop of Brenmoor* (12 questions): Part I one worker builds whole bikes (times);
  Part II four workers split the job (output per worker, the bottleneck); Part III selling to Kestria doubles the market,
  ending with the new output per worker and the number of workers hired.
- **Ledger**: `g7:usda-one-farmer-feeds` (USDA ERS figure); `g7:time-study` (a published assembly time study — e.g. the
  1913–14 Ford Highland Park chassis assembly time, from a primary-source page).

## g7-03 Gains from Trade: Comparative Advantage — `comparative-advantage`

Coverage: two people and two tasks with a table of hours; absolute advantage; comparative advantage as lower opportunity
cost; both gain even if one is better at everything; the range of exchange ratios; the same for two regions; first model
frame. All covered.

- **Sections**: 1 Two people, two tasks, a table of hours. 2 Absolute advantage. 3 Comparative advantage. 4 Both gain:
  the exchange ratios that work. 5 Two regions.
- **Definitions**: absolute advantage; comparative advantage; gains from trade; exchange ratio.
- **Models**: `model{Comparative advantage, two people and two goods}` (the series' first frame in plain words) —
  assumes: two people, two goods, fixed hours per unit, free exchange; predicts: each specialises in the good of lower
  opportunity cost; both consume more at any exchange ratio between the two opportunity costs; tested: small countries
  trade more (opening chart), Japan's opening to trade in the 1850s–1870s (Bernhofen and Brown 2004, *JPE* 112(1));
  breaks: moving between tasks costs time, the gains are unevenly shared inside a country (taken up in the grades 10–12
  volume), transport costs. Labelled "comparative advantage"; *Ricardo's model* is owned by grade 10 and is not named as a
  model here (the result's name may be given once: "a result economists owe to David Ricardo" — sync to confirm).
- **Recall**: opportunity cost (g7-01); specialisation, exchange (g7-02).
- **Opening chart** `[A]`: `exports_vs_size.csv` — exports of goods and services (% of GDP) against population, 2024,
  `wdi("NE.EXP.GNFS.ZS", countries_only=True)`, `SP.POP.TOTL`, times-ten x-axis. Shows small countries trade more.
- **Other charts**: `ricardo_brenland.csv` `[I]` — Brenland and Kestria hours per unit (`country` `ricardo.csv`) as a bar
  chart (invented, labelled).
- **Diagrams**: a table of hours drawn as two bars per person; a number line of exchange ratios with the gain region
  shaded (TikZ, numbers from the worked example).
- **Images**: AI — two neighbours at a fence, one with baskets of apples, the other with loaves.
- **Boxes**: `record[Japan opens to trade]` (1859 opening; prices moved toward world prices; exports rose in goods
  whose prices rose — Bernhofen–Brown); `measure[Hours per unit]`.
- **Exercises**: ★ R who is faster at each task; ★ C opportunity cost of one shirt in loaves; ★ R exports share of two
  countries; ★ C absolute advantage from a table; ★★ C comparative advantage from a table; ★★ C total output before and
  after specialising; ★★ P a ratio inside the range: who gains and how much; ★★ P a ratio outside the range: what
  happens; ★★ X what observation would contradict the model (a country exporting the good of its higher opportunity
  cost); ★★★ C Brenland and Kestria (`ricardo.csv`): comparative advantage and the gain; ★★★ P one person gets faster at
  both tasks — does trade still pay?; ★★★ X a gain that one side does not get — what the model leaves out.
- **Weekend problem** — *Grain and cloth across the border* (13 questions): Part I Brenland and Kestria's hours per unit
  (`ricardo.csv`); Part II opportunity costs and specialisation; Part III trade at a chosen ratio, ending with each
  country's gain in units of grain.
- **Ledger**: `g7:bernhofen-brown-2004`; `g7:japan-opening-1859` (treaty port opening date, primary source).

## g7-04 Money — `money`

Coverage: barter and the double coincidence; money's three functions; what has served as money; good money (scarce,
durable, divisible, hard to forge); a price is an amount of money. All covered. "Cash against electronic payments" needs
`[L]` (ECB SPACE, Federal Reserve *Diary of Consumer Payment Choice*) — `[A]` fallback below.

- **Sections**: 1 Barter. 2 What money does. 3 What has served as money. 4 What makes good money. 5 A price is an amount
  of money.
- **Definitions**: barter; double coincidence of wants; money; means of payment; unit of account; store of value; price.
- **Models**: `model{Money as a means of exchange}` — assumes: trading is costly without a common good everyone accepts;
  predicts: one widely accepted, durable, divisible good emerges as money; a society that loses its money returns to
  barter or to another good (cigarettes, foreign currency); tested: prisoner-of-war camp cigarettes (Radford 1945,
  *Economica* 12(48)), dollar use in high inflation (ledger); breaks: money that loses value fast stops being a store of
  value (hyperinflation, grade 8).
- **Recall**: exchange (g7-02); gains from trade (g7-03).
- **Opening chart** `[A]` fallback: `accounts.csv` — share of adults with an account (bank or mobile money), 2011 and
  2024, ten countries: `wdi("FX.OWN.TOTL.ZS")`, in a `dated{2026}` context. `[L]` preferred: cash share of point-of-sale
  payments in several countries (ECB SPACE 2024 report table; Fed Diary).
- **Diagrams**: a barter circle of three traders where no pair wants what the other has, and money breaking the circle
  (TikZ).
- **Images**: Photograph — a Lydian electrum coin or a cowrie-shell string (Commons, PD/CC BY-SA, licence read);
  AI — a barter market scene (goats, grain, pots).
- **Boxes**: `record[Cigarettes as money]` (Radford 1945); `measure[An account]`; `dated{2026}` (shares of payments).
- **Exercises**: ★ R account ownership in two countries, 2011 and 2024; ★ C prices in a barter market of 4 goods (how
  many exchange rates: 6) vs with money (4 prices); ★ R which function is used in a scene; ★ C a price list in two
  units; ★★ C number of barter rates for 10 goods; ★★ C prices in cigarettes and in dalens (invented camp); ★★ P a
  money that loses 50 % a month: what people do; ★★ R account ownership change in percentage points; ★★ X observation
  contradicting the model (a good accepted everywhere that is not durable); ★★★ C counting rates for n goods (table
  pattern); ★★★ P a forged-coin wave: what happens to the use of coins; ★★★ X what the account chart cannot say about how
  people pay.
- **Weekend problem** — *The island market* (12 questions): Part I five traders and their wants (barter fails); Part II
  shells as money (prices, the unit of account); Part III too many shells are found, ending with the new prices in shells
  (proportional).
- **Ledger**: `g7:radford-1945`; `g7:lydian-coin-date` (a museum's page on early coinage); `g7:ecb-space-cash-share`
  (if `[L]`).

## g7-05 Markets and Prices — `markets-and-prices`

Coverage: markets (stall, auction, platform); the price both accept; a rising price tells buyers to use less and sellers
to bring more; a price sums up what thousands know, with nobody collecting it; shortage or surplus when the price cannot
move. All covered. Opening chart needs prices `[N]`/`[L]`.

- **Sections**: 1 Where buyers meet sellers. 2 The price both accept. 3 A price is a signal. 4 What a price knows.
  5 When a price cannot move.
- **Definitions**: market; buyer and seller (in words, not defined); market price; shortage; surplus (market sense:
  quantity offered exceeds quantity wanted — the word in the qualified form *market surplus*, so that Book 2's *consumer
  surplus* keeps its sense).
- **Models**: `model{Prices as signals}` — assumes: many buyers and sellers, a price free to move; predicts: after a bad
  harvest the price rises, buyers use less, other growers and stocks bring more; tested: the opening chart's episode;
  the price of tin and other examples; breaks: price controls (shortages, grade 9), a single seller (grade 8). The
  information result is taught as a positive result about markets, with no reference to what it was written against.
- **Recall**: money and price (g7-04); exchange (g7-02).
- **Opening chart**: `[N]` World Bank Commodity Price Data ("Pink Sheet"): the world price of wheat, 2009–2012, around the
  2010 Russian harvest failure (monthly), or cocoa 2022–2025 around the West African harvest failures. `[A]` fallback:
  `russia_wheat.csv` — wheat production in Russia and the world, 2005–2015, `faostat_crops("Wheat", "Production")`, with
  the price change quoted in prose from a ledger row (World Bank or FAO price page).
- **Other charts** `[A]`: `wheat_area_response.csv` — area harvested of wheat in exporters other than Russia the year
  after (FAOSTAT `Area harvested`) — sellers bring more.
- **Diagrams**: a price "dial" with arrows to buyers (use less) and sellers (bring more) (TikZ); a market stall table
  with a shortage and a surplus marked.
- **Images**: AI — a morning fruit market with stalls; Photograph — a fish auction hall (Commons, licence read).
- **Boxes**: `record[The 2010 wheat harvest]` (dated facts with ledger: the drought, the export ban, the price rise;
  what the model said — the ban is a policy choice reported neutrally); `measure[A world price]`.
- **Exercises**: ★ R production in 2009 and 2010; ★ C a shortage from two quantities; ★ C a surplus from two quantities;
  ★ R which way the price moved; ★★ P a frost destroys half the strawberries: direction of price and quantity; ★★ P
  a new orchard doubles supply: direction; ★★ C the price change in percent (ledger values); ★★ R other exporters' area
  the year after; ★★ X observation contradicting the model (a bad harvest with a falling price and no other cause);
  ★★★ P a price kept fixed after a bad harvest: queue length (invented numbers); ★★★ C an auction: the price at which
  quantities match in an invented bid list; ★★★ X what the chart cannot show about who bore the higher price.
- **Weekend problem** — *A frost in the orchards* (12 questions): Part I the Brenmoor apple market before the frost
  (invented table); Part II the frost and the new price; Part III a fixed price set by the town, ending with the shortage
  in kilograms and the queue.
- **Ledger**: `g7:wheat-price-2010` (World Bank / FAO price page); `g7:russia-export-ban-2010` (decree date, primary
  source or FAO GIEWS); `g7:cocoa-price-2024` (ICCO, if cocoa is chosen).

## g7-06 Demand and Supply: A First Look — `demand-and-supply-first-look`

Coverage: demand table and curve point by point; supply table and curve; the matching price in table and graph; above
and below it; a change in tastes, incomes or costs moves a curve. All covered. Opening chart needs `[N]`/`[L]`.

- **Sections**: 1 A demand table and its curve. 2 A supply table and its curve. 3 Where they meet. 4 Above and below the
  meeting price. 5 When a curve moves.
- **Definitions**: quantity demanded; demand table; demand curve; quantity supplied; supply table; supply curve;
  equilibrium price; equilibrium quantity; shift of a curve.
- **Models**: none boxed here — the supply-and-demand model box is in g9-01 (the outline applies the frame there). The
  chapter sketches it in words and ends with "what would show this picture is wrong" exercises.
- **Recall**: market price, shortage, surplus (g7-05).
- **Opening chart**: `[N]` BLS Average Price Data (monthly U.S. retail price of strawberries or tomatoes) — price
  through the year; quantity would come from a USDA published table `[L]`. `[A]` fallback: `fruit_prices_eu.csv` — the
  annual HICP index for fresh fruit in two EU countries is not seasonal, so it does not answer the question; the fallback
  is an invented market `[I]` labelled as such: `brenmoor_strawberries.csv` (seeded script: weekly price and quantity
  through one year).
- **Other charts** `[I]`: the demand and supply tables of the worked example, plotted (`omchart` over the seeded table).
- **Diagrams** (TikZ `econ` styles): demand curve from a table; supply curve; both crossing at the worked example's
  equilibrium (numbers match); a shifted demand curve (`shifted`) after a heat wave.
- **Images**: AI — a stall with strawberry baskets and a scale (no text).
- **Boxes**: `measure[Quantity demanded is a plan]`.
- **Exercises**: ★ R a quantity demanded at a price; ★ C plot a demand table; ★ R the matching price in a table; ★ C a
  shortage at a low price; ★★ C a surplus at a high price; ★★ P incomes rise: which curve moves, which way; ★★ P a cost
  of fertiliser falls: which curve moves; ★★ R a new crossing on a graph; ★★ X an observation that contradicts the
  picture (price and quantity both rise after a cost rise with no demand change); ★★★ C new table after a shift and the
  new equilibrium; ★★★ P two shifts at once: what is certain, what is not; ★★★ X what a price-and-quantity chart alone
  cannot tell (which curve moved).
- **Weekend problem** — *The strawberry season* (12 questions): Part I the demand and supply tables in May; Part II the
  equilibrium on the graph; Part III June: supply doubles at every price, ending with the new price and quantity.
- **Ledger**: none if `[I]`; `g7:usda-strawberry-volume` if `[L]`.

## g7-07 Households: Income, Spending and Saving — `households`

Coverage: income sources (wages, a business, rent, interest, transfers); the budget and its shares; saving as spending
moved to later; budget shares change with income (food recalled). Economics only, no advice. All covered.

- **Sections**: 1 Where income comes from. 2 Taxes, transfers and what is left. 3 The budget and its shares. 4 Saving.
  5 Richer households, different shares (Engel's law).
- **Definitions**: household; income; wage; transfer; disposable income; budget; budget share; saving.
- **Models**: `model{Engel's law}` — assumes: households buy food first, then other goods; predicts: the food share falls
  as income rises, while food spending in money rises; tested: household surveys everywhere (Brenland's survey in the
  chapter; the national surveys behind the opening chart); breaks: very poor households where the share can first rise,
  the share of housing (does not follow the same pattern).
- **Recall**: food share of spending (g6-06); price (g7-04).
- **Opening chart**: `[L]` U.S. Consumer Expenditure Survey, Table "Quintiles of income before taxes" (BLS, public
  domain): budget shares of food, housing, transportation, entertainment at the 1st, 2nd, 4th and 5th quintiles. `[I]`
  fallback: `brenland_budget_shares.csv` — Brenland survey (`households.csv`), food share by quartile of disposable
  income (only food and total are in the survey). Real data preferred (facts before models).
- **Other charts** `[I]`: `brenland_engel.csv` — food spending and food share against disposable income, Brenland's 2,000
  households (scatter + binned means).
- **Diagrams**: a flow from gross income through taxes and transfers to disposable income, spending and saving (TikZ,
  numbers of a worked example).
- **Images**: AI — a family at a kitchen table with receipts and a jar of coins (no text).
- **Boxes**: `measure[A household budget survey]`.
- **Exercises**: ★ R the food share at the lowest and highest income group; ★ C disposable income from gross, tax and
  transfer; ★ C budget shares from a budget; ★ C saving from income and spending; ★★ C food share of three Brenland
  households (rows given); ★★ R/C binned food shares (chart); ★★ P income doubles: direction and rough size of the
  food share (from the chart's slope); ★★ C saving rate over a year; ★★ X a household that contradicts Engel's law —
  what it would look like; ★★★ C two households, same income, different sizes (spending per person); ★★★ P a transfer of
  \dal{1000}: food spending of a poor and a rich household (shares used); ★★★ X what a cross-section cannot say about one
  household over time.
- **Weekend problem** — *The Brenmoor household survey* (12 questions): Part I five households from `households.csv`:
  income, tax, transfers, disposable; Part II budget shares and saving; Part III income groups and Engel's law, ending
  with the food share of the bottom and top quarters.
- **Ledger**: `g7:bls-cex-quintiles` (rows per share, if `[L]`).

## g7-08 Firms: Costs, Revenue and Profit — `firms`

Coverage: a firm buys inputs, sells output; revenue; fixed and variable costs; profit and loss; break-even quantity by
arithmetic; the owner bears risk; profit draws firms in, losses move resources. All covered. Opening chart needs `[L]`/`[N]`.

- **Sections**: 1 What a firm does. 2 Revenue. 3 Fixed and variable costs. 4 Profit, loss and the break-even quantity.
  5 Risk, entry and exit.
- **Definitions**: firm; input; output (of a firm); revenue; fixed cost; variable cost; total cost; profit; loss;
  break-even quantity; entrepreneur.
- **Models**: `model{Entry and exit}` — assumes: anyone may open a firm, profits are visible; predicts: high profits draw
  new firms and the price falls toward cost; losses make firms close; tested: survival rates of new firms (opening chart),
  entry after a market opens (grade 8); breaks: licences, patents and large fixed costs (grade 8).
- **Recall**: price (g7-04); market (g7-05); revenue as price × quantity uses g7 maths (literal expressions).
- **Opening chart**: `[L]` BLS Business Employment Dynamics, "Survival of private sector establishments by opening year"
  (public domain published table): of 100 establishments, how many open after 1, 3, 5 years. `[N]` alternative: Eurostat
  business demography `bd_size` (Eurostat host approved, dataset not). `[I]` fallback: none sensible — the chapter would
  open on `brenland_firms_profit.csv` (Brenland census: share of firms with a loss, by sector).
- **Other charts** `[I]`: `brenland_firms_profit.csv` — profit rate by sector, Brenland's 500 firms (`firms.csv`).
- **Diagrams**: total revenue and total cost lines against quantity with the break-even point (TikZ; numbers from the
  worked example; affine lines drawn only as plotted points joined — g7 has no affine functions, so drawn from a table).
- **Images**: AI — a small bakery at dawn with an owner and a worker.
- **Boxes**: `measure[Profit in a firm's accounts]`.
- **Exercises**: ★ R firms still open after 3 years; ★ C revenue from price and quantity; ★ C total cost from fixed and
  variable; ★ C profit or loss; ★★ C break-even quantity by a table; ★★ C break-even by arithmetic; ★★ P a rise in rent:
  what happens to the break-even quantity, and by how much; ★★ R/C Brenland's sector with most loss-making firms; ★★ X
  observation contradicting the entry model (high profits that persist with no barrier); ★★★ C a price cut and the new
  break-even; ★★★ P many new bakeries open: price and profit, direction; ★★★ X what the survival chart cannot say about
  why firms close.
- **Weekend problem** — *Opening a juice stall* (12 questions): Part I costs (stall rent, fruit, cups); Part II revenue
  and profit at three prices; Part III a second stall opens next door, ending with the new profit and the break-even
  quantity.
- **Ledger**: `g7:bls-bed-survival-1`, `-3`, `-5` (if `[L]`).

---

# Grade 8 — The economy as a whole

Powers and weighted averages are available (mathematics g8). Opening chart per chapter.

## g8-01 Production and Productivity — `production-and-productivity`

Coverage: factors of production (labour, capital, land and resources, knowledge); output per worker and per hour; capital
per worker; better methods; productivity sets the living standard. All covered.

- **Sections**: 1 What production needs. 2 Output per worker and per hour. 3 Capital per worker. 4 Better methods.
  5 Why productivity sets the living standard.
- **Definitions**: factors of production; labour; capital (physical: tools, machines, buildings); natural resources (land);
  technology (knowledge of methods); labour productivity; capital per worker.
- **Models**: `model{Productivity and living standards}` — assumes: what a country consumes it must produce or buy with
  what it produces; predicts: income per person rises with output per hour; countries with more capital per worker
  produce more per hour; tested: opening chart; PWT capital per worker vs output per worker; breaks: oil exporters (income
  from resources), countries where many people do not work (participation), hours differences.
- **Recall**: division of labour (g7-02); income per person (g6-02); hours worked (g6-05).
- **Opening chart** `[A]`: `output_per_hour.csv` — output per hour worked (`rgdpo / (emp × avh)`) against income per
  person (`rgdpe / pop`), 2023, PWT (2021 dollars), both times-ten scale.
- **Other charts** `[A]`: `capital_per_worker.csv` — output per worker against capital per worker (`rnna / emp`), 2023,
  PWT, times-ten scales.
- **Diagrams**: a production "box" with inputs in and output out (TikZ).
- **Images**: Photograph — a historic assembly line (Commons, PD, e.g. a 1913 car assembly line, caption without names
  of persons); AI — a farmer with a hand tool beside one with a small tractor.
- **Boxes**: `measure[Output per hour]`; `measure[Measuring capital]` (the perpetual-inventory idea in words).
- **Exercises**: ★ R output per hour in two countries; ★ C output per worker; ★ C output per hour from output, workers,
  hours; ★ R capital per worker; ★★ C two countries: whose living standard is higher if same hours?; ★★ P capital per
  worker doubles in a workshop (invented table): direction and rough size of output per worker; ★★ C hours fall, output
  per hour rises: total output; ★★ R/C outliers in the opening chart (resource exporters); ★★ X observation contradicting
  the model; ★★★ C a weighted average of productivity across two sectors (powers not needed); ★★★ P moving workers from
  farms to factories: average productivity; ★★★ X what the chart cannot say about the cause.
- **Weekend problem** — *Brenland's factories* (13 questions): Part I Brenland's firms (`firms.csv`): output per worker
  by sector; Part II capital per worker and output; Part III moving 10 % of farm workers to manufacturing, ending with
  the new average output per worker (weighted average).
- **Ledger**: none needed beyond PWT (figdata).

## g8-02 Measuring an Economy: GDP — `gdp`

Coverage: value added and why sales are not added; GDP as production = income = spending (told); GDP per person; what it
leaves out. All covered.

- **Sections**: 1 From sales to value added. 2 Gross domestic product. 3 Three ways to the same total (told, with a
  circular-flow diagram). 4 GDP per person. 5 What GDP leaves out.
- **Definitions**: intermediate good; final good; value added; gross domestic product (GDP); GDP per person.
- **Models**: none boxed (accounting, not a model); a `measure[How GDP is measured]`.
- **Recall**: firms, revenue (g7-08); income per person (g6-02).
- **Opening chart** `[A]`: `largest_economies.csv` — the ten largest economies by GDP at purchasing-power parity, 2024, in
  total (`NY.GDP.MKTP.PP.KD`) and per person (`NY.GDP.PCAP.PP.KD`), paired bars, constant 2021 international dollars.
- **Other charts** `[A]`: `gdp_market_vs_ppp.csv`? — no (that is grade 9). Instead `brenland_gdp.csv` `[I]`: Brenland's
  GDP by spending (C, I, G, X − M) 2025, stacked bar (`accounts.csv`).
- **Diagrams**: a value-added chain (wheat → flour → bread) with sales and value added (TikZ); a circular flow of
  households and firms (TikZ).
- **Images**: AI — a mill, a bakery and a shop in one street.
- **Boxes**: `measure[How GDP is measured]`; `measure[What GDP leaves out]` (home work, leisure, nature, distribution).
- **Exercises**: ★ R the largest economy in total and per person; ★ C value added along a chain; ★ C GDP from final
  sales; ★ R per person rank; ★★ C double counting error; ★★ C GDP per person of an invented country; ★★ C Brenland's GDP
  from C, I, G, X, M (`accounts.csv` 2025); ★★ R/C China and the United States in total and per person (figdata);
  ★★ X what would show GDP per person a poor guide to a country's wellbeing; ★★★ C a home-cooked meal vs a restaurant
  meal: GDP changes; ★★★ C income side equals production side (invented economy of two firms); ★★★ X what GDP cannot say
  about who gets the income.
- **Weekend problem** — *Brenland's accounts* (12 questions): Part I a chain of firms and their value added; Part II the
  spending side from `accounts.csv`; Part III GDP per person and the share of each spending item, ending with GDP per
  person in dalens.
- **Ledger**: `g8:sna-2008` (the System of National Accounts definition page, UN statistics), for the measure box.

## g8-03 Inflation and Price Indices — `inflation-and-price-indices`

Coverage: a basket priced year after year; an index with base 100; the inflation rate; nominal and real values and a
wage corrected for prices; very high inflation; falling prices. All covered.

- **Sections**: 1 Pricing a basket. 2 An index with base 100. 3 The inflation rate. 4 Nominal and real. 5 Very high
  inflation, and falling prices.
- **Definitions**: basket (of goods); price index; base year; consumer price index; inflation rate; deflation;
  hyperinflation; nominal value; real value; real wage.
- **Models**: none boxed; the cause of inflation (money) belongs to the grades 10–12 volume — told in one sentence with a
  pointer. `record` boxes need a model, so the 1923 episode is a `measure`-style section with its chart and a
  photograph.
- **Recall**: weighted average (mathematics, grade 8, in prose); price (g7-04).
- **Opening chart** `[A]`: `inflation_century.csv` — yearly consumer-price inflation, 1920–2020, United States, United
  Kingdom, France, Japan: `jst(cols=["cpi"])`, percent change. (BLS extends the US to 2025 in prose.)
- **Other charts** `[A]`: `germany_1923.csv` — Germany's consumer price level, 1914–1924, times-ten scale (`jst("DEU")`,
  `cpi`, rebased 1914 = 1): about eleven powers of ten. `bls_cpi_us.csv` — US CPI since 1913 (`bls_cpi()`, annual M13),
  times-ten (optional).
- **Diagrams**: a basket of five goods priced in two years (TikZ table-figure).
- **Images**: Photograph — a German 1923 banknote (Commons, PD; check licence); AI — a shop shelf with price tags
  without readable numbers.
- **Boxes**: `measure[The consumer price index]` (survey of prices, basket weights from a spending survey; Brenland's
  basket uses 2015 weights).
- **Exercises**: ★ R inflation in one year from the chart; ★ C a basket cost in two years; ★ C an index with base 100;
  ★ C inflation rate from two index values; ★★ C Brenland's CPI from `basket.csv` for a year (Laspeyres, weighted average);
  ★★ C a real wage from a nominal wage and an index; ★★ R the years of deflation in the opening chart; ★★ C prices
  doubling every month for a year (powers of 2); ★★ X what would show the CPI overstates the rise in the cost of living
  (new goods, substitution — in words); ★★★ C a real value over 20 years (Brenland `accounts.csv` GDP and deflator);
  ★★★ R/C Germany's price level from 1919 to 1923 in powers of ten; ★★★ X what the index cannot say about one
  family's prices.
- **Weekend problem** — *The Brenmoor basket* (13 questions): Part I price the 2015 basket (`basket.csv`); Part II the
  CPI and inflation 2015–2025; Part III a wage of 2015 and 2025 in real terms, ending with the real wage change in percent.
- **Ledger**: `g8:german-1923-peak` (date of the stabilisation, Rentenmark, November 1923, primary source or central
  bank page); `g8:zimbabwe-2008` (optional).

## g8-04 Growth and Compounding — `growth-and-compounding`

Coverage: growth rate of real GDP per person; growth on growth with powers; doubling time and rule of 70 (admitted);
small differences over decades. All covered.

- **Sections**: 1 The growth rate. 2 Growth on growth. 3 Doubling time. 4 Small differences, large gaps.
- **Definitions**: growth rate; compound growth; doubling time; rule of 70 (as a result, stated with `\admitted`; proved
  with the logarithm in the grades 10–12 volume — a `proposition` with `\admitted`).
- **Models**: `model{Steady growth}` — assumes: income per person grows at a fixed yearly rate; predicts: it doubles every
  70/g years; tested: the United States near 2 % for 150 years (Maddison, figdata); breaks: catch-up episodes (South
  Korea), wars and crises, countries that stall.
- **Recall**: rate of change (g6-01); powers (mathematics, grade 8); income per person, catch-up (g6-02).
- **Opening chart** `[A]`: `three_speeds.csv` — real GDP per person since 1960 (`NY.GDP.PCAP.KD`, constant 2015 US$),
  three countries chosen by computed average growth near 1 %, 2 % and 6 % (candidates: Argentina/Mexico ~1 %,
  USA/France ~2 %, South Korea/China ~5–6 %), times-ten scale. Selection rule written in the script and tested.
- **Other charts** `[A]`: `us_two_centuries.csv` — US income per person 1820–2022 (Maddison) times-ten with a 2 % line.
- **Diagrams**: a staircase of compound growth vs simple growth (TikZ; values from a table).
- **Images**: AI — a child measuring height on a door frame year after year (metaphor-free: illustrates growth on growth
  of a quantity; caption says what it is).
- **Boxes**: `measure[Real GDP per person]`.
- **Exercises**: ★ R income per person of the three countries in 1960 and 2024; ★ C a growth rate from two years; ★ C
  growth on growth for 3 years; ★ C doubling time at 7 % by the rule of 70; ★★ C 1.02^35 with powers (≈ 2); ★★ C 20 years
  at 1 % vs 3 %; ★★ R average growth from the chart; ★★ P a country at 5 % from \$2,000: income in 28 years; ★★ X
  observation contradicting the model (US growth far from steady in 1930s); ★★★ C when does a poorer country at 6 % pass a
  richer one at 2 % (table by powers); ★★★ P halving the growth rate: doubling time; ★★★ X what the rule of 70 cannot say
  about why a country grows.
- **Weekend problem** — *Two neighbours, sixty years* (12 questions): Part I Brenland and Kestria's real GDP per person
  (`accounts.csv` Brenland; Kestria invented in the chapter script); Part II their growth rates; Part III projections,
  ending with the year Kestria would catch Brenland at constant rates.
- **Ledger**: none needed.

## g8-05 Jobs, Wages and Unemployment — `jobs-wages-unemployment`

Coverage: the labour market; employed, unemployed, outside; unemployment and participation rates and the survey; why
wages differ; wages and productivity over long periods. All covered.

- **Sections**: 1 The labour market. 2 Employed, unemployed, outside the labour force. 3 Two rates and the survey.
  4 Why wages differ. 5 Wages and productivity over a century.
- **Definitions**: labour market; employed person; unemployed person; labour force; outside the labour force;
  unemployment rate; participation rate; labour force survey. (*Wage* is owned by g7-07.)
- **Models**: `model{Wages follow productivity}` — assumes: competing employers pay workers up to what they add;
  predicts: over decades real wages rise with output per hour; tested: JST real wages against real GDP per person,
  1870–2020 (second chart); breaks: in the short run, and where the labour share changes (the size of any gap is an
  empirical question, taken up in a later volume).
- **Recall**: hours worked, sectors (g6-05); real wage (g8-03); productivity (g8-01).
- **Opening chart** `[A]`: `unemployment_fifty_years.csv` — unemployment rate, 1970–2020, United States, United Kingdom,
  Germany, Spain, Japan: `jst(cols=["unemp"])`.
- **Other charts** `[A]`: `real_wages.csv` — real wage index (`wage / cpi`) and real GDP per person (`rgdpmad`), 1870–2020,
  three JST countries, both 1913 = 100, times-ten scale.
- **Diagrams**: a population box split into under 15, outside the labour force, employed, unemployed (TikZ; numbers from
  Brenland 2025).
- **Images**: AI — a job fair hall with tables (no text).
- **Boxes**: `measure[The labour force survey]` (the ILO definition: no work, available, searching; ledger).
- **Exercises**: ★ R Spain's highest rate; ★ C unemployment rate from counts; ★ C participation rate; ★ R the year two
  lines cross; ★★ C Brenland's unemployment rate and labour force (`accounts.csv`); ★★ C a person who stops searching:
  rates change; ★★ R real wage growth over a century (figdata); ★★ P productivity rises 2 % a year for 35 years: direction
  and size of real wages (doubling); ★★ X observation that contradicts the model; ★★★ C a weighted average wage of two
  occupations; ★★★ P a fall in participation with the same employment: the rate; ★★★ X what the rate cannot say about
  hours or job quality.
- **Weekend problem** — *The Brenland labour survey* (12 questions): Part I classify 20 invented survey answers; Part II
  the rates; Part III Brenland 2000–2025 (`accounts.csv`), ending with the year of the highest rate and its value.
- **Ledger**: `g8:ilo-unemployment-definition` (ILO resolution, 13th/19th ICLS).

## g8-06 Banks, Saving and Interest — `banks-saving-interest`

Coverage: deposits and loans; interest as the price of borrowing; simple and compound interest; risk and duration; the
interest rate after inflation (first look); a bank keeps part of its deposits (told). All covered.

- **Sections**: 1 What a bank does. 2 Interest, the price of borrowing. 3 Simple and compound interest. 4 Why rates
  differ. 5 Interest after inflation, a first look. 6 What a bank keeps at hand (told).
- **Definitions**: bank; deposit; loan; principal; interest; interest rate; simple interest; compound interest; risk
  (of a loan: default). The *real interest rate* is owned by grade 12 (`present-value`): here "the interest rate minus
  inflation" in words, no definition pair (sync to confirm).
- **Models**: `model{Risk and the interest rate}` — assumes: lenders want to be paid for waiting and for the risk of not
  being repaid; predicts: riskier and longer loans carry higher rates; tested: government rates in the JST panel rise in
  crises; a long rate above a short rate most of the time (JST `ltrate` vs `stir`); breaks: when a central bank fixes
  rates, and in a flight to safety.
- **Recall**: saving (g7-07); money (g7-04); inflation rate (g8-03); powers (mathematics g8); compound growth (g8-04).
- **Opening chart** `[A]`: `long_rates.csv` — long-term government bond rates, 1870–2020, United States, United Kingdom,
  France, Germany, Italy, Japan (`jst(cols=["ltrate"])`). Outline says "two centuries": 150 years with JST.
- **Other charts** `[A]`: `long_minus_short.csv` — long rate minus short rate, United States, 1870–2020 (`ltrate`, `stir`).
- **Diagrams**: a bank's balance as two columns (deposits; loans and reserves) (TikZ); simple vs compound interest
  staircase.
- **Images**: AI — a small bank counter (no logo, no text).
- **Boxes**: `measure[A government bond's rate]`; `dated{2026}` (a current central-bank rate, ledger).
- **Exercises**: ★ R the 1980s peak in one country; ★ C simple interest; ★ C compound interest over 3 years; ★ R the
  lowest rates on the chart; ★★ C compound interest over 10 years with powers; ★★ C two loans: the cheaper one; ★★ P a
  riskier borrower: direction and size of the rate (invented spread); ★★ C rate minus inflation for two years (figdata);
  ★★ X observation contradicting the risk model; ★★★ C the doubling time of a deposit at 5 % (recall rule of 70);
  ★★★ C a bank with 10 % kept at hand: how much it can lend from a deposit (one step, told); ★★★ X what the chart cannot
  say about why rates fell after 1980.
- **Weekend problem** — *Saving for a boat* (12 questions): Part I a deposit at simple and compound interest; Part II a
  loan for the boat at two rates; Part III Brenland's policy rate and inflation (`accounts.csv`), ending with the rate
  minus inflation and what the deposit buys after ten years.
- **Ledger**: `g8:policy-rate-2026` (central bank page, dated).

## g8-07 Taxes and Public Spending — `taxes-and-public-spending`

Coverage: what governments spend on; the main taxes; budget, deficit and debt; a tax changes what people buy, sell, do
(first look). All covered; government failure is the grades 10–12 volume's (g11), named in one sentence.

- **Sections**: 1 What governments spend on. 2 The main taxes. 3 The budget, the deficit and the debt. 4 A tax changes
  behaviour. 5 Who decides (one paragraph, pointer to the later volume).
- **Definitions**: tax; public spending; income tax; tax on purchases (sales tax, value-added tax); payroll tax;
  government budget; budget deficit; budget surplus; public debt; average tax rate; marginal tax rate (contested with
  Book 2: see DEFINITIONS).
- **Models**: `model{Taxes change behaviour}` — assumes: people respond to after-tax prices and wages; predicts: a tax on a
  good lowers the quantity bought, more when buyers have alternatives; tested: cigarette taxes and consumption (a
  published estimate, ledger); breaks: goods with no substitutes in the short run; evasion.
- **Recall**: income, transfers, disposable income (g7-07); GDP (g8-02); interest (g8-06).
- **Opening chart** `[A]`: `public_spending.csv` — central government expenditure as a share of GDP, 1880–2020, United
  States, United Kingdom, France, Sweden, Japan, Germany (`jst(cols=["expenditure","gdp"])`). Caption: "central
  government" (JST definition). Outline says "public spending": general government needs OECD/IMF (refused); state it.
- **Other charts** `[A]`: `debt_gdp.csv` — public debt as a share of GDP, 1880–2020, same countries (`jst` `debtgdp`).
  `[I]`: Brenland's tax bands (`TAX_BANDS`) as a step chart.
- **Diagrams**: a bathtub of debt (deficits pour in, surpluses drain) (TikZ).
- **Images**: AI — a town street with a school, a road crew and a clinic.
- **Boxes**: `measure[General and central government]`; `dated{2026}` (one current VAT rate or income-tax band, ledger).
- **Exercises**: ★ R the share in 1913 and 1950 for two countries; ★ C a deficit from revenue and spending; ★ C debt next
  year from debt and deficit; ★ C a sales tax on a price; ★★ C income tax under Brenland's bands (`TAX_BANDS`); ★★ C
  average and marginal tax rates; ★★ R debt peaks after the wars; ★★ P a tax on sugary drinks: direction and rough size
  of the fall in purchases (elasticity told as a number from the ledger); ★★ X observation contradicting the model;
  ★★★ C debt as a share of GDP after two years with growth (Brenland `accounts.csv`); ★★★ C who pays a payroll tax in
  money (told split, numbers); ★★★ X what the spending chart cannot say about what the spending achieved.
- **Weekend problem** — *Brenland's budget* (13 questions): Part I revenue, spending, deficit 2015–2025 (`accounts.csv`);
  Part II the debt and the debt share of GDP; Part III a household's income tax under the bands, ending with its average
  and marginal rates.
- **Ledger**: `g8:cigarette-tax-elasticity` (a published estimate, e.g. a review in a public-health journal);
  `g8:vat-rate-2026` (a national tax authority page, dated).

## g8-08 Competition and Monopoly: A First Look — `competition-and-monopoly-first-look`

Coverage: many sellers vs one; competition pushes price toward cost and rewards a better product; a single seller sells
less at a higher price; sources of monopoly (patent, licence, network, large fixed costs); the threat of entry. All
covered. Opening chart: `[A]` fallback from Eurostat; `[L]` preferred.

- **Sections**: 1 Many sellers, one seller. 2 What competition does to the price. 3 What a single seller does. 4 Where a
  monopoly comes from. 5 The threat of entry.
- **Definitions**: competition; monopoly; barrier to entry; patent; network effect; natural monopoly (large fixed costs).
- **Models**: `model{Competition and entry}` — assumes: sellers can enter freely, buyers compare prices; predicts: price
  falls toward cost when entry opens; a sole seller sells less at a higher price; tested: the opening chart's
  liberalisation; airline deregulation (ledger); breaks: natural monopoly, network effects, collusion (grade 11).
- **Recall**: profit, entry and exit (g7-08); market price (g7-05).
- **Opening chart** `[A]` fallback: `telecom_prices.csv` — real price index of telephone equipment and services relative to
  all consumer prices, Germany and France, 1996–2025 (`eurostat("prc_hicp_aind")`, `CP0820`, `CP0830` ÷ `CP00`) — the EU
  opened telecom markets on 1 January 1998 (ledger). Few years before the opening: stated. `[L]` preferred: US average
  domestic air fare before and after 1978 (a published BTS/agency table) or the real price of a London–New York call.
- **Other charts**: `[I]` the juice-stall example of g7-08 with one seller vs five sellers (invented table).
- **Diagrams**: a market with one seller and with many (TikZ icons and a price scale).
- **Images**: AI — two bus companies' buses at one stop (no logos, no text).
- **Boxes**: `record[Opening the telephone market]` (EU 1998 liberalisation, what the model said, what the price did;
  ledger); `measure[A real price]`.
- **Exercises**: ★ R the fall of the real price of phones; ★ C a price above cost: the margin per unit; ★ R years of the
  steepest fall; ★ C revenue of a single seller at two prices; ★★ C the single seller's best price in a table; ★★ C the
  same market with free entry: price and quantity; ★★ P a patent expires: direction and rough size of the price (ledger
  generic-drug figure); ★★ R/C real price change in percent (figdata); ★★ X observation contradicting the model (entry
  with no price fall); ★★★ C a natural monopoly: average cost with large fixed cost and two firms vs one; ★★★ P a network
  good: why one seller can win; ★★★ X what the chart cannot say about quality changes.
- **Weekend problem** — *The ferry to Kestria* (12 questions): Part I one ferry company's prices and passengers
  (invented demand table); Part II a second company enters; Part III the threat of entry alone, ending with the price
  and the number of passengers with two firms.
- **Ledger**: `g8:eu-telecom-1998` (Directive 96/19/EC); `g8:generic-entry-price` (a published estimate, e.g. an FDA
  analysis page); `g8:airline-deregulation-1978` (Airline Deregulation Act date).

---

# Grade 9 — Markets with algebra, and the world economy

Affine functions and one-unknown equations are available; mean and median (mathematics g9).

## g9-01 Demand and Supply with Equations — `demand-and-supply-equations`

Coverage: affine demand and supply; equilibrium by one equation; a shift as a change of intercept; direction for each
shift; checked on a real episode; the full model frame. All covered.

- **Sections**: 1 Demand as an affine function of the price. 2 Supply as an affine function. 3 Solving for the
  equilibrium. 4 Shifts as changes of intercept. 5 Four predictions and a test.
- **Definitions**: demand function; supply function; shock (a change that shifts a curve). (Equilibrium price and
  quantity are g7-06's.)
- **Models**: `model{Supply and demand}` (Book 1's full frame) — assumes: many buyers and sellers, one good, free price;
  predicts: a fall in cost lowers the price and raises the quantity, by amounts set by the two slopes; tested: the opening
  chart's episode; laboratory markets (Smith 1962, *JPE* 70(2)); breaks: few sellers, hidden quality, a price that cannot
  move. Propositions: the equilibrium of $Q^d = a - bp$, $Q^s = c + dp$ is $p^* = (a-c)/(b+d)$ (proof by solving).
- **Recall**: demand and supply tables and curves, equilibrium (g7-06); affine functions (mathematics, grade 9).
- **Opening chart**: `[A]` fallback: `phones_price_quantity.csv` — mobile telephone equipment real price index (HICP
  `CP08202` ÷ `CP00`, EU countries with data) and mobile subscriptions per 100 people (`IT.CEL.SETS.P2`, `EUU`),
  1996–2010: price down, quantity up. `[L]` preferred: solar module price and installed capacity, 2010–2023 (IRENA
  published tables).
- **Other charts**: none; the diagrams carry the algebra.
- **Diagrams** (TikZ `econ`): the worked example's lines crossing at the computed equilibrium; a supply shift (`shifted`)
  with new equilibrium; the four shift cases in a 2 × 2 panel.
- **Images**: Photograph — solar panels in a field (Commons PD/CC BY), if the solar case is used.
- **Boxes**: `record[Laboratory markets]` (Smith 1962: prices converge to the predicted equilibrium); `measure[Reading a
  slope]`.
- **Exercises**: ★ R price and quantity from the opening chart; ★ C quantity demanded at a price from $Q^d$; ★ C the
  equilibrium of two given lines; ★ R intercept and slope from a graph; ★★ C the equilibrium after a demand shift; ★★ C
  after a supply shift; ★★ P a cost fall of \dal{2} per unit: price change (by the formula); ★★ C excess demand at a price
  below; ★★ X observation contradicting the model (price and quantity both up after a supply rise alone); ★★★ C both
  curves shift: new equilibrium; ★★★ P which curve is steeper decides who gets the price fall; ★★★ X what the opening chart
  cannot say (which curve moved, and whether demand moved too).
- **Weekend problem** — *The Brenmoor fish market* (13 questions): Part I demand and supply lines from invented tables;
  Part II equilibrium, surplus and shortage at given prices; Part III a new harbour lowers costs (intercept change),
  ending with the new price and quantity and the change in fishermen's revenue.
- **Ledger**: `g9:smith-1962`; `g9:irena-solar` (if `[L]`).

## g9-02 Elasticity: A First Look — `elasticity-first-look`

Coverage: % change in quantity for 1 % change in price; elastic and inelastic; revenue when price rises; necessities and
luxuries; long run vs short run. All covered. Opening chart needs `[L]`.

- **Sections**: 1 How strongly buyers respond. 2 Elastic and inelastic. 3 Price and revenue. 4 Necessities and luxuries.
  5 Short run and long run.
- **Definitions**: price elasticity of demand; elastic demand; inelastic demand; necessity; luxury. (Point and arc
  elasticities are grade 10's.)
- **Models**: `model{Elastic and inelastic demand}` — assumes: a stable demand, other things equal; predicts: a price rise
  raises revenue when demand is inelastic and lowers it when elastic; tested: fuel taxes and transit fares (ledger);
  breaks: when other things change at the same time, and when the long-run response differs.
- **Recall**: demand function (g9-01); percentage change as a multiplier (mathematics, grade 9); taxes change behaviour
  (g8-07).
- **Opening chart** `[L]`: `elasticities.csv` — mean price elasticities of demand for food categories (Andreyeva, Long and
  Brownell 2010, *AJPH* 100(2), Table 1: 16 categories), plus fuel (short and long run) and cigarettes — horizontal bars,
  each value a ledger row. **No `[A]` fallback exists**: approved datasets hold no elasticity. Without `[L]`, the opening
  chart would be Brenland-invented (unfit as an opening fact) — this is the chapter most dependent on the sync ruling.
- **Other charts**: `[I]` revenue against price along an invented affine demand (table).
- **Diagrams**: a steep and a flat demand line with the same price rise (TikZ); revenue rectangles before and after.
- **Images**: AI — a fuel station forecourt (no brand, no price display text).
- **Boxes**: `measure[An elasticity from data]` (comparing two periods; other things equal); `record[Fuel prices in 2022]`
  (short-run response small; ledger).
- **Exercises**: ★ R the most and least elastic goods; ★ C elasticity from two percent changes; ★ C elastic or inelastic;
  ★ C revenue at two prices; ★★ P a 10 % price rise with elasticity 0.4: quantity and revenue; ★★ P the same with 1.5;
  ★★ C elasticity from a table of prices and quantities (percent changes from the start point); ★★ R short vs long run for
  fuel; ★★ X observation contradicting the model; ★★★ C revenue-maximising price on an invented affine demand (by table);
  ★★★ P a tax on a necessity vs a luxury: which raises more revenue; ★★★ X why a measured elasticity may mislead.
- **Weekend problem** — *The bus fare of Brenmoor* (12 questions): Part I riders at two fares; Part II elasticity and
  revenue; Part III a fare cut and a long-run response, ending with the long-run revenue change in dalens.
- **Ledger**: `g9:andreyeva-2010-<category>` (16 rows); `g9:fuel-elasticity-short`, `-long` (a review, e.g. Havranek,
  Irsova and Janda 2012, *Energy Economics* 34(1)); `g9:cigarette-elasticity` (shared with g8 if possible).

## g9-03 Price Controls, Taxes and Subsidies — `price-controls-taxes-subsidies`

Coverage: price ceiling below equilibrium (shortage, queues, quality); price floor above (unsold surplus); tax per unit
(buyer's price rises by less than the tax; seller's falls; who bears it); subsidy as a negative tax; each with a
documented episode. All covered. Opening chart needs `[L]`.

- **Sections**: 1 A maximum price. 2 A minimum price. 3 A tax per unit. 4 Who bears the tax. 5 A subsidy.
- **Definitions**: price ceiling; price floor; tax per unit; subsidy. ("Tax incidence" and "deadweight loss" are grade
  10's: the chapter says "who bears the tax" in words, with numbers, and no definition pair.)
- **Models**: `model{A price ceiling}` — predicts a shortage equal to $Q^d - Q^s$ at the ceiling, queues and lower quality;
  tested: the opening chart's episode; breaks: if the ceiling is above the equilibrium (no effect), black markets.
  `model{A tax per unit}` — predicts the buyer's price rises by $\tau\,b/(b+d)$… in grade-9 form: by a share of the tax set
  by the slopes; tested: fuel tax pass-through (ledger study); breaks: few sellers.
- **Recall**: shortage and surplus (g7-05); supply and demand lines (g9-01); elasticity (g9-02).
- **Opening chart** `[L]`: rent control in San Francisco — rental supply of buildings covered by the 1994 extension vs
  not covered (Diamond, McQuade and Qian 2019, *AER* 109(9), published table values), or the US gasoline queues of 1979
  (EIA published monthly retail prices and a published queue study). No `[A]` fallback (sync).
- **Other charts**: `[I]` a price floor in an invented milk market (unsold stock by year).
- **Diagrams** (TikZ): ceiling below equilibrium with the shortage marked; floor above with the surplus; a tax wedge with
  buyer and seller prices (geometry from the worked example: lines and prices match); subsidy wedge.
- **Images**: AI — a queue outside a shop at dawn.
- **Boxes**: `record[Rent control in San Francisco]` (or 1979 gasoline); `record[A fuel tax cut]` (pass-through study,
  ledger: e.g. a published study of a temporary fuel-tax cut in 2022, Germany, Montag, Sagimuldina and Schnitzer); neutral
  wording: what the policy did, to whom, by how much.
- **Exercises**: ★ R the change in the opening chart; ★ C shortage at a ceiling; ★ C surplus at a floor; ★ C buyer's
  and seller's prices with a tax (given equilibrium); ★★ C the new equilibrium with a tax per unit (shift intercept);
  ★★ C tax revenue; ★★ P a ceiling above equilibrium: effect; ★★ C a subsidy's effect on price and quantity; ★★ X
  observation contradicting the ceiling model; ★★★ C who bears more of the tax with two slopes; ★★★ P a steeper supply:
  how the tax split changes; ★★★ X what a before-and-after chart cannot say about the cause.
- **Weekend problem** — *Bread in a hard winter* (13 questions): Part I Brenmoor's bread market (lines); Part II a town
  ceiling and the shortage; Part III the ceiling replaced by a subsidy per loaf, ending with the subsidy's cost and the
  price paid by buyers.
- **Ledger**: `g9:dmq-2019` (rows of the chart values); `g9:fuel-tax-cut-2022` (published study, pass-through share).

## g9-04 International Trade — `international-trade`

Coverage: comparative advantage between countries (recalled); exports, imports, trade balance; what countries sell each
other and how it changes; a tariff as a tax on imports, who gains and who loses (first look); distance and transport
costs. All covered. Programme note: migration and remittances (geography course) get one paragraph with a figdata number
(`BX.TRF.PWKR.DT.GD.ZS`).

- **Sections**: 1 Comparative advantage between countries. 2 Exports, imports and the balance. 3 What countries sell.
  4 A tariff. 5 Distance.
- **Definitions**: trade balance; trade surplus; trade deficit (qualified forms); tariff; import quota. (*Export* and
  *import*: g6-07 proposed; see DEFINITIONS.)
- **Models**: `model{A tariff in a small country}` — assumes: the country's buyers cannot move the world price; predicts:
  the home price rises by the tariff, imports fall, home producers and the state gain, home buyers lose more than they
  gain; tested: the 2018 US washing-machine tariffs (Flaaen, Hortaçsu and Tintelnot 2020, *AER* 110(7)): prices rose
  about 12 %; breaks: a large country moves the world price; retaliation.
- **Recall**: comparative advantage, exchange ratio (g7-03); exports, imports, trade share (g6-07); supply and demand lines
  (g9-01).
- **Opening chart** `[A]`: `korea_exports_mix.csv` — South Korea's merchandise exports by product group, 1965 and 2024
  (WDI `TX.VAL.FOOD.ZS.UN`, `TX.VAL.AGRI.ZS.UN`, `TX.VAL.FUEL.ZS.UN`, `TX.VAL.MMTL.ZS.UN`, `TX.VAL.MANF.ZS.UN`),
  paired bars: manufactures 59.3 % → 87.3 %.
- **Other charts** `[A]`: `world_tariffs.csv` — applied tariff, weighted mean, all products, world and five countries,
  1990s–2024 (`TM.TAX.MRCH.WM.AR.ZS`).
- **Diagrams**: a small-country tariff diagram on affine supply and demand with the world price line (TikZ; numbers
  match the worked example; areas described in words, surplus areas are grade 10's).
- **Images**: Photograph — a container ship in port (Commons, licence read; distinct from g6-07's port photo).
- **Boxes**: `record[Washing machines, 2018]`; `measure[The trade balance]`.
- **Exercises**: ★ R Korea's manufactures share in 1965 and 2024; ★ C a trade balance; ★ R a country's tariff in two
  years; ★ C a price with a tariff; ★★ C imports before and after a tariff (lines); ★★ C tariff revenue; ★★ P a tariff
  doubled: home price and imports, direction and size; ★★ C Brenland's trade balance with Kestria (`trade.csv`); ★★ X
  observation contradicting the model; ★★★ C who gains how much in dalens (producers' extra revenue on home sales vs
  buyers' extra spending — rectangles only); ★★★ P transport costs halve: trade, direction; ★★★ X what the export-mix
  chart cannot say about why Korea changed.
- **Weekend problem** — *A tariff on Kestrian cloth* (13 questions): Part I Brenland's cloth market and the world price;
  Part II a tariff: price, imports, revenue; Part III who gains and loses, ending with the buyers' extra spending against
  the producers' and state's gains in dalens.
- **Ledger**: `g9:fht-2020-price-effect`; `g9:remittances` is figdata (no row).

## g9-05 Exchange Rates and Purchasing Power — `exchange-rates-and-purchasing-power`

Coverage: the price of one currency in another; converting; a currency rising or falling and import/export prices; one
basket costs different amounts; purchasing-power conversion. All covered. Programme note: a currency shared by several
countries (the euro) gets one `dated{2026}` paragraph (ledger).

- **Sections**: 1 The price of a currency. 2 Converting amounts. 3 When a currency rises or falls. 4 One basket, many
  prices. 5 Purchasing-power conversion.
- **Definitions**: currency; exchange rate (domestic per foreign: the series convention); appreciation; depreciation;
  price level (of a country, relative); purchasing-power conversion (PPP rate).
- **Models**: `model{The law of one price}` — assumes: goods can be shipped cheaply and freely; predicts: a traded good
  costs about the same everywhere once converted; tested: the price level against income (second chart: poorer countries
  have lower price levels, because services are cheap); breaks: services that cannot be shipped (a haircut), tariffs,
  transport costs.
- **Recall**: price index (g8-03); GDP per person (g8-02); exports and imports (g6-07 or g9-04).
- **Opening chart** `[A]`: `market_vs_ppp.csv` — GDP per person of ten countries, 2024, at market exchange rates
  (`NY.GDP.PCAP.CD`) and at purchasing-power parity (`NY.GDP.PCAP.PP.CD`), current dollars, paired bars.
- **Other charts** `[A]`: `price_level_income.csv` — price level of household consumption (`PA.NUS.PRVT.PLI`) against GDP
  per person (PPP), 2024, `omincomex`.
- **Diagrams**: a two-way conversion arrow (dalens ↔ kests) with the rate (TikZ).
- **Images**: AI — a traveller at a currency exchange counter (no readable rates).
- **Boxes**: `measure[Purchasing-power conversion]` (ICP survey prices; ledger page); `dated{2026}` (euro-area members,
  ledger).
- **Exercises**: ★ R two countries' gap at market vs PPP; ★ C convert dalens to kests; ★ C a price after depreciation;
  ★ R the price level of two countries; ★★ C Brenland's rate (`trade.csv`): depreciation in percent; ★★ C an import's price
  after a 10 % depreciation; ★★ P a depreciation: exports and imports, direction; ★★ C a PPP rate from a basket in two
  currencies; ★★ X observation contradicting the law of one price; ★★★ C GDP per person converted both ways (invented);
  ★★★ P why a haircut is cheaper in a poorer country; ★★★ X what the market-rate comparison overstates or understates.
- **Weekend problem** — *A summer in Kestria* (12 questions): Part I convert a holiday budget; Part II the rate moves
  (`trade.csv`); Part III a basket in both countries and the PPP rate, ending with Brenland's and Kestria's GDP per person
  compared at both rates.
- **Ledger**: `g9:icp-2021` (World Bank ICP page, what PPP is); `g9:euro-members-2026` (ECB page, dated).

## g9-06 Why Some Countries Are Rich: Institutions — `institutions-and-prosperity`

Coverage: three natural experiments (Germanys, Koreas, China 1978); what differs (ownership, who decides, free prices,
contract enforcement); income against property rights and corruption; a cross-country correlation is not yet a cause. The
WGI chart is refused (licence): **gap** — "income against measures of property rights and corruption" is given through
cited study results (ledger), not a chart. Approved substitute chart: `IC.FRM.BRIB.ZS` (bribery incidence, World Bank
Enterprise Surveys, CC BY 4.0) against income — a measure of corruption from firm surveys `[A]`.

- **Sections**: 1 One people, two systems: the Koreas. 2 The two Germanys. 3 China before and after 1978. 4 What differs:
  ownership, decisions, prices, contracts. 5 Across countries: a correlation, not yet a cause.
- **Definitions**: institution; property right; contract enforcement; planned economy; market economy; natural
  experiment; correlation (if the mathematics series does not own it at grade 9 — harvest at writing).
- **Models**: `model{Institutions and income}` — assumes: people invest and trade more when they keep what they earn and
  contracts are enforced; predicts: with the same people and geography, market institutions give higher income per
  person over decades; tested: the Koreas, the Germanys, China after 1978; breaks: across countries the link is a
  correlation (geography, history, culture also differ), and fast growth has also happened without secure rights for
  everyone (the chapter states the evidence and leaves the cause question to the Year 3 volume).
- **Recall**: income per person, catch-up (g6-02); growth rates (g8-04); markets and prices (g7-05).
- **Opening chart** `[A]`: `koreas.csv` — income per person, South and North Korea, 1940–2022 (Maddison `KOR`, `PRK`),
  times-ten. **Maddison has no North Korea estimates for 1944–1989**: the line shows 1940–1943 and 1990–2022, the gap is
  stated in the caption. Values: 1940 North 2,624, South 1,975; 2022 North 1,569, South 41,321 (2011 dollars).
- **Other charts** `[A]`: `china_1978.csv` — China's income per person, 1950–2022 (Maddison), times-ten, 1978 marked;
  `bribery_income.csv` — share of firms asked for a bribe against income per person, latest survey year per country
  (`IC.FRM.BRIB.ZS`, `NY.GDP.PCAP.PP.KD`).
- **Diagrams**: a 2 × 2 table of what differs (TikZ).
- **Images**: Photograph — the Korean peninsula at night from the International Space Station (NASA, public domain).
- **Boxes**: `record[Germany, 1949–1990]` (East and West income per person at unification — ledger rows from a published
  estimate); `record[China after 1978]` (household responsibility system dates — ledger, e.g. Lin 1992, *AER* 82(1));
  `measure[A correlation across countries]`.
- **Exercises**: ★ R the two Koreas in 1940 and 2022; ★ C how many times richer the South is; ★ R China's income in 1978
  and 2022; ★ C China's average growth since 1978 (powers, by table); ★★ C the Koreas' growth rates 1990–2022; ★★ R/C
  bribery at two incomes; ★★ P a reform that secures farmers' right to sell output: direction of farm output (Lin 1992,
  size); ★★ C Germany: East as a share of West (ledger); ★★ X observation contradicting the model; ★★★ C a correlation in
  an invented 6-country table: what a third factor could do; ★★★ P what the model predicts for a country that
  nationalises farms; ★★★ X why the cross-country chart is not a cause.
- **Weekend problem** — *Two valleys* (12 questions): Part I two invented valleys, same land and people, different rules
  for harvests (seeded table); Part II their output over 20 years (growth rates); Part III a reform in the poorer valley,
  ending with the years needed to halve the gap.
- **Ledger**: `g9:germany-east-west-1989` (a published estimate, e.g. an official statistical office publication);
  `g9:lin-1992`; `g9:china-reform-1978` (date of the Third Plenum, primary source); `g9:north-korea-gap` (none, figdata).

## g9-07 Who Earns What: Income Distribution — `income-distribution`

Coverage: mean and median income; shares by fifths; inequality inside and between countries; the world distribution over
time; world poverty fell while inequality rose inside some countries. All covered; "1975" is not possible with the
approved PIP file (survey years only): **1990 and 2019** with a stated method, or a `[N]` lineup file.

- **Sections**: 1 Mean and median income. 2 Shares by fifths. 3 Inequality inside a country. 4 Between countries.
  5 The world distribution, then and now. 6 Two facts together.
- **Definitions**: income distribution; mean income; median income; income share of a fifth (quintile share);
  inequality within a country; inequality between countries; world income distribution. (Lorenz curve and Gini are grade
  11's.)
- **Models**: none boxed (a description chapter). A `debate` box? No: the open questions of inequality's causes go to
  grade 11 and Year 3.
- **Recall**: mean and median (mathematics, grade 9); poverty line, poverty rate (g6-03); purchasing-power conversion
  (g9-05).
- **Opening chart** `[A]` with a stated method: `world_distribution.csv` — the world distribution of income (people by
  income per day, 2021 PPP dollars, times-ten x-axis), around 1990 and around 2019: each country's survey percentiles
  (`pip_percentiles`) from the survey year nearest the target (±3 years), weighted by population (`SP.POP.TOTL`) in the
  target year; coverage in percent of world population printed in the caption. `[N]` preferred: PIP's line-up
  percentiles (every country in every year).
- **Other charts** `[A]`: `top_fifth_share.csv` — income share of the top fifth (`SI.DST.05TH.20`), United States, China,
  India, Brazil, Sweden, United Kingdom, survey years since 1980.
- **Diagrams**: five bars of fifths for an invented town (TikZ); mean vs median on a skewed invented distribution.
- **Images**: AI — a street of houses of different sizes (no text).
- **Boxes**: `measure[Income or consumption]` (surveys measure one or the other); `measure[World distribution]`.
- **Exercises**: ★ R the world's median-ish peak in 1990 and 2019; ★ C mean and median of a list of 9 incomes;
  ★ C shares by fifths of an invented town; ★ R the top-fifth share of two countries; ★★ C Brenland's fifths
  (`households.csv`, disposable income); ★★ C mean vs median after a rich newcomer; ★★ R/C the change in China's top-fifth
  share (figdata); ★★ C between-country gap with two countries (invented); ★★ X what would contradict "world poverty fell";
  ★★★ C a transfer from the top fifth: new shares; ★★★ R both facts in one table (world poverty share, two countries'
  top shares); ★★★ X what a fifths share cannot say about mobility.
- **Weekend problem** — *Brenland's fifths* (13 questions): Part I mean and median of Brenland's disposable income
  (`households.csv`); Part II shares by fifths before and after taxes and transfers (gross vs disposable); Part III the
  bottom fifth against the \$3.00 line converted (invented PPP rate), ending with the share of the top fifth before and
  after taxes and transfers.
- **Ledger**: none beyond figdata; `g9:pip-lineup-method` (PIP methodology page) for the measure box.

---

## Programme coverage (checked 2026-11-20)

Sources checked: CORE Econ *The Economy 2.0* unit list (books.core-econ.org, fetched); OpenStax *Principles of Economics
3e* (chapter 1 page fetched; detail page JavaScript-only, the rest from knowledge); a published principles textbook's
opening chapters from knowledge (ten principles, thinking like an economist, interdependence and gains from trade,
supply and demand, elasticity, controls and taxes; measuring income, cost of living, growth, saving, unemployment,
money); the cycle 4 geography programme (5e, 4e themes read from an academy copy of the programme; the BO n°31 of
30 July 2020 is the text of record).

| Item | Source | Chapter |
|---|---|---|
| scarcity, opportunity cost, incentives, trade-offs | principles ch. 1–2 | g7-01 (incentives: g7-05, g8-07) |
| interdependence, gains from trade | principles ch. 3; CORE 1 | g7-02, g7-03, g9-04 |
| supply and demand; elasticity; controls and taxes | principles ch. 4–6 | g7-05, g7-06, g9-01–03 |
| economic systems (market, planned) | OpenStax ch. 1.4 | g9-06 |
| models (thinking like an economist), positive vs normative | principles ch. 2; OpenStax 1.3 | frame used from g7; the notion is owned by g10 `economic-models` |
| measuring income (GDP), cost of living (CPI) | principles macro | g8-02, g8-03 |
| growth, productivity | principles macro; CORE 1–2 | g6-02, g8-01, g8-04 |
| saving, the financial system, interest | principles macro | g8-06 |
| unemployment, labour market | principles macro; CORE 3, 9 | g8-05 |
| money | principles macro | g7-04 |
| open economy, exchange rates | principles macro | g9-04, g9-05 |
| working hours and wellbeing | CORE 3 | g6-05, g7-01 |
| prosperity and inequality | CORE 1 | g6-02, g9-07 |
| 5e geography: population growth and development; wealth and poverty | cycle 4 | g6-02, g6-03, g6-04 |
| 5e geography: energy, water, food resources | cycle 4 | g6-06 (water: one paragraph, added) |
| 5e geography: risks and global change | cycle 4 | the Earth series owns climate; g6-06 names emissions only |
| 4e geography: urbanisation | cycle 4 | **gap**: one paragraph added to g6-04 (urban share, figdata) |
| 4e geography: transnational migration, tourism | cycle 4 | **gap**: one paragraph on remittances in g9-04; tourism not covered |
| 4e geography: spaces transformed by globalisation (seas, ports) | cycle 4 | g6-07, g9-04 (container ports) |
| 3e geography: France and the EU (single market, euro) | cycle 4 | **gap** in Book 1 beyond a `dated` paragraph in g9-05; the grades 10–12 volume holds European policy |
| production possibility frontier | principles ch. 2 | not in Book 1 (owned by g10) |
| consumer and producer surplus, deadweight loss | principles ch. 7–8 | not in Book 1 (owned by g10); g9-03/04 speak of who gains and loses with rectangles only |
| public goods, externalities | principles ch. 10–11 | not in Book 1 (g11); g6-06 shows emissions as facts |
| circular flow | principles ch. 2 | g8-02 (diagram) |
