# Book 4 (`bachelor-2`) — progress

## State

- 2026-11-20: **Phase A done.** `BRIEFS.md` (34 chapter briefs) and `DEFINITIONS.md` (~305 terms) written; programme check
  and data-availability check done; Phase A report sent. No chapter, figdata, code or ledger row written yet.
- 2026-11-20: sync read (S1--S5, R1--R3); `DEFINITIONS.md` updated to the rulings (R3 owners marked, Hotelling location
  game renamed *location game*, Y3 owns the Hotelling model) and frozen for Book 5.
- 2026-11-20: main session announced loaders (16:55): `eurostat("jvs_q_nace2")`, `eurostat("une_rt_q")`,
  `jolts("JO", rate=True)` (ch. 26 Beveridge), `fed_series("h15", code)` / `fed_find` (ch. 4 term structure, ch. 27
  Taylor rule; fed funds `RIFSPFF_N.M`), `fed_series("h41", "RESPPMA_N.WW")`, `ecb_total_assets()` (ch. 29), `cex_table`,
  `bls_ap`. No `% PENDING-DATA` stub needed so far: use them directly when the chapters come.

- 2026-11-20: **all 34 chapters written; Phase C done** (links curated, 1,443; full figure pass; fresh build 455 pp,
  0/0/0; gates, figdata and code tests green). Phase D report sent.

## Chapter log

| Ch. | Slug | Pages | Charts (data) | Diagrams | Ex. | Pb q. | Ledger rows | Tests | Status |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| 1 | expected-utility | 15 (pp. 12--26) | 1 opening chart, cited (KT 1979 Problems 1--4, `cited.py`) | 4 (triangle, chord, CRRA curves, CARA vs CRRA premium) | 12 (4/5/3) | 24 | 13 | 2 figdata + 6 code | gated 0/0/0; every figure page rendered and checked |
| 2 | insurance-and-risk-sharing | 13 (pp. 27--39) | 2 charts on WDI (opening: consumption vs GDP volatility, 123 countries, log-log; correlation with the world); 1 simulated table (Kestria survey regression, `pgfplotstabletypeset`) | 3 (contingent-goods diagram, Edgeworth box under risk, portfolio share vs $\gamma$) | 12 (4/5/3) | 25 | 6 | 2 figdata + 5 code | gated 0/0/0; every figure page rendered and checked |
| 3 | intertemporal-choice | 14 (pp. 40--53) | 1 cited opening chart (BLS CE Table 1300, 2023, 7 age groups, `cited.py`); 1 invented chart (Brenland survey by age band) | 3 (two-period Euler tangency, borrowing-limit corner, preference-reversal bars) | 12 (4/5/3) | 25 | 11 | 5 figdata + 6 code; 1 listing + 1 output | gated 0/0/0; every figure page rendered and checked |
| 4 | asset-prices | 15 (pp. 54--68) | 3 charts on JST (opening: cumulated real returns 1950--2020, 4 countries x 3 assets, groupplot; mean vs sd, 15 countries x 3 assets; equity autocorrelations with the 2/sqrt(n) band) | 3 (payoff plane with equal-price lines, frontier with capital line, security market line, said to be an illustration) | 12 (4/5/3) | 25 | 11 (6 qualitative) | 6 figdata + 6 code; 1 listing (JST) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 5 | behavioural-evidence | 14 (pp. 59--72) | 2 charts (opening: original vs replication r, 18 experiments, Camerer et al. 2016 Table S1; participation and default, Madrian--Shea 2000, 4 numbers) | 2 (value function, weighting function, illustrative parameters) | 12 (4/5/3) | 24 | 41 (18 Table S1 rows + 23 others incl. 8 sources) | 3 figdata + 6 code; 1 listing (simulation) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 6 | exchange-economies | 12 (pp. 74--85) | 1 chart (opening: average price per period as % of prediction, 6 of Smith's 1962 tests, from his Table 1) | 4 (box with budget line and equilibrium; contract curve, lens and core; offer curves; three-equilibrium excess demand) | 12 (4/5/3) | 24 | 11 (10 Table 1 rows + source) | 1 figdata + 5 code; 1 listing (tatonnement) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 7 | welfare-theorems | 12 (pp. 86--97) | 1 chart (opening: London--New York wheat gap split into freight, charges and residual, Persson 2002 Table 3) | 3 (Crusoe; first theorem in the box; non-convex technology) | 12 (4/5/3) | 24 | 4 (3 rows + source) | 1 figdata + 4 code; 1 listing (second theorem transfer) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 8 | prices-as-information | 12 (pp. 98--109) | 2 charts (opening: returns by type of bet, Snowberg--Wolfers 2010 text; China coal output by mine type, Zhang 2018 Table 12.2) + 1 model chart (Grossman--Stiglitz share and informativeness, computed) | 2 (planner vs market flows; naive vs revealing price) | 12 (4/5/3) | 24 | 5 rows + 4 sources | 3 figdata + 5 code; 1 listing (informed share simulation) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 9 | social-choice | 12 (pp. 110--121) | 1 chart (opening: flaw rates in 182 US ranked-choice elections, Graham-Squire--McCune 2023 Table 7) | 3 (compensation-test reversal; majority cycle; single-peaked vs not) | 12 (4/5/3) | 24 | 1 row + 1 source | 1 figdata + 3 code; 1 listing (cycles under random vs single-peaked preferences) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 10 | static-games | 10 (pp. 122--131) | 1 chart (opening: public-goods contributions with/without punishment, Fehr--Gaechter Tables 3--4) | 4 (three payoff matrices; public-good best responses; location line) | 12 (4/5/3) | 24 | 5 rows + 2 sources | 1 figdata + 4 code; 1 listing (iterated dominance + pure NE) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 11 | mixed-strategies | 10 (pp. 132--141) | 1 chart (opening: win rates after left/right first serves in 40 point games, Walker--Wooders 2001 Table 1) | 2 (best responses in the penalty game; penalty and inspection matrices) | 12 (4/5/3) | 24 | 3 rows + 2 sources | 1 figdata + 3 code; 1 listing (simulated equilibrium penalty play with Pearson tests) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 12 | dynamic-games | 12 (pp. 141--152) | 1 chart (opening: ultimatum mean offers and rejection rates in 18 groups, Henrich et al. 2001 Table 1) | 4 (entry tree, ultimatum tree, two-round bargaining tree, capacity-commitment best response) | 12 (4/5/3) | 24 | 4 rows + 2 sources | 1 figdata + 5 code; 1 listing (finite-horizon alternating offers converging to the infinite-horizon split) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 13 | repeated-games | 11 (pp. 153--163) | 1 chart (opening: cartel duration, average and range, in nine samples, Levenstein--Suslow 2006 Table 1) | 3 (feasible and individually rational payoffs; critical discount factor against n; deviation-and-punishment profit path) | 12 (4/5/3) | 24 | 4 rows + 2 sources | 1 figdata + 3 code; 1 listing (four strategies of the repeated prisoner's dilemma at two discount factors) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 14 | bayesian-games | 12 (pp. 164--175) | 1 chart (opening: fitted bid per unit of value of 18 lab subjects with 3 and 6 bidders against the risk-neutral prediction; Bajari--Hortacsu 2003 Table 1 on Dyer--Kagel--Levin 1989) | 3 (bid functions; winner's-curse correction against n; certificate signalling tree with beliefs) | 12 (4/5/3) | 24 | 4 rows + 2 sources | 1 figdata + 4 code; 1 listing (simulated first- and second-price revenues, with risk-averse bidders) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 15 | adverse-selection | 9 (pp. 176--184) | 1 chart (opening: change in five-year mortality by annuity feature, compulsory and voluntary markets, Finkelstein--Poterba 2004 Table 2) | 3 (lemons collapse; demand, average and marginal cost with the welfare loss; unravelling staircase) | 12 (4/5/3) | 24 | 4 rows + 3 sources | 1 figdata + 4 code; 1 listing (year-by-year unravelling with the welfare loss) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 16 | signalling-and-screening | 10 (pp. 185--194) | 1 chart (opening: mean 1975 earnings by years of schooling, NSW survey comparison sample, 15,992 men) | 3 (least-cost separating equilibrium; separating insurance menu in state-wealth space; two-plan screening tariff) | 12 (4/5/3) | 25 | 4 rows + 1 source | 1 figdata (3 tests) + 5 code tests; 1 listing (grid search for the best two-plan menu) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 17 | moral-hazard | 11 (pp. 195--205) | 2 charts (opening: three estimates of Safelite's piece-rate gain, Lazear 2000; doctor visits by coinsurance rate, RAND HIE via statsmodels randhie, idp = 0 plans, 14,941 person-years) | 3 (two-outcome contract in utilities; optimal share against noise; variance of the relative measure against the weight) | 12 (4/5/3) | 25 | 5 rows + 3 sources | 2 figdata (2 tests) + 4 code tests; 1 listing (grid search for the linear share) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 18 | externalities-and-public-goods-theory | 13 (pp. 206--218) | 2 charts (opening: US SO2 emissions, electricity and heat vs other, CEDS 1970--2023; SO2 allowance auction prices, five years quoted by Schmalensee--Stavins) | 4 (tax; prices vs quantities; vertical summation; listing replaces the Coase diagram) | 12 (4/5/3) | 25 | 6 rows + 3 sources | 2 figdata (2 tests) + 5 code tests; 1 listing (pivot mechanism with a check of all reports) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 19 | consumption | 10 (pp. 219--228) | 2 charts (opening: US quarterly growth of real consumption and disposable income, macrodata 1959--2009; household consumption share of GDP, USA/JPN/KOR/DEU, WDI 1970--2025) | 3 (life cycle; MPC by persistence (bars); convex marginal utility and precaution) | 12 (4/5/3) | 25 | 4 rows + 4 sources | 3 figdata + 4 code tests; 1 listing (Campbell--Mankiw lambda by IV on macrodata) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 20 | investment | 11 (pp. 229--239) | 2 charts (opening: Grunfeld's 11 firms, investment against market value, each relative to the firm's own mean, 1935--1954; investment share of GDP, USA/DEU/JPN, JST 1870--2020) | 3 ((K, q) phase diagram with saddle path; permanent profit-tax cut; option-value threshold (pgfplots)) | 12 (4/5/3) | 24 | 3 rows + 3 sources | 3 figdata + 3 code tests; 1 listing (trigger profit of an irreversible project by bisection) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 21 | government-debt | 11 (pp. 239--249) | 2 charts (opening: government debt/GDP, GBR/USA/FRA/JPN/ITA, JST 1870--2020; offset test, change in national saving against change in government net lending, 87 countries, WDI 2000--07 vs 2010--17) | 2 (debt-dynamics phase lines for i > g and i < g; two-period Ricardian budget) | 12 (4/5/3) | 24 | 5 rows + 5 sources | 3 figdata + 3 code tests; 1 listing (stabilising vs actual primary balance, Eurostat gov_10dd_edpt1, DE/FR/IT/EL) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 22 | overlapping-generations | 9 (pp. 249--257) | 2 charts (opening: old-age dependency ratio, JPN/ITA/KOR/USA/NGA/World, WDI 1960--2025; dynamic-efficiency test, capital income against gross investment, 140 economies, PWT 2019) | 3 (generations timeline; k_{t+1} against k_t with staircase; PAYG budget) | 12 (4/5/3) | 25 | 1 row + 1 source | 2 figdata + 3 code tests; 1 listing (OLG steady state with and without PAYG, bisection) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 23 | ramsey-model | 9 (pp. 257--265) | 3 charts (opening: gross domestic saving, KOR/CHN 1960--2024 and JPN 1970--2024, WDI; Korea capital/GDP, PWT 1960--2023; model simulation of k/k* and the saving rate for theta 2 and 6, labelled invented) | 2 (phase diagram from the computed saddle path; permanent rise in G) | 12 (4/5/3) | 25 | 1 row + 1 source | 2 figdata + 4 code tests; 1 listing (saddle path by shooting) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 24 | endogenous-growth | 8 (pp. 266--273) | 1 chart (opening, two panels: US TFP growth by decade, PWT 1954--2023; researchers per million, USA/DEU/JPN/KOR/CHN, WDI 1996--2023) | 2 (AK growth against s; growth of ideas for phi = 1 and phi < 1) | 12 (4/5/3) | 24 | 2 rows + 2 sources | 2 figdata + 3 code tests; 1 listing (doubling the research share in the semi-endogenous model) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 25 | expectations-and-lucas-critique | 9 (pp. 274--282) | 3 charts (opening: average inflation 1955--88, JST, against the Alesina--Summers index, 15 countries; US inflation against unemployment by decade, statsmodels macrodata 1960--2008; median CPI inflation around inflation-target adoption, WDI, 27 countries) | 2 (timeline of expectations and policy; inflation-bias diagram with loss contours) | 12 (4/5/3, one D) | 24 | 47 rows + 4 sources | 3 figdata + 4 code tests; 1 listing (Lucas critique: Phillips curve estimated under one target, used under another) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 26 | search-and-unemployment | 8 (pp. 283--290) | 1 chart (opening: euro-area Beveridge curve, Eurostat jvs_q_nace2 JVR B-S SA and une_rt_q 15--74 SA, EA21, 2009-Q1 to 2025-Q4) | 2 (wage curve and job creation in (theta, w) with the benefit shift; Beveridge curve and tightness rays in (u, v) with the benefit shift) | 12 (4/5/3) | 25 | 3 rows + 3 sources | 2 figdata + 4 code tests (incl. bisection vs closed form); 1 listing (DMP equilibrium, benefits, Shimer elasticity) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 27 | three-equation-model | 10 (pp. 291--300) | 2 charts (opening: federal funds rate, H.15, against the Taylor 1993 rule from macrodata CPI and HP gap, quarterly 1960--2008; CPI-U inflation and funds rate monthly 2019-01 to 2026-10) | 4 (WS--PS with a markup shift; PC--MR adjustment; interest-rate path; zero-lower-bound kink) | 12 (4/5/3, one D) | 25 | 3 rows + 3 sources | 3 figdata + 3 code tests (listing iterates, solutions closed form, both against hand values); 1 listing (path after an inflation shock) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 28 | business-cycles | 8 (pp. 301--308) | 2 charts + 1 table (opening: rolling 10-year s.d. of GDP-per-person growth, JST 1880--2020, USA/GBR/DEU and median of 17; HP cycles of US GDP, consumption, investment with NBER recessions, macrodata 1959--2009; moments table typeset from CSV) | 2 (trend/cycle sketch; impulse responses of the analytic RBC model) | 12 (4/5/3, one D) | 24 | 5 rows + 5 sources | 4 figdata + 4 code tests (listing iterates, closed form, hand values; growth moments via a second route); 1 listing (analytic RBC) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 29 | banks-and-crises | 10 (pp. 309--318) | 3 charts (opening: banking crises per decade, JST crisisJST, 18 economies; GDP-per-person paths after peaks with and without a crisis, JST event study; loans/GDP change before crises vs other windows, JST tloans/gdp) + 1 photograph (Northern Rock queue, Commons CC BY 2.0) | 3 (DD timeline; payoff-to-waiting diagram; leverage/fire-sale loop) | 12 (4/5/3, one D) | 25 | 15 rows + 9 sources | 3 figdata + 3 code tests (closed-form contract checked against budget and FOC directly, hand values); 1 listing (DD contract and threshold) + 1 output | gated 0/0/0; every figure page rendered and checked |
| 30 | multiple-regression | 11 (pp. 319--329) | 1 chart (opening: schooling coefficient as controls are added, with 95 % CIs, CPS comparison sample) | 2 (projection geometry; OVB sign table) | 12 (4/5/3, one D) | 25 | 1 row (+ Book 3's b1:lalonde1986, b1:dehejia1999 cited) | 2 figdata tests (statsmodels vs numpy lstsq) + 7 code tests (numpy solutions vs statsmodels; hand example; VIF vs statsmodels' variance_inflation_factor); 5 listings + 5 outputs | gated 0/0/0; every figure page rendered and checked |
| 31 | regression-inference | 10 (pp. 331--340) | 2 charts (opening: robust/classical SE ratio for ten RAND HIE coefficients, statsmodels randhie; residual s.d. by fitted-value bin, same data) | 0 (the brief's residual-spread diagram became the second chart) | 12 (4/5/3, one D) | 25 | 1 row + 1 source | 2 figdata tests (HC1 and classical SE rebuilt with numpy) + 6 code tests (sandwich and cluster covariance rebuilt by hand with numpy against statsmodels; hand variances; simulation outputs); 5 listings + 5 outputs | gated 0/0/0; every figure page rendered and checked |
| 32 | specification | 10 (pp. 341--350) | 1 chart (opening: simulated attenuation against lambda*beta, seeded, illustrative) | 0 | 12 (4/5/3, one D) | 25 | 1 row + 1 source | 2 figdata tests (plim by hand) + 6 code tests (Engel fits by numpy polyfit; proxy against its population formula worked by hand; attenuation against lambda; Brenland dummies by numpy lstsq); 5 listings + 5 outputs | gated 0/0/0; figure page rendered and checked |
| 33 | causality-and-experiments | 10 (pp. 350--359) | 1 chart (opening: NSW experiment means with CIs, Dehejia--Wahba subsample) | 0 | 12 (4/5/3, one D) | 25 | 2 rows + 2 sources (cites b1:lalonde1986, b2:nsw-cps) | 3 figdata tests + 7 code tests (difference and SE by plain loop; adjustment by numpy lstsq; selection identity from printed numbers; sample size and power against statsmodels NormalIndPower); 5 listings + 5 outputs | gated 0/0/0; figure page rendered and checked |
| 34 | time-series | 11 (pp. 360--370) | 3 charts (opening: two seeded random walks, illustrative; ACF of US inflation and unemployment, macrodata; four-quarter inflation forecasts 1986--2009, regression vs random walk, macrodata) | 0 | 12 (4/5/3, one D) | 25 | 2 rows + 2 sources | 3 figdata tests + 11 code tests (spurious-regression rate by correlation t; ACF by hand; AR fits by numpy; ADF, Granger F and Newey--West built by hand; D-exercise forecasts by statsmodels per window; Brenland AR(1) by closed form; delta method by numerical derivative); 7 listings + 7 outputs | gated 0/0/0; three figure pages rendered and checked (forecast chart's year ticks thinned) |

Chapter 1 notes. Notation clashes with the series table forced local symbols (notation box): money $z$, lotteries $\ell$,
mixing weight $\theta$, risk premium $\rho$, Arrow--Pratt $\mathcal{A}$, $\mathcal{R}$ ($p$, $w$, $\pi$, $\alpha$, $A$
are taken). KT 1979 printed shares imply at least 65 % of respondents chose B and C in Problems 1--2, while the article's
text says 61 % made the modal choice in both: the 61 % is not used. Sydnor (2010) numbers were not reachable from a primary
copy: cited qualitatively (abstract); the quantitative deductible facts are Collier et al. (NBER w23579). Rabin's sharper
\$1,000 statement is not printed; the chapter proves its own bound (\$2,400) and names Rabin (2000) as the sharper result.
Every solution number is recomputed in `code/bachelor-2/01-expected-utility/exercises/solutions.py` and tested.
Chapter 2 notes. Local symbols added: $\mu$ claim probability, $\chi$ cover at price $\psi$, $\Lambda$ loss, $\eta$
loading, $\omega_i(s)$, $\Omega(s)$, $c_{it}$, $m_{it}$, $\xi$ excess return. Prose numbers about the opening chart come from
`out/summary.csv` (world consumption sd 1.79; 8 of 123 countries have GDP sd below it; median ratio 1.53 low income, 1.12
high income, World Bank income groups via `wdi_countries`). Claims about home bias and enforcement are framed as the model's
candidate reasons, not findings (no ledger row). Townsend (1994) and Karlan et al. (2014) are the two records. The weekend
problem's Part IV regression is simulated (Kestria, seed 4202). Two traps: `\addplot[guide, domain..]{x}` on a
`loglogaxis` draws nothing visible (use `\draw (axis cs:..) -- (axis cs:..)`); a solution that divides rounded table
figures must say so when the table's $t$ comes from unrounded ones (22.6 vs 0.143/0.006 = 24).
Chapter 3 notes. Opening chart: income after taxes and spending less "personal insurance and pensions" (the CE's
expenditures include pension and Social Security contributions), 7 ledger rows of six numbers each, read from the published
table (xlsx). Present-bias factor is $\varphi$ (series $\beta$ = discount factor, $\delta$ = depreciation), with a remark on
the literature's $\beta$--$\delta$. Augenblick--Niederle--Sprenger cited from NBER WP 18734 (2013); the QJE (2015)
numbers were not checked. Brenland's survey makes consumption a function of current income only, so it serves as the
"no smoothing" contrast. Trap: `legend pos=south center` is not a pgfplots choice and kills the build (fatal, no PDF).
Chapter 4 notes. Opening chart deviation: 1950--2020 instead of 1900--2020, because JST has gaps that break a
cumulated index (French bill rates 1915--1921, Japanese equity returns 1946--1947); the brief's 16 countries are 15 (Spain's
series are not complete over 1950--2020; Canada and Ireland have no returns). The H.15 loaders were not needed (the term
structure stays in prose). Mehra--Prescott (1985) numbers are cited through Mehra (2003, NBER w9512, Table 4), whose text
also gives the gamma < 10 calibration. Shiller (1981), Marsh--Merton (1986), Campbell--Shiller (1988) are qualitative
rows. The listing \texttt{puzzle.py} reads JST: US premium 7.64 points 1950--2020, gamma needed 312, at least 25.1 with a
correlation of one. Trap: a listing that imports `econdata` must get PYTHONPATH in the test's subprocess.
Chapter 5 notes. Opening chart as briefed: Table S1 of the Science supplementary materials is an image; its 18 rows were
read from a 250-dpi render of the PDF page and typed into `src/camerer2016.csv`, one ledger row per study (the brief's 36
rows became 18 rows of two values each). Means from the two-decimal table are 0.472/0.277 against the paper's 0.474/0.279;
prose quotes the paper. Loss aversion is $\kappa$ (series reserves $\lambda$ for Lagrange multipliers), curvature $\eta$
($\alpha$ reserved), weighting $\omega(p)$ ($w$ reserved), tax $\tau$. The Tversky--Kahneman (1992) parameter estimates
could not be read from a primary source (Springer paywall, course copy 404), so the chapter uses explicitly illustrative
values ($\eta = 0.9$, $\kappa = 2$, $d = 0.65$) and the Brown et al. (2024) meta-analytic mean 1.955 as the only estimate.
List (2003) is cited from its abstract only (markets not named). Madrian--Shea from the NBER working paper text (37/86, 61/1,
3 per cent default). Listing: a winner's-curse simulation (no data). Trap: Book 4 ch. 1's calibration generalisation is
exercise 10, not 12.
Chapter 6 notes. Opening chart as briefed with Smith (1962), but from his printed Table 1 (period averages and the
coefficient of convergence), not read off his charts; the scanned article was rendered and read. Ten tests with three or
more periods are in the src table; six are charted, including the two that did not reach the prediction (4A, 9A). The
three-equilibrium economy is the classic quasi-linear example with $r = 2^{8/9} - 2^{1/9}$; its excess demand swings are
tiny, so the figure plots $1000 z_1$ on a log price axis. Existence is admitted in general and proved for two goods with the
intermediate value theorem. The core is defined and its shrinking proved for the two-replica case (exercise 12).
Chapter 7 notes. Opening chart deviation: the brief's rail candidates (Liverpool--Chicago gap, O'Rourke--Williamson, Jacks)
had no table reachable; Persson (2002, Copenhagen DP 02-02, later ERHE 2004) prints Table 3, the London--New York wheat
gap split into freight, charges and residual, and its own conclusion (market efficiency more than freight) is reported. The
record box is therefore "Shipping and the law of one price" (not railways); the problem keeps the railway, with invented
towns. No photograph. Assumption list points to ch. 2, 10, 15, 17, 18, 24 and to the Year 3 volume for public economics.
Chapter 8 notes. Opening chart deviation: no calibration table in Snowberg--Wolfers (their Figure 1 only), so the chart
shows the four rates of return the paper prints in its text (favourite -5.5, 4/1--9/1 -18, random -23, 100/1+ -61). The
second [L] chart (election-market error by days before the vote) had no table; replaced by Zhang (2018) Table 12.2 (China's
coal output by mine type, 1978--84) for the dual-track section, and the Iowa market numbers (1.91 / 1.49 / 1.58, 9 of 15)
went into the record box. Lau--Qian--Roland is cited for the interpretation only (its PDF copy holds two pages). Jordan
(1982) and Grossman--Stiglitz (1980) cited for theorems, not ledgered. "Hayek's result" appears only as a label in a remark.
Chapter 9 notes. Opening chart: the brief's "share with a Condorcet winner, by dataset" became the Table 7 flaw rates of one
dataset (182 elections; one without a Condorcet winner, computed 0.55 %), since no second dataset table was read. The
record box became the chart's own text. Pommerehne (1978) cited in the model box for what was estimated, not for a result
(abstract not reachable; citation details vary across sources). Arrow proof follows the pivotal-voter argument in 4 steps.
Chapter 10 notes. Opening chart deviation: round-by-round contributions exist only as figures, so the chart shows Tables 3
and 4 (mean over ten periods and final period, strangers/partners, without/with punishment) as per cent of the 20-token
endowment. Ostrom (1990) cited as a book of cases (no number); the Nobel lecture PDF returned 403 and the Nepal irrigation
numbers could not be verified, so no field number is printed. Removed an unsourced claim about how many rounds of
iterated reasoning laboratory subjects perform.

**Page projection at chapter 10:** chapters 1--10 fill pp. 2--131 (13.0 pp a chapter) and their solutions about 2.8 pp a
chapter; 34 x 15.8 + front matter and index gives about 550 pp against the 460 target: above target, no depth to restore.
Chapter 11 notes. Opening chart deviation: no penalty-kick field table was reachable (Palacios-Huerta 2003 not online;
the Volij copy failed on its certificate, the ministry copy 403), so the opener is the Wimbledon serve data (Walker--Wooders
2001 Table 1, 40 point games, parsed from the author's copy; server names dropped from the labels). The penalty-kick
numbers are the laboratory game of Palacios-Huerta--Volij (2008) as reported by Wooders (2008). The record box is
"Serves at Wimbledon" only (no field penalty record).
Chapter 12 notes. The opening chart uses Henrich et al. (2001) Table 1 (18 groups; Lamelara and Khazax have no
usable rejection rate). The debate uses Andersen et al. (2011) Tables 1--2; Cameron (1999) is cited only as summarised
there (its own text was not read). The "tested" line of the alternating-offers model box cites only the ultimatum
experiments: no strike-duration source was read, so the box says only that the model cannot produce a delay.
Chapter 13 notes. The discount factor is written beta, not delta as in the brief, to keep the series' reserved symbol.
Levenstein--Suslow's Figure 1 (a histogram of the 1990s sample) has no readable numbers, so the opener plots Table 1
(averages and ranges of nine samples). The eBay record cites the March 2006 working-paper version of Cabral--Hortacsu
(published JIE 2010) because the published copy was unreachable; it is cited as 2006. No laboratory source for
collusion was read, so the model box's "tested" line cites the cartel record only.
Chapter 14 notes. Opening-chart deviation: no Cox--Roberson--Smith or Cox--Smith--Walker table was reachable, so the
opener uses the per-subject risk-aversion estimates of Bajari--Hortacsu (2003, NBER WP version of the 2005 JPE paper),
converted back to fitted bid slopes by their own formula slope = (N-1)/(N-r). The oil-lease record and the jar
experiment are taken from Thaler (1988), which summarises Capen--Clapp--Campbell (1971), Hendricks--Porter--Boudreau
(1987, the brief named Hendricks--Porter 1988) and Bazerman--Samuelson (1983); none of those originals was read.
Page numbers shifted by one from chapter 14 on (front matter grew).
Chapter 15 notes. The debate box relies on the Chiappori--Salanie (2012) handbook survey for Chiappori--Salanie (2000),
Cohen (2005), He (2009) and Fang--Keane--Silverman (2008); Cohen--Einav (2007) was not read and is not cited. The
Massachusetts record uses only the AER abstract (no year or penalty details printed). The lemons model box was folded into
the text: no used-car or truck source was read, so the only model box is the demand-and-cost-curve one.
Chapter 16 notes. Hungerford--Solon (1987) and Tyler--Murnane--Willett (2000) are cited only as summarised by
Clark--Martorell (2014), the one paper read; the screening model box's "tested" line uses Finkelstein--Poterba (ch. 15),
as no phone-plan source was read. Opening chart: the brief's sample as asked, all ages 16--55 (the dip at 9--11 years is
explained in the text).

**Tooling finding (2026-11-20, for the main session).** `tools/figdata.sh` never runs the figdata pytest files: its test
step is `ls figdata/$t/test_*.py figdata/$t/*/test_*.py`, and `ls` exits non-zero when either glob matches nothing, which
for a chapter (no subdirectories) or a year (no top-level tests) is always the case, so the `pytest` line is skipped and
the script prints OK. Running Book 4's tests directly (`cd figdata/bachelor-2/NN-slug && PYTHONPATH=../../lib python -m
pytest .`) found three red tests: two used `s.median` (a pandas method, not the column) in chs. 12 and 13, and ch. 2's
risk-sharing test expected the coefficient on average consumption to be 1 when the simulation implies 1 - KEPT = 0.85
(the chapter text already said 0.853 rejects 1). All three tests fixed; no chapter number changed. From ch. 16 on, Book 4
runs its figdata tests directly as well as through the harness.
Chapter 17 notes. RAND HIE: the brief named Manning et al. (1987); the record box uses the RAND research brief RB-9174
(Brook et al. 2006) instead, the one source read. The randhie chart keeps only plans without an individual deductible
(idp = 0): in the bundled data, individual-deductible person-years are coded with coinsurance 0 or 100, so the rate does
not describe those plans. Safelite: the paper's own per-cent figures (20, 44, 22) are charted, not exp(coef) - 1 (44.5, 21.8).
West Bengal: the record names the reform's legal share and registration figures, and says the study cannot separate share
from security of tenure.
Chapter 18 notes. Opening chart changed from the brief: CEDS US SO2 emissions (approved data) instead of the EPA
auction-price series (which would have meant reading ~18 EPA pages); the allowance price is a second, five-point chart from
the prices Schmalensee--Stavins quote. The Coase diagram became a worked numerical bargain in the text (the fourth diagram's
place is taken by the pivot listing). Schmalensee--Stavins read as the 2012 HKS working paper, cited as the 2013 JEP article.
Chapter 19 notes. The listing's instrumented lambda (0.62, s.e. 0.20) comes with a first-stage F of 2.5, and the text says
the instruments are weak; Campbell--Mankiw (1989) is cited from its NBER abstract only (the "half" reading), Hall (1978) from
an archived scan of the article (abstract and introduction). The rebate record uses the two AER abstracts only. The brief's
"announcement versus receipt" argument is not printed (no source read on announcement dates); the record's contrast is with
the model's few-per-cent first-quarter spending. Opening chart labels the consumption share of GDP chart with real GDP per
person ratios from WDI NY.GDP.PCAP.KD (2.4--2.7, Korea 18.7).
Chapter 20 notes. Opening chart deviation from the brief: not $I/K$ against $V/K$. Grunfeld's recorded capital stock is
tiny for some firms in the first years (General Motors 2.8 in 1935, Westinghouse 1.8), so ratios to it reach I/K = 9 and
V/K = 89 and the cross-firm correlation is driven by the common denominator. The chart instead divides investment and
market value by each firm's own 1935--1954 mean (correlation 0.57, slope 0.93). The D exercise is Grunfeld's levels
regression; its fixed-effects coefficients (0.110 and 0.310) match the textbook values for these data, which confirms the
rows are aligned as the literature uses them (no lag added). The housing record uses JST real house prices and the total
investment share (JST has no residential-investment series); no BEA residential figure is printed. FHP (1988) cited from the
NBER WP 2387 abstract, KZ (1997) from WP 5267, BBV (2007) from WP 12383; Hayashi (1982) is not cited (marginal = average q is
admitted without a name). The recession numbers (investment -31.4 %, consumption -1.9 %, 2007Q4--2009Q2) come from macrodata.

**Page projection at chapter 20:** chapters 1--20 fill pp. 2--239 (11.9 pp a chapter) and their solutions about 2.2 pp a
chapter; 34 x 14.1 + front matter and index gives about 500 pp against the 460 target: above target, no depth to restore.
Chapter 21 notes. The record "after 1815 and after 1945" became "after 1945" only: JST starts in 1870 and no source for
1815 was read (the Bank of England millennium dataset would be a download). The UK record is descriptive (JST: debt 270 to
47 per cent of GDP 1946--1975, nominal growth 8.9 %, inflation 5.7 %, real growth 2.0 %, mean long rate 6.4 %); it makes no claim
about primary surpluses or wartime coupons. The 1953 record uses the Guinnane (2004) abstract as summarised on RePEc (the
paper itself refused the connection; AgEcon and CEPR pages 403). Kumar--Woo (2010) not read, not cited. The offset chart
uses 2000--2007 vs 2010--2017 averages instead of the brief's 1995--2019 two decades: it keeps 87 countries (60 with
1995--99) and straddles the crisis. The listing's stabilising balances use 2019--2024 nominal growth; the D exercise
shows they change with a 2014--2024 window (Italy -1.56 to -0.13). Notation: nominal growth is $\gamma$ (series $g$ is
government purchases).
Chapter 22 notes. The UN World Population Prospects 2024 projections (2050, 2100) are not printed: the summary PDF
exceeded the fetch size limit and the un.org copies returned 403, so the opening chart stays at 1960--2025 with no
projection in prose. Added a second chart not in the brief: the Abel et al. (1989) test applied to PWT 2019 (capital
income = 1 - labsh against csh_i; 137 of 140 above the line; exceptions BRB, CHN, CUW) -- the record box cites only the
NBER WP 2097 abstract for the paper's own conclusion. Listing line cap: the gate refuses listings over 40 lines (olg.py
shortened to 38).
Chapter 23 notes. The brief's "speed-of-convergence estimate" (Barro--Sala-i-Martin 1992) is cited only through the
JPE abstract on RePEc (convergence in US states, reconciled with the neoclassical model only if diminishing returns set in
very slowly); no "2 per cent a year" figure is printed, since neither the RePEc nor the NBER w3419 abstract states it.
The phase diagram plots the saddle path computed by the figdata script (shooting from k*/4 and 2k*), so it is exact for the
chapter's parameters. The third planned diagram (time paths) is the model-simulation chart. The Jacobian's entry b is
exactly -0.0048 and the eigenvalues exactly 0.08 and -0.06 for these parameters.
Chapter 24 notes. "Creative destruction" is recalled, not defined: Book 2 (g12 `ideas-institutions-growth`) owns it and
ch. 24 only tells the replacement model, so the R1 re-founding rule does not apply; DEFINITIONS.md row 210 updated. Bloom
et al. (2020) cited from the AEA and NBER abstracts only (the 18-fold Moore's-law figure; no aggregate factor or per-cent
decline is printed). Jones (1995) from the QJE abstract on RePEc. No D exercise (the brief had none); exercise 8 modifies
the listing.
Chapter 25 notes. Alesina--Summers (1993) read in full (scanned PDF from an author-hosted copy; Table A1 transcribed from
the rendered page): the 16 index values and the paper's own averages are ledger rows; the chart recomputes inflation from
JST for the 15 countries JST covers (no New Zealand). Inflation-target adoption years from the Bank of England CCBS
Handbook 29 (2012), 27 countries; where the handbook gives an informal and a formal date the formal/fully fledged year is
used (Israel 1997, Ghana 2007, Serbia 2009; Sweden 1993 announcement). Cukierman--Webb--Neyapti (1992) not cited: no
abstract could be read (RePEc has none, OUP and World Bank pages gave no text, the World Bank PDF 404); the debate box uses
Alesina--Summers and Campillo--Miron only. The US Phillips chart stops at 2008 (2009 has three quarters in macrodata).
Chapter 26 notes. The opening chart uses the approved Eurostat tables (euro area EA21, 2009-Q1 to 2025-Q4; une_rt_q
starts in 2009), so no fallback or new data was needed; the brief's "record[The Beveridge curve after 2008 and after
2020]" is folded into the opening chart's prose. The brief's third diagram (shifts after a benefit rise) is drawn inside
the two others. The brief's "Brenmoor" is read as Brenland (Brenmoor is the computer-science series' town). The bargaining
power is a local beta (declared in the notation box; the series' beta is the discount factor). Shimer (2005), Card--Chetty--
Weber (2007) and Lalive (2008) from abstracts only.
Ch. 25 change after the traps list: the US point of the opening chart now uses BLS CPI-U (4.51) instead of JST (4.36);
fit slope -1.83, intercept 10.29. Ch. 24: thousands separator changed to a thin space.
Chapter 27 notes. Opening chart uses the actual federal funds rate (H.15, approved and loaded) instead of the brief's
T-bill stand-in. Taylor (1993) read in the scanned author copy (rule and its definitions, p. 202). The 2021--23 record uses
H.15 and BLS data only, no FOMC statement rows (the dates of the moves come from the monthly funds rate). Taylor rule is
re-founded with a formal definition (Book 2 g12 defines it informally; SERIES_DEFINITIONS gives it to Y2). The HP filter is
used for the opening chart's gap and named in the caption; ch. 28 defines it. The forward-looking Phillips curve is told in
one paragraph.
Chapter 28 notes. Opening chart uses the 17 JST countries with data from 1870 (Ireland, from 1922, left out), so "median
of 17" as the brief says. The lowest ten-year volatility is the decade to 2019 (median 0.89), not to 2007: the text says so.
NBER dates and the dating procedure from the NBER pages (ledger rows); Hamilton (1983) abstract read from a course copy of
the JSTOR scan (RePEc and EconPapers carry no abstract). Identification (28.5) is told without citations. The model box's
"tested" uses the chapter's own moment table, not a calibration paper (none was read).
Chapter 29 notes. Bank run, deposit insurance and lender of last resort re-founded (g11 defines them in words;
SERIES_DEFINITIONS gives bank run and LLR to Y2 for re-founding; deposit insurance was listed "own" here but g11 also
defines it, so it is a re-found too). Maturity transformation: g11 has it in prose only, so defined here (own). "Brenmoor
savings bank" written as a Brenland savings bank (as in ch. 26). One photograph (first in Book 4): Northern Rock queue,
Brighton, 14 Sep 2007, Dominic Alves, CC BY 2.0, licence page read; credited in images/book4/CREDITS.md and
frontmatter/image-credits-book4.tex. 2008 dates from the St. Louis Fed FRASER timeline (not every Wikipedia-style claim:
the BNP and Northern Rock lines say only what FRASER says). The model box's "tested" uses FDIC suspension counts 1930--33
against nine insured failures in 1934, flagged as not a clean test. "Most crises follow a credit boom" dropped: the chart
compares averages only. Opening chart: 2010s show 0 crisis starts in JST crisisJST.
Chapter 30 notes. Data: `nsw("cps_controls")` (approved). Sample: men with positive 1975 and 1978 earnings (13,055).
Found and printed: 25.9 % of the 15,992 men sit at the 1978 maximum (25,564.7), a cap; the measure box says so and Exercise
2 asks what it does. Outputs print only machine-independent checks (allclose True), never 1e-12-sized differences. The
dummy-variable trap is described as perfect collinearity only (ch. 32 owns the term). OLS estimator not re-defined (Y1
owns it, R3). Brenland problem uses heads with positive gross income (1,922); experience = age - school - 6 is exactly
collinear.
Chapter 31 notes. Opening chart deviates from the brief: ratio of robust to classical SE per coefficient (bars),
since the ten intervals differ in scale by two orders of magnitude; the intervals themselves are in out/se.csv and the
robust_se listing. The ratio column is rounded to two decimals, as the listing prints it (0.955 would show 0.96 against
the listing's 0.95). Weekend problem: three sector clusters give a clustered SE a third of the robust one, the point of
Part IV. Bootstrap told, no listing. Coordinator rule S1 extension (author-year citations allowed in tested/breaks) noted.
Chapter 32 notes. Engel data: statsmodels `engel` (235 households, Belgian francs, Koenker--Bassett 1982 per the
dataset note; the text does not date the budgets, since the note does not). Problem III's reliability ratio 0.8 is an
invented validation-study figure, stated as such in the problem. RESET and leverage told. The model box is "Classical
measurement error" (the brief had none; the gate wants one per chapter's main model).
Chapter 33 notes. Matching and propensity scores left to Book 5 (said in print). Natural experiment re-founded as an
idea only; the designs (IV, DiD, RD) named as Year 3 material. Weekend problem: seeded simulation (seed 33, 800 workers);
the RCT estimate 1,100 is 1.1 s.e. below the true 1,499 (a chance draw, kept: the interval covers it). Survey comparison
with controls gives 794 against 1,794: the LaLonde point made on the DW subsample with the CPS controls.
Chapter 34 notes. Opening-chart seed 36 picked to show a related-looking pair (said in print: "The pair was picked to
make the point"); the listing gives the honest rate (84 per cent rejections in levels). Forecast model is an
autoregression on past inflation, not a Phillips curve; the D exercise adds unemployment (RMSE 1.775, no gain), matching
Atkeson--Ohanian's direction. statsmodels 0.15 warns on adfuller's tuple return, so the listing passes
result_object=False. HAC: the Newey--West t is -1.9, so significance at 5 per cent is lost (text says so). Brenland's
Dickey--Fuller fails to reject at 5 per cent (p 0.063) despite phi 0.48: the low-power lesson.

**Phase C (2026-11-20).** Term links: `--unwrap --apply`, then `--apply`; first pass 1,876 links, of which about 430
pointed ordinary words at game-theory definitions ("value" 296, "type(s)" 130, "support", "complete", "feasible",
"credible", "lottery" for random assignment, "signals" for cash flow, "p-value" and "critical value" at the value of a
game). Curated `tools/term_config/book4_en.py` (STOP 10 words, DROP 6 compounds, 6 EXTRA_PROTECT patterns): 1,443 links,
`--check` clean. Full per-figure pass: 141 figures (56 charts, 85 diagrams) on 122 pages rendered in 21 contact sheets,
plus the photograph; no defect found (ch. 34's forecast chart ticks had been thinned before). No PNG in `images/book4/ai/`,
no stub. Fresh forced build (`latexmk -g`): 455 pp, 0/0/0. `gates.sh bachelor-2` OK, `figdata.sh bachelor-2` OK (97
tests), `test_code.sh bachelor-2` GREEN (156 tests, 54 listings and outputs rerun).
- **Next action:** Phase D report sent; wait for the main session's verification.

## Web fetches

| Phase | Count | Notes |
|---|---:|---|
| A | 21 | programme texts (Nanterre L2 booklet, Lille MIASHS syllabi, Dauphine L2 page, Paris 1 guide, TSE: connection resets), textbook contents (Varian 8e, Romer 5e, Wooldridge 4e) |
| ch. 1 | 12 + 5 searches | KT 1979 (course copy, ok), Rabin 2000 (403s; MIT OCW handout ok), Sydnor 2010 (abstract only), Collier et al. 2018 NBER (ok) |
| ch. 2 | 5 + 2 searches | Townsend 1994 (AgEcon 403; MIT copy ok), Karlan et al. 2014 (IPA 500; NBER w18463 ok) |
| ch. 3 | 4 + 2 searches | BLS CE Table 1300 (published table, 33 KB xlsx); DellaVigna--Malmendier 2006 (RePEc abstract); Augenblick et al. (NBER w18734 PDF) |
| ch. 4 | 6 + 3 searches | Mehra 2003 NBER w9512 (PDF, ok); Fama--French 1992, Shiller 1981 (RePEc abstracts); Marsh--Merton, Campbell--Shiller (search records) |
| ch. 5 | 16 + 5 searches | Camerer 2016 MPRA manuscript (PDF) and Caltech SM (PDF, Table S1 rendered); Madrian--Shea w7682 (page + PDF); NBER w29453 (wrong paper, unused); RePEc abstracts CLK 2009, List 2003, CBLT 1997, KKT 1990; Farber 2015 (404, then search); Tversky--Kahneman 1992 (doi, Springer, course copy 404, Utah certificate refused; unused) |
| ch. 6 | 1 + 1 search | Smith 1962 scanned PDF (gwern mirror; Table 1 rendered) |
| ch. 7 | 4 + 1 search | Hynes--Jacks--O'Rourke 2009 (TCD PDF, interwar, unused); NBER w14767 page (unused); Persson 2002 (KU PDF, used) |
| ch. 8 | 4 + 3 searches | NBER w15923 (used, text numbers); IEM results draft (used); LQR 2000 PDF (2 pages, abstract only); ANU Zhang ch. 12 (used) |
| ch. 9 | 3 + 2 searches | arXiv 2301.12075v2 html, fetched 3 times for Table 7 (used) |
| ch. 10 | 2 + 2 searches | UZH IEW WP 10 (used); nobelprize.org Ostrom lecture (403, unused) |
| ch. 11 | 4 + 2 searches | Volij ECTA copy (certificate error); mintur PDF (403); Wooders 2008 (used); Walker--Wooders AER copy (used) |
| ch. 12 | 4 + 2 searches | Henrich AER copy at umass (403), eva.mpg (404), course copy (used); Andersen et al. author copy (used) |
| ch. 13 | 3 + 2 searches | Levenstein--Suslow author copy (used); luiscabral.net (refused); NYU archive working paper (used) |
| ch. 14 | 4 + 3 searches | Fullbrunn--Neugebauer (certificate error); NBER w9889 (used); AEA JEP pdf (403); Thaler copy at Chicago Booth (used) |
| ch. 15 | 3 + 3 searches | Finkelstein--Poterba MIT copy (used); HKK AEA abstract page (used); Chiappori--Salanie 2012 survey (used) |
| ch. 16 | 2 + 2 searches | Clark--Martorell course copy (used); RePEc JPE page 404 (not used) |
| ch. 17 | 6 + 2 searches | Lazear course copy (used); BGG author copy (used); RAND brief (used); unimi Lazear copy certificate error, LSE econ host refused, ISID certificate error, Queen's slides certificate error (not used) |
| ch. 18 | 5 + 2 searches | HKS Schmalensee--Stavins (used); Cheung archived scan (used); Hoesly et al. GMD abstract (used); AEA JEP PDF 403 (not used) |
| ch. 19 | 8 + 2 searches | AEA JPS 2006 and PSJM 2013 abstract pages (used); NBER w2924 (used); NBER w0015 (wrong paper, not used); RePEc Hall page (no abstract); Chicago and SSRN pages 403 (not used); archived Hall scan (used) |
| ch. 20 | 3 + 0 searches | NBER w2387, w5267, w12383 abstract pages (all used) |
| ch. 21 | 9 + 4 searches | NBER w15639 (used); RePEc PERI wp322 and IMF wp 14/34 (used); Bohn author copy (used); RePEc Guinnane abstract (used); CEPR VoxEU 403, AgEcon 403, PSE copy refused, Yale eliScholar (no abstract) (not used) |
| ch. 22 | 4 + 1 search | NBER w2097 (used); UN WPP 2024 summary (size limit), un.org summary PDF 403, un.org ageing page 403 (not used) |
| ch. 23 | 2 + 0 searches | RePEc JPE Barro--Sala-i-Martin abstract (used); NBER w3419 (no rate stated, not used) |
| ch. 24 | 3 + 0 searches | NBER w23782, AEA abstract page, RePEc Jones 1995 (all used) |
| ch. 25 | 9 + 3 searches | Alesina--Summers PDF (used), CCBS handbook PDF (used), NBER w5540 (used), Philadelphia Fed SPF page (used), NBER chapter page, RePEc CWN, OUP CWN, World Bank CWN page and PDF (no abstract, not used) |
| ch. 26 | 3 + 0 searches | RePEc Shimer 2005, NBER w12639, RePEc Lalive 2008 (all used) |
| ch. 27 | 5 + 0 searches | RePEc Taylor 1993 (no abstract), Stanford scan of Taylor 1993 (used), RePEc CGG 2000 (used), NBER w28005 (used) ; Taylor PDF counted once more for the page render |
| ch. 28 | 8 + 1 search | NBER FAQ and peak/trough table (used), NBER w9127 (used), RePEc McConnell--Perez-Quiros (used), RePEc and EconPapers Hamilton (no abstract), course copy of Hamilton 1983 (used) |
| ch. 29 | 11 + 3 searches | RePEc abstracts DD1983, DKD2002, ADZ2014, ST2012, FT2018 (used); Gorton 1985 (IDEAS 404; abstract via search of EconPapers/Cambridge, used); Fed History Panic of 1907 (used), Great Recession and Subprime essays (not used); FRASER crisis timeline (used); FDIC 1930--39 history (used); FDIC brief-history page (404); Commons file page + image (photo) |
| ch. 30 | 1 | Dehejia NSW data page (used) |
| ch. 33 | 3 | RePEc abstracts Krueger 1999, Allcott 2015, LaLonde 1986 (used) |
| ch. 34 | 2 | Minneapolis Fed page (404); RePEc abstract Atkeson--Ohanian 2001 (used) |
| triage | 1 | Persson (2002) KU WP 02-02 PDF, re-read for R4-007 (used: the 23 per cent runs to 1896--1900) |
| **total** | **217** | |

## Programme sources read (provenance only, never printed)

- Université Paris Nanterre, L2 économie-gestion booklet (Micro B S3, Micro C S4, Macro B, Macro C, statistics).
- Université de Lille, licence MIASHS economics syllabi 2020–2024 (S3 macro approfondie, S3 décisions microéconomiques,
  S4 équilibre général et économie publique, S4 monnaie banques marchés; S5–S6 jeux, choix social, incertain).
- Université Paris Dauphine-PSL, L2 sciences des organisations (course titles only).
- Textbooks: Varian, *Intermediate Microeconomics* 8e (contents); Romer, *Advanced Macroeconomics* 5e (contents, publisher
  page); Wooldridge, *Introductory Econometrics* 4e (contents).

## For the shared docs

- The statsmodels bundled datasets `macrodata`, `grunfeld`, `randhie`, `engel`, `longley`, `strikes`, `danish_data` carry a
  public-domain `COPYRIGHT` string in statsmodels 0.15.0; `star98`, `copper`, `fair` are "used with permission" and
  `fertility` is WDI — do not use those four.
- JST `crisisJST`: 88 crisis years 1870–2020, none in the 1940s–1960s.
- statsmodels 0.15: `adfuller` prints a FutureWarning into captured outputs unless called with `result_object=False`;
  `grangercausalitytests` no longer takes `verbose` (TypeError).
- A test that compares a printed 3-decimal figure with `round(np.float64, 3)` can disagree with the f-string the
  listing used (0.0595 prints 0.059, numpy rounds to 0.06): format the test value with the same f-string.
- Term linker: a single-word definition ("value" of a zero-sum game, "type" of a player) links every ordinary use across
  the book; STOP it, and protect compounds such as "p-value" and "critical value" with EXTRA_PROTECT (DROP alone did not
  stop "p-value" inside the defining chapter).
- WDI `GC.NLD.TOTL.GD.ZS` starts in 1972 and covers 34 countries in 1972, 85 in 2000: cross-country saving–deficit work
  needs 1995 onward.

## Fresh-reader triage (2026-11-20)

All 49 defects of `sources/book4/READER_REPORT.md` fixed, none rejected; the Resolution column records each. Changed
charts: ch. 19 (Germany from 1991), 20 (BLS deflator, record only), 22 (WDI investment at national prices, 129 economies),
23 (Korea K/Y from 1980, initial-stock share tested), 29 (war-free paths, credit window ending t - 1). New or changed
listings and outputs: ch. 3 life_plan, ch. 15 unravelling, ch. 24 ideas (balanced-path start). New independent tests: ch. 16
pooled-contract grid search, ch. 19 Germany, ch. 20 BLS M13 route, ch. 21 growth identity, ch. 22 recount, ch. 23 hand
perpetual inventory, ch. 24 closed form, ch. 33 trainee count. One deviation from the reader's numbers: R4-040 filters the
whole credit window for war years, so 13.35/10.55 (63 crises) rather than 11.85/9.18.

