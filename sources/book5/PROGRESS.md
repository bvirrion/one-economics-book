# Book 5 (University Year 3, `bachelor-3`) --- progress

## State

- **2026-11-20, Phase A done**; sync read (S1--S5, R1, R3); `DEFINITIONS.md` updated to the rulings (drops and owned
  terms listed in its header; remaining contested flags resolved: conditional convergence, infant-industry argument,
  fiscal rule, VAT recalled; Hotelling model, FDI, discrimination kept).
- **Ch. 01 `instrumental-variables` written and gated (2026-11-20).** Pages: 20 in the chapter (book pp. 2--21) plus
  4 of solutions. Build 0/0/0; `gates.sh bachelor-3` OK; `figdata.sh` OK; `test_code.sh bachelor-3` GREEN.
  - Charts (3): opening = first stage of the geographic instrument, 2019, 157 countries (CEPII Gravity BACI +
    `distw_harmonic`, contig, populations; WDI NE.TRD.GNFS.ZS; PWT coverage); 2SLS sampling densities at F = 2/10/50
    [simulated]; size of a nominal 5 % t-test against F [simulated]. The planned second-stage chart was dropped (the
    2SLS slope with a population control is not the bivariate slope of a plot).
  - Diagrams (3): causal graph z -> x -> y with u; supply/demand with a supply shifter (intersections computed);
    2x2 compliance types.
  - Listings (6, all captured): `schooling_data.py` (NORUN module), `ability_bias.py`, `tsls_by_hand.py`, `weak_iv.py`,
    `late_sim.py`, `geography_iv.py` (\omcodes, two ranges). Exercise solutions: `ex08_no_population.py`,
    `ex10_weak_f5.py`. Tests: 10 (chapter) + 5 (`code/bachelor-3/lib/tests/test_ivtools.py`, against statsmodels
    OLS/IV2SLS/f_test).
  - Ledger rows (8): `b3iv:ak91.panelA/B`, `b3iv:bjb95.t1/t3`, `b3iv:sy.rule`, `b3iv:sy.crit`, `b3iv:lmmp22.tf`,
    `b3iv:mss04.conflict` (all from printed tables or abstracts; AK, BJB and Stock--Yogo read from the PDFs).
  - Changes from the brief: weekend problem renamed "The Brenland college lottery" (Brenland, not Brenmoor); the
    geography uses population-weighted distance (`distw_harmonic`), because capital-to-capital distance makes
    Congo--Kinshasa explode the built share; the 2019 refit gives first-stage F 35.4 (16.7 without population) and
    2SLS 0.428 (0.382) against OLS 0.866 --- reported as such, in a `debate` box with Frankel--Romer, Rodriguez--Rodrik,
    Feyrer 2019 and Donaldson 2018 (no numbers cited from them). A `notation` box declares $\pi$, $\ell$, $W$, $D_i$,
    $s$ (series-notation clashes).
  - Deleted (single named file, 17:20): `code/bachelor-3/lib/econdata.py`, the shim I had added because
    `tools/capture_output.py` lacked `figdata/lib` on PYTHONPATH; the main session fixed the tool at 17:15. Outputs
    recaptured byte-identical; `test_code.sh bachelor-3` GREEN.
- **Length budget (main session, 17:15)**: ch. 1 may stay at 20 + 4 pp; from ch. 2, 14--16 pp of body. Keep one
  worked example per idea, move secondary derivations to exercises. Running page total at ch. 10 and ch. 20.
- **Ch. 02 `panel-data` written and gated (2026-11-20).** 12 pp of body (book pp. 22--33) + 3 pp of solutions.
  Build 0/0/0, gates, figdata and test_code green.
  - Charts (2): opening = two panels (groupplot) of CO2 per person against GDP per person, between (200 country means)
    and within (20 bins of deviations), WDI 1990--2022, 6,419 country-years; Nickell bias against T [simulated].
  - Diagrams (1): three units with parallel slopes and a steeper pooled line. (The planned cluster-structure sketch and
    the two-country chart were cut for the length budget.)
  - Listings (3): `pooled_vs_within.py` (WDI; pooled 2.756, between 2.716, within = dummies 0.999, two-way 2.068,
    within share of income variance 3.6 %), `random_effects.py`, `cluster_sim.py` (placebo laws: iid 0.396, cluster
    0.066). Exercise solutions: `ex05_year_effects.py`, `ex09_fertility.py`, `ex11_nickell.py`. New lib
    `paneltools.py` (demean, twoway_demean, ols_cluster) with 3 tests against statsmodels.
  - Weekend problem: invented Brenland firm panel generated and estimated in `figdata/.../make_firms.py` (tested),
    typeset with `pgfplotstable` from `out/firms_results.csv`.
  - Ledger: `b3pd:bdm04.placebo`.
  - Fix in ch. 1 as well: fitted lines inside `omscatter` axes need `sharp plot` (the style's `only marks` hid them).
- **Ch. 03 `difference-in-differences` written and gated (2026-11-20).** 13 pp of body (book pp. 34--46) + 4 pp
  of solutions. Build 0/0/0, gates, figdata and test_code green; every figure page checked rendered.
  - Charts (3): opening = Card--Krueger Table 3 means via `cited.py` (`src/ck.csv`, ledger `b3did:ck94.t3`) with the
    parallel-trends counterfactual (our arithmetic: DiD 2.75 from printed means, paper 2.76 from unrounded, both stated);
    event study on a simulated staggered roll-out [S]; synthetic control on a simulated region [S].
  - Diagram (1): the forbidden comparison timeline. (The four-point DiD diagram is merged into the opening chart.)
  - Listings (4): `did_nsw.py` (NSW trainees vs CPS: DiD 3,621 = OLS interaction), `lalonde_benchmark.py`
    (experiment 1,794; CPS/PSID x four estimators), `bacon.py` (truth 4.286, TWFE 2.547, clean 4.243), `synth_demo.py`.
    New lib `synth.py` (SLSQP over the simplex) with 2 tests. Exercises: `ex06_placebo_1974.py`, `ex10_anticipation.py`.
  - Weekend problem: invented Kestrian provinces panel (`make_kestria.py`, tested), five tables via `pgfplotstable`.
  - Ledger: CK1994 (`ck94.t3`, `ck94.design`), ADH2015 (`adh15.effect`, `adh15.weights`, `adh15.placebo`; units per
    the 2025 erratum). Brief changes: the `did_regression` and `event_study` listings were folded into `did_nsw.py` and
    the figdata chart for length; LaLonde's chart became a listing.
  - USGS DS 140 dropped (user ruling 2026-11-20): ch. 35 brief rewritten to cited tables / EKC; no `PENDING-DATA: USGS`
    stub existed in the text.
- **Ch. 04 `regression-discontinuity` written and gated (2026-11-20).** 12 pp of body (book pp. 57--68) + 3 pp of
  solutions. Build 0/0/0, gates, figdata and test_code green; figure pages checked rendered.
  - Charts (4, all [S]): opening = simulated close elections calibrated on Lee 2008's 0.077 (ledger `b3rd:lee08.vote`);
    estimates against the window (300 samples); Maimonides' rule and simulated schools (rule from ALLS 2019 eq. 1);
    exam-score histogram with re-marking.
  - Diagram (1): sharp vs fuzzy probability of treatment. (The triangular-window diagram was cut for length.)
  - Listings (4 + NORUN `elections.py`): `rd_sharp.py` (incl. the balance test; brief's `balance.py` folded in),
    `rd_bandwidth.py`, `rd_fuzzy.py`, `density_test.py`. New lib `rdtools.py` (local_linear, density_test) with 3 tests.
    Exercises: `ex05_global_polynomial.py`, `ex08_donut.py`, `ex11_coverage.py` (the chapter's conftest adds `listings/`
    to the subprocess PYTHONPATH so exercises can import `elections`).
  - Weekend problem: invented Brenmoor scholarship (`make_scholarship.py`, tested), table typeset from strings.
  - Ledger: Lee2008, CD2009 (NBER abstract: 21 % drinking days, 9 % mortality), AL1999 (abstract, qualitative),
    ALLS2019 (rule, redux finding). The Redux authors judge the enrolment sorting innocuous; the record box says so.
  - Two rounding traps handled: opening jump quoted at 4 decimals (0.5353 - 0.4597 = 0.0756); Wald -0.289 printed vs
    -0.288 from rounded numbers, both stated.
- **Ch. 05 `binary-outcomes`: DONE** (12 pp, PDF pp. 69-80). New lib `code/bachelor-3/lib/choicetools.py`
  (`logit_newton`, `clogit`; tests match statsmodels Logit / ConditionalLogit). Listings `lpm_logit_probit`,
  `newton_logit`, `travel_mode` (statsmodels `modechoice`, 210 travellers, VOT $17.2/h), `logit_demand` (simulated,
  log-share inversion, IIA cross elasticities). Exercises `ex05_zero_earnings`, `ex11_endogenous_price`.
  figdata: `make_work` (opening chart: all three fits miss the zero earners, 0.438 vs 0.665-0.704), `make_loglik`
  (Newton steps), `make_commuters` (invented Brenmoor problem, seed 2026: VOT 10.1 binary / 13.1 three-way dalens/h,
  express forecast 0.297). Ledger McF2001 `b3bo:mcf.bart`. Fetches +2 (McFadden PDF; nobelprize 403), searches +1.
- **Ch. 06 `credible-empirical-work`: DONE** (14 pp, PDF pp. 82-95). Opening chart SIMULATED (significance filter;
  Book 4 ch. 5 uses Camerer 2016, so the Camerer counts go in a record box citing Book 4's row `b2:camerer2016`).
  New lib `code/bachelor-3/lib/metatools.py` (power, filtered_mean, fixed_effect, dersimonian_laird, fat_pet; tests vs
  simulation and statsmodels WLS). Listings `significance_filter`, `forking_paths`, `funnel`, `reading_table` (NSW
  experiment, summary_col). Exercises `ex06_fat_pet`, `ex11_random_effects`. figdata `make_filter`,
  `make_exaggeration`, `make_funnel` (same draws as the listing, tested), `make_studies` (Brenland problem, seed 2027).
  Ledger: CL2015 (brief was wrong: 29 of 59 is WITH author help; 22 of 67 without), ISD2017, BLSZ2016, AEARCT.
  Evidence scale printed as `def:b3:credible-empirical-work:evidence-scale`. Fetches +4 (FEDS PDF, OUP page useless,
  RePEc ISD, RePEc Brodeur, registry about = 5), searches +1.
- **Ch. 07 `ricardian-trade`: DONE** (10 pp, PDF pp. 96-105; short of the budget, nothing padded). Opening chart:
  Bernhofen-Brown 2004 has no per-good table (only Fig. 4, not to be read), so the opening chart is their Table 2
  (inner product by year 1868-75, cited via `src/japan.csv`); ledger BB2004 (t1, t2.<year>, surplus, ryo), BB2005
  (gains <= 8-9 % of GDP), CD2012, GH2000. MacDougall 1951 not verifiable (JSTOR only): dropped, the productivity
  record uses Golub-Hsieh. FAOSTAT chart: wheat/maize relative yield vs relative area, 73 countries, corr -0.30
  (NEGATIVE: selection of land; text says so and why potential yields are needed). DFS chart simulated (seed 1977).
  Problem: `twelve.py` solver + `make_twelve.py` (cloth/grain from ricardo.csv, 10 goods added). No listings; code dir
  has `exercises/ex08_crops.py` only. Photo of Yokohama not added. Fetches +5, searches +3.
- **Ch. 08 `factor-endowments`: DONE** (10 pp, PDF pp. 107-116). Opening chart PWT 2019 shares of world capital /
  workers / output, 12 largest (dot plot); chart 2 PWT output vs capital per worker (slope 0.76, median capital share
  0.48 from labsh). Leontief 1953 numbers NOT verifiable (JSTOR only; secondary PDFs unreadable): no Leontief record,
  the tests record uses BLS 1987, Trefler 1995, Davis-Weinstein (NBER WP 6785 abstract). Magee 1980 via MIT OCW
  14.581 notes (19 of 21 industries) as a secondary source. Problem `make_boom.py` (fixed coefficients; HOV exact).
  Exercises code: `ex08_factor_content`, `ex11_hov_sign`. Fetches +9 (Trefler, DW x2, BLS, Leamer, iioa, Springer,
  MIT notes, DW NBER), searches +2.
- **Ch. 09 `scale-variety-firms`: DONE** (11 pp, PDF pp. 117-127). Opening chart BJRS 2007 Table 2 (21 industries,
  cited table `src/exporters.csv`, NBER w13054 text); exporter premia Table 3 in prose. Records: Trefler 2004 (NBER
  abstract), Broda-Weinstein (working-paper 2.8 % of GDP, said so in print), Pavcnik (qualitative), HMY (38 countries,
  52 sectors). Charts: home-market effect (model), Melitz revenues before/after (10,000 simulated entrants); diagram:
  productivity line. Listing `melitz_selection.py`; exercises `ex07_cutoff`, `ex11_industry_productivity`. Ex. 12 uses a
  fall in tau (the fixed-cost cut is the problem's Part III). Problem from `make_boom_firms.py` (sigma 3, k 4,
  f 40, f_e 2.5, tau 1.2, f_x 90 -> 45): agreement raises average productivity 4.1 %, 15.0 % of producers exit.
  Fetches +6, searches +1.
- **Ch. 10 `gravity`: DONE** (11 pp, PDF pp. 128-138). CEPII Gravity (BACI, positive flows only: the derived file has
  no zeros, so zeros are counted as absent pairs among the countries recorded each year, and PPML runs on positive
  flows; said in print). Listings `load_trade`, `gravity_ols`, `gravity_fe`, `gravity_ppml` (statsmodels formulas,
  C() dummies, 440 parameters; PPML ~15 s). Charts: opening binned scatter (50 bins, slope 1.18, R2 0.62), distance
  elasticity 1996-2020 every 4 years (OLS FE and PPML; figdata ~4 min with the determinism rerun), zero share, JST
  trade/GDP waves (13-18 economies, unweighted). Diagram: multilateral resistance. Records: Head-Mayer Tables 4-5
  (CEPII WP 2013-27 text), AvW abstract (McCallum 22, 44 %), Disdier-Head abstract, BEK container (GEP WP, ~700 %).
  No container photo (licence work skipped for budget). Exercises code ex05/06/10/12. Problem: invented 20-country
  world (`world.py`, structural gravity with border 1.5, union 0.5, noise falling with size; `make_union.py`); named
  result: Brenland's trade with members +27.0 %, non-members -10.5 % (PPML coefficients, resistance re-solved).
  Fetches +7 (Head-Mayer, AvW, Disdier-Head, BEK x1 + 1 search, BJRS-style PDF), searches +1.
- **Running page total at ch. 10:** chapters 1-10 occupy PDF pp. 13-138 (126 pp with the two part pages: about 12.4 pp
  per chapter); the whole PDF is now 204 pp with 26 stub chapters and the solutions of ch. 1-10. Under budget (14-16).
- **Ch. 11 `trade-policy`: DONE** (10 pp, PDF pp. 139-148). Opening chart WDI TM.TAX.MRCH.WM.AR.ZS, six economies,
  log scale; the U.S. 2019 value 13.78 (primary products 80.1) is a source-series break, dropped and said so in the
  caption (`out/tariffs_dropped.csv`). The [L] pass-through chart was dropped: the abstracts give "complete" / "almost
  fully", no coefficients to chart; the manufactures-vs-primary chart dropped for budget. Diagrams: large-country
  tariff (problem's lines), tariff game (payoff cells). Records: 2018-19 tariffs (ARW, FGKK, CGNT abstracts),
  infant industries (Juhasz); debate Trade and wages (ADH grade 2 with BHJ/GPSS, DFS grade 2, CDP grade 4; Krugman
  2008 and Feenstra et al. not used). Smoot-Hawley not printed (no source fetched). Problem `steel.py`/`make_steel.py`:
  +59.3 without retaliation, -18.6 with (million dalens); optimal tariff 40 % = 1/eps* (2.5). Exercises code ex08
  (WDI cuts), ex12 (shift-share). Fetches +9, searches 0.
- **Ch. 12 `current-account`: DONE** (10 pp, PDF pp. 149-158). Opening chart WDI current accounts / world GDP (USA,
  CHN, DEU, JPN from 1996, all others, sum = world discrepancy); FH scatter (122 countries, slope 0.22); sudden stops
  (MEX 1994, THA 1997, GRC 2010); Lucas scatter with quintile medians + PWT 2019 calculation (7.18 -> 19.2 with
  alpha 0.4; Lucas's 58 quoted via AKV 2008). Feldstein-Horioka 1980 original not readable (scanned PDF): the
  retention figure is Feldstein 1982's 85 cents (17 OECD, 1974-79), stated as such; the brief's "0.89" not printed.
  Glick-Rogoff, Calvo 1998, Obstfeld-Rogoff not fetched, not cited. Skipped: BoP T-account diagram and the sudden-stop
  constraint diagram (budget). Problem `make_borrow.py`: Brenland's net debt 45,000 at end-1999, interest = policy rate
  + 1; named result 0.40 % of GDP (2.0 % in a sudden stop). Exercises code ex07 (FH by period), ex12 (reversals).
  Fetches +6, searches +2.
- **Ch. 13 `exchange-rates`: DONE** (9 pp, PDF pp. 159-167). Opening chart WDI PLI vs PPP income 2023 (197
  countries, slope 0.20); JST real rates of five economies 1870-2020 and half-lives of 17 (median 5.5 / 2.5 years);
  UIP pooled regression 1974-2019 (slope -0.10, 782 obs). Ledger: Rogoff 1996 (read in full: half-life consensus,
  volatility, Japan), Meese-Rogoff 1983 abstract (PDF text), Burnside et al., Eichenbaum-Evans, Du-Tepper-Verdelhan
  (abstracts). Fama 1984, Balassa 1964, Samuelson 1964, Dornbusch 1976 and ICP 2021 not fetched: the regression is
  called the UIP regression, the B-S result is named only, the ICP is described generically (no figure). Chart (4)
  forecast errors and the CIP loop diagram skipped (budget). Dornbusch drawn as time paths, not a phase diagram.
  Problem `dalen.py`/`make_dalen.py`: Kestrian inflation 2.7 %, rate 3.0 % (assumptions); half-life 13.0 years,
  overshoot 9.0 points; the PPP forecast rule is given realised inflation, said in the problem. Exercises code ex05
  (half-lives), ex08 (UIP by country). Fetches +7, searches +2.
- **Ch. 14 `exchange-rate-regimes`: DONE** (11 pp, PDF pp. 168-178). Opening chart JST peg share, 18 economies (the
  brief's "seventeen" corrected: the database has 18 with peg data); trilemma test from JST peg_type/peg_base: slopes by
  era (1999-2020 pegs 0.91, floats 0.45; Bretton Woods pegs 0.28 = capital controls); euro-area HICP 1999-2015 (Eurostat);
  first-generation model in levels (`attack.py`: T = R0/mu - c/k) charted with the problem's numbers. Records: ERM 1992
  (BoE QB 1992 Q4: no 12 %/15 % rate claims, only what the page says), Asian crisis (WDI rates and growth only),
  euro `dated{2026}` (ECB press release: 21 states, Bulgaria), Argentina (InfoLEG law dates + WDI rate/growth; the
  1:1 rate is shown from WDI, not from the law text). Krugman 1979 and Mundell 1961 not cited by year (not fetched).
  Second-generation game in the text, OCA schematic. Problem: attack in year 8, board needs 120 bn dalens (4x
  reserves). Exercises code ex05 (trilemma by era), ex08 (Greece-Germany HICP). Fetches +6, searches +2.
- **Ch. 15 `central-banking`: DONE** (pages to confirm at the next build). Opening chart Fed H.4.1 and Eurosystem total
  assets over GDP (WDI, Eurostat EA) 2003-2025, ratios stated as ours; BoJ and BoE dropped (no approved data). Chart of
  fed funds and 10-year (H.15); inflation US CPI-U and EA HICP 2019-2025. The ECB corridor chart was dropped (would need
  ~45 ledger rows); six ECB key-rate rows in the ledger instead. Gagnon et al.: the SR 441 abstract has no basis-point
  figure, so the brief's "about 90 bp" is not printed. Debate 2021-23: Bernanke-Blanchard, Jorda et al., Shapiro,
  Benigno-Eggertsson (di Giovanni et al. not fetched). Jorda 2005 not cited (local projection defined only). Photo
  skipped. Problem `bank.py`: rule rate 15.3 % in 2022, NII -7.2 bn dalens. Exercise code ex08 (inflation peaks).
  Fetches +12, searches 0.
- **Ch. 16 `inflation-evidence`: DONE** (pages at the next build). Opening chart JST cpi, five economies, 1870 = 1, log
  scale (Germany left out: the 1923 break); money growth against inflation, WDI 146 countries 1990-2024 (slope 0.96);
  inflation around target adoption, Roger 2010 table (26 targeters, cited csv) with WDI; US ten-year breakeven from H.15
  nominal minus TIPS yields. Records: Germany 1923 and the four big inflations from the Sargent 1982 PDF text. Sargent-
  Wallace cited by title page only; Ball 1994 abstract. Hanke-Krus (Cato 403) and Fischer-Sahay-Vegh not fetched, so no
  hyperinflation table and no "50 % a month" source line (the definition is Y1's). Problem `cagan.py`: A = 20, alpha = 2,
  deficit 3 %: mu 0.245 (27.7 % a year), remonetisation 7.7 % of GDP. Exercise code ex06 (JST decades), ex11 (DiD).
  Fetches +7, searches +2.
- **Ch. 17 `efficiency-cost-of-taxation`: DONE** (pages at the next build). Opening chart JST central-government revenue
  over GDP, six economies; WDI revenue composition 1972/2024, five economies (stacked bars); analytic Laffer curve, a = 1.5.
  The problem's named result is on the **upper bands** (income above 40,000) rather than the 45 % top band, which has
  only 4 of 2,000 households: MCPF 2.17 at e = 0.25 (past the peak at e = 0.5). The VAT rate (18 %) and its MCPF (1.25)
  are problem assumptions. HMRC 2012 and the OBR box refused fetches: the UK 50p record is from the IFS BN214 PDF text.
  Kleven-Schultz and Saez-Slemrod-Giertz abstracts carry no numbers, so the brief's "0.12-0.40" is not printed. Sweden
  1991 record skipped (no source fetched). Diagrams: Harberger triangle, payroll wedge (the MEB two-triangle figure folded
  into the caption). Exercise code ex08 (composition 1990-2024). Fetches +12, searches +2.
- **Ch. 18 `transfers-and-incentives`: DONE** (pages at the next build). Opening chart: marginal effective tax rate of a
  single parent of two, U.S. 2024, from Rev. Proc. 2023-34, the 2024 Schedule 8812 instructions, the IRS CP08 page
  (CTC 2,000 for 2024; the current statute and the IRS CTC page give 2,200, the 2025 amount) and Topic 751; SNAP and state
  taxes left out (said in the caption; the SSA page refused). Chart 2 is Brenland's budget line before/after the
  problem's reform (the U.S. net-income line is not drawn). Gini chart dropped (no approved pre/post data); the
  redistribution section uses Brenland's survey and says why WDI Ginis cannot separate the two. Records: NIT experiments
  from an MSU summary of Robins 1985 ("roughly two weeks" etc., no per-year unit claimed), Finland from the STM press
  release, the 1987 EITC expansion from Eissa-Liebman (1.4 points, not the brief's 2.8). Saez 2002 not cited: the
  participation result is shown with a two-type example. Hendren-Sprung-Keyser not used. Problem: the support cliff at
  12,000 (rebuilt exactly from `country`), PTR at 15,000 64 % -> 40.7 %, 860 dalens a household. Exercise code ex08 (one
  child), ex12 (Gini). Fetches +10, searches +3.
- **Ch. 19 `social-insurance`: DONE** (pages at the next build). Opening chart: weeks per week of entitlement from four
  abstracts (Katz-Meyer 0.16-0.20, Lalive 0.09/0.32, Johnston-Mas 0.3/0.5; cited csv); Moffitt, Card-Levine, Card et al.
  2015 not fetched (one wrong NBER number). Chart 2 WDI old-age dependency, six economies. RAND from the JEP abstract;
  Oregon first year (NBER abstract) and two-year clinical results (MSU summary; PubMed refused). Disability record:
  Autor-Duggan. Problem `fund.py`: drop(r) = 0.24 - 0.28 r, gamma 3, eps 0.4 (assumptions); r* 35 % by the approximate
  formula, 46 % exact. The hazard-spike sketch and the two-state diagram skipped (budget); fund_curve.csv is written but
  not charted. Exercise code ex08 (ageing, countries of 1 m+), ex12 (simulated age RD). Fetches +11, searches +2.
- **Ch. 20 `cost-benefit-analysis`: DONE** (8 pp, printed 211-218). Opening chart: Flyvbjerg-Holm-Buhl 2002 Tables 1-2
  (arXiv accepted manuscript), overrun by type and region, cited csv; the brief's named-project audit chart (8-10 audit
  sources) dropped for budget. PV chart analytic. VSL: Viscusi-Aldy abstract (no dollar range printed); U.S. DOT page
  refused, OMB A-4 2023 status uncertain (a rescission was reported), Green Book page gave no numbers: the `dated` box of
  agency rates and values is dropped and the chapter names no agency number. Contingent valuation as a `debate`
  (Hausman 2012 vs Carson 2012 abstracts). Channel Tunnel record skipped (Anguera not fetched). Weitzman two-state
  result proved (not cited by name). Problem `bridge.py`: NPV 165 at 3.5 % (IRR 5.9 %); after the 33.8 % fixed-link
  correction 34.7 (IRR 3.9 %); with an MCPF of 1.3 it fails. Exercise code ex11 (hedonic regression with an omitted
  attribute). Ledger ids of this chapter use the prefix `b3ca:` (shared with ch. 12; ids unique). Fetches +7, searches +2.
- **Pages of ch. 15-19** (printed): ch. 15 168-176 (9), ch. 16 177-185 (9), ch. 17 186-195 (10), ch. 18 196-203 (8),
  ch. 19 204-210 (7). Printed page = PDF page - 13 now (the offset grew with the front matter).
- **Running page total at ch. 20:** chapters 1-20 occupy printed pp. 1-218 (with the part pages: about 10.9 pp per
  chapter; ch. 11-20 about 9 pp each). The PDF is 305 pp with 16 stub chapters and the solutions of ch. 1-20 (printed
  pp. ~239-292, about 2.7 pp per chapter). Projection at this rate: about 520 PDF pages for the finished book. Under the
  14-16 pp budget: chapters 11-20 dropped secondary charts and diagrams for the fetch budget, logged per chapter.
- **Ch. 21 `public-choice-voting`: DONE** (pages at the next build). Opening chart JST central-government expenditure
  over GDP, median and IQR of up to 18 economies; the suffrage event study dropped (no single fetched table of suffrage
  dates; Lott-Kenny's abstract not available). Meltzer-Richard tested on approved data: WDI expense vs Gini 2010-19, 75
  countries, slope -0.70 (-0.44 with income) --- the reverse of the prediction, said so. Wagner cross-section WDI 2019.
  Median voter tested with Lee-Moretti-Butler (NBER w9315) and Lee 2001 incumbency; Poterba 1994 record; Gelman-Silver-
  Edlin measure (PDF text). Tiebout `tested` names the boundary design without an estimate (Black 1999 not fetched).
  Diagram replaced by a computed chart (median household's net benefit, setter). Problem 24 questions (pool 6 lanes,
  setter 13.4, capitalisation 12,500). Exercise code ex08 (Wagner 2000/2019), ex12 (JST fixed effects). Fetches +7
  (one wrong NBER number), searches +1.
- **Ch. 22 `interest-groups-and-regulation`: DONE.** Opening chart: cited points (White House 2015 report quoting
  Kleiner-Krueger: State licences <5 % early 1950s drawn at 5, 25 % 2008; 29 % all levels; BLS CPS Table 49 licence
  share 2015/2019/2022/2025) with the measure break said. Tullock dissipation chart (analytic). Diagrams: Tullock
  rectangle vs Harberger triangle; Niskanen bureau. Peltzman proof needs an explicit condition at p^c (stated).
  Niskanen proof corrected: bureau output 2Q* needs a <= 2c. Capture tested with Kleiner-Krueger (14 % premium),
  Kleiner-Kudrle (dentistry), Rose 1987 (trucking union premium 50 -> <30 %); measure box Kleiner-Soltas (12 % of
  surplus). Bureau tested weakly with Domberger-Jensen (20 % savings). Privatisation record Megginson-Netter. Dropped:
  OIRA report (not fetched), OECD PSE, U.K. privatisation list, hair-braiding case. Problem 25 questions (licence social
  cost 5.66 m dalens a year = 1.6 Harberger + 4.06 Tullock). Code ex12 (invented-state DiD). Fetches +12, searches +5.
- **Ch. 23 `labour-supply-and-demand`: DONE.** Opening chart WDI women's participation 1990-2025 (USA, SWE, DEU, JPN,
  KOR, ITA); PWT hours 1950-2023 with output-per-hour ratios; U shape FM ratio vs income 2019 (177 countries, minimum
  ~11,000 $, R2 0.09). Fixed-cost participation proposition (quasi-linear), Hicks-Marshall derivation, a three-task
  automation example (low wage falls in it; said in `breaks`). Records: Goldin-Katz pill; measures Chetty (0.33/0.25)
  and Lichter-Peichl-Siegloch meta-analysis (no single value quoted: the abstract gives none). Dropped: Goldin's century
  numbers (abstract gives none), Bailey 2006, Huberman-Minns hours since 1870, effective retirement age (no approved
  series); the retirement section is short and uses the Brenland survey. Problem 25 questions (payroll cut: 35.5 thousand
  workers + 46.9 thousand FTE). Code ex05 (PWT hours), ex08 (U shape 2000/2019). Fetches +9, searches +2.
- **Ch. 24 `human-capital`: DONE.** Opening chart: Card (2000, NBER w7769) Table 2, ten studies, OLS vs IV with
  intervals (first model of each; Ichino-Winter-Ebmer left out, its schooling measure is a dummy); IV above OLS in 9 of
  10. Mincer chart on `nsw("cps_controls")` (13,820 men, 0.063; re78 top-coded for 30 %, said in caption). Records:
  compulsory schooling (Harmon-Walker 15.3 vs Devereux-Hart's reanalysis of Oreopoulos 3 % / men 4-7 %), STAR
  (Krueger); measure: twins (Ashenfelter-Krueger 16 %). Model tested with Psacharopoulos-Patrinos (9 %). Dropped:
  Isacsson, Hoxby, Angrist-Lavy, Card 2001 heterogeneity diagram, earnings-profile chart (kept as ex11 code). Problem
  25 questions (private 7.1 %, social 4.1 %). Code ex05, ex11. Fetches +9, searches +4.
- **Ch. 25 `wage-structure`: DONE.** Opening chart: Autor-Goldin-Katz 2020 (NBER w26705) Table A2, annual changes in
  premium, relative supply and demand by period 1914-2017 (bars); sigma 1.62 and the 75 % / 38 % split from the same
  paper. Oaxaca chart on `nsw("cps_controls")` white vs black men (gap 0.31, explained 0.09/0.11). Correspondence record
  (Bertrand-Mullainathan; Kline-Rose-Walters), taste model tested with KRW's profitability correlation (Black-Strahan
  and Hellerstein et al. not fetched). Union measure Card 1996. Mariel debate: Card 1990, Borjas 2017, Clemens-Hunt,
  Peri-Yasenov (Dustmann et al. not fetched). Immigration-surplus diagram. Problem: seeded invented series (sigma 1.78,
  premium 0.40 in 2035). Code ex06 (Oaxaca detail), ex12 (composition-change DiD). Fetches +8, searches 0.
- **Ch. 26 `minimum-wage`: DONE.** Opening chart: the brief's 15-study elasticity chart was not feasible from
  abstracts (most state no elasticity); replaced by the five estimates that their authors state as elasticities with
  respect to the minimum (NW 2000 for both New Jersey values, DLR 2010 panel and border pairs, NSW 2014 teens), with the
  selection rule printed. Funnel plot and FAT-PET exercise dropped (no standard errors for most); ex11 replaced by a
  firm-supply-elasticity simulation. Records NJ/PA and replies, Germany (Dustmann et al.); measure via model box: Dube
  et al. MTurk 0.1, Azar et al. 17 %. Debate box with grades. `dated` box of minimum-wage levels dropped (no agency
  table fetched). Brenland bunching chart from the survey with the problem's assumption. Problem 26 questions
  (employment-maximising floor 13; border DiD -1.5 %, own-wage -0.22). Code ex07, ex11. Fetches +17, searches +5.
- **Ch. 27 `oligopoly-and-collusion`: DONE.** Opening chart: Ashenfelter--Hosken (2008) section 5, six products of two
  mergers against two control groups (cited CSV); the ~8-row multi-study chart was not feasible (Kwoka, Weinberg give no
  fetched numbers). Lysine/vitamins cartel record dropped (Connor overcharge not in a fetched primary source); variance
  screen `measure` box (Abrantes-Metz et al. 2005). Rising-markups record: De Loecker--Eeckhout vs Traina (abstracts).
  Peters 2006 in the model box; Bresnahan--Reiss abstract only (no numbers). Discount factor written $\beta$ (local
  notation; $\delta$ is mean utility). Problem 26 questions (merged price +0.42, mean +0.29 predicted, +0.25 measured;
  neutral saving 36.5 %, UPP 25.2 %). Code ex08 thresholds, ex11 merger pairs. Fetches +8, searches +5.
- **Figdata test fixes (21:05 tool fix)**: stale tests fixed in ch. 01 (2SLS has no finite mean: 27 % of F=2 draws
  fall outside the window; prose now says so), 02 (Series.between clash; unequal bins), 05 (tolerance now 2.5 SE of the
  generating values; printed estimates unchanged), 12 (U.S. surplus in 1991), 17 (e = 0.5 is past the Laffer peak, as
  the text says; JST NaN), 20 (All row double-counted). No printed number changed except the ch. 01 sentence.
- **Ch. 28 `auctions-and-market-design`: DONE.** Opening chart Klemperer (2002) Table 1, nine auctions (cited CSV,
  table read from the paper's own table page). Records U.K./Netherlands (Klemperer), FCC incentive auction (FCC news
  release), Boston 2005 (APRS NBER w11965). Lucking-Reiley in the model box; Kagel lab results not fetched, omitted.
  Kidney-exchange count chart dropped (no approved data). Problem 25 questions (reserve 200, revenue 245; DA matching).
  Code ex06 DA both sides, ex11 risk-averse formats. Fetches +9, searches +2.
- **Ch. 29 `platforms-and-innovation`: DONE.** Opening chart: the brief's entry/exit-share chart was not feasible (FHK
  2001 PDF is scanned; abstracts give no numbers except DHH's 50 % / 80--90 %); replaced by WDI R&D/GDP 1996--2023, six
  economies (U.K. left out: 2013--14 break, said in print). Chart 2 patents per million vs income 2019 (111 countries,
  elasticity 1.56, R^2 0.48). Records: FHK retail + DHH; Williams 2013 vs Sampat--Williams 2019. QWERTY record dropped
  (Liebowitz--Margolis abstract not available). Inverted-U model box (ABBGH abstract). Problem 24 questions (fees 4.39 /
  -0.61; net entry 60.5 %). Code ex08 R&D vs patents, ex12 FHK on manufacturing firms. Fetches +10, searches +1.
- **Ch. 30 `competition-policy`: DONE.** Opening chart: cited Borenstein--Rose (2007) yield/traffic growth rates in three
  periods. The BLS CPI airline-fares series was computed and REJECTED: relative to all items it rises ~2x from 1978 to
  2000, contradicting yield data (known list-fare problem, no source fetched to explain it in print), so not shown.
  `dated{2026}` box: 2023 U.S. merger guidelines thresholds (PDF Guideline 1). A--J model box tested via the Cleveland
  Fed WP 8713 introduction (Courville, Spann...; Joskow's view; Ohio utilities). RPM/Leegin record dropped (MacKay--Smith
  SSRN 403). Water problem 25 questions (X = 1.03 shares the saving; A--J K/L 4.43, 29 % excess cost). Code ex08 HHI
  screens, ex11 price-cap path. Fetches +10, searches +4.
- **Ch. 31 `growth-empirics`: DONE.** Opening strip chart of decadal growth (PWT 11.0 rgdpe/pop, 1960s--2010s; medians
  2.9/2.0/1.2/1.8/3.4/2.5 %). Convergence 1960--2019: none across 111 countries (slope -0.0013, se 0.0017); Western
  Europe + offshoots, a group fixed by geography (Maddison regions), -0.0125, speed 2.3 %. Maddison paths ARG/JPN/KOR/VEN/
  USA 1900--2022; WDI agricultural employment 2019 (177 countries). Ledger b3ge: mrw, hj, ekps, hpr, sim, lr, young, jlps,
  glw, islam (abstracts only; Barro 1991 and Hsieh 2002 not cited). Code ex05 three samples (selection on outcome), ex06
  persistence, ex11 extreme bounds. Problem 24 questions on a 1975--2025 Brenland series (backcast in figdata).
  Fetches +10, searches 0.
- **Ch. 32 `institutions`: DONE.** Opening chart per the brief's proposal: China 1950--2022 (1978 marked) + Maddison
  regional Western/Eastern Europe. Koreas 1990--2022 (ratio 5.6 -> 26.3); transition index 1989 = 100 for POL/CZE/RUS/UKR.
  Germany told via Redding--Sturm only (no GDR productivity number fetched; Sinn--Sinn and EBRD reports not used).
  Tabellini 2010 not cited (no fetchable abstract); the ISS night photo NOT added (no image download done). Section 6
  (crime) kept with Levitt 1995 WP and Di Tella--Schargrodsky. Ledger b3in: ajr, albouy, glls, sachs, dell, lin, kornai,
  rs, levitt, dts. Problem 24 questions (synthetic North, 2SLS share 77 %). Code ex07 transition. Fetches +13, searches +1.
- **Ch. 33 `demographic-transition`: DONE.** Opening chart = the brief's fallback (Maddison GBR gdppc 1252--1850; Maddison
  has no annual English population before 1820, so no population line; Black Death +23.6 % 1348--51). TFR 1800--2024
  six countries (Gapminder <=1949 / WDI >=1960, not joined); TFR vs income 2023; old-age dependency 1960--2025 (no
  projections). Birth/death-rate chart not drawn. Brief's ex11 (income vs population growth before/after 1800) not
  feasible without annual population: replaced by half-century growth rates (py). Old-age dependency ratio recalled from
  Book 4, not redefined. Ledger b3dt: ag, clark, bckov, gw, bds, als, rz, qian, bl. Problem 25 questions
  (306 kg; 29.1 %; PAYG 17.9 % with an invented 1,950 thousand over-65s). Fetches +12, searches +1.
- **Ch. 34 `development-microeconomics`: DONE.** Opening chart [L] from Meager arXiv v3 Appendix A (general effect tau
  for six outcomes, joint model; cited src/meager.csv, ledger b3dm:meager.tab) -- the site-level estimates could not be
  mapped to site names from the text, so the chart shows the six pooled effects, not seven studies. FGT at $3.00 for
  eight countries 2022 from PIP percentile bins (no regions in the loader). Aid/GNI vs growth 1990--2019 (134
  countries). Ledger b3dm: meager.tab, meager, bkz, fgt, progresa (no numbers in the abstract), hs, egger (multiplier
  2.4), mk, aiken, gs, bd, elr, rs, gkxz, bandiera, km. Not cited: Balboni 2022 (record 404), Clemens 2012, Banerjee
  2015 Science, Hicks 2015, Field 2007, Dasgupta--Ray. ex6/ex11 use invented study tables. Problem 26 questions
  (effect 280 [107, 453]; 34,253 dalens per household lifted). Fetches +24, searches +2.
- **Ch. 35 `environmental-and-resource-economics`: DONE.** Opening chart = the brief's EKC fallback (CEDS SO2 per person
  vs Maddison income, six economies, 1850--2019); the Simon--Ehrlich wager dropped (no primary printed table found).
  CO2 per person vs income 2019 (elasticity 1.11). Cited table: EPA 2023 SC-GHG Table ES.1 (src/scc.csv, ledger
  b3er:epa, read from the PDF with pdftotext). No dated{2026} EU ETS box (no source fetched). Stern Review told
  through Nordhaus 2007 only; Livernois 2009 and Stern 2004 had no abstracts, not cited. Ledger b3er: gk, ss, kra,
  nordhaus, epa, way. Problem 26 questions (tax 1,200 dalens/t SO2; coal out in 2051). Coordinator's S1 extension
  (author-year citations in tested/breaks) noted and used in ch. 35. Fetches +13, searches +1.
- **Ch. 36 `income-and-wellbeing-evidence`: DONE.** Opening chart from the newly approved Eurostat ilc_pw01 (life
  satisfaction, 32 European countries, 2013 -> 2024 arrows) against WDI NY.GDP.PCAP.PP.KD, instead of the brief's
  published-slopes fallback. Chart 2: Jones--Klenow-style consumption-equivalent welfare, 115 countries, 2019, computed
  from PWT 11.0 (rgdpe, pop, csh_c, avh, emp), WDI life expectancy and Gini (latest 2010--2019); one year, no age
  structure, kappa = 5, theta from the U.S. FOC with labour share 0.6. The emotional-wellbeing chart is a debate box
  instead (no tabulated points). Decomposition table for six countries (not a chart). Closing section: themes table
  (13 data-strand themes, model, chapter, record) and the open debates with their strongest grades. Ledger b3iw: emssz,
  sw, kd, kil, kkm, jk (Easterlin 1974, Sacks et al. 2012, Deaton 2008 not fetched, not cited). Code ex05_ranks,
  ex11_kappa (shared welfare_data.py). Problem 24 questions (welfare growth 3.0 %/yr vs GDP 1.9 %/yr). Also added
  evidence grades to the ch. 32 and ch. 34 debate boxes, which had none. Fetches +7, searches +0.
- **Phase C (2026-11-20).** Term links: `--unwrap --apply` then `--apply`, 342 linkable terms, 1,018 links in 70
  files; `--check` clean. Curation in `tools/term_config/book5_en.py`: STOP (link only inside the defining chapter)
  for institutions/Institutions, poverty trap (ch. 18 vs ch. 34 senses), cutoff, reproduction, scale effect,
  monotonicity; EXTRA_PROTECT for "annuity factor" (ch. 20) and ch. 15's market event study. Per-figure pass: all 130
  charts and diagrams looked at on 3x2 contact sheets (pdfjam), ch. 35--36 at full size; fixed crowded year ticks in
  ch. 15 (2 charts), 16, 29 and 33, and the ch. 35 SO2 caption (annual peaks between five-year points). No AI image,
  no PNG, no stub. Final forced build 0/0/0, 451 PDF pp (body printed pp. 1--353, solutions 354--432, index 433), all ten years' gates OK, `test_code.sh bachelor-3` GREEN, figdata + pytest
  over bachelor-3.
- **Next action**: Phase D report sent; wait for the main session's verification.
- Data news (16:55): Fed H.4.1/H.15, ECB total assets, Eurostat ilc_pw01 now load (`fed_series`, `ecb_total_assets`,
  `eurostat`); USGS not yet (ch. 35: cited tables). Replace `% PENDING-DATA` at ch. 15 and 36.

## Web fetches (budget ~250)

| Date | Fetches | Searches | What |
|---|---:|---:|---|
| 2026-11-20 | 12 | 5 | programme check: Paris 1, Gustave Eiffel, Dauphine, Toulouse Capitole L3 lists; Mastering 'Metrics, Gruber TOCs (KOM, Borjas via search) |
| 2026-11-20 | 7 | 2 | ch. 04: NBER w13374, w5888 (+ scanned PDF, unreadable), w23486 (+ PDF), Lee 2008 final WP PDF; one wrong NBER page (w14443); searches for CD2009 and Lee |
| 2026-11-20 | 4 | 1 | ch. 03: Card--Krueger NBER w4509 PDF; ADH 2015 erratum and article PDFs (two hosts, one reset); search for ADH |
| 2026-11-20 | 1 | 0 | ch. 02: Bertrand--Duflo--Mullainathan abstract (NBER) |
| 2026-11-20 | 7 | 4 | ch. 01: Angrist--Krueger 1991 (PDF), Bound--Jaeger--Baker 1995 (PDF), Stock--Yogo 2002 (PDF, NBER page), Lee et al. 2022, Miguel et al. 2004 abstracts |

Running total: 328 fetches, 72 searches (ch. 5: 2 + 1; ch. 6: 5 + 1; ch. 7: 5 + 3; ch. 8: 9 + 2; ch. 9: 6 + 1; ch. 10: 5 + 1; ch. 11: 9 + 0; ch. 12: 6 + 2; ch. 13: 7 + 2; ch. 14: 6 + 2; ch. 15: 12 + 0; ch. 16: 7 + 2; ch. 17: 12 + 2; ch. 18: 10 + 3; ch. 19: 11 + 2; ch. 20: 7 + 2; ch. 21: 7 + 1; ch. 22: 12 + 5; ch. 23: 9 + 2; ch. 24: 9 + 4; ch. 25: 8 + 0; ch. 26: 17 + 5; ch. 27: 8 + 5; ch. 28: 9 + 2; ch. 29: 10 + 1; ch. 30: 10 + 4; ch. 31: 10 + 0; ch. 32: 13 + 1; ch. 33: 12 + 1; ch. 34: 24 + 2; ch. 35: 13 + 1; ch. 36: 7 + 0).

## Data probes done (approved data only, `econdata`, 2026-11-20)

- `gravity()`: 1996--2020, ~31,000 non-missing flows a year; 10 columns, all years = 117 MB in memory. No common-currency
  column (EU membership and FTA only).
- JST R6: 1870--2020, 17 economies; `peg`, `peg_type` (PEG/FLOAT/BASE), `peg_base`, `JSTtrilemmaIV`, `ca`, `revenue`,
  `expenditure`, `money`, `cpi`, `stir`, `xrusd` all present.
- Maddison 2023: GBR from 1252 (annual), CHN annual from 1950, KOR from 1950, **PRK only 1820 and 1990--2022**, **no
  separate East/West Germany**; regional "Eastern/Western Europe" in `maddison_regions`.
- WDI (checked codes): see BRIEFS; missing from the approved set: `PA.NUS.PPPC.RF`, `DT.ODA.ODAT.GD.ZS`, `IC.REG.DURS`;
  no world row for `TM.TAX.MRCH.WM.AR.ZS` and `FM.LBL.BMNY.ZG`. No governance (WGI) series; CPIA ratings only.
- NSW: `nsw_dw` 445, `cps_controls` 15,992, `psid_controls` 2,490 rows; columns treat, age, education, black, hispanic,
  married, nodegree, re74, re75, re78.
- FAOSTAT: 9 crops, elements Yield / Area harvested / Production, 1961--2024. BLS derived file: CPI all-items series
  only (20 area series). CEDS SO2 and CO2 1750--2023. EIA 1980--2024.
- Panel candidate slopes (log income per person, WDI): CO2 per person between 2.98 / within 1.22; fertility $-0.84$ /
  $-1.40$; female participation $-0.79$ / $+1.51$.

## For the shared docs

- Term links: `STOP` keeps a term linked inside its defining chapter only (it is not removed); use `EXTRA_PROTECT`
  phrases for a second sense inside other chapters (e.g. "annuity factor", a market "event study").
- pgfplots picks a 2-year tick step for 20--30-year `omtime` axes; at 0.7\linewidth the labels touch. Find them with
  `pdftotext -layout` (rows of 9+ year tokens) and set `xtick distance=5`. An explicit list `xtick={2005,2010,...,2025}` inside `omtime` fails (PGF Math
  Error: the style appends `.5` to the list) and kills the build.
- `ilc_pw01` has 32 countries in both 2013 and 2024; map Eurostat EL -> GR and UK -> GB before joining WDI's
  2-alpha codes.
- A consumption-equivalent welfare measure built from PWT hours counts unemployment and low participation as leisure
  (Jordan, Lebanon, Bosnia rise in the ranking); say so where it is used.
- No `debate` gate checks the evidence grades: ch. 32 and ch. 34 boxes had none until Phase C.
- No PIL in `.venv`: contact sheets for the per-figure pass are `pdfjam --nup 3x2 --landscape` + `pdftoppm -r 80`.

## Reader triage (2026-11-21)

Coordinator triage of `READER_REPORT.md` (85 defects: 7 major, 42 minor, 36 nits) plus depth restoration (target
13--15 pp of body where the material allows). Rulings: R5-048 (market Gini or "consistent with"), R5-072 (Levitt with
McCrary's comment and the reply, graded; ex. 12 on a range), R5-030 (describe the regression run; equality line;
Grenada), R5-014. New sections: ch. 11 WTO institutions + second chart; ch. 15 estimated local projection +
event-study magnitudes; ch. 19 Baily--Chetty on cited consumption drops + hazard-spike and two-state diagrams;
ch. 8 Leontief + Leamer. Restore dropped charts/records in ch. 18, 20, 21, 26--29, 35. Sweeps: tested fields,
clipping, ticks, back-filled series, measurement mixes, format-only tests, unused terms, unprinted problem data,
one-sided records. Resolution of each defect is logged in `sources/book5/FIXES.md` as it is made, and copied into
the report's Resolution column at the end. Work goes chapter by chapter from ch. 1; check PAUSE before each.

Triage closed 2026-11-21: 85 defects, 84 fixed, 1 rejected with evidence (R5-001); every resolution in `FIXES.md`
and in the report's new Resolution column. Depth added: ch. 8 (Leontief, Leamer), 11 (strategic trade, rules,
bound-vs-applied chart), 15 (local projection, LSAP numbers), 18 (Gini chart), 19 (consumption drops, Baily--Chetty
applied, two diagrams, crowd-out record), 20 (Green Book and EPA dated box, MVPF record, demand-forecast record),
21 (Condorcet cycles), 22 (RIA record, privatisation panel), 25 (gender gap record), 26 (Kaitz dated box), 28
(kidney exchange record, Roth 1991), 29 (Eurostat bd_size dynamism chart), 32 (police debate), 35 (SO2 costs and
benefits, Simon--Ehrlich). Series changes with re-derived numbers: ch. 23 PWT hours (interpolated runs masked),
ch. 31 growth from rgdpna, ch. 33 TFR fill-ins dropped and decade means. Not restored (no readable source or no
approved data): ch. 20 audit chart of named projects, ch. 26 funnel chart, ch. 28 kidney count chart, ch. 35
Hotelling price chart. No new data need. Fetches this triage: about 85 (+ 9 searches).
Running total: about 413 fetches, 81 searches.
