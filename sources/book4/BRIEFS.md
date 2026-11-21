# Book 4 (University Year 2, `bachelor-2`, prefix `b2`) — chapter briefs

Phase A, 2026-11-20. Written by the Book 4 writer. Binding inputs: `sources/BATCH_BOOKS_1-5.md`, `OUTLINE.md` (Book 4),
`sources/SERIES_DEFINITIONS.md`, `sources/data_ledger.md`. Target ~460 pp, 34 chapters at ~13.5 pp each.

## Conventions used in these briefs

- **Data routes.** Every chart below is tagged with how its numbers reach the page:
  - **[A]** an approved dataset through `econdata` (loader, series, years). Checked on 2026-11-20 (coverage noted).
  - **[S]** a dataset bundled inside `statsmodels` 0.15.0 and marked public domain in its own `COPYRIGHT` string:
    `macrodata` (US quarterly 1959Q1–2009Q3), `grunfeld` (11 US firms 1935–54), `randhie` (RAND Health Insurance
    Experiment, 20,190 person-years), `engel` (235 Belgian households, 1857). `sources/DATA_SOURCES_TO_APPROVE.md`
    calls bundled tables "no download"; **the sync must rule** that figdata scripts and listings may load them (no
    `econdata` loader exists) and that the Data Credits page lists them.
  - **[L]** a small table of numbers printed in a published paper or an agency's table, each number a ledger row in
    `sources/ledger/book4.md`, read into the figdata script from the ledger (never typed into the chart). **The sync
    must rule on this route** (see the Phase A report: a helper that reads ledger rows by id). Every [L] chart has a
    fallback if the route is refused.
  - **[I]** invented: Brenland/Kestria (`country`) or the chapter's seeded simulation, labelled as such.
- **Exercises.** 12 per chapter, 4★ then 5★★ then 3★★★. Kinds: **R** read a chart or table, **C** compute, **P** use a
  model to predict a direction and a size, **F** say what observation would falsify. Every chapter has at least two of
  each kind. A data exercise (marked **D**) has a tested Python solution in `code/bachelor-2/NN-<slug>/exercises/`.
- **Weekend problem.** 22–28 questions, Parts I–IV, story-driven, ending on a named quantified result.
- **Mathematics (level guard).** The Year 2 mathematics book: matrices (Y1), constrained optimisation with Lagrange
  proved (Y2 `differential-calculus`), eigenvalues (Y2 `reduction`), quadratic forms (Y2), discrete random variables
  (Y2), differential equations (Y1). Kuhn–Tucker, fixed-point theorems, the central limit theorem and the
  calculus of variations are used as `\admitted`.
- **Recalls.** "Y1" is the Year 1 volume (Book 3, prose pointer only), "school" the grades 10–12 volume.
- Labels: `def:b2:<slug>:<name>`; the full term list is in `DEFINITIONS.md`.

---

# Part I — Uncertainty and Time

## 1. Expected Utility (`expected-utility`)

Programme items: lotteries; vNM axioms and representation; risk aversion; CE and risk premium; Arrow–Pratt; CARA/CRRA;
lab and insurance tests; Allais; small stakes (Nanterre S3 "choix rationnel et incertitude"; Varian ch. 12; Lille S6).

- **Sections.** 1.1 Lotteries (simple, compound, reduction; the probability triangle). 1.2 The expected-utility theorem
  (completeness, transitivity, continuity, independence; representation proved for finitely many prizes; uniqueness up
  to a positive affine map, proved). 1.3 Attitudes to risk (concavity and Jensen recalled; certainty equivalent; risk
  premium; first-order stochastic dominance). 1.4 Measuring risk aversion (Arrow–Pratt absolute and relative; CARA,
  CRRA; small-risk approximation $\pi \approx \tfrac12 A(w)\sigma^2$, derived). 1.5 Where the model is tested and breaks.
- **Defines.** lottery, compound lottery, independence axiom, expected-utility representation, risk aversion
  (re-founded), certainty equivalent (re-founded), risk premium (re-founded), first-order stochastic dominance,
  coefficient of absolute risk aversion, coefficient of relative risk aversion, constant absolute risk aversion,
  constant relative risk aversion.
- **Model: Expected utility.** *Assumes* complete, transitive, continuous preferences over lotteries obeying independence.
  *Predicts* indifference lines straight and parallel in the triangle; the same choice in both Allais pairs; full cover at
  a fair price. *Tested* laboratory choice tasks; deductible choices in home and car insurance. *Breaks* the Allais pairs
  (common-consequence effect); risk aversion over small stakes too large to square with any concave utility of wealth.
- **Recalls.** School: expected utility first look, risk aversion (grades 10–12, `risk-and-insurance`). Mathematics:
  expectation, concavity (Jensen).
- **Opening chart [L].** The two Allais pairs: share of subjects choosing each option (Kahneman–Tversky 1979, Problems 1–2,
  N = 72). Bar chart, 4 ledger rows. *Fallback:* the probability triangle with the two pairs drawn (TikZ), the shares in
  prose with their ledger rows.
- **Other charts.** [I] CRRA utility curves for $\rho = 0.5, 1, 2, 5$ (a function plot: `omfigure`, not `omchart`).
  [L] implied relative risk aversion from deductible choices (Sydnor 2010, a few quantiles) if the table is usable.
- **Diagrams (3).** Concave utility with chord, CE and risk premium marked (geometry from Example 1.x numbers);
  probability triangle with parallel indifference lines and the Allais pairs; CARA against CRRA risk premium as wealth
  rises.
- **Boxes.** `record[The Allais pairs]` (KT 1979; Allais 1953 cited as the source of the pairs). `measure[Reading risk
  aversion off insurance deductibles]` (Sydnor 2010 AEJ:Applied; Cohen–Einav 2007 AER). `remark` on Rabin's
  calibration result (Rabin 2000, Econometrica), named as "the calibration result".
- **Exercises.** ★ C EU and CE of a lottery with $\ln$; R the Allais shares; C risk premium of a 50–50 bet; F which choice
  pair would violate independence. ★★ C CARA–normal premium; P effect of wealth on CE under CRRA (direction, size);
  C dominance check; R deductible table; F contradiction of CARA by wealth data. ★★★ proof that CRRA → $\ln$ as $\rho\to1$;
  proof of the affine-uniqueness converse; the small-stakes calibration in a two-bet case.
- **Weekend problem — A Brenland grain farmer's harvest.** I Lotteries (yields, prices in dalens); II EU and CE under CRRA;
  III an insurer's offer with a loading: accept or not; IV a survey of farmers with Allais-type pairs. *Named result:* the
  farmer's risk premium and the largest loading she accepts, in dalens. ~24 questions.
- **Ledger.** b2:kt1979-p1a/p1b/p2c/p2d (shares); b2:rabin2000; b2:sydnor2010-rra; b2:cohen-einav2007. ~8 rows.

## 2. Insurance and Risk Sharing (`insurance-and-risk-sharing`)

Programme items: insurance demand; state-contingent goods; efficient risk sharing; first portfolio choice; full-risk-sharing
test (Varian ch. 12–13; Nanterre S3).

- **Sections.** 2.1 The demand for insurance (full cover at a fair premium, proved; partial cover with a loading, proved;
  deductibles). 2.2 State-contingent goods (Arrow securities; contingent budget line; MRS with probabilities; the
  certainty line). 2.3 Efficient risk sharing (two agents, no aggregate risk → full insurance; with aggregate risk →
  consumption moves with the aggregate only, proved; pooling and the law of large numbers recalled). 2.4 A first
  portfolio choice (one safe, one risky asset; small-risk share $\approx$ premium/($A\sigma^2$); CARA-normal exact).
  2.5 Testing full risk sharing (the consumption-insurance regression; village and cross-country evidence). 2.6 Answers
  outside markets: mutual societies, family transfers, crop insurance with index triggers, public programmes — each
  with its evidence and its limits.
- **Defines.** state of the world, contingent commodity, Arrow security, actuarially fair premium, loading, deductible,
  idiosyncratic risk, aggregate risk, efficient risk sharing, portfolio share.
- **Models.** Demand for insurance (*tested* deductible and cover choices; *breaks* when the buyer's risk is private — ch. 15
  — or when the insurer's cost of claims is not fixed — ch. 17). Full risk sharing (*predicts* zero coefficient on own
  income given aggregate consumption; *tested* village surveys; *breaks* small but significant coefficients everywhere).
- **Recalls.** Ch. 1; school `risk-and-insurance` (pooling); mathematics: law of large numbers.
- **Opening chart [A] (deviates from outline).** Volatility of household consumption growth against volatility of GDP growth,
  per country, 1991–2023: `wdi('NE.CON.PRVT.PC.KD.ZG')` and `wdi('NY.GDP.PCAP.KD.ZG')`, `countries_only=True`, countries with
  ≥ 25 years; 45° line. *Why:* the outline's village survey (Townsend 1994) is not an approved dataset; the village test
  enters as a `record` box with ledger numbers.
- **Other charts.** [A] the correlation of a country's consumption growth with world consumption growth against the
  correlation of its output growth with world output growth (WDI, 1991–2023) — the cross-country risk-sharing test.
- **Diagrams (3).** Contingent-consumption diagram (certainty line, fair-odds line, tangency on the certainty line); risk
  sharing in an Edgeworth box (no aggregate risk → diagonal); portfolio share against risk aversion.
- **Boxes.** `record[Village risk sharing]` (Townsend 1994, Econometrica: coefficient on own income; Mace 1991 JPE).
  `measure[The consumption-insurance regression]`. `record[Index insurance for farmers]` (Karlan, Osei, Osei-Akoto,
  Udry 2014 QJE: take-up and investment).
- **Exercises.** ★ C fair premium; R the scatter (two countries named); C contingent budget line; F what would refute full
  sharing. ★★ C partial cover with loading; P effect of a larger loading on cover; C Borch-type allocation; D ratio of
  volatilities for six countries (WDI, Python); F cross-country correlations. ★★★ proof that consumption depends only
  on aggregate endowment; CARA-normal portfolio derivation; welfare gain of pooling $n$ risks.
- **Weekend problem — The Kestrian fishing cooperative.** Two boats with correlated catches. I contingent goods; II the
  efficient sharing rule; III an outside insurer with a loading; IV the cooperative's survey (seeded) and the regression
  test. *Named result:* the share of idiosyncratic risk the cooperative insures, and its welfare gain as a certainty
  equivalent in kests. ~25 questions.
- **Ledger.** b2:townsend1994-coef; b2:mace1991; b2:karlan2014-takeup; ~6 rows.

## 3. Intertemporal Choice (`intertemporal-choice`)

Programme items: discounting; Euler equation; smoothing; the interest rate; borrowing limits; time consistency; present
bias (Varian ch. 10; Nanterre S3 "arbitrage consommation–épargne"; Lille S3).

- **Sections.** 3.1 Discounting and time-separable utility (exponential; discount factor; rate of time preference). 3.2 The
  Euler equation ($T$ periods with Lagrange, proved; CRRA: consumption growth $\approx (r-\rho)/\theta$; the elasticity of
  intertemporal substitution). 3.3 Smoothing (an income profile, present value of lifetime resources; flat consumption when
  $\beta(1+r)=1$). 3.4 The interest rate (income and substitution effects of $r$, recalled from Y1's two-period case and
  extended). 3.5 Borrowing limits (kink; the young constrained). 3.6 Time consistency (exponential is consistent, proved;
  quasi-hyperbolic $\beta$–$\delta$ is not; commitment; naive and sophisticated). 3.7 Measured present bias.
- **Defines.** discount factor, rate of time preference, Euler equation, elasticity of intertemporal substitution,
  consumption smoothing, borrowing constraint, time consistency, quasi-hyperbolic discounting, present bias, commitment
  device.
- **Models.** Exponential discounting (*tested* consumption growth and interest rates; *breaks* preference reversals,
  demand for commitment). Quasi-hyperbolic discounting (*tested* effort-allocation experiments, gym contracts;
  *breaks* estimates of $\beta$ vary by domain; little present bias over money).
- **Recalls.** Y1 `labour-supply-and-saving` (two-period budget constraint, the interest rate); school `present-value`.
- **Opening chart [L].** Average income before taxes and average annual spending by age of the reference person, 7 age
  groups, from the BLS Consumer Expenditure Survey's published table (one year, read on the BLS page; 14 ledger rows).
  *Fallback [I]:* Brenland's household survey (`households.csv`: `age_head`, `disposable`, `consumption`), labelled
  invented.
- **Other charts.** [I] Brenland mean consumption and disposable income by age band (the same picture on the invented
  survey, used by exercises).
- **Diagrams (3).** Many-period budget line with the Euler tangency; borrowing limit kink; preference-reversal timeline for
  $\beta$–$\delta$.
- **Boxes.** `measure[Spending by age in an expenditure survey]` (BLS CE). `record[Paying not to go to the gym]`
  (DellaVigna–Malmendier 2006 AER). `record[Effort today or tomorrow]` (Augenblick, Niederle, Sprenger 2015 QJE).
- **Exercises.** ★ C PV of an income stream; C Euler with $\ln$; R the age table; F what refutes exponential discounting.
  ★★ C CRRA consumption growth; P effect of a rise in $r$ (sign depends on EIS: size for $\theta=2$); C borrowing limit
  binds?; D Brenland: does consumption track income by age (Python); F the commitment demand of an exponential agent.
  ★★★ proof of time consistency of exponential discounting only; sophisticated $\beta$–$\delta$ three-period
  equilibrium; welfare cost of a borrowing limit.
- **Weekend problem — An engineer in Brenmoor plans three periods.** I budget and PV; II Euler and smoothing; III a borrowing
  limit; IV a $\beta$–$\delta$ engineer and a commitment savings account. *Named result:* the certainty-equivalent cost of
  the borrowing limit and the value of commitment, in dalens. ~25 questions.
- **Ledger.** b2:bls-ce-age-* (14); b2:dellavigna2006; b2:augenblick2015-beta; ~18 rows.

## 4. Asset Prices: A First Model (`asset-prices`)

Programme items: no arbitrage; expected discounted payoff; covariance risk premium; mean–variance and tests; efficient
markets (Varian ch. 11, 13; Romer ch. 8.5, 10.4–10.5; Lille S4 money and financial markets).

- **Sections.** 4.1 No arbitrage (law of one price; state prices; no arbitrage ⇔ positive state prices, proved for two
  states). 4.2 A price as an expected discounted payoff (stochastic discount factor from the Euler equation; risk-free
  rate; bond prices and the expectations hypothesis of the term structure, short). 4.3 A risk premium from covariance
  ($E[R]-R_f = -R_f\,\mathrm{cov}(m,R)$; consumption risk; the size puzzle). 4.4 Mean–variance (two-asset frontier, the
  tangency portfolio, CAPM beta derived from the frontier; tests: the flat beta line). 4.5 Efficient markets (forms;
  event studies; return predictability; anomalies and what survived out of sample). The quant series is named in prose
  for depth.
- **Defines.** arbitrage, law of one price, state price, stochastic discount factor, excess return, equity premium,
  mean–variance frontier, beta (of an asset), capital asset pricing model, efficient-markets hypothesis, anomaly
  (asset-pricing).
- **Models.** Consumption-based pricing (*tested* JST premia vs consumption volatility; *breaks* the equity premium puzzle).
  CAPM (*tested* cross-section of returns; *breaks* flat beta line, size/value). Efficient markets (*tested* event studies,
  random-walk tests; *breaks* momentum, excess volatility debate).
- **Recalls.** Ch. 1, ch. 3 (Euler); school `present-value`.
- **Opening chart [A].** Cumulated real total returns on equities, bonds and bills, 1900–2020, USA, GBR, FRA, JPN (log
  axis): `jst(cols=['eq_tr','bond_tr','bill_rate','cpi'])` (coverage checked: eq_tr from 1870–1900 by country).
  Missing years (wars) shown as gaps, said in the source line.
- **Other charts.** [A] mean against standard deviation of annual real returns, 16 countries × 3 assets, 1950–2020 (JST).
  [A] autocorrelation of annual real equity returns by country (bars) — a weak-form test.
- **Diagrams (3).** State-price diagram for two states; two-asset mean–variance frontier with the capital line;
  security market line with a flat empirical line beside it (no data: drawn as an illustration and said so).
- **Boxes.** `measure[How a total-return index is built]`. `record[The equity premium puzzle]` (Mehra–Prescott 1985 JME;
  measured premium from JST figdata). `debate[Are stock prices too volatile?]` (Shiller 1981 AER vs Marsh–Merton 1986
  AER; Campbell–Shiller 1988) — empirical only.
- **Exercises.** ★ C state prices from two securities; C risk-free rate from $\beta$, consumption growth; R the
  cumulative-return chart; F what would refute the weak form. ★★ C CAPM beta; P effect of higher risk aversion on the
  premium (size); D geometric mean real return USA, GBR from JST (Python); C mean–variance weights; F joint-hypothesis
  problem. ★★★ proof of no-arbitrage ⇔ positive state prices (two states); derivation of the equity premium with
  lognormal consumption; size of $\theta$ needed to match the JST premium.
- **Weekend problem — The Brenmoor pension fund.** Seeded invented returns for Brenland equities and bonds. I no arbitrage
  and state prices; II the SDF; III mean–variance choice; IV a test of predictability. *Named result:* the fund's optimal
  equity share and the coefficient of relative risk aversion that justifies a 60/40 portfolio. ~25 questions.
- **Ledger.** b2:mehra-prescott1985; b2:shiller1981; b2:fama-french1992-beta; ~6 rows.

## 5. Behavioural Evidence: Where Rational Choice Breaks (`behavioural-evidence`)

Programme items: reference dependence, loss aversion, present bias, defaults, attention; replication record; prospect
theory; experience and stakes (Varian ch. 30; Lille S6 "économie de l'incertain").

- **Sections.** 5.1 What a replication counts (effect sizes, the large replication projects). 5.2 Reference dependence and
  loss aversion (endowment effect; mixed gambles; estimates of $\lambda$). 5.3 Present bias in the field (recall ch. 3).
  5.4 Defaults (automatic enrolment; the size and persistence). 5.5 Limited attention (tax salience; shrouded prices).
  5.6 Findings that did not hold up (named as findings, with the replications). 5.7 Prospect theory in the model frame.
  5.8 Experienced traders and high stakes. Neutral wording: no "irrational", no "nudge" as a verdict; defaults are set
  by firms and governments alike.
- **Defines.** reference point, loss aversion, endowment effect, prospect theory, value function (prospect theory),
  probability weighting function, default effect, salience (limited attention), replication rate.
- **Model: Prospect theory.** *Assumes* value over gains and losses from a reference point, loss aversion, diminishing
  sensitivity, probability weighting. *Predicts* the Allais pattern, the endowment effect, the fourfold pattern of risk
  attitudes. *Tested* laboratory gambles; deductible choices; field reference effects. *Breaks* the reference point is not
  pinned down; experienced traders show little endowment effect.
- **Recalls.** Ch. 1 (Allais), ch. 3 (present bias).
- **Opening chart [L].** Original against replication effect sizes (correlation coefficient) for the 18 laboratory
  economics experiments of Camerer et al. (2016, Science), with the 45° line (36 ledger rows). *Fallback:* the 11-of-18
  replication count and the mean relative effect size in a `record` box, no chart.
- **Other charts.** [L] participation in a firm's pension plan by tenure, before and after automatic enrolment
  (Madrian–Shea 2001 QJE, a few numbers).
- **Diagrams (2).** Prospect-theory value function (kinked at the reference point); probability weighting curve.
- **Boxes.** `debate[Do taxi drivers stop at a daily income target?]` (Camerer et al. 1997 QJE vs Farber 2005 JPE, 2015
  QJE). `record[Automatic enrolment]` (Madrian–Shea 2001). `record[Taxes not on the price tag]` (Chetty, Looney, Kroft
  2009 AER). `record[Traders and the endowment effect]` (List 2003 QJE).
- **Exercises.** ★ R replication chart; C accept a 50–50 mixed gamble with $\lambda=2$?; C endowment-effect WTA/WTP; F the
  observation that rejects loss aversion. ★★ C prospect value of a lottery; P effect of a default switch on participation
  (size from the record); C salience-adjusted demand; R the List table; F a test that separates loss aversion from
  transaction costs. ★★★ fourfold pattern from the weighting function; proof that EU cannot produce the endowment gap
  with small stakes; a reference-dependent labour-supply model and its prediction for hours.
- **Weekend problem — Brenmoor's pension plan.** I loss aversion from a survey of mixed gambles (invented); II the
  implied $\lambda$; III opt-in versus opt-out (participation and saving); IV prediction for an insurance choice and its
  test. *Named result:* the estimated loss-aversion coefficient and the predicted participation gap between the two
  defaults. ~24 questions.
- **Ledger.** b2:camerer2016-orig-*/rep-* (36), b2:madrian-shea2001-*, b2:chetty2009, b2:list2003, b2:camerer1997,
  b2:farber2015; ~48 rows.

# Part II — General Equilibrium and Welfare

## 6. Exchange Economies (`exchange-economies`)

Programme items: Edgeworth box; Pareto set; competitive equilibrium; Walras' law; existence; uniqueness (Nanterre S3
"équilibre général d'une économie de pur échange"; Lille S4; Varian ch. 31).

- **Sections.** 6.1 The economy (agents, endowments, allocations, feasibility; the Edgeworth box). 6.2 Pareto efficiency
  and the contract curve (tangency; Cobb–Douglas contract curve derived). 6.3 Competitive equilibrium (budget sets, excess
  demand; Walras' law proved; only relative prices matter; numeraire; computing an equilibrium). 6.4 Existence (told:
  continuity, boundary behaviour; fixed point `\admitted`). 6.5 Several equilibria and stability (an example with three;
  tâtonnement told).
- **Defines.** exchange economy, endowment, allocation, feasible allocation, Edgeworth box, Pareto-efficient allocation,
  contract curve, competitive equilibrium (general), excess demand function, Walras' law, numeraire, the core (told,
  defined).
- **Model: Walrasian exchange.** *Assumes* price taking, convex monotone preferences, no externalities, complete markets.
  *Predicts* convergence to market-clearing prices; equilibria on the contract curve. *Tested* laboratory double-auction
  markets. *Breaks* few traders (bargaining), multiple equilibria, unstable adjustment.
- **Recalls.** Y1 partial equilibrium; Y1 consumer choice.
- **Opening chart [L].** Transaction prices round by round in a laboratory market against the competitive prediction
  (candidate: Smith 1962 JPE, the first experiment; or a multi-market experiment with a printed per-period table —
  to be settled at writing; numbers read from the paper's table or figure, flagged "read from figure" in the ledger).
  *Fallback:* the opening becomes a `record` box and the first figure is the Edgeworth box.
- **Other charts.** None from data; [I] excess demand against relative price for the three-equilibrium example (function
  plot, `omfigure`).
- **Diagrams (4).** Edgeworth box with endowment and budget line; tangency and the contract curve; equilibrium
  offer curves; three equilibria.
- **Boxes.** `record[Markets in the laboratory]` (Smith 1962).
- **Exercises.** ★ C feasibility; C MRS and Pareto test; R the lab chart; F what would refute convergence. ★★ C competitive
  equilibrium with Cobb–Douglas; C contract curve; P effect of an endowment transfer on the price (direction, size);
  C Walras' law check; F test of uniqueness. ★★★ proof of Walras' law; three-equilibrium construction; the core shrinks
  as the economy is replicated (two-replica case).
- **Weekend problem — Fish for grain between Brenland and Kestria.** I the box; II Pareto set; III equilibrium price and
  allocation; IV a transfer of endowment and the new equilibrium. *Named result:* the equilibrium price of fish in grain,
  and each country's gain as an equivalent variation in grain. ~24 questions.
- **Ledger.** b2:smith1962-*; ~10 rows.

## 7. The Two Welfare Theorems (`welfare-theorems`)

Programme items: production; first theorem; second theorem and convexity; what carries the result; distribution
(Nanterre S3 "économie de Robinson"; Varian ch. 32; Lille S4).

- **Sections.** 7.1 Production added (firms, profit maximisation at given prices, the one-consumer–one-firm economy).
  7.2 The first welfare theorem (local non-satiation; proved). 7.3 The second welfare theorem (stated with convexity; the
  separating-hyperplane step `\admitted`; lump-sum transfers). 7.4 Which assumption carries the result (complete markets,
  price taking, no external effects, convexity — each failure named with its chapter). 7.5 The theorems are silent on
  distribution (Pareto set; transfers that are not lump-sum in practice — pointer to Y3).
- **Defines.** production economy (private-ownership economy), local non-satiation, first fundamental theorem of welfare
  economics, second fundamental theorem of welfare economics, lump-sum transfer, complete markets.
- **Model: The competitive economy with production.** *Assumes* the ch. 6 list plus convex technologies. *Predicts* efficient
  allocations; price gaps between connected markets equal transport costs. *Tested* market integration after transport
  improvements. *Breaks* external effects, market power, missing markets, non-convexities.
- **Recalls.** Ch. 6; Y1 firm and PPF; school `surplus-and-efficiency`.
- **Opening chart [L].** Grain price gap between two markets before and after a rail link (candidates: Liverpool–Chicago
  wheat gap 1870–1913, O'Rourke–Williamson 1999 book table, or Jacks 2005 EEH). *Fallback:* a record box; the chart is
  dropped.
- **Other charts.** none.
- **Diagrams (3).** Robinson Crusoe economy (PPF, price line, indifference curve); the proof of the first theorem as a
  picture; a non-convex case where the second theorem fails.
- **Photograph (optional).** A 19th-century grain railway or elevator (Commons, public domain).
- **Boxes.** `record[Railways and the law of one price]`.
- **Exercises.** ★ C Crusoe equilibrium; R price gap chart; C profit at prices; F refuting price-gap prediction.
  ★★ C equilibrium with production (Cobb–Douglas); P effect of a technology gain on wage and output; C which assumption
  fails in four cases; C transfers that reach a target allocation; F missing-market test. ★★★ proof of FWT with production;
  counterexample without local non-satiation; second-theorem transfer computation.
- **Weekend problem — Brenland's railway.** I two towns, transport cost; II equilibrium with production; III the rail link
  and price convergence; IV a transfer to reach a target allocation. *Named result:* the equilibrium after the link and
  the lump-sum transfer that delivers a chosen Pareto allocation. ~24 questions.
- **Ledger.** b2:orourke-williamson-wheatgap-*; ~6 rows.

## 8. Prices as Information (`prices-as-information`)

Programme items: the planner's information; prices as a short message; learning from prices; prediction markets; the
Grossman–Stiglitz limit; planned economies' prices as data (outline; the user's "what prices do" line).

- **Sections.** 8.1 What a planner would need to know (counting the information: preferences, technologies; a
  linear-economy example). 8.2 Prices as a short message (the market needs each agent's own information plus prices;
  message-size result told). 8.3 Equilibrium when traders learn from prices (a fully revealing equilibrium in a two-signal
  model). 8.4 The limit: costly information (Grossman–Stiglitz: no fully revealing equilibrium with costly signals; the
  equilibrium share of informed traders, in a simple version). 8.5 Prediction markets and their record. 8.6 Planned
  economies' internal prices, as data (shortages and queues, the dual-track price reform in China in the 1980s).
- **Defines.** informational efficiency (of an allocation mechanism), fully revealing equilibrium, informed trader,
  Grossman–Stiglitz paradox, prediction market, favourite–longshot bias, dual-track pricing.
- **Models.** Prices as information (*predicts* aggregation of dispersed signals; *tested* prediction markets, lab markets;
  *breaks* thin markets, manipulation, longshot bias). Grossman–Stiglitz (*predicts* prices partly revealing;
  *tested* analyst coverage and price informativeness; *breaks* hard to measure the informed share).
- **Recalls.** School `what-prices-do`; Y1 `price-theory-at-work`; ch. 6–7.
- **Opening chart [L].** Prediction-market price against the observed frequency of the events, by price bin (candidate:
  Snowberg–Wolfers 2010 JPE, horse-racing odds and win rates; or Page–Clemen 2013 EJ). *Fallback:* Berg et al. 2008
  election market forecasts against outcomes, a table.
- **Other charts.** [L] average absolute error of election markets and of polls, by days before the vote (Berg, Nelson,
  Rietz 2008 IJF).
- **Diagrams (2).** Information flows: planner versus market (schematic); the price as a function of the aggregate signal.
- **Boxes.** `record[Election markets against polls]`. `record[Two prices for the same goods: China's dual track]` (Lau,
  Qian, Roland 2000 JPE). `remark` naming "Hayek's result" as the label of the result.
- **Exercises.** ★ R calibration chart; C information count; C revealing price; F what would refute aggregation.
  ★★ C GS equilibrium informed share; P effect of a cheaper signal on informativeness; R election table; C longshot
  expected return; F manipulation test. ★★★ proof of full revelation in the two-signal model; GS non-existence argument;
  welfare of information acquisition.
- **Weekend problem — Kestria's harvest-forecast market.** I signals and a planner; II the market price; III costly
  information; IV the market's record against the forecast office (seeded). *Named result:* the equilibrium share of
  informed traders and the price's forecast error. ~24 questions.
- **Ledger.** b2:snowberg-wolfers2010-*; b2:berg2008-*; b2:lau-qian-roland2000; ~20 rows.

## 9. Social Choice (`social-choice`)

Programme items: Pareto criterion; compensation; SWFs; cycles; Arrow; single-peakedness and median voter; strategic voting
(Lille S5 "choix social"; Varian ch. 33). Gap noted: fair (envy-free) allocations (Varian 33) — a remark.

- **Sections.** 9.1 The Pareto criterion and compensation tests (Kaldor–Hicks; a reversal). 9.2 Social welfare functions as
  tools (utilitarian, maximin, weighted; none endorsed; what each implies). 9.3 Voting cycles (Condorcet paradox;
  Condorcet winner). 9.4 Arrow's theorem (unrestricted domain, weak Pareto, independence of irrelevant alternatives,
  non-dictatorship; proved, short proof). 9.5 Single-peaked preferences and the median voter (proved). 9.6 Strategic
  voting (Gibbard–Satterthwaite told). Remark: envy-free allocations.
- **Defines.** Pareto improvement, compensation test, social welfare function, Condorcet winner, Condorcet paradox (voting
  cycle), independence of irrelevant alternatives, social preference ordering, dictator (social choice), single-peaked
  preferences, median voter theorem, strategy-proof voting rule, envy-free allocation.
- **Model: The median-voter model.** *Assumes* one dimension, single-peaked preferences, majority voting over pairs.
  *Predicts* the median's ideal point wins. *Tested* local referenda on spending (Pommerehne 1978 JPubE, Swiss
  municipalities). *Breaks* several dimensions, turnout, agenda power. (Book 5 `public-choice-voting` tests it further.)
- **Recalls.** School `public-choice-first-look`; ch. 6–7.
- **Opening chart [L].** Share of real ranked-ballot elections with a Condorcet winner, by dataset (candidates:
  Graham-Squire–McCune 2023, US ranked-choice elections; Tideman 1987/2006 ballot data). *Fallback:* a record box.
- **Diagrams (3).** Utility-possibility frontier with a compensation test; single-peaked and non-single-peaked preferences
  on a line; majority cycle as a directed triangle.
- **Boxes.** `record[How often is there a Condorcet winner?]`.
- **Exercises.** ★ C Condorcet winner; C Pareto test; R the chart; F a vote that refutes median prediction. ★★ C
  Borda vs majority; check single-peakedness; P median shift after enfranchisement (direction); C Kaldor–Hicks reversal;
  F test with referenda data. ★★★ Arrow proof step (pivotal voter); median-voter proof with even $n$; strategic
  manipulation of Borda.
- **Weekend problem — Brenmoor council picks a park budget.** I ballots; II single-peakedness; III the median and pairwise
  votes; IV a second dimension and a cycle. *Named result:* the budget that wins every pairwise vote, and the agenda that
  produces each outcome once a second dimension is added. ~24 questions.
- **Ledger.** b2:graham-squire2023-*; b2:pommerehne1978; ~6 rows.

# Part III — Game Theory

## 10. Static Games (`static-games`)

Programme items: normal form; dominance; best responses; Nash; applications: quantity competition, public good, common
resource, location (Nanterre S4 Micro C ch. 2–3; Varian ch. 28–29; Lille S5).

- **Sections.** 10.1 The normal form. 10.2 Dominance and iterated elimination. 10.3 Best responses and Nash equilibrium
  (re-founded; existence in pure strategies not guaranteed). 10.4 Quantity competition as a game (Y1 Cournot recalled as a
  Nash equilibrium; $n$ firms). 10.5 Contributions to a public good (equilibrium underprovision, proved). 10.6 A common
  resource (equilibrium over-use; community rules, licences, quotas, each with evidence). 10.7 Location (two candidates
  or sellers on a line: both at the median).
- **Defines.** normal-form game, strategy profile, strictly dominant strategy, strictly dominated strategy, iterated
  elimination of strictly dominated strategies, best response, Nash equilibrium (re-founded), coordination game,
  common-pool resource (re-founded), Hotelling location game.
- **Model: Nash equilibrium as a model of play.** *Assumes* rational players with correct beliefs. *Predicts* zero
  contributions in a linear public-goods game; over-use of a commons. *Tested* public-goods experiments; field commons.
  *Breaks* first-round contributions of 40–60 %; groups that manage commons by their own rules.
- **Recalls.** School `oligopoly-and-games`, `public-goods-and-commons`; Y1 `cournot-and-bertrand`.
- **Opening chart [L].** Average contribution (share of endowment) round by round in a repeated public-goods experiment
  (candidate: Fehr–Gächter 2000 AER without/with punishment, or Andreoni 1988 JPubE partners/strangers). *Fallback:*
  record box.
- **Diagrams (3).** Payoff matrices (dominance, coordination, prisoner's dilemma); best-response lines in the
  public-good game; Hotelling line.
- **Boxes.** `record[Contributions fall with repetition]`. `record[Commons governed by their users]` (Ostrom 1990 book;
  field studies of irrigation and fisheries, cited as studies).
- **Exercises.** ★ C iterated dominance; C pure NE of 3×3; R contribution chart; F refute the NE contribution prediction.
  ★★ C $n$-firm Cournot; C public good NE vs optimum; P effect of group size on contributions (direction, size);
  C commons over-use; F location test with candidates' positions. ★★★ proof of underprovision for any $n$;
  existence failure example; equilibrium in a three-seller location game.
- **Weekend problem — Kestria's fishing ground.** I the catch game; II the Nash catch; III the efficient catch; IV two
  answers: a licence fee and a community quota with monitoring. *Named result:* the equilibrium over-fishing as a share of
  the efficient catch, and the fee that restores efficiency. ~24 questions.
- **Ledger.** b2:fehr-gaechter2000-*; b2:ostrom1990; ~22 rows.

## 11. Mixed Strategies (`mixed-strategies`)

- **Sections.** 11.1 Randomised strategies (matching pennies). 11.2 The indifference condition (support lemma, proved).
  11.3 Existence (Nash's theorem `\admitted`). 11.4 Zero-sum games and the minimax theorem (proved for 2×2; general
  `\admitted`). 11.5 Tested on professional sport (penalty kicks, tennis serves: equal win rates, serial independence).
  11.6 An inspection game (audits and evasion).
- **Defines.** mixed strategy, support (of a mixed strategy), zero-sum game, maximin strategy, value of a zero-sum game,
  minimax theorem, inspection game.
- **Model: Mixed-strategy equilibrium.** *Predicts* equal scoring rates across sides; no serial correlation. *Tested*
  penalties (Chiappori–Levitt–Groseclose 2002 AER; Palacios-Huerta 2003 REStud), serves (Walker–Wooders 2001 AER).
  *Breaks* novices in the lab alternate too often.
- **Recalls.** Ch. 10.
- **Opening chart [L].** Penalty kicks: share of kicks to each side and the scoring rate by side, kicker and keeper
  (Palacios-Huerta 2003, table). *Fallback:* record box.
- **Diagrams (2).** Best-response correspondences crossing at the mixed equilibrium; payoff matrices.
- **Boxes.** `record[Penalty kicks]`; `record[Serves at Wimbledon]`.
- **Exercises.** mixed NE computations (C), reading the penalty table (R), predicting the effect of a better keeper on
  kick frequencies (P: the counter-intuitive direction), falsification tests (F); ★★★ minimax proof, existence in 2×2,
  inspection-game comparative statics.
- **Weekend problem — Brenland's tax inspectors.** I the inspection game; II mixed equilibrium; III a higher fine:
  evasion unchanged, audits fall; IV a commitment to an audit rate. *Named result:* equilibrium audit probability and
  evasion rate, and the fine at which commitment pays. ~24 questions.
- **Ledger.** b2:palacios-huerta2003-*; b2:walker-wooders2001; b2:cl-g2002; ~14 rows.

## 12. Dynamic Games (`dynamic-games`)

- **Sections.** 12.1 Extensive form (trees with `forest`). 12.2 Backward induction. 12.3 Subgame-perfect equilibrium
  (a Nash equilibrium with a non-credible threat). 12.4 Commitment and credible threats (Stackelberg recalled from Y1).
  12.5 Entry deterrence (capacity as commitment; a two-stage model). 12.6 Alternating-offers bargaining (finite horizon;
  infinite horizon SPE split derived, unequal patience). 12.7 Ultimatum experiments: where the model breaks.
- **Defines.** extensive-form game, subgame, subgame-perfect equilibrium, backward induction, credible threat,
  commitment (strategic), entry deterrence, ultimatum game, alternating-offers bargaining model.
- **Models.** SPE (*tested* bargaining experiments; *breaks* ultimatum offers of 40–50 % and rejections). Alternating offers
  (*predicts* immediate agreement, patience = power; *tested* strike durations, lab; *breaks* delays happen).
- **Opening chart [L].** Mean ultimatum offers and rejection rates across fifteen small-scale societies (Henrich et al. 2001
  AER P&P, table). *Fallback:* Roth et al. 1991 AER four-country table.
- **Diagrams (4).** Game trees (entry, ultimatum, two-round bargaining); capacity-commitment best responses.
- **Boxes.** `record[Ultimatum offers in fifteen societies]`. `debate[Do higher stakes change ultimatum behaviour?]`
  (Cameron 1999 EI; Andersen, Ertaç, Gneezy, Hoffman, List 2011 AER).
- **Weekend problem — Harbour wages in Brenmoor.** I strike costs; II two-round bargaining; III infinite horizon with
  unequal discount factors; IV an outside option. *Named result:* the SPE wage split and how a one-day strike cost moves
  it. ~25 questions.
- **Exercises.** standard mix: backward induction (C), the society table (R), predicting the split with patience (P), F a
  delay observation; ★★★ uniqueness of the Rubinstein SPE (sketch with sup/inf), entry deterrence threshold, chain-store
  in finite horizon.
- **Ledger.** b2:henrich2001-* (~30), b2:andersen2011, b2:cameron1999; ~34 rows.

## 13. Repeated Games (`repeated-games`)

- **Sections.** 13.1 Finite repetition (unravelling, proved). 13.2 Infinite repetition and discounting (discounted average
  payoff). 13.3 Trigger strategies (grim trigger in the prisoner's dilemma: $\delta \ge (T-R)/(T-P)$, proved). 13.4 The
  folk theorem (stated; proved for the PD with grim trigger). 13.5 When collusion can be sustained (Bertrand $\delta\ge 1-1/n$;
  Cournot; demand growth, detection lags, transparency). 13.6 Reputation (incomplete information told; feedback systems).
- **Defines.** repeated game, stage game, discounted payoff (average), grim-trigger strategy, tit for tat, folk theorem,
  collusion (contested: DEFINITIONS #121), critical discount factor, reputation.
- **Model: Collusion in a repeated game.** *Predicts* more firms, lower transparency → less collusion. *Tested* cartel case
  data, lab. *Breaks* multiplicity: the theory allows almost anything.
- **Opening chart [L].** Distribution of the duration of discovered cartels (Levenstein–Suslow 2006 JEL / 2011 JLE
  summary table). *Fallback:* record box.
- **Diagrams (3).** Feasible and individually rational payoff set (folk theorem); critical $\delta$ against $n$; timeline of
  a deviation and punishment.
- **Boxes.** `record[How long cartels last]`; `record[Ratings on online markets]` (Cabral–Hortaçsu 2010 JIE) — a private
  answer to hidden quality.
- **Weekend problem — Two cement makers of Brenmoor.** I stage game; II grim trigger; III detection lag of $L$ periods;
  IV a third entrant. *Named result:* the critical discount factor with a detection lag, and the highest sustainable
  price. ~24 questions.
- **Ledger.** b2:levenstein-suslow-*; b2:cabral-hortacsu2010; ~10 rows.

## 14. Games of Incomplete Information (`bayesian-games`)

- **Sections.** 14.1 Types and beliefs (common prior; Bayes' rule recalled). 14.2 Bayesian Nash equilibrium (Cournot with
  a private cost). 14.3 First-price and second-price auctions (independent private values; uniform case derived;
  truth-telling dominant in the second-price auction, proved). 14.4 Revenue equivalence (stated; both formats give
  $(n-1)/(n+1)$, computed; proof in the Year 3 volume). 14.5 Common values and the winner's curse. 14.6 A first look at
  perfect Bayesian equilibrium.
- **Defines.** type, common prior, Bayesian game, Bayesian Nash equilibrium, first-price sealed-bid auction, second-price
  sealed-bid auction, private values, common-value auction, winner's curse, revenue equivalence theorem, perfect Bayesian
  equilibrium.
- **Model: Independent-private-values auction.** *Predicts* bids $(n-1)v/n$ (risk neutral, uniform); equal expected revenue.
  *Tested* laboratory auctions. *Breaks* overbidding in first-price auctions (risk aversion or other), winner's curse in
  common-value labs and oil leases.
- **Opening chart [L].** Average bid as a share of value by number of bidders, against the risk-neutral prediction
  (candidate: Cox, Roberson, Smith 1982 / Cox–Smith–Walker 1988, table). *Fallback:* record box.
- **Diagrams (3).** Bid functions; expected value conditional on winning (winner's curse); signalling tree with beliefs.
- **Boxes.** `record[Bidding above the prediction]`; `record[Oil leases and the winner's curse]` (Capen, Clapp, Campbell
  1971 JPT; Hendricks–Porter 1988 AER).
- **Weekend problem — Brenland's fishing-licence auction.** I values and types; II first-price equilibrium; III
  second-price; IV a common-value licence and the corrected bid. *Named result:* the equal expected revenue of both
  formats and the winner's-curse correction to a naive bid. ~24 questions. (Reserve prices are left to the Year 3 volume.)
- **Ledger.** b2:cox1982-*; b2:hendricks-porter1988; b2:capen1971; ~10 rows.

# Part IV — Information and Incentives

## 15. Adverse Selection (`adverse-selection`)

- **Sections.** 15.1 The lemons model (proved collapse for uniform quality). 15.2 Insurance with hidden types (two types; a
  pooled price). 15.3 Unravelling (the demand and average-cost curve framework; a death spiral). 15.4 Testing for adverse
  selection (the positive-correlation test; mixed results). 15.5 Selection that runs the other way (advantageous
  selection). 15.6 Private and compulsory answers, with their evidence: warranties, certification, reputation, employer
  groups, risk rating, mandates — and their costs.
- **Defines.** adverse selection (re-founded), lemons model, unravelling (adverse-selection spiral), positive-correlation
  test, advantageous selection, risk classification, community rating, insurance mandate.
- **Models.** Lemons (*tested* used-car and truck markets; *breaks* warranties and dealers fix much of it).
  Demand-and-cost-curve model of insurance (*tested* employer plan prices; *breaks* when preference heterogeneity
  dominates).
- **Recalls.** School `asymmetric-information`; ch. 1–2.
- **Opening chart [L].** Claims rate against the cover chosen (candidate: Cohen 2005 REStat car insurance by deductible;
  Finkelstein–Poterba 2004 JPE annuitant mortality by guarantee). *Fallback:* record box.
- **Other charts.** [S] none here (RAND HIE is used in ch. 17).
- **Diagrams (3).** Lemons with average quality; demand, average cost and marginal cost in an insurance market (equilibrium
  vs efficient, welfare triangle); unravelling steps.
- **Boxes.** `debate[How much adverse selection is there in insurance?]` (Chiappori–Salanié 2000 JPE; Finkelstein–Poterba
  2004; Cohen–Einav 2007). `record[The 2006 Massachusetts mandate]` (Hackmann, Kolstad, Kowalski 2015 AER).
- **Weekend problem — Kestria's health cooperative.** I two risk types; II pooled premium and who leaves; III demand and
  cost curves, the welfare loss; IV a mandate and risk-rated premiums compared. *Named result:* equilibrium coverage and
  the welfare loss of selection, and the change under each answer. ~25 questions.
- **Ledger.** b2:cohen2005-*; b2:finkelstein-poterba2004; b2:chiappori-salanie2000; b2:hkk2015; ~12 rows.

## 16. Signalling and Screening (`signalling-and-screening`)

- **Sections.** 16.1 The education-signal model (separating equilibria, the range; pooling; the intuitive criterion told;
  signalling as waste). 16.2 Screening by a menu (two-type insurance: separating contracts; pooling is not an equilibrium,
  proved). 16.3 Price discrimination as screening (two-type nonlinear pricing: no distortion at the top, rent to the high
  type, proved; recall Y1 second-degree discrimination). 16.4 Diplomas: signal or skill, and the evidence.
- **Defines.** signal (job-market), separating equilibrium, pooling equilibrium, screening,
  incentive-compatibility constraint, participation constraint, information rent, sheepskin effect.
- **Models.** Job-market signalling (*predicts* a wage jump at diploma years; *tested* sheepskin effects; *breaks* diploma
  discontinuities show small signalling value). Screening (*tested* insurance menus, phone plans).
- **Opening chart [A].** Mean 1975 earnings by years of schooling, men in the CPS comparison sample:
  `nsw('cps_controls')` (`education` 0–18, `re75`; N = 15,992). Jumps at 12 and 16 to be checked at writing; the chart
  shows what it shows.
- **Diagrams (3).** Signalling: wage schedule and cost indifference curves of two types; screening contracts in
  (wealth if no loss, wealth if loss) space; two-type nonlinear tariff.
- **Boxes.** `debate[Diplomas: signal or skill?]` (Hungerford–Solon 1987 REStat; Tyler, Murnane, Willett 2000 QJE; Clark–
  Martorell 2014 JPE).
- **Weekend problem — Brenmoor phone plans.** I two consumer types; II full-information plans; III the screening menu;
  IV welfare and the information rent. *Named result:* the optimal menu, the distortion at the bottom and the high type's
  rent, in dalens. ~25 questions.
- **Ledger.** b2:hungerford-solon1987; b2:tyler2000; b2:clark-martorell2014; ~6 rows.

## 17. Moral Hazard and Contracts (`moral-hazard`)

- **Sections.** 17.1 Principal and agent (observable effort first best). 17.2 Insurance against incentives (two outcomes,
  risk-averse agent; second best). 17.3 Linear contracts (CARA–normal: $b^* = 1/(1+rc\sigma^2)$, derived). 17.4 Several
  tasks (muted incentives, told with a two-task example). 17.5 Teams and relative performance (free riding; relative
  evaluation filters a common shock, proved). 17.6 Field evidence (piece rates; sharecropping and tenancy reform; moral
  hazard in health insurance). 17.7 Incomplete contracts and the boundary of the firm (hold-up, told).
- **Defines.** principal–agent problem, moral hazard (re-founded), second-best contract, linear incentive contract, piece
  rate, relative performance evaluation, hold-up problem, incomplete contract, coinsurance rate.
- **Model: Principal–agent with linear contracts.** *Predicts* weaker incentives with more noise and more risk aversion;
  output rises with piece rates. *Tested* Safelite, sharecropping, RAND HIE. *Breaks* multitask gaming; intrinsic
  motivation crowding (evidence mixed).
- **Opening chart [L].** Output per worker before and after the switch to piece rates at an auto-glass installer (Lazear
  2000 AER; a few numbers). *Fallback:* record box.
- **Other charts.** [S] Mean outpatient visits by coinsurance rate in the RAND Health Insurance Experiment
  (`statsmodels.datasets.randhie`: `mdvis` by `lncoins` level; randomised plans) — moral hazard in insurance.
- **Diagrams (3).** Risk–incentive trade-off ($b^*$ against $\sigma^2$); two-outcome contract; common shock filtered by
  relative evaluation.
- **Boxes.** `record[Piece rates at Safelite]` (firm named with its public source). `record[Tenancy reform in West
  Bengal]` (Banerjee, Gertler, Ghatak 2002 JPE). `record[The RAND Health Insurance Experiment]` (Manning et al. 1987 AER).
- **Weekend problem — Sharecropping in a Brenland orchard.** I effort and output; II first best; III the linear share;
  IV a common weather shock and a neighbour's yield in the contract. *Named result:* the optimal share, the agency cost,
  and its fall with relative evaluation. ~25 questions.
- **Ledger.** b2:lazear2000-*; b2:bgg2002; b2:manning1987; ~8 rows.

## 18. Externalities and Public Goods: The Formal Theory (`externalities-and-public-goods-theory`)

- **Sections.** 18.1 An external effect in general equilibrium (inefficiency proved). 18.2 The corrective tax and permits.
  18.3 The Coase theorem and transaction costs (proved with quasi-linear utility; evidence: bees and orchards, contracts
  over externalities). 18.4 Prices against quantities under uncertainty (the slopes rule, derived). 18.5 Public goods: the
  Samuelson condition (proved). 18.6 Voluntary provision falls short (recall ch. 10). 18.7 Personalised prices. 18.8 A
  mechanism that makes people reveal their valuations (the pivot mechanism: truth-telling dominant, proved; its budget
  imbalance). 18.9 Government failure beside market failure (pointer to Year 3 Part V).
- **Defines.** externality (re-founded), corrective tax, tradable emission permit, Coase theorem, transaction cost, public
  good (re-founded), Samuelson condition, personalised (Lindahl) prices, pivot mechanism, club good.
- **Models.** Corrective tax (*tested* fuel and carbon taxes' measured abatement). Coase bargaining (*tested* pollination
  contracts; *breaks* many parties). Prices vs quantities (*tested* permit price volatility). Samuelson provision.
- **Opening chart [L].** The price of a sulphur-dioxide allowance in the US permit market, yearly, from the EPA's annual
  auction results (AGENCY rows, ~18 years). *Alternative [L]:* the EU ETS allowance price, 2008–2023 (EEA). To be settled
  at writing.
- **Other charts.** [A] US sulphur-dioxide emissions 1970–2022, `ceds('so2', isos='USA')`, with the permit programme's start
  marked.
- **Diagrams (4).** Marginal private and social cost with the tax; Weitzman diagram; vertical summation of marginal
  benefits; Coase bargaining.
- **Boxes.** `record[The sulphur-dioxide permit market]` (Schmalensee–Stavins 2013 JEP). `record[Bees and orchards]`
  (Cheung 1973 JLE). `measure[How emissions are counted]` (CEDS).
- **Weekend problem — Brenmoor's river.** I a mill and a fishery; II efficient emission; III the tax and a permit; IV cost
  uncertainty: tax or quota. *Named result:* the efficient level, the corrective tax, and the expected welfare loss of
  each instrument under cost uncertainty. ~25 questions.
- **Ledger.** b2:epa-so2-auction-* (~18); b2:schmalensee-stavins2013; b2:cheung1973; ~22 rows.

# Part V — Macroeconomic Dynamics

## 19. Consumption (`consumption`)

- **Sections.** 19.1 The simple consumption function against the data (short-run vs long-run propensities). 19.2 The
  life-cycle and permanent-income models (derived from ch. 3). 19.3 The Euler equation and the random walk (derived;
  the excess-sensitivity test). 19.4 Precautionary saving and borrowing limits (prudence; buffer stocks told). 19.5 Where
  it breaks: households spend much of a transitory payment (rebates; hand-to-mouth households).
- **Defines.** average propensity to consume, life-cycle hypothesis, permanent income, permanent-income hypothesis,
  random-walk hypothesis (of consumption), excess sensitivity, precautionary saving, prudence, hand-to-mouth household.
- **Models.** Life-cycle/PIH; random-walk consumption (*tested* Hall 1978, Campbell–Mankiw 1989: λ ≈ 0.5; *breaks* rebates).
- **Recalls.** School `keynesian-cross` (marginal propensity to consume, consumption function); ch. 3.
- **Opening chart [S] (deviates from outline).** Quarterly growth of US real consumption and of real disposable income,
  1959–2009 (`macrodata`: `realcons`, `realdpi`). *Why:* weekly spending around a rebate is a study's figure; the rebate
  enters as a `record` box with ledger numbers.
- **Other charts.** [A] household consumption as a share of GDP, 1960–2024, USA, JPN, KOR, DEU (`wdi('NE.CON.PRVT.ZS')`).
- **Diagrams (3).** Life-cycle income and consumption profiles; MPC out of transitory and permanent income; precautionary
  saving (convex marginal utility).
- **Boxes.** `record[The 2001 and 2008 tax rebates]` (Johnson, Parker, Souleles 2006 AER; Parker, Souleles, Johnson,
  McClelland 2013 AER). `measure[The household saving rate]`.
- **D exercise.** Campbell–Mankiw λ on `macrodata` (Python).
- **Weekend problem — A Brenland household gets a bonus.** I PIH; II transitory vs permanent; III borrowing limit; IV a
  population with a hand-to-mouth share. *Named result:* the aggregate MPC out of a one-off payment and the share of
  hand-to-mouth households it implies. ~25 questions.
- **Ledger.** b2:jps2006; b2:psjm2013; b2:hall1978; b2:campbell-mankiw1989; ~6 rows.

## 20. Investment (`investment`)

- **Sections.** 20.1 The user cost of capital (derived; taxes told). 20.2 Adjustment costs and Tobin's $q$ (convex costs;
  $I/K$ as a function of $q$; marginal and average $q$ equal under constant returns, told). 20.3 The $q$ phase diagram.
  20.4 Irreversible investment under uncertainty (option value of waiting, two-period). 20.5 Financing constraints
  (cash-flow sensitivity and the debate). 20.6 Inventories and housing (short).
- **Defines.** user cost of capital, desired capital stock, adjustment cost, Tobin's q (marginal, average), option value of
  waiting, financing constraint.
- **Models.** $q$ theory (*tested* Grunfeld firms, aggregate $q$ regressions; *breaks* low fit, cash flow matters).
  Irreversible investment (*tested* investment falls with uncertainty: Bloom, Bond, Van Reenen 2007 REStud).
- **Opening chart [S] (deviates from outline).** Investment rate against firm value over capital (a $q$ proxy) for the
  Grunfeld firms, 1935–1954 (`statsmodels.datasets.grunfeld`: `invest`, `value`, `capital`). *Why:* aggregate $q$ over
  fifty years is not in the approved data.
- **Other charts.** [A] investment as a share of GDP, 1870–2020, USA, DEU, JPN (`jst`, `iy`).
- **Diagrams (3).** $(K,q)$ phase diagram with saddle path; response to a tax change; option-value threshold.
- **Boxes.** `debate[Do financing constraints drive investment?]` (Fazzari, Hubbard, Petersen 1988 BPEA; Kaplan–Zingales
  1997 QJE). `record[Housing investment around 2006]` (JST `hpnom`, figdata).
- **D exercise.** Grunfeld pooled regression of $I/K$ on $V/K$ (Python).
- **Weekend problem — The Brenmoor container terminal.** I user cost; II $q$ with adjustment costs; III irreversibility and
  uncertainty; IV the timing threshold. *Named result:* the option value of waiting and the demand level that triggers
  investment. ~24 questions.
- **Ledger.** b2:fhp1988; b2:kz1997; b2:bbv2007; ~4 rows.

## 21. Government Debt and Ricardian Equivalence (`government-debt`)

- **Sections.** 21.1 The budget constraint over time (primary balance; debt dynamics $b_{t+1} = \frac{1+r}{1+g}b_t - s_t$).
  21.2 Sustainability (stabilising surplus; the response of surpluses to debt: Bohn's test). 21.3 Ricardian equivalence
  (statement, two-period proof, assumptions, evidence: partial offset). 21.4 Tax smoothing. 21.5 How large debts ended
  (growth, inflation, financial repression, default, surpluses — cases). 21.6 A `debate` box on debt and growth.
- **Defines.** primary balance, intertemporal government budget constraint, debt-stabilising primary surplus, fiscal
  sustainability, Ricardian equivalence, tax smoothing, financial repression.
- **Models.** Ricardian equivalence (*tested* saving offsets; *breaks* liquidity constraints, finite horizons). Tax
  smoothing (*tested* war finance).
- **Recalls.** School `fiscal-policy-and-debt`; Y1 `long-run-model` (crowding out).
- **Opening chart [A] (deviates from outline).** Public debt as a share of GDP, 1870–2020, GBR, USA, FRA, JPN, ITA
  (`jst`, `debtgdp`). *Why:* private saving is not in the approved data as a series.
- **Other charts.** [A] change in national saving against change in government net lending, across countries, two
  decades (`wdi('NY.GNS.ICTR.ZS')`, `wdi('GC.NLD.TOTL.GD.ZS')`, 1995–2019; coverage: 85 countries in 2000) — the offset
  test, with the caveat that net lending includes public investment.
- **Diagrams (2).** Debt dynamics phase line for $r>g$ and $r<g$; two-period Ricardian budget.
- **Boxes.** `debate[Does high public debt slow growth?]` (Reinhart–Rogoff 2010 AER P&P; Herndon, Ash, Pollin 2014 CJE;
  Pescatori, Sandri, Simon 2014 IMF WP; Kumar–Woo 2010). `record[How Britain's debt fell after 1815 and after 1945]` (JST
  figdata; ledger for dates). `record[Germany's debt agreement of 1953]` (ledger).
- **D exercise.** Debt-stabilising primary surplus for four countries (Eurostat `gov_10dd_edpt1`, Python).
- **Weekend problem — Brenland's debt.** (`accounts.csv`: `debt`, `deficit`, `gdp`, invented.) I accounting; II dynamics and
  the stabilising surplus; III a Ricardian household and a constrained one; IV years to reach a target ratio.
  *Named result:* the stabilising primary surplus and the saving offset of a debt-financed tax cut. ~25 questions.
- **Ledger.** b2:bohn1998; b2:rr2010; b2:hap2014; b2:pss2014; b2:london1953; ~10 rows.

## 22. Overlapping Generations (`overlapping-generations`)

- **Sections.** 22.1 The two-period model (log utility, Cobb–Douglas: the capital accumulation equation derived). 22.2 The
  steady state and its stability. 22.3 Too much capital is possible (dynamic inefficiency; the test on capital income and
  investment). 22.4 Pay-as-you-go and funded pensions (returns $n+g$ and $r$; transition; crowding out of capital).
  22.5 The arithmetic of ageing (contribution rate = dependency ratio × replacement rate). 22.6 Debt across generations.
- **Defines.** overlapping-generations model, dynamic inefficiency, pay-as-you-go pension, funded pension, replacement
  rate, old-age dependency ratio.
- **Model: The overlapping-generations model.** *Tested* Abel et al. 1989 REStud (capital income exceeds investment →
  efficient). *Breaks* two periods; no bequests.
- **Recalls.** Y1 `solow-model`; ch. 3, ch. 21.
- **Opening chart [A] (shortened).** People of 65 and over per 100 of working age, 1960–2025, JPN, ITA, KOR, USA, NGA, World
  (`wdi('SP.POP.DPND.OL')`). The projections to 2100 are not in the approved data: two or three projected values (2050,
  2100) from the UN's published *World Population Prospects 2024* summary, as ledger rows, in prose only.
- **Diagrams (3).** Generations timeline; $k_{t+1}$ against $k_t$ with the 45° line; PAYG budget identity.
- **Boxes.** `measure[The old-age dependency ratio]`. `record[Is the capital stock too large?]` (Abel et al. 1989).
- **D exercise.** Contribution rate needed in 2025 at a given replacement rate, for five countries (WDI, Python).
- **Weekend problem — Brenland's pension reform.** I the model; II steady state without pensions; III a PAYG system;
  IV the transition generation. *Named result:* steady-state capital with and without PAYG, and the windfall of the first
  old generation, in dalens. ~25 questions.
- **Ledger.** b2:abel1989; b2:wpp2024-oadr-*; ~6 rows.

## 23. The Ramsey Model (`ramsey-model`)

- **Sections.** 23.1 The household with an infinite horizon (continuous-time Euler $\dot c/c = (r-\rho)/\theta$; derivation from
  the discrete Euler and a limit; transversality told). 23.2 Capital accumulation. 23.3 The phase diagram and the saddle
  path (linearisation; Jacobian eigenvalues of opposite signs, proved). 23.4 The modified golden rule. 23.5 The market
  equals the planner (proved via the Euler and budget equations). 23.6 A change in government purchases (permanent,
  temporary told). Toy-model frame.
- **Defines.** Ramsey model (Ramsey–Cass–Koopmans), representative household, phase diagram, saddle path, modified golden
  rule, transversality condition.
- **Model: Ramsey.** *Predicts* convergence along the saddle path; saving rate falling or rising depending on parameters.
  *Tested* saving rates along catch-up; speed of convergence. *Breaks* one household; implausibly fast convergence
  without adjustment costs.
- **Recalls.** Y1 `solow-model` (steady state, golden rule); ch. 3; mathematics: differential equations, eigenvalues.
- **Opening chart [A].** Gross domestic saving as a share of GDP, Korea 1960–2024 (with Japan 1970–2024 and China
  1960–2024): `wdi('NY.GDS.TOTL.ZS')`.
- **Other charts.** [A] Korea's capital–output ratio, 1953–2023 (`pwt`, `rnna`/`rgdpna`). [I] simulated transition paths
  (figdata seeded numerical solution of the model; a model chart, labelled).
- **Diagrams (3).** Phase diagram with loci, arrows, saddle path (checked against the chapter's parameters); response to a
  permanent rise in $G$; time paths.
- **Boxes.** `record[Korea's saving and capital deepening]`.
- **Weekend problem — Kestria's catch-up.** I the household; II the steady state; III linearisation and the convergence
  speed; IV a permanent rise in government purchases. *Named result:* steady-state capital, the saving rate, and the
  half-life of convergence. ~25 questions.
- **Ledger.** ~2 rows (speed-of-convergence estimate, Barro–Sala-i-Martin 1992 JPE).

## 24. Ideas and Endogenous Growth (`endogenous-growth`)

- **Sections.** 24.1 Constant returns to capital (AK model; prediction that saving rates change growth). 24.2 Ideas used by
  all at once (nonrivalry; increasing returns; why some monopoly is needed). 24.3 The research-sector model (ideas
  production; balanced growth). 24.4 The scale effect it predicts, and its refutation. 24.5 The semi-endogenous version.
  24.6 Growth through replacement of old products (told). 24.7 Are ideas getting harder to find?
- **Defines.** AK model, nonrival good, ideas production function, research sector, scale effect (of growth models),
  semi-endogenous growth model, creative destruction, research productivity.
- **Models.** AK (*breaks* saving rate and growth weakly related). Research-sector model (*breaks* scale effect refuted:
  researchers up, growth flat). Semi-endogenous (*tested* consistent with flat growth; *breaks* long-run growth tied to
  population).
- **Opening chart [A + L] (adapted).** US total factor productivity growth by decade, 1954–2023 (`pwt`, `rtfpna`), beside
  researchers per million people, 1996–2024, for USA, DEU, JPN, KOR, CHN (`wdi('SP.POP.SCIE.RD.P6')`). The seventy-year
  research-effort series (Bloom et al. 2020 AER) enters as ledger numbers in prose.
- **Diagrams (2).** AK growth against $s$; ideas growth for $\phi<1$ and $\phi=1$.
- **Boxes.** `record[Ideas are getting harder to find]` (Bloom, Jones, Van Reenen, Webb 2020 AER). `record[The scale effect
  and the post-war data]` (Jones 1995 QJE).
- **Weekend problem — Brenland's research labs.** I the ideas function; II balanced growth; III doubling the research share;
  IV the level effect. *Named result:* the balanced growth rate and the long-run level gain from doubling the research
  share. ~24 questions.
- **Ledger.** b2:bloom2020-*; b2:jones1995; ~6 rows.

## 25. Expectations and the Lucas Critique (`expectations-and-lucas-critique`)

- **Sections.** 25.1 Adaptive and rational expectations (Y1's adaptive recalled; rational defined; unforecastable errors).
  25.2 The Lucas critique (an estimated Phillips curve shifts when policy changes, derived). 25.3 Policy ineffectiveness
  and its limits (Lucas supply model; contracts and sticky prices). 25.4 Time inconsistency (the inflation-bias model,
  discretion vs commitment, derived). 25.5 Credibility, central-bank independence and inflation targets, with the
  evidence. 25.6 Survey measures of expectations.
- **Defines.** rational expectations, Lucas critique, policy-ineffectiveness proposition, time inconsistency (of policy),
  inflation bias, central-bank independence, inflation targeting, credibility (of policy), central-bank loss function (first used here; ch. 27 recalls).
- **Models.** Lucas supply model (*tested* 1970s; *breaks* anticipated money matters with sticky prices). Inflation-bias
  model (*tested* CBI and inflation; *breaks* low inflation in dependent banks too, causality).
- **Recalls.** Y1 `aggregate-supply` (adaptive expectations, expectations-augmented Phillips curve); school
  `phillips-curve`.
- **Opening chart [A + L].** Average inflation 1955–1988 against an index of legal central-bank independence, for the
  JST countries in Alesina–Summers (1993): inflation from `jst` (`cpi`), the index as ledger rows (~16).
  *Fallback:* the [A] inflation chart below as opening.
- **Other charts.** [S] US inflation against unemployment, 1960–2009, coloured by decade (`macrodata`, `infl`, `unemp`).
  [A + L] median inflation in the years around adoption of an inflation target (`wdi('FP.CPI.TOTL.ZG')`, adoption years
  as ledger rows).
- **Diagrams (2).** Inflation-bias diagram (Phillips line and loss contours: discretion vs commitment); timeline of
  expectations and policy.
- **Boxes.** `debate[Does central-bank independence lower inflation?]` (Alesina–Summers 1993 JMCB; Campillo–Miron 1997;
  Cukierman, Webb, Neyapti 1992 WBER). `record[The shifting Phillips curve, 1960–1985]` (macrodata). `measure[How
  expectations are surveyed]`.
- **D exercise.** Average inflation by decade for 18 JST countries (Python).
- **Weekend problem — Brenland's central-bank law.** I the loss function; II discretion; III a conservative central banker;
  IV the stabilisation trade-off. *Named result:* the inflation bias under discretion and the weight that minimises
  expected social loss. ~24 questions.
- **Ledger.** b2:as1993-cbi-* (16); b2:it-adopt-* (~12); b2:cukierman1992; b2:campillo1997; ~32 rows.

## 26. Search and Unemployment (`search-and-unemployment`)

- **Sections.** 26.1 The matching function (constant returns; tightness). 26.2 Flows and the Beveridge curve (recall Y1;
  derived from the steady state). 26.3 Job creation (free entry of vacancies). 26.4 Wage bargaining (Nash bargaining
  solution, derived). 26.5 Equilibrium unemployment (the DMP model). 26.6 Benefits and productivity (comparative statics,
  with evidence). 26.7 Where it breaks: unemployment moves too little over the cycle.
- **Defines.** matching function, labour-market tightness, vacancy-filling rate, job-creation condition, Nash bargaining
  solution, bargaining power, Diamond–Mortensen–Pissarides model, unemployment-volatility puzzle.
- **Model: DMP.** *Predicts* benefits up → tightness down; productivity up → tightness up. *Tested* benefit-duration
  studies. *Breaks* Shimer (2005 AER): with standard calibration, tightness moves a twentieth of what it does.
- **Recalls.** Y1 `unemployment-flows` (separation and job-finding rates, the Beveridge curve, efficiency wages).
- **Opening chart: DATA TO APPROVE.** A Beveridge curve 2000–2023 needs vacancies. Requested: Eurostat `jvs_q_nace2` and
  `une_rt_q` (same host and licence as the approved Eurostat tables), or the BLS JOLTS (`jt`) and `ln` flat files.
  *Fallback until approved [L]:* the US job-openings rate and unemployment rate, annual averages 2001–2023, from BLS
  published tables as ledger rows (~46) — or the chapter opens on Y1's flow chart, recalled in prose, and draws the
  Beveridge curve as a diagram.
- **Diagrams (3).** Beveridge curve and job-creation line in $(u,v)$; wage curve and job creation in $(\theta,w)$;
  shifts after a benefit rise.
- **Boxes.** `record[The Beveridge curve after 2008 and after 2020]` (if data). `record[How benefits change job finding]`
  (Card, Chetty, Weber 2007 QJE; Lalive 2008 JoE) — the full debate is the Year 3 volume's.
- **Weekend problem — Brenmoor's labour market.** I flows; II matching; III wage and job creation; IV a benefit rise.
  *Named result:* equilibrium tightness, unemployment and wage, and the effect of the benefit rise. ~25 questions.
- **Ledger.** b2:shimer2005; b2:ccw2007; b2:lalive2008; ~4 rows (+46 if the fallback).

## 27. The Three-Equation Model (`three-equation-model`)

Programme gap closed here: the WS–PS model (Nanterre S3 Macro B, Lille S3) as the supply side.

- **Sections.** 27.1 Wage setting and price setting (WS and PS curves; equilibrium unemployment; recall Y1 natural rate).
  27.2 A demand curve with expectations (IS with the real rate). 27.3 A Phillips curve. 27.4 A monetary rule (loss
  function; the MR curve; the interest-rate rule derived). 27.5 Shocks and responses (demand, supply, inflation shocks:
  paths). 27.6 The rule must react more than one for one (the Taylor principle, proved in the model). 27.7 The zero lower
  bound. Toy-model frame; remark on the forward-looking Phillips curve (told).
- **Defines.** wage-setting curve, price-setting curve, three-equation model, monetary-rule curve, Taylor rule, Taylor
  principle.
- **Model: Three-equation model.** *Tested* 1985–2007 rates close to a simple rule. *Breaks* 2008 (no financial sector),
  a flat Phillips curve, 2021 (inflation rose before rates).
- **Recalls.** Y1 `is-lm` (interest-rate rule version), `aggregate-supply`; ch. 25.
- **Opening chart [S].** US short-term rate against a simple rule, 1960–2009 (`macrodata`: `tbilrate`; rule from `infl` and an
  HP-filtered gap of `realgdp`). The 3-month bill rate stands in for the policy rate, said in the caption.
- **Other charts.** [A] US CPI inflation 2019–2025 (`bls_cpi`), with policy-rate decisions as ledger rows (Federal Reserve
  statements, AGENCY) — the 2021–23 record.
- **Diagrams (4).** WS–PS; the three-panel IS–PC–MR adjustment after a shock (geometry matches the example); interest-rate
  path; ZLB kink.
- **Boxes.** `record[Rules and rates, 1960–2007]` (Taylor 1993 CRCSPP; Clarida, Galí, Gertler 2000 QJE). `record[2021–23]`
  (BLS figdata + ledger). `dated{2026}` none planned.
- **D exercise.** Taylor-rule residuals by decade (macrodata, Python).
- **Weekend problem — Brenland's central bank meets a supply shock.** I WS–PS; II PC and MR; III the path; IV the cost.
  *Named result:* the interest-rate path, the cumulated output loss and the sacrifice ratio of the disinflation.
  ~25 questions.
- **Ledger.** b2:taylor1993; b2:cgg2000; b2:fomc-2022-* (~6); b2:hazell2022; ~10 rows.

## 28. Business Cycles and Shocks (`business-cycles`)

- **Sections.** 28.1 The facts (volatility, co-movement, persistence: a table of moments computed by figdata). 28.2 Trend
  and cycle (the HP filter, differences; their artefacts told). 28.3 The real-business-cycle model as a toy model (full
  depreciation, log utility: the analytic case derived; propagation). 28.4 Technology, demand, financial and oil shocks.
  28.5 How a shock is identified (told: narrative and timing restrictions). 28.6 The fall in volatility after 1985 and its
  end.
- **Defines.** cyclical component ("business cycle" itself recalled from school), Hodrick–Prescott filter, procyclical
  variable, countercyclical variable, real-business-cycle model, technology shock, impulse response, Great Moderation.
- **Model: RBC.** *Predicts* procyclical hours, consumption smoother than output, investment more volatile. *Tested*
  matches relative volatilities. *Breaks* weak propagation; productivity–hours correlation; no role for money or finance.
- **Opening chart [A].** Standard deviation of real GDP-per-person growth over rolling ten-year windows, 1880–2020, USA, GBR,
  DEU, and the median of 17 (`jst`, `rgdpmad`).
- **Other charts.** [S] HP cyclical components of US GDP, consumption and investment, 1959–2009 (`macrodata`). [S] a table
  of moments (typeset from a figdata CSV: needs `pgfplotstable`, see report).
- **Diagrams (2).** Trend/cycle decomposition sketch; impulse response of output to a technology shock (model, seeded).
- **Boxes.** `record[The Great Moderation and its end]` (Stock–Watson 2002 NBER MA; McConnell–Perez-Quiros 2000 AER).
  `record[Oil shocks and recessions]` (Hamilton 1983 JPE). `measure[How recessions are dated]`.
- **D exercise.** Relative volatilities and correlations from macrodata (Python).
- **Weekend problem — Brenland's harvest shocks.** I the planner's problem; II the analytic policy rule; III a 1 % shock;
  IV persistence. *Named result:* the impulse response of output and its half-life. ~24 questions.
- **Ledger.** b2:stock-watson2002; b2:mcconnell2000; b2:hamilton1983; b2:nber-dates; ~6 rows.

## 29. Banks, Runs and Financial Crises (`banks-and-crises`)

- **Sections.** 29.1 Short deposits, long loans. 29.2 The bank-run model (two equilibria, derived). 29.3 Deposit insurance
  and the lender of last resort, with the risk-taking they invite. 29.4 Leverage and forced sales. 29.5 2008 step by step.
  29.6 Banks and government debt. 29.7 150 years of crises: credit booms before, slow recoveries after. Private answers
  next to public ones: capital, clearing houses, suspension of convertibility.
- **Defines.** maturity transformation, bank run, Diamond–Dybvig model, deposit insurance, lender of last resort, leverage
  ratio (bank), fire sale, banking crisis, credit boom, bank–sovereign loop.
- **Model: Diamond–Dybvig.** *Predicts* runs as a second equilibrium; insurance removes it. *Tested* the run record
  before and after deposit insurance. *Breaks* runs on solvent banks are rare in data; insurance invites risk.
- **Opening chart [A].** Banking crises per decade, 1870–2020, 18 economies (`jst`, `crisisJST`; checked: 88 crisis years,
  none in 1940–1969).
- **Other charts.** [A] average path of real GDP per person in the five years after a financial-crisis recession and after a
  normal recession (JST, event study). [A] growth of bank loans to GDP in the five years before crises against other years
  (`tloans`, `gdp`).
- **Photograph.** The queue outside a bank branch in 2007 (Commons; licence page read before use) or a public-domain
  photograph of a 1930s bank run.
- **Diagrams (3).** DD timeline and payoffs; a bank balance sheet; the leverage–fire-sale loop.
- **Boxes.** `record[2008 step by step]` (ledger: dated events). `record[Clearing houses in the panic of 1907]` (Gorton
  1985 JEH). `debate[Does deposit insurance make crises more likely?]` (Demirgüç-Kunt–Detragiache 2002 JME; Anginer,
  Demirgüç-Kunt, Zhu 2014 JBF).
- **D exercise.** Crises per decade and credit growth before them (JST, Python).
- **Weekend problem — The Brenmoor savings bank.** I depositors' types; II the optimal deposit contract; III the run
  equilibrium; IV insurance and suspension. *Named result:* the optimal first-period payout and the share of early
  withdrawals at which the bank fails. ~25 questions.
- **Ledger.** b2:dd1983; b2:dkd2002; b2:adz2014; b2:gorton1985; b2:2008-* (~8 dated events); b2:schularick-taylor2012;
  ~14 rows.

# Part VI — Econometrics I, in Python

Shared code: none in `code/shared/`; if a helper is needed it goes in `code/bachelor-2/lib/` (e.g. a loader for the
statsmodels datasets, a table printer). Every listing ≤ 40 printed lines, 88 columns, English names, pandas/numpy/
statsmodels/scipy only, `OMP_NUM_THREADS=1`, data through `econdata`, `country` or (ruling pending) `statsmodels.datasets`.
Each chapter: `code/bachelor-2/NN-<slug>/{listings,outputs,exercises,tests}`; 4–6 data exercises with tested solutions.

## 30. Multiple Regression (`multiple-regression`)

- **Sections.** 30.1 The model in matrix form (assumptions). 30.2 The least-squares estimator (normal equations; the
  projection recalled from mathematics). 30.3 Partialling out (the Frisch–Waugh–Lovell theorem, proved). 30.4 The
  omitted-variable bias formula (derived; sign table). 30.5 Near-collinear regressors (variance of $\hat\beta_j$; the
  variance inflation factor; perfect collinearity and the dummy trap). 30.6 Fit: $R^2$ recalled, adjusted $R^2$.
- **Defines.** multiple regression model, regressor matrix, OLS estimator (multiple), normal equations, Frisch–Waugh–Lovell
  theorem, omitted-variable bias, perfect collinearity, variance inflation factor, adjusted R-squared.
- **Model: The linear regression model** (as a model of a conditional mean: *assumes* linearity, full rank, zero
  conditional mean; *breaks* omitted variables).
- **Opening chart [A].** The estimated return to a year of schooling as controls are added one by one, with 95 % intervals:
  log 1978 earnings of men with positive earnings in the CPS comparison sample (`nsw('cps_controls')`), controls age,
  age², black, hispanic, married, log 1975 earnings.
- **Listings (5) and outputs.** `load_cps.py` (sample, summary); `ols_by_hand.py` (normal equations with numpy against
  `statsmodels.OLS`); `fwl.py` (residualise, regress, same coefficient); `ovb.py` (short = long + δγ, exact);
  `collinearity.py` (simulated correlated regressors: SE against ρ; VIF).
- **Tests.** each listing's numbers (params to 1e-8 between methods; the OVB identity exactly; SE increasing in ρ).
- **Diagrams (2).** Projection geometry ($y$, column space, residual); OVB sign table.
- **Boxes.** `measure[The comparison sample]` (LaLonde 1986 AER; Dehejia–Wahba 1999 JASA; the CPS men).
- **Exercises.** D regressions on Brenland households (`school_years`, `age_head`, `disposable`) and on the CPS sample;
  C matrix algebra by hand ($3\times3$); P OVB sign; F what would show a control is a bad control (pointer ch. 32).
- **Weekend problem — Brenland's household survey.** I matrices; II returns to schooling with controls; III FWL and OVB;
  IV collinearity of age and experience. *Named result:* the return to schooling with its interval and the size of the
  omitted-variable bias. ~25 questions.
- **Ledger.** b2:lalonde1986; b2:dw1999; ~2 rows.

## 31. Inference in Regression (`regression-inference`)

- **Sections.** 31.1 The Gauss–Markov theorem (proved). 31.2 Normal errors: $t$ and $F$ (the restricted/unrestricted $F$
  statistic). 31.3 Unequal error variances and robust standard errors (sandwich derived). 31.4 Clustered errors (the
  Moulton factor, derived for equal groups; few clusters warned). 31.5 Large-sample results (consistency, asymptotic
  normality; CLT `\admitted`). 31.6 The bootstrap (told, one listing optional).
- **Defines.** Gauss–Markov assumptions, best linear unbiased estimator, homoskedasticity, heteroskedasticity, F statistic,
  joint hypothesis, heteroskedasticity-robust standard error, cluster-robust standard error, Moulton factor, asymptotic
  normality, bootstrap.
- **Opening chart [S].** Classical and heteroskedasticity-robust 95 % intervals for the ten coefficients of a regression of
  outpatient visits on plan and health variables in the RAND HIE (`randhie`: `mdvis` on `lncoins`, `idp`, `lpi`, `fmde`,
  `physlm`, `disea`, `hlthg`, `hlthf`, `hlthp` + constant). *Fallback [A]:* the CPS regression of ch. 30 with ten
  coefficients.
- **Listings (5).** `gauss_markov_sim.py` (OLS against another linear unbiased estimator, variances); `t_and_f.py` (HIE
  table; joint F test of the health dummies, by hand and with statsmodels); `robust_se.py` (HC0/HC1 by hand against
  `cov_type='HC1'`); `cluster_sim.py` (grouped data: classical, robust, cluster SE; Moulton); `size_sim.py` (rejection
  rate of a nominal 5 % test, classical vs robust).
- **Tests.** each; simulations seeded, tolerances on rates.
- **Diagrams (1).** Residual spread against fitted value (from the HIE regression, a figdata scatter).
- **Weekend problem — Brenland's census of firms.** (`firms.csv`, invented; sector clusters.) I log production function;
  II robust and clustered intervals; III the F test of constant returns; IV what changes with three clusters. *Named
  result:* the capital elasticity with robust and clustered intervals, and the verdict on constant returns. ~25 questions.

## 32. Specification (`specification`)

- **Sections.** 32.1 Logarithms and elasticities (Engel curve). 32.2 Polynomials, dummy variables and interactions.
  32.3 Measurement error and attenuation (classical error in $x$: plim $=\lambda\beta$, derived; error in $y$).
  32.4 Proxies and bad controls. 32.5 Why searching over specifications voids the tests (simulation). 32.6 Functional
  form checks and outliers (RESET told; leverage told).
- **Defines.** log-log model (constant-elasticity regression), semi-elasticity, dummy variable, interaction term,
  dummy-variable trap, classical measurement error, attenuation bias, reliability ratio, proxy variable, bad control,
  specification search.
- **Opening chart [I].** A simulated slope estimate shrinking as measurement noise grows, with the curve $\lambda\beta$
  (seeded figdata).
- **Listings (5).** `engel.py` (log-log food Engel curve on `statsmodels.datasets.engel`, elasticity); `dummies.py`
  (Brenland households: owner dummy, household-size dummies, an interaction); `attenuation.py`; `proxy.py` (simulated
  ability proxy); `search.py` (20 noise regressors, best one kept: rejection rate).
- **Weekend problem — Brenland's food survey.** I logs; II dummies and interactions; III reported income with a known
  reliability; IV a specification search and an honest threshold. *Named result:* the corrected food–income elasticity and
  the Bonferroni threshold for twenty tries. ~25 questions.
- **Ledger.** b2:engel-source (Koenker–Bassett 1982 for the data); ~2 rows.

## 33. Causality and the Experimental Ideal (`causality-and-experiments`)

- **Sections.** 33.1 Potential outcomes. 33.2 Average effects (ATE, ATT). 33.3 Selection bias (the decomposition, proved).
  33.4 What randomisation buys (balance; regression adjustment for precision). 33.5 Regression as adjustment (conditional
  independence). 33.6 Classic experiments (job training: the NSW; class size: Tennessee STAR, ledger). 33.7 Whether a
  result travels. 33.8 The idea of a natural experiment (the Year 3 volume's designs named in prose).
- **Defines.** potential outcome, treatment effect, average treatment effect, average treatment effect on the treated,
  selection bias, randomised controlled trial, covariate balance, conditional independence assumption, external validity,
  natural experiment, stable unit treatment value assumption.
- **Opening chart [A].** Mean 1978 earnings of treated and control men in the National Supported Work experiment, with 95 %
  intervals (`nsw('nsw_dw')`, N = 445).
- **Listings (5).** `nsw_experiment.py` (difference in means and its SE); `balance.py` (pre-treatment table);
  `naive_cps.py` (treated against the CPS comparison: a large negative "effect"); `regression_adjust.py` (controls in the
  experiment and in the observational comparison); `selection_sim.py` (simulated potential outcomes: the decomposition
  exactly).
- **Coordination with Book 5.** Book 5 owns matching and propensity scores on the NSW samples; this chapter stops at the
  experiment, the naive comparison and regression adjustment.
- **Boxes.** `record[The National Supported Work demonstration]` (LaLonde 1986). `record[Tennessee's class-size
  experiment]` (Krueger 1999 QJE). `record[Results that did not travel]` (Allcott 2015 QJE).
- **Weekend problem — Brenland's training-voucher pilot.** (Seeded simulation of an RCT.) I potential outcomes; II the
  estimate and its interval; III a non-random roll-out and its bias; IV the sample size for a given power. *Named result:*
  the ATE with its interval, the naive bias, and the sample size for 80 % power. ~25 questions.
- **Ledger.** b2:lalonde1986; b2:krueger1999; b2:allcott2015; ~5 rows.

## 34. Time Series: A First Course (`time-series`)

- **Sections.** 34.1 Trend and season. 34.2 Autocorrelation. 34.3 Stationarity. 34.4 Autoregressive and moving-average
  models (AR(1) moments and ACF derived; MA(1)). 34.5 Unit roots and spurious regression, by simulation (Dickey–Fuller).
  34.6 Distributed lags (dynamic and long-run multipliers). 34.7 Forecasting and scoring (pseudo out-of-sample, RMSE,
  random-walk benchmark). 34.8 What Granger causality does and does not mean. 34.9 Serial correlation in regressions:
  HAC standard errors (short).
- **Defines.** autocorrelation function, weak stationarity, white noise, autoregressive process, moving-average process,
  unit root, spurious regression, Dickey–Fuller test, distributed-lag model, dynamic multiplier, out-of-sample forecast,
  root mean squared forecast error, Granger causality, HAC standard error.
- **Opening chart [I].** Two independent simulated random walks that look related, with the $R^2$ of one on the other
  (seeded figdata).
- **Other charts.** [S] sample ACF of US inflation and of unemployment (`macrodata`). [S] one-step forecasts of inflation:
  AR against random walk, 1985–2009.
- **Listings (6).** `random_walks.py` (spurious-regression rejection rate); `acf.py`; `ar_fit.py` (AR(1), AR(2) on
  unemployment, OLS vs `AutoReg`); `adf.py` (log real GDP and its growth); `forecast.py` (rolling forecasts, RMSE);
  `granger.py` (money growth and inflation, `grangercausalitytests`); `hac.py` (Newey–West against classical) — 7 if
  space.
- **Boxes.** `record[Inflation forecasts against a random walk]` (Atkeson–Ohanian 2001 FRB Minneapolis QR).
- **Weekend problem — Brenland's inflation.** (`accounts.csv`: `cpi` 2000–2025, invented.) I growth rates and ACF; II AR(1);
  III a unit-root test; IV a forecast and its interval. *Named result:* the AR(1) persistence, the half-life of an inflation
  shock and a two-year forecast interval. ~25 questions.
- **Ledger.** b2:atkeson-ohanian2001; ~2 rows.

---

## Totals (plan)

- Charts: ~75 (A ≈ 34, S ≈ 11, L ≈ 22 pending the sync, I ≈ 8). Diagrams ≈ 95. Photographs 2–3. AI images 0.
- Listings: ~27 printed in Part VI, plus ~40 data-exercise solutions across the book.
- Ledger rows: ~330 (≈ 200 without the [L] opening tables).
- Web fetches: ~250 planned; 21 used in Phase A.
