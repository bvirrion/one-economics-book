# Book 2 (Grades 10–12) — chapter briefs (Phase A, 2026-11-20)

Written by the Book 2 writer under `sources/BATCH_BOOKS_1-5.md`. Provenance only; nothing here is printed.
Target: 40 chapters, ~420 pp (~10.5 pp each), 15 exercises (5★, 6★★, 4★★★) and one weekend problem (18–22 questions,
Parts I–IV, a named result) per chapter. No code is printed. No AI illustrations (grades 6–9 only). Photographs sparingly.

Conventions used below:
- **Owns**: the terms the chapter defines (`\emph{}\index{}` inside a `definition`); labels are in `DEFINITIONS.md`.
- **Recalls**: Book 1 notions (recalled in prose, never redefined) and sister-series notions (`recall` box naming the series).
- **Charts**: `econdata` loader and series, years. **[A]** approved data, available now (checked 2026-11-20);
  **[L]** a ledger table (a published table transcribed with a ledger row per value; mechanism awaits the sync, see
  "Questions for the sync" at the end); **[D]** needs data to approve (fallback named); **[I]** invented (Brenland/Kestria or a
  seeded chapter script).
- **Exercises**: kinds are **R** read a chart or table, **C** compute, **P** use a model to predict a direction and a size,
  **X** say what observation would contradict the model.
- Programme codes: **S**n seconde, **P**n première, **T**n terminale (economics items, listed in the coverage table at the end),
  **PR** the international principles sequence.

**Sync update (2026-11-20, rulings S1–S5, R1–R3).** Where this file and the rulings differ, the rulings win:
- correlation, natural experiment, unit-elastic, average/marginal tax rate, barrier to entry, natural monopoly, capital per
  worker, CPI, real GDP, disposable income, hyperinflation, import quota, patent, average annual growth rate are Book 1's:
  recalled, never defined here (see `DEFINITIONS.md`);
- g10-01 as written: the opening chart is the line fitted on 1870–1929 judged on 1930–2022 (US, Argentina), plus a chart of
  the misses of 21 countries; it recalls Book 1's steady growth and adds only the out-of-sample test. It owns *reverse
  causation* too. The problem fits 2000–2007 (not 2000–2014);
- g10-12 opening chart: BLS item indexes (e.g. new vehicles, college tuition, airline fares against all items), never the
  Eurostat computer index;
- g12-06 opening chart: no WGI; a Maddison pair or period different from Book 1 g9-06 (Germanys, Koreas, China 1978);
- every Pink Sheet [D] chart: a cited table (`figdata/lib/cited.py`), a BLS item index, EIA quantities or JST;
- Eurostat C1 and H.15 charts: `% PENDING-DATA: <dataset>` stubs until the main session announces the loaders.

---

## Grade 10 — Markets

### g10-01 Economic Models (`economic-models`)
- **Programme**: S1 (data and models; correlation and causation), PR "thinking like an economist", T methods (correlation and
  causality).
- **Sections**: 1 What a model is (assumptions, the variables it explains and the ones it takes as given, other things equal);
  2 The four-point frame (assumes, predicts, tested, breaks), worked on a constant-growth model; 3 Facts and values (positive and
  normative statements); 4 Correlation and cause (confounding factor, reverse causation, the randomised experiment, the natural
  experiment, first look).
- **Owns**: economic model, endogenous variable, exogenous variable, other things equal, positive statement, normative
  statement, correlation (in words, no coefficient), causal effect, confounding factor, randomised experiment, natural
  experiment.
- **Recalls**: Book 1 — growth rate and compounding (g8), the times-ten scale (g6), the three natural experiments (g9, prose
  only). Mathematics — geometric sequences in words (grade 11 is later: here only "the same percentage each year").
- **Models**: *Constant growth of income per person* — assumes a fixed yearly growth rate; predicts a straight line on a
  times-ten scale; tested on the United States 1870–2022 (a trend fitted on 1870–1929 lands close to 2022); breaks for
  Argentina after 1930 and for any country through a war or a collapse. (This is the worked example of the frame.)
- **Charts**: opening [A] `maddison(["USA","ARG"], since=1870)` gdppc, observed against the constant-growth line fitted on
  1870–1929 and extended to 2022, `omtimesten`, 2011 international dollars. Second [A] `wdi` AG.YLD.CREL.KG against
  AG.CON.FERT.ZS (2018–20 means, `countries_only=True`): a correlation that a field trial, not the scatter, turns into a cause
  (ledger: Duflo, Kremer and Robinson 2008 trial results are kept for g11-02, here only "trials exist").
- **Diagrams**: the frame as a four-box figure; a causal diagram (confounder pointing to both variables) with three nodes.
- **Photographs**: none.
- **Boxes**: `model` (constant growth); `measure`[How a trend line is drawn on a times-ten scale]; `record`[A forecast that held,
  and one that did not] (US against Argentina, from the opening chart).
- **Exercises**: ★ R opening chart ×2, sort statements into positive/normative, name exogenous/endogenous ×2; ★★ C a constant
  growth projection (powers of 1.02, grade-10 arithmetic) ×2, P what the model predicts for a doubling time, R the scatter, find
  a confounder ×2; ★★★ X two observations that would break the constant-growth model, design a randomised comparison,
  reverse causation case, a natural experiment's assumption.
- **Problem**: *Brenland's trend* — fit a constant-growth rate on Brenland's real GDP per person 2000–2014
  (`accounts.csv`: real_gdp/pop), project 2015–2025, compare. Named result: **the forecast error of the constant-growth model in
  2025, in per cent**. Parts: I the data; II the fitted rate; III the projection; IV what broke (the series' slow-down) and
  whether the model or a shock is to blame.
- **Ledger**: g10:trend-sources none beyond Maddison; one row for the Argentina 1930 break description (a published source
  on Argentina's relative decline), one row for the definition of a randomised trial if a citation is used.

### g10-02 The Production Possibility Frontier (`production-possibility-frontier`)
- **Programme**: PR interdependence; S3 recalled (factors).
- **Sections**: 1 Two goods, fixed resources (on, inside, outside); 2 Opportunity cost as the slope (straight frontier from one
  linear constraint, solved as a linear equation); 3 The bowed frontier (inputs differ in fitness; two regions or two kinds of
  land; increasing opportunity cost, proved on a two-region example); 4 Moving the frontier (more resources, better technology;
  a choice today moves the frontier tomorrow).
- **Owns**: production possibility frontier, productively efficient, law of increasing opportunity cost.
- **Recalls**: Book 1 — opportunity cost (g7), factors of production (g8). Mathematics — linear functions and slopes (g10).
- **Models**: *The production possibility frontier* — assumes fixed resources and technology, two goods; predicts that more of
  one good costs more and more of the other when inputs differ; tested: the war economies (US 1941–45: military output rose,
  consumption per person held about flat while unemployed resources were drawn in, so the economy was first inside its
  frontier); breaks: when resources are idle (the economy is inside), and over long periods (the frontier moves).
- **Charts**: opening [A] `jst(["USA"], 1929–1950)` rgdpbarro and rconsbarro (index, 1929 = 100) and expenditure/gdp,
  `omtime`: output rose ~80 % while consumption per person rose little and the government share jumped from 10 % to 41 %.
  (Replaces "civilian and military output": the approved data have GDP, consumption and government spending, not munitions.)
  Second [A] the same for the United Kingdom (`jst(["GBR"])`), where consumption fell: an economy already near its frontier.
- **Diagrams**: straight frontier with points A (on), B (inside), C (outside); bowed frontier built from two regions (the kink
  then the smooth limit); the frontier shifting out (biased shift for a new technology in one good).
- **Photographs**: one, a US wartime factory floor (aircraft assembly, US government work, public domain; Library of Congress
  or NARA via Commons), paired with the JST chart.
- **Boxes**: `model` (PPF); `record`[1941–45: output, consumption and the frontier] (JST numbers, dated facts in ledger).
- **Exercises**: ★ R opening chart ×2, place points on a frontier, opportunity cost from a straight frontier ×2; ★★ C a
  two-region bowed frontier (Brenland's two valleys), P effect of a new tractor, C slope between two points ×2, R the UK chart;
  ★★★ X observation that would show increasing cost is false, prove the combined frontier is bowed (two lines), a frontier
  with three regions, the choice between investment and consumption goods over two periods.
- **Problem**: *Brenland's harvest campaign* — two regions with different hours per unit of grain and cloth (a seeded table in
  the chapter's own script, not `ricardo.csv`, which is kept for g10-03), the combined frontier, the cost of a campaign to raise
  grain. Named result: **the opportunity cost of the last 1,000 tonnes of grain, in metres of cloth**.
- **Ledger**: US and UK wartime dates (entry into the war, demobilisation) as dated facts; one row on wartime rationing in the
  US (start date) if quoted.

### g10-03 Ricardo's Model of Comparative Advantage (`ricardo-model`)
- **Programme**: T6 (technological advantage), PR interdependence and gains from trade.
- **Sections**: 1 Two countries, two goods, labour only (unit labour requirements, autarky prices); 2 Who exports what (the
  pattern from relative requirements, proved); 3 Terms of trade and the gains (between the two autarky ratios; gains measured in
  goods and in hours; the consumption possibility frontier); 4 Wages follow productivity (relative wage bounds, why a low-wage
  country does not undersell everything); 5 Tested and where it breaks.
- **Owns**: unit labour requirement, autarky price, terms of trade, complete specialisation, consumption possibility frontier;
  *Ricardo's model* indexed in its `model` box.
- **Recalls**: Book 1 — comparative advantage with a table (g7), absolute advantage (g7), exports and imports (g9). This chapter
  — the PPF (g10-02).
- **Models**: *Ricardo's model* — assumes two goods, two countries, labour the only input, constant unit requirements, free
  movement of labour inside a country; predicts each country exports the good with the lower relative labour requirement, the
  terms of trade lie between the autarky ratios, both gain, the relative wage lies between the productivity ratios; tested:
  relative exports against relative productivity across industries (MacDougall's 1937 US/UK comparison and later replications,
  ledger), wages tracking output per worker across countries (chart); breaks: one factor only, nobody loses inside a country (the
  losers are taken up in g12-13), complete specialisation is rare, transport costs.
- **Charts**: opening [A] `pwt(since=2019, until=2019)` labour compensation per worker (labsh × rgdpo / emp) against output per
  worker (rgdpo / emp), `omincomex` both axes on a times-ten scale (log axes before grade 12 are the times-ten scale), 2021
  dollars: wages follow productivity. Source line says that both come from the same national accounts. Second [L] MacDougall
  (1951) industry table: US/UK output per worker ratio against US/UK export ratio, about 25 industries, 1937 (only if the
  paper's table is reachable at its primary host; otherwise dropped and cited in prose from a ledger row to a reachable
  replication).
- **Diagrams**: the two PPFs (Brenland, Kestria) from `ricardo.csv`; the consumption possibility frontier at the terms of trade;
  the world relative supply step curve with the terms of trade.
- **Photographs**: none.
- **Boxes**: `model` (Ricardo); `measure`[Output per worker across countries] (PPP, PWT).
- **Exercises**: ★ R `ricardo.csv` table, compute autarky prices, identify comparative advantage ×2, R opening chart; ★★ C gains
  in hours at given terms of trade ×2, P effect of a productivity gain in Kestria's grain on the pattern, C relative wage bounds,
  R second chart (or a printed table), C consumption possibilities; ★★★ X what export pattern would contradict the model, three
  goods ranked by relative requirement (chain of comparative advantage), why a country with the highest wages still exports,
  proof that the terms of trade lie between the autarky ratios.
- **Problem**: *Opening the Bren–Kest border* — from `ricardo.csv` (Brenland 4 h cloth, 2 h grain; Kestria 6 h cloth, 12 h grain)
  and the labour forces in `accounts.csv` scaled to hours: autarky, specialisation, trade at 1 cloth = 1 grain, gains. Named
  result: **each country's gain from trade, in hours of work saved per unit consumed**, and the relative wage.
- **Ledger**: MacDougall (1951) table or a replication (Golub and Hsieh 2000); Bernhofen and Brown (2004) Japan's opening as a
  test (prose); MacDougall's year and coverage.

### g10-04 Demand (`demand`)
- **Programme**: S9–S10, P2, PR market forces.
- **Sections**: 1 From one buyer to the market (individual demand tables and lines, horizontal summing, a kinked market line);
  2 The law of demand (with the exceptions honestly stated); 3 What moves the curve (income, tastes, prices of other goods,
  expectations, number of buyers; substitutes, complements, normal and inferior goods); 4 Moving along against moving the curve
  (other things equal, recalled from g10-01), with the oil chart as a case where both happened.
- **Owns**: market demand, law of demand, substitutes, complements, normal good, inferior good.
- **Recalls**: Book 1 — demand table and curve (g7), affine demand and shifts (g9). Mathematics — affine functions, piecewise
  definitions (g10).
- **Models**: *The law of demand* — assumes other things equal; predicts quantity falls when price rises; tested: fuel and
  tobacco price rises, the 1979 and 2008 oil price peaks (opening chart); breaks: rare Giffen behaviour among very poor
  households (Jensen and Miller 2008, rice in Hunan, ledger), snob and status goods not shown to reverse the law in market
  data (stated carefully as unproven).
- **Charts**: opening **[D]** oil consumption per person in rich countries against the real price of crude oil, 1970–2023:
  needs World Bank Commodity Price Data (crude price) and petroleum consumption from the EIA INTL file (already downloaded,
  needs re-derivation by the main session). Fallback [A]: `eurostat("prc_hicp_aind")` CP0722 fuels index relative to CP00,
  against nothing (price only) — weak; a better fallback is to leave the opening chart as a grey stub until the sync. Second [I]
  a Brenmoor bus-pass demand built from three buyer types (seeded script).
- **Diagrams**: horizontal summation of two linear demands (kink); movement along versus shift (two panels); substitutes and
  complements (two linked panels).
- **Photographs**: none.
- **Boxes**: `model` (law of demand); `record`[Rice in Hunan: when a price rise raised purchases] (Jensen and Miller 2008).
- **Exercises**: ★ R a demand table, classify substitutes/complements ×2, normal/inferior from income data (Brenland survey,
  food), R opening chart; ★★ C horizontal sum of two linear demands ×2, P direction of a shift for five events, C a shifted
  intercept, R distinguish along/shift in a two-period table, C demand of a kinked market line; ★★★ X what would contradict the
  law of demand in a market, why the opening chart is not a demand curve (income moved), the Giffen condition in words,
  aggregation with an inferior good.
- **Problem**: *Brenmoor's bus passes* — three groups of riders (students, workers, retirees) with linear demands; the market
  demand; a fare rise; a new tram line (a substitute) shifts demand. Named result: **the fall in passes sold after the fare
  rise, with and without the tram line**.
- **Ledger**: Jensen and Miller (2008, AER) key estimate; dates of the 1979 and 2008 oil-price peaks (from the chart data once
  approved).

### g10-05 Supply (`supply`)
- **Programme**: S10, P2, PR market forces.
- **Sections**: 1 The quantity offered at each price (a seller's lowest acceptable price; individual and market supply);
  2 What moves the curve (input prices, technology, number of sellers, expectations, weather); 3 Time to adjust: short-run and
  long-run supply (capacity, entry); 4 The shale-oil response as a case.
- **Owns**: market supply, law of supply, short-run supply, long-run supply.
- **Recalls**: Book 1 — supply table and curve (g7), costs (g7 firms). This book — market demand (g10-04).
- **Models**: *Supply with time to adjust* — assumes sellers expand capacity when prices stay high; predicts a small short-run
  response and a larger long-run one; tested: US crude oil production after the 2005–2014 price rise (chart), farm acreage
  responses (ledger); breaks: when capacity is fixed by nature (beachfront land) or by rule.
- **Charts**: opening **[D]** US crude oil production against the real price of oil, 1980–2024: needs crude production from
  the EIA INTL file (re-derivation, no download) and the World Bank commodity price (to approve). Fallback [A]
  `eia_energy("Total energy production", isos=["USA"])` alone, with the price story in prose from ledger rows. Second [A]
  `faostat_crops(item="Soya beans", element="Area harvested")`, Brazil 1990–2024 (checked: 1961–2024 available) as the long-run
  supply response.
- **Diagrams**: individual to market supply (sum); short-run and long-run supply through one point; a supply shift from a
  cost fall.
- **Photographs**: one, a drilling rig or a pumpjack in a named field (Commons, CC BY or PD, licence read at writing).
- **Boxes**: `model` (supply with time to adjust); `measure`[What a supply curve is not: the cost of the marginal seller].
- **Exercises**: ★ R a supply table, list shifters ×2, R opening chart, C market supply of two sellers; ★★ C intercept change from
  a cost rise ×2, P short- and long-run response, R soybean area chart, C a kinked market supply, P an import ban on an input;
  ★★★ X what would contradict the time-to-adjust model, why production fell with a lag in 2015–16, supply with a fixed
  capacity, the elasticity of long-run supply in words (taken up in g10-07).
- **Problem**: *Kestria's dairy farms* — 40 small and 10 large farms with linear supplies; market supply; a feed-price rise;
  entry of new farms over three years. Named result: **the long-run quantity response to a lasting price rise, against the
  first-year response**.
- **Ledger**: US shale dates (horizontal drilling at scale), one farm-acreage response study (e.g. a published estimate of
  acreage elasticity).

### g10-06 Market Equilibrium (`market-equilibrium`)
- **Programme**: S11, P2–P3, PR market forces.
- **Sections**: 1 Equilibrium as the solution of a linear system (proved: unique when slopes differ in sign); 2 Excess demand and
  excess supply, and how the price adjusts (a step rule as a story, no dynamics); 3 Comparative statics: one shift, two shifts at
  once (the four cases, the ambiguous one proved); 4 Linked markets (substitutes, inputs); 5 Tested and where it breaks.
- **Owns**: excess demand, excess supply, comparative statics, price taker.
- **Recalls**: Book 1 — equilibrium in a table and on a graph, shortage and surplus (g7), affine equations (g9). Mathematics —
  linear systems (g10 `lines-and-systems`).
- **Models**: *The competitive market (linear)* — assumes many price-taking buyers and sellers of one good, prices free to move;
  predicts the equilibrium and the sign of each shift; tested: laboratory double auctions converge on the predicted price
  (Smith 1962, ledger), the maize market after the US ethanol mandate (chart); breaks: few traders, prices fixed by rule or slow
  to move, goods of hidden quality (g11-08).
- **Charts**: opening **[D]** world maize price (World Bank commodity prices, deflated by `bls_cpi`) and world maize production
  (`faostat_crops(item="Maize (corn)", element="Production")`, World), 2000–2015: price and quantity both rose — a demand shift.
  Fallback: the laboratory market (Smith 1962) as a ledger table if the paper's summary table is reachable [L]; else stub.
  Second [A]: `faostat_crops` maize production in the United States and the world, to separate the two shifts (US output up,
  world supply also up).
- **Diagrams**: equilibrium with excess demand and supply marked; the four two-shift cases in a 2×2 grid; linked markets
  (a frost shifts apple supply, pears' demand moves).
- **Photographs**: none.
- **Boxes**: `model` (competitive market); `record`[The ethanol mandate and the price of maize] (dated law, ledger);
  `measure`[What a laboratory market is] (Smith's design).
- **Exercises**: ★ solve a 2×2 system ×2, R excess demand at a price, R opening chart, identify the shift; ★★ C equilibrium after
  a tax-free shift ×2, P two shifts with sizes given, C linked markets, R second chart, C equilibrium with three sellers' lines;
  ★★★ X observations contradicting a pure demand shift, prove the ambiguous case, a market with a price fixed by rule, slopes of
  equal sign (no equilibrium).
- **Problem**: *A frost in Kestria's orchards* — apples and pears, substitutes, linear demand and supply in each, a frost cuts
  apple supply. Named result: **the new equilibrium prices and quantities in both markets** (a 4-unknown linear system).
- **Ledger**: Smith (1962, JPE) convergence summary; US Renewable Fuel Standard dates (2005, 2007 laws); maize used for ethanol
  share (USDA page).

### g10-07 Elasticities (`elasticities`)
- **Programme**: PR elasticity; S10.
- **Sections**: 1 Price elasticity of demand between two points (arc, midpoint) and at a point on a line (slope × p/q);
  2 How it changes along a straight demand line (proved: |ε| = 1 at the midpoint); 3 Elasticity and revenue (proved for a line);
  4 Income and cross-price elasticities; 5 Elasticity of supply; what makes demand elastic (substitutes, share of budget, time).
- **Owns**: point elasticity, arc elasticity, unit-elastic demand, income elasticity of demand, cross-price elasticity, price
  elasticity of supply, perfectly elastic, perfectly inelastic.
- **Recalls**: Book 1 — elasticity as a ratio of percentages, elastic and inelastic, revenue (g9), food share of spending (g6).
  This book — substitutes, normal and inferior goods (g10-04).
- **Models**: none new (a measure, not a model).
- **Charts**: opening [A] `wdi("SH.XPD.CHEX.PP.CD")` against `wdi("NY.GDP.PCAP.PP.CD")`, 2019, `countries_only=True`
  (186 countries), both axes times-ten scale: a tenfold income goes with about a thirteenfold health spending (fitted slope
  1.12 checked; the prose reads it as "more than proportional", income elasticity above one). (Replaces "cars per 1,000 people":
  no vehicle series is approved.) Second [I] Brenland food spending against disposable income (`households.csv`): income
  elasticity below one.
- **Diagrams**: elasticity along a straight demand line (elastic, unit, inelastic segments) with the revenue curve beneath;
  perfectly elastic and perfectly inelastic lines.
- **Photographs**: none.
- **Boxes**: `measure`[How an elasticity is estimated: comparing like with like]; `debate` none.
- **Exercises**: ★ arc elasticity ×2, read opening chart, sign of cross elasticity, classify; ★★ point elasticity on a line ×2,
  revenue-maximising price, C income elasticity from the Brenland table, P revenue after a price change, R published estimates
  table (ledger: short- and long-run gasoline elasticities); ★★★ X what would contradict |ε|<1 for a good, prove the midpoint
  result, constant-elasticity curve in words, why long-run elasticities are larger.
- **Problem**: *Brenmoor's toll bridge* — linear demand for crossings estimated from two years of data; elasticity at the current
  toll; revenue-maximising toll; a new ferry raises elasticity. Named result: **the revenue-maximising toll and the revenue it
  brings, before and after the ferry**.
- **Ledger**: published short- and long-run price elasticities of gasoline and of cigarettes (one survey each); the health
  spending caveat (cross-country, not a demand curve).

### g10-08 Surplus and Efficiency (`surplus-and-efficiency`)
- **Programme**: P5–P6, PR consumers, producers and efficiency.
- **Sections**: 1 Willingness to pay and consumer surplus (a staircase of buyers, then the area under a line); 2 Cost and producer
  surplus; 3 Total surplus and the competitive equilibrium (proposition: with the model's assumptions, the equilibrium quantity
  maximises total surplus; proof by the staircase argument); 4 What the result does not cover (who gets the surplus; people outside
  the market; the measure uses money, so it weighs the rich more).
- **Owns**: willingness to pay, consumer surplus, producer surplus, total surplus, allocative efficiency.
- **Recalls**: Book 1 — demand and supply curves (g7). This book — market equilibrium (g10-06).
- **Models**: *Efficiency of the competitive market* — assumes price-taking buyers and sellers, no effects on outsiders, full
  information; predicts total surplus is largest at the equilibrium quantity; tested: laboratory markets reach 95–100 % of
  the maximum surplus (Smith; Gode and Sunder 1993, ledger); breaks: externalities (g11-06), market power (g11-04), hidden
  information (g11-08).
- **Charts**: opening [L] median willingness to accept to give up a free digital good for a year (search engines, email, maps,
  video, e-commerce, social media, music, messaging), Brynjolfsson, Collis and Eggers (2019, PNAS, open access) table: consumer
  surplus that GDP does not count. (Replaces "the WTP of 100 buyers, ranked", for which no real dataset is approved; the ranked
  staircase becomes the first diagram [I].) Second [I] a ranked staircase of 100 Brenmoor buyers (seeded script) with the price.
- **Diagrams**: consumer surplus as a staircase then a triangle; producer surplus; total surplus at and away from equilibrium
  (the lost triangle, named only here, defined in g10-09).
- **Photographs**: none.
- **Boxes**: `model` (efficiency); `measure`[Valuing a free good: asking people what they would accept] (the PNAS method).
- **Exercises**: ★ surplus of one buyer ×2, R opening chart, CS of a linear demand, PS of a linear supply; ★★ total surplus at
  equilibrium ×2, surplus at a quantity below equilibrium, P effect of a cost fall on CS and PS, R the staircase, C surplus split
  after a demand shift; ★★★ X evidence that would show a market misses surplus, prove the maximisation for linear curves (with
  areas of triangles and trapezoids only: grade 10 has no derivative), why money-weighted surplus is not welfare, a market with
  an outsider harmed.
- **Problem**: *Brenmoor's Saturday market* — 20 sellers and 30 buyers with listed costs and values (seeded table); the
  equilibrium price band; surplus; a cap on the number of stalls. Named result: **the surplus lost to the stall cap, in dalens
  and as a share of the maximum**.
- **Ledger**: Brynjolfsson et al. (2019) table values; Gode and Sunder (1993) efficiency figures; Smith (1962) efficiency.

### g10-09 What Prices Do (`what-prices-do`)
- **Programme**: P1 (the market as an institution), PR price controls; "what prices do" (user, 2026-11-19), taught as a
  positive result.
- **Sections**: 1 Three jobs of a price (inform, give a reason to act, ration); how a price change spreads knowledge no one holds
  whole; 2 Arbitrage and the single price (across places; transport cost as the band); 3 Storage and speculation move goods
  through time (a two-season model); 4 Price ceilings and floors with surplus (deadweight loss defined; queues, quality, side
  payments, black markets); 5 The record of price controls; 6 The market as an institution (property, contracts, a place to meet).
- **Owns**: arbitrage, law of one price, speculation, deadweight loss, non-price rationing, black market.
- **Recalls**: Book 1 — the price as a signal, shortage and surplus (g7), price ceiling and price floor (g9). This book — surplus
  (g10-08).
- **Models**: *A price ceiling in a competitive market* — assumes the competitive model; predicts excess demand, a deadweight
  loss, non-price rationing; tested: US gasoline queues 1973–74 and 1979, rent control in San Francisco (Diamond, McQuade and
  Qian 2019: landlords converted and withdrew units, ledger); breaks: a buyer with market power (monopsony, g11-10), when
  quantity is fixed in the short run (rent control on existing units costs little at first). *Arbitrage* — assumes traders can
  move goods at a cost; predicts prices in two places differ by at most the transport cost; tested: Kerala fish markets after
  mobile phones (Jensen 2007, ledger).
- **Charts**: opening **[D]** Thai and Vietnamese rice export prices, monthly 2000–2024 (World Bank commodity prices): two
  neighbouring markets, one price up to a band; fallback [L] Jensen (2007) coefficient of variation of fish prices before and
  after phones, by region (a table from the paper if reachable). Second [A] `eurostat("prc_hicp_aind")` CP0722 fuels index in
  several countries (prices moving together through arbitrage), optional.
- **Diagrams**: binding ceiling with DWL and the shortage; binding floor with excess supply; two-place arbitrage with the
  transport band; two-season storage (prices equalised up to storage cost).
- **Photographs**: one, a historic grain exchange or commodity trading floor (public domain, licence read at writing).
- **Boxes**: `model` ×2 (ceiling, arbitrage); `record`[Petrol queues, 1973–74 and 1979] (dated, ledger); `record`[Rent control
  in San Francisco] (Diamond et al. 2019).
- **Exercises**: ★ name the three jobs in a story, R opening chart, compute a shortage ×2, DWL of a ceiling; ★★ C DWL and
  transfer under a ceiling ×2, P a floor's effects, C arbitrage band, P storage between seasons, C a black-market price; ★★★ X
  what would contradict the arbitrage model, a ceiling that does not bind, a rationing scheme and its cost in queue time, a floor
  with government purchases (cost to taxpayers).
- **Problem**: *Rent control in Brenmoor* — linear demand and supply of flats; a ceiling; queues; side payments; conversions over
  five years (supply becomes more elastic). Named result: **the deadweight loss and the black-market rent, in the first year and
  after five years**.
- **Ledger**: Jensen (2007, QJE) key numbers; Diamond, McQuade and Qian (2019, AER) estimates; US price-control dates (1971,
  1973–74, 1979, 1981 decontrol).

### g10-10 Tax Incidence and Deadweight Loss (`tax-incidence`)
- **Programme**: S12, P3 (a per-unit tax with numbers), PR costs of taxation, T28 (incentive effects) in part.
- **Sections**: 1 The wedge (buyer's price, seller's price; per-unit and ad valorem); 2 The burden does not depend on who hands
  over the tax (proved with linear curves); 3 The less elastic side bears more (proved: shares in terms of slopes);
  4 Deadweight loss and why it grows with the square of the rate (proved for lines); revenue against the rate (a parabola for
  lines, the peak); 5 A subsidy.
- **Owns**: tax wedge, statutory incidence, economic incidence, pass-through rate, ad valorem tax, Laffer curve (as the label of
  revenue against rate).
- **Recalls**: Book 1 — taxes (g8), tax per unit, subsidy (g9). This book — elasticities (g10-07), surplus (g10-08), deadweight
  loss (g10-09).
- **Models**: *Tax incidence in a competitive market* — assumes the competitive model; predicts a tax raises the buyer's price by
  a share set by elasticities, whichever side pays; tested: the German VAT cut of July–December 2020 (chart; published
  pass-through estimates, ledger), fuel-tax pass-through; breaks: market power, taxes buyers do not notice (salience: Chetty,
  Looney and Kroft 2009, ledger).
- **Charts**: opening [A] `eurostat("prc_hicp_manr")` Germany CP00 and CP01, monthly 2019-01 to 2021-12, with the cut window
  shaded: annual inflation fell about 0.8 points in July 2020 and jumped in January 2021 (checked). Second [A] the same for CP0722
  fuels, or Brenland's fuel tax table [I] for the revenue curve.
- **Diagrams**: the wedge on buyers and on sellers (same outcome, two panels); incidence with steep demand versus steep supply;
  DWL triangle and revenue rectangle; revenue against the rate (parabola).
- **Photographs**: none.
- **Boxes**: `model` (incidence, the CONTRIBUTING example); `record`[The German VAT cut of 2020]; `measure`[How pass-through is
  measured].
- **Exercises**: ★ wedge prices ×2, R opening chart, share borne by buyers, revenue; ★★ DWL ×2, P incidence with a steeper
  demand, C ad valorem tax, C a subsidy's cost and gain, P doubling the rate (DWL ×4); ★★★ X evidence contradicting "who pays
  does not matter", the revenue-maximising rate, a tax with perfectly inelastic supply (land), salience.
- **Problem**: *Brenland's fuel tax* — linear demand and supply for fuel (dalens per litre); a tax of 0.20, then 0.40; incidence;
  revenue; DWL; the revenue curve. Named result: **the revenue-maximising tax per litre and the deadweight loss at that rate**.
- **Ledger**: German VAT rates and dates (19→16 %, 7→5 %, 1 July–31 December 2020; the law); published pass-through estimates
  (Fuest, Neumeier and Stöhlker 2021, or the Bundesbank's); Chetty, Looney and Kroft (2009, AER).

### g10-11 National Accounts (`national-accounts`)
- **Programme**: S2 (market and non-market production), S4–S5, S7, PR measuring a nation's income.
- **Sections**: 1 Three ways to the same total (production, income, expenditure; the identity proved on a three-firm economy);
  2 Consumption, investment, government purchases, net exports; 3 GDP and national income (GNI, depreciation, net product);
  4 Nominal and real GDP and the deflator; 5 Comparisons across countries (purchasing-power GDP, recalled and extended); the
  limits (non-market production, home work, the informal economy, quality, distribution).
- **Owns**: final expenditure, investment (as an expenditure component), government purchases, net exports, gross national
  income, depreciation (consumption of fixed capital), non-market production, nominal GDP, real GDP, GDP deflator.
- **Recalls**: Book 1 — GDP, value added (g8), real and nominal values (g8), purchasing-power conversion (g9).
- **Models**: none (accounting identities; a `measure` chapter).
- **Charts**: opening [A] `wdi` NE.CON.PRVT.ZS, NE.GDI.TOTL.ZS, NE.CON.GOVT.ZS, NE.EXP.GNFS.ZS, NE.IMP.GNFS.ZS for five
  countries (USA, CHN, DEU, IND, NGA), latest common year, stacked bars (imports negative). Second [I] Brenland's
  `accounts.csv` 2000–2025: nominal and real GDP and the deflator.
- **Diagrams**: the circular flow (households, firms, government, rest of the world); a three-firm value-added chain (wheat,
  flour, bread) with the three totals.
- **Photographs**: none.
- **Boxes**: `measure`[How GDP is measured, three ways]; `measure`[Non-market production: valued at its cost]; `dated{2026}` none.
- **Exercises**: ★ R opening chart ×2, compute GDP by expenditure, value added in a chain, C GNI from GDP; ★★ real GDP and the
  deflator from Brenland ×2, real growth rate, C net product, P what a rise in home cooking does to GDP, R a two-way table of
  sectors; ★★★ X a case where the three totals would differ (and what that means: a statistical discrepancy), chain the
  deflator over five years, GDP with a non-market sector, why imports are subtracted.
- **Problem**: *Brenland's accounts for 2025* — from `accounts.csv`: check the identity, compute nominal and real growth, the
  deflator's inflation, the shares, the per-person values. Named result: **real growth of GDP per person in 2025 and how much of
  nominal growth was prices**.
- **Ledger**: the international standard's name (System of National Accounts 2008, UN page) if cited; none else.

### g10-12 Price Indices and the Cost of Living (`price-indices`)
- **Programme**: S methods (simple index, composite index, weighted mean, nominal and real), P methods (nominal and real
  interest rates), PR cost of living.
- **Sections**: 1 A fixed basket (Laspeyres) and a current basket (Paasche) (proposition: Laspeyres ≥ Paasche under
  substitution, proved on two goods); 2 Biases: substitution, new goods, quality change (quality adjustment, hedonic idea);
  3 The consumer price index and the GDP deflator compared; 4 Indexing a wage, a pension, a contract; 5 The real interest rate
  (exact and approximate).
- **Owns**: Laspeyres index, Paasche index, consumer price index, substitution bias, quality adjustment, chain-linked index,
  indexation, real interest rate.
- **Recalls**: Book 1 — price index with base 100, inflation rate, real and nominal (g8), interest (g8). This book — the GDP
  deflator (g10-11). Mathematics — weighted means (g8).
- **Models**: none.
- **Charts**: opening [A] `eurostat("prc_hicp_aind")` unit INX_A_AVG, CP09131 personal computers for France (the only
  country with it from 1996) and CP0913 information processing equipment for the euro area, against CP00 all items, 1996–2024,
  log y axis (grade 10: times-ten scale) (checked: FR computers 1966 in 1996 to 72 in 2024, all items 75 to 123). (Replaces the US constant-quality computer series: BLS components are not
  derived.) Second [I] Brenland's basket (`basket.csv`): the Laspeyres CPI against a Paasche index built in the script.
- **Diagrams**: two-good substitution diagram (budget lines for the two baskets) kept in words and a table — no indifference
  curves (Year 1 owns the consumer); a bar figure of a basket's weights.
- **Photographs**: none.
- **Boxes**: `measure`[How a consumer price index is built] (basket, weights, collection, quality adjustment);
  `record`[The measured bias of a price index] (a published bias estimate, e.g. the 1996 US review's 1.1 points, ledger).
- **Exercises**: ★ simple index ×2, R opening chart, weighted index from a table, a real wage; ★★ Laspeyres and Paasche ×2,
  chain three years, P what substitution does to the index, C real interest rate exact and approximate, C index a rent clause;
  ★★★ X a case where Laspeyres < Paasche (what it would mean), quality adjustment of a phone, new-goods bias, deflating with the
  wrong index.
- **Problem**: *Brenland's basket, 2015–2025* — from `basket.csv`: rebuild the CPI, compute a Paasche index with current
  quantities from a seeded consumption table, the substitution gap, a wage indexed on each. Named result: **the substitution
  bias of the Brenland CPI over ten years, in index points and per year**.
- **Ledger**: the 1996 US advisory commission bias estimate (primary report page); Eurostat HICP methodology page (quality
  adjustment) for the `measure` box.

---

## Grade 11 — Firms, market failure, government failure, labour

### g11-01 Marginal Reasoning (`marginal-reasoning`)
- **Programme**: P4 (in part), PR thinking at the margin; T methods (rates of change).
- **Sections**: 1 A marginal quantity as a derivative (recall box: the derivative, mathematics grade 11); the marginal value of
  a discrete step against the derivative; 2 The rule marginal benefit equals marginal cost (proposition, proved from a
  differentiable net benefit); 3 Average and marginal (proposition: the average rises when the marginal is above it, proved);
  marginal and average tax rates as a case; 4 Sunk costs once more (only marginal quantities enter).
- **Owns**: marginal quantity, marginal benefit, marginal cost, marginal revenue, net benefit, marginal tax rate, average tax
  rate.
- **Recalls**: Book 1 — opportunity cost, a cost already paid does not count (g7), revenue and costs (g7). Mathematics —
  derivative, variations, extrema (g11 `differentiation`, `functions-variations`).
- **Models**: *The optimising decision-maker* — assumes a person or firm chooses to maximise net benefit; predicts responses to
  marginal changes and none to sunk costs; tested: firms' output responds to marginal cost changes (fuel and electricity, ledger);
  breaks: the sunk-cost effect is measured in some experiments (Arkes and Blumer 1985, ledger), and decisions in steps are not
  smooth.
- **Charts**: opening [A] `wdi("SP.DYN.LE00.IN")` against `wdi("SH.XPD.CHEX.PP.CD")`, 2019, `countries_only=True`, x on a
  times-ten scale: the gain in life expectancy from the next 100 dollars falls as spending rises — a falling marginal benefit.
  (Replaces the electricity merit order: no plant-level cost data are approved.) Second [I] Brenland's `TAX_BANDS` schedule: the
  marginal rate (steps) and the average rate (smooth) against income.
- **Diagrams**: total benefit and total cost curves with the gap largest where slopes are equal; marginal benefit and marginal
  cost lines crossing; average and marginal cost (U and its marginal through the bottom).
- **Photographs**: none.
- **Boxes**: `model` (optimiser); `measure`[Marginal and average tax rates].
- **Exercises**: ★ marginal cost from a table ×2, derivative of a cost function, R opening chart, a sunk-cost decision; ★★
  optimum of a net-benefit function ×2, marginal and average tax from Brenland's bands ×2, P effect of a cost rise on the chosen
  quantity, C average rising/falling; ★★★ X evidence of a sunk-cost effect and what it breaks, prove the average–marginal
  proposition, a decision in whole units (the derivative misleads), the marginal rate of a means-tested benefit.
- **Problem**: *Brenmoor's bakery* — revenue and cost of loaves as functions (a quadratic cost); marginal revenue and cost;
  the profit-maximising output; a rise in flour prices; the oven bought last year is sunk. Named result: **the
  profit-maximising number of loaves and the profit, before and after the flour price rise**.
- **Ledger**: Arkes and Blumer (1985) result; one published estimate of output response to marginal cost.

### g11-02 Production and Costs (`production-and-costs`)
- **Programme**: P4 (rising marginal cost), PR costs of production.
- **Sections**: 1 The production function with one variable input (short run); 2 Diminishing marginal product (proposition and
  the fertiliser evidence); 3 Total, average and marginal cost (fixed and variable recalled); proposition: marginal cost cuts
  average cost at its lowest point (proved with the derivative); 4 The long run (all inputs vary; economies and diseconomies of
  scale; minimum efficient scale); learning: unit cost falls with cumulative output.
- **Owns**: production function, fixed input, variable input, short run, long run, marginal product, diminishing marginal
  product, average total cost, average variable cost, average fixed cost, economies of scale, diseconomies of scale, minimum
  efficient scale, learning curve.
- **Recalls**: Book 1 — revenue, fixed and variable cost, profit (g7), factors and productivity (g8). This book — marginal cost
  (g11-01). Mathematics — derivative of a quotient (g11).
- **Models**: *Diminishing marginal product* — assumes one input varies, the others fixed; predicts each extra unit adds less;
  tested: fertiliser trials in Kenya (Duflo, Kremer and Robinson 2008: the return at half the recommended dose exceeds the return
  at the full dose, ledger); breaks: at very low input levels returns can rise, and over time (learning, Liberty ships).
- **Charts**: opening [A] `wdi("AG.YLD.CREL.KG")` against `wdi("AG.CON.FERT.ZS")`, 2018–20 means (179 countries, checked),
  x on a times-ten scale: yields rise with fertiliser, by less and less (with the confounders said). Second [L] Liberty ships:
  labour hours per ship by month of delivery, 1941–44 (Searle 1945, *Monthly Labor Review*, BLS, public domain): the learning
  curve.
- **Diagrams**: total product and marginal product; the cost family (ATC, AVC, AFC, MC) with MC through the minima; long-run
  average cost as the envelope of three short-run curves; economies and diseconomies of scale marked.
- **Photographs**: one, the launch of a Liberty ship (US government photograph, public domain), paired with the learning chart.
- **Boxes**: `model` (diminishing marginal product); `record`[Liberty ships, 1941–44].
- **Exercises**: ★ marginal product from a table ×2, average cost ×2, R opening chart; ★★ MC and ATC from a cost function ×2,
  minimum of ATC (derivative), P a rise in the fixed cost (ATC moves, MC does not), R the Liberty chart, C learning rate per
  doubling; ★★★ X what would contradict diminishing returns in the fertiliser data, prove MC = ATC at the minimum, long-run cost
  from three plant sizes, scale versus learning.
- **Problem**: *Kestria's textile mill* — a cost function C(q) = F + aq + bq² (kests); the cost family; efficient scale; three
  plant sizes for the long run. Named result: **the minimum efficient scale and the minimum average cost**.
- **Ledger**: Duflo, Kremer and Robinson (2008, AER) returns; Searle (1945) table; Thornton and Thompson (2001) if cited.

### g11-03 Perfect Competition (`perfect-competition`)
- **Programme**: P1, P4 (the supply curve from profit maximisation; P = MC), PR firms in competitive markets.
- **Sections**: 1 The price-taking firm (marginal revenue equals the price); 2 Output where price equals marginal cost (proved);
  3 When to shut down (the price below minimum AVC; proved); the firm's supply curve and the industry's; 4 Entry, exit and zero
  economic profit (long-run equilibrium; price at minimum ATC); economic and accounting profit; 5 Tested and where it breaks.
- **Owns**: perfect competition, shutdown price, firm supply curve, industry supply curve, economic profit, accounting profit,
  free entry, long-run competitive equilibrium.
- **Recalls**: Book 1 — profit draws firms in (g7), competition in words (g8). This book — price taker (g10-06), the cost family
  (g11-02), marginal revenue (g11-01).
- **Models**: *Perfect competition* — assumes many price-taking firms, identical product, free entry and exit; predicts P = MC,
  zero economic profit in the long run, entry after a demand rise; tested: soybean area in Brazil after the 2000s price rise and the
  price falling back (chart); laboratory markets; breaks: few sellers, entry barriers, product differences.
- **Charts**: opening **[D]** real world soybean price (World Bank commodity prices, deflated by `bls_cpi`) and Brazil's soybean
  area harvested (`faostat_crops(item="Soya beans", element="Area harvested")`), 1995–2023: entry after a price rise. Fallback
  [A] the area series alone, with the price in prose from ledger rows. Second [I] the firm and the industry side by side for
  Brenland's egg farms.
- **Diagrams**: firm and industry panels (short run); the shutdown point; long-run adjustment after a demand rise (three
  panels).
- **Photographs**: none.
- **Boxes**: `model` (perfect competition); `measure`[Economic and accounting profit].
- **Exercises**: ★ profit at a price ×2, shutdown decision, R opening chart, accounting versus economic profit; ★★ supply curve
  from a cost function ×2, industry supply of n firms, P entry after a demand rise (number of firms), C long-run price, R firm
  panel; ★★★ X what would contradict zero long-run profit, a constant-cost against an increasing-cost industry, a fixed licence
  number, a sunk entry cost.
- **Problem**: *Brenland's egg industry* — identical farms with a quadratic cost; demand linear; short-run equilibrium with 40
  farms; demand rises; entry. Named result: **the long-run number of farms and the long-run price of a dozen eggs**.
- **Ledger**: Brazil soybean expansion dates (published USDA or FAO page), China's soybean import growth (a published figure).

### g11-04 Monopoly (`monopoly`)
- **Programme**: P7–P9, P11 and T22 (competition policy: abuse of dominance, mergers), PR monopoly.
- **Sections**: 1 Marginal revenue below price (proved for a line: twice the slope); 2 The monopoly output and price (MR = MC);
  the markup and the elasticity (Lerner, proved); 3 Deadweight loss of monopoly; 4 Where market power comes from (patents,
  licences, networks, scale: natural monopoly); 5 Different prices for different buyers (first look); 6 What erodes a monopoly
  (entry, substitutes, new products) and competition law (mergers, abuse of dominance), each with its evidence and its own
  risk of error.
- **Owns**: market power, barrier to entry, monopoly output, markup, Lerner index, natural monopoly, price discrimination,
  contestable market, abuse of a dominant position.
- **Recalls**: Book 1 — monopoly in words, patents and licences (g8). This book — marginal revenue (g11-01), DWL (g10-09),
  elasticities (g10-07). Mathematics — quadratic functions (g11).
- **Models**: *Monopoly* — assumes one seller facing the market demand, no entry; predicts lower output, higher price, a markup
  set by elasticity; tested: drug prices fall as generic makers enter after a patent expires (FDA 2019 table, opening chart);
  breaks: threat of entry (contestable markets), regulation, a durable good buyers can wait for.
- **Charts**: opening [L] generic price relative to the brand price by number of generic producers (FDA 2019, *Generic
  Competition and Drug Prices: New Evidence*, US government, public domain). (Replaces "one medicine before and after": a
  published table of many drugs is a stronger test.) Second [I] the monopoly diagram's numbers as a revenue/profit parabola.
- **Diagrams**: monopoly with MR, MC, price, DWL; natural monopoly with falling ATC (regulated price at AC); two-market price
  discrimination.
- **Photographs**: none.
- **Boxes**: `model` (monopoly); `record`[Generic entry and the price of a medicine]; `measure`[How a market's concentration is
  measured] (concentration ratio, Herfindahl index — told).
- **Exercises**: ★ MR from a demand line ×2, monopoly price and quantity, R opening chart, Lerner index; ★★ DWL ×2, P effect of
  a cost rise on price (pass-through half for a line), C price discrimination in two markets, P a natural monopoly priced at MC
  (loss), R the FDA table, — (6); ★★★ X evidence contradicting the monopoly model in a patented market, a contestable market,
  why a monopoly never sets price on the inelastic part (proved), a merger's price effect versus cost savings.
- **Problem**: *Brenland's only ferry* — linear demand for crossings, constant marginal cost; monopoly pricing; DWL; a
  regulated price; two-part tariff; a bridge as a new entrant. Named result: **the deadweight loss of the ferry monopoly and the
  share recovered by the regulated price**.
- **Ledger**: FDA (2019) table; a published merger-retrospective estimate (e.g. a hospital or airline study); EU and US
  competition-law articles (Article 102 TFEU; Sherman Act section 2) as LAW rows.

### g11-05 Oligopoly and a First Look at Games (`oligopoly-and-games`)
- **Programme**: P7, P10, P11, T22 (cartels, leniency), PR oligopoly and monopolistic competition.
- **Sections**: 1 A few sellers; many sellers of differentiated products (monopolistic competition, in words and one
  diagram); 2 A game: players, strategies, payoffs; dominant strategy; Nash equilibrium (defined on payoff tables); 3 The
  prisoner's dilemma and why cartels are unstable (a cartel's table derived from quantities); 4 Repeated play (first look:
  punishment strategies in words); 5 Cartels and the law (fines, leniency programmes, the evidence on overcharges).
- **Owns**: oligopoly, monopolistic competition, product differentiation, game, strategy, payoff, dominant strategy, Nash
  equilibrium, prisoner's dilemma, cartel, collusion, repeated game, leniency programme.
- **Recalls**: Book 1 — competition (g8). This book — monopoly output (g11-04), economic profit (g11-03).
- **Models**: *The cartel as a prisoner's dilemma* — assumes each member chooses output to maximise its own profit, with no
  binding contract; predicts each member produces above its quota, so a cartel breaks down unless it can punish; tested: OPEC
  in 1981–86 (members above quota while Saudi Arabia cut, then the 1986 price collapse; chart and ledger); breaks: when play is
  repeated and cheating is seen quickly, cartels last (the lysine and vitamins cartels, ledger), and laboratory subjects
  cooperate more than the one-shot model predicts.
- **Charts**: opening **[D]** crude oil production of Saudi Arabia and of the other OPEC members, 1979–1990 (EIA INTL file,
  re-derivation; no download), with the real oil price (World Bank, to approve). Fallback [L] OPEC quotas and production from a
  published table (e.g. a paper's table), or stub. Second [L] median cartel overcharge from a published survey (Connor's
  meta-analysis, or the European Commission's figures), as bars by period.
- **Diagrams**: payoff tables (2×2) for the cartel and for a pricing game; monopolistic competition long run (demand tangent to
  ATC); a game with two Nash equilibria (coordination).
- **Photographs**: none.
- **Boxes**: `model` (cartel); `record`[OPEC, 1981–86]; `dated{2026}`[cartel fines: one recent EU decision, ledger].
- **Exercises**: ★ dominant strategy ×2, Nash equilibrium in a table ×2, R opening chart; ★★ build a cartel table from quantities
  ×2, cheating gain, P effect of a leniency programme on a two-firm game, R overcharge chart, find all Nash equilibria; ★★★ X
  evidence contradicting the one-shot model, a repeated game with a trigger strategy (when is cooperation stable: a geometric sum
  is grade 11 sequences — admitted sum), monopolistic competition's zero profit, a coordination game.
- **Problem**: *Two quarries in Kestria* — two firms, linear demand for gravel, identical costs; the cartel quantity; each firm's
  best deviation (computed with derivatives); the payoff table; repeated play with a ten-year horizon. Named result: **the gain
  from cheating on the cartel, and the punishment that removes it**.
- **Ledger**: OPEC quota decisions 1982–86 (dated); Connor survey; EU leniency notice; one cartel case (lysine) with dates.

### g11-06 Externalities (`externalities`)
- **Programme**: P12, P15, T5, T31 (instruments: regulation, emissions trading, taxation, green-innovation subsidy; their
  limits; failures in implementation), S8, PR externalities.
- **Sections**: 1 Private and social cost and benefit (negative and positive externalities; too much or too little; DWL);
  2 Bargaining when rights are clear and bargaining is cheap (the Coase result, with transaction costs); 3 A corrective tax;
  tradable permits; rules and standards; subsidies for green innovation; 4 The evidence on each (US SO₂ trading, carbon taxes,
  standards); 5 Positive externalities: knowledge, vaccination; 6 Government failure in this market (mismeasured damage, permits
  given away, lobbying) — forward pointer to g11-09.
- **Owns**: externality, negative externality, positive externality, private cost, external cost, social cost, social benefit,
  Pigouvian tax, tradable permit, Coase theorem (as a result label), transaction cost, emission standard.
- **Recalls**: Book 1 — pollution and income charts (g6). Earth and space sciences — the physical climate (grade 12
  `climate-change`), recalled, never re-taught. This book — DWL (g10-09), surplus (g10-08), tax incidence (g10-10).
- **Models**: *The Pigouvian tax* — assumes the marginal external cost is known and constant; predicts the tax equal to it
  restores the efficient quantity; tested: Sweden's carbon tax (Andersson 2019, transport emissions about 11 % lower, ledger);
  breaks: when damage is unknown or varies by place, and when the tax is set by lobbying. *The Coase result* — assumes clear
  rights, few parties, low transaction costs; predicts the efficient outcome whoever holds the right; tested: bargaining in
  laboratory experiments and in some local disputes (ledger); breaks: many parties (air pollution). *Tradable permits* — tested:
  the US acid rain programme (Schmalensee and Stavins 2013, ledger).
- **Charts**: opening [A] `ceds("so2")` against `maddison` gdppc for USA, GBR, DEU, JPN, CHN, IND, 1850–2022, times-ten x
  axis (rise then fall in rich countries; source line names both). Second [A] `ceds("so2", isos=["USA"])` 1970–2022 with the
  1990 law and the 1995 start marked (dates from the ledger, a vertical guide drawn from a one-row ledger table: see sync
  questions).
- **Diagrams**: social cost above private cost with the DWL; the tax restoring the efficient quantity; Coase bargaining table
  (two parties, two rights assignments); permits market (cap, permit price).
- **Photographs**: one, London's smog of December 1952 (Commons, licence read at writing; CC BY-SA if the known photograph).
- **Boxes**: `model` ×3 (Pigou, Coase, permits); `record`[The US acid-rain programme, 1995–2010]; `debate` none (the
  instrument comparison is empirical but not one of the outline's open questions; kept as `record` boxes).
- **Exercises**: ★ social cost from a table ×2, R opening chart, the efficient quantity, the Pigouvian tax; ★★ DWL of an
  externality ×2, Coase bargain under two rights ×2, P a permit price after a tighter cap, C positive externality subsidy;
  ★★★ X evidence contradicting the Coase result, a standard versus a tax with two firms of different abatement cost (the tax is
  cheaper, proved), a tax set too high, a vaccination subsidy.
- **Problem**: *The tannery on the Bren* — a tannery's marginal benefit and the fishery's marginal damage (linear); the market
  outcome, the efficient one, a Pigouvian tax, a Coase bargain, a permit market with two tanneries. Named result: **the
  efficient tax and the surplus it recovers, and the saving of permits over a uniform standard**.
- **Ledger**: Clean Air Act Amendments 1990 (LAW), programme start 1995; Schmalensee and Stavins (2013, JEP); Andersson (2019,
  AEJ: Policy); Sweden carbon tax start (1991); a published estimate of the cost saving of trading.

### g11-07 Public Goods and Common Resources (`public-goods-and-commons`)
- **Programme**: P13, P15, T30 (in part), T32 (international agreements and free riding), PR public goods and common
  resources.
- **Sections**: 1 Rival or not, excludable or not (four kinds of goods); 2 Free riding and how public goods get provided (taxes,
  clubs, bundling, technology that excludes, private provision with the lighthouse record); 3 Overuse of a common resource (the
  open-access model: entry until average catch equals cost); 4 Answers and their record (property rights, transferable quotas,
  community rules, international agreements and free riding).
- **Owns**: rival good, excludable good, private good, public good, club good, common resource, free rider, tragedy of the
  commons, individual transferable quota.
- **Recalls**: Book 1 — property rights (g9 institutions; check Book 1's definition). This book — externality (g11-06), Nash
  equilibrium and the prisoner's dilemma (g11-05).
- **Models**: *Open access to a common resource* — assumes free entry and a catch that falls with total effort; predicts effort
  until rent is gone and the stock is overused; tested: the Peruvian anchoveta 1960–73 (chart), cod off Newfoundland (ledger);
  breaks: small communities with enforced rules (field studies, ledger), quotas with secure rights (Costello, Gaines and Lynham
  2008, ledger).
- **Charts**: opening [A] `wdi("ER.FSH.CAPT.MT", isos=["PER"])` 1960–2000 (checked: 12.5 Mt in 1970, 4.1 Mt by 1974),
  thousand tonnes. Second [A] the same for Iceland and New Zealand (transferable quotas from 1984–90), or Canada around 1992.
- **Diagrams**: the 2×2 goods table; the open-access fishery (total revenue curve, cost line, open-access and efficient effort);
  a public-goods contribution game.
- **Photographs**: one, a historic British lighthouse (Commons, PD) for the private-provision record.
- **Boxes**: `model` (open access); `record`[The anchoveta collapse, 1972–73]; `record`[Lighthouses paid by port dues] (ledger,
  with the published debate on how private they were, stated fairly).
- **Exercises**: ★ classify goods ×3, R opening chart ×2; ★★ open-access effort ×2, efficient effort, P a quota's effect, C a
  club's fee covering cost, R the ITQ chart; ★★★ X evidence contradicting the tragedy of the commons, a voluntary contribution
  game with n players, an international agreement as a prisoner's dilemma, a quota price.
- **Problem**: *The Kestrian fishery* — catch per boat falls with the number of boats; open access; the rent-maximising fleet; an
  ITQ system; the quota price. Named result: **the rent dissipated under open access and the price of a one-tonne quota**.
- **Ledger**: El Niño 1972–73 and the anchoveta (published FAO/IMARPE page); Newfoundland cod moratorium (2 July 1992);
  Costello et al. (2008, Science); Iceland/New Zealand ITQ start dates; Coase (1974) and later reassessment (Bertrand 2006) for the
  lighthouse box.

### g11-08 Asymmetric Information (`asymmetric-information`)
- **Programme**: P14 (adverse selection, used cars, moral hazard, insurance, no equilibrium), P15, P29 (managers and owners, as a
  principal–agent case), PR asymmetric information.
- **Sections**: 1 Hidden quality: the used-car market can unravel (lemons model, proved for a uniform quality); 2 Hidden action:
  insurance changes behaviour (moral hazard); principal and agent (an owner and a manager); 3 Answers on the informed side
  (warranties, reputation, certification, signals) and on the other side (deductibles, screening, experience rating);
  4 Compulsory and voluntary cover (what adverse selection predicts for each, and the record).
- **Owns**: asymmetric information, adverse selection, moral hazard, signalling, screening, deductible, principal–agent problem.
- **Recalls**: Book 1 — markets (g7). This book — willingness to pay (g10-08).
- **Models**: *The lemons model* (Akerlof's model as a label) — assumes sellers know quality, buyers know only the average;
  predicts good cars leave the market and the price falls, possibly to collapse; tested: mixed — used pickup trucks showed no
  lemons effect (Bond 1982), certified-car premia and warranties exist where it bites (ledger); breaks: inspection, reputation,
  warranties. *Moral hazard in insurance* — tested: the RAND Health Insurance Experiment (spending fell as the share paid rose,
  ledger table).
- **Charts**: opening [L] RAND experiment: spending per person by coinsurance plan (free, 25 %, 50 %, 95 %), Manning et al.
  (1987, AER) / RAND report R-3476 (free at rand.org). (Replaces car resale by age: no approved car-price data.) Second [I] the
  unravelling of a lemons market: price and average quality over rounds, a seeded simulation, labelled as invented.
- **Diagrams**: the lemons unravelling (quality distribution, buyers' offer, sellers' threshold); a moral-hazard effort choice
  (benefit of care against cost); a signalling separating diagram (two types, cost of the signal).
- **Photographs**: none.
- **Boxes**: `model` ×2 (lemons, moral hazard); `record`[The RAND Health Insurance Experiment, 1974–82].
- **Exercises**: ★ classify adverse selection/moral hazard ×3, R opening chart ×2; ★★ lemons price with two qualities ×2, P a
  warranty's effect, C deductible and expected cost, C signal cost condition, R the simulation chart; ★★★ X evidence contradicting
  the lemons model (the trucks), an insurance pool unravelling with three risk types, a manager's bonus as a fix and its cost,
  compulsory cover and the pool.
- **Problem**: *Brenmoor's used-car market* — car qualities uniform between two values; sellers value at quality, buyers at 1.5 ×
  quality; the market price; an inspection service. Named result: **the price at which the market settles, and the share of cars
  traded, with and without inspection**.
- **Ledger**: RAND HIE spending table; Bond (1982, AER); one certification/warranty study; HIE dates.

### g11-09 Public Choice: A First Look (`public-choice-first-look`)
- **Programme**: P15 and T31 (failures of public action), PR political economy; user addition (2026-11-19/20).
- **Sections**: 1 The same assumption about incentives, for voters, elected officials and agencies; 2 Why a voter stays
  uninformed (the expected value of a vote against the cost of learning); 3 Concentrated benefits and dispersed costs (who
  organises); lobbying and rent seeking (the cost of the contest, not only the transfer); 4 Capture of a regulator by the
  regulated; 5 The comparison that matters: an imperfect market against an imperfect government (each with its evidence).
- **Owns**: government failure, rational ignorance, interest group, concentrated benefits and dispersed costs, rent seeking,
  regulatory capture.
- **Recalls**: Book 1 — taxes and public spending (g8). This book — DWL (g10-09), externalities (g11-06), the prisoner's dilemma
  (g11-05). Mathematics — expectation (g11).
- **Models**: *Concentrated benefits, dispersed costs* — assumes each group spends on influence up to its stake, organising has
  a cost; predicts policies with small per-person costs and large per-firm gains survive; tested: the US sugar programme (GAO,
  ledger; opening chart), farm support across countries; breaks: when an issue becomes salient (mass attention), or when costs
  are concentrated too (industrial users of sugar lobbied back). *Rent seeking* — tested: estimates of resources spent on
  lobbying (ledger); breaks: open, contestable rules.
- **Charts**: opening [L] the US sugar programme: cost per US household against gain per sugar producer (GAO 2000 report,
  public domain), two bars on a times-ten scale. Second [I] Brenland's sugar quota from the chapter script.
- **Diagrams**: the transfer rectangle plus the DWL triangles of a protection programme (pointer to g12-13 for the tariff
  version); a rent-seeking contest (expected prize against spending).
- **Photographs**: none.
- **Boxes**: `model` ×2; `record`[Sugar in the United States]; `record`[Capture: a documented regulatory case] (e.g. the US
  Interstate Commerce Commission and trucking regulation until 1980, with its deregulation price effects, ledger).
- **Exercises**: ★ cost per household from totals ×2, R opening chart, identify concentrated/dispersed, the expected value of a
  vote; ★★ rent-seeking spending in a contest ×2, P a quota's transfer and DWL, C a voter's information decision, R second chart,
  P salience; ★★★ X evidence contradicting the interest-group model, a regulator's choice with a revolving door, comparing a
  market failure's DWL with a programme's DWL, a log-rolling vote table.
- **Problem**: *Brenland's sugar quota* — demand and supply of sugar, a world price, an import quota; the domestic price; the
  transfer to 200 growers; the cost to 3 million households; lobbying spending. Named result: **the gain per grower against the
  cost per household, and the share of the transfer spent on lobbying**.
- **Ledger**: GAO/RCED-00-126 figures; Motor Carrier Act 1980 (LAW) and a published deregulation price estimate; one rent-seeking
  estimate; the probability-of-being-decisive estimate (Gelman, Silver and Edlin 2012) for the vote example.

### g11-10 The Labour Market (`labour-market`)
- **Programme**: S13 (schooling as human capital; returns; qualification and unemployment; wage by education; experience,
  firm, gender), T13 (minimum wage), PR factor markets, earnings and discrimination.
- **Sections**: 1 Labour demand from the value of the marginal product (proved: hire until VMPL = w); 2 Labour supply: work against
  free time (the reservation wage; a rising supply curve, with backward bending as a possibility); 3 The wage and wage
  differences (human capital and the return to a year of schooling; compensating differences; measured pay gaps and what
  decompositions explain and leave unexplained); 4 One large employer (monopsony, first look); 5 The minimum wage: what two models
  predict, and the measured effect (`debate`).
- **Owns**: value of the marginal product of labour, labour demand, labour supply, reservation wage, human capital, return to
  schooling, compensating differential, monopsony, minimum wage.
- **Recalls**: Book 1 — unemployment and participation rates, why wages differ (g8). This book — marginal product (g11-02),
  tax incidence (g10-10, for payroll taxes).
- **Models**: *The competitive labour market* — assumes price-taking employers and workers; predicts w = VMPL and a binding
  minimum wage lowers employment; *Monopsony* — assumes one employer facing the market supply; predicts a moderate minimum wage can
  raise employment; tested: the minimum-wage studies (`debate` box); returns to schooling from twins and from natural experiments
  (Ashenfelter and Krueger 1994; Angrist and Krueger 1991; ledger); breaks: heterogeneity across workers, large rises.
- **Charts**: opening [L] median weekly earnings and unemployment rate by educational attainment (BLS, *Education pays*, US,
  public domain, one recent year): a short table drawn as bars. (Replaces earnings by years of schooling: the approved NSW/CPS
  sample's earnings are top-coded at 25,244 and give a flat profile for prime-age men — checked.) Second [A] `wdi`
  SL.UEM.BASC.ZS / SL.UEM.INTM.ZS / SL.UEM.ADVN.ZS across countries (unemployment by education).
- **Diagrams**: labour demand as VMPL; labour supply; minimum wage in the competitive model (unemployment); monopsony (marginal
  cost of labour above supply; a minimum wage between).
- **Photographs**: none.
- **Boxes**: `model` ×2; `debate`[The employment effect of a minimum wage] (Card and Krueger 1994; Neumark and Wascher 2008
  review; Cengiz, Dube, Lindner and Zipperer 2019 bunching; Jardim et al. 2017/2022 Seattle hours; each with its weakness);
  `dated{2026}`[minimum wages in several countries, ledger]; `measure`[How a pay gap is decomposed].
- **Exercises**: ★ VMPL from a table ×2, R opening chart, compensating differential, the reservation wage; ★★ labour demand
  from a production function ×2, P a payroll tax's incidence, C the return to schooling from two wages, C monopsony wage and
  employment, R second chart; ★★★ X evidence contradicting the competitive model's minimum-wage prediction (and what each side
  answers), a minimum wage in monopsony that raises employment (proved on lines), why schooling and earnings correlate without
  all of it being cause, an unexplained gap is not a measured discrimination.
- **Problem**: *A minimum wage for Brenmoor's cafés* — labour supply and demand (lines); a competitive market and a monopsony
  version; minimum wages of 11, 13 and 15 dalens per hour. Named result: **the employment change under each model at each minimum
  wage, and the wage at which the monopsony prediction turns negative**.
- **Ledger**: BLS *Education pays* values; the `debate` studies' estimates; Ashenfelter and Krueger (1994); minimum-wage levels
  (dated); Blau and Kahn (2017, JEL) decomposition shares.

### g11-11 Inequality (`inequality`)
- **Programme**: T25–T26 (trends since 1900, inter-quantile ratio, Lorenz, Gini, top 1 %, parent–child correlation), T methods
  (mobility tables: destiny and recruitment), T4 (technical progress and inequality), T28 (redistribution and its incentive
  costs, measured), S7, PR income inequality and poverty, design of the tax system (progressive and regressive taxes).
- **Sections**: 1 The Lorenz curve and the Gini coefficient (Gini by trapezoids; properties proved: 0 for equality, the curve
  below the diagonal and convex for ranked data); inter-quantile ratios; top shares; 2 Before and after taxes and transfers
  (market and disposable income; progressive and regressive taxes; the equivalence scale); 3 Income, consumption and wealth;
  4 Between countries and inside them (recall Book 1's world distribution); the supply and demand for skills (technical change);
  5 Mobility from one generation to the next (mobility tables, outflow and inflow; the parent–child correlation, read not
  computed); 6 What the measures miss (household size, age, in-kind benefits, taxes not seen).
- **Owns**: market income, disposable income, equivalence scale, Lorenz curve, Gini coefficient, interdecile ratio, top income
  share, wealth, progressive tax, regressive tax, intergenerational mobility, mobility table.
- **Recalls**: Book 1 — mean and median income, shares by fifths, the world distribution (g9), poverty line (g6). Mathematics —
  quartiles and standard deviation (g11 `descriptive-statistics`). This book — marginal and average tax rates (g11-01).
- **Models**: *Supply and demand for skills* — assumes two kinds of labour, relative demand shifts with technology; predicts the
  skill premium rises when demand outpaces supply; tested: the US college premium 1963–2010 (Goldin and Katz; Autor 2014, ledger);
  breaks: it does not explain top 1 % shares, and the premium stalled after 2000.
- **Charts**: opening **[D]** Gini before and after taxes and transfers across European countries (Eurostat ilc_di12 and
  ilc_di12b/c, to approve). Fallback [A] `pip_percentiles` Lorenz curves for SWE, USA, BRA, ZAF (latest year, 2021 PPP,
  national; checked coverage) — this is drawn anyway as the second chart; the opening becomes Brenland's before/after
  Lorenz [I] if the Eurostat tables are refused. Third [A] `wdi("SI.POV.GINI")` against income per person across countries.
- **Diagrams**: Lorenz curve with the Gini area; trapezoid computation figure; a 3×3 mobility table (outflow and inflow
  versions).
- **Photographs**: none.
- **Boxes**: `model` (skills); `measure`[How a Gini coefficient is computed from a survey]; `measure`[Equivalence scales];
  `record`[Top income shares in the twentieth century] (ledger, from the published series: WID values as cited numbers).
- **Exercises**: ★ shares by fifths to Lorenz points ×2, R opening chart, interdecile ratio, read a mobility table; ★★ Gini by
  trapezoids ×2, before/after transfers from Brenland, progressive or regressive from a table, outflow to inflow table, P a flat
  transfer's effect on the Gini; ★★★ X evidence contradicting the skills model, a Gini that falls while the poorest lose (a
  constructed case), equivalence scales change the ranking, consumption against income inequality.
- **Problem**: *Brenland's household survey* — from `households.csv`: equivalised income, Lorenz curves before and after taxes
  and transfers, Gini by trapezoids over fifths, the interdecile ratio, the share of the top tenth. Named result: **the Gini
  coefficient before and after taxes and transfers, and the reduction in points**.
- **Ledger**: WID top-1 % shares for two countries at a few dates; Goldin–Katz / Autor premium values; Chetty et al. (2014)
  US mobility figures; OECD equivalence scale definition (square root scale) page.

### g11-12 Unemployment (`unemployment`)
- **Programme**: T11 (unemployment, underemployment, employment rate), T12 (matching, efficiency wages), T13 (minimum wage,
  employment protection), T14 (cyclical unemployment), T15 (policies: demand support, lower labour costs, training, flexibility —
  each described with its evidence, no prescription), S13 (lack of qualification), PR the natural rate of unemployment.
- **Sections**: 1 The survey definitions in detail (ILO criteria; employment rate; underemployment; discouraged workers);
  2 Flows into and out of unemployment (stocks and flows; the steady-state rate u = s/(s+f), derived as the limit of a
  recurrence — grade 11 sequences); how long spells last; 3 Frictional, structural, cyclical; the natural rate; 4 Why wages do not
  fall to clear the market (efficiency wages, contracts, minimum wages); 5 What the evidence says about benefits, hiring rules and
  the main policies (each with its best study).
- **Owns**: ILO unemployment, employment rate, underemployment, separation rate, job-finding rate, frictional unemployment,
  structural unemployment, cyclical unemployment, natural rate of unemployment, long-term unemployment, efficiency wage,
  employment protection, replacement rate.
- **Recalls**: Book 1 — unemployment and participation rates, the survey (g8). This book — minimum wage (g11-10).
  Mathematics — arithmetic-geometric recurrences and their limit (g11 `sequences`).
- **Models**: *Stock–flow model of unemployment* — assumes constant separation and job-finding rates; predicts u* = s/(s+f) and
  convergence to it; tested: US and European flow rates (ledger); breaks: rates move with the cycle. *Efficiency wages* — tested:
  Ford's 1914 five-dollar day (Raff and Summers 1987, ledger).
- **Charts**: opening [A] `eurostat("une_rt_a")` youth (Y15-24) and total (Y15-74) unemployment, PC_ACT, across European
  countries, 2024, bars: similar economies, very different structural rates. (Replaces unemployed against vacancies: no vacancy
  data approved.) Second [A] JST `unemp` for USA, GBR, DEU 1870–2020 (cyclical swings; the 2019 USA value in JST R6 is 2.0, a
  data error: use WDI SL.UEM.TOTL.NE.ZS for 2019).
- **Diagrams**: the labour-force boxes with the flows; convergence of u to u* (a recurrence plot); a labour market with a wage
  above the clearing level.
- **Photographs**: one, a 1930s unemployment queue (US government photograph, PD), for the cyclical section.
- **Boxes**: `model` ×2; `measure`[Who counts as unemployed]; `record`[The five-dollar day, 1914]; `record`[Unemployment benefit
  duration and spell length] (a published natural-experiment estimate, e.g. Card, Chetty and Weber 2007 Austria; Lalive 2008).
- **Exercises**: ★ classify people by ILO status ×2, rates from counts ×2, R opening chart; ★★ steady-state rate ×2, iterate the
  recurrence three years, P a fall in the job-finding rate, R JST chart (cyclical peaks), C long-term share; ★★★ X evidence
  contradicting a constant natural rate, an efficiency-wage condition, a benefit change in the flow model, why the youth rate is
  higher in some countries (several mechanisms, the evidence for each).
- **Problem**: *Brenland's labour flows* — monthly separation and job-finding rates for two groups (with and without upper
  secondary schooling); steady states; the aggregate rate; a recession lowers job finding for a year; the path back. Named result:
  **the steady-state unemployment rate of each group and of Brenland, and the months to close half the gap after the recession**.
- **Ledger**: ILO definitions (the 2013 resolution); Shimer (2012) US flow rates; Raff and Summers (1987); Card, Chetty and Weber
  (2007); a published employment-protection estimate.

### g11-13 Money and Banking (`money-and-banking`)
- **Programme**: P21 (recalled), P22 (credit creates money, balance sheets), P23 (the central bank steers the short rate), T18
  (bank panics), T20 (supervision, capital ratio), T16 (the 1930s banking crisis, as a record), PR the monetary system.
- **Sections**: 1 A bank's balance sheet (assets, liabilities, capital; T-accounts); 2 Reserves; loans create deposits (worked
  T-accounts); 3 The money multiplier as a toy model (derived as a geometric sum) and why it broke after 2008 (banks held large
  reserves; the opening chart); measures of money; 4 The central bank: banker to the banks, setter of the policy rate (how it
  steers the overnight rate, told); 5 Bank runs, deposit insurance, capital ratios and supervision (first look; the trade-off with
  moral hazard).
- **Owns**: balance sheet, bank capital, reserves, central bank money, broad money, money creation, money multiplier, policy
  rate, bank run, deposit insurance, lender of last resort, capital ratio.
- **Recalls**: Book 1 — money and its three functions (g7), bank, deposit, loan, interest (g8). This book — moral hazard (g11-08).
  Mathematics — geometric sums (g11).
- **Models**: *The money multiplier* (toy) — assumes banks lend all excess reserves and the public holds a fixed share of cash;
  predicts broad money = multiplier × central bank money; tested: roughly before 2008; breaks: after 2008, central bank money
  quintupled while broad money grew slowly (JST: US narrow money 847 → 3,427 between 2007 and 2019, checked). *Bank run as a
  coordination game* — tested: the 1930–33 US waves of runs (ledger); breaks: deposit insurance, credible lender of last resort.
- **Charts**: opening [A] `jst(["USA"], 2000–2020)` narrowm and money (index 2000 = 100), `omtime` (JST narrow money for the
  US matches the monetary base's 2008 jump; source line says "narrow money as JST defines it"). Second [A] the same for GBR or JPN,
  or `wdi("FM.LBL.BMNY.GD.ZS")`.
- **Diagrams**: T-accounts of a loan creating a deposit; a two-bank chain with reserves; the bank-run game table.
- **Photographs**: one, a crowd outside a US bank in 1931–33 (PD), for the run.
- **Boxes**: `model` ×2; `record`[Bank runs in the United States, 1930–33] (dated; deposit insurance 1933, LAW);
  `measure`[Measures of money]; `dated{2026}`[capital requirements in force, ledger].
- **Exercises**: ★ T-account entries ×3, R opening chart, a capital ratio; ★★ multiplier with cash and reserve shares ×2, a loan
  repaid destroys money, P a reserve injection under the two regimes, C capital after a loss, R second chart; ★★★ X evidence
  contradicting the multiplier model (the chart), the run game's two equilibria, deposit insurance and risk-taking, a bank's
  maximum loss before insolvency.
- **Problem**: *The banks of Brenland* — three banks' balance sheets; a loan wave; reserves and the multiplier; the central bank
  doubles reserves in two regimes (banks lend / banks hold); a run on one bank. Named result: **broad money after the reserve
  injection in each regime, and the share of deposits that can be withdrawn before the bank fails**.
- **Ledger**: Banking Act 1933 (FDIC, LAW); Friedman–Schwartz / FDIC counts of bank suspensions 1930–33 (FDIC or Fed history page);
  Basel III minimum ratios (BIS page, dated); Bank of England (2014) "Money creation in the modern economy" (primary).

---

## Grade 12 — Time, growth, the short run, the open economy

### g12-01 Present Value (`present-value`)
- **Programme**: P16–P17 (in part), PR the tools of finance.
- **Sections**: 1 Compounding, yearly and continuous (the exponential recalled; the limit of (1 + r/n)^n); 2 Discounting and the
  present value of a stream (a geometric sum, proved); perpetuity and annuity (formulas proved); 3 A bond's price falls when its
  yield rises (proved for a perpetuity and for a two-year bond); 4 Net present value of an investment; real and nominal rates
  (recalled and applied).
- **Owns**: continuous compounding, present value, discount rate, discounting, net present value, perpetuity, annuity, bond,
  coupon, yield to maturity.
- **Recalls**: Book 1 — compound interest, doubling time (g8). This book — real interest rate (g10-12). Mathematics — geometric
  sums (g11), exponential and logarithm, limits (g12).
- **Models**: *Bond price by present value* — assumes payments are certain; predicts price falls as yield rises, more for long
  bonds; tested: the 1980–2020 fall in long yields with rising prices (chart); breaks: default risk, inflation surprises (the
  nominal payments lose value).
- **Charts**: opening [A] `jst(["USA","GBR"], 1980–2020)` ltrate, with the price of a perpetuity paying 1 per year (1/ltrate)
  computed in the script (labelled as computed), `omtime`. Second [A] `jst` bond_tr cumulative index for the same countries.
- **Diagrams**: a time line of cash flows with discount factors; price–yield curve for a perpetuity and a ten-year bond.
- **Photographs**: none.
- **Boxes**: `model`; `measure`[What a bond's yield is].
- **Exercises**: ★ compound values ×2, present value ×2, R opening chart; ★★ annuity ×2, perpetuity price at two yields, P
  price change of a long versus a short bond, C NPV with a real rate, C continuous compounding; ★★★ X what would contradict the
  price–yield rule (a default), the yield of a bond from its price (two-year, a quadratic), the limit proof, choosing between two
  projects whose ranking changes with the rate.
- **Problem**: *Financing Brenmoor's new bridge* — construction cost, tolls for 30 years, maintenance; NPV at 2 %, 4 % and 6 %;
  financing by a perpetual bond; the rate at which NPV is zero (found by bisection). Named result: **the net present value at 4 %
  and the break-even discount rate**.
- **Ledger**: UK consol history (dated: issued 1752, redeemed 2015; HM Treasury page) for a perpetuity example.

### g12-02 Risk and Insurance (`risk-and-insurance`)
- **Programme**: P24–P28 (risks; attitudes; benefits and moral hazard of risk sharing; prevention, pooling, diversification;
  institutions: family, insurers and mutuals, public bodies; social insurance and assistance — described as instruments),
  PR risk.
- **Sections**: 1 Expected value recalled; risk aversion from a concave utility (Jensen's inequality for two outcomes, proved);
  2 The certainty equivalent and the risk premium; 3 A fair premium and a loaded one; the most a person will pay; 4 Pooling and
  the law of large numbers (recalled); when pooling fails (common shocks); spreading risk across assets (first look); 5 Who carries
  risk: families, insurers and mutuals, public social insurance and means-tested assistance; hidden quality and hidden action
  recalled.
- **Owns**: risk aversion, risk neutrality, expected utility, certainty equivalent, risk premium, actuarially fair premium,
  loading, pooling, diversification, social insurance, means-tested assistance, prevention.
- **Recalls**: Mathematics — expectation (g11–g12), convexity (g12), the law of large numbers (g12 `sums-lln`). This book —
  adverse selection and moral hazard (g11-08).
- **Models**: *Expected utility* — assumes a concave utility of wealth; predicts people pay more than the fair premium to insure
  large losses; tested: insurance demand, deductible choices (ledger); breaks: people buy lottery tickets and insurance at once,
  overweight small probabilities (ledger; behavioural evidence is Year 2's).
- **Charts**: opening [A] `wdi("SP.DYN.CDRT.IN")` for FRA, JPN, SWE, USA 2000–2024 (deaths per 1,000 people): stable for the
  pool, with the 2020 jump showing a common shock (checked). (Replaces claims per 1,000 policies: no insurance data approved.)
  Second [I] the spread of the average loss as the pool grows (seeded simulation, 10 to 10,000 members).
- **Diagrams**: concave utility with the certainty equivalent and the risk premium; the fair-odds line; the shrinking spread of a
  pooled average.
- **Photographs**: none.
- **Boxes**: `model`; `measure`[How a premium is priced]; `record`[Hurricane Andrew 1992 and the insurers it broke] (a common
  shock; ledger).
- **Exercises**: ★ expected value ×2, R opening chart, certainty equivalent with √, a fair premium; ★★ risk premium ×2, maximum
  premium, P loading and demand, C pooled standard deviation for n members, C diversification of two assets (variance, admitted
  formula for independent); ★★★ X evidence contradicting expected utility, pooling with correlated risks, social insurance
  compared with private cover under adverse selection, prevention as a substitute for insurance.
- **Problem**: *Insuring Kestria's orchards* — a grower with √ utility, a frost probability; certainty equivalent; maximum premium;
  a mutual of 400 growers; a common frost that hits all. Named result: **the maximum premium a grower pays, and the reserve the
  mutual needs to survive a common frost with given probability**.
- **Ledger**: Hurricane Andrew insured losses and insolvencies (published page); a deductible-choice study (Sydnor 2010);
  lottery participation figure.

### g12-03 Inflation and the Quantity of Money (`inflation-and-money`)
- **Programme**: P23 (effects on prices), PR money growth and inflation.
- **Sections**: 1 The quantity equation and its growth-rate form (logarithm: growth rates add, proved); 2 The record across
  countries and decades (opening chart); 3 Hyperinflations and how they ended (Germany 1923, Hungary 1946, Zimbabwe 2008:
  seigniorage, the inflation tax); 4 The costs of inflation (expected and unexpected; redistribution between lenders and
  borrowers); 5 Nominal and real interest rates (Fisher, recalled and extended).
- **Owns**: velocity of money, quantity equation, quantity theory of money (in its `model` box), hyperinflation, seigniorage,
  inflation tax, Fisher effect, unexpected inflation.
- **Recalls**: Book 1 — inflation rate, real and nominal (g8), very high inflation (g8). This book — real interest rate (g10-12),
  central bank money and broad money (g11-13). Mathematics — logarithm (g12).
- **Models**: *The quantity theory* — assumes velocity and real output grow at stable rates, money is set by the central bank;
  predicts inflation ≈ money growth − output growth; tested: high and long inflations across countries 1990–2019 (chart; checked
  123 countries, correlation 0.98 of averages); breaks: low inflation, where velocity moves (the US after 2008).
- **Charts**: opening [A] `wdi("FM.LBL.BMNY.ZG")` against `wdi("FP.CPI.TOTL.ZG")`, country averages 1990–2019 (25+ years of
  data), log axes (grade 12: the logarithmic scale replaces the times-ten scale), with the 45° line. Second [A] JST velocity
  (gdp/money) for USA 1960–2020.
- **Diagrams**: none required beyond the 45° line on the chart; a T-account of money printing to pay a deficit.
- **Photographs**: one or two hyperinflation banknotes (Germany 1923 or Hungary 1946, public domain; licence read at writing;
  Zimbabwe notes only if the licence page allows).
- **Boxes**: `model`; `record`[Germany 1923]; `record`[Zimbabwe 2007–09]; `measure`[Measuring inflation in a hyperinflation].
- **Exercises**: ★ quantity equation ×2, growth-rate form, R opening chart ×2; ★★ velocity from data ×2, P inflation from money
  growth and output growth, C seigniorage, C Fisher real rate, R JST velocity chart; ★★★ X evidence contradicting the quantity
  theory (2008–19), inflation tax rate as a function of inflation, who gains from unexpected inflation, why hyperinflations end with
  a fiscal reform.
- **Problem**: *Kestria's printing press* — a deficit financed by money; money growth; velocity rising as people flee money;
  monthly inflation; the stabilisation. Named result: **the monthly inflation rate when velocity doubles, and the seigniorage
  collected before and after**.
- **Ledger**: German 1923 price figures (a published table); Hungary 1946 peak monthly rate (Hanke and Krus table); Zimbabwe 2008
  (the same source); Rentenmark date.

### g12-04 Growth and the Production Function (`growth-and-production-function`)
- **Programme**: T1 (accumulation and total factor productivity), T methods (average rate of change), S3, S6, PR production and
  growth.
- **Sections**: 1 The aggregate production function with capital, labour and technology; constant returns and diminishing
  returns to capital (proved for Cobb–Douglas); output per worker y = A k^α; 2 The shares of income going to labour and capital
  (under competition, α is capital's share; the PWT labour share); 3 Growth accounting with logarithms (growth rates of a product
  add, proved; the residual); 4 What the accounts show (US, Korea, a few others; the average annual growth rate as a geometric
  mean).
- **Owns**: aggregate production function, constant returns to scale, diminishing returns to capital, capital per worker,
  labour share of income, Cobb–Douglas production function, total factor productivity, growth accounting, average annual growth
  rate.
- **Recalls**: Book 1 — factors of production and productivity (g8), growth rate (g8), income per person over the long run (g6).
  This book — human capital (g11-10), depreciation (g10-11). Mathematics — logarithm (g12).
- **Models**: *The Cobb–Douglas aggregate production function* — assumes constant returns, smooth substitution, a constant
  capital share; predicts stable income shares and diminishing returns to capital per worker; tested: labour shares near two
  thirds for decades in rich countries (PWT labsh, chart); breaks: the labour share's decline in several countries since 1980
  (Karabarbounis and Neiman 2014, ledger).
- **Charts**: opening [A] `pwt(since=2019, until=2019)` cgdpo/emp against cn/emp (current-PPP levels, the PWT's own advice
  for cross-country comparisons), log axes, 2021 dollars. Second [A] `pwt` labsh for USA, GBR, FRA, JPN, KOR 1950–2023.
- **Diagrams**: y = A k^α with two values of A; the growth-accounting decomposition as stacked bars (from the chart data).
- **Photographs**: none.
- **Boxes**: `model`; `measure`[How a capital stock is measured] (perpetual inventory); `record`[Korea 1960–2000: accumulation
  and productivity] (published growth-accounting results, ledger).
- **Exercises**: ★ output from a Cobb–Douglas ×2, R opening chart, average annual growth rate ×2; ★★ returns to scale check ×2,
  growth accounting ×2, P effect of doubling k, R labour share chart; ★★★ X evidence contradicting constant shares, the residual
  with human capital, why capital alone cannot explain income gaps (a k^α calculation), a production function with increasing
  returns.
- **Problem**: *Brenland's growth accounts, 2000–2025* — capital built by perpetual inventory from `accounts.csv` investment
  (deflated) with an initial stock and δ given; employment; α = 0.35; TFP growth as the residual. Named result: **the share of
  Brenland's growth of output per worker due to TFP**.
- **Ledger**: Karabarbounis and Neiman (2014, QJE); Young (1995) East Asian growth accounting; PWT documentation for labsh.

### g12-05 The Solow Model: A First Look (`solow-first-look`)
- **Programme**: T1, PR production and growth.
- **Sections**: 1 Saving, depreciation and accumulation as a recurrence (k_{t+1} = s A k_t^α + (1−δ)k_t, per worker, with no
  population growth first); 2 The steady state (existence and the convergence of the recurrence, proved for α < 1 with the
  monotonicity argument at grade-12 level); 3 A higher saving rate raises the level of income, not its long-run growth; 4
  Convergence (among similar countries; conditional convergence); 5 Sustained growth needs better technology.
- **Owns**: saving rate, capital accumulation equation, steady state, conditional convergence, absolute convergence; the *Solow model*
  indexed in its `model` box.
- **Recalls**: This book — aggregate production function, TFP (g12-04), depreciation (g10-11). The chapter owns *saving rate*
  (the share of output saved); g12-07, which comes later, owns national, private and public saving. Book 1 — growth and compounding (g8). Mathematics — recurrences and
  limits (g12 `sequences`).
- **Models**: *The Solow model* — assumes a constant saving rate, diminishing returns to capital, exogenous technology; predicts a
  steady state, faster growth below it, a level effect of saving; tested: postwar recovery of West Germany and Japan (ledger),
  convergence among rich countries (chart); breaks: does not explain technology; capital explains little of the gap between rich
  and poor countries.
- **Charts**: opening [A] `pwt` or `maddison`: growth of income per person 1960–2019 against income in 1960, OECD-founding
  members highlighted against all countries, x log axis. Second [I] the recurrence path from two starting points (seeded script,
  exact).
- **Diagrams**: the Solow diagram (sAk^α against δk) with the steady state; the effect of a higher saving rate; the time path of
  k after a saving rise.
- **Photographs**: one, a rebuilt German or Japanese city in the 1950s, or wartime destruction (PD or free licence, read at
  writing).
- **Boxes**: `model`; `record`[Recovery after 1945] (ledger: Davis and Weinstein 2002 on Japanese cities; Maddison values from a
  chart table).
- **Exercises**: ★ iterate the recurrence ×2, steady state ×2, R opening chart; ★★ effect of s on k* and y* ×2, P growth below
  the steady state, C half-life numerically, R the recurrence chart, C with population growth; ★★★ X evidence contradicting
  absolute convergence (the chart), why saving cannot sustain growth (proved: the limit), a war that destroys half of k, TFP
  versus k in explaining a gap.
- **Problem**: *Brenland's steady state* — parameters from Brenland's accounts (s = I/GDP, δ = 0.05, α = 0.35); the steady state;
  the path from today's k; a rise in the saving rate. Named result: **the steady-state output per worker and the years needed to
  close half the gap after the saving rise**.
- **Ledger**: Davis and Weinstein (2002, AER); West German postwar growth figures (from Maddison tables); Mankiw, Romer and Weil
  (1992) result (prose).

### g12-06 Ideas, Institutions and Growth (`ideas-institutions-growth`)
- **Programme**: T2 (endogenous technical progress, innovation), T3 (institutions and property rights; creative destruction),
  T4 (technical progress and inequality, pointer to g11-11), T5 (ecological limits and innovation), S8.
- **Sections**: 1 An idea can be used by everyone at once (nonrival; recall the four goods); 2 The incentives to invent: patents,
  prizes, competition (with the evidence on each); creative destruction (firms entering and exiting, the measured churn);
  3 Institutions recalled, then measured: an index of the rule of law against income (correlation, and the natural experiments
  recalled); 4 Why the best methods do not spread everywhere (diffusion lags, measured); 5 Growth and the environment: resources,
  pollution, climate; what innovation has done (energy intensity falling, chart), and what it has not.
- **Owns**: idea (as a nonrival good), patent, innovation prize, creative destruction, research and development, technology
  diffusion, energy intensity.
- **Recalls**: Book 1 — institutions and the three natural experiments (g9). This book — nonrival goods (g11-07), externalities
  (g11-06), TFP (g12-04), Solow (g12-05).
- **Models**: *Ideas-driven growth (toy)* — assumes the growth of A is proportional to research effort; predicts growth rises
  with researchers; tested: research effort has risen for decades while TFP growth has not (Bloom, Jones, Van Reenen and Webb
  2020, ledger) — so the toy breaks: ideas get harder to find.
- **Charts**: opening [A] `wdi("GOV_WGI_RL_EST")` against `wdi("NY.GDP.PCAP.PP.KD")`, 2019–2023 means, `countries_only=True`,
  log x (replaces "property rights index": the WGI rule-of-law estimate is approved and is the closest measure; caption says
  what it measures). Second [A] `wdi("EG.USE.COMM.GD.PP.KD")` or EG.EGY.PRIM.PP.KD energy intensity over time for several
  countries. Third (optional) [A] `wdi("GB.XPD.RSDV.GD.ZS")` R&D share against income.
- **Diagrams**: the patent trade-off (monopoly DWL now against invention later); a diffusion S-curve (logistic, admitted).
- **Photographs**: one, the Korean peninsula at night (NASA, public domain), for the institutions section.
- **Boxes**: `model`; `record`[The Korean peninsula at night]; `measure`[What a governance index measures] (WGI method and its
  limits); `debate` none.
- **Exercises**: ★ classify rival/nonrival ×2, R opening chart ×2, a patent's deadweight loss; ★★ prize versus patent PV ×2, P
  effect of a stronger patent, C energy intensity fall per year, R second chart, C diffusion lag; ★★★ X evidence contradicting the
  toy model, correlation versus cause in the opening chart, the growth effect of a rise in researchers under the toy model,
  creative destruction and inequality.
- **Problem**: *Two inventors in Brenmoor* — a medicine's demand; patent pricing for 20 years against a prize equal to the
  consumer surplus; PV calculations. Named result: **the prize that gives the inventor the same present value as the patent, and
  the deadweight loss it avoids**.
- **Ledger**: Bloom et al. (2020, AER); WGI methodology page; one prize example (Longitude Act 1714, LAW; or a modern advance
  market commitment) with dates; a creative-destruction churn figure (e.g. job reallocation rate, a published estimate).

### g12-07 Saving, Investment and the Financial System (`saving-and-investment`)
- **Programme**: P16–P20 (financing needs and capacities, the interest rate as the price on the loanable-funds market, household
  saving, gross operating surplus, self-financing and external finance: loans, shares, bonds, budget balance and crowding out),
  T16–T17 and T19 (bubbles and the transmission of a financial crisis, as a record), PR saving, investment and the financial
  system.
- **Sections**: 1 Saving equals investment in a closed economy (proved from the identities); private and public saving; who has a
  financing need and who has a capacity; 2 The market for loanable funds and the real interest rate; 3 A government deficit and
  crowding out (with linear curves: the size of the effect); 4 How firms finance investment: self-financing, bank loans, shares
  and bonds (told); 5 When finance fails: a bubble and how a crisis reaches the real economy (wealth, collateral, fire sales,
  credit), as a record of 1929–33 and 2007–09.
- **Owns**: national saving, private saving, public saving, net lending, market for loanable funds, crowding out, financial
  intermediary, share (equity), gross operating surplus, self-financing, speculative bubble.
- **Recalls**: Book 1 — saving (g7), banks (g8). This book — the accounting identities (g10-11), real interest rate (g10-12),
  bond and present value (g12-01), banks (g11-13).
- **Models**: *The loanable-funds market* — assumes a closed economy, saving rising and investment falling with the real rate;
  predicts a deficit raises the rate and crowds out investment; tested: in open economies the link weakens (Feldstein and
  Horioka 1980, the opening chart and the ledger); breaks: open capital markets, a liquidity trap.
- **Charts**: opening [A] `wdi("NY.GNS.ICTR.ZS")` against `wdi("NE.GDI.TOTL.ZS")`, 2010–2019 averages, `countries_only=True`,
  with the 45° line. Second [A] `jst` hpnom or eq_tr for USA 1995–2012 (a boom and bust) — optional.
- **Diagrams**: loanable funds with a deficit shift; a firm's financing structure (bars); the crisis-transmission chain
  (boxes and arrows).
- **Photographs**: one, a stock-exchange floor (historic, PD), for the shares section.
- **Boxes**: `model`; `record`[1929–33 and 2007–09: from a crash to output and jobs] (ledger: GDP and unemployment from JST, dates
  from primary sources); `measure`[Net lending in the accounts].
- **Exercises**: ★ S = I from accounts ×2, R opening chart, private and public saving, net lending of a sector; ★★ loanable-funds
  equilibrium ×2, crowding out with a deficit, P a saving glut, C a firm's self-financing ratio, R JST chart; ★★★ X evidence
  contradicting the closed-economy model (the chart), a bubble's price path from a growing-expectations rule, collateral and fire
  sales in numbers, the deficit's effect in an open economy.
- **Problem**: *Brenland's loanable funds* — saving and investment functions of the real rate; a deficit of 2 % of GDP; crowding
  out; capital inflows from Kestria at a world rate. Named result: **the crowding-out ratio in the closed economy, and the current
  account deficit once capital flows**.
- **Ledger**: Feldstein and Horioka (1980, EJ) coefficient; 1929 crash dates; Lehman date (15 September 2008); US unemployment
  peak values (from JST/WDI tables).

### g12-08 Aggregate Demand and Supply (`aggregate-demand-and-supply`)
- **Programme**: T14 (fluctuations), T23 (policy and the cycle, in part), T16 (2008 as a record), PR aggregate demand and
  aggregate supply.
- **Sections**: 1 The facts of the business cycle (recessions, expansions, the output gap; how a recession is dated);
  2 The long-run model: output set by factors and technology, money changes only prices (neutrality); 3 The short-run model:
  prices and wages slow to move; aggregate demand and short-run aggregate supply; 4 Demand shocks and supply shocks (2008, 1973–74,
  2020, 2021–22); 5 The return to the long run (the adjustment through prices), each model in its frame.
- **Owns**: business cycle, recession, expansion, potential output, output gap, aggregate demand, long-run aggregate supply,
  short-run aggregate supply, demand shock, supply shock, sticky price, neutrality of money.
- **Recalls**: This book — quantity equation (g12-03), national accounts (g10-11), aggregate production function (g12-04).
- **Models**: *The long-run aggregate model* — assumes flexible prices; predicts money affects only prices; tested: long-run
  money and inflation (g12-03 chart); breaks: in the short run. *The short-run AD–AS model* — assumes sticky prices; predicts a
  demand fall lowers output and prices, a supply shock raises prices and lowers output; tested: 2008–09 (demand), 1973–74 and
  2021–22 (supply, with demand in 2021); breaks: it does not say how long prices take, and expectations move the curves (g12-12).
- **Charts**: opening [A] `wdi("NY.GDP.MKTP.KD", isos=["USA"])` 1960–2024 against a log-linear trend fitted in the script
  (statsmodels allowed), log y axis, recessions shaded **[L]** from NBER dates (ledger table, see sync questions). Second [A]
  the output gap (percentage deviation from trend) as bars.
- **Diagrams**: AD–SRAS–LRAS with a demand shock; with a supply shock; the return to the long run (SRAS shifting).
- **Photographs**: none.
- **Boxes**: `model` ×2; `measure`[How a recession is dated] (NBER committee, ledger); `record`[2008–09];
  `record`[1973–74].
- **Exercises**: ★ read recessions on the chart ×2, output gap from numbers ×2, classify shocks; ★★ AD–AS equilibrium with lines ×2,
  P demand shock effects short and long run ×2, C trend growth from two points (log), R gap chart; ★★★ X evidence contradicting
  neutrality, a supply and a demand shock at once (2021), the adjustment path in three steps, why the trend is not potential
  output.
- **Problem**: *A drought in Kestria* — linear AD and SRAS; LRAS at potential; a supply shock; prices adjust 40 % of the gap a year;
  the path for five years. Named result: **the output gap in each of five years and the cumulative output lost**.
- **Ledger**: NBER business-cycle dates (the committee's page) as a ledger table; 1973 oil embargo dates; 2020 dates.

### g12-09 The Keynesian Cross and the Multiplier (`keynesian-cross`)
- **Programme**: T23, P20 (the demand effect of public spending against crowding out), PR the influence of policy on aggregate
  demand.
- **Sections**: 1 The consumption function (marginal propensity to consume); planned spending and equilibrium output; 2 The
  multiplier as a geometric series (proved), with taxes and imports; 3 A toy model, stated: fixed prices, a fixed interest rate,
  households that do not look ahead, idle capacity; what shrinks the multiplier: taxes, imports, the interest rate, expectations,
  full capacity; 4 Measured multipliers (`debate`); the large fixed multiplier taught as refuted.
- **Owns**: consumption function, marginal propensity to consume, autonomous spending, planned expenditure, spending multiplier,
  marginal propensity to import; the *Keynesian cross* indexed in its `model` box.
- **Recalls**: This book — national accounts (g10-11), AD–AS (g12-08), crowding out (g12-07). Mathematics — geometric series and
  their limit (g12).
- **Models**: *The Keynesian cross* — assumes fixed prices, a fixed interest rate, consumption tied to current income, idle
  capacity; predicts a multiplier 1/(1 − c(1 − t) + m); tested: measured multipliers are mostly between 0.6 and 1.5, higher in
  deep slumps and at the zero lower bound, lower with a floating rate and open trade (Ramey 2019, ledger); breaks: full capacity,
  monetary offset, forward-looking households; what the record refuted: a large, fixed multiplier.
- **Charts**: opening [L] the range of fiscal multipliers estimated by published studies (Ramey 2019 JEP tables, open access),
  as intervals by method. Second [I] the cross for Brenland's numbers.
- **Diagrams**: the 45° cross with planned expenditure; a spending rise and the multiplier steps; the leakage version.
- **Photographs**: none.
- **Boxes**: `model`; `debate`[How large is the government-spending multiplier?] (Ramey and Zubairy 2018; Nakamura and Steinsson
  2014 regional; Blanchard and Leigh 2013 forecast errors; Barro and Redlick 2011; each with its weakness).
- **Exercises**: ★ equilibrium output ×2, multiplier with c only, R opening chart ×2; ★★ multiplier with tax and imports ×2, P a
  spending rise and output, C geometric steps (three rounds), R the cross, P with monetary offset (zero); ★★★ X evidence
  contradicting a large fixed multiplier, a balanced-budget change in the toy model, a multiplier at full capacity (zero: prices
  rise), why open economies have smaller multipliers.
- **Problem**: *Brenland's stimulus* — c, t and m estimated from Brenland's accounts; a spending rise of 1 % of GDP; the toy-model
  output gain; then the same with the central bank raising rates (an offset given) and at full capacity. Named result: **the
  toy-model multiplier and the multiplier left once imports, taxes and the monetary offset are counted**.
- **Ledger**: Ramey (2019, JEP) table values; the `debate` studies' estimates.

### g12-10 Monetary Policy (`monetary-policy`)
- **Programme**: P23, T23, T24 (a single monetary policy for a currency union, the ECB's independence), PR the influence of
  monetary policy.
- **Sections**: 1 What a central bank aims at (inflation target, sometimes employment) and what it controls (the policy rate);
  2 From the policy rate to market rates, spending and the exchange rate; delays; 3 Rules and discretion (a Taylor-type rule as a
  description; time inconsistency; credibility and independence, with the evidence); 4 The record: the Volcker disinflation, the
  zero lower bound after 2008 (quantitative easing, forward guidance), 2021–23; 5 One policy for many countries (the euro area,
  told).
- **Owns**: inflation target, monetary transmission, policy lag, policy rule, Taylor rule (label), time inconsistency, central
  bank independence, credibility, zero lower bound, quantitative easing, forward guidance.
- **Recalls**: This book — policy rate, central bank (g11-13), quantity equation (g12-03), AD–AS (g12-08), real interest rate
  (g10-12).
- **Models**: *A Taylor rule* (as a description of policy) — assumes the bank reacts to inflation and the output gap; predicts
  the rate path; tested: fits the US 1987–2007 (Taylor 1993, ledger); breaks: the zero lower bound, 2021 (rates stayed low while
  inflation rose).
- **Charts**: opening [A] `jst(["USA"], 1965–2020)` stir and CPI inflation, `omtime`, extended to 2024 **[D]** with the Federal
  Reserve H.15 effective federal funds rate (public domain, to approve) and `bls_cpi` (approved) for inflation; fallback: JST to
  2020 and BLS inflation to 2025 with the rate path 2021–25 in a `dated` box from ledger rows. Second [A] the Taylor-rule rate
  computed from JST/WDI against the actual rate (script).
- **Diagrams**: the transmission chain (boxes and arrows); a time-inconsistency payoff table.
- **Photographs**: none.
- **Boxes**: `model`; `record`[The Volcker disinflation, 1979–83]; `record`[2021–23]; `debate` none; `dated{2026}`[policy rates
  and targets of three central banks, ledger]; `measure`[How a central bank sets an overnight rate] (corridor, told).
- **Exercises**: ★ read the opening chart ×2, a Taylor-rule rate ×2, real policy rate; ★★ rule-implied rate path ×2, P a rate rise
  through the chain, C a lag, R second chart, the zero bound case; ★★★ X evidence contradicting the rule (2021), the
  time-inconsistency game's equilibrium, independence and average inflation (a published cross-country result), one rate for two
  regions with different shocks.
- **Problem**: *Brenland's central bank* — `accounts.csv` policy_rate and CPI 2015–2025; potential output from a trend; a rule
  with given weights; the rule's path against the actual. Named result: **the gap between the rule's rate and the actual policy
  rate in 2022, and the inflation the rule would have reacted to**.
- **Ledger**: FOMC dates (October 1979), Fed target ranges 2022–23 (dated), ECB start (1999), Taylor (1993), Alesina and
  Summers (1993) result.

### g12-11 Fiscal Policy and Public Debt (`fiscal-policy-and-debt`)
- **Programme**: P20 (the budget balance, deficit financed by borrowing, demand effect against crowding out), T23, T24 (fiscal
  rules in a currency union, as a record), PR fiscal policy; Book 1 recall (ageing, for future spending).
- **Sections**: 1 Budget balance and primary balance; automatic stabilisers; 2 The debt ratio as a recurrence in the interest
  rate and the growth rate (b_{t+1} = (1+r)/(1+g) b_t − p, proved; its limit); 3 When a debt is sustainable (r < g, r > g); crowding
  out recalled; 4 Do households expect the future taxes (Ricardian equivalence, first look, with the evidence); 5 How large debts
  ended: growth, surpluses, inflation, default (records); "deficits don't matter" against the record; fiscal rules.
- **Owns**: primary balance, structural balance, automatic stabiliser, debt ratio, sustainable debt, Ricardian equivalence,
  sovereign default, fiscal rule.
- **Recalls**: Book 1 — budget, deficit and debt (g8), ageing (g6). This book — crowding out (g12-07), multiplier (g12-09),
  present value (g12-01). Mathematics — arithmetic-geometric sequences (g12).
- **Models**: *Debt dynamics* — an identity plus assumptions on r, g and the primary balance; predicts the debt ratio's path;
  tested: UK 1815–1914 and 1946–1975, US 1946–1980 (chart and problem); breaks: r and g are not independent of the debt (risk
  premia: Greece 2010–12). *Ricardian equivalence* — tested: saving responses to tax rebates are partial (Parker et al. 2013,
  ledger); breaks.
- **Charts**: opening [A] `jst(["GBR","USA"])` debtgdp 1870–2020 (checked; 150 years), `omtime`. Second [A] `eurostat
  ("gov_10dd_edpt1")` GD (debt) for euro-area countries 2000–2024, or B9 (net lending) for automatic stabilisers 2007–2010.
- **Diagrams**: the debt recurrence as a cobweb-type staircase (b_{t+1} against b_t, two cases r < g and r > g).
- **Photographs**: none.
- **Boxes**: `model` ×2; `record`[How the United Kingdom's debt fell after 1945]; `record`[Greece 2010–12]; `record`[A fiscal rule
  in a currency union] (the 3 % and 60 % rules, LAW, with the record of compliance).
- **Exercises**: ★ primary balance from totals ×2, R opening chart ×2, debt ratio next year; ★★ iterate the recurrence ×2, the
  stabilising primary balance, P a rise in r, R Eurostat chart, C automatic stabiliser size; ★★★ X evidence contradicting
  Ricardian equivalence, the limit of the recurrence (proved), inflation's effect on the ratio, a default's arithmetic.
- **Problem**: *How the United Kingdom's debt ratio fell, 1946–1975* — JST debtgdp, nominal growth, the long rate; the decomposition
  of the fall into growth, inflation and primary surpluses (a printed table from the chapter's script). Named result: **the share
  of the fall due to nominal growth above the interest rate**.
- **Ledger**: Treaty on the Functioning of the EU Protocol 12 (3 %, 60 %; LAW); Greek PSI date (March 2012) and haircut; Parker
  et al. (2013, AER); Reinhart–Rogoff list of how debts ended (a published table).

### g12-12 The Phillips Curve and Its Breakdown (`phillips-curve`)
- **Programme**: PR the short-run trade-off between inflation and unemployment; outline (refuted claims taught as refuted).
- **Sections**: 1 The relation seen in the 1950s and 1960s (chart); 2 The claim of a stable trade-off, and the stagflation of the
  1970s that refuted it; 3 Expectations: the expectations-augmented curve; the natural rate and no long-run trade-off (proved with
  adaptive expectations: a recurrence); 4 The cost of bringing inflation down (the sacrifice ratio, measured); 5 Anchored
  expectations; 2021–23.
- **Owns**: Phillips curve, stagflation, adaptive expectations, expectations-augmented Phillips curve, anchored expectations,
  disinflation, sacrifice ratio.
- **Recalls**: This book — natural rate of unemployment (g11-12), AD–AS (g12-08), monetary policy (g12-10).
- **Models**: *The stable Phillips trade-off* — assumes a fixed relation; predicts a menu of inflation and unemployment; tested
  and refuted: 1970–83 (chart). *The expectations-augmented Phillips curve* — assumes adaptive expectations and a natural rate;
  predicts no long-run trade-off and accelerating inflation if unemployment is held below the natural rate; tested: 1970s, Volcker;
  breaks: with anchored expectations the curve is flat (2010s), and supply shocks shift it (2021–22).
- **Charts**: opening [A] `jst(["USA"])` CPI inflation against unemp, 1960–69 and 1970–83 (checked values), connected scatter in
  two colours. Second [A] the same for 2015–2024 from `wdi("SL.UEM.TOTL.NE.ZS")` and `bls_cpi` (JST ends 2020, and its 2019 US
  unemployment value is wrong).
- **Diagrams**: short-run curves shifting up with expectations, the vertical long-run curve; the disinflation path.
- **Photographs**: none.
- **Boxes**: `model` ×2; `record`[Stagflation, 1973–82]; `record`[The Volcker disinflation and its cost]; `record`[2021–23].
- **Exercises**: ★ read the opening chart ×2, compute inflation from CPI, natural rate from the curve, a sacrifice ratio; ★★
  adaptive-expectations path ×2, P holding u below u^n for three years, C sacrifice ratio from US data, R second chart, anchored vs
  adaptive; ★★★ X evidence contradicting the stable trade-off (state it), a supply shock in the augmented curve, the limit of the
  path, why the 2010s curve looked flat.
- **Problem**: *The Volcker disinflation, 1979–1986* — US inflation and unemployment (JST table printed from the script); the
  natural rate given; cumulative unemployment above it; the sacrifice ratio. Named result: **the sacrifice ratio of the US
  disinflation, in point-years of unemployment per point of inflation**.
- **Ledger**: Phillips (1958) and Samuelson–Solow (1960) dates as dated facts (as the labels of the relation, not biography);
  Volcker's appointment (August 1979); Ball (1994) sacrifice-ratio estimates.

### g12-13 Trade beyond Ricardo, and Trade Policy (`trade-and-trade-policy`)
- **Programme**: T6 (factor endowments), T7 (trade between similar countries: variety, quality, value-chain fragmentation), T8
  (firm productivity and exports), T9 (value chains), T10 (gains, inequality between and within countries; free trade and
  protection, as evidence), T21 (the single market as a trade agreement, its measured effect), PR international trade.
- **Sections**: 1 Trade from different endowments, from scale and from variety (told; the Heckscher–Ohlin model as a label);
  value chains; exporters are the more productive firms (measured); 2 Winners and losers inside a country (the China shock,
  measured); 3 A tariff and a quota with surplus (small open economy; proved: DWL two triangles); 4 The arguments for protection,
  each with its evidence (infant industry, terms of trade, national security, anti-dumping) and the government-failure risk
  (recall g11-09); 5 Trade agreements, customs unions and the single market; `debate` on trade and wages.
- **Owns**: world price, small open economy, import quota, factor endowment, Heckscher–Ohlin model (label), intra-industry
  trade, global value chain, infant-industry argument, anti-dumping duty, trade agreement, customs union, single market.
- **Recalls**: Book 1 — exports, imports, tariff (g9), trade as a share of output (g6). This book — Ricardo's model, terms of
  trade (g10-03), surplus (g10-08), tax incidence (g10-10), rent seeking (g11-09).
- **Models**: *A tariff in a small open economy* — assumes a fixed world price; predicts a higher domestic price, a transfer, two
  DWL triangles; tested: the 2018 US tariffs passed almost fully into import prices (Amiti, Redding and Weinstein 2019;
  Fajgelbaum et al. 2020, ledger); breaks: a large country can shift part to foreigners. *The endowments model* — tested: the
  Leontief result and later factor-content tests (ledger); breaks: technology differs (Ricardo again).
- **Charts**: opening [A] `wdi("TM.TAX.MRCH.WM.AR.ZS")` for CHN, IND, BRA, MEX, KOR, USA, EUU 1988–2022 (checked: China 32 → 2,
  India 56 → 5). **[D, optional]** two centuries of US tariffs (USITC, public domain table) would restore the outline's chart.
  Second [L] Autor, Dorn and Hanson (2013) or a published summary: the employment effect of import exposure (a few numbers), or
  `gravity` intra-industry is impossible (no products): drop.
- **Diagrams**: tariff with domestic supply and demand, world price, the four areas; quota with the licence rent; a value chain
  (stages across countries).
- **Photographs**: one, a container port (Commons, CC BY-SA or PD, licence read at writing).
- **Boxes**: `model` ×2; `debate`[Trade and wages] (Autor, Dorn and Hanson 2013; Feenstra–Hanson; Krugman 2008; the gains to
  consumers, e.g. Fajgelbaum and Khandelwal 2016; each with its weakness); `record`[The 2018–19 US tariffs]; `record`[The single
  market, 1993] (a published estimate of its effect).
- **Exercises**: ★ domestic price and imports under a tariff ×2, R opening chart ×2, a quota rent; ★★ DWL of a tariff ×2, tariff
  versus quota, P a large country's tariff, C effective protection (told), C gains and losers' sizes; ★★★ X evidence contradicting
  full pass-through, the infant-industry condition (PV of future cost savings), endowments predict who loses, an anti-dumping
  duty and its rent seeking.
- **Problem**: *Kestria's tariff on cloth* — linear demand and supply, world price; a 20 % tariff; a quota with the same imports;
  the licence rent; a retaliatory tariff on Kestria's grain by Brenland. Named result: **the deadweight loss of the tariff and the
  net loss to Kestria after retaliation**.
- **Ledger**: Amiti et al. (2019, JEP), Fajgelbaum et al. (2020, QJE), Autor et al. (2013, AER), Leontief (1953) result, the
  single market date and one estimate; WTO founding (1995).

### g12-14 Exchange Rates and the Balance of Payments (`exchange-rates-and-balance-of-payments`)
- **Programme**: T21 and T24 (the euro area; one monetary policy, national fiscal policies; asymmetric shocks), PR open-economy
  concepts and theory.
- **Sections**: 1 The current account and the financial account (the balance of payments sums to zero); 2 Saving minus investment
  equals the current account (proved from the identities); 3 Purchasing-power parity as a long-run anchor; the real exchange rate;
  interest parity (first look); 4 Fixed and floating rates; the three aims that cannot all be met (told); a currency union as the
  hardest fix, asymmetric shocks; 5 Currency crises (first look: 1992, 1997, the record).
- **Owns**: balance of payments, current account, financial account, net foreign assets, purchasing-power parity, real exchange
  rate, currency appreciation, currency depreciation, interest parity, floating exchange rate, fixed exchange rate, currency
  union, impossible trinity, currency crisis, asymmetric shock.
- **Recalls**: Book 1 — exchange rate, purchasing-power conversion (g9), trade balance (g9). This book — national saving and
  investment (g12-07), monetary policy (g12-10).
- **Models**: *Purchasing-power parity* — assumes arbitrage in goods; predicts the real exchange rate returns to a constant;
  tested: deviations die out with a half-life of three to five years (Rogoff 1996, ledger); breaks: in the short run, and for
  non-traded goods (the price level rises with income: chart, PA.NUS.PRVT.PLI). *Uncovered interest parity* (first look) — tested:
  fails at short horizons (ledger).
- **Charts**: opening [A] `wdi("BN.CAB.XOKA.CD")` USA, CHN, JPN (from 1996), DEU, IND, GBR 1980–2024, billions of dollars.
  Second [A] `wdi("PA.NUS.PRVT.PLI")` against income per person (the price level rises with income), log x.
- **Diagrams**: the balance-of-payments T-table; the trilemma triangle; the real-exchange-rate path back to parity.
- **Photographs**: none.
- **Boxes**: `model` ×2; `record`[Sterling leaves the exchange-rate mechanism, 16 September 1992]; `record`[One currency, several
  economies: the euro area 2010–12] (ledger); `dated{2026}`[members of the euro area, ledger].
- **Exercises**: ★ BoP entries ×2, R opening chart ×2, a real exchange rate; ★★ S − I = CA from accounts ×2, P a depreciation's
  effect on import prices, C PPP rate, C interest-parity expected depreciation, R price-level chart; ★★★ X evidence contradicting
  PPP in the short run, the trilemma for three countries' choices, an asymmetric shock in a currency union with fixed wages, a
  crisis in a fixed peg (reserves run out).
- **Problem**: *Brenland's balance of payments* — `accounts.csv` and `trade.csv`: S − I, the current account, the dalen per kest
  rate, the real exchange rate with both CPIs (Kestria's CPI in a seeded table), PPP. Named result: **the real depreciation of the
  dalen against the kest, 2015–2025, and the current account it went with**.
- **Ledger**: Rogoff (1996, JEL) half-life; Black Wednesday date; euro members (dated); Asian crisis dates (July 1997);
  Obstfeld–Shambaugh–Taylor trilemma reference (prose).

### g12-15 Income and Wellbeing (`income-and-wellbeing`)
- **Programme**: S7 (GDP does not show inequality), PR (what income per person leaves out); outline (wellbeing theme).
- **Sections**: 1 Life satisfaction against income, across countries and inside them (how the question is asked); 2 A relation in
  the logarithm of income (the same gain for each doubling, proved from the fitted form); 3 What GDP leaves out, with numbers: free
  time, health, the distribution, nature; 4 Other indicators and how closely they follow income per person (life expectancy,
  schooling, a composite index); 5 What economics measures and what it does not (closing the book).
- **Owns**: life satisfaction, subjective wellbeing, composite indicator.
- **Recalls**: Book 1 — what GDP leaves out (g8), life expectancy (g6). This book — Gini (g11-11), national accounts (g10-11).
  Mathematics — logarithm (g12).
- **Models**: *Log-income model of life satisfaction* — assumes satisfaction rises with the logarithm of income; predicts the same
  gain per doubling at all incomes; tested: across countries and within them (Stevenson and Wolfers 2008; Deaton 2008, ledger);
  breaks: the time series of some countries (the Easterlin result, prose with both readings), and satiation findings at high
  incomes are disputed (Killingsworth 2021; Kahneman–Killingsworth–Mellers 2023, ledger).
- **Charts**: opening **[D]** average life satisfaction against income per person, log x: needs a licensed dataset (Eurostat
  ilc_pw01, CC BY 4.0, EU countries only — proposed; or the World Happiness Report tables, licence unclear). Fallback [A]
  `wdi("SP.DYN.LE00.IN")` against `wdi("NY.GDP.PCAP.PP.KD")` (other indicators against income), and the life-satisfaction
  relation in prose from ledger rows. Second [A] hours worked per worker (`pwt` avh) against income per person: free time rises
  with income.
- **Diagrams**: the log relation (same rise for each doubling) on linear and log axes.
- **Photographs**: none.
- **Boxes**: `model`; `measure`[How life satisfaction is measured]; `debate` none (Year 3 owns the open question); a closing
  remark.
- **Exercises**: ★ read the opening chart ×2, a doubling's effect, GDP per person against free time, an index from three
  indicators; ★★ fit of the log model from two points ×2, P a 10 % rise in income, C a composite indicator's weights change the
  ranking, R the hours chart, C value of leisure; ★★★ X evidence contradicting the log model, why a cross-country slope is not a
  causal effect, adjusting GDP for leisure, inequality-adjusted comparison of two countries.
- **Problem**: *Five countries, one ladder* — a seeded table of five invented countries' income, hours, life expectancy and mean
  satisfaction; fit the log model; rank by three indicators. Named result: **the satisfaction gain per doubling of income, and the
  income gain that would match one more year of life expectancy under the fitted indices**.
- **Ledger**: Stevenson and Wolfers (2008, BPEA), Deaton (2008, JEP), Killingsworth (2021, PNAS), Kahneman, Killingsworth and
  Mellers (2023, PNAS), Easterlin (1974) as a dated label.

---

## Programme coverage

Checked against the official texts (2026-11-20): the seconde SES programme (eduscol annex, BO spécial n°1 of 22 January 2019),
the première spécialité SES programme (same BO), the terminale spécialité SES programme (BO spécial n°8 of 25 July 2019), all
read at eduscol.education.gouv.fr. The international principles sequence is checked against the standard two-semester
principles table of contents (micro: ten principles → factor markets, inequality, consumer choice, frontiers; macro: national
income → open-economy theory, AD–AS, the Phillips curve); a publisher page could not be read, so this list is from the standard
sequence, to recheck if the sync wants a cited page.

| Code | Item (economics only) | Chapter(s) |
|---|---|---|
| S1 | economists use data and models; correlation and causation | g10-01 |
| S2 | diversity of producers; market and non-market production | g10-11 |
| S3 | production combines labour, capital, technology, natural resources | Book 1 g8; g12-04 |
| S4 | firm indicators (turnover, value added, profit) | Book 1 g7–g8; g10-11 |
| S5 | GDP as the sum of value added | Book 1 g8; g10-11 |
| S6 | growth as the change in GDP; long-run world trends | Book 1 g6, g8; g12-04 |
| S7 | GDP does not show income inequality | g10-11, g11-11, g12-15 |
| S8 | ecological limits of growth | g11-06, g12-06 |
| S9–S11 | the market; demand falls and supply rises with price; equilibrium and its graph | g10-04, g10-05, g10-06 |
| S12 | the effect of a tax or a subsidy on equilibrium | g10-10 |
| S13 | schooling as human capital; returns; qualification and unemployment; wage by education, experience, firm, gender | g11-10, g11-12 |
| P1 | the market as an institution; degrees of competition | g10-09, g11-03–g11-05 |
| P2–P3 | supply and demand curves, slopes, shifts, a per-unit tax with numbers | g10-04–g10-06, g10-10 |
| P4 | supply from profit maximisation; P = MC | g11-01, g11-03 |
| P5–P6 | producer and consumer surplus; gains from exchange; surplus maximised at equilibrium | g10-08 |
| P7–P9 | sources of market power; monopoly; its inefficiency | g11-04, g11-05 |
| P10 | oligopoly and the prisoner's dilemma | g11-05 |
| P11 | competition policy (mergers, cartels, abuse of dominance) | **added sections** in g11-04 and g11-05 (not in the outline's descriptions) |
| P12–P15 | externalities; commons and public goods; adverse selection and moral hazard; public intervention | g11-06–g11-09 |
| P16–P20 | financing needs and capacities; interest rate on loanable funds; household saving; gross operating surplus, self-financing, loans, shares, bonds; budget balance, deficit, crowding out | g12-07, g12-11 |
| P21–P23 | functions of money (Book 1); credit creates money; the central bank steers the short rate | g11-13, g12-10 |
| P24–P28 | risks, attitudes to risk, risk sharing and moral hazard, prevention, pooling, diversification, institutions, social insurance and assistance | g12-02 |
| P29 | firms: life cycle, entrepreneurs, governance | Book 1 g7 (life cycle); g11-08 (owners and managers); **rest dropped** (management and sociology) |
| T1–T5 | growth sources, TFP; endogenous innovation; institutions and property rights; creative destruction; technical progress and inequality; ecological limits | g12-04, g12-06, g11-11 |
| T6–T10 | endowments and technology; trade between similar countries; firm productivity and exports; value chains; effects of trade; free trade and protection | g10-03, g12-13 |
| T11–T15 | unemployment and underemployment; matching; efficiency wages; minimum wage and employment protection; cyclical unemployment; the main policies | g11-10, g11-12, g12-08 |
| T16–T20 | the 1930s and 2008 crises; bubbles; bank panics; transmission to the real economy; supervision and capital ratios | **no chapter of its own**: `record` boxes and sections in g11-13, g12-07, g12-08 |
| T21–T24 | European integration (single market, euro area); competition policy; monetary and fiscal policy and the cycle; one monetary policy, national budgets, asymmetric shocks | **no chapter of its own**: sections in g12-13 (single market), g12-14 (currency union), g12-10, g12-11 (fiscal rules), g11-04/05 (competition policy) |
| T25–T26 | inequality trends since 1900; inter-quantile ratio, Lorenz, Gini, top 1 %, parent–child correlation | g11-11 |
| T27 | conceptions of social justice (utilitarianism, libertarianism, liberal egalitarianism, strict egalitarianism) | **dropped** (normative philosophy; the series teaches no normative debate) |
| T28 | public action against inequality under a financing constraint; efficiency and disincentives | g11-11 (measured redistribution), g10-10 (DWL), g11-10 (labour supply); the rest is Year 3's |
| T29–T30 | environmental actors and agenda-setting; scales of action | **dropped** (political science), except international agreements |
| T31–T32 | instruments against a climate externality; free riding in international agreements | g11-06, g11-07, g11-09 |
| Methods | proportions, rates of change, multiplier coefficient, simple and composite index, weighted mean, median, nominal and real (interest rates), two-way tables, distribution and time-series charts, supply/demand/cost graphs, inter-quantile ratio, Gini, correlation and causality, average rate of change, mobility tables, Lorenz | throughout; g10-01, g10-12, g11-11, g12-04 |
| PR | the two-semester principles sequence | all chapters; **consumer choice theory** (budget line, indifference curves) is left to Year 1, which owns the consumer; **design of the tax system** (efficiency and equity) is covered by g10-10, g11-01 (marginal and average rates) and g11-11 (progressivity) |

**Items no chapter covers as a whole** (proposed handling, no change to the chapter list): competition policy (sections in
g11-04, g11-05); financial crises 1930s and 2008 (sections and records in g11-13, g12-07, g12-08); European integration and the
euro area (sections in g12-10, g12-11, g12-13, g12-14); creative destruction (g12-06). Dropped as non-economics: conceptions of
justice, environmental agenda-setting, firm governance as sociology, socially differentiated access to schooling (only its
measurable part, intergenerational mobility, stays in g11-11).

## Questions for the sync (copied into the Phase A report)

1. **Ledger tables.** Several opening charts can only come from a published table (FDA generic prices, RAND HIE spending, GAO
   sugar, BLS *Education pays*, Ramey's multipliers, Brynjolfsson et al.'s digital goods, Liberty ships, NBER recession dates).
   Proposed mechanism: `figdata/<year>/NN-slug/src/<name>.csv`, transcribed from a published **table** (never digitised from a
   figure), one row per value with its ledger id in a column; the chapter's `make_<name>.py` reads it, writes `out/<name>.csv`, and
   its test checks every ledger id exists in `sources/ledger/book2.md` and that the values equal the ledger rows' value cells.
2. **Recession shading and dated guides** on a time chart (NBER dates, a law's date): through the same ledger-table route.
3. **Data to approve** (in the report).
4. **EIA INTL re-derivation**: crude oil production and petroleum consumption by country, from the INTL.zip already downloaded
   (a `tools/derive_data.py` change, main session; no download).
