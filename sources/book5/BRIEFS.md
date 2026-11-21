# Book 5 (University Year 3, `bachelor-3`, prefix `b3`) --- chapter briefs

Phase A, 2026-11-20. Owner: the Book 5 writer. Binding inputs: `sources/BATCH_BOOKS_1-5.md`, `OUTLINE.md` (Book 5,
the ownership maps), `../economics_series.md`, `CONTRIBUTING.md`, `sources/SERIES_DEFINITIONS.md`, `sources/data_ledger.md`.
Terms and labels are listed once more, flat, in `DEFINITIONS.md`.

## Conventions of this file

- **Data status of each chart**:
  - **[A]** approved dataset through `econdata` (loader, series, years checked on 2026-11-20 against `data/derived/`);
  - **[L]** a *cited table*: a small table of published numbers (a paper's table, an agency's page), one ledger row per
    number, written to `out/` by a figdata script that checks every row's ledger id. **Needs a sync ruling** (report,
    "Shared files"); fallback named each time;
  - **[S]** simulated by the chapter's seeded script, calibrated on a study's published moments (ledger), and the caption
    says "simulated";
  - **[B]** Brenland / Kestria (`country`);
  - **[?]** needs a dataset not approved (report, "Data to approve"); the fallback is what gets written meanwhile.
- **Exercises**: 12 per chapter, in order 4 x ★, 5 x ★★, 3 x ★★★. Kinds: **R** read a chart or table, **C** compute,
  **P** predict a direction and a size with a model, **X** say what observation would contradict the model. **(py)** marks a
  data exercise with a tested solution in `code/bachelor-3/NN-<slug>/exercises/`.
- **Weekend problem**: 22--28 questions, Parts I--IV, building to a named quantified result.
- **Listings** (Part I and ch. 10 only): `code/bachelor-3/NN-<slug>/listings/<stem>.py`, output `outputs/<stem>.txt` by
  `tools/capture_output.py`, test `tests/test_<chapter>.py`. Shared helpers (never printed): `code/bachelor-3/lib/`
  (`ivtools.py`: 2SLS with robust and clustered errors, first-stage F; `rdtools.py`: local linear fit with a triangular
  kernel; `synth.py`: synthetic-control weights by `scipy.optimize`), each with its own tests.
  Every simulation is seeded; every estimate is tested to a tolerance.
- **Page budget**: 36 chapters x 13.6 pp = ~490 pp. Each chapter: body ~600 source lines, solutions ~300, 2--4 charts,
  2--4 diagrams.
- Recall sources are named the way the book will print them: "the Year 1 volume" (Book 3), "the Year 2 volume" (Book 4),
  "the grades 10--12 volume" (Book 2), "the mathematics books".

---

# Part I --- Econometrics II: establishing cause

The part assumes Book 4 Part VI (multiple regression in matrix form, OVB formula, robust and clustered errors, potential
outcomes, randomisation) and Book 3 Part VII (pandas, statsmodels, sampling and inference). It recalls those in prose and
never re-teaches them. All six chapters print tested Python.

## 01 `instrumental-variables` --- Instrumental Variables

- **Programme items**: endogeneity (L3 econometrics courses: "Introduction à l'économétrie", "Econometrics 3:
  applications"); IV and 2SLS; weak instruments; LATE (Angrist--Pischke, *Mastering 'Metrics* ch. 3 and 6).
- **Sections**: 1 Endogenous regressors (three sources: omitted variable, measurement error, simultaneity --- recalled
  from the Year 2 volume, made one problem); 2 The instrument and the Wald estimator; 3 Two-stage least squares (matrix
  form, the first stage, the reduced form, standard errors, over-identification told); 4 Weak instruments; 5 Who the
  estimate is about: the local average treatment effect; 6 Instruments examined (quarter of birth, weather, geography,
  lottery draws; what was found wrong with some).
- **Defines**: endogenous regressor; instrumental variable (relevance, exclusion); Wald estimator; reduced form; first
  stage; two-stage least squares; weak instrument (first-stage $F$); compliers, always-takers, never-takers, defiers;
  monotonicity; local average treatment effect.
- **Propositions with proofs**: consistency of the IV estimator (plim argument, LLN recalled from the Year 1 volume);
  2SLS = IV with the fitted first stage; the bias of 2SLS towards OLS with weak instruments (simulation + the
  approximate formula, told); the LATE theorem (Imbens--Angrist) proved for a binary instrument and treatment.
- **Models**: none in a model box (method chapter); the *returns-to-schooling equation* used as the running example is
  Book 5 ch. 24's model, previewed only.
- **Recalls**: OVB formula, robust errors, potential outcomes and ATE (Year 2 volume); conditional expectation (Year 1
  volume); simultaneity of supply and demand (Year 1 volume, `models-and-data`).
- **Opening chart (proposal A, approved data)**: *a country's trade share against the trade share its geography
  predicts* --- the first stage of the geographic instrument (Frankel--Romer type). [A] `gravity(2019, columns=[year,
  iso3_o, iso3_d, tradeflow_baci, dist, contig, pop_o, pop_d])` gives a bilateral geography-only fit; aggregated to a
  predicted trade share; actual trade share `wdi("NE.TRD.GNFS.ZS", 2019, countries_only=True)`. ~150 countries.
  **Proposal B (the outline's chart)**: years of schooling and log weekly earnings by quarter of birth --- [L] from the
  published group means of the quarter-of-birth study (Angrist and Krueger 1991, QJE, Table III, men born 1930--39),
  or [?] the study's extract. Recommendation: A as the opening chart, B as the worked Wald example (4 numbers, a
  `measure` box). The sync decides.
- **Other charts**: (2) the weak-instrument simulation: sampling distribution of OLS and 2SLS at first-stage $F$ = 2, 10,
  50 [S]; (3) second stage of the geographic instrument: log output per worker (PWT `rgdpo/emp`, 2019) against the fitted
  trade share [A].
- **Diagrams**: the causal graph $Z \to D \to Y$ with the confounder $U$, and the exclusion arrow that is not drawn; the
  four compliance types as a 2x2 table-diagram; supply and demand with a demand shifter tracing the supply curve
  (simultaneity, with numbers matching an exercise).
- **Photos**: none.
- **Boxes**: `measure[The first-stage F statistic]` (Staiger--Stock rule of thumb, Stock--Yogo critical values,
  Lee--McCrary--Moreira--Porter 2022 "$tF$" correction told); `record[Quarter of birth and the weak-instrument critique]`
  (Angrist--Krueger 1991; Bound--Jaeger--Baker 1995 showed random quarter-of-birth instruments reproduce the estimate
  with 180 interactions); `record[Rainfall as an instrument]` (Miguel--Satyanath--Sergenti 2004 rainfall and conflict;
  Sarsons 2015 on the exclusion restriction failing in dams districts).
- **Listings / outputs / tests**:
  - `ability_bias.py`: simulated wages with unobserved ability and a binary instrument (seeded, $n$ = 20,000); prints OLS,
    the Wald estimate, the truth. Output `ability_bias.txt`.
  - `tsls_by_hand.py`: 2SLS in matrix form with numpy; checks against the helper `ivtools.tsls`; prints both and the
    first-stage $F$. Output.
  - `weak_iv.py`: 2,000 replications at three instrument strengths; prints the median bias of OLS and 2SLS and the
    rejection rate of a nominal 5 % test. Output (also feeds chart 2 through figdata).
  - `late_sim.py`: compliers, always- and never-takers with different effects; prints ATE, ATT, LATE and the Wald
    estimate.
  - `geography_iv.py`: the geographic instrument on approved data: first stage, OLS, 2SLS; prints coefficients, robust
    errors, first-stage $F$.
  - Tests: estimates within tolerance of the simulation truth; Wald = 2SLS for one binary instrument; $F$ above 10 in the
    strong case; `geography_iv` first-stage slope positive with $F > 10$ (tolerance on the coefficient, not digits).
- **Exercises**: ★ 1 [R] read the first-stage chart: slope, outliers; 2 [C] a Wald estimate from four group means;
  3 [C] the bias of OLS from the OVB formula with given covariances; 4 [X] what would show the exclusion restriction false
  for distance to college. ★★ 5 [C] 2SLS by hand with a 3x2 design; 6 [P] direction of the OLS bias with measurement error
  vs ability; 7 [C] LATE from compliance shares (fractions of compliers, always-takers); 8 (py) [C] re-run
  `geography_iv` with population added as a control and compare; 9 [X] a placebo outcome for a lottery instrument.
  ★★★ 10 (py) [C] weak-instrument simulation at $F$ = 5: coverage of the 95 % interval; 11 [P] proof: with a binary
  instrument, IV = ratio of reduced form to first stage; 12 [X] monotonicity: construct a case with defiers where the
  Wald estimate has the wrong sign.
- **Weekend problem --- "The Brenmoor college lottery"**: Brenmoor's public college is over-subscribed and admits by
  lottery (invented, [B]-style seeded data in the problem text: offer rates, enrolment, earnings). Part I the naive
  comparison and its bias; Part II the lottery as an instrument (first stage, reduced form, Wald); Part III who the
  compliers are and what they earn (Abadie's $\kappa$ told as means of complier characteristics); Part IV a second campus
  where offers raise enrolment by less: weak-instrument diagnostics, then pooling. Named result: *the LATE of college on
  earnings in Brenmoor, with its 95 % interval*. 24 questions.
- **Ledger**: Angrist--Krueger 1991 (Table III Wald numbers); Bound--Jaeger--Baker 1995; Staiger--Stock 1997 ($F$ > 10);
  Lee et al. 2022 (AER, $tF$, critical value 104.7 for a 5 % test); Imbens--Angrist 1994; Miguel et al. 2004; Sarsons
  2015; Frankel--Romer 1999 (AER) estimate for comparison.

## 02 `panel-data` --- Panel Data

- **Programme items**: panel econometrics (L3 "Econometrics 3: applications"; Wooldridge-style intermediate chapters).
- **Sections**: 1 The same units over time; 2 Pooled regression and the fixed-effects model; 3 The within and
  first-difference estimators; 4 Random effects and the choice between them; 5 What variation identifies the coefficient;
  6 Errors that move together: clustering in panels; 7 Dynamic panels (told).
- **Defines**: pooled regression; unit fixed effect; within (fixed-effects) estimator; first-difference estimator;
  two-way fixed effects; random-effects estimator; identifying variation; dynamic panel bias (Nickell bias).
- **Propositions**: the within estimator = least squares with unit dummies (Frisch--Waugh, recalled from the Year 2
  volume, proved here in the panel case); FD = within when $T$ = 2; random effects consistent only if the effect is
  uncorrelated with the regressors (proof); Nickell bias of order $1/T$ (stated, $\admitted$, simulated).
- **Recalls**: Frisch--Waugh--Lovell and clustered errors (Year 2 volume); panel as a data shape (Year 1 volume,
  `economic-data-python`).
- **Opening chart**: *carbon dioxide per person against income per person: across countries (country means) and inside
  countries over time (deviations from the country mean)* --- two slopes, 3.0 between, 1.2 within in a first computation
  (tonnes per person per unit of log income). [A] `wdi("EN.GHG.CO2.PC.CE.AR5")` 1970--2024, `wdi("NY.GDP.PCAP.KD")`,
  `countries_only=True`, ~200 countries. Alternative with the same shape: fertility (between $-0.8$, within $-1.4$).
- **Other charts**: (2) a two-country illustration of within variation (two countries' paths, their means, the two
  fitted lines) [A]; (3) the Nickell-bias simulation: estimated persistence against $T$ [S].
- **Diagrams**: the "parallel lines" picture of fixed effects (three units, same slope, different intercepts, pooled
  line steeper); a cluster structure sketch (units x years, correlated shocks).
- **Boxes**: `record[Bertrand, Duflo and Mullainathan's placebo laws]` (2004 QJE: with iid errors, 45 % of placebo laws
  "significant" at 5 %); `measure[What a fixed effect absorbs]`.
- **Listings**: `pooled_vs_within.py` (WDI CO2 and income: pooled, between, within; prints three slopes); `dummies_vs_
  within.py` (identical coefficient both ways; prints both); `first_difference.py`; `random_effects.py` (statsmodels
  `MixedLM` or GLS by hand on a simulated panel; prints RE vs FE when the effect is correlated); `cluster_sim.py`
  (placebo treatments on a serially correlated panel: rejection rates with iid, robust and clustered errors); `nickell.py`.
  Tests: within = dummies to 1e-8; FD = FE at $T$ = 2; cluster rejection rate near 0.05, iid far above; Nickell bias
  shrinks with $T$.
- **Exercises**: ★ 1 [R] read the opening chart (signs, which slope is steeper and why); 2 [C] within transformation of a
  2-unit, 3-year table; 3 [C] FD by hand; 4 [X] what result would show the country effects were not constant.
  ★★ 5 (py) [C] add year effects to the within regression; 6 [P] direction of pooled bias when richer countries have
  cleaner technology; 7 [C] clustered vs iid standard error from a given design effect; 8 [P] RE vs FE: which moves when
  the unit effect correlates with $x$; 9 (py) [C] fertility: between and within slopes. ★★★ 10 [C] prove FD = FE at
  $T$ = 2; 11 (py) [C] Nickell bias at $T$ = 5, 10, 20 vs $-(1+\rho)/(T-1)$; 12 [X] a test of strict exogeneity
  (lead of $x$).
- **Weekend problem --- "Fifteen years of Brenland's firms"**: a seeded panel of 300 Brenland firms 2011--2025 (generated
  in the chapter's figdata from `country` firms' sizes; invented). Part I pooled regression of output on capital and the
  bias from unobserved management quality; Part II within and FD estimates; Part III a training subsidy given to some
  firms in 2018: two-way FE estimate; Part IV clustered errors and the interval. Named result: *the return to capital
  inside firms, and the subsidy's effect on output, each with a clustered 95 % interval*. 25 questions.
- **Ledger**: Bertrand--Duflo--Mullainathan 2004; Nickell 1981 (Econometrica) bias formula; Mundlak 1978 (told).

## 03 `difference-in-differences` --- Difference-in-Differences

- **Programme items**: DiD, event studies, synthetic control (*Mastering 'Metrics* ch. 5; L3 applied econometrics).
- **Sections**: 1 Two groups, two periods; 2 Parallel trends, and how to look at them; 3 The regression form and its
  errors; 4 Event-study plots; 5 Staggered adoption: what two-way fixed effects gets wrong, and the fixes; 6 Synthetic
  control.
- **Defines**: difference-in-differences estimator; parallel-trends assumption; event study; placebo test;
  staggered adoption; synthetic control (donor pool, weights).
- **Propositions**: DiD identifies the ATT under parallel trends (proof in potential outcomes); the regression with
  group, period and interaction gives the DiD; the TWFE coefficient is a weighted average of 2x2 comparisons with some
  negative weights under heterogeneous effects (Goodman-Bacon 2021, stated, shown in a three-cohort example computed by
  hand); synthetic-control weights solve a constrained least-squares problem (stated).
- **Recalls**: potential outcomes, ATT (Year 2 volume); clustered errors (ch. 2).
- **Opening chart**: *full-time-equivalent employment per fast-food restaurant in New Jersey and eastern Pennsylvania,
  February and November 1992* --- [L] Card and Krueger 1994 (AER) Table 3 (4 means + standard errors), or [?] Card's
  public file. Fallback on approved data: NSW treated vs CPS controls, mean earnings 1974, 1975, 1978 [A] (`nsw("nsw_dw")`,
  `nsw("cps_controls")`) --- a real two-group, before/after picture but not of regions.
- **Other charts**: (2) LaLonde's lesson: DiD of NSW treated against CPS and PSID controls next to the experimental
  benchmark [A]; (3) event-study plot on a simulated staggered panel [S]; (4) synthetic control: treated unit, its
  synthetic twin, the gap [S] (calibrated on Abadie--Diamond--Hainmueller 2015's published effect, ledger).
- **Diagrams**: the four-point DiD picture with the counterfactual dashed line; the Goodman-Bacon "forbidden
  comparison" (early vs late cohorts) as a timeline diagram.
- **Boxes**: `record[Fast food in New Jersey, 1992]` (the design only; the minimum-wage debate is ch. 26's);
  `record[LaLonde's test of non-experimental estimators]` (LaLonde 1986; Dehejia--Wahba 1999; Smith--Todd 2005);
  `record[Reunification and West German output]` (ADH 2015, the synthetic-control estimate, ledger).
- **Listings**: `did_two_by_two.py` (means table and the DiD, NSW vs CPS); `did_regression.py` (same by OLS with
  interaction and clustered errors); `lalonde_benchmark.py` (experimental vs DiD vs regression with controls); `event_
  study.py` (simulated staggered rollout, leads and lags); `bacon.py` (the 2x2 weights of TWFE in a 3-cohort simulation,
  and a clean "not-yet-treated" estimator); `synth_demo.py` (weights via `synth.py`, prints weights and pre-period
  RMSPE, placebo ranks). Tests: 2x2 = regression coefficient exactly; benchmark within tolerance of the published
  \$1,794 experimental estimate (Dehejia--Wahba sample, re78); Bacon weights sum to 1; synth weights non-negative, sum
  to 1.
- **Exercises**: ★ 1 [R] read the opening chart and compute the DiD; 2 [C] DiD from a 2x2 table of means; 3 [R] read an
  event-study plot (pre-trends); 4 [X] what pre-period pattern contradicts parallel trends. ★★ 5 [C] DiD in logs vs
  levels: when they disagree; 6 (py) [C] DiD of NSW vs PSID controls; 7 [P] Ashenfelter's dip: direction of the bias;
  8 [C] the TWFE weights in a two-cohort example; 9 [X] a placebo group for a regional tax change. ★★★ 10 (py) [C] event
  study with an anticipation effect; 11 [C] synthetic weights for a 3-donor problem by hand (a convex combination);
  12 [P] triple differences: when a third difference removes a bias.
- **Weekend problem --- "The Kestrian border tax"**: Kestria raises a sales tax in its western provinces only (invented
  panel of shops on both sides of the border, generated in figdata). Part I 2x2 DiD; Part II pre-trends and an event
  study; Part III staggered roll-out to the eastern provinces two years later and the TWFE trap; Part IV synthetic
  control for a single treated province. Named result: *the tax's effect on cross-border shopping, by three
  estimators, and why they differ*. 26 questions.
- **Ledger**: Card--Krueger 1994 Table 3; LaLonde 1986; Dehejia--Wahba 1999 (\$1,794 benchmark); Smith--Todd 2005;
  Ashenfelter 1978 (the dip); Goodman-Bacon 2021; Callaway--Sant'Anna 2021; de Chaisemartin--D'Haultf\oe uille 2020;
  ADH 2015.

## 04 `regression-discontinuity` --- Regression Discontinuity

- **Programme items**: RD designs (*Mastering 'Metrics* ch. 4).
- **Sections**: 1 A rule that jumps; 2 The sharp design; 3 Estimation: local linear fits and the choice of window;
  4 The fuzzy design (an IV at the threshold); 5 Can the running variable be manipulated? Tests; 6 Classic applications:
  class-size rules, score thresholds, age thresholds.
- **Defines**: running variable; cutoff; sharp regression discontinuity; fuzzy regression discontinuity; bandwidth;
  local linear regression (triangular kernel); manipulation test (density test); covariate balance test.
- **Propositions**: continuity of potential outcomes at the cutoff identifies the effect at the cutoff (proof); fuzzy RD
  = Wald ratio at the cutoff (proof, recalls ch. 1); bias of a local constant fit grows linearly in the bandwidth while
  local linear's grows quadratically (shown).
- **Recalls**: ch. 1 (Wald estimator, LATE).
- **Opening chart**: *an outcome against a score, with the jump at the threshold* --- [S] simulated, calibrated on a
  published sharp design (Lee 2008, U.S. House elections: incumbency raises the next vote share by about 7.7 points;
  ledger). The caption says "simulated, calibrated on". No approved dataset carries a real threshold.
- **Other charts**: (2) estimates against the bandwidth (the trade-off) [S]; (3) the class-size rule: predicted class
  size against enrolment, the saw-tooth (computed from the rule, Maimonides' rule with a cap of 40) and simulated
  schools [S] calibrated on Angrist--Lavy 1999; (4) density of the running variable with bunching just above a
  manipulated cutoff [S].
- **Diagrams**: sharp vs fuzzy: probability of treatment against the score (0/1 step vs partial jump); the local linear
  window with triangular weights.
- **Boxes**: `record[Class size in Israel]` (Angrist--Lavy 1999; the later re-examination Angrist, Lavy, Leder-Luis,
  Shany 2019 finding manipulation and no effect); `record[The minimum legal drinking age]` (Carpenter--Dobkin 2009
  mortality jump at 21); `measure[Choosing the window]` (Imbens--Kalyanaraman; Calonico--Cattaneo--Titiunik, told).
- **Listings**: `rd_sharp.py` (simulated; local linear at three bandwidths; prints estimates and robust errors);
  `rd_bandwidth.py` (bias--variance over 2,000 draws); `rd_fuzzy.py` (Maimonides rule on simulated schools; first stage
  and Wald); `density_test.py` (binned density, McCrary-style log difference); `balance.py` (covariates at the cutoff).
  Tests: estimate within tolerance of truth; fuzzy = Wald; density test detects the planted manipulation and not the
  clean case.
- **Exercises**: ★ 1 [R] read the jump off the opening chart; 2 [C] the Maimonides class size at enrolments 40, 41, 80,
  81; 3 [C] a sharp RD estimate from two local means; 4 [X] what a balance test failing would mean. ★★ 5 (py) [C]
  quadratic vs linear fits: global polynomial danger (Gelman--Imbens); 6 [C] fuzzy RD from jumps in treatment and
  outcome; 7 [P] direction of bias if students cluster just above a scholarship cutoff; 8 (py) [C] donut RD;
  9 [X] what result would show a cutoff was set after scores were known. ★★★ 10 [C] prove the local linear estimator's
  intercept difference equals a weighted difference of means; 11 (py) [C] coverage of the interval at small
  bandwidths; 12 [P] external validity: effect far from the cutoff.
- **Weekend problem --- "The Brenmoor scholarship"**: a scholarship for school-leavers scoring 70 or more; invented
  scores, take-up and later earnings. Part I sharp estimate of being offered; Part II take-up is partial: fuzzy RD;
  Part III window choice and a placebo cutoff at 60; Part IV a teacher can re-mark one exam: density test and what it
  finds. Named result: *the effect of the scholarship on earnings at the threshold, with its interval and its density
  test*. 24 questions.
- **Ledger**: Lee 2008; Angrist--Lavy 1999; Angrist et al. 2019 (AER: Insights); Carpenter--Dobkin 2009; McCrary 2008;
  Gelman--Imbens 2019; Calonico--Cattaneo--Titiunik 2014; Thistlethwaite--Campbell 1960 (named only as the first RD,
  as a result's label --- or omitted; no history).

## 05 `binary-outcomes` --- Binary Outcomes and Maximum Likelihood

- **Programme items**: limited dependent variables, ML estimation (L3 econometrics; discrete choice in IO courses).
- **Sections**: 1 When the outcome is yes or no; 2 The linear probability model; 3 Logit and probit as latent-variable
  models; 4 The likelihood and its maximum; 5 Marginal effects and how to report them; 6 Discrete choice from random
  utility, and the logit model of demand.
- **Defines**: linear probability model; latent variable; probit model; logit model; likelihood function;
  log-likelihood; maximum likelihood estimator; average marginal effect; random utility model; multinomial logit;
  independence of irrelevant alternatives; market share inversion (the Berry log-share equation).
- **Propositions**: the logit log-likelihood is concave (proof via the Hessian); score equations of logit = "fitted
  probabilities match observed shares by regressor" (proof); the Gumbel random-utility model gives logit choice
  probabilities (proof for two options, general case stated); IIA (proof); consistency and asymptotic normality of the
  ML estimator ($\admitted$, with the inverse information as the variance).
- **Model box**: `model{Random utility and logit demand}` --- assumes: utility = mean utility + iid extreme-value taste
  shock; predicts: shares $s_j = e^{\delta_j}/\sum e^{\delta_k}$, substitution in proportion to shares; tested:
  transport mode choice (McFadden's BART forecast of 1975, ledger) ; breaks: IIA (red bus / blue bus), substitution
  between close products (fixed by nested logit, random coefficients --- told).
- **Recalls**: logistic regression as a classifier is in the artificial-intelligence books (prose); this chapter takes
  the econometric reading (marginal effects, inference, structure).
- **Opening chart**: *share of men with earnings in 1978 against age, fitted three ways (LPM, logit, probit)* --- [A]
  `nsw("cps_controls")`, 15,992 men, outcome `re78 > 0`, age 16--55, fitted curves by figdata. Caption note: a
  survey sample of men, so "having earnings", not the labour-force concept.
- **Other charts**: (2) the log-likelihood of a one-parameter logit as a function of $\beta$, with Newton steps [A same
  data]; (3) LPM fitted values outside [0,1] (the same data, education and age) [A].
- **Diagrams**: latent index with threshold (the probit picture); the Gumbel densities and the choice between two
  options; nest tree for nested logit (told).
- **Boxes**: `record[Forecasting a new rail line from a logit model]` (McFadden 1974/2001: BART share forecast 6.3 %,
  realised 6.2 %, ledger to verify); `measure[Reporting a logit: odds ratios and marginal effects]`.
- **Listings**: `lpm_logit_probit.py` (fits on CPS controls; prints coefficients and AMEs side by side);
  `newton_logit.py` (Newton--Raphson by hand; prints the iterations and matches statsmodels); `marginal_effects.py`
  (AME vs effect at the mean); `logit_demand.py` (simulated market of 4 products: shares, Berry inversion recovers
  price coefficient by OLS of $\ln s_j - \ln s_0$ on price; prints own and cross elasticities, shows IIA).
  Tests: Newton = statsmodels to 1e-6; AMEs of logit and probit within 0.01; Berry recovers simulated
  $\alpha$ within tolerance.
- **Exercises**: ★ 1 [R] read the opening chart (where the three fits differ); 2 [C] a logit probability and its
  marginal effect at a point; 3 [C] odds ratio from a coefficient; 4 [X] what data would contradict IIA. ★★ 5 (py) [C]
  add education to the participation model; 6 [C] log-likelihood of 5 observations, by hand; 7 [P] logit demand: effect
  of a 1 % price rise on own and rival shares; 8 [C] Newton step for a one-parameter logit; 9 [X] a sign of
  misspecification in the LPM. ★★★ 10 [C] prove the logit score equations; 11 (py) [C] Berry inversion with a
  price-endogeneity problem: OLS vs IV with a cost shifter; 12 [P] a new product's share and whom it takes customers
  from under IIA.
- **Weekend problem --- "A new bus line in Brenmoor"**: commuters choose car, bus or bicycle (invented survey). Part I
  binary choice car vs bus by logit, by hand and by ML; Part II marginal effects of fare and time; the value of
  travel time; Part III three-way multinomial logit; Part IV forecast of the new line's share and the IIA caveat. Named
  result: *the commuters' value of travel time, in dalens per hour, and the new line's forecast share*. 25 questions.
- **Ledger**: McFadden 1974 / McFadden Nobel lecture 2001 (BART numbers); Berry 1994 (RAND J.).

## 06 `credible-empirical-work` --- Credible Empirical Work

- **Programme items**: "Données et tests", research methods; meta-analysis; replication.
- **Sections**: 1 How results get published; 2 Specification search and the garden of forking paths; 3 Low power and
  exaggerated estimates; 4 The replication record of economics; 5 Pre-registration and pre-analysis plans;
  6 Meta-analysis and funnel plots; 7 Reading a results table; 8 The evidence scale of this series.
- **Defines**: publication bias; specification search; exaggeration ratio (type M error); sign error (type S);
  reproduction; replication; pre-analysis plan; meta-analysis; funnel plot; precision-effect test (FAT--PET);
  evidence scale (the series' four grades for `debate` boxes).
- **Propositions**: under a significance filter, the expected published estimate exceeds the true effect (proof in the
  normal case, formula for the truncated mean); probability that the best of $k$ independent specifications is
  significant: $1 - 0.95^k$ (proof); FAT--PET regression: under no bias, the intercept of $t$ on precision is zero
  (derivation). Power (recalled from the Year 1 volume) used, not defined.
- **The evidence scale** (printed here, used by every later `debate` box): (1) several randomised or natural
  experiments that agree; (2) one strong design, or several that disagree in size; (3) correlations with controls and
  a plausible mechanism; (4) a theory with no design-based test yet. Each `debate` box tags its studies with this scale.
- **Recalls**: tests, $p$-values, power, many tests at once (Year 1 volume); ch. 1--4 designs.
- **Opening chart**: the outline's (heap of published $z$-statistics just above 1.96, Brodeur et al.) is not
  tabulated in the papers and its data need an account (openICPSR): not usable. **Proposal**: [L] *original against
  replication effect sizes for the 18 laboratory experiments of Camerer et al. (2016, Science)*, one row per study
  from the paper's table. **Contested** with Book 4 ch. 5 (`behavioural-evidence`, opening chart "original effect sizes
  against replication"): if Book 4 uses Camerer 2016, this chapter uses [S] a simulated significance filter for its
  opening chart and gives the published counts in a `record` box.
- **Other charts**: (2) exaggeration ratio against power [S, analytic]; (3) a funnel plot with and without a
  publication filter [S]; (4) the minimum-wage funnel is ch. 26's (forward reference in prose).
- **Diagrams**: the "forking paths" tree of analysis choices; a stylised results table with every part labelled
  (coefficient, standard error, stars, $N$, fixed effects, clustering).
- **Boxes**: `record[Replication of economics experiments]` (Camerer et al. 2016: 11 of 18 replicated, mean relative
  effect size 66 %, ledger to verify); `record[Reproducing published papers from their code]` (Chang--Li 2015/2022:
  29 of 59 macro papers reproduced without author help, ledger to verify); `measure[Power in economics]`
  (Ioannidis--Stanley--Doucouliagos 2017: median power about 18 %, ledger); `measure[The evidence scale]`.
- **Listings**: `significance_filter.py` (simulated studies of a true effect 0.1 with various $n$; prints the mean of
  published estimates and the exaggeration ratio); `forking_paths.py` (one null dataset, 16 defensible
  specifications; prints how many are significant); `funnel.py` (simulated literature with a filter; FAT--PET);
  `reading_table.py` (statsmodels `summary_col` of three nested regressions on NSW data, then the same numbers
  re-printed as a clean table). Tests: exaggeration ratio > 1 at low power; FAT intercept significant only with the
  filter; seeds fixed.
- **Exercises**: ★ 1 [R] read a results table (which number is the standard error, what the stars hide); 2 [C]
  $1-0.95^k$ for $k$ = 5, 20; 3 [C] power of a test given effect and SE; 4 [X] what would show a literature is not
  biased (funnel symmetric). ★★ 5 [C] exaggeration ratio at power 0.2 (normal approximation); 6 (py) [C] FAT--PET on a
  given table of 12 estimates; 7 [P] what pre-registration changes in the forking-paths simulation; 8 [C] a
  fixed-effect meta-analytic mean with inverse-variance weights; 9 [X] a replication that fails: what it does and does
  not show. ★★★ 10 [C] truncated-normal mean of published estimates (proof of the proposition); 11 (py) [C] random-
  effects meta-analysis ($\tau^2$ by DerSimonian--Laird); 12 [P] grade three published studies on the evidence scale and
  defend the grade.
- **Weekend problem --- "Twenty studies of a training programme"**: a literature of 20 invented evaluations of a
  Brenland job-training programme, sizes and SEs given. Part I the naive average; Part II funnel and FAT--PET; Part III
  a pre-registered large trial arrives; Part IV a meta-analytic estimate corrected for selection, and its grade on the
  evidence scale. Named result: *the bias-corrected effect of the programme and its grade*. 24 questions.
- **Ledger**: Brodeur et al. 2016 (AEJ: Applied), Brodeur--Cook--Heyes 2020 (AER) (described, numbers if tabulated);
  Camerer et al. 2016; Chang--Li 2022; Ioannidis--Stanley--Doucouliagos 2017 (EJ); Gelman--Carlin 2014; Stanley--
  Doucouliagos 2012/2014; AEA RCT registry founding date (dated fact, AGENCY).

---

# Part II --- International trade

Assumes Ricardo's two-good model, the PPF and the terms of trade (grades 10--12 volume) and the general-equilibrium tools
of the Year 2 volume. This part re-founds comparative advantage with many goods (ownership table "From school to
university"). Only ch. 10 prints code.

## 07 `ricardian-trade` --- Ricardian Trade in Full

- **Programme items**: Ricardian model (Krugman--Obstfeld--Melitz part 1; L3 "Commerce international", "Économie
  internationale I").
- **Sections**: 1 Two goods recalled, then many: the chain of comparative advantage; 2 A continuum of goods: the
  relative wage and the range each country makes (Dornbusch--Fischer--Samuelson); 3 Transport costs and non-traded
  goods; 4 A productivity gain abroad: who gains; 5 Many countries (told: Eaton--Kortum, the gains-from-trade formula
  of Arkolakis--Costinot--Rodríguez-Clare); 6 The tests: a country opened by force; crop yields and what regions grow.
- **Defines**: comparative advantage (many goods; re-founded); chain of comparative advantage; terms of trade
  (re-founded here with the general-equilibrium price: to confirm at sync); the Dornbusch--Fischer--Samuelson model;
  iceberg trade cost; non-traded good; autarky price; gains-from-trade formula (domestic expenditure share and trade
  elasticity).
- **Propositions**: with $n$ goods ranked by relative labour requirement, Home makes every good up to a cut-off set by the
  relative wage (proof); the DFS equilibrium exists and is unique (proof, the $A(z)$ and $B(z)$ curves); with iceberg
  costs, a band of non-traded goods (proof); a uniform productivity gain abroad raises Home's real wage (proof); the ACR
  formula $\hat W = \hat\lambda^{1/\varepsilon}$ ($\admitted$, applied with numbers).
- **Model box**: `model{The Ricardian model with many goods}` --- assumes: one factor, constant labour requirements
  differing across countries, perfect competition, balanced trade; predicts: each country exports goods of lowest
  relative labour cost, trade raises real wages in both; tested: Japan's opening (Bernhofen--Brown 2004), U.S./U.K.
  export ratios against productivity ratios (MacDougall 1951, Golub--Hsieh 2000), crop yields and land use
  (Costinot--Donaldson 2012); breaks: complete specialisation is rare; capital and land matter; firms differ.
- **Recalls**: Ricardo's two-good model, opportunity cost, PPF (grades 10--12 volume); the Edgeworth box and general
  equilibrium (Year 2 volume).
- **Opening chart**: *Japan after 1859: change in each good's price against its net exports in the first years of
  trade* --- [L] Bernhofen and Brown (2004, JPE) table of goods (autarky prices 1851--53, net exports 1868--75). Fallback
  if the table is not public: [L] the paper's headline numbers in a `record` box and the opening chart below moved up.
- **Other charts**: (2) *relative crop yields against relative areas planted, wheat and maize, across countries* [A]
  `faostat_crops("Wheat","Yield")`, `("Wheat","Area harvested")`, same for maize, 2020--2022 average; caption says
  actual yields are not the potential yields of the published test; (3) the DFS diagram drawn from a computed
  example (figdata: a seeded continuum of 200 goods) [S].
- **Diagrams**: the chain of comparative advantage (goods ranked on a line, the wage cut); the DFS $A(z)$ and $B(z)$
  curves with the equilibrium; the band of non-traded goods with iceberg costs.
- **Photos**: Yokohama harbour in the 1860s (public-domain woodblock print or photograph, Wikimedia Commons; licence to
  verify).
- **Boxes**: `record[Japan opens its ports, 1859]` (Bernhofen--Brown 2004; gains bounded at up to about 8--9 % of GDP,
  ledger to verify); `record[Labour productivity and exports, U.S. against U.K.]` (MacDougall 1951);
  `measure[Domestic expenditure share]` (the ACR formula's input).
- **Code**: no printed listings; figdata only. Exercises (py) solutions in `exercises/`.
- **Exercises**: ★ 1 [R] read the opening chart (sign of the relation); 2 [C] rank five goods by relative labour
  requirement and find the cut-off at a given relative wage; 3 [C] terms of trade after opening, two goods; 4 [X] what
  pattern in Japan's data would contradict the model. ★★ 5 [C] DFS equilibrium with linear $A(z)$; 6 [P] productivity
  gain in Kestria's grain: effect on Brenland's real wage ([B] `ricardo.csv`); 7 [C] band of non-traded goods with an
  iceberg cost of 20 %; 8 (py) [R] FAOSTAT: correlation of relative yields and areas; 9 [C] ACR gains: $\lambda$ = 0.8,
  $\varepsilon$ = 5. ★★★ 10 [C] prove uniqueness of DFS equilibrium; 11 [P] a transport-cost fall: which goods become
  traded; 12 [X] specialisation is incomplete in the data: two reasons inside and outside the model.
- **Weekend problem --- "Brenland and Kestria with twelve goods"**: twelve goods with labour requirements in both
  countries (invented; extends `ricardo.csv`). Part I autarky prices and the chain; Part II the equilibrium relative
  wage with given expenditure shares; Part III a 10 % iceberg cost: non-traded goods and the new wage; Part IV a
  productivity gain in Kestria, gains for both, and the ACR check. Named result: *Brenland's gain from trade, in % of
  real income, computed two ways*. 25 questions.
- **Ledger**: Bernhofen--Brown 2004, 2005 (AER gains); MacDougall 1951 (EJ); Golub--Hsieh 2000; Costinot--Donaldson
  2012 (AER P&P); Arkolakis--Costinot--Rodríguez-Clare 2012 (AER); Eaton--Kortum 2002 (trade elasticity ~8.28, to verify).

## 08 `factor-endowments` --- Factor Endowments

- **Programme items**: specific factors, Heckscher--Ohlin (KOM ch. 4--5).
- **Sections**: 1 Specific factors: who gains from opening in the short run; 2 Two factors, two goods: the
  Heckscher--Ohlin model; 3 Factor prices: Stolper--Samuelson and factor-price equalisation; 4 Outputs: Rybczynski;
  5 The factor content of trade and its tests: Leontief's result, the missing trade, the fixes.
- **Defines**: specific-factors model; factor intensity; factor abundance; Heckscher--Ohlin model; Stolper--Samuelson
  theorem; Rybczynski theorem; factor-price equalisation; factor content of trade; Heckscher--Ohlin--Vanek equation;
  missing trade.
- **Propositions with proofs**: specific factors: a price rise raises the specific factor's real return in that sector
  and lowers the other's, the mobile factor's real wage ambiguous (proof); Stolper--Samuelson (proof by the zero-profit
  conditions, the magnification effect); Rybczynski (proof by full employment); HOV (derivation from identical
  technologies and homothetic tastes).
- **Model boxes**: `model{Specific factors}` (assumes immobile factors in the short run; predicts distributional
  conflict by sector; tested: sector-level wage and return responses to trade shocks, e.g., Magee's lobbying by sector
  1980; breaks: long run, labour mobility); `model{Heckscher--Ohlin}` (assumes identical technologies, two mobile
  factors, homothetic tastes; predicts exports intensive in abundant factor, Stolper--Samuelson; tested: Leontief 1953,
  Bowen--Leamer--Sveikauskas 1987, Trefler 1995, Davis--Weinstein 2001; breaks: technology differences, home bias ---
  the missing trade).
- **Recalls**: PPF, opportunity cost (grades 10--12 volume); production functions, isoquants, cost minimisation (Year 1
  volume); general equilibrium (Year 2 volume).
- **Opening chart**: the outline's (predicted against measured factor content) needs Trefler's 33 x 9 table: heavy, and
  its numbers are not in an approved dataset. **Proposal**: *each country's share of world capital, of world workers and
  of world output, for twenty large economies* --- [A] `pwt(2019, cols=["rnna","emp","hc","rgdpo"])` (capital stock,
  workers, workers x human capital, output; 2021 dollars at PPP). It shows endowments, the model's input, and sets up
  HOV. Leontief's and Trefler's results go in `record` boxes [L].
- **Other charts**: (2) capital per worker against output per worker across countries [A PWT]; (3) relative factor
  endowments (skilled/unskilled via `hc`) of the five largest exporters [A].
- **Diagrams**: the specific-factors diagram (two sectors' labour demand, the wage); the Lerner--Pearce diagram / unit
  isoquants and factor-price determination; the Rybczynski shift in the Edgeworth box of factors.
- **Boxes**: `record[Leontief's 1953 result]` (capital per worker in U.S. exports below that of import replacements,
  ledger numbers); `record[The missing trade]` (Trefler 1995; Davis--Weinstein 2001 restore HOV with technology
  differences and trade costs).
- **Exercises**: ★ 1 [R] read the opening chart: which countries are capital-abundant relative to their GDP share;
  2 [C] factor intensities from a 2x2 input table; 3 [C] zero-profit conditions: factor prices from goods prices;
  4 [X] what would contradict HO for a labour-abundant country's exports. ★★ 5 [C] magnification effect: 10 % price rise
  of the labour-intensive good; 6 [C] Rybczynski: outputs after a 10 % rise in capital; 7 [P] specific factors: who gains
  when grain prices rise in Brenland; 8 (py) [C] factor content of trade with a given technology matrix; 9 [X] FPE: what
  wage data contradict it. ★★★ 10 [C] prove Stolper--Samuelson in the 2x2 model; 11 (py) [C] HOV sign test on a
  simulated 10-country, 3-factor world; 12 [P] immigration in an HO economy: outputs adjust, wages do not --- conditions.
- **Weekend problem --- "Kestria's capital boom"**: two goods (machines, textiles), two factors; invented technology.
  Part I autarky prices; Part II free trade with Brenland and FPE; Part III Kestria's capital stock rises 25 %:
  Rybczynski; Part IV the factor content of each country's trade and an HOV check. Named result: *the change in
  Kestria's textile output and in its workers' real wage after the boom*. 24 questions.
- **Ledger**: Leontief 1953 (Proc. Am. Phil. Soc.), numbers; Trefler 1995 (AER); Davis--Weinstein 2001 (AER);
  Bowen--Leamer--Sveikauskas 1987; Magee 1980.

## 09 `scale-variety-firms` --- Scale, Variety and Firms

- **Programme items**: new trade theory, heterogeneous firms (KOM ch. 7--8; L3 IO/trade).
- **Sections**: 1 Trade inside industries; 2 Love of variety and monopolistic competition; 3 The Krugman model of
  trade; 4 The home-market effect; 5 Firms that differ: the Melitz model (told, with its predictions); 6 Exporters are
  few, large and productive; 7 Reallocation after a trade agreement; multinationals and offshoring (told).
- **Defines**: intra-industry trade; Grubel--Lloyd index; love of variety (CES preferences); monopolistic competition
  (**contested**: check whether Book 2 or 3 defines it); Krugman model of trade; home-market effect; heterogeneous-firms
  model (Melitz); export cut-off (selection into exporting); foreign direct investment (horizontal, vertical; told).
- **Propositions**: CES demand gives a constant markup $\sigma/(\sigma-1)$ (proof); free entry pins firm size, trade
  raises the number of varieties consumed (proof); the home-market effect in the two-country Krugman model (proof with
  linear transport cost); Melitz: opening raises the productivity cut-off (stated, shown numerically).
- **Model boxes**: `model{Monopolistic competition and trade}` (assumes CES, increasing returns, free entry; predicts
  intra-industry trade between similar countries, gains from variety; tested: Broda--Weinstein 2006 variety gains;
  breaks: why most firms do not export); `model{Heterogeneous firms}` (assumes productivity draws, fixed export cost;
  predicts exporters larger and more productive, trade liberalisation raises industry productivity; tested: Bernard
  et al. 2007, Pavcnik 2002 (Chile), Trefler 2004 (Canada--U.S. FTA); breaks: no role for quality, demand differences).
- **Recalls**: monopoly pricing, Lerner index, economies of scale (Year 1 volume).
- **Opening chart**: *share of firms that export, by manufacturing industry, U.S. census of 2002* --- [L] Bernard,
  Jensen, Redding and Schott (2007, JEP) Table 2 (share exporting, exports as share of shipments), ~21 industries.
- **Other charts**: (2) the Melitz cut-offs on a simulated productivity distribution (closed, open) [S]; (3) the
  home-market effect: Home's share of production against its share of demand, computed from the model [S].
- **Diagrams**: CES demand and the markup; the free-entry diagram (PP and ZZ curves of KOM style, or the $AC$ tangency);
  productivity line with domestic and export cut-offs.
- **Boxes**: `record[The Canada--U.S. free trade agreement, 1989]` (Trefler 2004: labour productivity in most-affected
  industries rose ~15 %, ledger to verify); `record[Gains from new varieties]` (Broda--Weinstein 2006: ~2.6 % of GDP,
  ledger to verify); `measure[The Grubel--Lloyd index]`.
- **Exercises**: ★ 1 [R] read the opening chart (range across industries); 2 [C] Grubel--Lloyd index from a 3-industry
  table [B: invented Brenland--Kestria flows]; 3 [C] CES markup at $\sigma$ = 4; 4 [X] observation contradicting the
  home-market effect. ★★ 5 [C] free-entry firm size and number with given $F$, $c$, $\sigma$; 6 [P] trade doubles
  market size: number of varieties, price; 7 (py) [C] Melitz cut-off on a Pareto productivity draw; 8 [C] share of
  firms exporting from a given distribution; 9 [X] what firm data would contradict selection into exporting. ★★★ 10 [C]
  prove the constant markup from CES; 11 (py) [C] industry productivity before and after opening in a simulation;
  12 [P] a fall in the fixed export cost: extensive vs intensive margin.
- **Weekend problem --- "Brenland's furniture makers"**: 500 firms from `firms.csv` (manufacturing) with a seeded
  productivity, a fixed export cost to Kestria. Part I closed economy: markup, cut-off, average productivity; Part II
  opening: export cut-off, exporters' share and size premium; Part III a trade agreement halves the fixed cost; Part IV
  industry productivity and the welfare gain from variety. Named result: *the rise in average industry productivity
  after the agreement, and the share of firms that exit*. 26 questions.
- **Ledger**: Bernard et al. 2007 (JEP Table 2 and headline 18 % of U.S. manufacturing firms export, to verify);
  Grubel--Lloyd 1975; Krugman 1980 (AER); Melitz 2003; Pavcnik 2002; Trefler 2004; Broda--Weinstein 2006; Helpman--
  Melitz--Yeaple 2004 (FDI vs exports, told).

## 10 `gravity` --- Gravity and the Trade Data

- **Programme items**: empirical trade (KOM ch. 2; "Economie internationale appliquée").
- **Sections**: 1 The trade data and what they measure; 2 The gravity equation; 3 Estimating it in Python (OLS on
  logs); 4 Multilateral resistance and fixed effects; 5 Zeros and Poisson pseudo-maximum likelihood; 6 Distance,
  borders, language, agreements, currency; 7 Measured trade costs; 8 The container and the two waves of
  globalisation.
- **Defines**: gravity equation; distance elasticity; multilateral resistance; exporter and importer fixed effects;
  Poisson pseudo-maximum-likelihood (PPML) estimator; tariff-equivalent trade cost; the two waves of globalisation (as
  a dated fact pattern; maybe not a definition).
- **Propositions**: gravity from CES demand with iceberg costs (Anderson--van Wincoop, derivation in the simple
  symmetric case); log-linear OLS is inconsistent under heteroskedasticity, PPML is consistent if the conditional mean
  is right (Santos Silva--Tenreyro 2006, proof of the Jensen argument, consistency $\admitted$); a tariff-equivalent
  from the trade-cost elasticity (derivation).
- **Model box**: `model{The gravity equation}` --- assumes: CES demand, iceberg costs, market clearing; predicts: trade
  proportional to the product of GDPs over trade costs, distance elasticity near $-1$; tested: thousands of estimates
  (Head--Mayer 2014 meta-analysis; median distance elasticity about $-0.9$, ledger), this chapter's own fit; breaks:
  zeros, services, time-varying costs; the "distance puzzle" (no fall in the distance elasticity over time).
- **Recalls**: ch. 5 (likelihood); ch. 2 (fixed effects); Year 2 volume (multiple regression).
- **Opening chart**: *trade between country pairs in 2019 against the product of their GDPs divided by distance* --- [A]
  `gravity(since=2019, until=2019, columns=["year","iso3_o","iso3_d","tradeflow_baci","gdp_o","gdp_d","dist"])`,
  ~31,000 pairs (binned scatter of 50 bins, so the PDF stays small; full scatter if size allows).
- **Other charts**: (2) estimated distance elasticity by year, 1996--2020 (OLS with exporter and importer fixed
  effects, and PPML) [A]; (3) trade as a share of output, 1870--2020, average over 17 economies --- the two waves [A]
  `jst(cols=["imports","exports","gdp"])` (same currency, ratio); (4) the share of zero flows by year [A].
- **Diagrams**: the iceberg; a map-free schematic of multilateral resistance (two remote countries trade more with each
  other than their distance alone suggests: three-node diagram).
- **Photos**: a container ship or a container terminal (Commons, CC BY or PD; licence to verify).
- **Boxes**: `record[The container]` (Bernhofen--El-Sahli--Kneller 2016: containerisation's effect on trade, ledger to
  verify); `measure[What BACI records]` (reconciled mirror flows, CIF/FOB); `record[The first wave of globalisation and
  its end, 1870--1945]` (JST trade shares; tariffs in the 1930s with ledger dates).
- **Listings / outputs / tests** (memory: `gravity()` always with `columns=` and one year or a short range; under
  1.5 GB; `OMP_NUM_THREADS=1`):
  - `load_trade.py`: load 2019, count pairs, zeros, the largest flows; prints a small table.
  - `gravity_ols.py`: log trade on log GDPs and log distance, contiguity, language, colony, FTA; prints coefficients
    and robust errors.
  - `gravity_fe.py`: exporter and importer fixed effects (dummy columns, ~400) by OLS; prints distance and FTA.
  - `gravity_ppml.py`: GLM Poisson with the same fixed effects, zeros kept; prints the same coefficients.
  - `distance_by_year.py`: the distance elasticity for 1996, 2002, ..., 2020 (feeds chart 2 via figdata, the listing
    prints the table).
  - `tariff_equivalent.py`: the tariff-equivalent of a border/distance effect for a given trade elasticity.
  - Tests: coefficients within tolerance of a stored reference (distance between $-1.3$ and $-0.6$), PPML converges,
    memory guard (rows of one year < 40,000).
- **Exercises**: ★ 1 [R] read the opening chart; 2 [C] predicted trade ratio for two pairs given GDPs and distances;
  3 [C] a distance elasticity of $-0.9$: effect of doubling distance; 4 [X] what would contradict gravity for a pair.
  ★★ 5 (py) [C] add a common-official-language dummy; 6 (py) [C] FTA effect by OLS vs PPML; 7 [C] tariff equivalent of
  a contiguity coefficient with $\varepsilon$ = 5; 8 [P] effect of a new port that halves the cost to one partner;
  9 [X] why the log-linear fit drops zeros, and what that biases. ★★★ 10 (py) [C] the distance puzzle: is the trend in
  the elasticity significant? 11 [C] derive gravity in the symmetric two-country CES case; 12 (py) [C] PPML vs OLS
  under simulated heteroskedastic errors.
- **Weekend problem --- "Brenland joins a customs union"**: a fully invented 20-country world (GDPs, distances,
  flows) generated in the chapter's figdata, Brenland and Kestria among them (no real and invented data in one table).
  Part I fit gravity; Part II multilateral resistance and fixed effects; Part III the union's effect by PPML; Part IV
  trade creation and diversion for Brenland. Named result: *the union's effect on Brenland's
  trade with members and non-members, in %*. 25 questions.
- **Ledger**: Head--Mayer 2014 (Handbook) meta-analysis numbers; Anderson--van Wincoop 2003; Santos Silva--Tenreyro 2006;
  Disdier--Head 2008 (distance puzzle); Bernhofen--El-Sahli--Kneller 2016 (JIE); Novy 2013 (trade cost measure);
  McCallum 1995 border effect (22x, to verify).

## 11 `trade-policy` --- Trade Policy

- **Programme items**: instruments and political economy of trade policy (KOM part 2).
- **Sections**: 1 A tariff in a small and a large country: the terms-of-trade effect and the optimal tariff;
  2 Retaliation: the tariff game; 3 Quotas, export restraints and who gets the rent; 4 Effective protection;
  5 The political economy of protection (public choice recalled, ch. 21--22 forward); 6 Evidence: who paid recent
  tariffs; local labour markets after an import surge; infant industries.
- **Defines**: terms-of-trade effect; optimal tariff; tariff war (as a prisoner's dilemma application, recall Nash
  from the Year 2 volume); import quota; quota rent; voluntary export restraint; effective rate of protection;
  tariff pass-through; infant-industry argument.
- **Propositions**: welfare change of a small tariff in a large country = terms-of-trade gain minus efficiency loss
  (proof); optimal tariff = $1/\varepsilon^*$ (inverse of foreign export supply elasticity; proof); quota equivalence
  to a tariff under competition, non-equivalence under monopoly (proof); ERP formula (derivation).
- **Model box**: `model{The large-country tariff}` (assumes competitive markets, upward-sloping foreign export supply;
  predicts foreign exporters absorb part of the tariff, a small tariff can raise welfare absent retaliation; tested:
  2018--19 U.S. tariffs: pass-through near complete to import prices (Amiti--Redding--Weinstein 2019; Fajgelbaum et al.
  2020), partial absorption on steel; Smoot--Hawley retaliation; breaks: retaliation, which removes the gain;
  imperfect competition).
- **Recalls**: tariff, deadweight loss, incidence (grades 10--12 volume); Nash equilibrium, prisoner's dilemma,
  repeated games (Year 2 volume); rent seeking (ch. 22 re-founds; here first use with a forward pointer).
- **Opening chart**: the outline's (import prices before and after a tariff) is a figure, not a table, in the papers.
  **Proposal**: *applied tariff rates, weighted mean, 1988--2022, for six economies* [A]
  `wdi("TM.TAX.MRCH.WM.AR.ZS")` (USA, CHN, IND, BRA, JPN, one EU member; WDI has no world row for this series,
  checked 2026-11-20). The pass-through evidence then goes in a
  small [L] coefficient chart (chart 2).
- **Other charts**: (2) estimated pass-through of tariffs to import prices, by study (Amiti et al. 2019; Fajgelbaum
  et al. 2020; Cavallo et al. 2021, retail vs at-the-dock) [L]; (3) tariffs on manufactures vs primary products,
  1988--2022 [A].
- **Diagrams**: large-country tariff (home market with the world price falling, the areas of terms-of-trade gain and
  deadweight loss); quota rent; the tariff game in normal form (with `payoff` cells).
- **Boxes**: `debate[Trade and wages]` --- the question: how much did import competition lower wages and employment
  for exposed workers, and did aggregate gains offset it? Studies: Autor--Dorn--Hanson 2013 (AER, U.S. commuting
  zones, China shock: manufacturing employment fell by about 1.5 points per \$1,000 per worker of exposure, ledger to
  verify; grade 2 on the evidence scale: a strong shift-share design, with the Borusyak--Hull--Jaravel 2022 and
  Goldsmith-Pinkham et al. 2020 critiques of shift-share inference); Caliendo--Dvorkin--Parro 2019 (Econometrica,
  aggregate welfare gains with local losses; model-based, grade 3--4); Dauth--Findeisen--Suedekum 2014 (JEEA, Germany:
  net employment gains from export exposure to Eastern Europe); Krugman 2008 (Brookings: factor-content estimates of
  wage effects small then, larger after China); Feenstra--Ma--Xu 2019 (export gains offset). Weaknesses named for each.
  `record[The U.S.--China tariffs of 2018--2019]` (pass-through; retaliation on farm exports; transfer to farmers,
  ledger); `record[Infant industries: the evidence]` (Juhász 2018, Napoleonic blockade and French cotton spinning,
  AER --- a natural experiment where protection worked; Krueger--Tuncer 1982 negative); `measure[Effective protection]`.
- **Exercises**: ★ 1 [R] read the opening chart (fall of tariffs, dates); 2 [C] small-country tariff deadweight loss
  with linear curves; 3 [C] ERP for a car with given input shares and tariffs; 4 [X] what price data would show full
  absorption by foreign exporters. ★★ 5 [C] large-country tariff: terms-of-trade gain and DWL with numbers; 6 [C]
  optimal tariff for $\varepsilon^*$ = 4; 7 [P] retaliation: payoffs and the Nash equilibrium of the tariff game;
  8 (py) [R] WDI: which of five countries cut tariffs most, 1990--2020; 9 [X] infant-industry claim: what data would
  refute it. ★★★ 10 [C] prove the optimal-tariff formula; 11 [P] quota vs tariff under a domestic monopoly;
  12 (py) [C] shift-share exposure measure on an invented 5-region, 3-industry table and its regression.
- **Weekend problem --- "Brenland's steel tariff"**: invented demand, supply and Kestrian export supply for steel; a
  25 % tariff. Part I small-country benchmark; Part II large-country version: price paid abroad, terms-of-trade gain,
  DWL; Part III retaliation on Brenland's grain exports; Part IV the steel-using industries' ERP and jobs. Named
  result: *the net welfare change of the tariff, with and without retaliation, in millions of dalens*. 26 questions.
- **Ledger**: Amiti--Redding--Weinstein 2019 (JEP); Fajgelbaum--Goldberg--Kennedy--Khandelwal 2020 (QJE);
  Cavallo--Gopinath--Neiman--Tang 2021 (AER: Insights); Autor--Dorn--Hanson 2013; Caliendo--Dvorkin--Parro 2019;
  Dauth et al. 2014; Krugman 2008; Feenstra et al. 2019; Juhász 2018; Krueger--Tuncer 1982; Smoot--Hawley Act (LAW,
  date, average rates on dutiable imports to verify); Borusyak--Hull--Jaravel 2022; Goldsmith-Pinkham--Sorkin--Swift
  2020.

---

# Part III --- International macroeconomics

Assumes the Year 1 volume's open economy (real exchange rate, Mundell--Fleming, the trilemma) and the Year 2 volume's
intertemporal choice and Euler equation. Re-founds the open economy at the level of the field (ownership table: open
economy, Y1 `open-economy` -> Y3 Part III). Charts only, no printed code.

## 12 `current-account` --- The Current Account

- **Programme items**: international macroeconomics ("macroéconomie monétaire internationale"; KOM part 3; financial
  globalisation).
- **Sections**: 1 Balance-of-payments accounting in depth (current, capital and financial accounts, the investment
  position, valuation effects); 2 The current account as a choice over time (two-period small open economy);
  3 Sustainability: the long-run budget constraint and the net foreign asset position; 4 Sudden stops; 5 Saving and
  investment across countries (Feldstein--Horioka); 6 Why capital does not flow to poor countries (Lucas).
- **Defines**: current account (re-founded); financial account; net international investment position; valuation
  effect; intertemporal approach to the current account; external sustainability (no-Ponzi condition); sudden stop;
  Feldstein--Horioka puzzle; Lucas paradox.
- **Propositions**: CA = S -- I = change in NIIP net of valuation (identity, derivation); two-period model: a temporary
  output fall gives a deficit, a permanent one does not (proof with log utility); intertemporal budget constraint and
  the sustainable trade surplus (proof); the Lucas calculation: with Cobb--Douglas and equal TFP, the marginal product
  of capital in India would be 58 times the U.S. one (derivation; numbers recomputed with PWT, not Lucas's 1988 data).
- **Model box**: `model{The intertemporal current account}` (assumes a small open economy, perfect capital mobility,
  consumption smoothing; predicts deficits after temporary shocks and in investment booms; tested: current-account
  responses to terms-of-trade shocks, Glick--Rogoff 1995; Feldstein--Horioka's correlation as a rejection; breaks:
  borrowing limits, sudden stops, the "allocation puzzle" of Gourinchas--Jeanne 2013).
- **Recalls**: balance of payments (grades 10--12 volume); national accounts identities (Year 1 volume); Euler
  equation and intertemporal choice (Year 2 volume).
- **Opening chart**: *current-account balances by region, as a share of world output, 1980--2024* --- [A]
  `wdi("BN.CAB.XOKA.CD")` summed by region (WDI country regions via `wdi_countries()`), over world GDP
  `wdi("NY.GDP.MKTP.CD", iso3="WLD")`; China, the United States and Germany shown apart; the global discrepancy
  plotted as its own line (it does not sum to zero).
- **Other charts**: (2) saving rate against investment rate, country averages 2000--2024 (Feldstein--Horioka) [A]
  `NY.GNS.ICTR.ZS`, `NE.GDI.TOTL.ZS`; (3) current accounts around sudden stops (Mexico 1994, Thailand 1997, Greece
  2010--12: years $-3$ to $+3$) [A] `BN.CAB.XOKA.GD.ZS`; (4) net capital inflows (FDI) against income per person [A]
  `BX.KLT.DINV.WD.GD.ZS` (the Lucas pattern).
- **Diagrams**: two-period small open economy (endowment point, consumption point, world interest rate line); the
  BoP sign conventions as a T-account; sudden stop as an inward shift of the financing constraint.
- **Boxes**: `record[Sudden stops of the 1990s]` (Calvo 1998; current-account reversal sizes from the WDI chart);
  `record[The euro-area periphery, 2008--2013]`; `measure[Valuation effects in the investment position]`
  (Gourinchas--Rey 2007, U.S. "exorbitant privilege" return differential, ledger); `measure[Why the world's current
  accounts do not add to zero]`.
- **Exercises**: ★ 1 [R] read the opening chart; 2 [C] BoP entries for four transactions; 3 [C] CA from S and I;
  4 [X] what contradicts consumption smoothing in a current-account series. ★★ 5 [C] two-period model: CA after a
  temporary output fall, log utility; 6 [C] sustainable trade balance given NIIP, $r$, $g$; 7 (py) [C]
  Feldstein--Horioka coefficient on WDI, two decades; 8 [P] a permanent terms-of-trade fall: response of CA; 9 [X]
  what would show capital is perfectly mobile. ★★★ 10 [C] the Lucas calculation with PWT numbers (given); 11 [P]
  sudden stop: required change in the trade balance and the real exchange rate; 12 (py) [C] reversal episodes: mean
  change of CA/GDP after a 3-point drop in inflows.
- **Weekend problem --- "Brenland's borrowing years"**: from `country` accounts (X, M, $r$) 2000--2025 [B]. Part I
  the BoP of Brenland and its NIIP; Part II a two-period model fitted to a temporary export collapse; Part III
  sustainability: the trade surplus needed to stabilise the NIIP; Part IV a sudden stop: the adjustment if inflows stop.
  Named result: *the trade surplus, in % of GDP, that stabilises Brenland's external debt*. 24 questions.
- **Ledger**: Feldstein--Horioka 1980 (EJ coefficient ~0.89, to verify); Lucas 1990 (AER P&P, factor of 58); Calvo
  1998; Gourinchas--Rey 2007; Gourinchas--Jeanne 2013; Glick--Rogoff 1995; Obstfeld--Rogoff 2000 (puzzles, told).

## 13 `exchange-rates` --- Exchange Rates

- **Sections**: 1 Purchasing-power parity, absolute and relative, and its tests; 2 Productivity and price levels
  (Balassa--Samuelson); 3 Interest parity: covered holds, uncovered fails; 4 The monetary model; 5 Overshooting;
  6 Forecasting: a random walk beats the models.
- **Defines**: law of one price; absolute PPP; relative PPP (re-founded from the grades 6--9 conversion);
  half-life of a deviation; Balassa--Samuelson effect; price level index (measure box); covered interest parity;
  uncovered interest parity; forward premium puzzle (carry trade); monetary model of the exchange rate; overshooting
  (Dornbusch model); Meese--Rogoff result.
- **Propositions**: relative PPP from absolute in growth rates; Balassa--Samuelson derivation (two sectors, mobile
  labour, LOP in tradables); CIP by arbitrage (proof); the monetary model's exchange rate as a discounted sum of future
  fundamentals (derivation, recurrence from the grades 10--12 volume's sequences); Dornbusch: impact depreciation
  exceeds the long-run one (proof in the linear model).
- **Model boxes**: `model{Purchasing-power parity}` (assumes arbitrage of goods; predicts real rates revert; tested:
  half-lives of 3--5 years, Rogoff 1996, here from JST; breaks: non-traded goods, the short run); `model{The
  Dornbusch overshooting model}` (assumes sticky prices, UIP, money demand; predicts overshooting after a monetary
  shock; tested: VAR evidence mixed, delayed overshooting --- Eichenbaum--Evans 1995; breaks: UIP fails).
- **Recalls**: real exchange rate, nominal rate convention (Year 1 volume; the series: a rise of $e$ is a
  depreciation); PPP conversion (grades 6--9 volume); expectations (Year 2 volume).
- **Opening chart**: *price levels against income per person across countries, 2023* --- [A] `wdi("PA.NUS.GDP.PLI")`
  (price level ratio) against `NY.GDP.PCAP.PP.KD` (2021 PPP dollars), ~190 countries, semilogx.
- **Other charts**: (2) real exchange rates against the dollar, 1870--2020, for five JST economies [A] `jst(cols=
  ["xrusd","cpi"])` with U.S. CPI; (3) the UIP (Fama) regression: realised depreciation against the interest
  differential, annual, 17 economies [A] `jst(cols=["xrusd","stir"])`; (4) random-walk vs model forecast errors on
  a simulated example [S] or a JST pseudo-out-of-sample test [A] (to decide at writing).
- **Diagrams**: Dornbusch's phase diagram (exchange rate and price level, saddle path, the jump); CIP arbitrage loop.
- **Boxes**: `record[Meese and Rogoff, 1983]`; `record[The carry trade]` (Burnside et al. 2011; crash risk 2008);
  `measure[How a price level index is made]` (the International Comparison Program; ICP 2021 benchmark, ledger).
- **Exercises**: ★ 1 [R] read the opening chart; 2 [C] relative PPP prediction from two inflation rates; 3 [C] CIP
  forward rate; 4 [X] what would contradict PPP in the long run. ★★ 5 (py) [C] half-life from an AR(1) on JST real
  rates; 6 [C] Balassa--Samuelson: price level gap from productivity numbers; 7 [P] Dornbusch: impact of a 10 % money
  rise; 8 (py) [C] Fama regression slope on JST; 9 [X] what forecast record would contradict Meese--Rogoff. ★★★
  10 [C] prove the overshooting condition; 11 [C] monetary model: exchange rate with a money-growth path; 12 [P]
  carry trade return decomposition.
- **Weekend problem --- "The dalen against the kest"**: `country` `trade.csv` gives the rate 2000--2025 [B]; invented
  inflation and interest paths. Part I PPP and the real rate; Part II UIP and the forward premium; Part III a Kestrian
  monetary expansion in a Dornbusch model; Part IV a forecast contest. Named result: *the overshoot of the dalen, in %,
  and the half-life of its real deviation*. 25 questions.
- **Ledger**: Rogoff 1996 (JEL, half-lives); Meese--Rogoff 1983; Fama 1984; Burnside et al. 2011; Balassa 1964 and
  Samuelson 1964 (named as the result only); Dornbusch 1976; Eichenbaum--Evans 1995; ICP 2021 (AGENCY); Du--Tepper--
  Verdelhan 2018 (CIP deviations after 2008, to mention).

## 14 `exchange-rate-regimes` --- Exchange-Rate Regimes and Currency Unions

- **Sections**: 1 Regimes in the data: gold standard, pegs, floats; 2 The trilemma, tested; 3 Currency crises: three
  generations of models; 4 The criteria for a common currency; 5 The record of the euro; 6 Currency boards and
  dollarisation.
- **Defines**: exchange-rate regime; gold standard; peg (hard, soft); currency board; dollarisation; first-generation
  crisis model (Krugman 1979); second-generation (self-fulfilling) crisis model (Obstfeld); third-generation (balance-
  sheet) crisis; optimum currency area (criteria); internal devaluation. Trilemma: **recalled** from the Year 1 volume.
- **Propositions**: Krugman 1979: the timing of the attack when reserves hit a threshold (proof in the linear model);
  multiple equilibria in a second-generation model (proof with a payoff table); OCA trade-off (stated).
- **Model boxes**: `model{The first-generation crisis model}` (assumes a peg with deficits financed by credit; predicts
  a speculative attack before reserves run out; tested: Mexico 1982, Argentina 1981; breaks: ERM 1992 when reserves were
  ample); `model{Optimum currency areas}` (assumes asymmetric shocks, wage rigidity; predicts unions work with mobility,
  fiscal transfers, correlated shocks; tested: euro-area divergence 1999--2012; breaks: endogeneity of the criteria,
  Frankel--Rose 1998).
- **Recalls**: trilemma, Mundell--Fleming (Year 1 volume); ch. 12--13.
- **Opening chart**: *share of seventeen advanced economies with a pegged exchange rate, 1870--2020* --- [A]
  `jst(cols=["peg","peg_type"])`; caption: seventeen economies, the JST classification. (The outline's "countries by
  regime since 1870" for the whole world needs the Ilzetzki--Reinhart--Rogoff classification, not approved.)
- **Other charts**: (2) the trilemma test: change in the home short rate against the base country's change, pegs vs
  floats [A] `jst(cols=["stir","peg","peg_base"])`; (3) unit labour costs or inflation in the euro area core vs
  periphery 1999--2012 [A] Eurostat `prc_hicp_aind` (index), `nama_10_gdp`; (4) reserves before the attack (simulated
  first-generation model) [S].
- **Diagrams**: the trilemma triangle (recalled, small); reserve path and shadow exchange rate (Krugman 1979); the
  OCA diagram (openness vs symmetry, Frankel--Rose line).
- **Photos**: none (a gold bar is a stock image; skip).
- **Boxes**: `record[Sterling leaves the ERM, 16 September 1992]`; `record[Argentina's currency board, 1991--2002]`;
  `record[The euro, 1999 to today]` with `dated{2026}` (members of the euro area, ledger); `record[The Asian crisis,
  1997]` (third generation).
- **Exercises**: ★ 1 [R] read the opening chart (eras); 2 [C] trilemma: classify four regimes; 3 [C] shadow exchange
  rate at a given reserve level; 4 [X] what would contradict the trilemma for a peg. ★★ 5 (py) [C] trilemma regression
  on JST; 6 [C] attack date in the Krugman model; 7 [P] second generation: multiple equilibria with payoffs;
  8 (py) [R] Eurostat: inflation gap Greece vs Germany 1999--2008; 9 [X] what shows the OCA criteria are endogenous.
  ★★★ 10 [C] prove the attack time formula; 11 [P] internal devaluation: wage cut needed for a 15 % real depreciation;
  12 [C] currency board: money supply after a capital outflow.
- **Weekend problem --- "Brenland pegs the dalen to the kest"**: invented reserves, credit growth, money demand. Part I
  the peg and its arithmetic; Part II credit growth and the attack date; Part III a second-generation scare with a
  high-unemployment cost; Part IV a currency board instead. Named result: *the date of the speculative attack, and the
  reserve cover a currency board needs*. 24 questions.
- **Ledger**: Krugman 1979; Obstfeld 1996 (EER); Obstfeld--Shambaugh--Taylor 2005 (trilemma test); Frankel--Rose 1998;
  Mundell 1961 (named as the OCA result); ERM 1992 dates (AGENCY: Bank of England); Argentina convertibility law 1991
  (LAW); euro members (AGENCY, ECB) dated 2026.

---

# Part IV --- Money and banking

Assumes Book 3 `money-and-inflation` (quantity theory, velocity, inflation tax, Fisher effect, the monetarist
propositions scored) and Book 4 `expectations-and-lucas-critique` (credibility, independence, inflation targets),
`three-equation-model` (the rule, the Taylor principle, the zero lower bound) and `banks-and-crises` (runs, deposit
insurance, lender of last resort). Ownership table: money and inflation -> Y3 `central-banking`, `inflation-evidence`.

## 15 `central-banking` --- Central Banking in Practice

- **Programme items**: monetary economics, "Banque et marchés", "Monnaie Banque Finance" (L3 options).
- **Sections**: 1 The central bank's balance sheet; 2 How the policy rate is implemented: corridor and floor systems;
  3 Inflation targeting in practice (the target recalled; the reaction function, the forecast); 4 Guidance about the
  future; 5 Asset purchases and their measured effects; 6 How the effect of a monetary shock is measured (high-frequency
  identification, local projections --- told; fills the time-series gap of the programme check); 7 Financial stability
  and macroprudential tools; 8 2021--23.
- **Defines**: central-bank balance sheet; bank reserves (settlement balances); corridor system; floor system; standing
  facility; forward guidance; quantitative easing (large-scale asset purchases); term premium; monetary policy shock
  (high-frequency surprise); local projection (told); macroprudential policy.
- **Propositions**: in a corridor, the overnight rate lies between the deposit and lending rates (arbitrage proof); with
  abundant reserves the rate equals the deposit rate (floor; proof); the expectations hypothesis of the long rate, plus
  a term premium (decomposition); a guidance promise's value is its credibility (time-consistency recalled).
- **Model box**: `model{The portfolio-balance channel of asset purchases}` (assumes imperfect substitutability of bonds;
  predicts purchases lower term premia; tested: event studies of 2008--09 announcements (Gagnon et al. 2011:
  10-year yields down about 90 basis points in total, ledger to verify), later rounds smaller; breaks: effects shrink
  once markets anticipate, exit effects).
- **Recalls**: money creation, central bank (grades 10--12 volume); inflation targets, credibility, independence
  (Year 2 volume); the policy rule and the zero lower bound (Year 2 volume); lender of last resort (Year 2 volume).
- **Opening chart**: *central-bank balance sheets as a share of output, 2005--2025: Federal Reserve, ECB, Bank of
  Japan, Bank of England* --- [?] (not in approved data) fallback [L] year-end total assets from each bank's published
  annual accounts or statistical release at 2007, 2010, 2014, 2019, 2021, 2024 (24 rows), over nominal GDP from WDI
  `NY.GDP.MKTP.CD`/Eurostat (both approved; numerator from the ledger). Data to approve, preferred: Fed H.4.1 weekly
  total assets (public domain) and ECB consolidated weekly financial statement.
- **Other charts**: (2) the policy-rate corridor in the euro area: deposit rate, main refinancing rate, marginal
  lending rate, overnight rate, 2008--2025 [L/?] (ECB key-rate dates are ledger rows: decision dates and levels,
  ~45 rows; the overnight rate needs data: drop it, plot the three key rates as steps); (3) inflation in four economies
  2019--2025 [A] Eurostat `prc_hicp_manr` (euro area), BLS CPI-U (U.S.) --- two sources, two lines, named.
- **Diagrams**: T-account of a central bank (assets: securities, loans to banks, gold, FX; liabilities: currency,
  reserves, government deposits); the corridor diagram (reserve demand curve, corridor rates, supply vertical; floor
  case); yield-curve decomposition (expected path + term premium).
- **Photos**: the ECB or the Federal Reserve building (Commons, licence to verify) --- optional, one at most.
- **Boxes**: `debate[What caused the inflation of 2021--23]` --- Bernanke--Blanchard 2023 (Brookings/PIIE: initially
  energy, food and sectoral shocks; labour-market tightness later and more persistent; grade 3); Jordà--Liu--Nechio--
  Rivera-Reyes 2022 (SF Fed: U.S. fiscal support raised inflation by about 3 points by late 2021, cross-country
  comparison; grade 3); di Giovanni--Kalemli-Özcan--Silva--Yildirim 2022/2023 (supply bottlenecks and demand together;
  model-based, grade 3--4); Shapiro 2022 (SF Fed decomposition of PCE inflation into supply- and demand-driven
  categories; grade 3); Benigno--Eggertsson 2023 (nonlinear Phillips curve once vacancies exceed unemployment).
  Weaknesses: short sample, simultaneity of shocks, model dependence. `record[Asset purchases, 2008--2014]`;
  `record[Forward guidance at the zero lower bound]`; `dated{2026}` policy rates of the four banks (ledger rows).
  `measure[What a central bank's balance sheet records]`.
- **Exercises**: ★ 1 [R] read the opening chart; 2 [C] T-account after a 100 bn asset purchase; 3 [C] overnight rate
  in a corridor with given reserves; 4 [X] what market data would show forward guidance not believed. ★★ 5 [C]
  expectations hypothesis: 2-year rate from an expected path, plus a term premium; 6 [P] floor system: effect of a
  deposit-rate rise on the overnight rate; 7 [C] an event study: yield changes on announcement days (given table);
  8 (py) [R] Eurostat/BLS: peak inflation and dates; 9 [X] what would contradict the portfolio-balance channel. ★★★
  10 [C] reserve demand curve and the corridor equilibrium with a given demand function; 11 [P] the central bank's
  income when it pays interest on reserves and holds long bonds; 12 [P] a macroprudential cap on loan-to-value: who is
  constrained, what the evidence says.
- **Weekend problem --- "The Bank of Brenland's balance sheet"**: invented balance sheet and money market, using
  `country` `policy_rate` and CPI [B]. Part I the T-account and money creation; Part II corridor to floor;
  Part III an asset-purchase programme: reserves, term premium, the bank's income; Part IV inflation overshoots: the
  rate path a simple rule gives (recall of the Year 2 volume) and the guidance announced. Named result: *the policy
  rate implied by the rule and the central bank's net interest income at that rate*. 24 questions.
- **Ledger**: Gagnon--Raskin--Remache--Sack 2011; Krishnamurthy--Vissing-Jorgensen 2011; ECB key rates (AGENCY),
  Fed, BoE, BoJ policy rates (AGENCY, dated 2026); balance-sheet totals (AGENCY, 24 rows); Bernanke--Blanchard 2023;
  Jordà et al. 2022; di Giovanni et al. 2022; Shapiro 2022; Benigno--Eggertsson 2023; Nakamura--Steinsson 2018
  (high-frequency identification); Jordà 2005 (local projections).

## 16 `inflation-evidence` --- Inflation: The Evidence across Time and Countries

- **Sections**: 1 Prices under metallic and paper standards; 2 Hyperinflations: their fiscal origin and how they end;
  3 Disinflations and what they cost; 4 Measured expectations; 5 Fiscal and monetary explanations set against the same
  episodes.
- **Defines**: hyperinflation (Cagan's threshold, re-founded); seigniorage (**contested**: Book 3 `money-and-inflation`
  defines the inflation tax; if it also defines seigniorage, recall); Cagan money-demand model; Laffer curve of
  seigniorage (revenue-maximising inflation); fiscal theory of the price level (as a model name);
  "unpleasant arithmetic" of Sargent--Wallace (as a result's name); credibility bonus of a regime change; survey and
  market measures of expected inflation (breakeven inflation).
- **Propositions**: Cagan model: seigniorage maximised at money growth $1/\alpha$ (proof); Sargent--Wallace: with a fixed
  primary deficit and $r > g$, tighter money now means higher inflation later (proof in the two-period model);
  government's intertemporal budget constraint in real terms (derivation); breakeven inflation = nominal minus indexed
  yield, minus risk premia (decomposition).
- **Model boxes**: `model{The quantity theory over the long run}` --- recalled with the cross-country evidence
  (assumes stable velocity growth; predicts money growth and inflation one for one over decades; tested: cross-country
  decade averages, WDI broad money vs CPI; breaks: low-inflation samples, velocity shifts); `model{The Cagan model of
  hyperinflation}` (assumes money demand falling with expected inflation; predicts seigniorage peaks; tested: Cagan
  1956's seven episodes; breaks: at the end of hyperinflations, regime changes).
- **Recalls**: quantity equation, inflation tax, Fisher effect, monetarist propositions (Year 1 volume); sacrifice ratio
  (Year 1 volume); Volcker disinflation record (grades 10--12 and Year 1 volumes: recall, not retold);
  rational expectations, credibility (Year 2 volume); government debt dynamics (Year 2 volume).
- **Opening chart**: the outline's "price level of one country over three centuries" needs the Bank of England's
  Millennium dataset [?]. **Fallback** [A]: *the price level of five economies, 1870--2020, on a logarithmic scale*
  `jst(cols=["cpi"])` (GBR, USA, FRA, DEU, ITA; DEU with the 1923 break shown as a gap, caption says so).
- **Other charts**: (2) money growth against inflation, country averages 1990--2024 [A] `FM.LBL.BMNY.ZG` (broad money
  growth, approved, checked) against `FP.CPI.TOTL.ZG`; and JST `money` and `cpi`, 17 economies, decade averages
  since 1870; (3) inflation before and after independence/target adoption for
  inflation-targeting countries [A] WDI `FP.CPI.TOTL.ZG` with adoption dates from the ledger; (4) seigniorage Laffer
  curve (computed from a Cagan model) [S].
- **Diagrams**: Cagan's seigniorage curve with the peak; Sargent--Wallace timeline (two periods, the debt path).
- **Photos**: a hyperinflation banknote (Germany 1923 or Zimbabwe 2008, public domain or CC on Commons; licence to
  verify; banknote designs are not AI-generated here, they are photographs of real notes).
- **Boxes**: `record[Germany, 1923]` (the end of the hyperinflation: the Rentenmark, the budget; Sargent 1982 "The ends
  of four big inflations"); `record[Zimbabwe, 2007--2009]` (dollarisation ended it; ledger); `record[Brazil's Real
  Plan, 1994]`; `record[Disinflations with and without credibility]` (Ball 1994 sacrifice ratios; Israel 1985 plan);
  `measure[How old price indices are built]` (with the Millennium dataset if approved; else Officer--Williamson
  MeasuringWorth? not approved --- the box describes method only); `measure[Breakeven inflation]`.
- **Exercises**: ★ 1 [R] read the opening chart (eras of stable and rising prices); 2 [C] monthly to annual inflation in a
  hyperinflation; 3 [C] seigniorage at given money growth and base; 4 [X] what episode would contradict the fiscal origin
  of hyperinflations. ★★ 5 [C] Cagan peak money growth for $\alpha$ = 2; 6 (py) [C] decade-average money growth vs
  inflation on JST: the slope; 7 [P] Sargent--Wallace with numbers; 8 [C] sacrifice ratio from an episode table; 9 [X]
  what would show breakeven inflation is not expected inflation. ★★★ 10 [C] prove the seigniorage maximum; 11 (py)
  [C] inflation before and after target adoption in 8 countries (DiD-style, recalling ch. 3); 12 [P] a fiscal
  consolidation that ends a hyperinflation: path of money demand and real balances.
- **Weekend problem --- "Kestria's printing press"**: invented Kestrian budget, money demand (Cagan), debt. Part I the
  deficit and seigniorage; Part II the inflation rate that finances it, and the Laffer peak; Part III the
  stabilisation: a fiscal reform plus a currency board; remonetisation; Part IV the cost in output of an alternative
  gradual disinflation (sacrifice ratio). Named result: *the inflation rate that finances Kestria's deficit, and the
  remonetisation gain after the reform*. 25 questions.
- **Ledger**: Cagan 1956 (table of seven hyperinflations); Sargent 1982; Sargent--Wallace 1981 (FRB Minneapolis QR);
  Ball 1994; Hanke--Krus 2013 (hyperinflation table, Zimbabwe peak); Brazil Real Plan dates; inflation-targeting
  adoption dates (AGENCY or Roger 2010 IMF); Fischer--Sahay--Végh 2002 (high inflation, JEL).

---

# Part V --- Public economics and public choice

Public choice is a full half of the part (user). Market failure and government failure sit side by side: chapters 17--20
measure what taxes, transfers and programmes do; chapters 21--22 model the decisions that make them. Assumes Book 3
`partial-equilibrium-welfare` (DWL in elasticity form, the incidence formula), `labour-supply-and-saving` (kinks,
implicit marginal rates) and Book 4 Parts I and IV (insurance, adverse selection, moral hazard), `social-choice` (Arrow,
median voter), `externalities-and-public-goods-theory`, `overlapping-generations` (pay-as-you-go vs funded).

## 17 `efficiency-cost-of-taxation` --- The Efficiency Cost of Taxation

- **Programme items**: "Économie publique" (all four universities); Gruber part IV.
- **Sections**: 1 The excess burden of a tax: compensated demand and the Harberger formula; 2 Many goods and the
  marginal cost of public funds; 3 The inverse-elasticity (Ramsey) rule; 4 Incidence beyond one market: payroll, profit,
  value-added taxes; taxes on capital and saving (told: what the elasticities say); 5 The elasticity of taxable income;
  6 Revenue against the rate, where it was measured; 7 Taxes people do not notice.
- **Defines**: excess burden (re-founded from deadweight loss, general form); Harberger formula; marginal excess burden;
  marginal cost of public funds; Ramsey rule (inverse-elasticity rule) --- label `ramsey-rule`, distinct from Book 4's
  Ramsey model and ch. 35's discounting formula; payroll tax incidence; value-added tax; elasticity of taxable income;
  revenue-maximising tax rate (Laffer curve); tax salience.
- **Propositions with proofs**: Harberger's approximation $\tfrac12 \varepsilon \tau^2 pq$ from compensated demand
  (proof; the Year 1 volume's triangle recalled, here with income effects removed); marginal excess burden rises with
  the rate (proof: linear in $\tau$); Ramsey rule from minimising excess burden subject to revenue (Lagrange, proof
  with independent demands); revenue-maximising rate $\tau^* = 1/(1+a e)$ with Pareto parameter $a$ and ETI $e$
  (Saez's formula; proof); incidence of a payroll tax independent of the statutory side (proof, recalled).
- **Model box**: `model{The elasticity of taxable income}` (assumes taxable income responds to the net-of-tax rate;
  predicts excess burden from all margins, avoidance included; tested: tax reforms --- U.S. 1986, U.K. 2010 50p rate,
  Danish administrative data (Kleven--Schultz 2014), ETI of about 0.12--0.40 (Saez--Slemrod--Giertz 2012, ledger);
  breaks: the elasticity is not a structural constant --- it depends on the tax base and enforcement).
- **Recalls**: tax incidence, DWL (grades 10--12 volume; Year 1 volume in elasticity form); compensated demand,
  EV/CV (Year 1 volume); Lagrange's method (Year 1 volume, admitted; proved in the mathematics books).
- **Opening chart**: the outline's (revenue by type of tax over a century) is not in approved data (OECD Revenue
  Statistics from 1965 would need approval; by type over a century needs a historical source). **Proposal**: [A]
  *general-government revenue as a share of output, 1870--2020, six economies* `jst(cols=["revenue","gdp"])`; second
  chart (2) *tax revenue by type, 1972--2024, five economies* [A] WDI `GC.TAX.YPKG.RV.ZS`, `GC.TAX.GSRV.RV.ZS`,
  `GC.REV.SOCL.ZS`, `GC.TAX.INTT.RV.ZS` (central government: say so).
- **Other charts**: (3) revenue against the top rate: the Laffer curve computed for ETI = 0.25 and 0.5 with $a = 1.5$
  [S, analytic]; (4) the U.K. 50p episode: reported top incomes around April 2010--2013 [L] HMRC 2012 report numbers.
- **Diagrams**: compensated demand and the Harberger triangle; MEB rising with $\tau$ (two triangles); payroll-tax
  wedge in the labour market (both sides).
- **Boxes**: `record[The U.K. 50 % top rate, 2010--2013]` (HMRC 2012: estimated ETI ~0.45, revenue ~\pounds0.1 bn ---
  numbers via ledger; note the currency macro: the style has `\usd` and `\eur` only, so write "100 million pounds" in
  words or ask for `\gbp`); `record[Salience: posted and unposted sales taxes]` (Chetty--Looney--Kroft 2009, AER);
  `record[Sweden's 1991 reform]`; `measure[How an ETI is estimated]` (DiD on tax reforms, bunching at kinks: Saez
  2010).
- **Exercises**: ★ 1 [R] read the opening chart (when revenue shares rose); 2 [C] Harberger excess burden, $\varepsilon
  = 0.5$, $\tau = 0.2$; 3 [C] MCPF from MEB; 4 [X] what evidence would contradict full pass-through of a VAT to
  consumers. ★★ 5 [C] Ramsey rule with two goods; 6 [C] revenue-maximising top rate with $a=1.5$, $e=0.25$; 7 [P]
  payroll tax: incidence with given elasticities; 8 (py) [R] WDI: composition change in five countries; 9 [X] what
  would show bunching at a kink is real responses, not reporting. ★★★ 10 [C] prove the Ramsey rule (Lagrange); 11 [C]
  bunching: ETI from excess mass at a kink; 12 [P] a salient vs non-salient tax: who bears it.
- **Weekend problem --- "Brenland's tax reform"**: `country` `TAX_BANDS` and `households.csv` [B] (gross income,
  tax). Part I the schedule and average/marginal rates; Part II excess burden of the top band with an ETI;
  Part III a reform that cuts the top rate and raises VAT: revenue and burden; Part IV the MCPF and a project funded at
  the margin. Named result: *the marginal cost of public funds of Brenland's top band*. 26 questions.
- **Ledger**: Saez--Slemrod--Giertz 2012 (JEL); Saez 2001 / Diamond--Saez 2011 formula; Kleven--Schultz 2014; HMRC 2012
  (AGENCY); Chetty--Looney--Kroft 2009; Saez 2010 (bunching); Harberger 1964; Feldstein 1999 (ETI and excess burden).

## 18 `transfers-and-incentives` --- Transfers, Incentives and Redistribution

- **Sections**: 1 Budget sets under a benefit system: implicit marginal rates and poverty traps; 2 Measured responses:
  income-guarantee experiments; 3 In-work credits; 4 The optimal income tax as a trade-off between elasticities and
  weights; the inputs it needs; 5 Redistribution measured across countries.
- **Defines**: participation tax rate; poverty trap; negative income tax; in-work tax credit; phase-in and phase-out
  rates; social welfare weight; optimal top tax rate (Saez formula, applied; defined in ch. 17 as the
  revenue-maximising rate --- here with weights); redistribution (market vs disposable Gini; the measure). Implicit
  marginal tax rate: **recalled** from the Year 1 volume (contested if Book 3 does not define it).
- **Propositions**: the top-rate formula $\tau = (1-g)/(1-g+ae)$ (proof by a small reform); an NIT with guarantee $G$
  and rate $t$ has break-even income $G/t$ (proof); participation responses favour in-work credits over guarantees
  when extensive elasticities are large (Saez 2002, stated, shown with a two-type example).
- **Model box**: `model{The negative income tax}` (assumes a guarantee withdrawn at a constant rate; predicts lower
  hours and participation among recipients; tested: U.S. income-maintenance experiments 1968--1982 (hours fell by about
  5--7 % for husbands, more for wives; Robins 1985, ledger), Mincome (Manitoba) and the Finnish basic-income
  experiment 2017--18 (employment effect near zero, ledger); breaks: small samples, short horizons, general-equilibrium
  effects not observed).
- **Recalls**: Lorenz curve and Gini (grades 10--12 volume); kinks and implicit marginal rates in the budget set, labour
  supply (Year 1 volume); social welfare functions (Year 2 volume); ch. 17.
- **Opening chart**: *the marginal effective tax rate faced by a single parent with two children as earnings rise, one
  country and year* --- [L] statutory parameters (federal income tax, payroll tax, EITC, child tax credit, SNAP benefit
  reduction rate --- U.S. 2024) from IRS / SSA / USDA pages, one ledger row per parameter, computed by the figdata
  script. Alternative [B]: Brenland's `TAX_BANDS` plus an invented benefit schedule. Recommendation: the real U.S.
  schedule (it is the evidence of section 3).
- **Other charts**: (2) the budget line under the same schedule (net income against gross) [L]; (3) Gini of market and
  of disposable income: not in approved data (OECD IDD). Fallback [A]: WDI `SI.POV.GINI` (disposable or consumption)
  against income per person, with a caption that it does not separate pre- and post-transfer --- or drop the chart and
  give ledger numbers in a `measure` box. Data to approve (optional): OECD Income Distribution Database.
- **Diagrams**: budget set with a means-tested benefit (flat, kinked); NIT budget line; EITC trapezoid.
- **Boxes**: `record[The income-maintenance experiments]`; `record[The 1993 expansion of the in-work credit]`
  (Eissa--Liebman 1996: participation of single mothers up 2.8 points, ledger to verify); `record[Finland's basic income
  experiment, 2017--2018]` (Kela final report 2020); `measure[Marginal effective and participation tax rates]`.
- **Exercises**: ★ 1 [R] read the opening chart (where the rate peaks); 2 [C] net income at three earnings levels;
  3 [C] NIT break-even income; 4 [X] what hours data would contradict the NIT prediction. ★★ 5 [C] participation tax
  rate from a given schedule; 6 [C] Saez top rate with $g$ = 0.2, $a$ = 2, $e$ = 0.25; 7 [P] a lower phase-out rate:
  who works more, who less; 8 (py) [C] compute the MTR schedule for another family type from the ledger parameters;
  9 [X] what would contradict a large extensive elasticity for single mothers. ★★★ 10 [C] prove the top-rate formula;
  11 [P] two-type participation model: guarantee vs in-work credit; 12 (py) [B] redistribution in Brenland's survey:
  Gini of gross vs disposable income.
- **Weekend problem --- "Reforming Brenland's family benefit"**: `households.csv` [B]. Part I the current schedule and
  its implicit rates; Part II a poverty trap: the hours a parent needs to escape; Part III an in-work credit with
  phase-in and phase-out: cost and incentives; Part IV redistribution: Gini before and after. Named result: *the
  participation tax rate before and after the reform, and its cost per household*. 25 questions.
- **Ledger**: IRS Rev. Proc. 2023-34 (2024 EITC parameters); SSA payroll rates; USDA SNAP benefit reduction (AGENCY);
  Robins 1985 (J. Human Resources); Kela 2020 Finnish basic-income report; Eissa--Liebman 1996 (QJE); Saez 2001, 2002;
  Hendren--Sprung-Keyser 2020 (MVPF, told; links ch. 20).

## 19 `social-insurance` --- Social Insurance

- **Sections**: 1 Why private markets for some risks stay thin (adverse selection and correlated risks, recalled);
  2 Unemployment insurance: smoothing against search (Baily--Chetty); 3 Health insurance: the randomised evidence;
  4 Pensions, saving and ageing; 5 Disability insurance.
- **Defines**: social insurance; replacement rate; potential benefit duration; Baily--Chetty formula; consumption-
  smoothing benefit; annuity; disability insurance; crowd-out (of private saving or insurance). Moral hazard, adverse
  selection: **recalled** (Year 2 volume); pay-as-you-go and funded pensions: **recalled** (Year 2 volume).
- **Propositions**: the Baily--Chetty condition (proof in the two-state model: marginal benefit of smoothing equals
  the fiscal externality from longer search); with a fair annuity, risk-averse retirees annuitise fully (Yaari, proof
  in a two-period example); PAYG return = $n + g$ (recalled, used).
- **Model box**: `model{Unemployment insurance and search}` (assumes job search effort falls with benefits;
  predicts longer spells with longer or higher benefits, a spike at exhaustion; tested: Katz--Meyer 1990,
  Card--Chetty--Weber 2007 (Austria), Schmieder--von Wachter--Bender 2012 (Germany RD at age thresholds): roughly
  0.1--0.2 weeks of non-employment per extra week of entitlement (ledger, to verify); breaks: liquidity effects,
  Chetty 2008 --- part of the response is consumption smoothing).
- **Recalls**: risk aversion, insurance, adverse selection, moral hazard (Year 2 volume); OLG pensions, dependency
  arithmetic (Year 2 volume); RD (ch. 4).
- **Opening chart**: the outline's (weeks of unemployment against weeks of entitlement) is a figure in the papers.
  **Proposal** [L]: *estimated extra weeks of unemployment per extra week of benefit entitlement, by study* (Moffitt
  1985, Katz--Meyer 1990, Card--Levine 2000, Lalive 2008, Schmieder--von Wachter--Bender 2012, Card et al. 2015,
  Johnston--Mas 2018), each estimate with its interval, one ledger row each. Fallback if [L] is refused: [A] *old-age
  dependency ratio 1960--2025, six economies* `SP.POP.DPND.OL` (becomes chart 2 otherwise).
- **Other charts**: (2) [A] old-age dependency ratio; (3) the RAND and Oregon results: spending and health outcomes
  [L] (small coefficient chart, 2 studies, 6 outcomes).
- **Diagrams**: the two-state UI model (consumption employed/unemployed, the smoothing gain); the hazard of leaving
  unemployment with the spike at exhaustion (illustrative, labelled as a model sketch, not data); annuity value.
- **Boxes**: `record[The RAND Health Insurance Experiment, 1974--1982]` (cost sharing cut spending by about 30 %
  with little effect on health for the average person, ledger); `record[The Oregon lottery, 2008]` (Finkelstein et al.
  2012, Baicker et al. 2013: more use, less financial strain and depression, no measured change in physical health over
  two years); `record[Disability rolls and the 1984 reform]` or Autor--Duggan 2003, or Norway (Autor et al. 2019)
  --- one only; `measure[The replacement rate]`.
- **Exercises**: ★ 1 [R] read the opening chart (range, intervals); 2 [C] replacement rate and benefit; 3 [C] PAYG
  return with $n$ = 0.5 %, $g$ = 1.5 %; 4 [X] what would contradict moral hazard in UI. ★★ 5 [C] Baily--Chetty optimum
  with given elasticity and consumption drop; 6 [P] extending benefits from 26 to 39 weeks: spell length (from the
  chart); 7 [C] annuity price for a two-period life with survival probability; 8 (py) [R] dependency ratios: which
  country ages fastest 2000--2025; 9 [X] what the Oregon data would have shown under the "insurance improves physical
  health in two years" hypothesis. ★★★ 10 [C] prove the Baily--Chetty condition; 11 [P] adverse selection in a
  voluntary pension annuity market: the unravelling price; 12 (py) [C] RD at an age threshold for UI duration
  (simulated, recalls ch. 4).
- **Weekend problem --- "Brenland's unemployment fund"**: invented spells, wages, benefit rules, using `accounts.csv`
  unemployment rates [B]. Part I the fund's budget; Part II a search model's response to the replacement rate;
  Part III the Baily--Chetty optimum; Part IV an extension of duration evaluated with an age RD. Named result:
  *Brenland's optimal replacement rate under the measured elasticity*. 25 questions.
- **Ledger**: Baily 1978; Chetty 2006, 2008; Katz--Meyer 1990; Moffitt 1985; Card--Chetty--Weber 2007; Schmieder et
  al. 2012; Lalive 2008; Card et al. 2015; Johnston--Mas 2018; Manning et al. 1987 (RAND); Aron-Dine--Einav--Finkelstein
  2013; Finkelstein et al. 2012; Baicker et al. 2013; Autor--Duggan 2003; Yaari 1965.

## 20 `cost-benefit-analysis` --- Cost--Benefit Analysis

- **Sections**: 1 Willingness to pay and accounting prices; 2 Discounting; 3 The value of a statistical life; 4 Risk;
  5 Revealed and stated preferences; 6 Forecasts against outcomes for large projects; the marginal value of public
  funds (told).
- **Defines**: cost--benefit analysis; accounting price (shadow price of a resource in project appraisal; "shadow
  price" itself is the Year 1 volume's multiplier --- **contested**, so the qualified term); social discount rate;
  net present value (re-founded? present value is grades 10--12's: only the decision rule is defined here --- to
  confirm); value of a statistical life; hedonic wage (compensating-differential) method; travel-cost method;
  contingent valuation; optimism bias; reference-class forecasting; marginal value of public funds.
- **Propositions**: NPV rule = Kaldor--Hicks improvement under the stated assumptions (recalled compensation tests,
  Year 2 volume); VSL = WTP for a small risk change / risk change (derivation from expected utility); with a declining
  certainty-equivalent discount rate under uncertain future rates (Weitzman 1998 result, proof in a two-state example).
- **Model box**: `model{Hedonic wages and the value of a statistical life}` (assumes workers trade wage against fatal
  risk in competitive markets; predicts a wage premium proportional to risk; tested: U.S. labour-market estimates of
  roughly \$7--12 million (Viscusi--Aldy 2003 meta-analysis; the U.S. DOT guidance 2024 figure, ledger); breaks:
  misperceived risk, sorting by risk tolerance, omitted job attributes).
- **Recalls**: present value, discounting (grades 10--12 volume); compensating and equivalent variation (Year 1
  volume); compensation tests (Year 2 volume); expected utility (Year 2 volume); ch. 18 MVPF.
- **Opening chart**: *forecast against final cost for large public projects* --- [L] named projects, each with an
  official or audit source (e.g., Sydney Opera House, Channel Tunnel, Boston Central Artery, Denver airport, Scottish
  Parliament building, Berlin Brandenburg airport, Elbphilharmonie, the U.K. High Speed 2 --- ~8--10 rows, chosen
  only where a primary audit or government source gives both figures) plus the summary statistic of Flyvbjerg,
  Holm and Buhl (2002: average rail overrun 44.7 %, 258 projects, ledger to verify).
- **Other charts**: (2) present value of \$1 over 100 years at 1.4 %, 3 %, 7 % [S, analytic]; (3) VSL estimates by
  method (labour-market, stated preference, agencies' values) [L].
- **Diagrams**: WTP and accounting price for a project input bought in a distorted market (DWL areas); the hedonic
  wage locus as the envelope of offer and indifference curves.
- **Photos**: Sydney Opera House (Commons, licence to verify) --- optional.
- **Boxes**: `record[The Channel Tunnel]` (forecast vs outturn traffic and cost, Anguera 2006); `measure[The value of a
  statistical life]`; `dated{2026}` agencies' discount rates and VSL (U.S. OMB Circular A-4 2023: 2 %; U.K. Green Book:
  3.5 % declining; U.S. DOT VSL 2024 --- ledger); `record[Stated preference and the Exxon Valdez valuation]`
  (contingent valuation debate --- the evidence on hypothetical bias, Hausman 2012 vs Carson 2012).
- **Exercises**: ★ 1 [R] read the opening chart (median overrun); 2 [C] NPV of a bridge at 3 % and 7 %; 3 [C] VSL
  from a wage premium of \$1,000 for a 1-in-10,000 risk; 4 [X] what forecast data would contradict "random errors"
  vs optimism bias. ★★ 5 [C] accounting price of labour with unemployment; 6 [C] certainty-equivalent discount rate in a
  two-state world; 7 [P] effect of the discount rate on a climate-type project's sign; 8 (py) [C] reference-class
  adjustment of a forecast using the chart's distribution; 9 [X] what would show stated WTP is biased. ★★★ 10 [C]
  prove the Weitzman declining rate in the two-state case; 11 [C] hedonic regression on invented job data (py);
  12 [P] MVPF of two programmes (given costs and WTP) and the ranking.
- **Weekend problem --- "A new bridge for Brenmoor"**: invented traffic, costs, time savings, accident risk. Part I
  benefits in dalens (time valued from ch. 5's value of travel time); Part II safety benefits with a VSL; Part III
  discounting and NPV under three rates; Part IV a reference-class correction of the cost forecast. Named result: *the
  bridge's NPV after the optimism-bias correction, and the discount rate at which it turns negative*. 25 questions.
- **Ledger**: Flyvbjerg et al. 2002 (JAPA); project audit sources (AGENCY, ~8 rows); Viscusi--Aldy 2003; U.S. DOT VSL
  guidance 2024; OMB A-4 2023; HM Treasury Green Book 2022; Weitzman 1998; Hausman 2012; Carson 2012 (JEP pair);
  Anguera 2006; Hendren--Sprung-Keyser 2020.

## 21 `public-choice-voting` --- Public Choice: Voting

- **Programme items**: political economy (Gruber ch. 9--10; L3 "Économie publique"; government failure, user ruling).
- **Sections**: 1 The median-voter result and its tests; 2 Turnout and the uninformed voter; 3 Vote trading and agenda
  setting; 4 Models of the size of government, each tested (Meltzer--Richard; Wagner's law; Baumol's cost disease;
  the Peltzman tax-share hypothesis, told); 5 Fiscal rules; 6 Local governments and people who move between them.
- **Defines**: calculus of voting (paradox of voting); rational ignorance; logrolling (vote trading); agenda setter
  (Romer--Rosenthal model); Meltzer--Richard model; Wagner's law (as a measured regularity); Baumol cost disease;
  fiscal rule; Tiebout sorting; fiscal competition (told). Median voter theorem and single-peaked preferences:
  **recalled** from the Year 2 volume.
- **Propositions**: Meltzer--Richard: the chosen tax rate rises with the ratio of mean to median income (proof with
  linear tax and lump-sum transfer); agenda setter with a reversion point gets more than the median voter wants
  (proof); Baumol: with productivity growth only in one sector, the stagnant sector's relative price rises at the
  productivity gap (proof).
- **Model boxes**: `model{The median voter}` (recalled model, the **tested** and **breaks** are this chapter's: assumes
  one dimension, single-peaked preferences, two office-seeking parties; predicts convergence to the median; tested:
  Pettersson-Lidbom; Lee--Moretti--Butler 2004 RD finds voters elect policies, not affect them --- partial convergence;
  breaks: party discipline, turnout, multiple dimensions); `model{Meltzer--Richard}` (predicts redistribution rising
  with inequality; tested: cross-country evidence weak (Perotti 1996), suffrage extensions raise spending (Husted--
  Kenny 1997; Lott--Kenny 1999 women's suffrage); breaks: the "Robin Hood paradox"); `model{Tiebout sorting}`
  (assumes mobile residents and many jurisdictions; predicts sorting and capitalisation of local taxes and services
  into house prices; tested: Oates 1969, Black 1999 school-quality RD on boundaries; breaks: zoning, moving costs).
- **Recalls**: public choice first look (grades 10--12 volume); social choice, Arrow, median voter (Year 2 volume); RD
  (ch. 4); capitalisation (Year 1 volume, `competitive-industry`).
- **Opening chart**: *public spending as a share of output, 1870--2020, against the year the vote was extended to all
  adult men and to women, 17 economies* --- [A] `jst(cols=["expenditure","gdp"])` + [L] suffrage dates (one ledger row
  per country and extension, from a single published table where possible, e.g., Przeworski 2009 (BJPolS) or the
  Inter-Parliamentary Union's page; to verify). Plot: years relative to suffrage extension (an event-time line,
  average across countries) --- the event-study shape recalls ch. 3.
- **Other charts**: (2) spending share against log income across countries, 2019 (Wagner's law in a cross-section)
  [A] `GC.XPN.TOTL.GD.ZS` vs `NY.GDP.PCAP.PP.KD`; (3) relative price of services vs goods (Baumol): not in approved
  data except via BLS all-items --- **drop** unless the main session derives BLS CPI services/commodities series
  (`CUUR0000SAS`, `CUUR0000SAC`) from the approved BLS flat files (no new download).
- **Diagrams**: single-peaked preferences and the median (recalled small); Romer--Rosenthal agenda-setter diagram
  (reversion point, setter's proposal); Tiebout: two towns' tax--service bundles and sorting.
- **Boxes**: `record[Women's suffrage and public spending]` (Lott--Kenny 1999; Miller 2008 child mortality);
  `record[Balanced-budget rules in the U.S. states]` (Poterba 1994: states with stricter rules cut faster after shocks,
  ledger); `record[Swiss cantons' debt brakes]` (Feld--Kirchgässner, told) --- one of the two; `measure[Turnout and
  the probability of being decisive]` (Gelman--Silver--Edlin 2012: about 1 in 60 million for a U.S. presidential vote,
  ledger to verify).
- **Exercises**: ★ 1 [R] read the opening chart (before/after); 2 [C] the median voter's tax rate with given incomes;
  3 [C] probability of a tie in a 1,001-voter election with $p$ = 0.5 (binomial, grades 10--12 recall); 4 [X] what
  would contradict the median-voter prediction in a two-party race. ★★ 5 [C] Meltzer--Richard tax rate with given
  mean/median; 6 [P] agenda setter: proposal with a low reversion point; 7 [C] Baumol: relative price after 20 years
  with 2 % vs 0 % growth; 8 (py) [C] cross-country Wagner slope, 1990 vs 2019; 9 [X] what house prices would contradict
  Tiebout capitalisation. ★★★ 10 [C] prove the Meltzer--Richard comparative static; 11 [P] logrolling: three voters,
  two projects, the coalition; 12 (py) [C] event-time average of spending around suffrage dates (recalls ch. 3; given
  data).
- **Weekend problem --- "Brenmoor votes on a pool"**: invented electorate (incomes, preferences), a referendum, a council
  agenda setter, a neighbouring town. Part I the median voter's choice; Part II the agenda setter; Part III a
  redistributive tax under Meltzer--Richard with Brenland's household survey [B]; Part IV Tiebout: households move,
  house prices adjust. Named result: *the pool size the referendum chooses, the setter's proposal, and the house-price
  capitalisation of the tax difference*. 25 questions.
- **Ledger**: Meltzer--Richard 1981 (JPE); Romer--Rosenthal 1978; Lee--Moretti--Butler 2004 (QJE); Husted--Kenny 1997;
  Lott--Kenny 1999; Miller 2008; Perotti 1996; Poterba 1994; Oates 1969; Black 1999; Gelman et al. 2012; Downs 1957
  (rational ignorance, as the result's label); suffrage dates (17 rows, PAPER/AGENCY); Baumol 1967.

## 22 `interest-groups-and-regulation` --- Interest Groups, Bureaucracy and Regulation

- **Sections**: 1 The logic of collective action; 2 Rent seeking and its cost; 3 The capture model of regulation
  (Stigler--Peltzman); 4 The budget-maximising bureau; 5 Evidence: occupational licences, farm programmes; 6 Measured
  costs and benefits of regulation; 7 The record of privatisation and deregulation.
- **Defines**: collective action problem (concentrated benefits, diffuse costs); rent seeking (re-founded from the
  grades 10--12 volume); rent dissipation (Tullock contest); regulatory capture (re-founded); Peltzman model of
  regulation; budget-maximising bureau (Niskanen model); occupational licensing; privatisation; regulatory impact
  assessment.
- **Propositions**: Tullock contest with $n$ symmetric risk-neutral players dissipates $(n-1)/n$ of the rent (proof);
  Olson: group provision falls with group size (proof with a public-good contribution game, recalled from the Year 2
  volume); Niskanen: the bureau chooses output where total cost = total benefit, double the efficient output with
  linear curves (proof); Peltzman: regulated price lies between the competitive and the monopoly price (proof with a
  support function).
- **Model boxes**: `model{The capture model of regulation}` (assumes regulators maximise political support; predicts
  regulation favours concentrated producers; tested: licensing raises wages ~10--15 % with little measured quality gain
  (Kleiner--Krueger 2013; Kleiner--Soltas 2023), trucking and airline rents before deregulation (Rose 1987); breaks:
  consumer-led regulation, e.g., environmental rules); `model{The budget-maximising bureau}` (tested weakly: cost
  comparisons of public and contracted services --- Domberger--Jensen 1997; breaks: monitoring by sponsors).
- **Recalls**: rent seeking, capture (grades 10--12 volume); public goods contribution game (Year 2 volume); monopoly
  DWL (Year 1 volume); ch. 21.
- **Opening chart**: *share of U.S. workers who need a licence to do their job, 1950s to 2023* --- [L] Kleiner and
  Krueger 2013 (JOLE: about 5 % in the early 1950s, 29 % in 2008 by their survey), Kleiner 2006 (1970, 1980s), BLS CPS
  licensing question from 2015 (~22--25 %, BLS table, ledger). Caption says the measures change in 2015 (a break,
  drawn as a gap).
- **Other charts**: (2) the Tullock dissipation share against $n$ [S, analytic]; (3) agricultural support: not in
  approved data (OECD PSE) --- [L] OECD PSE % for five economies at three dates from the OECD's monitoring report, or
  drop; recommendation: a `record` box instead of a chart.
- **Diagrams**: Tullock rectangle vs Harberger triangle (monopoly with rent-seeking cost); Niskanen bureau diagram
  (total benefit, total cost, efficient vs bureau output); Peltzman support curve.
- **Boxes**: `record[Occupational licensing and prices]` (dental hygienists, Kleiner--Kudrle 2000; hair-braiding
  rules; one well-sourced case only); `record[Airline and trucking deregulation, 1978--1980]` (forward to ch. 30 for
  prices; here the political economy: who lobbied); `record[U.K. privatisations, 1979--1997]` (Megginson--Netter 2001
  survey: efficiency gains in most studies; Galal et al. 1994 welfare calculations); `measure[How a regulation's cost
  is counted]` (the U.S. OIRA report to Congress, ledger, dated).
- **Exercises**: ★ 1 [R] read the opening chart (and the measurement break); 2 [C] Tullock dissipation with 4
  players; 3 [C] Harberger triangle and Tullock rectangle for a given monopoly; 4 [X] what evidence would contradict
  capture in a licensed profession. ★★ 5 [C] Niskanen output with given linear curves; 6 [P] Olson: large vs small
  group lobbying success; 7 [C] wage premium of licensing in an invented regression table; 8 [P] Peltzman with a
  demand shift; 9 [X] what quality data would support licensing as consumer protection. ★★★ 10 [C] prove the Tullock
  dissipation result; 11 [P] privatisation of a natural monopoly with price-cap regulation (recall ch. 30 forward,
  Year 1 volume rules); 12 (py) [C] a DiD on invented state licensing reforms (recalls ch. 3).
- **Weekend problem --- "Brenland licenses its electricians"**: invented market, a proposed licensing law, two
  lobbies. Part I the market without licences; Part II the licence: wage premium, price, quantity, DWL; Part III the
  rent-seeking contest between the trade association and a consumer group; Part IV a later repeal evaluated by DiD
  across Brenland's regions. Named result: *the total social cost of the licence: Harberger plus Tullock, in millions of
  dalens*. 25 questions.
- **Ledger**: Olson 1965 (as the result's label); Tullock 1967/1980; Stigler 1971; Peltzman 1976; Niskanen 1971;
  Kleiner--Krueger 2013; Kleiner 2006; BLS CPS licensing table (AGENCY, 2023); Kleiner--Soltas 2023 (REStud);
  Kleiner--Kudrle 2000; Megginson--Netter 2001; Galal et al. 1994; Rose 1987; Domberger--Jensen 1997; OIRA report
  (AGENCY).

---

# Part VI --- Labour economics

Assumes Book 3 `labour-supply-and-saving`, `factor-markets` (derived demand, the single-buyer model), `unemployment-
flows`, and Book 4 `signalling-and-screening`, `search-and-unemployment`, Part VI. Ownership table: minimum wage
Y1 `factor-markets` -> Y3 `minimum-wage`; education g6 -> ... -> Y3 `human-capital`.

## 23 `labour-supply-and-demand` --- Labour Supply and Demand in the Data

- **Sections**: 1 Two margins of labour supply: hours and participation; 2 Hours of work over the long run; 3 Women's
  participation and its causes; 4 The elasticity of labour demand (Hicks--Marshall); 5 Technology and tasks; 6 Retirement.
- **Defines**: intensive margin; extensive margin; Frisch elasticity (and Hicksian/Marshallian, recalled); Hicks--
  Marshall rules of derived demand; constant-output and scale effects; task-based model of technology; routine task;
  job polarisation; effective retirement age (measure). Labour supply elasticity: **recalled** (Year 1 volume).
- **Propositions**: Hicks--Marshall: the own-wage elasticity of labour demand $= -(1-s)\sigma - s\eta$ (derivation for
  two factors); with a fixed cost of work, participation responds discontinuously (proof in the quasi-linear case);
  task model: automation of routine tasks lowers middle wages and raises the employment share at both ends (shown in
  a three-task example).
- **Model box**: `model{The task-based model of technology}` (assumes tasks allocated between capital and skill groups
  by comparative advantage; predicts polarisation; tested: U.S. and European occupation shares 1980--2010 (Autor--Dorn
  2013; Goos--Manning--Salomons 2014); breaks: the 2010s, when the low end stopped growing in some countries).
- **Recalls**: consumption--leisure choice, income and substitution effects of the wage (Year 1 volume); derived demand,
  factor shares (Year 1 volume); elasticity of substitution (Year 1 volume).
- **Opening chart**: the outline's (women's participation over a century in six countries) is not in approved data
  before 1990. **Proposal** [A]: *women's labour-force participation, 1990--2025, six economies* `SL.TLF.CACT.FE.ZS`
  (ILO modelled estimates; caption says so); a century for the United States in a `record` box with ledger numbers
  (Goldin 1990/2006: about 20 % in 1900 to about 60 % in 2000, to verify).
- **Other charts**: (2) average annual hours worked per worker, 1950--2023, six economies [A] `pwt(cols=["avh"])`;
  (3) female--male participation ratio against income per person (the U-shape, Goldin 1995) [A] `SL.TLF.CACT.FM.ZS`
  vs `NY.GDP.PCAP.PP.KD`; (4) employment share of agriculture vs income (forward to ch. 31) --- maybe not.
- **Diagrams**: budget set with a fixed cost of work (participation kink); the Hicks--Marshall decomposition (scale vs
  substitution in an isoquant diagram); a three-task line with automation shifting the threshold.
- **Boxes**: `record[The pill and women's careers]` (Goldin--Katz 2002; Bailey 2006 using state law variation);
  `record[Hours since 1870]` (Huberman--Minns 2007 numbers via ledger, because PWT starts in 1950);
  `measure[Hours worked: what the surveys count]`; `measure[Elasticities: what a review finds]` (Chetty et al.
  2011/2013 macro vs micro elasticities: Frisch ~0.5 intensive, extensive ~0.25 --- ledger to verify).
- **Exercises**: ★ 1 [R] read the opening chart; 2 [C] hours change from a given elasticity and a 10 % wage rise; 3 [C]
  Hicks--Marshall elasticity with $s$ = 0.3, $\sigma$ = 1, $\eta$ = 2; 4 [X] what contradicts the task model in an
  occupation table. ★★ 5 (py) [C] PWT hours: average annual decline, 1950--2023; 6 [P] fixed cost of work falls:
  who enters; 7 [C] participation threshold wage in a quasi-linear model; 8 (py) [R] the U-shape: where the minimum
  lies; 9 [X] what would contradict a large extensive elasticity among older workers. ★★★ 10 [C] derive Hicks--Marshall;
  11 [P] a payroll tax cut targeted at low wages: employment effect from elasticities; 12 [P] automation of a middle
  task: wage changes for three groups in the task model.
- **Weekend problem --- "Brenland's working hours"**: `households.csv` hours and incomes [B]. Part I hours against
  wages: what a regression shows and why it is not a supply curve (recall ch. 1); Part II a tax reform as a natural
  experiment (invented): intensive and extensive responses; Part III labour demand in Brenland's firms (`firms.csv`):
  Hicks--Marshall; Part IV the incidence and employment effect of a payroll tax cut. Named result: *the employment
  effect of the payroll-tax cut, intensive plus extensive, in thousands of workers*. 25 questions.
- **Ledger**: Goldin 1990, 1995, 2006; Goldin--Katz 2002; Bailey 2006; Huberman--Minns 2007; Chetty et al. 2011
  (AER P&P); Autor--Dorn 2013; Goos--Manning--Salomons 2014; Hamermesh 1993 (labour demand elasticities, review);
  Lichter--Peichl--Siegloch 2015 (meta-analysis of labour-demand elasticities).

## 24 `human-capital` --- Human Capital and the Returns to Schooling

- **Sections**: 1 The schooling decision; 2 The earnings equation; 3 Ability bias and the natural experiments that
  address it; 4 Signal or skill, again, with the tests; 5 School resources; 6 Training on the job.
- **Defines**: human capital (re-founded with the investment model; school owner g11); internal rate of return to
  schooling; Mincer earnings equation; ability bias (named case of OVB); education production function; general
  training; specific training (Becker). Sheepskin effect and the signalling model: **recalled** (Year 2 volume).
- **Propositions**: the optimal stopping rule for schooling ($r$ = marginal return) and the Mincer coefficient as the
  rate of return under no tuition and constant earnings growth (proof); Becker: firms pay for specific, not general,
  training under competition (proof); ability bias sign (proof via OVB).
- **Model box**: `model{The Mincer earnings equation}` (assumes schooling as investment, earnings growing with
  experience; predicts log earnings linear in schooling, concave in experience; tested: hundreds of datasets,
  coefficients 6--12 % (Card 1999; Psacharopoulos--Patrinos 2018 world average ~9 %, ledger); breaks: credential
  jumps, heterogeneous returns, rising convexity of returns since 1980).
- **Recalls**: IV, LATE (ch. 1), RD (ch. 4); signalling and diplomas (Year 2 volume); multiple regression and OVB
  (Year 2 volume); simple regression of earnings on schooling (Year 1 volume, its opening chart).
- **Opening chart**: *estimated returns to a year of schooling, by method of estimation* --- [L] one row per study
  with its estimate and interval: OLS (Card 1999 survey), quarter of birth IV (Angrist--Krueger 1991), proximity IV
  (Card 1995), twins (Ashenfelter--Krueger 1994; Ashenfelter--Rouse 1998), compulsory schooling (Harmon--Walker 1995;
  Oreopoulos 2006 U.K.), school construction (Duflo 2001, Indonesia), Swedish twins with measurement-error corrections
  (Isacsson 1999) --- 9--11 rows.
- **Other charts**: (2) log earnings in 1978 against years of schooling, CPS men, with the Mincer fit [A]
  `nsw("cps_controls")` (`education`, `re78`, `age`); (3) earnings profiles by schooling group against age, same data
  [A]; (4) school resources: class-size estimates by design (Tennessee STAR, Angrist--Lavy, Hoxby 2000) [L] --- or a
  `record` box.
- **Diagrams**: the schooling decision (present value of earnings streams by years of schooling, marginal return vs $r$);
  the Card (2001) heterogeneous-returns diagram (marginal benefit and cost by individual); training cost--wage profile.
- **Boxes**: `record[Compulsory schooling laws]` (Oreopoulos 2006 vs Devereux--Hart 2010 re-estimate: the U.K. return
  falls from ~15 % to ~4--7 % for men, ledger to verify); `record[Project STAR]` (Krueger 1999); `measure[What a Mincer
  coefficient measures]`.
- **Exercises**: ★ 1 [R] read the opening chart (OLS vs IV estimates); 2 [C] IRR of a degree from a cost and an
  earnings stream; 3 [C] Mincer coefficient to a % premium ($e^{\beta}-1$); 4 [X] what twin data would contradict the
  ability-bias story. ★★ 5 (py) [C] Mincer regression on CPS controls with experience squared; 6 [P] direction of
  measurement-error bias in twins differences; 7 [C] Wald estimate from compulsory-schooling cohort means; 8 [P]
  Becker: who pays for a forklift licence vs a firm's software training; 9 [X] signal vs skill: what the
  sheepskin test would show under pure human capital. ★★★ 10 [C] prove the Mincer coefficient = rate of return
  under the stated assumptions; 11 (py) [C] earnings--age profiles, peak age by schooling group; 12 [P] why IV
  estimates exceed OLS: the LATE reading (ch. 1).
- **Weekend problem --- "The last year of school in Brenland"**: `households.csv` `school_years` and incomes [B]
  plus an invented school-leaving-age reform. Part I the private return by OLS; Part II the reform as an instrument;
  Part III LATE and who the compliers are; Part IV the social return with taxes and a signalling share. Named
  result: *the private and the social return to the extra year, in %*. 25 questions.
- **Ledger**: Mincer 1974; Card 1995, 1999, 2001; Angrist--Krueger 1991; Ashenfelter--Krueger 1994; Ashenfelter--Rouse
  1998; Harmon--Walker 1995; Oreopoulos 2006; Devereux--Hart 2010; Duflo 2001; Isacsson 1999; Psacharopoulos--Patrinos
  2018; Krueger 1999; Hoxby 2000; Becker 1964 (label).

## 25 `wage-structure` --- The Wage Structure

- **Sections**: 1 Compensating differences; 2 The skill premium as a race between the supply and the demand for skills;
  3 Discrimination: models and evidence (audit studies, decompositions); 4 Unions; 5 Migration and local wages.
- **Defines**: compensating wage differential (**contested**: check whether Book 2 g11 `labour-market` defines it);
  skill premium (college wage premium); skill-biased technical change; canonical supply--demand model of the skill
  premium (Katz--Murphy); taste-based discrimination (Becker); statistical discrimination; correspondence (audit) study;
  Oaxaca--Blinder decomposition; union wage premium; immigration surplus.
- **Propositions**: Katz--Murphy: $\ln(w_s/w_u) = \tfrac1\sigma[D_t - \ln(S/U)]$ (derivation from CES); Becker: taste
  discrimination is competed away with free entry of unprejudiced employers (proof sketch with numbers);
  Oaxaca--Blinder decomposition (derivation, the index-number problem stated); immigration surplus with a downward
  labour demand: triangle formula (proof).
- **Model boxes**: `model{The race between education and technology}` (assumes two skill groups, CES, steady demand
  shift; predicts the premium falls when supply outpaces demand; tested: U.S. 1915--2005 with $\sigma$ about 1.4--1.6
  (Katz--Murphy 1992; Goldin--Katz 2008); breaks: the 1990s--2010s flattening, within-group inequality);
  `model{Taste-based discrimination}` (predicts gaps shrink with competition; tested: Black--Strahan 2001 bank
  deregulation, Hellerstein--Neumark--Troske 2002; breaks: persistent gaps in callback studies).
- **Recalls**: Lorenz and Gini (grades 10--12 volume); elasticity of substitution (Year 1 volume); ch. 1, ch. 3, ch. 23.
- **Opening chart**: *the college wage premium and the relative supply of college workers, United States, 1915--2005*
  --- [L] Goldin and Katz (2008, *The Race between Education and Technology*, Table 8.1 or their published appendix;
  decadal rows, ~10). "Over sixty years" in the outline becomes "over ninety years"; or 1963--2017 from Autor 2014 /
  Autor--Goldin--Katz 2020 (AEA P&P) Table 1 [L].
- **Other charts**: (2) Oaxaca--Blinder decomposition of the black--white earnings gap among CPS men in 1978 [A]
  `nsw("cps_controls")` (education, age, married, black); (3) callback rates by name in correspondence studies [L]
  (Bertrand--Mullainathan 2004 and two later studies; or a `record` box).
- **Diagrams**: hedonic wage locus (compensating differences, recalls ch. 20); supply and demand for skill with shifts
  (race diagram); union wage effect in a two-sector model (spillover).
- **Boxes**: `debate[Immigration and local wages]` --- Card 1990 (ILR Review: Mariel boatlift, Miami wages of
  low-skilled workers unchanged relative to comparison cities; grade 2); Borjas 2017 (ILR Review: non-Hispanic
  prime-age male high-school dropouts' wages fell 10--30 %; grade 2--3, small cells); Clemens--Hunt 2019 (ILR Review:
  Borjas's result coincides with a change in the CPS sample's composition); Peri--Yasenov 2019 (synthetic control: no
  effect); Dustmann--Schönberg--Stuhler 2017 (QJE: Czech commuters into German border areas, employment of natives
  fell, wages little; grade 1--2). Weaknesses: small samples, the choice of comparison, displacement vs wages.
  `record[Names on résumés]` (Bertrand--Mullainathan 2004: callbacks 9.65 % vs 6.45 %, ledger to verify; Kline--Rose--
  Walters 2022 large-firm study); `measure[The Oaxaca--Blinder decomposition]`.
- **Exercises**: ★ 1 [R] read the opening chart; 2 [C] compensating differential from a risk premium; 3 [C] Oaxaca
  decomposition with given means and coefficients; 4 [X] what callback data would contradict statistical
  discrimination. ★★ 5 [C] Katz--Murphy: implied $\sigma$ from two decades; 6 (py) [C] Oaxaca on CPS controls with
  the other reference group (index-number problem); 7 [P] a surge of graduates: premium change with $\sigma$ = 1.5;
  8 [C] immigration surplus triangle; 9 [X] what would show the union premium is selection. ★★★ 10 [C] derive the
  Katz--Murphy equation; 11 [P] Becker with entry: profits of a prejudiced firm; 12 (py) [C] a Mariel-style DiD on an
  invented city panel with a composition change, to see the Clemens--Hunt point.
- **Weekend problem --- "Brenland's graduates"**: invented supply of graduates 1990--2025 and wages (seeded). Part I
  the premium and relative supply; Part II estimate $\sigma$ and the demand trend; Part III forecast the premium if
  graduate supply grows 2 % a year; Part IV a gap between two groups decomposed. Named result: *Brenland's elasticity
  of substitution between graduates and non-graduates, and the forecast premium in 2035*. 25 questions.
- **Ledger**: Goldin--Katz 2008; Katz--Murphy 1992; Autor--Goldin--Katz 2020; Card 1990; Borjas 2017; Clemens--Hunt
  2019; Peri--Yasenov 2019; Dustmann et al. 2017; Bertrand--Mullainathan 2004; Kline--Rose--Walters 2022; Black--Strahan
  2001; Hellerstein et al. 2002; Freeman--Medoff / Card 1996 (union premium); Rosen 1986 (compensating differentials).

## 26 `minimum-wage` --- Minimum Wages and Monopsony

- **Sections**: 1 The competitive prediction; 2 The single-buyer and search predictions; 3 The first natural experiment
  and the replies; 4 Border-pair and bunching estimates; 5 Other margins: hours, prices, entry, machines; 6 Small and
  large increases. The series' model `debate` box.
- **Defines**: own-wage elasticity of employment; labour supply elasticity to the firm; monopsonistic competition in
  the labour market (search frictions; dynamic monopsony); Kaitz index (minimum to median wage); border-pair design;
  bunching estimator (Cengiz et al.); spillover effect. Single-buyer (monopsony) model: **recalled** (Year 1 volume).
- **Propositions**: with a single buyer, a minimum wage between the monopsony wage and the competitive wage raises
  employment (recalled and extended to the firm-level supply elasticity: markdown $= 1/(1+\varepsilon_{LS})$, proof);
  in the Burdett--Mortensen search model, firms face an upward-sloping supply even with many firms (stated, admitted);
  the bunching estimator: missing jobs below and excess jobs at and above the new minimum (derivation of the
  employment change as the difference).
- **Model boxes**: `model{The competitive labour market with a wage floor}` (predicts employment falls with the
  labour-demand elasticity; tested: elasticities near zero to moderately negative for teens, Neumark--Wascher 2008
  review; breaks: monopsony power); `model{Monopsony in the labour market}` (assumes upward-sloping supply to the
  firm; predicts modest increases can raise employment; tested: firm-level supply elasticities of about 1--5 (Manning
  2021 review, Dube et al. 2020), concentration and wages (Azar et al. 2022); breaks: large increases beyond the
  competitive wage).
- **Recalls**: single-buyer model and wage floor (Year 1 volume, `factor-markets`); search and matching (Year 2 volume);
  DiD (ch. 3), RD (ch. 4), meta-analysis and funnel plots (ch. 6).
- **Opening chart**: *published estimates of the employment elasticity, by year of publication* --- [L] ~15 studies,
  each a ledger row with its estimate (own-wage elasticity where reported, converted with the study's own wage effect
  otherwise, the conversion stated), its interval, design and country: Card--Krueger 1994; Neumark--Wascher 2000;
  Card--Krueger 2000; Neumark--Wascher 2008 (review number); Dube--Lester--Reich 2010; Allegretto--Dube--Reich 2011;
  Neumark--Salas--Wascher 2014; Meer--West 2016; Jardim et al. 2017/2022 (Seattle); Cengiz--Dube--Lindner--Zipperer
  2019; Harasztosi--Lindner 2019 (Hungary); Clemens--Wither 2019; Dustmann et al. 2022 (Germany); Derenoncourt--
  Montialoux 2021; Neumark--Shirley 2022 (review). The selection rule is printed (every well-known study on both sides,
  chosen before the estimates were plotted; listed in BRIEFS before writing) to keep the chart neutral.
- **Other charts**: (2) the funnel plot of the same estimates against precision (ch. 6 method) [L]; (3) the Kaitz index
  in the euro area / OECD? Not in approved data --- [L] or drop; (4) bunching picture from a simulated wage
  distribution [S].
- **Diagrams**: competitive floor (employment loss, DWL); monopsony with MC of labour and the floor in the
  employment-raising range; the bunching picture (missing and excess jobs bins).
- **Boxes**: `debate[The employment effect of a minimum wage]` --- the series' model box: question, the estimates by
  design (state panels, border pairs, bunching, large single increases: Seattle, Hungary, Germany 2015), each on the
  evidence scale with its weakness (choice of controls in panel studies; spillovers in border pairs; hours vs heads in
  Seattle; Hungary's large increase with price pass-through and some job loss in tradables); what is agreed (small
  effects of moderate increases on teen employment, near-full pass-through to some prices) and what is open (large
  increases relative to the median). `record[New Jersey and Pennsylvania, 1992]` (the design was ch. 3's: here the
  replies: Neumark--Wascher payroll data, Card--Krueger 2000 BLS data); `record[Germany's national minimum wage,
  2015]` (Dustmann et al. 2022: wages up, no employment loss, reallocation to more productive firms);
  `dated{2026}` minimum-wage levels in three countries and their Kaitz indices (ledger).
- **Exercises**: ★ 1 [R] read the opening chart (spread, sign, any trend); 2 [C] employment loss with elasticity
  $-0.2$ and a 10 % increase; 3 [C] monopsony wage and employment with linear curves; 4 [X] what observation would
  contradict monopsony for a given employer. ★★ 5 [C] markdown from $\varepsilon_{LS}$ = 4; 6 [C] employment with a
  floor in the monopsony range and above it; 7 (py) [C] bunching estimate from an invented wage histogram before/after;
  8 [P] price pass-through: restaurant price rise from labour share and wage rise; 9 [X] the ch. 6 funnel: what
  asymmetry would indicate. ★★★ 10 [C] prove the markdown formula; 11 (py) [C] FAT--PET on the chart's estimates
  (recalls ch. 6); 12 [P] a 40 % increase in a low-wage region: which model applies where.
- **Weekend problem --- "A minimum wage for Brenland"**: `households.csv` wages and `firms.csv` [B] plus an invented
  firm-level supply elasticity. Part I the competitive prediction; Part II monopsony: the employment-maximising
  floor; Part III bunching in Brenland's wage distribution after the floor; Part IV the reform evaluated by a
  border-pair DiD with Kestria (which has no floor). Named result: *the employment-maximising minimum wage in dalens per
  hour, and the measured employment effect of the actual floor*. 26 questions.
- **Ledger**: all studies above (15 rows plus their conversion notes); Manning 2021 (ILR Review); Dube--Jacobs--Naidu--
  Suri 2020; Azar--Marinescu--Steinbaum 2022; Burdett--Mortensen 1998; Doucouliagos--Stanley 2009 (funnel of the
  literature); minimum wage levels (AGENCY, dated 2026).

---

# Part VII --- Industrial organisation

Assumes Book 3 Part IV (monopoly pricing and the Lerner index, natural-monopoly pricing rules, Cournot and Bertrand)
and Book 4 Part III (static, dynamic, repeated and Bayesian games; first- and second-price auctions and the statement of
revenue equivalence). Ownership table: games g11 -> Y1 `cournot-and-bertrand` -> Y2 Part III -> Y3 Part VII.

## 27 `oligopoly-and-collusion` --- Oligopoly and Collusion

- **Sections**: 1 Differentiated products: location (Hotelling) and logit demand; 2 Entry and market structure
  (Bresnahan--Reiss); 3 Estimating market power (demand-side markups; production-side markups); 4 Tacit collusion;
  5 Detecting cartels; 6 Mergers and what retrospectives found.
- **Defines**: Hotelling model (linear city); product differentiation (horizontal, vertical); entry threshold;
  markup (price over marginal cost; Lerner index **recalled**); production-approach markup (De Loecker--Warzynski);
  tacit collusion; cartel; leniency programme; merger simulation; upward pricing pressure; merger retrospective.
  Repeated-game collusion condition: **recalled** (Year 2 volume).
- **Propositions**: Hotelling with quadratic transport costs: prices $c + t$ and maximal differentiation (proof);
  Bertrand with logit demand: markup $1/(\alpha(1-s_j))$ (proof, recalls ch. 5); Bresnahan--Reiss: entry thresholds
  rise less than proportionally if competition is fierce (derivation); collusion sustainable iff $\delta \ge$ a
  threshold rising with $n$ (recalled, extended to capacity and demand cycles); UPP formula (derivation).
- **Model boxes**: `model{Price competition with differentiated products}` (logit/Bertrand; predicts markups falling
  with own share's complement and with the price sensitivity; tested: merger simulations vs retrospectives (Peters
  2006 airline mergers: simulations under-predicted price rises); breaks: conduct not Bertrand, dynamic pricing);
  `model{Entry and market structure}` (Bresnahan--Reiss 1991: the fifth dentist adds little competition; breaks:
  quality competition).
- **Recalls**: Cournot, Bertrand, Lerner (Year 1 volume); repeated games, folk theorem (Year 2 volume); logit demand
  (ch. 5); DiD (ch. 3).
- **Opening chart**: *price changes after completed mergers, from retrospective studies* --- [L] one row per merger or
  study (Ashenfelter--Hosken 2010: five consumer-products mergers, 3--7 %; Kwoka 2015 meta-analysis mean ~7 %; Peters
  2006 airlines; Weinberg 2007 survey; Ashenfelter--Hosken--Weinberg 2015 Miller--Coors) --- ~8 rows with intervals.
- **Other charts**: (2) aggregate markups by the production approach, U.S. 1955--2016, as published (De Loecker--
  Eeckhout--Unger 2020: 1.21 to 1.61) [L] --- with the critique (Traina 2018 with operating expenses: much smaller rise)
  in a `record` box; or two numbers only; (3) a Hotelling equilibrium as a function of $t$ [S].
- **Diagrams**: the linear city with two firms and the indifferent consumer; best-response functions in prices
  (upward-sloping, strategic complements); the collusion condition: $\delta^*(n)$.
- **Boxes**: `record[The lysine cartel, 1992--1995]` (Connor 2001, overcharge, ledger); `record[The vitamins cartel]`
  --- one only; `record[Rising markups?]` (De Loecker et al. 2020 vs Traina 2018 vs Basu 2019, an open measurement
  question; a short balanced record, not a debate box since it is measurement); `measure[How a cartel is detected]`
  (screens: price variance falls, Abrantes-Metz et al. 2006).
- **Exercises**: ★ 1 [R] read the opening chart (median price change); 2 [C] Hotelling prices with $c$ = 10, $t$ = 4;
  3 [C] logit markup for a 20 % share, $\alpha$ = 0.5; 4 [X] what price data would contradict tacit collusion in a
  market. ★★ 5 [C] collusion threshold $\delta^*$ for $n$ = 2, 5; 6 [P] merger of two of three logit firms: price
  effect (simulation by hand, py helper); 7 [C] UPP for given diversion ratio and margin; 8 (py) [C] Bresnahan--Reiss
  thresholds from an invented town table; 9 [X] what would show a markup rise is a measurement artefact. ★★★ 10 [C]
  prove the logit markup formula; 11 (py) [C] merger simulation with nested choices (simple nested logit numbers given);
  12 [P] leniency programme: why it destabilises cartels (game with a reporting option).
- **Weekend problem --- "Three bakeries in Brenmoor"**: invented logit demand and costs; a proposed merger. Part I
  logit demand and equilibrium prices; Part II merger simulation: prices, shares, consumer surplus; Part III efficiency
  gains needed to offset (UPP); Part IV a retrospective two years later by DiD against another town. Named result:
  *the merger's predicted and measured price effects, and the cost saving that would have made it neutral*. 26
  questions.
- **Ledger**: Ashenfelter--Hosken 2010; Kwoka 2015 (book); Peters 2006; Weinberg 2007; Ashenfelter et al. 2015;
  De Loecker--Eeckhout--Unger 2020; Traina 2018; Basu 2019 (JEP); Bresnahan--Reiss 1991; Connor 2001; Abrantes-Metz et
  al. 2006; Farrell--Shapiro 2010 (UPP); DOJ/FTC 2023 Merger Guidelines (AGENCY, HHI thresholds dated).

## 28 `auctions-and-market-design` --- Auctions and Market Design

- **Sections**: 1 Auction formats; 2 Revenue equivalence, proved; 3 Reserve prices; 4 Common values and the winner's
  curse; 5 Multi-unit auctions and the record of spectrum sales; 6 Matching: deferred acceptance, school choice, kidney
  exchange.
- **Defines**: English auction; Dutch auction (first-price and second-price sealed bids, winner's curse: **recalled**
  from the Year 2 volume --- **contested** with the AI series' definitions in prose only); independent private values;
  revenue equivalence theorem (proved here; stated in the Year 2 volume --- the definition pair belongs to whichever
  book the sync names); optimal reserve price; affiliated / common values; linkage principle (told); simultaneous
  ascending auction; clock auction; stable matching; deferred acceptance algorithm; strategy-proofness; top trading
  cycles; kidney exchange.
- **Propositions with proofs**: revenue equivalence for symmetric IPV, risk-neutral bidders, via the envelope theorem
  (Year 1 volume's envelope theorem recalled); optimal reserve $r$ solves $r - (1-F(r))/f(r) = v_0$ (proof); with
  uniform values, $r$ = 1/2 regardless of $n$ (example); deferred acceptance yields a stable matching, optimal for the
  proposing side (proof, Gale--Shapley); DA is strategy-proof for proposers ($\admitted$, Dubins--Freedman); TTC is
  Pareto efficient and strategy-proof ($\admitted$).
- **Model box**: `model{Independent private values}` (predicts revenue equivalence; tested: laboratory auctions ---
  bidding above risk-neutral Nash in first-price auctions (Kagel 1995), and field tests of formats (Lucking-Reiley 1999
  online magic cards: Dutch raised revenue ~30 %, ledger to verify); breaks: risk aversion, asymmetry, common values).
- **Recalls**: Bayesian Nash equilibrium, first- and second-price auctions, revenue equivalence statement, winner's
  curse (Year 2 volume); envelope theorem (Year 1 volume); order statistics (simple expectations from the mathematics
  books).
- **Opening chart**: *revenue per person from the European third-generation mobile licence auctions, 2000--2001* --- [L]
  Klemperer (2002, EER or JEP "How (not) to run auctions") table: U.K., Germany, Italy, Netherlands, Austria,
  Switzerland, Belgium, Greece, Denmark (euro per person, ~9 rows from one table).
- **Other charts**: (2) expected revenue against the reserve price, uniform values, $n$ = 2, 5 [S, analytic]; (3) the
  kidney exchange's transplants by year: not in approved data --- [L] from the U.S. UNOS/OPTN or the U.K. NHSBT
  annual report (a few rows) or drop.
- **Diagrams**: bid functions in a first-price auction ($b(v) = \frac{n-1}{n} v$, uniform); the deferred acceptance
  rounds as a small table-diagram (3 students x 3 schools); a 3-pair kidney exchange cycle.
- **Boxes**: `record[Spectrum auctions: the U.K. and the Netherlands, 2000]` (format, entry, revenue); `record[The
  U.S. incentive auction, 2016--2017]` (FCC, ledger); `record[Boston's school choice, 2005]` (Abdulkadiroğlu--Pathak--
  Roth--Sönmez 2005: replacing the Boston mechanism with DA); `measure[Measuring a matching market's stability]`.
- **Exercises**: ★ 1 [R] read the opening chart (spread of revenue); 2 [C] expected revenue of a second-price auction
  with 3 uniform bidders; 3 [C] first-price bid function at $v$ = 0.6, $n$ = 4; 4 [X] what lab evidence contradicts
  revenue equivalence. ★★ 5 [C] optimal reserve with uniform values and $v_0$ = 0.2; 6 [C] run DA on a 4x4 table;
  7 [P] entry deterrence in an English auction with an asymmetric strong bidder (Dutch hybrid, told); 8 [C] winner's
  curse: expected value given winning with a signal; 9 [X] what an applicant's strategy data would show if a mechanism
  is not strategy-proof. ★★★ 10 [C] prove revenue equivalence with the envelope argument; 11 (py) [C] simulate four
  formats with risk-averse bidders; 12 [P] TTC on a 4-pair kidney exchange.
- **Weekend problem --- "Brenland sells its radio spectrum"**: invented bidders' value distributions, licences, and a
  school-choice market in Brenmoor. Part I format choice: revenue of English vs sealed-bid; Part II the reserve price;
  Part III two licences: substitutes, exposure; Part IV Brenmoor's schools: DA vs the old mechanism. Named result: *the
  revenue-maximising reserve and the expected revenue, and the matching DA produces*. 25 questions.
- **Ledger**: Klemperer 2002; Binmore--Klemperer 2002 (U.K. 3G); Lucking-Reiley 1999; Kagel 1995 (Handbook);
  Milgrom 2004; FCC incentive auction (AGENCY); Gale--Shapley 1962; Abdulkadiroğlu et al. 2005; Roth--Sönmez--Ünver
  2004; Myerson 1981; Riley--Samuelson 1981.

## 29 `platforms-and-innovation` --- Platforms and Innovation

- **Sections**: 1 Network effects and tipping; 2 Pricing on two sides; 3 Switching costs; 4 Patents: the incentive and the
  deadweight loss; 5 Patent races; 6 Competition and innovation; 7 Entry and exit of firms as a source of productivity
  growth.
- **Defines**: network effect (direct, indirect); critical mass; tipping; two-sided platform; switching cost; patent
  (as an institution: term, breadth); optimal patent length (Nordhaus trade-off); patent race; Arrow replacement effect;
  inverted-U relation between competition and innovation (Aghion et al.); reallocation decomposition (within,
  between, entry, exit; Foster--Haltiwanger--Krizan); business dynamism (entry and exit rates).
- **Propositions**: with network effects, demand has multiple equilibria (proof in the Rohlfs model); two-sided pricing:
  the side with the larger cross-externality is subsidised (Rochet--Tirole / Armstrong, proof in a linear model);
  switching costs: bargains then rip-offs (two-period proof); Arrow: a monopolist gains less from a cost-reducing
  innovation than an entrant (proof); the FHK decomposition (identity, derivation).
- **Model boxes**: `model{Two-sided platforms}` (predicts below-cost prices on one side; tested: payment cards, video
  games, newspapers' pricing; Rysman 2009 survey; breaks: multi-homing); `model{Competition and innovation, the
  inverted U}` (Aghion--Bloom--Blundell--Griffith--Howitt 2005, U.K. panel; breaks: the shape depends on the measure,
  later replications mixed).
- **Recalls**: growth through ideas, replacement (Year 2 volume, `endogenous-growth`); monopoly DWL (Year 1 volume);
  dynamic games (Year 2 volume).
- **Opening chart**: *the share of productivity growth from the entry and exit of firms, by study and sector* --- [L]
  Foster--Haltiwanger--Krizan 2001 (U.S. manufacturing 1977--87: net entry ~25 % of five-year and ~50 % of ten-year
  growth), FHK 2006 (U.S. retail: nearly all), Baily--Hulten--Campbell 1992, Bartelsman--Haltiwanger--Scarpetta 2009
  (cross-country), Disney--Haskel--Heden 2003 (U.K.) --- 6--8 rows, to verify.
- **Other charts**: (2) patent applications by residents per million people against income, 2019 [A] `IP.PAT.RESD`,
  `SP.POP.TOTL`, `NY.GDP.PCAP.PP.KD`; (3) R&D spending as % of GDP, 1996--2024, six economies [A]
  `GB.XPD.RSDV.GD.ZS`; (4) new business density across countries [A] `IC.BUS.NDNS.ZS` --- choose two of the three.
- **Diagrams**: network-effect demand (inverted U willingness-to-pay with two equilibria and critical mass); the
  patent trade-off (DWL during the patent vs the innovation's value); the inverted U.
- **Boxes**: `record[The QWERTY claim, examined]` (Liebowitz--Margolis 1990 on lock-in evidence) --- or a cleaner
  case; `record[Patent buyouts and patent terms]` (Williams 2013, human genome IP: Celera's IP lowered follow-on
  research ~20--30 %, ledger to verify; Sampat--Williams 2019 found no effect for gene patents --- two studies, one
  record); `measure[How productivity growth is decomposed]`.
- **Exercises**: ★ 1 [R] read the opening chart (entry/exit share); 2 [C] FHK decomposition of a 4-firm table;
  3 [C] Rohlfs equilibria with a given demand; 4 [X] what data would contradict tipping in a market with two
  platforms. ★★ 5 [C] two-sided prices in a linear model; 6 [P] switching costs and first-period prices; 7 [C] Arrow
  replacement: gains of monopolist vs entrant; 8 (py) [R] R&D vs patents across countries; 9 [X] the inverted U: what
  shape would refute it in a panel. ★★★ 10 [C] prove the two-sided pricing rule; 11 [C] optimal patent length in the
  Nordhaus model with numbers; 12 (py) [C] FHK on `firms.csv`-based invented two-year panel [B].
- **Weekend problem --- "Brenmoor's ride platform"**: invented riders, drivers, cross-externalities. Part I network
  demand and critical mass; Part II two-sided pricing; Part III a rival platform and multi-homing; Part IV productivity
  of Brenland's taxi sector before and after entry, decomposed. Named result: *the platform's price structure and the
  share of sector productivity growth from entry and exit*. 24 questions.
- **Ledger**: FHK 2001, 2006; Baily et al. 1992; Bartelsman et al. 2009; Disney et al. 2003; Aghion et al. 2005; Rysman
  2009; Rochet--Tirole 2003; Armstrong 2006; Arrow 1962 (label); Nordhaus 1969 (label); Williams 2013; Sampat--Williams
  2019; Liebowitz--Margolis 1990; Klemperer 1987 (switching costs).

## 30 `competition-policy` --- Competition Policy and Regulation

- **Sections**: 1 Defining a market and measuring concentration; 2 Vertical restraints: efficiency and foreclosure, with
  the evidence; 3 Pricing rules for natural monopolies and how firms respond to them; 4 The record of deregulation;
  5 Errors of both kinds.
- **Defines**: relevant market; hypothetical monopolist (SSNIP) test; Herfindahl--Hirschman index (**contested**: may be
  Book 3's, `cournot-and-bertrand` or `monopoly-pricing`); vertical restraint; resale price maintenance; exclusive
  dealing; double marginalisation; foreclosure; rate-of-return regulation; Averch--Johnson effect; yardstick
  competition; type I and type II errors of enforcement. Average-cost and price-cap rules: **recalled** (Year 1 volume).
- **Propositions**: HHI and the average Cournot Lerner index: $\bar L = HHI/\varepsilon$ (proof); double
  marginalisation: vertical integration lowers the retail price (proof with linear demand); critical loss of a SSNIP
  (derivation); Averch--Johnson: capital over-use under binding rate-of-return regulation (proof with a Lagrangian);
  price caps (RPI$-X$) give cost-reduction incentives that rate of return does not (shown in a two-period example).
- **Model box**: `model{Rate-of-return regulation}` (predicts over-capitalisation; tested: mixed --- Courville 1974
  supportive, later studies weak; price caps' cost reductions in U.K. utilities (ledger); breaks: regulatory lag acts
  like a price cap).
- **Recalls**: natural monopoly, price-cap and average-cost rules, Lerner index (Year 1 volume); Cournot (Year 1
  volume); ch. 22 (capture), ch. 27 (mergers).
- **Opening chart**: *real air fares in the United States before and after the 1978 deregulation* --- [L] real yield
  per passenger-mile at a few dates (Borenstein--Rose 2014, NBER *Economic Regulation and Its Reform*, figure numbers
  or tables; or the A4A annual summary) --- or, **preferred**, [A] the BLS CPI airline fares index (`CUUR0000SETG01`,
  from 1963? to verify) deflated by the all-items CPI, if the main session derives that series from the approved BLS
  files (no new download).
- **Other charts**: (2) HHI and critical loss as functions of margins [S, analytic]; (3) price index of telephone
  services or another deregulated industry from the same BLS files [A if derived] --- or drop.
- **Diagrams**: double marginalisation (two-stage markups); Averch--Johnson isoquant with the regulatory constraint;
  the error trade-off (type I vs type II as a function of the standard of proof).
- **Boxes**: `record[Airline deregulation, 1978]` (Morrison--Winston 1986/1995 gains; hub premia, Borenstein 1989);
  `record[Resale price maintenance after Leegin, 2007]` (MacKay--Smith 2014 price and quantity evidence, ledger);
  `record[The break-up of AT&T, 1984]` --- one of the two; `measure[The SSNIP test]`; `dated{2026}` HHI thresholds of
  the U.S. 2023 guidelines and the EU guidelines (ledger).
- **Exercises**: ★ 1 [R] read the opening chart; 2 [C] HHI of a 5-firm market, before and after a merger; 3 [C]
  double marginalisation: prices separate vs integrated; 4 [X] what price data would show RPM is collusive rather than
  service-promoting. ★★ 5 [C] critical loss for a 5 % SSNIP and 40 % margin; 6 [C] Lerner from HHI with
  $\varepsilon$ = 2; 7 [P] Averch--Johnson with numbers; 8 (py) [R] BLS fares series (if derived): real change
  1978--2000; 9 [X] what would refute the "deregulation lowers prices" claim for a route. ★★★ 10 [C] prove
  $\bar L = HHI/\varepsilon$; 11 [P] price cap RPI$-X$ with productivity growth: profits and prices over five years;
  12 [P] error costs: optimal standard of proof under given priors.
- **Weekend problem --- "Brenland's water company"**: invented natural monopoly: cost function, demand, regulator.
  Part I unregulated monopoly; Part II average-cost pricing and its DWL (recall); Part III rate-of-return regulation and
  capital over-use; Part IV a price cap with $X$ and the cost reduction it induces. Named result: *consumer and producer
  surplus under each regime, and the $X$ that shares the cost saving equally*. 25 questions.
- **Ledger**: Borenstein--Rose 2014; Morrison--Winston 1995; Borenstein 1989; MacKay--Smith 2014; Averch--Johnson 1962;
  Courville 1974; DOJ/FTC 2023 guidelines (AGENCY), EU horizontal merger guidelines (LAW); Joskow 2007 (review);
  BLS series if derived (no row needed: dataset).

---

# Part VIII --- Growth, development and environment

The data strand's closing chapters. Assumes Book 3 `solow-model`, `growth-accounting`, Book 4 `ramsey-model`,
`endogenous-growth`, `overlapping-generations`, `externalities-and-public-goods-theory`.

## 31 `growth-empirics` --- Growth Empirics and Convergence

- **Sections**: 1 Growth rates across countries and decades; 2 Convergence: absolute, conditional; 3 Cross-country growth
  regressions and their fragility; 4 Growth miracles and disasters; growth that stops; 5 The move out of agriculture.
- **Defines**: beta convergence; sigma convergence; conditional convergence; growth regression; robustness of a growth
  determinant (extreme-bounds analysis; Bayesian averaging told); growth acceleration (Hausmann--Pritchett--Rodrik
  rule); growth collapse; structural transformation; agricultural productivity gap.
- **Propositions**: Solow's linearisation gives $\ln y_{T} - \ln y_0 = -(1-e^{-\lambda T})(\ln y_0 - \ln y^*)$ and the
  speed $\lambda = (1-\alpha)(n+g+\delta)$ (recalled derivation, used to read $\beta$); beta convergence is necessary,
  not sufficient, for sigma convergence (proof, Galton's fallacy --- regression to the mean recalled from the Year 1
  volume); persistence of growth: low decade-to-decade correlation (Easterly et al. 1993) as a measured fact.
- **Model box**: `model{The augmented Solow model in cross-country data}` (Mankiw--Romer--Weil 1992: assumes common
  technology, exogenous saving and schooling; predicts conditional convergence at ~2 % a year; tested: MRW, PWT
  re-estimates; breaks: TFP differences are large (Hall--Jones 1999), fixed-effects estimates give much faster
  convergence (Islam 1995) --- panel bias recalled from ch. 2).
- **Recalls**: Solow model, speed of convergence, growth accounting (Year 1 volume); Ramsey, endogenous growth (Year 2
  volume); panel data (ch. 2); credible empirical work and specification search (ch. 6).
- **Opening chart**: *growth of income per person by country, decade by decade, 1960s to 2010s* --- [A] `pwt(cols=
  ["rgdpe","pop"])` or Maddison `gdppc`: per-country decadal growth as dots (strip chart), with the median per decade.
- **Other charts**: (2) absolute convergence: growth 1960--2019 against 1960 income, all countries and the OECD-1960
  subset [A PWT/Maddison]; (3) correlation of a country's growth across successive decades [A]; (4) employment share of
  agriculture against income per person [A] `SL.AGR.EMPL.ZS`; (5) Maddison per-person income of Argentina, Japan,
  South Korea, and Venezuela? (miracles and disasters, 1900--2022) [A] --- choose 3--4 charts in all.
- **Diagrams**: beta vs sigma convergence sketch (dispersion of log incomes over time); the HPR acceleration rule on a
  stylised series.
- **Boxes**: `record[The East Asian growth miracle]` (Young 1995: accumulation vs TFP; Hsieh 2002 dual measures);
  `record[Growth that stops: Argentina in the twentieth century]` (Maddison numbers, figdata); `measure[Which vintage of
  the data?]` (Johnson--Larson--Papageorgiou--Subramanian 2013: growth rates differ across PWT vintages);
  `record[Fragile determinants]` (Levine--Renelt 1992; Sala-i-Martin 1997 "I just ran two million regressions").
- **Exercises**: ★ 1 [R] read the opening chart (dispersion by decade); 2 [C] convergence speed from $\beta$; 3 [C]
  doubling time at 2 % vs 7 %; 4 [X] what data would contradict conditional convergence. ★★ 5 (py) [C] absolute
  convergence regression on PWT, two samples; 6 (py) [C] decade-to-decade growth correlation; 7 [P] MRW: predicted steady
  state from saving and schooling for two countries; 8 [C] HPR rule on a given series; 9 [X] Galton's fallacy: what
  sigma would show. ★★★ 10 [C] derive the speed of convergence; 11 (py) [C] extreme bounds on an invented cross-country
  table [S]; 12 [P] structural transformation: aggregate productivity growth from moving 10 % of workers out of farming
  with a given productivity gap.
- **Weekend problem --- "Brenland's fifty years"**: `accounts.csv` [B] plus an invented long series extending Brenland
  back to 1975 with the same seed logic (in figdata). Part I growth rates and doubling; Part II Brenland among
  invented peers: beta convergence; Part III its growth acceleration and the HPR test; Part IV structural
  transformation's share of its growth. Named result: *Brenland's convergence speed and the share of its growth from
  the move out of farming*. 24 questions.
- **Ledger**: Mankiw--Romer--Weil 1992; Islam 1995; Hall--Jones 1999; Easterly--Kremer--Pritchett--Summers 1993;
  Hausmann--Pritchett--Rodrik 2005; Levine--Renelt 1992; Sala-i-Martin 1997; Young 1995; Hsieh 2002; Johnson et al.
  2013; Gollin--Lagakos--Waugh 2014 (agricultural productivity gap); Barro 1991.

## 32 `institutions` --- Institutions and Long-Run Prosperity

- **Sections**: 1 Defining and measuring institutions; 2 The natural experiments, treated with the methods of Part I:
  the two Koreas, the two Germanys, China's reforms from 1978; 3 Instruments for institutions and their critics;
  4 Planned economies in the data; 5 The transitions of the 1990s; 6 Crime, corruption and the rule of law (programme
  gap: economics of crime; told, with two natural experiments --- to confirm at sync).
- **Defines**: institutions (re-founded: rules of the game, with a measurement); property rights; rule of law (as a
  measured index); expropriation risk; settler-mortality instrument; planned economy (re-founded: allocation by plan,
  with the soft budget constraint); soft budget constraint (Kornai, as the result's label); transition recession;
  deterrence elasticity of crime (if section 6 kept).
- **Propositions**: none beyond the econometric ones (IV conditions applied: proof that the reduced form of income on
  settler mortality divided by the first stage is the 2SLS coefficient --- recalls ch. 1); a simple holdup/expropriation
  model: investment falls with the expropriation probability (proof).
- **Model box**: `model{Institutions as the cause of income differences}` (assumes secure property rights and
  constraints on rulers raise investment; predicts large income gaps between neighbours with different rules;
  tested: Korea, Germany, China 1978, AJR 2001, Dell 2010; breaks: the measures of institutions are outcomes
  themselves; Glaeser et al. 2004).
- **Recalls**: institutions and the three natural experiments (grades 6--9 and 10--12 volumes); growth accounting,
  misallocation, planned economies' low TFP growth (Year 1 volume); prices as information and planned economies'
  internal prices (Year 2 volume); IV, DiD, RD, synthetic control (ch. 1--4).
- **Opening chart**: the outline's (East and West Germany, 1950 to today) needs separate series for the two states,
  which Maddison 2023 does not carry. **Proposal** [A]: *income per person in China, 1950--2022 (with 1978 marked), and in
  Western and Eastern Europe (Maddison's own regional estimates), 1950--2022*, `maddison("CHN")`,
  `maddison_regions(["Western Europe","Eastern Europe"])`. The two Koreas are drawn from 1990 only (Maddison's North
  Korea series starts in 1990) on chart 2; the two Germanys in a `record` box with ledger numbers (GDR productivity
  in 1990 about one third of the West's; Sinn--Sinn 1992 or official statistics; to verify).
- **Other charts**: (2) the two Koreas, 1990--2022 [A] `maddison(["KOR","PRK"])`; (3) [?] rule of law against income
  across countries --- needs the Worldwide Governance Indicators (data to approve); fallback none: a `measure` box
  describes the indices with ledger numbers for three countries; (4) the transition recessions: income per person in
  Poland, Russia, Ukraine, Czechia, 1985--2022 [A] Maddison (`POL`, `RUS`, `UKR`, `CZE` with `CSK`/`SUN` before;
  caption on the break).
- **Diagrams**: the AJR causal chain with the exclusion restriction marked; the expropriation/investment model diagram.
- **Photos**: the Korean peninsula at night from the International Space Station (NASA, public domain; verify the
  file's licence page).
- **Boxes**: `debate[Geography, institutions or culture?]` --- AJR 2001 (AER: settler mortality as an instrument;
  institutions explain most of the gap; grade 2); Albouy 2012 (AER: mortality data constructed from few observations;
  the first stage weakens; grade 2 critique); Glaeser--La Porta--Lopez-de-Silanes--Shleifer 2004 (JEG: human capital
  first, institutions measures are outcomes); Sachs 2003 (NBER WP: malaria and geography matter directly);
  Tabellini 2010 (JEEA: culture within European regions); Dell 2010 (Econometrica: the mita, an RD --- institutions
  persist locally; grade 1--2). Weaknesses for each. `record[China's household responsibility system, 1978--1984]`
  (Lin 1992: about half of output growth in agriculture, ledger to verify); `record[Two Germanys]`;
  `record[Transition: big bang and gradual paths]` (EBRD transition reports, ledger); `measure[Measuring institutions]`.
- **Exercises**: ★ 1 [R] read the opening chart (China before and after 1978); 2 [C] the Korean gap in 2022 as a ratio
  and in doubling times; 3 [C] IV: 2SLS from AJR-style reduced form and first stage numbers (given); 4 [X] what would
  contradict institutions as the main cause for the Koreas. ★★ 5 [C] expropriation risk and investment in the
  holdup model; 6 [P] Albouy's critique: direction of the change when the first stage weakens; 7 (py) [R] transition
  recessions: depth and duration in four countries; 8 [C] synthetic-control reading of a published reunification gap
  (ledger numbers); 9 [X] what pattern in Dell's mita data would break the RD. ★★★ 10 [C] exclusion restriction: build
  a case where settler mortality affects income through health; 11 [P] soft budget constraint: firm effort with and
  without bail-out; 12 [P] deterrence: crime response to a police increase with an elasticity (Levitt 1997;
  Di Tella--Schargrodsky 2004) --- if section 6 kept.
- **Weekend problem --- "Brenland and the land across the river"**: invented twin regions with one shared history up to
  a split and different property regimes after; seeded series. Part I the gap and its growth path; Part II a
  synthetic control for the region that reforms; Part III an instrument for property security (invented) and 2SLS;
  Part IV the investment model calibrated to the gap. Named result: *the share of the income gap explained by property
  security, by 2SLS*. 24 questions.
- **Ledger**: AJR 2001; Albouy 2012; Glaeser et al. 2004; Sachs 2003; Tabellini 2010; Dell 2010; Lin 1992; Kornai 1986;
  Sinn--Sinn 1992; EBRD reports (AGENCY); Levitt 1997; Di Tella--Schargrodsky 2004; Burchardi--Hassan 2013 or Redding--
  Sturm 2008 (division of Germany as an experiment, told).

## 33 `demographic-transition` --- Population and the Demographic Transition

- **Sections**: 1 The Malthusian model in its frame: tested on wages and population before 1800, broken after; 2 The
  demographic transition; 3 The trade-off between the number of children and their schooling; 4 Ageing and the
  dependency ratio.
- **Defines**: Malthusian model (re-founded? not in the school map --- owned here); Malthusian equilibrium (subsistence
  income); demographic transition; total fertility rate (**contested**: the grades 6--9 volume owns "births per woman";
  here the formal definition, to confirm); net reproduction rate; quantity--quality trade-off (Becker--Lewis);
  demographic dividend; old-age dependency ratio (**contested** with Book 4 `overlapping-generations`).
- **Propositions**: Malthusian dynamics: with population growth rising in income and income falling in population, a
  stable steady state at subsistence; a technology gain raises population, not income, in the long run (proof, phase
  line); Becker--Lewis: with a quality cost proportional to numbers, a rise in the return to schooling lowers the number
  of children (proof in the Cobb--Douglas case); dependency arithmetic: PAYG contribution rate = benefit ratio x
  dependency ratio (recalled from the Year 2 volume, applied).
- **Model box**: `model{The Malthusian model}` (in its frame, user ruling: assumes diminishing returns to labour on fixed
  land and population growth rising with income; predicts stagnant income per person, population tracking technology;
  tested: England 1250--1800, the Black Death raising real wages (Clark 2007; Broadberry et al. 2015); Ashraf--Galor
  2011 cross-country: technology raised density, not income, before 1500; breaks: after about 1800, income and
  population rise together, and then fertility falls with income).
- **Recalls**: life expectancy, births per woman, ageing (grades 6--9 volume); OLG, pensions, the arithmetic of ageing
  (Year 2 volume); Solow (Year 1 volume).
- **Opening chart**: the outline's (real wages and population in England, 1250--1850) needs the Bank of England's
  Millennium dataset or Clark's series [?]. **Fallback** [A]: *income per person and population, England/Great
  Britain, 1252--1850* `maddison("GBR", until=1850)` (gdppc, pop; Broadberry et al. series inside Maddison).
  Real wages appear if the Millennium dataset is approved.
- **Other charts**: (2) the demographic transition: crude birth and death rates from 1960 [A] `SP.DYN.CBRT.IN`,
  `SP.DYN.CDRT.IN` (checked), and total fertility, 1800--2024, for six countries
  [A] Gapminder `children_per_woman_total_fertility` to 1949 spliced with WDI `SP.DYN.TFRT.IN` from 1960 (the splice
  named in the source line); (3) fertility against income per person, 2023 [A]; (4) old-age dependency ratio,
  1960--2025, six economies [A] `SP.POP.DPND.OL` (projections need UN WPP --- not approved; no projection line).
- **Diagrams**: the Malthusian two-panel diagram (birth/death rates against income; income against population with
  technology shift); the Becker--Lewis budget set in (number, quality).
- **Boxes**: `record[The Black Death, 1348--1351]` (Maddison figdata: income rise after the population fall);
  `record[China's birth policy, 1980--2015]` (natural-experiment evidence on quantity--quality: Rosenzweig--Zhang 2009,
  Qian 2009 --- balanced); `record[Twins and family size]` (Black--Devereux--Salvanes 2005: no quantity--quality
  trade-off in Norway once birth order is controlled; Angrist--Lavy--Schlosser 2010 null); `measure[The total
  fertility rate]`.
- **Exercises**: ★ 1 [R] read the opening chart (pre-1800 co-movement; after); 2 [C] Malthusian steady state with
  linear curves; 3 [C] dependency ratio and PAYG rate; 4 [X] what pre-1800 data would contradict the Malthusian model.
  ★★ 5 [P] a technology gain: path of income and population (phase line); 6 [C] TFR from age-specific rates (table);
  7 (py) [C] fertility--income slope, 1960 vs 2023; 8 [P] Becker--Lewis: return to schooling rises; 9 [X] what twins
  evidence would contradict the trade-off. ★★★ 10 [C] prove stability of the Malthusian steady state; 11 (py) [C]
  Maddison: correlation of income and population growth before and after 1800 for England; 12 [P] the demographic
  dividend: income per person when the working-age share rises 10 points.
- **Weekend problem --- "Brenland before the factories"**: an invented agrarian Brenland, 1500--1900, with land,
  technology, a plague and an industrial take-off; seeded series. Part I Malthusian dynamics; Part II the plague and
  the wage rise; Part III the take-off and fertility decline with Becker--Lewis; Part IV ageing and the PAYG rate in
  2025 using `accounts.csv` population [B]. Named result: *the Malthusian steady-state income, the plague's wage
  premium, and Brenland's PAYG contribution rate in 2025*. 25 questions.
- **Ledger**: Clark 2007 (book) / Clark 2005 (JPE); Broadberry et al. 2015; Ashraf--Galor 2011 (AER); Becker--Lewis
  1973; Black--Devereux--Salvanes 2005 (QJE); Angrist--Lavy--Schlosser 2010 (JOLE); Rosenzweig--Zhang 2009; Qian 2009
  (NBER WP); Galor--Weil 2000 (unified growth, told).

## 34 `development-microeconomics` --- Development Microeconomics

- **Sections**: 1 Measuring poverty in depth; 2 Health and nutrition; 3 Schooling programmes; 4 Credit and
  microfinance: the randomised evidence; 5 Cash transfers; 6 Property titles; 7 Aid and growth; 8 Whether a result
  travels.
- **Defines**: poverty gap index; squared poverty gap (Foster--Greer--Thorbecke family); international poverty line
  (re-founded from the grades 6--9 volume? --- "poverty line" is g6's; here only the FGT measures are new);
  nutrition-based poverty trap (efficiency-wage model of nutrition); microcredit; group liability; conditional cash
  transfer; unconditional cash transfer; property titling; external validity (Book 4 "whether a result travels" ---
  **contested**: recall); general-equilibrium effects of a programme (told).
- **Propositions**: FGT axioms: $P_1$ satisfies monotonicity, $P_2$ also transfer sensitivity (proof); a nutrition-
  based poverty trap needs an S-shaped capacity curve (proof, phase line); a transfer that is fully consumed vs
  invested: the test of a poverty trap from the effect of a one-time transfer (Balboni et al. 2022, stated).
- **Model box**: `model{The poverty trap}` (assumes increasing returns at low wealth; predicts that a large enough
  one-time transfer moves households to a higher path, a small one does not; tested: Bandiera et al. 2017 /
  Balboni et al. 2022 (Bangladesh asset transfers: a threshold found), Banerjee et al. 2015 (six-country graduation
  programme); breaks: many tests find no threshold --- Kraay--McKenzie 2014).
- **Recalls**: poverty line and poverty rate (grades 6--9 volume); RCTs and external validity (Year 2 volume); IV, RD
  (ch. 1, 4); meta-analysis (ch. 6); human capital (ch. 24).
- **Opening chart**: *measured effects of microcredit on household business profit (or consumption) in seven
  randomised studies* --- [L] Meager (2019, AEJ: Applied) table of the seven studies' estimates and standard errors
  (Angelucci et al. Mexico; Attanasio et al. Mongolia; Augsburg et al. Bosnia; Banerjee et al. India; Crépon et al.
  Morocco; Karlan--Zinman Philippines; Tarozzi et al. Ethiopia) and her pooled estimate.
- **Other charts**: (2) the world poverty headcount, poverty gap and squared gap at \$3.00 a day, by region, latest
  year [A] `pip_percentiles(...)` (FGT measures computed from the percentiles: the measurement lesson of section 1);
  (3) the Progresa effects on enrolment by grade [L] (Schultz 2004 table) --- or a `record` box; (4) aid received as %
  of GNI against growth, 1990--2019, country averages [A] `DT.ODA.ALLD.CD` / `NY.GDP.MKTP.CD` and growth (the
  correlation the debate box warns about).
- **Diagrams**: the poverty-trap phase line (S-shaped capacity curve); FGT measures on a Pen's-parade sketch; the
  group-liability game (two borrowers).
- **Boxes**: `debate[Aid and growth]` --- Burnside--Dollar 2000 (AER: aid helps in good policy environments; grade 3);
  Easterly--Levine--Roodman 2004 (AER: result disappears with more data); Rajan--Subramanian 2008 (REStat: no robust
  effect, with an instrument); Clemens--Radelet--Bhavnani--Bazzi 2012 (EJ: modest positive effect of early-impact aid);
  Galiani--Knack--Xu--Zou 2017 (JEG: IDA income threshold as an instrument, positive effect; grade 2). Weaknesses:
  instruments, reverse causation, heterogeneity of aid. `record[Progresa, 1997]` (Schultz 2004: enrolment up, mostly in
  secondary transition); `record[GiveDirectly in Kenya]` (Haushofer--Shapiro 2016; Egger et al. 2022 local multiplier
  ~2.5, ledger to verify); `record[Deworming]` (Miguel--Kremer 2004 and the replication exchange: Aiken et al. 2015,
  Hicks et al. 2015 --- a case for ch. 6's lessons); `record[Land titles in Buenos Aires]` (Galiani--Schargrodsky 2010)
  or Peru (Field 2007) --- one; `measure[The FGT poverty measures]`.
- **Exercises**: ★ 1 [R] read the opening chart (pooled vs single estimates); 2 [C] FGT measures for 5 households;
  3 [C] the transfer needed to end poverty in a given table (the poverty gap times $N$ times $z$); 4 [X] what result
  would contradict the poverty-trap model in an asset-transfer RCT. ★★ 5 (py) [C] FGT from PIP percentiles for one
  country; 6 [C] inverse-variance pooled estimate from the seven studies (recall ch. 6); 7 [P] group liability and
  repayment; 8 [C] a CCT's cost per extra year of schooling (given effects); 9 [X] what would show a GiveDirectly
  effect is a price effect, not real consumption. ★★★ 10 [C] prove transfer sensitivity of $P_2$; 11 (py) [C]
  heterogeneity across the seven studies ($\tau^2$, recall ch. 6); 12 [P] scaling up: general-equilibrium effects of a
  transfer programme on local prices.
- **Weekend problem --- "A cash transfer for Brenland's poorest districts"**: `households.csv` [B] (disposable income,
  food). Part I poverty line, headcount, gap; Part II a randomised transfer across invented districts; Part III a
  threshold test of a poverty trap; Part IV cost-effectiveness against a training programme. Named result: *the effect
  of the transfer on consumption after two years, with its interval, and the cost per household lifted above the
  line*. 26 questions.
- **Ledger**: Meager 2019 (7 rows + pooled); Banerjee--Karlan--Zinman 2015 (AEJ: Applied intro); Foster--Greer--
  Thorbecke 1984; Schultz 2004; Haushofer--Shapiro 2016; Egger et al. 2022 (Econometrica); Miguel--Kremer 2004; Aiken
  et al. 2015; Hicks--Kremer--Miguel 2015; Galiani--Schargrodsky 2010; Field 2007; Burnside--Dollar 2000; Easterly et
  al. 2004; Rajan--Subramanian 2008; Clemens et al. 2012; Galiani et al. 2017; Bandiera et al. 2017; Balboni et al.
  2022; Banerjee et al. 2015 (Science); Kraay--McKenzie 2014; Dasgupta--Ray 1986 (nutrition model).

## 35 `environmental-and-resource-economics` --- Environmental and Resource Economics

- **Sections**: 1 Valuing damages; 2 Taxes, permits and standards compared on the evidence; 3 Pollution against income: a
  hump for local pollutants, none for carbon dioxide; 4 The social cost of carbon as a calculation, and what
  discounting does to it; 5 Exhaustible resources: the rule for their price, and its failure in the data; 6 Learning
  curves in energy.
- **Defines**: damage function; marginal abatement cost; emission standard (performance vs technology); environmental
  Kuznets curve; social cost of carbon; Ramsey formula for the discount rate (label `ramsey-discount`; distinct from
  ch. 17's Ramsey rule and Book 4's Ramsey model); Hotelling rule; scarcity rent; backstop technology; learning rate
  (per doubling of cumulative output). Corrective tax, permits, Coase, prices vs quantities: **recalled** (Year 2
  volume); learning by doing: **recalled** (Year 1 volume).
- **Propositions with proofs**: equal marginal abatement costs minimise total cost, achieved by a uniform tax or a
  traded permit, not by uniform standards (proof); Weitzman's comparison recalled and applied with numbers;
  Hotelling: the net price rises at the interest rate (proof by arbitrage, then by optimal control told); the SCC as
  the discounted sum of marginal damages (derivation), its sensitivity to $\rho$ and $\eta$ in $r = \rho + \eta g$
  (Ramsey formula, derivation from the Euler equation recalled); learning curve: cost $\propto Q^{-b}$, learning rate
  $1-2^{-b}$ (derivation).
- **Model boxes**: `model{The Hotelling rule}` (assumes known stock, competitive owners, no extraction-cost change;
  predicts rising real prices; tested: real mineral prices flat or falling over a century (Krautkraemer 1998; Livernois
  2009); breaks: discoveries, technical change in extraction, backstops); `model{The environmental Kuznets curve}`
  (predicts pollution first rising then falling with income; tested: SO2 hump in CEDS data (this chapter), Grossman--
  Krueger 1995; breaks: CO2 per person keeps rising with income across countries, and the hump comes from regulation,
  not income itself --- Stern 2004).
- **Recalls**: externality (grades 10--12 volume); corrective tax, Coase, prices vs quantities, emission-permit price
  (Year 2 volume, whose opening chart was the permit price); learning by doing, solar module costs (Year 1 volume);
  discounting and CBA (ch. 20); the physical science of climate change (the Earth and space sciences books, named in
  prose: no climate science re-taught).
- **Opening chart** (USGS DS 140 dropped for good by the user, 2026-11-20): [L] a cited-number chart via
  `figdata/lib/cited.py` --- real prices of the five metals of the Simon--Ehrlich wager, 1980 and 1990, from printed
  tables or text only; or, if that table is too thin, the EKC chart (SO2 paths, [A] CEDS + Maddison) as the opening chart
  and the wager in a `record` box. EIA quantities and JST are other options.
- **Other charts**: (2) sulphur dioxide per person against income per person, country paths 1850--2019 for six
  economies [A] `ceds("so2")` / `maddison` pop and gdppc (the hump); (3) carbon dioxide per person against income per
  person, 2019 cross-section [A] `ceds("co2")` or `EN.GHG.CO2.PC.CE.AR5`; (4) the SCC as a function of the discount rate
  (computed from a stylised damage path) [S, analytic]; (5) PM2.5 exposure against income [A] `EN.ATM.PM25.MC.M3`
  --- choose 3--4.
- **Diagrams**: marginal abatement costs of two firms and the equal-MAC allocation; the Hotelling price path with a
  backstop; damage and abatement (MAC = MD) diagram.
- **Photos**: an open-pit copper mine (e.g., Bingham Canyon or Chuquicamata, Commons, licence to verify); a solar farm
  --- one or two.
- **Boxes**: `record[The U.S. sulphur dioxide market, 1995--2010]` (Schmalensee--Stavins 2013: cost savings vs
  command and control, ledger); `record[The Simon--Ehrlich wager, 1980--1990]`; `record[Discount rates in published
  climate assessments]` (Stern 2007 1.4 %; Nordhaus DICE ~4 %; U.S. EPA 2023 SCC \$190 at 2 %, ledger --- the
  positive point: the SCC's range is mostly a choice of $\rho$ and $\eta$, with the inputs stated); `dated{2026}` EU ETS
  price and carbon-tax rates in two countries (ledger); `measure[How damages are valued]` (hedonic, health dose-
  response, recall ch. 20).
- **Exercises**: ★ 1 [R] read the opening chart; 2 [C] equal-MAC allocation of a 100-tonne cut between two firms; 3 [C]
  Hotelling price in 10 years at $r$ = 3 %; 4 [X] what price data contradict the Hotelling rule. ★★ 5 [C] SCC with a
  constant damage stream at 1.4 %, 3 %, 5 %; 6 [C] Ramsey formula: $r$ for $\rho$ = 0.1 %, $\eta$ = 1, $g$ = 1.3 % vs
  $\rho$ = 1.5 %, $\eta$ = 2; 7 (py) [R] CEDS SO2 hump: income at the peak for three countries; 8 [P] tax vs permit
  under cost uncertainty (Weitzman, given slopes); 9 [X] what data would show the EKC is regulation not income. ★★★
  10 [C] prove the Hotelling rule by arbitrage; 11 [C] learning rate from two cost--cumulative-output points (Year 1
  volume's solar data recalled); 12 (py) [C] an SCC calculation with a damage path and three discount schedules.
- **Weekend problem --- "Brenland's coal and its smoke"**: invented coal stock, extraction cost, SO2 damages, two power
  firms. Part I the Hotelling path of Brenland's coal and the backstop date; Part II local pollution: damages valued
  with a dose--response and a VSL (ch. 20); Part III tax vs permits between the two firms; Part IV the social cost of
  carbon for Brenland's emissions at two discount rates. Named result: *the efficient SO2 tax and the year Brenland's
  coal is exhausted*. 26 questions.
- **Ledger**: Krautkraemer 1998 (JEL); Livernois 2009; Grossman--Krueger 1995; Stern 2004 (World Dev.); Schmalensee--
  Stavins 2013 (JEP); Simon--Ehrlich wager prices (ledger, primary source to find: Tierney 1990 NYT is secondary ---
  USGS dropped: printed tables only); Stern 2007; Nordhaus 2017 (PNAS, SCC); U.S. EPA 2023 SCC report (AGENCY);
  EU ETS price (AGENCY, dated 2026); Weitzman 1974 (recall); Way et al. 2022 (Joule, learning rates) or Lafond et al.
  2018.

## 36 `income-and-wellbeing-evidence` --- Income, Wellbeing and What Economics Measures

- **Sections**: 1 Life satisfaction and income: between countries, inside countries, over time; 2 Does the relation
  flatten? (debate); 3 Welfare measures beyond GDP: consumption, leisure, mortality, inequality in one number;
  4 A return to the twenty charts of the first volume: what the models of the series explained, and what stays open.
- **Defines**: life satisfaction (the survey measure, Cantril ladder); Easterlin paradox; hedonic adaptation (as a
  measured pattern; may not need a definition); consumption-equivalent welfare (Jones--Klenow); equivalent income.
  Wellbeing first look: **recalled** (grades 10--12 volume).
- **Propositions**: the Jones--Klenow decomposition of log welfare into life expectancy, consumption, leisure and
  inequality terms (derivation with log utility and lognormal consumption); a log-linear satisfaction--income relation
  implies equal satisfaction gains from equal percentage raises (proof), so "flattening" in levels is not flattening
  in logs.
- **Model box**: none new (measurement chapter); the closing section has a table of the series' models (one line
  each: the model, its chapter, its record), with the four-point frame summarised --- not a model box.
- **Recalls**: income and wellbeing first look (grades 10--12 volume); GDP and what it leaves out (grades 6--9 and
  10--12 volumes, Year 1 volume); the twenty-one opening charts (grades 6--9 volume, named in prose, none reprinted);
  ch. 6's evidence scale.
- **Opening chart**: *life satisfaction against income over time inside countries* --- [?] needs a life-satisfaction
  dataset (World Happiness Report / Gallup World Poll averages, licence unclear; or the World Values Survey,
  registration) --- none approved, and Book 2's g12 `income-and-wellbeing` has the same need (series-wide). **Fallback**
  [L]: published within-country slopes and their intervals (Stevenson--Wolfers 2008, Brookings Papers, tables; Sacks--
  Stevenson--Wolfers 2012) with the between-country slope for comparison; second fallback: the Jones--Klenow-style
  welfare chart below becomes the opening chart.
- **Other charts**: (2) consumption-equivalent welfare against income per person, computed from approved data [A] ---
  consumption share `pwt(cols=["csh_c"])`, life expectancy `SP.DYN.LE00.IN`, hours `avh`, inequality `SI.POV.GINI`
  (lognormal assumption), ~100 countries, 2019, with the Jones--Klenow (2016) published values for a few countries in a
  `measure` box for comparison [L]; (3) emotional wellbeing and income: Kahneman--Deaton 2010 vs Killingsworth 2021 vs
  the 2023 joint paper [L] (a few published points) --- or a debate-box table without a chart.
- **Diagrams**: none required; possibly the Jones--Klenow decomposition as a bar diagram drawn from the computed table
  (that is a chart, from figdata).
- **Boxes**: `debate[Does wellbeing stop rising with income?]` --- Easterlin 1974 / Easterlin et al. 2010 (PNAS: no
  long-run relation within countries; grade 3); Stevenson--Wolfers 2008 (positive within and between, log-linear;
  grade 3); Kahneman--Deaton 2010 (PNAS: emotional wellbeing plateaus near \$75,000); Killingsworth 2021 (PNAS: no
  plateau, experience sampling); Killingsworth--Kahneman--Mellers 2023 (PNAS adversarial collaboration: plateau only for
  the least happy fifth). Weaknesses: scale-use, survey changes, short within-country series. `measure[How life
  satisfaction is asked]`; `measure[Welfare in one number]` (Jones--Klenow).
- **The closing section**: a table "what the series' models explained" (one row per data-strand theme: the first
  chart, the model, the test, the record) and "what stays open" (each debate box of the series named by chapter, its
  current grade). Prose only; no chart reprinted; no prescriptive conclusion.
- **Exercises**: ★ 1 [R] read the opening chart; 2 [C] a 10 % income rise in a log-linear model: satisfaction change;
  3 [C] Jones--Klenow: welfare from a life-expectancy gap (formula given); 4 [X] what data would contradict
  adaptation. ★★ 5 (py) [C] welfare vs income ranks: which countries move most; 6 [C] equivalent income for two
  countries with different leisure; 7 [P] a fall in inequality with fixed mean: welfare change (lognormal);
  8 [C] between-country slope from given means; 9 [X] what would show scale-use differences drive a gap. ★★★ 10 [C]
  derive the Jones--Klenow decomposition; 11 (py) [C] sensitivity of the welfare ranking to the VSL-like value of a
  year of life; 12 [P] the closing synthesis: pick two data-strand themes and say which model explains each and what
  observation would refute it.
- **Weekend problem --- "Fifty years of Brenland, in one number"**: `accounts.csv` and `households.csv` [B] plus an
  invented life-expectancy and hours path. Part I GDP per person growth; Part II consumption-equivalent welfare with
  leisure and mortality; Part III inequality from the household survey; Part IV Brenland against Kestria in welfare
  terms. Named result: *Brenland's consumption-equivalent welfare growth 1975--2025, against its GDP growth*. 24
  questions.
- **Ledger**: Easterlin 1974; Easterlin et al. 2010; Stevenson--Wolfers 2008; Sacks et al. 2012; Kahneman--Deaton 2010;
  Killingsworth 2021; Killingsworth et al. 2023; Jones--Klenow 2016 (AER); Deaton 2008 (JEP); Cantril 1965 (the ladder,
  as label).

---

# Appendix A --- Programme check (2026-11-20)

Sources read (public pages only, as data; provenance, never printed): third-year *licence* course lists of four
universities --- Paris 1 Panthéon-Sorbonne (licence sheet 2021--22, S5--S6), Université Gustave Eiffel (L3 Économie
sheet 2024), Université Paris-Dauphine (L3 Économie internationale et développement, 2026--27), Université Toulouse 1
Capitole (L3 Économie, CFVU deliberation 2021--22, annex of courses); and the tables of contents of four field
textbooks on the publishers' or authors' pages: Angrist--Pischke *Mastering 'Metrics* (Princeton UP), Krugman--
Obstfeld--Melitz *International Economics* 12th ed. (Pearson; via search snippets), Gruber *Public Finance and Public
Policy* 8th ed. (Macmillan), Borjas *Labor Economics* 9th ed. (McGraw-Hill; via search snippets). Fetches: 12 pages
(3 PDFs read with `pdftotext`), 5 searches.

| Programme item (where seen) | Book 5 chapter(s) | Status |
|---|---|---|
| Econometrics: linear model, applications (Eiffel S5--S6, Paris 1 S6, Toulouse S6, Dauphine S6) | 01--06 | covered (linear model itself: Book 4) |
| Time-series econometrics (Eiffel "Econométrie 2: séries temporelles") | Book 4 ch. 34; here 15 §6 (local projections, told) | **thin**: no VAR / cointegration chapter; proposed: section in ch. 15 only |
| Commerce international / économie internationale (all four) | 07--11 | covered |
| Macroéconomie monétaire internationale (Paris 1 S5) | 12--14 | covered |
| Croissance (Paris 1 S5, Eiffel S5, Dauphine option) | 31 (+ Book 4 Ramsey, endogenous growth) | covered |
| Économie publique (all four) | 17--22 | covered |
| Économie du travail (Eiffel, Montpellier, Paris 1 L2) ; Borjas ch. 2--12 | 23--26 | covered; incentive pay = Book 4 `moral-hazard`; unemployment = Books 3--4 |
| Économie industrielle (Eiffel S6, Toulouse S6) ; organisations et marchés (Paris 1 S6) | 27--30 | covered; theory of the firm/organisations: Book 4 (incomplete contracts told) |
| Économie du développement (Paris 1, Eiffel, Dauphine) | 33--34 | covered |
| Économie de l'environnement / du climat / développement durable (Paris 1, Toulouse) | 35 | covered (no degrowth, user ruling) |
| Économie expérimentale (Paris 1 option) | Book 4 `behavioural-evidence`; 06 (replication of experiments); 28 (lab auctions) | covered across books |
| Économie du droit et des institutions (Paris 1 option); économie du crime / corruption (Dauphine option) | 32 | **gap**: proposed §6 of ch. 32 on crime, deterrence and corruption (two natural experiments), to confirm |
| Taxes on saving and capital (Gruber ch. 22--24) | 17 §4 (told) | thin, by design |
| State and local government, education finance (Gruber ch. 10--11) | 21 (Tiebout), 24 (school resources) | covered |
| Health insurance, Social Security, UI, DI (Gruber ch. 12--16) | 19 | covered in one chapter (dense: expect ~15 pp) |
| Firms in the global economy: offshoring, multinationals (KOM ch. 8) | 09 §7 (told) | thin, by design; FDI data shown in ch. 12 |
| Financial globalisation; developing-country crises (KOM part 4) | 12, 14 | covered |
| Finance de marché, banque et marchés, mécanismes financiers (options) | --- | out of scope: the quant series owns finance (outline) |
| Théorie des jeux (Eiffel S6); micro under uncertainty and information (Paris 1 S5) | Book 4 | covered elsewhere |
| History of thought (Paris 1 S5), history of macroeconomics, comparative development history 1800--2020 (Dauphine) | --- | dropped (user ruling); dated episodes only as `record` boxes |
| Sociology of stratification (Paris 1 option) | --- | dropped (pure economics) |

No chapter of the list is uncovered by the programmes. Proposed changes to the chapter list: **none**. Proposed
content changes: ch. 15 §6 (how a monetary shock's effect is measured); ch. 32 §6 (crime, deterrence, corruption).

# Appendix B --- Data status of the opening charts

| Ch. | Opening chart | Status | Change from the outline |
|---:|---|---|---|
| 1 | trade share vs geography-predicted share (first stage) | A (gravity 2019, WDI) | **yes** (QOB → worked example [L]) unless the sync keeps QOB [L] |
| 2 | CO2 per person vs income: between vs within | A (WDI) | variable chosen |
| 3 | NJ/PA fast-food employment 1992 | L (Card--Krueger Table 3) / ? / fallback A (NSW) | no |
| 4 | outcome vs score with a jump | S (calibrated on Lee 2008) | no (simulated, said so) |
| 5 | earnings in 1978 (yes/no) vs age, three fits | A (NSW CPS controls) | "participation" → "having earnings" |
| 6 | original vs replication effect sizes (18 experiments) | L (Camerer 2016) | **yes** (z-heap not usable); contested with Book 4 ch. 5 |
| 7 | Japan 1859: price changes vs net exports | L (Bernhofen--Brown 2004) | no |
| 8 | country shares of world capital, workers, output | A (PWT) | **yes** (Trefler's table too large) |
| 9 | share of firms exporting by industry | L (Bernard et al. 2007 Table 2) | no |
| 10 | pair trade vs GDP product / distance | A (gravity 2019) | no |
| 11 | applied tariffs 1988--2022, six economies | A (WDI) | **yes** (pass-through → chart 2 [L]) |
| 12 | current accounts by region / world output 1980--2024 | A (WDI) | no |
| 13 | price levels vs income per person | A (WDI) | no |
| 14 | share of 17 economies pegged, 1870--2020 | A (JST) | scope: 17 economies |
| 15 | central-bank balance sheets / output 2005--2025 | ? (Fed H.4.1, ECB) / fallback L (24 rows) | no |
| 16 | price level over three centuries | ? (BoE Millennium) / fallback A (JST five economies 1870--2020) | scope if no approval |
| 17 | revenue / output 1870--2020 (JST) + by type 1972--2024 (WDI) | A | **yes** (by type over a century not available) |
| 18 | marginal effective tax rate vs earnings | L (U.S. 2024 statutory parameters) / B | no |
| 19 | extra weeks unemployed per week of entitlement, by study | L (~7 studies) / fallback A (dependency ratio) | form changed (estimates, not durations) |
| 20 | forecast vs final cost, large projects | L (~8--10 audit rows + Flyvbjerg 2002) | no |
| 21 | spending / output around suffrage extensions | A (JST) + L (17 dates) | no |
| 22 | share of workers licensed, 1950s--2023 | L (~6 rows, with a measurement break) | no |
| 23 | women's participation 1990--2025, six economies | A (WDI/ILO) | **yes** (three decades, not a century; U.S. century in a record box [L]) |
| 24 | returns to schooling by method | L (~10 studies) | no |
| 25 | college premium and relative supply | L (Goldin--Katz 2008, 1915--2005) | span widened |
| 26 | employment elasticities by year of publication | L (~15 studies) | no |
| 27 | price effects of completed mergers | L (~8 rows) | no |
| 28 | 3G auction revenue per person, 2000--01 | L (Klemperer 2002) | no |
| 29 | share of productivity growth from entry/exit | L (6--8 rows) | no |
| 30 | real air fares before/after 1978 | A if BLS airline-fare CPI derived / else L | no |
| 31 | decadal growth rates by country | A (PWT/Maddison) | no |
| 32 | China 1950--2022; Western vs Eastern Europe | A (Maddison) | **yes** (no separate East/West Germany series; Koreas from 1990) |
| 33 | income and population, England, 1252--1850 | ? (BoE Millennium for real wages) / fallback A (Maddison) | variable if no approval |
| 34 | microcredit effects in seven RCTs | L (Meager 2019) | no |
| 35 | five metals of the Simon--Ehrlich wager (cited) or EKC paths | L / A (USGS dropped 2026-11-20) | |
| 36 | life satisfaction vs income inside countries | ? (no approved wellbeing data; series-wide) / fallback L (Stevenson--Wolfers) | scope if no approval |

Totals: [A] 13 opening charts, [A]+[L] 1 (ch. 21), [A] if a BLS series is derived 1 (ch. 30), [L] 15, [S] 1,
[?]-first 5 (each with a fallback: [A] for ch. 16 and 33, [L] for ch. 15, 35, 36). Across all charts of the book
(about 110), roughly 60 % [A], 25 % [L], 15 % [S].

# Appendix C --- What Book 5 expects Books 3 and 4 to define (for the sync)

Book 5 recalls these in prose ("defined in the Year 1 volume", "the Year 2 volume") and does not define them. If a
writer of Book 3 or 4 does not plan to define one, the sync must place it.

**From Book 3 (Year 1)**: equilibrium, comparative statics, envelope theorem (used in ch. 28's proof); elasticity as a
log-derivative; Lagrange multiplier as a **shadow price** (so ch. 20 says *accounting price*); compensated demand,
Slutsky, CV/EV, consumer surplus (ch. 17); labour supply, kinks, **implicit marginal tax rate** (ch. 18 recalls);
production function, elasticity of substitution (ch. 23, 25); economies of scale, learning by doing (ch. 9, 35);
capitalisation (ch. 21); **deadweight loss in elasticity form, the incidence formula** (ch. 17 re-founds as excess
burden); Lerner index, price discrimination, two-part tariff, **average-cost and price-cap rules for a natural
monopoly** (ch. 30 recalls); derived demand, marginal revenue product, the **single-buyer (monopsony) model** and a
wage floor (ch. 26); Cournot, Bertrand, Stackelberg, possibly **HHI** (ch. 30 defines it if Book 3 does not); national
accounts, chain-linking, PPP construction (ch. 13 `measure`); Solow model, speed of convergence, golden rule, Solow
residual, misallocation (ch. 31); job-finding and separation rates, efficiency wages, **Beveridge curve**;
quantity theory, velocity, **inflation tax** (and **seigniorage**?), Fisher effect (ch. 16); IS--LM, liquidity trap;
expectations-augmented Phillips curve, **sacrifice ratio** (ch. 16); automatic stabilisers, multiplier measurement;
**real exchange rate**, Mundell--Fleming, **trilemma** (ch. 14 tests, does not define); cross-section, time series,
**panel** (as data shapes; ch. 2 defines the estimators), seasonal adjustment; skewness, conditional mean, Simpson's
paradox; LLN, CLT as admitted tools; estimator, bias, consistency, standard error, confidence interval, $p$-value,
**power**, multiple testing (ch. 6 uses); least-squares line, $R^2$, regression to the mean (ch. 31 uses).

**From Book 4 (Year 2)**: lottery, expected utility, risk aversion, certainty equivalent (ch. 19, 20, 28); full
insurance, risk sharing (ch. 19); Euler equation, discounting, present bias (ch. 12, 35); asset-pricing basics, no
arbitrage (ch. 13 CIP uses arbitrage only); Edgeworth box, Pareto efficiency, welfare theorems, Walras' law (ch. 7, 8);
prices as information (ch. 32); Pareto criterion, **compensation tests** (ch. 20), social welfare function (ch. 18),
**Arrow's theorem, single-peaked preferences, median voter theorem** (ch. 21 recalls and tests); normal form,
dominance, Nash equilibrium, public-good contribution game (ch. 22), mixed strategies, subgame perfection, credible
threats, **repeated games, trigger strategies, folk theorem, collusion condition** (ch. 27), Bayesian Nash equilibrium,
**first- and second-price auctions, revenue equivalence (stated), winner's curse** (ch. 28 proves revenue equivalence
--- which book holds the definition pair is for the sync); lemons, adverse selection (ch. 19), signalling, screening,
**sheepskin effects** (ch. 24), moral hazard, principal--agent, piece rates (ch. 19, 23); corrective (Pigouvian) tax,
**Coase theorem, prices vs quantities (Weitzman), emission permits**, Samuelson condition (ch. 35); consumption
function, permanent income, liquidity constraints; Tobin's $q$; government budget constraint, debt dynamics,
**Ricardian equivalence** (ch. 16); OLG, **pay-as-you-go and funded pensions, return $n+g$, old-age dependency ratio**
(ch. 19, 33 --- the dependency ratio is contested); Ramsey model, modified golden rule; ideas, research sector, scale
effect, **creative destruction / growth through replacement** (ch. 29); adaptive and rational expectations, **Lucas
critique, time inconsistency, central-bank independence, inflation targeting** (ch. 15 recalls, defines only the
implementation terms); matching function, **search model of unemployment** (ch. 26); three-equation model, **Taylor
rule and Taylor principle**, zero lower bound (ch. 15); business cycles, shock identification (told); **bank run,
deposit insurance, lender of last resort, leverage** (ch. 15); multiple regression in matrix form, Frisch--Waugh--Lovell,
**omitted-variable bias formula**, Gauss--Markov, robust errors, **clustered standard errors** (ch. 2--3 use), bootstrap;
logs and elasticities, dummies, interactions, **measurement error and attenuation** (ch. 1, 24), bad controls;
**potential outcomes, ATE, ATT, selection bias, randomisation, natural experiment, external validity** (ch. 1--4, 34);
stationarity, AR/MA, unit roots, spurious regression, **Granger causality**, forecasting scores (ch. 13).

**From the school volumes** (Books 1--2; Book 5 re-founds only where the outline's table says so): comparative
advantage and the terms of trade (ch. 7 re-founds; terms of trade to confirm), tariff (ch. 11 recalls), rent seeking and
capture (ch. 22 re-founds), human capital (ch. 24 re-founds), balance of payments / current account (ch. 12 re-founds),
PPP conversion (ch. 13 re-founds), institutions and planned economies (ch. 32 re-founds), minimum wage (ch. 26),
poverty line (ch. 34 recalls), life expectancy, births per woman (ch. 33: total fertility rate contested), Lorenz curve
and Gini (ch. 18, 25 recall), wellbeing first look (ch. 36 recalls), present value (ch. 20 recalls).

**From other series**: the mathematics books (LLN, CLT, matrices, optimisation under constraint proved, order
statistics only as expectations); the Earth and space sciences books (climate science, natural resources as geology:
ch. 35 recalls in prose); the artificial-intelligence books (logistic regression as a classifier, maximum likelihood in
an ML setting, ad auctions: ch. 5 and 28 name them in prose and take the econometric/economic angle --- **to confirm**
that Book 5 may define *logit model*, *maximum likelihood estimator*, *reserve price* for this series).
