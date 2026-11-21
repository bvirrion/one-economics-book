# Book 3 (University Year 1, `bachelor-1`, prefix `b1`) --- chapter briefs

Phase A, written 2026-11-20 by the Book 3 writer under `sources/BATCH_BOOKS_1-5.md`. Binding once the sync has ruled on the
points in the Phase A report; changes after the sync are logged in `PROGRESS.md`. Definitions and labels are in
`DEFINITIONS.md` (this file names them only by their short names).

## Conventions for the whole book

- **Target**: ~430 pp, 32 chapters, ~13.4 pp each (body ~600 source lines, solutions ~300). Exactly 12 exercises per chapter
  (4 x one star, 5 x two stars, 3 x three stars, in order) and one weekend problem of 22--28 questions in Parts I--IV, ending on
  a named, quantified result.
- **Kinds of exercise**, marked in each list below: **R** read a chart or table, **C** compute, **P** use the model to predict a
  direction and a size, **F** say what observation would contradict the model. Every chapter has at least two of each of R, C
  and P and at least one F.
- **Code.** Python is printed only in Part VII (chapters 28--32), the first Python of the series. Parts I--VI print no listing,
  but every *data* exercise (an R or C exercise on a real dataset or a Brenland table) has its tested solution script in
  `code/bachelor-1/NN-<slug>/exercises/` with a test in `tests/`; the printed solution quotes the numbers the script prints.
  From chapter 28 on, listings live in `listings/`, outputs only through `tools/capture_output.py`, and the reader is assumed
  to have done the computer science series' Python (recalled in prose, never re-taught).
- **Charts**: one `openingchart` per chapter, 2--4 charts in all, every one pgfplots over a CSV from a tested script in
  `figdata/bachelor-1/NN-<slug>/`. Theory curves (indifference maps, cost curves, IS--LM) are TikZ `omfigure` diagrams, ~3 per
  chapter, their geometry computed from the chapter's own numbers. From this year the long-run charts use a logarithmic axis,
  called so (`omtimesten` style, the word "logarithmic").
- **Data**: approved datasets only, through `econdata`; Brenland/Kestria through `country`. Every number in prose carries
  `% figdata:` or `% ledger:`. Price bases named on every axis (Maddison 2011 int. \$, PWT 2021 \$, PIP 2021 PPP \$/day).
- **Mathematics** (level guard, the Year 1 mathematics volume): one-variable calculus, Taylor, integrals, first- and
  second-order linear differential equations, matrices (b1 ch. 21), two-variable functions and partial derivatives (its last
  chapter, so chapter 2 here is self-contained on what it uses). Lagrange's method is **admitted** (proved in the Year 2
  mathematics volume); implicit differentiation is derived from the chain rule along a level curve; the central limit
  theorem is admitted. Covariance of two random variables comes in the Year 2 mathematics volume: chapter 30 states it in a
  `notation` box with a pointer, without a definition pair (see the Phase A report).
- **Names**: a person appears only as the label of a model or a result (the Slutsky equation, Shephard's lemma, the Cournot
  model, the Solow model, the Mundell--Fleming model, the Lucas critique is Year 2's). Never "classical", "neoclassical",
  "monetarist" or any school label in print: chapter 23 says "the money-growth propositions", chapter 19 "the separation of
  real and nominal variables" (no "classical dichotomy").
- **Recall boxes** name Books 1--2 in prose ("the grades 10--12 volume"); the mathematics and computer science series in prose.
- **Photographs** (free licence, after reading each Commons licence page; `images/book3/CREDITS.md`): at most six in the book
  (chapters 10, 12, 14, 23, 28 planned below). No AI illustrations (Book 1 only).

## Sync rulings applied (2026-11-20)

These override the chapter briefs below where they differ (run file "Sync decisions" S1--S5; `SERIES_DEFINITIONS.md` R1, R3).

- **Recalled, not defined** (R1, accepted): automatic stabiliser, output gap, supply and demand shocks, velocity *as a Book 2
  term* (ch. 23 owns *velocity* at university per R3), real exchange rate, substitution bias, chained index, sacrifice ratio,
  **deflator** (ch. 1 drops `def:b1:models-and-data:deflator`). Endogenous/exogenous variables are re-founded in ch. 1 with a
  formal definition (a model as a map $y = g(x;\theta)$).
- **Book 4 owns**: Nash equilibrium (general), discount factor, Euler equation, law of one price, Pareto efficiency and
  improvement, Taylor rule, rational expectations, user cost, phase diagram, normal equations, OVB formula, semi-elasticity,
  stationarity. Book 3 names them in prose at most.
- **Wording**: "the money-growth propositions"; "separation of real and nominal variables"; "the long-run model".
- **Data now available** (main session, 16:55): `cex_table` (ch. 4, 5, 7: BLS CE by income quintile; ch. 5 opening chart from
  it, no invented chart needed), `jolts` (ch. 22 vacancies and hires), `fed_series` (ch. 24 H.4.1, H.15), `ecb_total_assets`,
  `eurostat("une_rt_q")` (ch. 31), `bls_ap` (ch. 11, 14: retail food prices in place of FAOSTAT producer prices),
  `bls_cpi` item indexes, `sm_dataset` (macrodata etc.). Not approved: FAOSTAT prices, BLS `ln`, Pink Sheet.
- **Cited-number charts** (`figdata/lib/cited.py`): ch. 10 solar module prices, ch. 15 markups, ch. 17 entry; ch. 22 BLS
  published flow rates.
- **Different cut from Book 2 g12**: ch. 20 (convergence) and ch. 25 (inflation--unemployment) must differ from Book 2's
  `solow-first-look` and `phillips-curve` charts.
- **Code printed only in Part VII**; every chapter has tested solutions in `code/bachelor-1/NN-slug/exercises/`.
- **Ledger ids** must match `tools/check_ledger.py`: one colon only, `b1:<short-name>` (e.g. `b1:graddy-iv`).

## Programme check (Phase A)

Sources read 2026-11-20 (public course pages; provenance only, never printed):

- University A (Paris, licence mention Économie, L1, course sheet 2025--26): S1 introduction to economics, contemporary
  economic problems, economic history, mathematics for economic modelling, descriptive statistics; S2 macroeconomics:
  national accounts, microeconomics: the producer and the consumer, comparative economic theories (value and distribution),
  social protection, introduction to international economics, mathematics for economists.
- University B (Paris region, L1 économie-gestion, second campus): S1 macroeconomics 1: the long run, accounting,
  mathematics 1, statistics 1, principles of economics; S2 microeconomics 1: consumption, macroeconomics 2: the short run,
  mathematics 2, statistics 2; option economic history.
- University C (Paris-Saclay area, L1 économie et gestion): S1 economics: concepts and measures, contemporary economic
  problems, economic sociology, mathematics 1; S2 microeconomics 1: behaviour and markets, macroeconomics 1: economic policy,
  statistics 1, economic history. (University D, south, older sheet: S2 macroeconomics 1, microeconomics 1, statistics 1.)
- International intermediate textbooks: a microeconomics text (38 chapters: market, budget constraint, preferences, utility,
  choice, demand, revealed preference, Slutsky equation, buying and selling, intertemporal choice, asset markets,
  uncertainty, risky assets, consumer's surplus, market demand, equilibrium, auctions, technology, profit maximisation, cost
  minimisation, cost curves, firm supply, industry supply, monopoly, monopoly behaviour, factor markets, oligopoly, game
  theory, ..., exchange, production, welfare, externalities, public goods, asymmetric information); a macroeconomics text
  (20 chapters: science and data of macroeconomics; national income; the monetary system; inflation; the open economy;
  unemployment and the labour market; capital accumulation; population growth and technological progress; growth empirics;
  fluctuations; IS--LM I and II; Mundell--Fleming and regimes; aggregate supply and the short-run trade-off; a dynamic model
  of fluctuations; stabilisation policy; government debt; the financial system; consumption and investment).

Coverage, per chapter, is in each brief below (**Programme items**). Items the sources list that no Book 3 chapter covers:

| Item | Where it goes instead | Proposal |
|---|---|---|
| "Comparative economic theories: value and distribution" (University A, S2) | nowhere: it is history of thought | dropped (user ruling) |
| Economic history, economic sociology, contemporary problems | nowhere as subjects; dated episodes appear in `record` boxes | dropped (outline) |
| Social protection (University A, S2) | Y3 `social-insurance`, `transfers-and-incentives`; Y1 ch. 8 has the kinked budget line | none |
| Introduction to international economics: trade (University A, S2) | g10 `ricardo-model`, g12 `trade-and-trade-policy`, Y3 Part II; Y1 ch. 27 is open-economy macro only | none; ch. 27 recalls the gains from trade in two lines |
| Accounting, law, management, office software | out of scope (`outline_sources.md`) | none |
| Microeconomics text: intertemporal choice, asset markets, uncertainty, risky assets, auctions, exchange, welfare, externalities, public goods, asymmetric information, game theory | Y2 Parts I--IV | none; ch. 8 does the two-period budget only |
| Microeconomics text: market demand (aggregation of individual demands) | not explicit anywhere in Y1 | **add** a section "From individual to market demand" in ch. 5 (horizontal sum; aggregation is exact only under linear Engel curves, told) |
| Microeconomics text: "buying and selling" (endowment income, net demand) | partly ch. 8 (time endowment, full income) | **add** an endowment budget example in ch. 5 (a seller of her own good) so ch. 8's full income is a case of it |
| Macroeconomics text: "a dynamic model of fluctuations" | Y2 `three-equation-model` | none |
| Macroeconomics text: "the financial system" | Y2 `banks-and-crises` | none |
| Macroeconomics text: "government debt and budget deficits" | Y2 `government-debt`; ch. 26 has automatic stabilisers and the debt arithmetic recalled from g12 | none |
| Macroeconomics text: "population growth" in the Solow model | ch. 20 has $n$ throughout | none |
| Statistics 1--2 (Universities B--D): probability, discrete and continuous laws, sampling, estimation, tests | ch. 29--31 (statistics for economists; the probability theory stays the mathematics series') | none |

No chapter of the outline lacks a programme item; the outline's ch. 14 (price theory at work) and ch. 21 (development
accounting, planned economies) go beyond the French L1 sheets, as intended (the international sequence).

---
## Part I --- Method

### 1. Models and Data (`01-models-and-data`)

**Programme items**: introduction to economics and its method (Universities A--C, S1); "the science and the data of
macroeconomics" (macro text ch. 1--2); stocks and flows, real and nominal, growth rates (statistics S1).

**Hook**: a fish market where yesterday's price was higher *and* more fish were sold. Does demand slope up?

**Sections**
1. Given and explained variables --- the four-point frame recalled for a reader with calculus; a model as a map from given
   variables (parameters, exogenous) to explained ones (endogenous); equilibrium as a fixed point; comparative statics in one
   line (preview of ch. 3).
2. Stocks, flows, levels and rates --- stock and flow (a stock is a flow accumulated: $K_{t+1} = (1-\delta)K_t + I_t$);
   continuous growth rate $\dot x/x = \dd\ln x/\dd t$; the rule $\ln(1+g)\approx g$ and its error; growth of a product and of
   a ratio (sum and difference of growth rates).
3. Real and nominal --- deflating by a price index; real growth $\approx$ nominal growth minus inflation (exact form
   $(1+g_N)/(1+\pi)-1$); the Fisher relation previewed in the notation table only.
4. The series notation --- the table of `sources/SERIES_DEFINITIONS.md` printed in full, with a sentence per row on where it
   is used (this book prints it; Books 4--5 recall it).
5. Observed prices and quantities --- a first look at identification: every observed point is an intersection; with both
   curves shifting, the cloud traces neither; a demand shifter that moves supply only traces demand (the idea of an
   instrument, told, named again in Year 3).

**Definitions owned**: endogenous variable, exogenous variable, parameter (one definition), equilibrium (of a model), stock,
flow, continuous growth rate, real value / nominal value (re-founded: "real and nominal" are g8's; this chapter defines
*deflator* only), identification problem, supply shifter / demand shifter (one definition: *shifter*).

**Models**: `model{The market model with shifting curves}` --- assumes linear $Q^d = a - bp + u^d_t$, $Q^s = c + dp + u^s_t$
with independent shocks; predicts the observed slope of the cloud is a weighted mix of $-1/b$ and $1/d$ (derived in the
text: the weights are the shock variances); tested: the price--quantity cloud of the opening chart has a slope near zero and a
correlation of about $-0.4$ in yearly changes; breaks: when shocks to the two curves are correlated, or when the quantity
is set before the price (crops), the formula changes.

**Recalls**: the four-point frame, fact and value, correlation and cause (g10 `economic-models`); growth rates, compounding
and logarithmic growth (g8 `growth-and-compounding`, g12); price index, real and nominal (g8, g10); logarithm and
exponential (mathematics g12).

**Opening chart**: *Yearly change in total hours worked against yearly change in real labour compensation per hour, United
States, 1981--2023* --- PWT 11.0, `pwt(["USA"])`: hours $= emp \times avh$, real compensation per hour
$= labsh \times rgdpna/(emp \times avh)$ (2021 \$ at constant national prices); log differences in per cent. A cloud
(n = 43, correlation about $-0.4$). Caption: "the labour market: one price, one quantity". `make_labour_cloud.py`, test:
43 rows, the 2009 point has negative hours growth.

**Other charts**: (2) *Nominal and real GDP per person, United States, 1960--2024* (WDI `NY.GDP.PCAP.CN`, `NY.GDP.PCAP.KN`,
deflator `NY.GDP.DEFL.ZS`; log axis): the gap is the price level. (3) *A level on a logarithmic axis*: Maddison GDP per person
of the United Kingdom and Japan 1870--2022 (`maddison`), on a logarithmic axis, slopes read as growth rates.

**Diagrams**: (a) a model as a box: given variables in, explained out, parameters on top; (b) three supply--demand pairs
shifting and the cloud of their intersections (geometry from a seeded table in the chapter's figdata, drawn as TikZ with
`demand`/`supply` lines whose equations match the table); (c) stock and flow: a bathtub schematic with $I_t$ in, $\delta K_t$
out.

**Boxes**: `measure[Real values and the deflator]` (how WDI's constant-price series are built, base years); `record[A cloud
read as a curve]` --- a classic case: early statistical demand curves for farm goods that sloped the wrong way (ledger: a
review of the identification problem, e.g. Working 1927, QJE 41(2), named only as the source; the person is not named in
print).

**Exercises** (12): ★ R read two points off the opening chart and say which curve moved (R); ★ growth of $Y/L$ from growth
of $Y$ and $L$ (C); ★ real from nominal with a deflator, Brenland `accounts.csv` 2015--2025 (C, data); ★ stock or flow:
classify eight quantities (R). ★★ the exact and approximate real growth rates when $\pi = 40\%$ (C); ★★ doubling time from a
continuous rate and from $\ln 2/g$ (C); ★★ in the shifting-curves model, compute the slope of the cloud for given variances
(C, P); ★★ predict the sign of the cloud's slope when only demand shifts, then only supply (P); ★★ read the logarithmic chart:
which decade grew fastest (R). ★★★ derive the cloud's slope formula (C); ★★★ a demand shifter that is also a supply
shifter: show identification fails (F); ★★★ name the observation that would contradict "only demand moved" in the opening
chart (F).

**Weekend problem**: *The fish market of Brenmoor.* A seeded table of 40 days of price and catch (`figdata` and
`exercises/`), weather as a supply shifter, a festival as a demand shifter. Part I stocks and flows (cold store), Part II real
and nominal (a price index of the market), Part III the cloud and its slope, Part IV using the weather days to recover the
demand slope. Named result: "the demand elasticity of fish at the mean, recovered from weather days: about $-0.8$" (number
fixed by the seeded script). 24 questions.

**Ledger**: b1:models-and-data:working1927 (paper, as a source comment only); WDI and PWT need none.

### 2. Optimisation under Constraint (`02-constrained-optimisation`)

**Programme items**: mathematics for economists (A, S2: functions of several variables, optimisation); the micro text's
"choice" method; corner solutions.

**Hook**: a student with 60 hours a week to split between paid work and study, and a scholarship that falls as earnings
rise.

**Sections**
1. Functions of two variables --- level curves, partial derivatives, the gradient is perpendicular to a level curve (recall
   from the mathematics volume, self-contained statement); the slope of a level curve, $-f_x/f_y$, derived from the chain
   rule along the curve (this is the implicit-differentiation rule the book uses everywhere).
2. A maximum under one equality constraint --- substitution; tangency: the slope of the level curve equals the slope of the
   constraint; a worked example with $f = x^{1/2}y^{1/2}$, $x + 2y = 12$.
3. Lagrange's method --- the Lagrangian, the first-order conditions (admitted; proved in the Year 2 mathematics volume),
   equivalence with tangency in the two-variable case (proved), the method box.
4. The multiplier as a shadow price --- $\dd f^*/\dd b = \lambda$, proved for the two-variable case by differentiating the
   value function (a first envelope result, generalised in ch. 3); units of $\lambda$.
5. Corners and the second-order check --- inequality constraints by cases ($x \ge 0$); a corner when the tangency would need
   a negative quantity; the bordered second-order condition told, with a picture (a level curve that touches from the wrong
   side is a minimum).

**Definitions owned**: constrained maximum (and minimum), tangency condition, Lagrangian, Lagrange multiplier (economic
reading: *shadow price*; the mathematics series owns "extrema under constraint", so the definition is of the Lagrangian as
used here and of the shadow price), value function, corner solution, interior solution, binding constraint.

**Models**: `model{The constrained optimiser}` --- assumes an agent maximises a known objective under a known constraint;
predicts choices that equalise marginal rates to price ratios and respond to the shadow price; tested: households'
hours fall as the hourly wage rises across countries (opening chart), workers bunch at kinks of tax schedules (ledger:
Saez 2010, AEJ: Economic Policy 2(3), bunching at the first EITC kink by the self-employed); breaks: when the agent does not
know the constraint (complex schedules: ledger: Chetty, Friedman and Saez 2013, AER 103(7), knowledge of the EITC kink
varies across neighbourhoods) or faces fixed hours.

**Recalls**: partial derivatives, gradient, critical points (mathematics Year 1, last chapter); derivative and extremum
(mathematics g11--g12); opportunity cost and the budget (g7, g10 `production-possibility-frontier`).

**Opening chart**: *Annual hours worked per person employed against labour compensation per hour, 2019, 112 countries* ---
PWT 11.0 `avh`; compensation per hour $= labsh \times cgdpo/(emp \times avh)$, 2021 \$ PPP, logarithmic $x$ axis
(`omincomex`). Correlation of $\ln$ wage with hours about $-0.45$. `make_hours_wage.py`; test: n = 112, every value positive,
the United States row matches PWT.

**Other charts**: (2) the same countries binned: median hours by tenth of compensation per hour (a table and a step
chart), so the slope can be read without the cloud.

**Diagrams**: (a) level curves of $x^{1/2}y^{1/2}$ with the constraint line and the tangency at $(6,3)$; (b) the
multiplier: two constraint lines $b$ and $b + \Delta b$ and the gain $\lambda\,\Delta b$; (c) a corner: quasi-linear level
curves meeting $x = 0$; (d) the student's kinked constraint (scholarship withdrawal).

**Boxes**: `record[Bunching at a kink]` (Saez 2010); `measure[Hours worked in the national accounts]` (how PWT's `avh`
is assembled from labour-force surveys and national accounts; ledger: PWT documentation, the hours chapter).

**Exercises** (12): ★ read the opening chart: hours in the top and bottom wage deciles (R, data); ★ solve by substitution
$\max xy$ s.t. $2x + 3y = 24$ (C); ★ the slope of the level curve of $x^2y$ at $(1,2)$ (C); ★ binding or not: three
constraints (R). ★★ Lagrange on $\max \ln x + 2\ln y$ s.t. $p_1x + p_2y = m$ (C); ★★ interpret $\lambda$ and its units, then
predict $f^*$ after $m$ rises by 10 (P); ★★ a corner: $\max x + \ln y$ with small $m$ (C); ★★ the student's kinked
constraint: compute the implicit wage on each segment (C); ★★ predict the direction of hours after a rise in the scholarship
withdrawal rate (P). ★★★ show tangency and the Lagrange conditions are equivalent for any smooth $f, g$ (C); ★★★ a
minimisation dual: min cost of reaching a level curve, and its multiplier (C); ★★★ what observation in the opening chart
would contradict "hours fall as the wage rises because the income effect dominates" --- and why the chart cannot decide (F).

**Weekend problem**: *A farm with one field and two crops.* Land and labour constraints, Part I substitution, Part II
Lagrange, Part III the shadow price of land and the rent a neighbour would pay, Part IV a second constraint (water) that
binds or not. Named result: "the shadow rent of one hectare: \dal{...}" (number from the seeded script). 24 questions.

**Ledger**: b1:constrained-optimisation:saez2010, :cfs2013, :pwt-hours (PWT 11.0 user guide, the hours data).

### 3. Comparative Statics (`03-comparative-statics`)

**Programme items**: micro text "demand" (comparative statics of demand); the method of all intermediate courses.

**Hook**: a fuel tax rises by ten cents. Who can tell, before it happens, how much less fuel will be sold?

**Sections**
1. How a solution moves --- $x^*(\theta)$ from $F(x,\theta) = 0$; $\dd x^*/\dd\theta = -F_\theta/F_x$ derived from the chain rule
   (implicit differentiation, with its condition $F_x \neq 0$); a market equilibrium moved by a tax.
2. Elasticities as logarithmic derivatives --- $\varepsilon = \dd\ln q/\dd\ln p$; constant-elasticity functions; elasticity of
   a product and of a composition (chain rule); the slope of a log--log chart is an elasticity (opening chart).
3. The envelope theorem --- statement and proof for one constraint: $\dd V/\dd\theta = \partial\mathcal L/\partial\theta$ at the
   optimum; the unconstrained case first; applications previewed (Roy's identity ch. 5, Shephard's lemma ch. 10, Hotelling's
   lemma ch. 11).
4. Sign predictions --- when a model only signs a derivative; monotone comparative statics told on one example (a
   supermodular profit); what a test of a sign can refute; the tax example with its sign and size.

**Definitions owned**: comparative statics (the implicit-derivative rule is a `proposition`, not a definition: the notion is
the mathematics series'), elasticity (**re-founded** as $\dd\ln y/\dd\ln x$ --- the outline's "From school to university": elasticity
is g9/g10's; this chapter defines *point elasticity* with calculus), constant-elasticity function, envelope theorem (a
`theorem`, labelled; the term is indexed), sign prediction.

**Models**: `model{A market with a per-unit tax}` --- assumes demand $D(p)$ and supply $S(p - \tau)$, smooth, slopes of the
usual signs; predicts $\dd p/\dd\tau = \varepsilon_s/(\varepsilon_s - \varepsilon_d) \in (0,1)$ and
$\dd\ln q/\dd\tau$ larger when demand is elastic; tested: pass-through of fuel taxes close to one (ledger: Marion and Muehlegger
2011, JPubE 95(9--10)), the falling short-run price elasticity of US gasoline demand (Hughes, Knittel and Sperling 2008,
Energy Journal 29(1)); breaks: market power (pass-through above one), salience (taxes not posted are under-reacted to:
ledger Chetty, Looney and Kroft 2009, AER 99(4)).

**Recalls**: elasticity as a ratio of percentages, point and arc elasticities (g9, g10 `elasticities`); tax incidence in
words and lines (g10 `tax-incidence`); the derivative and the chain rule (mathematics).

**Opening chart**: *Energy use per person against GDP per person, 2019, about 190 countries, logarithmic axes* --- EIA
"Energy consumption per capita" (million Btu per person), WDI `NY.GDP.PCAP.PP.KD` (2021 int. \$), `countries_only=True`;
with the least-squares line (slope about 1.25, an income elasticity read off a chart; the regression is fitted by the
figdata script, its slope printed in the caption with `% figdata:`). Replaces the outline's "the fall in quantity after the
same tax rise, in markets of different elasticities", for which no approved dataset exists (Phase A report). Test: slope
between 0.9 and 1.6, n > 150.

**Other charts**: (2) *The same countries, 1990 and 2019*: has the elasticity moved? (EIA, WDI). 

**Diagrams**: (a) the equilibrium moved by $\tau$: $D$, $S$ and $S$ shifted up by $\tau$, with $\dd p$ and $\dd q$ marked,
for an elastic and an inelastic demand side by side (numbers from the chapter's example); (b) the envelope: a family of
short-run cost curves and their lower envelope (prepares ch. 10); (c) a constant-elasticity demand on linear and log--log
axes.

**Boxes**: `record[Salience]` (Chetty, Looney and Kroft 2009); `measure[An elasticity from a log--log chart]` (what the
slope of a cross-country line does and does not measure).

**Exercises** (12): ★ elasticity of $q = 50p^{-0.5}$ (C); ★ read the elasticity off the opening chart (R, data); ★ sign of
$\dd q^*/\dd a$ for a demand shift (P); ★ elasticity of a product $p\,q$ (C). ★★ implicit derivative of a market equilibrium
with $D = 100 - 2p$, $S = 3(p - \tau)$ (C); ★★ the pass-through formula with $\varepsilon_d = -0.3$, $\varepsilon_s = 1.2$,
then predict the price rise for a 10-cent tax (P); ★★ envelope theorem on $V(a) = \max_x (ax - x^2)$ (C); ★★ the 1990 and 2019
slopes from the second chart (R, data); ★★ which elasticity, demand or supply, does a cross-country chart estimate, if
either (F). ★★★ prove the envelope theorem with one constraint (C); ★★★ derive pass-through under a monopolist with
constant-elasticity demand and show it exceeds one (P); ★★★ an observation that would refute "pass-through lies in (0, 1)"
in a competitive market, and how the salience finding fits (F).

**Weekend problem**: *A carbon levy on Kestria's cement.* Linear and constant-elasticity versions; Part I equilibrium and
its implicit derivatives, Part II elasticities and pass-through, Part III an envelope argument for the cement firm's profit,
Part IV a 10\% levy: price, quantity and revenue changes to first order, and the error of the first-order approximation
against the exact solution. Named result: "the levy's pass-through: 71 cents of every kest" (number from the script). 24
questions.

**Ledger**: b1:comparative-statics:marion2011, :hughes2008, :chetty2009.

---
## Part II --- The consumer

### 4. Preferences and Utility (`04-preferences-and-utility`)

**Programme items**: microeconomics: the consumer (A S2, B S2 "consumption", C S2); micro text ch. 3--4.

**Hook**: a household's grocery basket in 1996 and in 2024, when some prices tripled and others halved.

**Sections**
1. Preference relations --- weak preference, strict preference, indifference; completeness and transitivity (rationality);
   monotonicity; convexity; each axiom with what it rules out.
2. Indifference curves and the marginal rate of substitution --- curves cannot cross (proved from transitivity and
   monotonicity); MRS as the slope; diminishing MRS from convexity.
3. Utility functions --- representation; ordinal meaning: any increasing transformation represents the same ordering
   (proved); $\mathrm{MRS} = u_1/u_2$ is invariant (proved); a lexicographic ordering has no utility representation (told,
   with the picture).
4. The standard forms --- Cobb--Douglas, perfect substitutes, perfect complements, quasi-linear: indifference maps, MRS,
   where each is used.
5. Testing the axioms --- revealed choices and consistency (the generalised axiom of revealed preference told here, owned by
   ch. 5); the experimental evidence.

**Definitions owned**: preference relation (weak, strict, indifference in one definition), completeness, transitivity
(*rational preferences*), monotonicity, convex preferences, indifference curve, marginal rate of substitution, utility
function, ordinal utility, Cobb--Douglas utility, perfect substitutes, perfect complements, quasi-linear utility.

**Models**: `model{Rational preferences}` --- assumes complete, transitive, monotone, convex preferences, stable over the
period; predicts consistent choices (no cycles; GARP) and diminishing MRS; tested: most subjects' budget choices nearly
satisfy GARP (ledger: Choi, Fisman, Gale and Kariv 2007, AER 97(5)); consistency rises with age in children (Harbaugh,
Krause and Berry 2001, AER 91(5)); breaks: choices that depend on how options are framed or on a default (Y2
`behavioural-evidence`, named in prose), addictive goods whose preferences change with use.

**Recalls**: substitutes and complements, the law of demand (g10 `demand`); the budget in words (g7 `households`).

**Opening chart**: *Euro-area consumer prices of selected goods and services, 1996--2024, index 2015 = 100, logarithmic axis*
--- Eurostat `prc_hicp_aind`, `geo == "EA"`, `unit == "INX_A_AVG"`, COICOP `CP00` (all items), `CP0111` (bread and
cereals), `CP0451` (electricity), `CP041` (actual rentals), `CP0911`/`CP0913` (audio-visual and computing equipment), `CP073`
(transport services). Relative prices moved by factors of 3 to 10: what does a consumer do? Replaces the outline's "budget
shares of broad categories across household incomes", for which no approved dataset exists (Data to approve: BLS Consumer
Expenditure Survey tables). Test: the 2015 row is 100 in every column, `CP0913` falls by more than 80\% over the period.

**Other charts**: (2) *Brenland: food share of spending against total spending, by tenth of households, survey of 2025*
(`country` `households.csv`, invented; labelled so): a first Engel picture that ch. 5 explains.

**Diagrams**: (a) the better-than set and an indifference curve, with the axioms marked; (b) two crossing curves and the
contradiction (proof figure); (c) four maps side by side: Cobb--Douglas, substitutes, complements, quasi-linear; (d) a
lexicographic order: the "indifference set" is a point.

**Boxes**: `measure[A price index by category]` (how the HICP's COICOP categories are priced, quality adjustment of
computing equipment; ledger: Eurostat HICP methodological manual); `record[Consistent choices in the laboratory]` (Choi et
al. 2007).

**Exercises** (12): ★ MRS of $u = x_1^{0.3}x_2^{0.7}$ (C); ★ which axiom fails in four described choices (R); ★ ratio of
2024 to 1996 prices for computing equipment and rentals from the opening chart table (R, data); ★ is $v = \ln u$ the same
preference (C). ★★ show perfect complements have no MRS at the kink and draw the map (C); ★★ a quasi-linear MRS does not
depend on $x_2$ (C); ★★ predict which way a Cobb--Douglas consumer's quantities move after the relative price change of the
opening chart, and by how much in budget share (P); ★★ cycles in three observed choices (R); ★★ an observation that would
refute convexity (F). ★★★ prove that every strictly increasing transformation preserves the MRS (C); ★★★ show that
preferences represented by $u = \min(x_1, 2x_2)$ are convex but not strictly (C); ★★★ design three budgets whose choices
would reveal a violation of transitivity; say what the experimental record found (F, P).

**Weekend problem**: *Two flatmates and a shared fridge.* Part I axioms on their stated rankings, Part II utility
representations and MRS, Part III which standard form fits each, from observed swaps, Part IV a trade between them at a
given MRS and whether both gain. Named result: "the swap rate they agree on: 1.6 litres of milk per loaf" (exact from the
utility forms). 24 questions.

**Ledger**: b1:preferences-and-utility:choi2007, :harbaugh2001, :hicp-manual.

### 5. Consumer Choice (`05-consumer-choice`)

**Programme items**: micro text ch. 2 (budget constraint), 5 (choice), 6 (demand), 7 (revealed preference), 15 (market
demand); A S2, B S2.

**Hook**: a household survey shows that the share of spending on food falls as households get richer (Engel's law, as a
regularity named by its label).

**Sections**
1. The budget set --- $p_1x_1 + p_2x_2 \le m$; slope, intercepts; shifts with $m$, $p_1$; an endowment instead of money
   income (a seller of her own good: budget through the endowment point).
2. The optimum --- tangency $\mathrm{MRS} = p_1/p_2$ (Lagrange, ch. 2); corner solutions with substitutes and quasi-linear
   utility; Kuhn--Tucker conditions told on the corner case.
3. Demand functions --- Cobb--Douglas ($x_i = a_i m/p_i$), complements, substitutes, quasi-linear; homogeneity of degree
   zero (proved); Walras' law for the consumer (budget exhausted under monotonicity, proved); Engel curves and normal and
   inferior goods (re-founded with derivatives).
4. Indirect utility --- $v(p, m)$, its properties; Roy's identity from the envelope theorem (proved).
5. Revealed preference --- the weak axiom; a WARP violation found in data; from individual to market demand: horizontal
   sum, and why aggregate demand behaves like one consumer only under special forms (told).

**Definitions owned**: budget set, budget line, demand function (Marshallian), Engel curve, normal good / inferior good
(**re-founded** with $\partial x/\partial m$; g10 owns them), homogeneity of degree zero (economic reading only;
"homogeneous function" is mathematics --- stated as a `proposition`), indirect utility function, Roy's identity
(`theorem`), revealed preference (directly revealed preferred), weak axiom of revealed preference, market demand.

**Models**: `model{The utility-maximising consumer}` --- assumes rational convex preferences, prices taken as given, all
income spent; predicts demand homogeneous of degree zero, budget shares constant under Cobb--Douglas, Engel curves whose
slope signs normal and inferior goods; tested: Engel's law in every household survey (ledger: Banks, Blundell and Lewbel
1997, REStat 79(4), quadratic Engel curves); no money illusion in demand systems (homogeneity is rejected in some systems:
ledger: Deaton and Muellbauer 1980, AER 70(3), the almost ideal demand system --- the person names are model labels only);
breaks: Cobb--Douglas's constant shares fail in the data (food share falls with income), and households in surveys
violate WARP occasionally.

**Recalls**: normal and inferior goods, income elasticity (g10 `demand`, `elasticities`); food share of spending (g6
`food-and-energy`, g7 `households`); Lagrange's method (ch. 2); the envelope theorem (ch. 3).

**Opening chart**: *Food spending against total consumption, Brenland household survey of 2025, 2,000 households* ---
`country` `households.csv` (`food`, `consumption`, dalens); invented, labelled "invented data" in the source line; with the
binned means. An Engel curve. Primary choice, if the user approves the BLS Consumer Expenditure Survey tables (Data to
approve): *food share of spending by income fifth, United States, 1984--2023*, and the Brenland chart moves to an exercise.
Test: 2,000 rows, food share of the bottom tenth above that of the top tenth.

**Other charts**: (2) *Engel curves on log axes*: the slope is the income elasticity of food, below one (Brenland).

**Diagrams**: (a) the budget set and its shifts; (b) the tangency optimum and a corner optimum side by side; (c) the
income-expansion path and the Engel curve derived from it (Cobb--Douglas numbers); (d) a WARP violation: two budgets, two
choices, each inside the other's set.

**Boxes**: `record[Engel's law]` (Banks--Blundell--Lewbel 1997, and the Brenland chart); `measure[A household budget
survey]` (diaries, interviews, what is under-reported; ledger: the BLS CE handbook of methods page).

**Exercises** (12): ★ Cobb--Douglas demands with $a_1 = 0.25$ (C); ★ read the food share at two incomes off the opening
chart (R, data); ★ budget line after a price rise (C); ★ is a good normal or inferior from two Engel points (R). ★★ demands
for $u = \min(x_1, 3x_2)$ (C); ★★ quasi-linear demand with a corner (C); ★★ Roy's identity on Cobb--Douglas indirect utility
(C); ★★ predict the change in food spending when Brenland's incomes rise by 10\%, using the log slope (P, data); ★★ check WARP
on a three-period table (R). ★★★ prove homogeneity of degree zero and Walras' law for any utility (C); ★★★ market demand of
two Cobb--Douglas consumers with different incomes: when does it depend on the income distribution (P); ★★★ what pattern in
a household survey would refute "Cobb--Douglas preferences, the same for all" (F).

**Weekend problem**: *The Brenland survey, read with a model.* Part I budget sets of three households, Part II fitting a
Cobb--Douglas share and seeing it fail, Part III an alternative with a subsistence quantity (Stone--Geary as a label), its
demand and Engel curve, Part IV predicting the food share of the poorest tenth after a 10\% income rise. Named result: "the
subsistence food spending that fits the survey: about \dal{...} a year" (fitted by the tested script in `exercises/`).
26 questions.

**Ledger**: b1:consumer-choice:banks1997, :deaton1980, :ce-handbook.

### 6. Income and Substitution Effects (`06-income-and-substitution-effects`)

**Programme items**: micro text ch. 8 (Slutsky equation), 9 (buying and selling: the endowment effect of a price);
A S2.

**Hook**: Sweden taxed carbon in fuels from 1991 and cut income taxes in the same reform. Would drivers cut back if the
money came back to them?

**Sections**
1. A price change split in two --- the Slutsky way (keep the old bundle affordable) and the Hicks way (keep utility); the
   two pictures; numbers on Cobb--Douglas.
2. Compensated demand and the expenditure function --- $h(p, u)$, $e(p, u)$; duality $h(p,v(p,m)) = x(p,m)$; Shephard's
   lemma for the consumer $\partial e/\partial p_i = h_i$ from the envelope theorem (proved; the producer version is ch. 10).
3. The Slutsky equation --- derived by differentiating the duality identity; compensated demand slopes down (proved from
   concavity of $e$, admitted that $e$ is concave via a short argument); the law of demand holds for normal goods.
4. Giffen goods --- when the income effect beats the substitution effect; the conditions; the evidence on rice and wheat
   (ledger: Jensen and Miller 2008, AER 98(4)).
5. Adding up --- Engel and Cournot aggregation (proved from the budget identity); symmetry of cross effects (stated, from
   Young's theorem); what a fully tested demand system looks like.

**Definitions owned**: substitution effect, income effect (one definition, Slutsky and Hicks forms), compensated
(Hicksian) demand, expenditure function, Slutsky equation (`theorem`), Giffen good, Engel aggregation and Cournot
aggregation (one `proposition`, indexed), net substitutes / net complements.

**Models**: `model{Slutsky decomposition}` --- assumes the consumer of ch. 5 with smooth preferences; predicts negative own
compensated slope, symmetric cross effects, the uncompensated slope smaller in size for a normal good; tested: a
compensated fuel tax still cuts fuel use (the opening chart, ledger: Andersson 2019, AEJ: Economic Policy 11(4), a fall in
transport emissions of about 11\% against a synthetic control); Giffen behaviour in subsidised rice in Hunan (Jensen and
Miller 2008); symmetry is often rejected in estimated systems (told); breaks: when the "income" returned is not seen as
such, or when goods are lumpy (cars).

**Recalls**: ch. 5 demand and indirect utility; envelope theorem (ch. 3); normal and inferior goods.

**Opening chart**: *Carbon dioxide from road transport per person, Sweden against ten western European countries,
1960--2022* --- CEDS `ceds("co2", "country_sector")`, sector `1A3b_Road`, kt; population WDI `SP.POP.TOTL`; tonnes per
person; peers DNK, NOR, FIN, NLD, BEL, DEU, FRA, AUT, CHE, GBR (unweighted mean, said so). Vertical line at 1991. Test:
Sweden's 2019 value below the peers' mean, both series start in 1960. (The tax rates and the income-tax cut: ledger rows
from the Swedish government's page and Andersson 2019.)

**Other charts**: none other from data; the chapter is diagram-led.

**Diagrams**: (a) Slutsky decomposition: old and new budget lines, the pivoted line through the old bundle, three
bundles; (b) Hicks decomposition on the same numbers; (c) a Giffen case: the new optimum moves the "wrong" way; (d)
compensated and uncompensated demand curves through the same point.

**Boxes**: `record[A carbon tax handed back]` (Sweden 1991; what the model said: a compensated price rise lowers use by the
substitution effect alone); `record[Rice in Hunan]` (Jensen--Miller 2008).

**Exercises** (12): ★ Slutsky decomposition with Cobb--Douglas numbers (C); ★ sign of the income effect for an inferior
good (P); ★ read Sweden's and the peers' values in 1990 and 2019 from the chart table (R, data); ★ expenditure function of
$u = x_1x_2$ (C). ★★ Hicks decomposition on the same numbers and its difference from Slutsky (C); ★★ verify Shephard's lemma
on the expenditure function (C); ★★ a 20\% fuel price rise, compensated, with elasticities given: predict the fall in use (P);
★★ Cournot aggregation on a two-good example (C); ★★ why the opening chart alone cannot show the effect of the tax (F).
★★★ derive the Slutsky equation in elasticity form (C); ★★★ show that a Giffen good must be inferior and must take a large
budget share (C, P); ★★★ what data from Hunan would have refuted Giffen behaviour (F).

**Weekend problem**: *A fuel levy with a cheque in the post.* Brenland households with Cobb--Douglas fuel shares, Part I
Slutsky and Hicks effects, Part II expenditure functions and the exact compensation, Part III the aggregate fall in fuel
use and the revenue, Part IV who gains: households whose fuel share is below the mean. Named result: "with the cheque, fuel
use still falls by 12.5\%" (exact). 24 questions.

**Ledger**: b1:income-and-substitution-effects:andersson2019, :jensen2008, :sweden-co2-tax (rate in 1991 and its scope;
AGENCY: Swedish government page), :sweden-1991-reform (income tax cut; source to find, primary preferred).

### 7. Consumer Welfare (`07-consumer-welfare`)

**Programme items**: micro text ch. 14 (consumer's surplus); price indices (statistics S1--S2, all four universities);
the true cost-of-living index.

**Hook**: the consumer price index rose 2.6\% a year in the United States from 1990 to 2024, the consumption deflator 2.2\%.
Which one measures the cost of living?

**Sections**
1. Money measures of a price change --- compensating variation $e(p^1,u^0) - e(p^0,u^0)$ and equivalent variation
   $e(p^1,u^1) - e(p^0,u^1)$, as areas under compensated demands (proved with Shephard's lemma); signs and order for a normal
   good.
2. Consumer surplus --- the area under the Marshallian demand; it lies between CV and EV for a normal good; exact for
   quasi-linear utility (proved); Willig's bound told, with its size for small budget shares.
3. The true cost-of-living index --- $e(p^1,u)/e(p^0,u)$; Laspeyres overstates it, Paasche understates it (proved for the
   reference utilities); substitution bias; chained indices; the geometric index for Cobb--Douglas.
4. New goods and quality --- the virtual (reservation) price of a good before it existed; the value of a new good; quality
   adjustment; the measured biases.

**Definitions owned**: compensating variation, equivalent variation, consumer surplus (**re-founded** as an integral; g10
owns it), true cost-of-living index, substitution bias (if g10 does not define it --- see the report; otherwise recalled),
chained index, virtual price.

**Models**: `model{The cost-of-living index}` --- assumes a representative consumer with stable preferences; predicts the
fixed-basket index exceeds the true index, and a chained index lies closer to it; tested: the measured gap between
fixed-basket and chained indices (opening chart; ledger: BLS C-CPI-U against CPI-U, about 0.25 pp a year, from the BLS
page --- a cited number, not a dataset); the 1996 review's estimate of 1.1 pp of total bias (ledger: Boskin et al. 1998,
JEP 12(1)); breaks: households differ, so no single index is "true" for all; new goods and quality changes need values no
survey observes.

**Recalls**: fixed and current baskets, CPI and deflator (g10 `price-indices`); consumer surplus (g10
`surplus-and-efficiency`); expenditure function and Shephard's lemma (ch. 6); the integral (mathematics g12).

**Opening chart**: *Two measures of US consumer prices, 1990--2024, index 1990 = 100*: the CPI-U (annual average, BLS
`bls_cpi("CUUR0000SA0")`, period M13), a fixed basket updated every two years, against the deflator of household
consumption (WDI `NE.CON.PRVT.CN`/`NE.CON.PRVT.KN`, a chained index). Average growth 2.61\% against 2.16\% a year (probe;
the script's table governs). Caption and `measure` box say that scope and weights also differ, so the gap is not all
substitution bias. Test: both 100 in 1990, CPI above the deflator in 2024.

**Other charts**: (2) *The price of light*: none (no approved data); the new-goods section uses a ledger number (Nordhaus
1996, "Do real-output and real-wage measures capture reality? The history of lighting suggests not", in Bresnahan and Gordon
(eds), NBER) in prose.

**Diagrams**: (a) CV and EV as areas between $p^0$ and $p^1$ under two compensated demands and the Marshallian demand; (b)
the Laspeyres bound: an indifference curve, the old bundle, the new price line; (c) the virtual price of a new good: a
demand curve meeting the axis.

**Boxes**: `measure[Fixed-basket and chained indices]` (how the CPI-U and the C-CPI-U are built; ledger: BLS handbook);
`record[The 1996 review of the CPI]` (Boskin et al.: the biases, what was changed after); `record[A new good]` (Hausman
1999, JBES 17(2), cellular telephones).

**Exercises** (12): ★ consumer surplus under a linear demand after a price rise (C); ★ average yearly growth of the two
indices in the opening chart table (R, data); ★ Laspeyres and Paasche from a two-good table (C); ★ sign of CV and EV for a
price fall (P). ★★ CV and EV for Cobb--Douglas with $m = 1000$ and a doubled price (C); ★★ show CS lies between them on the
same numbers (C); ★★ the true index for Cobb--Douglas and the Laspeyres error (C); ★★ Brenland `basket.csv`: rebuild the
Laspeyres CPI and a chained version from the prices and the 2015 basket, with a Cobb--Douglas substitution assumption (C,
data); ★★ predict the size of substitution bias with a 2\% spread in price growth across goods (P). ★★★ prove the Laspeyres
bound (C); ★★★ quasi-linear utility: show CV = EV = CS (C); ★★★ what evidence would refute "the CPI overstates the cost of
living" for a low-income household (F).

**Weekend problem**: *Brenland's statistician revises the CPI.* From `basket.csv`. Part I Laspeyres and Paasche over
2015--2025, Part II a Cobb--Douglas true index and the substitution bias, Part III a new good (a phone) with a virtual price
and its value, Part IV indexing a pension: what the bias costs over ten years. Named result: "the CPI's substitution bias
in Brenland, 2015--2025: 0.3 points a year" (number from the script). 26 questions.

**Ledger**: b1:consumer-welfare:boskin1998, :ccpiu-gap (BLS page on C-CPI-U), :hausman1999, :nordhaus1996, :bls-cpi-handbook.

### 8. Labour Supply and Saving (`08-labour-supply-and-saving`)

**Programme items**: micro text ch. 9 (buying and selling: labour supply), ch. 10 (intertemporal choice: the two-period
budget only); B S2 consumption; macro text ch. 20 (consumption, microfoundations --- the two-period budget only).

**Hook**: in 1950 a French worker worked about 2,350 hours a year; in 2019 about 1,500. Real hourly pay rose several
times over.

**Sections**
1. Consumption and free time --- the time endowment, full income, the budget $c = w(T - \ell) + y$; the optimum; the
   reservation wage and the participation decision.
2. The wage: income and substitution effects --- the Slutsky equation with an endowment (derived); a backward-bending
   supply possible; uncompensated and compensated elasticities; the Cobb--Douglas case (hours independent of the wage
   without non-labour income).
3. Taxes and transfers bend the budget line --- a proportional tax, a benefit withdrawn at a rate, the kink, the implicit
   marginal rate; bunching; the extensive and intensive margins.
4. Consumption over two periods --- the intertemporal budget $c_1 + c_2/(1+r) = y_1 + y_2/(1+r)$; saving; the effect of the
   interest rate split into substitution and income effects (lender and borrower differ); borrowing limits as a corner.
5. Measured elasticities --- intensive and extensive; micro against macro estimates; the debate stated with its numbers.

**Definitions owned**: time endowment, full income, reservation wage, labour supply function, intensive margin and
extensive margin (one definition), implicit marginal tax rate, intertemporal budget constraint (two-period; Y2
`intertemporal-choice` recalls it), saving (as $y_1 - c_1$; the macro saving rate is g12's: here *household saving* in the
two-period model only).

**Models**: `model{The labour--leisure choice}` --- assumes a worker free to choose hours at a given wage, leisure a normal
good; predicts participation rises with the wage, hours may rise or fall, a benefit withdrawal lowers hours above the kink;
tested: hours per worker fell as real wages rose for seventy years in rich countries (opening chart); extensive-margin
elasticities about 0.25 and intensive Hicksian about 0.33 (ledger: Chetty, Guren, Manoli and Weber 2011, AER P&P 101(3));
bunching at kinks (ch. 2's record); breaks: fixed hours set by employers; the measured long-run fall also reflects
composition (more part-time workers).
`model{Two-period saving}` --- assumes perfect capital markets, known incomes; predicts consumption depends on lifetime
income, not current income, and the response to $r$ has an ambiguous sign; tested: the sign is ambiguous in data too; breaks:
borrowing limits (Y2 `consumption` picks it up).

**Recalls**: hours worked and the sectors of work (g6 `school-and-work`); the labour market (g11 `labour-market`); present
value and the real interest rate (g12 `present-value`); Slutsky (ch. 6).

**Opening chart**: *Hours worked per worker against real labour compensation per hour, 1950--2023, France, Germany, Japan,
the Netherlands, the United Kingdom, the United States* --- PWT 11.0 `avh`, $labsh \times rgdpna/(emp \times avh)$ (2021 \$
at constant national prices, logarithmic $x$ axis), one path per country. Seventy-three years, not the outline's "century"
(PWT starts in 1950; JST has no hours). Test: every country's 2019 hours below its 1950 hours.

**Other charts**: (2) *Labour-force participation of women and men aged 15--64, 1991--2024, six countries* (WDI
`SL.TLF.ACTI.FE.ZS`, `SL.TLF.ACTI.MA.ZS`, modelled ILO estimates; said so) --- the extensive margin.

**Diagrams**: (a) the consumption--leisure budget with a non-labour income and the optimum; (b) a wage rise split into
income and substitution effects; (c) a backward-bending labour supply curve from (b)'s optima; (d) the kinked budget of a
benefit withdrawn at 50\%; (e) the two-period budget and a lender's and a borrower's optima.

**Boxes**: `debate[How elastic is labour supply?]` --- micro (quasi-experimental) against macro (cross-country) estimates:
Chetty et al. 2011's reconciliation against Prescott 2004 (FRB Minneapolis QR 28(1), "Why do Americans work so much more
than Europeans?", large elasticity), each with its weakness (empirical, not normative); `measure[Hours per worker]`
(recalled from ch. 2, short).

**Exercises** (12): ★ reservation wage with Cobb--Douglas and non-labour income (C); ★ hours in 1950 and 2019 for two
countries from the opening chart table (R, data); ★ budget line with a 30\% tax (C); ★ sign of the income effect of a wage rise
on hours (P). ★★ labour supply of $u = \ln c + \ln \ell$ with $y > 0$ (C); ★★ implicit marginal rate of a benefit withdrawn at
60\% plus a 20\% tax (C); ★★ predict participation and hours after a rise in the withdrawal rate (P); ★★ two-period choice with
$u = \ln c_1 + \beta\ln c_2$ (C); ★★ women's participation change 1991--2024 from the second chart (R, data). ★★★ Slutsky with
an endowment, in elasticity form (C); ★★★ a borrower and a lender facing a rise in $r$: signs of the saving response (P);
★★★ what cross-country evidence would refute "Europeans work less because of higher marginal tax rates" (F).

**Weekend problem**: *A benefit, a tax and a second job.* A Brenland worker with an hourly wage, a benefit withdrawn at a
rate and the income tax `TAX_BANDS`. Part I the budget with its kinks, Part II the optimum for two preference forms, Part III
a reform that lowers the withdrawal rate: hours and the government's net cost, Part IV the two-period saving decision with
the same worker. Named result: "the implicit marginal rate on the second job: 68\%" (from `TAX_BANDS` and the benefit
rule). 26 questions.

**Ledger**: b1:labour-supply-and-saving:chetty2011, :prescott2004, :pwt-hours (shared with ch. 2).

---
## Part III --- The firm

### 9. Technology (`09-technology`)

**Programme items**: microeconomics: the producer (A S2, C S2); micro text ch. 18 (technology).

**Hook**: two bakeries make the same bread, one with six workers and one oven, the other with two workers and a line of
machines. Which is efficient?

**Sections**
1. Production functions and isoquants --- inputs, outputs, technically efficient plans; isoquants; marginal products and
   diminishing marginal product (recalled from g11 and made partial).
2. The marginal rate of technical substitution --- slope of an isoquant, $\mathrm{MRTS} = f_K/f_L$ (from the chain rule);
   convex isoquants.
3. Returns to scale --- constant, increasing, decreasing; homogeneous functions of degree $k$; Euler's theorem proved here
   (used in ch. 19); local returns to scale.
4. The elasticity of substitution --- definition $\sigma = \dd\ln(K/L)/\dd\ln(\mathrm{MRTS})$; Cobb--Douglas $\sigma = 1$,
   fixed proportions $\sigma = 0$, CES $\sigma = 1/(1-\rho)$ (derived); estimates.
5. Technical progress --- Hicks-neutral, labour-augmenting, capital-augmenting; what a measured productivity rise can mean.

**Definitions owned**: production function, technically efficient, isoquant, marginal product (**re-founded** as a partial
derivative; g11 owns it), marginal rate of technical substitution, returns to scale (constant, increasing, decreasing in one
definition), elasticity of substitution, Cobb--Douglas production function, fixed-proportions (Leontief) production
function, CES production function, technical progress (Hicks-neutral, labour-augmenting: one definition).

**Models**: `model{The Cobb--Douglas technology}` --- assumes $Y = AK^\alpha L^{1-\alpha}$, $0 < \alpha < 1$; predicts
constant factor shares under cost minimisation and $\sigma = 1$; tested: factor shares roughly stable for decades (PWT,
ch. 19), capital per worker rises with the wage across countries with a slope near one (opening chart); breaks: estimates
of $\sigma$ below one in most firm and industry data (ledger: Chirinko 2008, Journal of Macroeconomics 30(2), a range of
0.40 to 0.60), the decline in labour shares since 1980 (ch. 19).

**Recalls**: production function with one variable input, diminishing marginal product (g11 `production-and-costs`); the
aggregate production function (g12 `growth-and-production-function`); partial derivatives (mathematics).

**Opening chart**: *Capital per hour worked against labour compensation per hour, 2019, 112 countries, logarithmic axes* ---
PWT 11.0, `cn/(emp*avh)` (2021 \$ PPP) against $labsh \times cgdpo/(emp \times avh)$; least-squares slope about 0.94, printed.
Whole economies, not one industry as the outline proposes (no approved industry data). Test: n = 112, slope between 0.7 and
1.2.

**Other charts**: (2) *The capital--labour ratio and the wage--rental ratio over time, United States and Korea, 1953--2019*
(PWT; rental $= (1-labsh)\,Y/K$ in nominal terms): a time-series slope, read as a rough $\sigma$ --- with the caveat that
technical progress moves both.

**Diagrams**: (a) an isoquant map with MRTS at a point; (b) three isoquant shapes (Cobb--Douglas, fixed proportions, perfect
substitutes); (c) returns to scale on a ray: isoquants for 10, 20, 30 spaced closer or wider; (d) Hicks-neutral and
labour-augmenting progress moving an isoquant.

**Boxes**: `measure[A capital stock]` (perpetual inventory, depreciation rates; ledger: PWT documentation, capital chapter);
`record[The elasticity of substitution]` (Chirinko 2008 range).

**Exercises** (12): ★ MRTS of $K^{0.3}L^{0.7}$ at $(8, 27)$ (C); ★ returns to scale of three functions (C); ★ read the
capital per hour of two countries from the chart table (R, data); ★ which shape: four input tables (R). ★★ $\sigma$ for CES
(C); ★★ show Cobb--Douglas is the limit of CES as $\rho \to 0$ (C); ★★ predict $K/L$ after the wage--rental ratio doubles,
for $\sigma = 0.5$ and $\sigma = 1$ (P); ★★ local returns to scale of $f = K^{0.5}L^{0.5} - 2$ (C); ★★ estimate $\sigma$ from
the second chart's table between 1980 and 2019 (R, C, data). ★★★ prove Euler's theorem for degree-$k$ homogeneous
functions (C); ★★★ labour-augmenting progress in CES: does the capital share rise or fall when $\sigma < 1$ (P); ★★★ what
evidence in the opening chart would refute "same Cobb--Douglas technology everywhere" (F).

**Weekend problem**: *Two bakeries and a new oven.* CES technologies, Part I isoquants and MRTS, Part II returns to scale and
the size of each bakery, Part III the elasticity of substitution from their choices at two wages, Part IV an oven that
augments capital: who switches. Named result: "the elasticity of substitution revealed by the two bakeries: 0.6". 24
questions.

**Ledger**: b1:technology:chirinko2008, :pwt-capital.

### 10. Cost Minimisation (`10-cost-minimisation`)

**Programme items**: micro text ch. 20--21 (cost minimisation, cost curves); A S2 (the producer).

**Hook**: the price of a solar module fell by more than 99\% from 1976 to 2023 (ledger). Was that the same technology made
cheaper, or a technology that learned?

**Sections**
1. Isocost lines and the cost-minimising plan --- tangency $\mathrm{MRTS} = w/r$; Lagrange; conditional factor demands for
   Cobb--Douglas and fixed proportions.
2. The cost function and its properties --- increasing in prices, homogeneous of degree one, concave in prices (proved);
   Shephard's lemma from the envelope theorem (proved); the Cobb--Douglas cost function derived.
3. Short run and long run --- a fixed factor; short-run cost curves; the long-run curve as their lower envelope (ch. 3's
   picture, proved); economies of scale and returns to scale (proved: increasing returns imply falling average cost).
4. Average and marginal cost with calculus --- $MC$ cuts $AC$ at its minimum (proved again in one line, recalled from g11);
   minimum efficient scale.
5. Learning by doing --- cost falls with cumulative output; the learning rate; the evidence (Liberty ships, solar modules).

**Definitions owned**: isocost line, conditional factor demand, cost function, Shephard's lemma (`theorem`), short-run cost
function / long-run cost function (one definition), economies of scale (**re-founded** as falling long-run $AC$; g11
owns the words), minimum efficient scale, learning curve (with its *learning rate*).

**Models**: `model{The cost-minimising firm}` --- assumes a firm minimises the cost of each output at given factor prices;
predicts factor demands that fall with own price, Shephard's lemma, $MC = AC$ at minimum efficient scale; tested: input
mixes respond to relative prices (ch. 9); breaks: managers who do not minimise cost (ledger: Bloom et al. 2013, ch. 11).
`model{Learning by doing}` --- assumes unit cost $c = c_0 Q_{\mathrm{cum}}^{-b}$; predicts a fixed percentage fall per
doubling of cumulative output; tested: Liberty-ship labour hours (ledger: Thornton and Thompson 2001, AER 91(5)), solar
modules (ledger: learning rates near 20\%, e.g. Way, Ives, Mealy and Farmer 2022, Joule 6(9)); breaks: costs also fall
with research and scale, which the curve does not separate.

**Recalls**: total, average and marginal cost, short and long run, economies of scale (g11 `production-and-costs`);
marginal cost (g11 `marginal-reasoning`); envelope theorem (ch. 3).

**Opening chart**: *Price of solar modules against cumulative installed capacity, logarithmic axes* --- **needs a ruling**:
no approved dataset holds it. Option A (preferred): a figdata table built from a handful of ledger rows (prices and
cumulative capacity at about eight dates from the published paper), read by a figdata script that checks each value
against the ledger (shared-tool request in the Phase A report). Option B: a dataset to approve (see report). Fallback
meanwhile: *average cost against output in Brenland's census of firms, by sector* (`country` `firms.csv`, invented, labelled),
and the solar numbers in prose with ledger rows.

**Other charts**: (2) *Brenland's census: average cost against output, three sectors* (if not the opening chart).

**Diagrams**: (a) isoquant and isocost tangency, with the expansion path; (b) short-run AC curves and their long-run
envelope (numbers from the Cobb--Douglas example); (c) $AC$, $AVC$, $MC$ with $MC$ through the minima; (d) a learning curve
on linear and log--log axes.

**Boxes**: `record[Liberty ships]` (Thornton--Thompson 2001); `dated{2026}` (current module prices, one ledger row from a
primary source) only if a primary source is found; else none.

**Photograph**: a solar farm (free licence from Wikimedia Commons, licence page read; credit if CC BY/BY-SA).

**Exercises** (12): ★ conditional factor demands for $K^{0.5}L^{0.5}$ (C); ★ cost of 100 units with fixed proportions (C);
★ read the average cost of the largest and smallest firms in the census table (R, data); ★ which shifts the cost function:
a wage rise or a demand rise (P). ★★ Cobb--Douglas cost function and Shephard's lemma check (C); ★★ short-run cost with
$K = 4$, and the long-run cost (C); ★★ minimum efficient scale for $C = 100 + 2q + 0.01q^2$ (C); ★★ a 20\% learning rate:
predict the cost after three doublings (P); ★★ estimate a learning rate from two points of a table (R, C). ★★★ prove
concavity of the cost function in factor prices (C); ★★★ show the long-run curve is the envelope of short-run curves and
touches each where $K$ is optimal (C); ★★★ what data would separate learning by doing from economies of scale (F).

**Weekend problem**: *A battery plant.* Part I the plant's Cobb--Douglas technology and its cost function, Part II short
run with a fixed line, Part III learning by doing across five years of cumulative output, Part IV the price a buyer can
expect in year 8. Named result: "the plant's learning rate: 18\% per doubling; unit cost in year 8: \dal{...}". 25
questions.

**Ledger**: b1:cost-minimisation:thornton2001, :way2022, :pv-price-1976, :pv-price-2023 (primary sources to find).

### 11. Profit Maximisation and Supply (`11-profit-maximisation`)

**Programme items**: micro text ch. 19 (profit maximisation), 22 (firm supply); A S2 (the producer).

**Hook**: after the 2006--08 rise in grain prices, farmers in the Americas planted more maize and soya. How much more, and
how fast?

**Sections**
1. The price-taking firm's problem --- $\max_{K,L} pf(K,L) - wL - rK$; first-order conditions $p f_L = w$, $p f_K = r$; the
   value of the marginal product; second-order conditions and why constant returns give no interior maximum.
2. The supply function and the factor demands --- through the cost function: $p = MC$, the shut-down condition $p \ge \min
   AVC$ (re-founded); supply slopes up (proved from convexity of costs); factor demands slope down.
3. The profit function --- properties (convex in prices, proved); Hotelling's lemma from the envelope theorem (proved); the
   law of supply.
4. Do firms maximise profit? --- the evidence: management experiments, survival, supply responses; what the model needs
   and what it does not (an "as if" prediction tested on its predictions).

**Definitions owned**: profit function, supply function (of the firm; **re-founded**: g11 owns "supply curve of the firm"),
unconditional factor demand, Hotelling's lemma (`theorem`), shut-down price (**re-founded**), law of supply (`proposition`,
indexed).

**Models**: `model{The profit-maximising firm}` --- assumes a price-taking firm with convex costs maximising profit;
predicts supply rising with price, factor demands falling with their own price, Hotelling symmetry; tested: acreage responds
to expected prices, with small short-run elasticities (ledger: Roberts and Schlenker 2013, AER 103(6), supply elasticity
about 0.1); a randomised management intervention raised productivity, so firms had left profit on the table (ledger: Bloom,
Eifert, Mahajan, McKenzie and Roberts 2013, QJE 128(1)); breaks: firms that do not know their costs; non-price-takers (ch.
15).

**Recalls**: price equals marginal cost, shut down (g11 `perfect-competition`); cost function (ch. 10); envelope theorem.

**Opening chart**: *Area harvested of maize and soya beans, Brazil and the United States, 1961--2024, millions of hectares*
--- FAOSTAT `faostat_crops("Maize (corn)", "Area harvested")`, `("Soya beans", ...)`. Quantities only: the prices of the
outline's chart ("against its expected price") are not in the approved data (Data to approve: FAOSTAT Producer Prices,
same host and licence). The 2006--08 price rise is cited in prose from a ledger row. Test: Brazil's soya area in 2024 more
than ten times its 1970 value.

**Other charts**: (2) *Cereal yield per hectare, 1961--2024, five regions* (FAOSTAT `Cereals, primary`, `Yield`): supply grows
on the intensive margin too.

**Diagrams**: (a) $MC$, $AVC$, $AC$ and the supply curve as the part of $MC$ above $\min AVC$; (b) profit as a rectangle at a
price above $AC$; (c) the profit function convex in $p$ (a curve above its tangent line: proof figure).

**Boxes**: `record[Management as a missing input]` (Bloom et al. 2013); `measure[Area harvested and yield]` (what FAOSTAT
measures; ledger: FAOSTAT QCL definitions).

**Exercises** (12): ★ supply of a firm with $C = q^2/4$ (C); ★ shut-down price for $C = 50 + 10q - q^2 + q^3/3$ (C); ★ read
Brazil's soya area in 1990 and 2024 from the table (R, data); ★ sign of the labour demand response to a wage rise (P). ★★
factor demands for $f = K^{0.25}L^{0.5}$ (C); ★★ Hotelling's lemma check on its profit function (C); ★★ with a supply
elasticity of 0.1, predict the area response to a 30\% price rise (P); ★★ yield growth per year 1961--2024 for two regions (R,
C, data); ★★ why constant returns and price taking leave the firm's size undetermined (C). ★★★ prove convexity of the
profit function (C); ★★★ derive the supply elasticity of a Cobb--Douglas firm with one fixed factor (C, P); ★★★ what evidence
would refute profit maximisation as a model of farm supply (F).

**Weekend problem**: *A Kestrian farm in a price boom.* Part I technology and profit function, Part II supply and factor
demands, Part III a price boom: short run (land fixed) and long run, Part IV a fertiliser price rise at the same time: net
effect on output. Named result: "the farm's long-run supply elasticity: 1.0 against 0.33 in the short run" (exact from the
functional forms). 24 questions.

**Ledger**: b1:profit-maximisation:roberts2013, :bloom2013, :grain-prices-2008 (primary: FAO or World Bank page),
:faostat-qcl-defs.

### 12. The Competitive Industry (`12-competitive-industry`)

**Programme items**: micro text ch. 23 (industry supply); free entry; rents (A S2).

**Hook**: a New York taxi medallion sold for about \$1 million around 2013 and for a small fraction of that in 2021
(ledger rows). Who gained when the city capped the number of taxis?

**Sections**
1. Short-run industry supply --- the horizontal sum; a fixed number of firms.
2. Long-run supply with free entry --- zero profit, $p = \min AC$; the number of firms; constant-cost industry: flat
   long-run supply; increasing-cost industry: rising long-run supply from a scarce input.
3. Rents and quasi-rents --- payments to a factor in fixed supply; quasi-rent as revenue minus variable cost in the short
   run; who earns the rent in an increasing-cost industry.
4. Capitalisation --- a stream of rents becomes the price of the asset that earns them (present value recalled); a licence,
   land, a subsidy: the first owner gains, later buyers earn only the normal return; when the rule changes.

**Definitions owned**: industry supply (short run), free entry, long-run industry supply, constant-cost industry /
increasing-cost industry (one definition), economic rent, quasi-rent, capitalisation.

**Models**: `model{Free entry}` --- assumes identical potential firms, no barriers, U-shaped average cost; predicts zero
long-run profit, price at minimum average cost, entry after a demand rise; tested: prices and the number of producers after
demand shocks (g11's chart recalled in prose, no reprint); land rents rise in a fixed-supply input (opening chart); breaks:
licences and patents, firms that differ in cost (then inframarginal rents persist).
`model{Capitalisation}` --- assumes a known, permanent stream and a discount rate; predicts the asset price equals the
present value; a rule change is capitalised at once; tested: medallion prices and their collapse (ledger: the NYC Taxi and
Limousine Commission's medallion transfer data, or a study); house prices rise with fixed land (ledger: Knoll, Schularick and
Steger 2017, AER 107(2), about 80\% of the rise in house prices since 1950 came from land prices); breaks: when the stream is
uncertain or the owners cannot sell.

**Recalls**: economic profit, entry and exit (g11 `perfect-competition`); present value (g12 `present-value`); supply of the
firm (ch. 11).

**Opening chart**: *Real house prices, 1870--2020, five countries, 1990 = 100, logarithmic axis* --- JST R6 `hpnom/cpi`,
AUS, CAN (from 1921), FRA, GBR (from 1899), USA (from 1890). Flat for eighty years, then up: the rent of a fixed factor, land.
Replaces the taxi licence chart, which no approved dataset holds; the medallion prices go in a `record` box from ledger
rows (or into a ledger-built chart if the sync allows one). Test: every country's 2020 value above its 1950 value.

**Other charts**: (2) none from data.

**Diagrams**: (a) firm and industry side by side: a demand rise, short-run price up, entry, back to $\min AC$
(constant-cost); (b) the increasing-cost case: rising long-run supply and the rent area above it; (c) quasi-rent as an area
on the firm's diagram; (d) a licence cap: supply vertical at the cap, the rent per licence, its capitalised value.

**Photograph**: a New York taxi or a taxi medallion plate (Commons, licence page read), only if a free file shows no brand
or readable plate number; else none.

**Boxes**: `record[Taxi medallions]` (prices around 2013 and 2021, the cap, what capitalisation predicted, what happened
when ride-hailing entered; ledger); `measure[A house-price index]` (repeat sales and hedonic methods; ledger: JST
documentation, Knoll et al. 2017).

**Exercises** (12): ★ industry supply of 50 firms with $q = p/2$ (C); ★ long-run price and number of firms for
$C = 100 + q^2$ and $D = 1000 - 10p$ (C); ★ read the real house price ratio 2020/1950 for two countries (R, data); ★ predict the
long-run price after a demand rise in a constant-cost industry (P). ★★ an increasing-cost industry: price, quantity and land
rent (C); ★★ quasi-rent of a firm at a given price (C); ★★ capitalised value of a licence earning \$40{,}000 a year at 5\% (C);
★★ predict the licence price after the city adds 20\% more licences (P); ★★ growth of real house prices 1950--2020 per year (R,
C, data). ★★★ show that a subsidy per unit to a constant-cost industry is passed fully to buyers in the long run, and to the
input owners in an increasing-cost industry (C, P); ★★★ an unexpected and an expected rule change: who loses in each (P);
★★★ what observation would refute "house prices rose because land is scarce" (F).

**Weekend problem**: *Fishing licences in Brenland.* Part I a free-entry fishery and its long-run price, Part II a cap on
boats and the licence rent, Part III capitalisation: the licence price at 4\% and a later buyer's return, Part IV the cap is
lifted: who loses and how much. Named result: "the capitalised value of one licence: \dal{...}; its fall when the cap
goes: 100\%". 25 questions.

**Ledger**: b1:competitive-industry:knoll2017, :nyc-medallion-2013, :nyc-medallion-2021 (primary: NYC TLC pages or a
study), :jst-house-docs.

---
## Part IV --- Markets and price theory

### 13. Partial Equilibrium and Welfare (`13-partial-equilibrium-welfare`)

**Programme items**: micro text ch. 14--16 (consumer's surplus, market demand, equilibrium); C S2 "behaviour and
markets"; taxes and incidence with calculus.

**Hook**: Germany cut its value-added tax from 19\% to 16\% for the second half of 2020. Consumer-price inflation fell at once
by about two points and jumped back in January 2021.

**Sections**
1. Equilibrium with general functions --- existence and uniqueness for continuous monotone $D$ and $S$ (intermediate value
   theorem, proved); stability of price adjustment $\dot p = k(D(p) - S(p))$ (the linear differential equation recalled, proved
   stable when $D' < S'$); a cobweb told.
2. Surplus as an integral --- $CS = \int_{p^*}^{\bar p} D(p)\,\dd p$, $PS = \int S$; total surplus is maximised at the
   competitive equilibrium (proved by the first-order condition on $\int_0^q (P^d - P^s)$).
3. Deadweight loss and elasticities --- the triangle to second order, $DWL \approx \tfrac12 \tau^2 \,\dfrac{\dd q}{\dd\tau}$,
   in elasticities $\tfrac12 \tau^2 q/p \cdot \varepsilon_s\varepsilon_d/(\varepsilon_s - \varepsilon_d)$ (derived); the square rule.
4. Incidence --- the incidence formula of ch. 3 again with surplus; statutory and economic incidence; a subsidy; the record
   on pass-through (VAT, cigarettes, fuel).
5. When one market can be studied alone --- small budget share, small income effects, few links; the error otherwise (a
   second market's surplus changes when a substitute is taxed).

**Definitions owned**: partial equilibrium (an equilibrium of one market with other prices given), stable equilibrium (of
price adjustment), producer surplus (**re-founded**), total surplus, deadweight loss (**re-founded** as an integral and its
second-order formula: the *Harberger triangle* is indexed as its label), statutory incidence / economic incidence (one
definition; **re-founds** g10's tax incidence), pass-through rate.

**Models**: `model{Competitive partial equilibrium}` --- assumes one market, price-taking, other prices fixed, no external
effects; predicts the incidence shares $\varepsilon_s/(\varepsilon_s-\varepsilon_d)$ for buyers, a DWL growing with the square
of the tax; tested: the German VAT cut (opening chart; ledger: Fuest, Neumeier and Stöhlker, pass-through study of the 2020
German VAT cut --- exact reference to verify), cigarette tax pass-through near or above one (ledger: Harding, Leibtag and
Lovenheim 2012, AEJ: Economic Policy 4(4)), laboratory markets converge to the predicted price (recalled from g10, ledger:
Smith 1962, JPE 70(2)); breaks: market power, temporary changes (asymmetric pass-through of the cut and the return), large
markets that move other prices.

**Recalls**: consumer and producer surplus, deadweight loss, tax incidence (g10 `surplus-and-efficiency`, `what-prices-do`,
`tax-incidence`); the integral (mathematics g12); comparative statics (ch. 3); CV and EV (ch. 7).

**Opening chart**: *Germany: yearly consumer-price inflation, month by month, January 2019 -- December 2022, all items and
food* --- Eurostat `prc_hicp_manr`, `geo == "DE"`, COICOP `CP00` and `CP01`, unit RCH\_A; the July--December 2020 cut shaded.
Inflation went from 0.8\% in June to 0.0\% in July 2020 and from $-0.7\%$ in December to 1.6\% in January 2021 (probe; table
governs). Replaces the outline's "estimated DWL against the tax rate", which is theory, not data; that curve becomes diagram
(c). Test: the January 2021 value exceeds the December 2020 value by more than 2 points.

**Other charts**: (2) none.

**Diagrams**: (a) surplus areas as integrals under non-linear $D$ and $S$ (numbers from $D = 100/p$, $S = p$); (b) the tax
wedge with incidence shares and the DWL triangle; (c) DWL against the tax rate for $\varepsilon_d = -1$, $\varepsilon_s = 2$: a
pgfplots function plot inside an `omfigure` (a diagram, not data), against the revenue curve; (d) the phase line of price
adjustment.

**Boxes**: `record[A temporary VAT cut]` (Germany 2020: what the model said: buyers' share $\varepsilon_s/(\varepsilon_s-\varepsilon_d)$;
what was measured; LAW row for the cut's dates and rates); `measure[Monthly inflation from the HICP]` (12-month rates, base
effects: why the cut shows twice).

**Exercises** (12): ★ CS and PS for $D = 120 - 2p$, $S = p$ (C); ★ the inflation drop and rebound from the chart table (R,
data); ★ buyers' share of a tax with $\varepsilon_d = -0.5$, $\varepsilon_s = 1.5$ (C); ★ predict which side bears more of a
cigarette tax (P). ★★ CS for $D = 100/p$ between $p = 1$ and $p = 2$ (C); ★★ DWL exactly and by the second-order formula for
a 10\% tax; compare (C); ★★ doubling the tax: predict DWL and revenue (P); ★★ stability of $\dot p = 0.5(D - S)$ for an
upward-sloping demand that crosses supply from below (C); ★★ the 2020 VAT cut was 3 points on 19: a full pass-through
predicts what fall in prices; compare with the table (R, P, data). ★★★ prove total surplus is maximised at the competitive
quantity (C); ★★★ a tax on a good with a close substitute: the surplus change in the second market and the error of the
one-market DWL (C); ★★★ what pattern in the 2020--21 data would refute competitive incidence (F).

**Weekend problem**: *A sugar tax in Brenland.* Constant-elasticity demand and supply calibrated to Brenland's `basket.csv`
price and an invented quantity. Part I equilibrium and stability, Part II the tax: prices, quantity, revenue, Part III
surplus changes and DWL exactly and to second order, Part IV the rate that raises the most revenue, and its DWL per dalen
raised. Named result: "the marginal deadweight loss of the last dalen raised at a 20\% rate: 0.31 dalens". 26 questions.

**Ledger**: b1:partial-equilibrium-welfare:de-vat-2020 (LAW), :fuest-vat (paper), :harding2012, :smith1962.

### 14. Price Theory at Work (`14-price-theory-at-work`)

**Programme items**: the international sequence's price theory (outline addition); C S2 "markets"; arbitrage, storage,
controls.

**Hook**: why does a flat cost the same to buy as twenty or thirty years of its rent, and why did that number move so much
in a century?

**Sections**
1. The full price --- money price plus time and the shadow value of quality; queues under a ceiling; a toll against a
   congested free road; quality adjusts when price cannot.
2. Around a controlled price --- a ceiling: shortage, queues, quality, side payments, a black market, and who gains (with
   surplus); rent control's long-run supply response; a floor.
3. Quota against tariff --- the same quantity, different rents: who earns the quota rent; a voluntary export restraint; the
   record.
4. Arbitrage over space and over time --- the law of one price net of transport cost; storage: the price rises through the
   crop year by the cost of carry; the convenience yield; a futures price (told: the quantitative finance series owns
   futures).
5. Buying against renting --- the arbitrage condition: rent $=$ price $\times$ (real interest rate $+$ depreciation $-$ expected
   real price growth); capitalisation of ch. 12 at work; the rent yield and the interest rate (opening chart).

**Definitions owned**: full price, black market (as *parallel market*: neutral word: "an unrecorded market above the
ceiling"), quota rent, spatial arbitrage condition (the *law of one price* is g10's? --- see the report; here
*arbitrage condition*), cost of carry, convenience yield, rent--price arbitrage condition (the *user cost of housing* is
avoided: Y2 owns *user cost of capital*), rental yield.

**Models**: `model{Arbitrage}` --- assumes traders who can buy, store, ship or rent at known costs; predicts price gaps
equal to transport costs, prices rising through the crop year by the cost of carry, rental yields tracking the real interest
rate; tested: rental yields and real long rates over 150 years (opening chart); price dispersion and transport costs (Y3
`gravity`, named in prose); breaks: when shorting or storage is impossible, when expectations of price growth swing
(1980s, 2000s housing).
`model{A price ceiling}` --- assumes a competitive market with a binding ceiling; predicts shortage, non-price rationing,
lower quality and long-run supply loss; tested: rent control in San Francisco reduced rental supply by about 15\% (ledger:
Diamond, McQuade and Qian 2019, AER 109(9)); petrol queues under the 1970s US controls (ledger: a study, e.g. Frech and Lee
1987, QJE 102(1)); breaks: where landlords cannot convert or exit, short-run effects are small.

**Recalls**: price ceiling and floor (g9 `price-controls-taxes-subsidies`); what prices do, arbitrage and storage (g10
`what-prices-do`); capitalisation (ch. 12); present value (g12).

**Opening chart**: *Housing rental yield and the real long-term interest rate, 1950--2020, France, the United Kingdom, the
United States* --- JST R6 `housing_rent_yd` (per cent), real long rate $= ltrate - $ CPI inflation (`cpi`, smoothed over
three years, said so). Replaces the outline's "price of a storable crop through the crop year", for which no approved
monthly price exists (Data to approve: FAOSTAT Producer Prices, monthly). Test: three countries, 71 years each, yields between
1\% and 10\%.

**Other charts**: (2) *Rental yields in 1950, 1980 and 2020 across the 16 JST countries with data* (bar-like dot plot, JST).

**Diagrams**: (a) a binding ceiling with the queue cost per unit making the full price; (b) quota against tariff: the same
quantity, rent to licence holders against revenue to the state; (c) the price path through a crop year: a saw-tooth rising
by the cost of carry, falling at harvest; (d) two regions with a transport cost: excess supply and demand curves and the
traded quantity.

**Boxes**: `record[Rent control in San Francisco]` (Diamond--McQuade--Qian 2019; what the model said, what was found:
landlords converted units); `record[A voluntary export restraint]` (US--Japan cars 1981: quota rents to the exporting firms;
ledger: Berry, Levinsohn and Pakes 1999, AER 89(3)); `measure[A rental yield]` (JST's construction; ledger: Jordà et al.
2019, QJE 134(3), "The rate of return on everything").

**Photograph**: a grain elevator or silo (free licence, Commons).

**Exercises** (12): ★ full price with a 2-hour queue at a wage of 15 (C); ★ read the rental yield and real rate of one
country in 1980 and 2020 from the table (R, data); ★ quota rent of a quota of 40 units (C); ★ predict the price gap of two
markets 300 km apart (P). ★★ shortage and DWL under a ceiling, with and without queueing cost (C); ★★ a tariff and a quota
with the same import level: compare surpluses (C); ★★ crop-year price path with storage cost 1\% a month and interest 0.5\%
(C); ★★ predict the rent after the real rate falls by two points, holding expected growth (P); ★★ correlation of the yield
and the real rate in the table, by country (R, C, data). ★★★ derive the rent--price condition from no-arbitrage (C); ★★★ a
ceiling with heterogeneous buyers and random rationing: the surplus loss exceeds the triangle (C, P); ★★★ what observation
would refute "rents equal the user cost" in the opening chart (F).

**Weekend problem**: *The grain store of Brenmoor.* Part I harvest, storage cost and the monthly price path, Part II
arbitrage with Kestria across the border at a transport cost, Part III a price ceiling in the lean months: queues and the
full price, Part IV the store's value capitalised. Named result: "the lean-month price premium the store earns: 9.5\%". 25
questions.

**Ledger**: b1:price-theory-at-work:diamond2019, :frech1987, :berry1999, :jorda2019.

### 15. Monopoly and Pricing (`15-monopoly-pricing`)

**Programme items**: micro text ch. 24--25 (monopoly, monopoly behaviour); C S2; regulation of natural monopoly.

**Hook**: an airline sells the same seat at five prices; a cinema offers student tickets; a phone plan has a monthly fee and
a price per gigabyte.

**Sections**
1. Monopoly with calculus --- $MR = p(1 + 1/\varepsilon)$ (derived); the markup rule; the Lerner index
   $L = (p - MC)/p = -1/\varepsilon$; DWL; the monopolist never prices on the inelastic part.
2. Price discrimination --- first degree (perfect: no DWL, all surplus to the seller), third degree (separate markets:
   $MR_1 = MR_2 = MC$, the more elastic market pays less, proved), second degree (menus, quantity discounts; screening is Y2's,
   named in prose); welfare effects.
3. Two-part tariffs and bundling --- the optimal two-part tariff with identical buyers ($p = MC$, fee $= CS$); with two types;
   bundling two goods with negatively correlated valuations.
4. Natural monopoly --- subadditive costs; marginal-cost pricing loses money; average-cost pricing; price caps (RPI$-X$):
   incentives to cut cost; the record.
5. Measuring market power --- Lerner from elasticities; the production approach to markups (told); the measured rise in
   markups and its debate.

**Definitions owned**: Lerner index, markup (**re-founded** as $p/MC$; g11 owns "markup" in words --- see report), price
discrimination (first, second, third degree in one definition; **re-founds** g11's first look), two-part tariff, bundling,
natural monopoly (**re-founded** with subadditivity), average-cost pricing, price-cap regulation.

**Models**: `model{Monopoly pricing}` --- assumes one seller, a known demand, no entry; predicts $p > MC$ with the inverse-
elasticity markup, higher prices to less elastic buyers, a DWL; tested: price discrimination in theatre tickets (ledger:
Leslie 2004, RAND Journal of Economics 35(3)); measured markups (ledger: De Loecker, Eeckhout and Unger 2020, QJE 135(2), an
aggregate markup from 1.21 in 1980 to 1.61 in 2016); breaks: entry and new products (Y3 `competition-policy`), durable goods
(the monopolist competes with its future self, told), regulated firms.

**Recalls**: monopoly, marginal revenue, natural monopoly, different prices for different buyers (g11 `monopoly`);
elasticity (ch. 3); surplus as an integral (ch. 13).

**Opening chart**: *Price--cost margins across industries* --- **needs a ruling** (no approved dataset): Option A, a
ledger-built table of published markups (De Loecker--Eeckhout--Unger 2020's aggregate series at about ten dates, or
industry margins from a primary source); fallback meanwhile: *lending--deposit spreads of banks across countries, 2019,
against income per person* (WDI `FR.INR.LNDP`, `NY.GDP.PCAP.PP.KD`, `countries_only=True`) --- a margin in one industry,
real data, with its caveats (risk premia). Test: n > 80, spreads positive.

**Other charts**: (2) the Brenland census: profit per unit of output by sector (`firms.csv`, invented) if the fallback is
used.

**Diagrams**: (a) monopoly: $D$, $MR$, $MC$, the price, the DWL; (b) third-degree discrimination in two markets with a
common $MC$; (c) the two-part tariff: fee $=$ CS area, unit price $= MC$; (d) natural monopoly: falling $AC$, $MC$ below,
the loss under $MC$ pricing and the average-cost price.

**Boxes**: `record[Price caps for utilities]` (RPI$-X$ in the UK from the 1980s: what the model said about cost incentives,
what happened; ledger: a primary regulator or a paper); `debate[Have markups risen?]` --- De Loecker--Eeckhout--Unger 2020
against the critiques of the production approach (ledger: Traina 2018 working paper, or Basu 2019, JEP 33(3), "Are price-cost
markups rising in the United States? A discussion of the evidence"), each with its weakness.

**Exercises** (12): ★ monopoly with $p = 100 - q$, $MC = 20$ (C); ★ Lerner index from an elasticity of $-4$ (C); ★ read the
spread of two countries from the chart table (R, data); ★ predict the price in the more elastic of two markets (P). ★★ third-
degree discrimination with two linear demands (C); ★★ welfare: discrimination against a single price on the same numbers (C);
★★ optimal two-part tariff with $q = 10 - p$, $MC = 2$ (C); ★★ bundling with two buyers and negatively correlated values (C);
★★ predict the price after a regulator moves from average-cost pricing to a price cap with $X = 3\%$ and inflation 2\% (P).
★★★ derive $MR = p(1 + 1/\varepsilon)$ and the markup rule; show the monopolist never sets $|\varepsilon| < 1$ (C); ★★★ a
natural monopoly with $C = F + cq$: the second-best price under a zero-profit constraint (Ramsey pricing told) (C, P); ★★★
what observation would refute "markups rose because market power rose" (F).

**Weekend problem**: *The ferry between Brenland and Kestria.* A single operator, two kinds of travellers (residents,
tourists), Part I monopoly price, Part II third-degree discrimination, Part III a season pass as a two-part tariff, Part IV
the regulator's average-cost price and a price cap: profits, surplus and DWL in each regime. Named result: "the deadweight
loss under the single price that discrimination removes: 62\%". 27 questions.

**Ledger**: b1:monopoly-pricing:leslie2004, :deloecker2020, :basu2019, :rpi-x (primary).

### 16. Factor Markets (`16-factor-markets`)

**Programme items**: micro text ch. 26 (factor markets); the minimum wage with one buyer (outline: Y1 re-founds g11's
first look); factor shares.

**Hook**: in a town with one large employer, a higher wage floor can raise employment. When, and by how much?

**Sections**
1. Derived demand --- demand for a factor from the demand for output; the marginal revenue product $MRP = MR \cdot MP$; under
   price taking, the value of the marginal product; the rules of derived demand told (Marshall's rules as a label), the
   one with substitution proved.
2. The single-buyer model --- an upward-sloping labour supply to the firm; the marginal cost of labour; the wage below the
   marginal product, the markdown $\mathrm{MRP}/w - 1 = 1/\varepsilon_{L}$ (derived); employment below the competitive level.
3. A wage floor under one buyer --- between the monopsony wage and the competitive wage, employment rises; above it, falls
   (proved); the maximum gain; why the result needs the floor in the right range.
4. Economic rent and the price of capital --- rent of a factor in fixed supply (recalled from ch. 12); the rental price of
   capital $R = P_K(r + \delta) - \dot P_K$ (derived from no-arbitrage); factor shares and what sets them.

**Definitions owned**: derived demand, marginal revenue product, value of the marginal product (**re-founded**; g11 owns
it), monopsony (*single buyer*), marginal cost of labour, markdown, rental price of capital, factor share (*labour share*
in the same definition).

**Models**: `model{Monopsony}` --- assumes one employer facing an upward-sloping labour supply, one wage for all; predicts a
wage below the marginal revenue product, a markdown set by the supply elasticity, employment that rises with a floor up to
the competitive wage; tested: measured firm-level supply elasticities of about 4 (ledger: Card, Cardoso, Heining and Kline
2018, Journal of Labor Economics 36(S1)), wages lower where employers are concentrated (ledger: Azar, Marinescu and
Steinbaum 2022, Journal of Human Resources 57(S)); breaks: many employers competing for workers, wage discrimination
across workers. The minimum-wage evidence is Y3's `debate` (named in prose).

**Recalls**: labour demand from the value of the marginal product, the minimum wage in two models (g11 `labour-market`);
profit maximisation and factor demands (ch. 11); economic rent (ch. 12); monopoly (ch. 15).

**Opening chart**: *Labour's share of national income against income per person, 2019, about 140 countries* --- PWT 11.0
`labsh` against `rgdpe/pop` (2021 \$ PPP, logarithmic $x$ axis). Replaces the outline's "wages against the concentration of
employers", for which no approved dataset exists (the study's result goes in the `model` box). Test: n > 120, shares in
(0, 1), median between 0.45 and 0.6.

**Other charts**: (2) *Labour share and the self-employed share of employment, 2019* (PWT `labsh`, WDI `SL.EMP.SELF.ZS`):
why a measured labour share depends on how the income of the self-employed is split (a `measure` box topic).

**Diagrams**: (a) competitive factor market and a firm's VMP curve; (b) monopsony: supply, marginal cost of labour, MRP,
the wage and employment; (c) a wage floor in three positions: below the monopsony wage, between, above the competitive wage
(numbers from the chapter's example); (d) the rental price of capital as the flow cost of owning a machine.

**Boxes**: `measure[Labour's share and the self-employed]` (PWT's adjustment; ledger: PWT documentation, labour share
appendix; Gollin 2002, JPE 110(2)); `record[A wage floor in a company town]` --- the model's numbers against a historical
case only if a primary source is found; else none.

**Exercises** (12): ★ MRP with $q = 10L^{0.5}$, $p = 4$ (C); ★ labour share of two countries from the table (R, data); ★
monopsony wage with $w = 2 + 0.1L$, $MRP = 20 - 0.1L$ (C); ★ predict employment after a floor of 12 in that market (P). ★★
the floor that maximises employment, and the gain (C); ★★ markdown from a supply elasticity of 4 (C); ★★ derived demand
elasticity of labour for a Cobb--Douglas firm facing an output demand of elasticity $-2$ (C, P); ★★ rental price of a machine
costing 10,000 with $r = 4\%$, $\delta = 10\%$ and a 2\% price fall (C); ★★ correlation of the labour share and the
self-employed share in the second chart's table (R, C, data). ★★★ derive the markdown formula (C); ★★★ a floor above the
competitive wage under monopsony: the employment loss compared with a competitive market (P); ★★★ what evidence would
separate monopsony from a competitive market with a rising labour supply curve to the industry (F).

**Weekend problem**: *The mill town.* One mill, a labour supply from the valley, Part I the competitive benchmark, Part II
the mill's monopsony, Part III a wage floor and its best level, Part IV a second mill opens: the markdown shrinks. Named
result: "the employment-maximising wage floor: 15 dalens an hour, with 50 more workers". 25 questions.

**Ledger**: b1:factor-markets:card2018, :azar2022, :gollin2002, :pwt-labsh.

### 17. Oligopoly: Cournot and Bertrand (`17-cournot-and-bertrand`)

**Programme items**: micro text ch. 27 (oligopoly); C S2; the leader--follower model.

**Hook**: an isolated town with one dentist, then two, then three: how does the price change, and how many towns does it
take to support a fourth?

**Sections**
1. Cournot competition --- best-response functions in quantities; the equilibrium with two firms (a Nash equilibrium,
   recalled from g11); $n$ firms with linear demand: $q_i = (a - c)/(b(n+1))$; the markup $L = -1/(n\varepsilon)$ for a firm
   with share $1/n$ (derived); the competitive limit as $n \to \infty$ (proved).
2. Bertrand competition --- prices as strategies; two firms with equal costs price at marginal cost (proved); the paradox;
   unequal costs.
3. Capacities and differentiation --- capacity constraints soften Bertrand (told, with the Cournot outcome); differentiated
   products: linear demands, best responses in prices slope up, the equilibrium.
4. The leader--follower model --- Stackelberg: backward induction on the follower's best response; the leader produces more,
   earns more (derived); commitment value.
5. Margins against the number of competitors --- entry thresholds; the evidence from isolated markets and the laboratory.

**Definitions owned**: best-response function, Cournot equilibrium, Bertrand equilibrium, Bertrand paradox (in a `remark`,
indexed), Stackelberg equilibrium (*leader--follower*), strategic substitutes / strategic complements (one definition),
entry threshold. (**Nash equilibrium** is recalled from the grades 10--12 volume and *not re-founded* here, so that Y2
`static-games` owns the general definition: contested term, see the report.)

**Models**: `model{Cournot oligopoly}` --- assumes $n$ identical firms choosing quantities simultaneously, a homogeneous good;
predicts margins falling as $1/n$, approaching marginal cost; tested: entry thresholds in isolated US towns (ledger:
Bresnahan and Reiss 1991, JPE 99(5): most of the fall in margins happens by the third firm); laboratory markets (ledger:
Huck, Normann and Oechssler 2004, JEBO 53(4), "Two are few and four are many"); breaks: when firms can collude (Y2
`repeated-games`), or compete in prices with spare capacity.
`model{Bertrand competition}` --- assumes price competition, a homogeneous good, no capacity limits; predicts price at
marginal cost with two firms; tested: prices fall sharply from one to two sellers in the laboratory (ledger: Dufwenberg and
Gneezy 2000, GEB 30(1)); breaks: prices stay above cost with two sellers in most real markets (differentiation, capacity).

**Recalls**: oligopoly, Nash equilibrium, prisoner's dilemma (g11 `oligopoly-and-games`); monopoly and the Lerner index
(ch. 15).

**Opening chart**: *Prices against the number of sellers in isolated local markets* --- **needs a ruling**: Option A, a
ledger-built table (Bresnahan--Reiss 1991's entry-threshold ratios by industry and number of firms, a published table of
about 15 numbers); fallback meanwhile: *Cournot margins in Brenland's 40 island towns* (a seeded invented table in figdata,
labelled invented), with the published numbers in prose.

**Other charts**: none other.

**Diagrams**: (a) Cournot best responses and their crossing, with the monopoly and competitive points; (b) Bertrand best
responses in prices, the undercutting staircase; (c) differentiated Bertrand best responses sloping up; (d) the Stackelberg
point on the follower's best response.

**Boxes**: `record[Entry in isolated towns]` (Bresnahan--Reiss 1991); `record[Two are few]` (laboratory Cournot and
Bertrand: Huck et al. 2004, Dufwenberg--Gneezy 2000).

**Exercises** (12): ★ Cournot duopoly with $p = 120 - Q$, $c = 30$ (C); ★ Bertrand duopoly with equal costs (C); ★ read
margins for one, two and three sellers from the chart table (R, data); ★ predict the price when a third firm enters a Cournot
market (P). ★★ $n$-firm Cournot: price and total surplus as functions of $n$ (C); ★★ the Lerner index of a Cournot firm with
share $s$ (C); ★★ Bertrand with costs 10 and 12 (C); ★★ Stackelberg on the duopoly numbers: compare outputs and profits (C);
★★ differentiated Bertrand with $q_i = 100 - 2p_i + p_j$ (C). ★★★ prove the competitive limit of Cournot and its rate (C);
★★★ entry thresholds with a fixed cost: the market size for $n$ firms and the ratio $S_{n+1}/S_n$ (C, P); ★★★ what evidence
would refute "the second firm brings the price to marginal cost" (F).

**Weekend problem**: *Ferries to the islands.* Part I one ferry (monopoly), Part II a Cournot duopoly with capacity
choices, Part III a price war (Bertrand) when capacity is ample, Part IV entry: how many passengers a third ferry needs.
Named result: "the market size that supports three ferries: 2.6 times that for one". 26 questions.

**Ledger**: b1:cournot-and-bertrand:bresnahan1991, :huck2004, :dufwenberg2000.

---
## Part V --- Macroeconomics: the long run

### 18. National Accounts in Depth (`18-national-accounts-in-depth`)

**Programme items**: macroeconomics: national accounts (A S2 "comptabilité nationale", C S1 "concepts and measures");
macro text ch. 2.

**Hook**: in 2015 Ireland's real GDP grew by 26\% in one year, and in 2010 Ghana's GDP was revised up by about 60\% in one
day (ledger). Neither economy changed overnight.

**Sections**
1. Sectors and the sequence of accounts --- institutional sectors (households, firms, financial corporations, government,
   rest of the world); production account, generation and distribution of income, use of income; GDP, GNI, disposable
   income; the identities derived from the sequence.
2. Saving, investment and net lending --- for each sector $S - I =$ net lending; the sum over sectors equals minus the rest
   of the world's (proved); the government's deficit and the current account in one table.
3. Volumes and prices --- chain-linked volumes (the chain index from ch. 7 applied); non-additivity of chained components
   (shown on numbers); the deflator.
4. Purchasing-power parities --- how a PPP is built: item prices, a basket, multilateral aggregation (told: the
   international comparison programme); PPP against market exchange rates.
5. What the accounts estimate --- benchmark revisions, rebasing, the informal sector, multinational profits; the size of
   revisions; three national accounts of the same growth (opening chart).

**Definitions owned**: institutional sector, gross national income (**re-founded**? g10 owns "national income"; here *GNI*
and *disposable income* of a sector), net lending (and net borrowing), chain-linked volume, purchasing-power parity
(**re-founded** as the parity of a basket; g9 owns "purchasing-power conversion" --- see report), statistical revision
(*benchmark revision* in the same definition).

**Models**: none in the four-point frame (an accounting chapter); the identities are `proposition`s with proofs, and the
measurement questions go in `measure` boxes.

**Recalls**: GDP, value added, the three approaches, the accounting identities (g8 `gdp`, g10 `national-accounts`); purchasing-
power conversion (g9 `exchange-rates-and-purchasing-power`); chain index (ch. 7).

**Opening chart**: *Two estimates of the same growth: average yearly growth of real GDP per person, 1990--2019, WDI against
PWT, 171 countries* --- WDI `NY.GDP.PCAP.KD`, PWT `rgdpna/pop`, with the 45-degree line; median absolute gap 0.13 points,
18\% of countries more than half a point apart (probe; the table governs). Replaces the outline's "first estimates of
quarterly GDP growth against the final figures" (Data to approve: a real-time data set). Test: n > 150, median gap below 0.3.

**Other charts**: (2) *Net lending by sector, euro area or one country, 1999--2023* --- Eurostat `gov_10dd_edpt1` (B9 of S13,
per cent of GDP) and the current account (WDI `BN.CAB.XOKA.GD.ZS`); households and firms from the identity are not in the
approved data, so the chart shows government and the rest of the world only, said so. (3) *Price level against income
per person, 2021* (WDI `PA.NUS.PRVT.PLI`, `NY.GDP.PCAP.PP.KD`): why PPP and market rates differ (prepares ch. 27).

**Diagrams**: (a) the sequence of accounts as a waterfall from output to disposable income to saving; (b) the sector
balances as a closed circuit (net lending sums to zero with the rest of the world); (c) chained against fixed-base
volumes on a two-good example.

**Boxes**: `measure[Chain-linked volumes]`; `measure[Building a PPP]` (ICP 2021, ledger: World Bank ICP page);
`record[Ireland 2015 and Ghana 2010]` (ledger: CSO Ireland release; Ghana Statistical Service rebasing release) ---
what the accounts estimate rather than observe; `record[How large are revisions?]` (ledger: BEA, Fixler et al., Survey of
Current Business, the mean absolute revision of quarterly growth).

**Exercises** (12): ★ GNI from GDP and net primary income (C); ★ net lending of three sectors that sum to the current
account (C); ★ read the five largest WDI--PWT gaps from the table (R, data); ★ predict the sign of the government's net
lending in a recession (P). ★★ a chained volume index for two goods over three years, and the non-additivity (C); ★★ GDP in
PPP from a three-good basket (C); ★★ Brenland `accounts.csv`: real GDP growth, deflator, and the identity check (C, data);
★★ predict the change in measured GDP after a firm moves its intellectual property into the country (P); ★★ the price level
of a country with given PPP and market rate (C). ★★★ prove that sectoral net lending sums to minus the rest of the world's
(C); ★★★ show that fixed-base volumes overstate growth when quantities shift to goods whose prices fall (C); ★★★ what
observation would show that a country's growth is mismeasured rather than slow (F).

**Weekend problem**: *Brenland's statistician rebases the accounts.* `accounts.csv` throughout. Part I the sequence of
accounts for 2025, Part II sector balances and the current account, Part III chain-linking 2015--2025 and the gap to fixed
2015 prices, Part IV an informal sector added at the rebasing: the new level and the unchanged growth. Named result: "the
rebasing raises 2025 GDP by 14\% but growth 2015--2025 by only 0.1 points a year". 25 questions.

**Ledger**: b1:national-accounts-in-depth:ireland-2015 (CSO), :ghana-2010 (GSS), :fixler-revisions (BEA), :icp-2021 (World
Bank).

### 19. The Long-Run Model (`19-long-run-model`)

**Programme items**: macroeconomics 1: the long run (University B, S1); macro text ch. 3 (national income: where it comes
from and where it goes).

**Hook**: for seventy years, about three-fifths of national income in rich countries has gone to labour, though output per
worker rose four- or fivefold.

**Sections**
1. Output from the factors --- $Y = F(K, L)$ with constant returns; supplies taken as given in the long run.
2. Factor prices --- competitive firms pay marginal products: $w = F_L$, $r = F_K$ (from ch. 11); Euler's theorem: $F_K K + F_L L
   = Y$ (recalled from ch. 9); Cobb--Douglas shares $\alpha$ and $1-\alpha$; the labour share in the data.
3. Uses of output --- $Y = C + I + G$ (closed); consumption from disposable income; investment from the real interest rate;
   $G$ and $T$ given.
4. The market for loanable funds --- national saving $S = Y - C - G$ equals $I(r)$; the equilibrium $r$; a rise in $G$
   crowds out investment one for one in this model (derived); a tax cut; a shift in investment demand.
5. Money apart --- real variables set without money; the price level from money (preview of ch. 23); where the model breaks:
   the short run.

**Definitions owned**: long-run model (`model` box and a definition of *the long-run equilibrium*), loanable funds market
(*national saving*, *private saving*, *public saving* in one definition; **re-founds** g12's saving and investment), crowding
out (**re-founded**; g12 owns the word), monetary neutrality (*neutrality of money*: real variables do not depend on the
money supply).

**Models**: `model{The long-run model}` --- assumes flexible prices and wages, full employment of given $K$ and $L$, a closed
economy, competitive factor markets; predicts factor shares set by technology, $r$ that clears loanable funds, full crowding
out, money neutral; tested: labour shares stable for decades (opening chart, with their recent fall: ledger Karabarbounis and
Neiman 2014, QJE 129(1), a fall of about 5 points worldwide since 1975), money neutral in the long run (ch. 23); breaks: the
short run (Part VI), open economies (ch. 27), the decline of labour shares since 1980 contradicts constant Cobb--Douglas
shares.

**Recalls**: the aggregate production function, capital's share (g12 `growth-and-production-function`); saving and
investment, crowding out (g12 `saving-and-investment`); the long-run model in words (g12 `aggregate-demand-and-supply`); Euler's
theorem (ch. 9); profit maximisation (ch. 11); factor shares (ch. 16).

**Opening chart**: *Labour's share of national income, 1950--2023, France, Germany, Japan, the United Kingdom, the United
States* --- PWT 11.0 `labsh`. Seventy-three years (not the outline's century: PWT starts in 1950). Test: five series, 74 rows
each, all shares in (0.4, 0.8).

**Other charts**: (2) *Investment and the real interest rate, United States, 1950--2020* (JST `iy` and `ltrate` minus
inflation): loanable funds in the data --- a cloud, recalling ch. 1's identification lesson.

**Diagrams**: (a) the circular flow of the long-run model with the loanable funds market; (b) loanable funds: $S$ vertical at
$Y - C(Y - T) - G$, $I(r)$ downward, the effect of a rise in $G$; (c) the factor market: $F_L(K, L)$ and the vertical labour
supply.

**Boxes**: `record[The fall of the labour share]` (Karabarbounis--Neiman 2014; the measurement debate: self-employed and
housing, ledger Gollin 2002 recalled); `measure[Labour's share in the Penn World Table]` (recalled from ch. 16 briefly).

**Exercises** (12): ★ factor prices with $Y = 10K^{0.3}L^{0.7}$, $K = 100$, $L = 400$ (C); ★ read the labour share of two
countries in 1950 and 2023 (R, data); ★ check Euler's theorem on those numbers (C); ★ predict $r$ after a rise in $G$ (P). ★★
loanable funds equilibrium with $C = 100 + 0.6(Y - T)$, $I = 500 - 20r$ (C); ★★ a tax cut of 50: $r$, $I$, $C$ (C); ★★ an
immigration wave raises $L$ by 10\%: predict $w$, $r$, the shares (P); ★★ the trend in the labour share 1980--2023 per decade
from the table (R, C, data); ★★ Brenland: national saving and investment from `accounts.csv` (C, data). ★★★ show that with CES
and $\sigma < 1$ a rise in $K/L$ raises the labour share (C, P); ★★★ derive the full crowding-out result and what an
interest-sensitive saving changes (C); ★★★ what observation would refute monetary neutrality in the long run (F).

**Weekend problem**: *Brenland in the long run.* Calibrated to `accounts.csv` (2025). Part I factor prices and shares, Part II
loanable funds and the real rate, Part III a defence build-up of 2\% of GDP: crowding out, Part IV a technology gain: wages,
rates and shares. Named result: "the defence build-up raises the real interest rate by 0.8 points and crowds out
investment one for one". 24 questions.

**Ledger**: b1:long-run-model:karabarbounis2014, :gollin2002 (shared with ch. 16, cite ch. 16's row).

### 20. The Solow Model (`20-solow-model`)

**Programme items**: macro text ch. 8--10 (capital accumulation, population growth and technological progress, growth
empirics); B S1 (long run).

**Hook**: countries that invest a quarter of their output are, on average, far richer than those that invest a tenth. Is
investment the cause, and how much of the gap can it explain?

**Sections**
1. The model in continuous time --- $\dot k = s f(k) - (n + \delta)k$ (derived from $\dot K = sY - \delta K$); the phase line;
   the steady state, its existence and stability (proved for Cobb--Douglas and for any $f$ with Inada conditions).
2. Comparative statics of the steady state --- $k^* = (s/(n+\delta))^{1/(1-\alpha)}$; $s$ raises the level not the growth rate;
   elasticity of $y^*$ to $s$ is $\alpha/(1-\alpha)$ (derived).
3. The golden rule --- the $s$ that maximises steady-state consumption: $f'(k) = n + \delta$ (proved); dynamic efficiency.
4. The speed of convergence --- linearising: $\dot{\ln y} \approx -\lambda(\ln y - \ln y^*)$, $\lambda = (1-\alpha)(n+\delta)$
   (derived); half-life; the predicted $\lambda$ against the measured 2\% a year.
5. Technical progress and balanced growth --- labour-augmenting $A$ growing at $g$; per effective worker; balanced growth
   path (proved); the model to data: the cross-country regression with human capital added (Mankiw--Romer--Weil as a label);
   what it explains and what it does not.

**Definitions owned**: steady state (**re-founded** in continuous time; g12 owns it), golden-rule capital stock, dynamic
inefficiency, speed of convergence (and half-life), balanced growth path, capital per effective worker, conditional
convergence (**re-founds** g12's "convergence"; Y3 `growth-empirics` recalls), Inada conditions.

**Models**: `model{The Solow model}` --- assumes a closed economy, constant saving rate, exogenous $n$, $\delta$, $g$, constant
returns and diminishing returns to capital; predicts steady-state income rising with $s$ and falling with $n$, conditional
convergence, growth in the long run only from $g$; tested: the augmented model fits about 78\% of cross-country income
variance with plausible shares (ledger: Mankiw, Romer and Weil 1992, QJE 107(2)), convergence at about 2\% a year (ledger:
Barro and Sala-i-Martin 1992, JPE 100(2)); breaks: $g$ is unexplained (Y2 `endogenous-growth`), the basic model needs a
capital share near 0.6 to fit, capital does not flow to poor countries (Y3).

**Recalls**: the Solow model as a recurrence, steady state, convergence (g12 `solow-first-look`); differential equations
(mathematics g12, Year 1); the long-run model (ch. 19).

**Opening chart**: *GDP per person in 2019 against the average investment share 1960--2019, about 180 countries* --- PWT 11.0
`rgdpe/pop` (2021 \$ PPP, logarithmic axis) and `csh_i` averaged (correlation of $\ln y$ with $s$ about 0.35 on the probe;
the table governs). Test: n > 150.

**Other charts**: (2) *Predicted against actual GDP per person, the augmented Solow model, 2019* (PWT `csh_i`, `pop`
growth, `hc`, $\delta = 0.05$ as in the cited paper's convention; fitted by the tested script in `exercises/`, the regression
recalled from ch. 32 by a forward pointer: the chapter prints the fitted shares only). (3) *Growth 1960--2019 against
income in 1960 for the OECD's 1960 members and for all countries* --- conditional and absolute convergence. The g12
opening chart is the same idea: check Book 2's chart list at the sync and drop (3) if it duplicates.

**Diagrams**: (a) $sf(k)$ and $(n + \delta)k$ with the steady state and the phase arrows (numbers from $\alpha = 1/3$,
$s = 0.2$, $n + \delta = 0.06$); (b) a rise in $s$: the transition path of $\ln y$ over time; (c) the golden rule: $f(k)$,
$(n+\delta)k$, consumption maximal where slopes are equal; (d) the phase line $\dot k$ against $k$.

**Boxes**: `record[Postwar recoveries]` (Germany and Japan's growth after 1945 as a convergence test, Maddison data; recalled
from g12 briefly, no reprint); `measure[Human capital in the Penn World Table]` (the `hc` index from years of schooling and a
return; ledger: PWT documentation).

**Exercises** (12): ★ steady state $k^*$ and $y^*$ with given $s, n, \delta, \alpha$ (C); ★ read the incomes of the two highest-
investment countries from the table (R, data); ★ predict the long-run growth rate after $s$ rises (P); ★ golden-rule $s$ for
Cobb--Douglas (C). ★★ half-life of convergence with $\alpha = 1/3$, $n + \delta = 0.07$ (C); ★★ elasticity of $y^*$ to $s$
and the predicted income ratio of two countries with $s = 0.25$ and $0.10$ (C, P); ★★ with technical progress: growth of $Y$,
$Y/L$, $K/Y$ on the balanced path (C); ★★ dynamic inefficiency: show a country above the golden rule can raise consumption
at all dates (C); ★★ the augmented model's prediction for one country against its actual income (R, C, data). ★★★ prove
global stability of the steady state for Cobb--Douglas by solving the differential equation in $k^{1-\alpha}$ (C); ★★★
derive the speed of convergence by linearisation (C); ★★★ what cross-country evidence would refute the Solow model's
explanation of income gaps (F).

**Weekend problem**: *Kestria after the war.* Part I steady state of the prewar economy, Part II the capital stock halved:
the transition and its half-life, Part III a saving reform to the golden rule: consumption along the path, Part IV
technical progress and the balanced path. Named result: "Kestria recovers half its gap in 17 years". 26 questions.

**Ledger**: b1:solow-model:mrw1992, :barro1992, :pwt-hc.

### 21. Growth and Development Accounting (`21-growth-accounting`)

**Programme items**: macro text ch. 9--10 (growth empirics and policy); the outline's planned-economy data (user ruling).

**Hook**: from 1966 to 1990 Singapore's output grew about 8\% a year. Most of it came from more capital and more workers,
not from doing more with them (ledger).

**Sections**
1. The Solow residual --- $g_Y = \alpha g_K + (1-\alpha)(g_L + g_H) + g_A$ (derived from the production function); measuring
   each term; the residual as "a measure of our ignorance".
2. The sources of growth --- eight economies 1960--2019 (opening chart); fast growers: East Asia; the debate on how much was
   accumulation.
3. Levels accounting --- $y = A k^\alpha h^{1-\alpha}$ in levels; how much of the income gap is capital, schooling and
   productivity (development accounting, the ratio $\mathrm{Var}(\ln y_{KH})/\mathrm{Var}(\ln y)$); most of it is productivity.
4. Misallocation --- the same factors, badly allocated across firms, lower aggregate productivity (a two-firm example
   proved); the measured gains from reallocation.
5. Planned economies as data --- high investment, low productivity growth (the Soviet Union in the accounts, ledger);
   China before and after 1978 in PWT; institutions as a deeper cause, the subject of Y3 `institutions` (named in prose).

**Definitions owned**: growth accounting (**re-founded**; g12 owns "growth accounting with logarithms" --- see report), Solow
residual, total factor productivity (**re-founded** if g12 defines it; else owned here), development accounting (*levels
accounting*), misallocation.

**Models**: `model{Growth accounting}` --- assumes a Cobb--Douglas aggregate technology, competitive factor shares, measured
inputs; predicts the decomposition of growth (an accounting, not a cause); tested: East Asian growth mostly from
accumulation (ledger: Young 1995, QJE 110(3)); development accounting gives productivity the larger part of income gaps
(ledger: Caselli 2005, Handbook of Economic Growth 1A, ch. 9, or Hall and Jones 1999, QJE 114(1)); misallocation: China's and
India's productivity would rise by 30--50\% and 40--60\% with US-level allocation (ledger: Hsieh and Klenow 2009, QJE
124(4)); breaks: shares not constant, mismeasured capital and quality, the residual absorbs all errors.

**Recalls**: growth accounting with logarithms (g12 `growth-and-production-function`); institutions and the three natural
experiments (g9 `institutions-and-prosperity`, g12 `ideas-institutions-growth`); the Solow model (ch. 20).

**Opening chart**: *Growth of output split into capital, labour, human capital and productivity, eight economies,
1960--2019* --- PWT 11.0: `rgdpna`, `rnna`, `emp`, `avh` (where present), `hc`, `labsh` (Törnqvist shares: average of
adjacent years) for CHN (from 1960; the 1952 start shown in the second chart), KOR, JPN, USA, DEU, IND, BRA, SGP; stacked
bars. Test: for each country the four parts sum to output growth within 0.01 points.

**Other charts**: (2) *China: output, capital and TFP per worker, 1952--2019* (PWT `rgdpna`, `rnna`, `emp`, `rtfpna`, the
1978 reform marked); (3) *Development accounting: actual income against the income predicted from $K$ and $H$ alone,
2019* (PWT `cgdpo`, `cn`, `hc`, `emp`), the 45-degree line.

**Diagrams**: (a) the growth-accounting identity as a stacked bar with its terms; (b) misallocation: two firms with
different marginal products, output gained by moving a worker.

**Boxes**: `record[The Soviet economy in the accounts]` (ledger: Easterly and Fischer 1995, World Bank Economic Review
9(3)); `record[China after 1978]` (PWT-based; the 1978 date and the household responsibility system from a ledger row; the
outcome of the reform in the data, no history narrative); `debate[How much of East Asian growth was productivity?]` (Young
1995 against Hsieh 2002, AER 92(3), dual (price-based) estimates; each with its weakness).

**Exercises** (12): ★ the Solow residual from $g_Y = 4\%$, $g_K = 6\%$, $g_L = 1\%$, $\alpha = 0.35$ (C); ★ read the TFP share
of two countries from the opening chart table (R, data); ★ predict growth per worker in a steady state with $g_A = 1.5\%$
(P); ★ which term changed most in China after 1978 (R, data). ★★ development accounting for two countries from given $k, h$,
$y$ (C); ★★ the misallocation gain in a two-firm example (C); ★★ growth accounting with hours: the difference made by $avh$
(C, data); ★★ predict the residual's bias if capital quality improves and is not measured (P); ★★ the share of the
cross-country variance of $\ln y$ explained by $K$ and $H$ in the third chart's table (R, C, data). ★★★ derive the Törnqvist
decomposition and its error against the continuous one (C); ★★★ show that under the Solow model a TFP rise also raises $K$, so
growth accounting understates TFP's role (C, P); ★★★ what observation would refute "planned economies grew by accumulation
alone" (F).

**Weekend problem**: *Brenland's growth review.* From `accounts.csv` and the firm census. Part I growth accounting 2000--2025,
Part II the residual and its uncertainty with two values of $\alpha$, Part III misallocation in the census: output gained by
equalising marginal products, Part IV a comparison with Kestria in levels. Named result: "equalising marginal products in
Brenland's census would raise output by 11\%". 26 questions.

**Ledger**: b1:growth-accounting:young1995, :hsieh2002, :caselli2005, :hall1999, :hsieh2009, :easterly1995, :china-1978.

### 22. Unemployment: Stocks and Flows (`22-unemployment-flows`)

**Programme items**: macro text ch. 7 (unemployment and the labour market); the steady-state rate from flows; efficiency
wages and bargaining.

**Hook**: in a typical month in the United States, millions of people lose or leave a job and millions find one, while the
unemployment rate barely moves (ledger).

**Sections**
1. Flows and the steady state --- separation rate $s$, job-finding rate $f$; $\dot u = s(1 - u) - fu$; steady state $u^* = s/(s +
   f)$ (derived), convergence speed $s + f$; which flow moves unemployment in recessions.
2. Duration --- expected duration $1/f$ with a constant rate; duration dependence; long-term unemployment.
3. Why wages stay above the clearing level --- efficiency wages (the shirking model in a simple form, derived no-shirking
   condition); bargaining and unions (Nash bargaining told as a split of the surplus); minimum wages (ch. 16 recalled).
4. The Beveridge curve --- vacancies against unemployment; movements along (cycle) and shifts (matching efficiency); the
   matching function is Y2's (`search-and-unemployment`, named in prose).
5. Benefits and hiring rules as evidence --- the measured effects of benefit duration and of firing costs; what they do to
   $s$ and $f$.

**Definitions owned**: separation rate, job-finding rate, steady-state unemployment rate (**re-founds** g11's natural rate
in flow form), unemployment duration (expected), efficiency wage, no-shirking condition, Beveridge curve (owned here, Y2
recalls: contested, see the report).

**Models**: `model{The flow model of unemployment}` --- assumes constant separation and job-finding rates, a fixed labour
force; predicts $u^* = s/(s + f)$ and fast convergence to it; tested: the steady-state rate tracks the actual rate closely in
US monthly data, and most of the cyclical rise comes from lower job finding (ledger: Shimer 2012, Review of Economic Dynamics
15(2)); breaks: participation flows ignored, rates vary with duration.
`model{Efficiency wages}` --- assumes effort that falls when the cost of job loss is low; predicts wages above clearing,
involuntary unemployment, lower turnover at high-wage firms; tested: a car maker's doubled wage in 1914 cut quits and
absenteeism (ledger: Raff and Summers 1987, Journal of Labor Economics 5(4)); breaks: it does not explain why wages do not
fall more in deep recessions.

**Recalls**: unemployment and participation rates, the survey (g8 `jobs-wages-unemployment`); flows, the natural rate, why wages
do not clear (g11 `unemployment`); the first-order linear differential equation (mathematics); monopsony and wage floors
(ch. 16).

**Opening chart**: *Unemployment rate, United States, 1890--2020, and the euro area's countries 2000--2024* --- JST R6
`unemp` (USA) for the long series; Eurostat `une_rt_a` for a European panel. Replaces the outline's "job-finding and
separation rates through four cycles" (Data to approve: BLS labour-force flows); with that dataset approved, the flows
chart becomes the opening chart and this one moves to the second place. Test: the US 1933 value above 20\%, series complete
from 1948.

**Other charts**: (2) *Unemployment rates of 15--24-year-olds against all ages, European countries, 2023* (Eurostat
`une_rt_a`, age `Y15-24` and `Y15-74`).

**Diagrams**: (a) the bathtub of flows: employed and unemployed pools with $s$ and $f$ arrows; (b) the steady state as the
crossing of inflow and outflow lines in $u$; (c) the no-shirking condition against labour demand; (d) a Beveridge curve with a
movement along and a shift.

**Boxes**: `record[Five dollars a day]` (Raff--Summers 1987); `debate[Do longer benefits lengthen unemployment?]` (ledger:
Schmieder, von Wachter and Bender 2012, QJE 127(2), against Card, Chetty and Weber 2007, QJE 122(4), the liquidity
channel; each with its weakness); `measure[The flow data]` (how labour-force status flows are matched month to month;
ledger: BLS page).

**Exercises** (12): ★ $u^*$ with $s = 2\%$, $f = 28\%$ a month (C); ★ expected duration with $f = 25\%$ (C); ★ read the US
rate in 1933, 1982, 2009 and 2020 from the table (R, data); ★ predict $u^*$ after $f$ falls to 20\% (P). ★★ the half-life of
convergence to $u^*$ (C); ★★ which flow moved more: given two months of $s$ and $f$ (R, C); ★★ the no-shirking wage with given
detection rate and discount rate (C); ★★ predict the effect on $u^*$ of a firing cost that lowers both $s$ and $f$ by 20\% (P);
★★ youth against all-age rates: the ratio by country from the second chart (R, C, data). ★★★ solve $\dot u = s(1-u) - fu$
and show convergence at rate $s + f$ (C); ★★★ a two-state model with participation: derive the steady-state rate (C); ★★★ what
observation would refute "recessions raise unemployment mainly through more separations" (F).

**Weekend problem**: *Brenland's labour market after a factory closes.* Part I flows and the steady state from
`accounts.csv` (calibrated $s$ and $f$), Part II a one-off layoff: the path back, Part III efficiency wages at the new
employer, Part IV a benefit reform that lowers $f$: the new $u^*$ and its half-life. Named result: "the reform raises the
steady-state rate from 6.7\% to 7.9\%". 25 questions.

**Ledger**: b1:unemployment-flows:shimer2012, :raff1987, :schmieder2012, :card2007, :bls-flows-scale (monthly flows in
millions, BLS page), :bls-flows-method.

### 23. Money and Inflation (`23-money-and-inflation`)

**Programme items**: macro text ch. 4--5 (the monetary system; inflation: its causes, effects and costs); the money-growth
propositions scored (outline); B S1.

**Hook**: the ratio of US nominal GDP to the broad money stock hovered near 1.8 for decades, then fell to about 1.2 in
2020 (JST). The quantity equation still holds as an identity. What broke?

**Sections**
1. Money demand --- real balances $M/P = L(i, Y)$; the opportunity cost $i$; a log-linear form and its elasticities; velocity as
   $1/L$ per unit of income.
2. The quantity theory --- $MV = PY$ as an identity, then as a theory with stable $V$; in growth rates $\pi = g_M + g_V - g_Y$;
   the long-run link across countries and decades.
3. The money-growth propositions scored --- (i) long-run link of money and prices: holds (high-inflation evidence); (ii)
   effects with long and variable delays: holds; (iii) money-growth targets: failed when velocity moved (the 1980s,
   financial innovation); a fixed money-growth rule's record. Each with its test.
4. The inflation tax and hyperinflation --- seigniorage $\pi \cdot M/P$; the Laffer curve of the inflation tax; money demand in
   a hyperinflation: real balances collapse as expected inflation rises (Cagan's money demand as a label), the
   revenue-maximising inflation rate (derived).
5. The Fisher effect --- $i = r + \pi^e$ (re-founded); the evidence over long horizons; costs of inflation (shoe-leather,
   menu, tax distortions, uncertainty).

**Definitions owned**: money demand function, velocity of money (**re-founded**; g12 owns the quantity equation), quantity
theory of money (as a theory: stable velocity; *quantity equation* stays g12's), seigniorage, inflation tax,
hyperinflation (**re-founded**? g12 uses it --- see report), Fisher effect.

**Models**: `model{The quantity theory}` --- assumes velocity stable or predictable, output set by real factors; predicts
inflation equal to money growth minus output growth in the long run; tested: across countries over decades the
money-growth--inflation correlation is about 0.95 (ledger: McCandless and Weber 1995, FRB Minneapolis Quarterly Review 19(3));
breaks: at low inflation, velocity moves (opening chart), and money-growth targeting was abandoned by the Federal Reserve in
the 1980s (ledger: Federal Reserve primary source).
`model{Money demand in a hyperinflation}` --- assumes real balances falling exponentially with expected inflation; predicts
a revenue-maximising inflation rate $1/\alpha$ and that governments in hyperinflation exceed it; tested: real balances fell
as inflation rose in Bolivia 1984--85, Peru and Brazil (second chart, WDI); breaks: expectations that jump at
stabilisation.

**Recalls**: money and its functions, money creation, central bank (g7, g11 `money-and-banking`); the quantity equation,
hyperinflations, real and nominal rates (g12 `inflation-and-money`); the long-run model and neutrality (ch. 19).

**Opening chart**: *Velocity of broad money, 1950--2020, United States, the United Kingdom, Germany, Japan* --- JST R6
`gdp/money`. Test: US 2020 value below 1960 value; four series.

**Other charts**: (2) *Broad money as a share of GDP against inflation, Bolivia, Peru and Brazil, 1980--1995, logarithmic
inflation axis* --- WDI `FM.LBL.BMNY.GD.ZS`, `FP.CPI.TOTL.ZG`. (3) *Short-term interest rate against inflation, 18
economies, decade averages 1870--2020* (JST `stir`, `cpi`): the Fisher effect over long horizons.

**Diagrams**: (a) money market: money demand $L(i, Y)$ and a vertical supply; (b) the inflation-tax Laffer curve,
revenue against $\pi$ for the calibrated money demand; (c) the price level under a step in money growth (path of $P$, $M$,
$i$).

**Photograph**: a 1923 German Reichsbank note or a Hungarian 1946 pengő note (Commons, licence page read --- public domain
by age only if stated).

**Boxes**: `record[Velocity in the 1980s]` (financial innovation and the end of money-growth targets; what the model said;
ledger: Fed); `record[Bolivia 1985]` (stabilisation after hyperinflation: the inflation rate and its end; ledger: Sachs 1987,
AER P&P 77(2), "The Bolivian hyperinflation and stabilization"); `measure[Broad and narrow money]` (JST's `money` and
`narrowm`; ledger: JST documentation).

**Exercises** (12): ★ inflation from $g_M = 8\%$, $g_Y = 3\%$, constant $V$ (C); ★ read US velocity in 1960, 2000 and 2020 (R,
data); ★ seigniorage with $\pi = 20\%$ and $M/P = 10\%$ of GDP (C); ★ predict the nominal rate after expected inflation rises
3 points (P). ★★ log-linear money demand: elasticity of velocity to $i$ (C); ★★ revenue-maximising inflation with
$M/P = Ye^{-\alpha\pi}$, $\alpha = 2$ (C); ★★ real balances in Bolivia at two inflation rates from the second chart (R, C, data);
★★ predict inflation in a country where $g_M = 6\%$, $g_Y = 2\%$ and velocity falls 1\% a year (P); ★★ the Fisher relation over
decades from the third chart: slope of $i$ on $\pi$ (R, C, data). ★★★ derive the revenue-maximising inflation rate and show
it does not depend on $Y$ (C); ★★★ steady inflation under a money-growth rule with velocity shocks: variance of inflation
(C, P); ★★★ what evidence would refute "inflation is always caused by money growth" at low inflation, and why the
long-run cross-country link survives it (F).

**Weekend problem**: *Kestria's printing press.* Part I money demand and velocity, Part II a deficit financed by money: the
inflation that pays for it, Part III the Laffer curve and the maximum revenue, Part IV a stabilisation: fiscal reform and a
new currency, the jump in real balances. Named result: "the largest deficit Kestria can finance by printing: 3.7\% of
GDP". 25 questions.

**Ledger**: b1:money-and-inflation:mccandless1995, :fed-targets, :sachs1987, :jst-money-docs.

---
## Part VI --- The short run

### 24. The IS--LM Model (`24-is-lm`)

**Programme items**: macroeconomics 2: the short run (University B, S2); macro text ch. 11--13 (fluctuations, IS--LM I and II).

**Hook**: from December 2008 to December 2015 the Federal Reserve's policy rate sat between 0 and 0.25\% (ledger), while the
money in the banking system multiplied. Why did more money not lower the rate further?

**Sections**
1. The goods market and the IS curve --- planned spending $C(Y - T) + I(r) + G$; equilibrium; the IS curve, its slope
   $\dd r/\dd Y = (1 - C')/I'$ (derived); shifts by $G$, $T$; the multiplier recalled from g12 and its size here.
2. The money market and the LM curve --- $M/P = L(r, Y)$ with $P$ fixed; the LM curve, its slope $-L_Y/L_r$; shifts by $M$.
3. Equilibrium and policy --- solving the two equations (linear case in closed form; general case by implicit
   differentiation, ch. 3); fiscal and monetary multipliers; crowding out partial (proved $0 < \dd Y/\dd G < 1/(1 - C')$).
4. The liquidity trap --- a horizontal LM at the floor on $r$; money has no effect, fiscal policy no crowding out; the
   record of 2008--2015.
5. The version with an interest-rate rule --- the central bank sets $r$: an MP curve replaces LM; shocks and responses;
   this is how central banks describe themselves (prepares Y2 `three-equation-model`).
6. The toy model in its frame --- fixed $P$, closed, no expectations; the sign tests and where it breaks.

**Definitions owned**: IS curve, LM curve, IS--LM model (indexed in the `model` box), liquidity trap (*zero lower bound*
in the same definition), MP curve (*interest-rate rule* in the same definition), fiscal multiplier (in IS--LM; the
*multiplier* is g12's). The transmission of monetary policy is named in prose only (Y3 `central-banking`).

**Models**: `model{IS--LM}` --- assumes a fixed price level, a closed economy, no expectations, money supply or the interest
rate set by the central bank; predicts a fiscal expansion raises $Y$ and $r$ (LM) or $Y$ alone (MP), a money expansion
lowers $r$ and raises $Y$ except in a trap; tested: signs of responses to identified monetary shocks (ledger: Romer and
Romer 2004, AER 94(4)), the ineffectiveness of base-money growth at the zero lower bound (opening chart); breaks: prices that
move (ch. 25), open economies (ch. 27), expectations (Y2), financial frictions (2008; Y2 `banks-and-crises`). Taught as a
toy model: the size of its multipliers is not to be trusted (ch. 26's `debate`).

**Recalls**: the Keynesian cross and the multiplier, its limits and the refuted large fixed multiplier (g12 `keynesian-cross`);
the policy rate (g12 `monetary-policy`); money demand (ch. 23); loanable funds (ch. 19); implicit differentiation (ch. 3).

**Opening chart**: *Short-term interest rates and narrow money, 2000--2020, United States, the United Kingdom, Japan,
Germany* --- JST R6 `stir` (per cent) and `narrowm` (index 2007 = 100, logarithmic right axis). JST holds narrow money, not
central-bank money as the outline proposes (Data to approve: a central-bank balance-sheet series); the caption says
"narrow money". Test: every country's 2015 `stir` below 1\%; `narrowm` 2015 above 2007.

**Other charts**: none from data.

**Diagrams**: (a) the Keynesian cross deriving the IS curve (two panels); (b) the money market deriving LM (two panels);
(c) IS--LM with a fiscal and a monetary shift (numbers from the chapter's linear example); (d) the liquidity trap: a kinked
LM and two IS curves; (e) IS--MP.

**Boxes**: `record[The zero lower bound, 2008--2015]` (Fed funds target 0--0.25\% from 16 December 2008 to 16 December 2015,
ledger: Federal Reserve press releases; Japan from 1999, ledger: Bank of Japan); `measure[A policy rate and a market rate]`
(short: the policy rate is an overnight rate, market rates add term and risk premia).

**Exercises** (12): ★ IS curve with $C = 50 + 0.75(Y - T)$, $I = 300 - 25r$, $G = T = 100$ (C); ★ LM curve with $M/P = 500$,
$L = Y - 100r$ (C); ★ read the 2007 and 2015 rates from the chart table (R, data); ★ predict the sign of $\Delta r$ after a rise
in $G$ under LM and under MP (P). ★★ the equilibrium and the fiscal multiplier on those numbers (C); ★★ the monetary
multiplier (C); ★★ a liquidity trap at $r = 0$: the effect of doubling $M$ (C, P); ★★ IS--MP: a fall in confidence
lowers $I$ by 40; the rate cut that restores $Y$ (C); ★★ narrow money growth 2007--2015 by country (R, C, data). ★★★ derive
the general multipliers by implicit differentiation and sign them (C); ★★★ when does crowding out vanish and when is it
complete, in the slopes of IS and LM (C, P); ★★★ what observation in 2008--2015 would have refuted the liquidity-trap
prediction (F).

**Weekend problem**: *Brenland's recession of 2025.* An IS--LM economy calibrated to `accounts.csv`. Part I IS and LM, Part
II a fall in exports (IS shift), Part III monetary and fiscal answers, Part IV the rate hits zero: what each policy can
still do. Named result: "at the zero bound, the fiscal multiplier rises from 1.1 to 2.5 in the toy model --- and why
that number is the model's, not the economy's". 26 questions.

**Ledger**: b1:is-lm:fed-zlb-2008, :fed-liftoff-2015, :boj-zirp-1999, :romer2004.

### 25. Aggregate Supply and the Phillips Curve (`25-aggregate-supply`)

**Programme items**: macro text ch. 15 (aggregate supply and the short-run trade-off); B S2.

**Hook**: in the United States between 1960 and 2019, years of low unemployment were followed by rising inflation, years of
high unemployment by falling inflation. The level of inflation said almost nothing.

**Sections**
1. Three short-run supply stories --- sticky wages, sticky prices, imperfect information; each gives $Y = \bar Y + a(P - P^e)$
   (derived for sticky prices with a share of firms that cannot adjust).
2. AD--AS --- aggregate demand from IS--LM with $P$ free (derived); short-run and long-run equilibrium; a demand shock and a
   supply shock; the return to $\bar Y$ as $P^e$ adjusts.
3. The expectations-augmented Phillips curve --- $\pi = \pi^e - \beta(u - u^n) + v$ from Okun's law and AS (derived); no
   long-run trade-off.
4. Adaptive expectations --- $\pi^e_t = \pi_{t-1}$; holding $u$ below $u^n$ makes inflation accelerate (proved); estimating
   $u^n$ from $\Delta\pi$ against $u$ (opening chart).
5. The cost of disinflation --- the sacrifice ratio; gradual and fast disinflation; the Volcker disinflation as a test;
   what credibility changes (Y2 `expectations-and-lucas-critique`, named in prose).
6. The record --- the 1960s curve, the 1970s breakdown, anchoring after 1990, the flat curve, 2021--23.

**Definitions owned**: short-run aggregate supply curve, aggregate demand curve (**re-founded** from IS--LM; g12 owns
"aggregate demand" in words), Okun's law (`proposition`-like empirical rule, indexed as a label), expectations-augmented
Phillips curve, adaptive expectations (Y2 owns *rational expectations*), sacrifice ratio, supply shock (**re-founded**? g12
owns "demand shock, supply shock" --- see report).

**Models**: `model{The expectations-augmented Phillips curve}` --- assumes expectations formed from past inflation, a natural
rate set by real factors; predicts accelerating inflation when $u < u^n$, no long-run trade-off, a disinflation costing
unemployment; tested: the stagflation of the 1970s refuted the stable trade-off; $\Delta\pi$ against $u$ gives $u^n \approx 6\%$
for the US 1960--2019 (opening chart; the slope about $-0.34$ on the probe); the Volcker disinflation's sacrifice ratio
(ledger: Ball 1994, in Mankiw (ed.) *Monetary Policy*, NBER); breaks: after 1995 inflation stopped responding to its past
(anchored expectations), the curve flattened, and 2021--23 moved fast.

**Recalls**: the Phillips curve and its breakdown, stagflation, the natural rate (g12 `phillips-curve`, g11 `unemployment`);
the long-run and short-run models (g12 `aggregate-demand-and-supply`); IS--LM (ch. 24).

**Opening chart**: *Change in inflation against the unemployment rate, United States, 1960--2019* --- JST R6: inflation $=
\Delta\ln cpi$, $\Delta\pi$ against `unemp`, with the fitted line and the zero crossing. Test: 59 points, fitted slope negative.

**Other charts**: (2) *Inflation and unemployment, United States, 1960--2020, as a connected path by decade* (JST); the g12
opening chart is 1960--69 and 1970--83 of "one country": check Book 2's choice at the sync and use the euro area (Eurostat
`prc_hicp_aind`, `une_rt_a`, 1999--2024) if it is the US.

**Diagrams**: (a) AD--AS with SRAS and LRAS, a demand shock and the adjustment; (b) a supply shock; (c) short-run Phillips
curves shifting with $\pi^e$ and the vertical long-run curve; (d) a disinflation path in $(u, \pi)$.

**Boxes**: `record[The 1970s]` (stagflation; what the stable trade-off said; what happened --- refuted); `record[The Volcker
disinflation]` (dates and rates from Fed press releases and JST; the sacrifice ratio from Ball 1994); `record[2021--23]`
(US CPI peak in June 2022 from BLS `bls_cpi` --- a figdata number; the fall after); `measure[Estimating the natural rate]`
(CBO's estimate, ledger, against the chart's crossing point).

**Exercises** (12): ★ SRAS: output when $P = 1.05$, $P^e = 1$, $a = 2000$, $\bar Y = 10000$ (C); ★ read $\Delta\pi$ for 1974 and
1982 from the table (R, data); ★ predict inflation next year with $\pi^e = \pi_{-1} = 3\%$, $u = 4\%$, $u^n = 5\%$, $\beta = 0.5$
(P); ★ Okun's law: output gap from an unemployment gap (C). ★★ inflation path for five years with $u$ held 1 point below
$u^n$ (C); ★★ the sacrifice ratio of cutting inflation from 10\% to 4\% with $\beta = 0.5$ and Okun's coefficient 2 (C); ★★
estimate $u^n$ from the fitted line in the table (R, C, data); ★★ a supply shock $v = 2$: the choice between holding $u$ and
holding $\pi$ (P); ★★ AD--AS: a demand shock's short- and long-run effects (C). ★★★ derive the Phillips curve from sticky
prices and Okun's law (C); ★★★ with $\pi^e = \lambda\pi_{-1} + (1-\lambda)\bar\pi$: show a long-run trade-off reappears unless
$\lambda = 1$, and what the 1970s said about $\lambda$ (C, F); ★★★ what pattern after 1995 would refute adaptive expectations,
and does the data show it (F).

**Weekend problem**: *Kestria's disinflation.* Part I the Phillips curve calibrated, Part II a cold-turkey disinflation: the
unemployment path, Part III a gradual path and its sacrifice ratio, Part IV a credible announcement moves $\pi^e$ at once:
the saving in unemployment. Named result: "the cold-turkey and gradual paths cost the same 12 point-years of
unemployment under adaptive expectations; credibility saves 8". 25 questions.

**Ledger**: b1:aggregate-supply:ball1994, :fed-volcker-1979, :cbo-nrou, :okun-coefficient (a primary estimate).

### 26. Stabilisation Policy and Its Limits (`26-stabilisation-policy`)

**Programme items**: macro text ch. 17 (stabilisation policy), part of 18 (debt, briefly); C S2 "macroeconomic policy".

**Hook**: of the many recessions in rich and emerging economies since 1990, forecasters a year ahead predicted almost none
(ledger: An, Jalles and Loungani 2018).

**Sections**
1. Delays --- recognition, decision, action, effect; a policy that arrives late can amplify a cycle (shown on a
   deterministic cycle with a lagged response: a numerical example in TikZ, derived).
2. Uncertainty about the model --- multiplicative uncertainty: act less (derived in a quadratic-loss example); real-time
   output-gap errors (ledger: Orphanides 2001, AER 91(4)).
3. The record of fine-tuning --- the 1960s--70s; what the record refuted (fine-tuning) taught as refuted.
4. Automatic stabilisers --- taxes and benefits that move with income; their size across countries; the evidence from
   2008--09 (second chart).
5. Rules and discretion --- a rule's commitment; a simple interest-rate rule (Taylor rule as a label); time inconsistency
   (Y2 owns it; told in one paragraph and named in prose).
6. How multipliers are measured --- narrative shocks, regional cross-sections, structural models; the `debate`; fiscal
   policy at the zero lower bound; 2020--23: transfers, then inflation.

**Definitions owned**: policy lag (inside lag, outside lag in one definition), automatic stabiliser (**re-founded**? g12
owns it --- see report; if g12 owns it, recalled), policy rule (vs discretion; a *Taylor rule* indexed as a label), output
gap (**re-founded**? check g12), local (relative) multiplier.

**Models**: `model{Stabilisation with lags}` --- assumes the IS--LM/AS economy of chapters 24--25 with a lag of $k$
periods between a shock and the response; predicts a lagged countercyclical policy can raise volatility when the lag is
long relative to the cycle; tested: forecast records (opening chart if approved; else the `record` box) and real-time gap
errors (Orphanides 2001); breaks: rules that respond to current data (Taylor rule), automatic stabilisers that need no
decision.

**Recalls**: monetary policy, rules and discretion (g12 `monetary-policy`); fiscal policy and debt, automatic stabilisers
(g12 `fiscal-policy-and-debt`); IS--LM, AD--AS (ch. 24--25).

**Opening chart**: *Forecasts of GDP growth made a year ahead against the outcome* --- **Data to approve** (Philadelphia
Fed Survey of Professional Forecasters or the IMF's historical WEO forecasts). Fallback meanwhile: *Change in the budget
balance against the change in GDP growth from 2007 to 2009, 31 European countries* (Eurostat `gov_10dd_edpt1` B9 S13 per cent
of GDP; `nama_10_gdp` B1GQ CLV\_PCH\_PRE): automatic stabilisers plus discretion. Test: 31 rows, budget balance fell in most.

**Other charts**: (2) *US CPI inflation, monthly, 2019--2024* (BLS `bls_cpi("CUUR0000SA0")`, 12-month change) with the 2020--21
fiscal packages marked by date (ledger rows).

**Diagrams**: (a) the lags on a time line; (b) a cycle and a lagged policy response that amplifies it (computed path); (c)
the loss with multiplicative uncertainty: optimal response below the certainty-equivalent one.

**Boxes**: `debate[How large are fiscal multipliers?]` --- Ramey and Zubairy 2018 (JPE 126(2): 0.6--1.0, little state
dependence) against Auerbach and Gorodnichenko 2012 (AEJ: Economic Policy 4(2): larger in recessions), with Nakamura and
Steinsson 2014 (AER 104(3): local multiplier about 1.5) and what each design identifies; weaknesses of each; the large fixed
multiplier taught as refuted; `record[Fine-tuning]` (the 1960s--70s; what the record refuted); `record[2020--23]` (the
packages and their sizes, ledger: CBO; inflation from BLS); `dated{2026}` none planned.

**Exercises** (12): ★ the three lags of a stated episode (R); ★ read the change in budget balance and growth for two
countries from the table (R, data); ★ a Taylor rule rate with $\pi = 4\%$, gap $= -1\%$ (C); ★ predict the sign of the budget
balance change in a recession with no discretion (P). ★★ the lagged-response cycle: variance with and without policy (C);
★★ optimal response under multiplicative uncertainty (C); ★★ slope of the budget change on the growth change across the
table: the size of stabilisers (R, C, data); ★★ predict the error of a policy based on a real-time gap overstated by 2 points
(P); ★★ a local multiplier of 1.5 and a national one: why they differ (C, P). ★★★ derive the variance-raising condition
for a lagged response in a simple AR(1) economy (C); ★★★ a rule against discretion with a shock the rule ignores: the loss
comparison (C, P); ★★★ what evidence would refute "fiscal multipliers are larger at the zero lower bound" (F).

**Weekend problem**: *Brenland's finance minister and a forecast.* Part I a recession forecast with error, Part II acting with
a two-quarter lag: the outcome in three scenarios, Part III the automatic stabilisers of the household survey's tax and
transfer schedule, Part IV a rule that ties spending to the output gap: volatility compared. Named result: "Brenland's
automatic stabilisers offset 28\% of a fall in market income" (from `households.csv` and `TAX_BANDS`). 26 questions.

**Ledger**: b1:stabilisation-policy:an2018, :orphanides2001, :ramey2018, :auerbach2012, :nakamura2014, :cbo-2020-packages,
:taylor1993 (as a label source).

### 27. The Open Economy (`27-open-economy`)

**Programme items**: macro text ch. 6 (the open economy) and ch. 14 (Mundell--Fleming, regimes); international economics
introduction (A S2, the macro half).

**Hook**: from 1979 to 1998 the Netherlands' short-term interest rate stayed within a point or two of Germany's; France's
and Italy's did not, and in September 1992 Sweden's overnight rate briefly went to 500\% (ledger).

**Sections**
1. Open-economy accounts --- $Y = C + I + G + NX$; $S - I = NX$ (= current account, ignoring income flows, re-founded with
   ch. 18's sectors); the net foreign asset position.
2. The real exchange rate --- $\varepsilon_r = eP^*/P$ in the series' convention (a rise is a real depreciation); net exports
   rise with $\varepsilon_r$ (the Marshall--Lerner condition derived as a label); purchasing-power parity as a long-run
   benchmark (recalled).
3. The small open economy in the long run --- $r = r^*$; $NX = S - I(r^*)$; the real exchange rate clears $NX$; a fiscal
   expansion at home and abroad.
4. The Mundell--Fleming model --- IS$^*$ and LM$^*$ with $r = r^*$; floating rates: fiscal policy ineffective, monetary
   effective; fixed rates: the reverse (derived); a toy model in its frame.
5. The trilemma --- free capital flows, a fixed rate, independent monetary policy: two of three (proved within the
   model); the data: pegged rates follow the base (opening chart).

**Definitions owned**: net foreign asset position, real exchange rate (**re-founded**; g12 owns exchange rates and PPP ---
see report), Marshall--Lerner condition, small open economy, Mundell--Fleming model (in the `model` box), trilemma
(*impossible trinity*; owned here, Y3 `exchange-rate-regimes` recalls --- see report). Interest parity is only the assumption $r = r^*$ of perfect capital mobility here; *uncovered
interest parity* is Y3's.

**Models**: `model{The Mundell--Fleming model}` --- assumes a small open economy, perfect capital mobility, fixed prices,
static expectations of the exchange rate; predicts fiscal policy moves only the exchange rate under floating and output under
a peg, monetary policy the reverse; tested: pegged countries' rates follow the base country's (ledger: Obstfeld, Shambaugh
and Taylor 2005, REStat 87(3)); the 1992 ERM crisis (record); breaks: prices adjust, expectations of devaluation (the
1992 spikes), imperfect capital mobility, large economies.
`model{The small open economy in the long run}` --- assumes $r = r^*$, full employment; predicts a home fiscal expansion
lowers $NX$ and appreciates the real exchange rate; tested: saving and investment are highly correlated across countries
(ledger: Feldstein and Horioka 1980, Economic Journal 90(358)) --- a puzzle for the model; breaks: capital mobility is not
perfect.

**Recalls**: exchange rates and purchasing-power conversion (g9); the balance of payments, PPP, interest parity first look,
the three aims (g12 `exchange-rates-and-balance-of-payments`); IS--LM (ch. 24); sector balances (ch. 18); the gains from
trade in two lines (g10 `ricardo-model`).

**Opening chart**: *Short-term interest rate minus Germany's, 1979--1998, for currencies pegged to the Deutsche Mark:
Netherlands, Belgium, Denmark, France, Italy, Spain, Sweden (from 1991)* --- JST R6 `stir`, with `peg == 1` and `peg_base ==
"DEU"` marking the pegged years (annual). Test: the Netherlands' mean gap below France's; peg years flagged from the data.

**Other charts**: (2) *Price levels against income per person, 2021* --- WDI `PA.NUS.PRVT.PLI` and `NY.GDP.PCAP.PP.KD`
(only if ch. 18 does not carry it; otherwise: *Saving and investment rates across countries, average 2000--2019*, WDI
`NY.GNS.ICTR.ZS` (check availability at writing) and `NE.GDI.TOTL.ZS`, the Feldstein--Horioka picture).

**Diagrams**: (a) the small open economy: $S$ vertical, $I(r)$, the world rate and $NX$; (b) $NX(\varepsilon_r)$ and the
real exchange rate clearing; (c) Mundell--Fleming in $(Y, e)$: in the series' convention a rise in $e$ is a depreciation, so IS$^*$ slopes **up** in
$(Y, e)$ (higher $e$, higher $NX$, higher $Y$) and LM$^*$ is vertical; floating and fixed cases; (d) the trilemma triangle.

**Boxes**: `record[September 1992]` (the ERM crisis: Sweden's marginal rate at 500\%, the UK's exit; ledger: Riksbank, Bank of
England); `record[Saving and investment]` (Feldstein--Horioka 1980 and later evidence); `measure[A real effective exchange
rate]` (WDI `PX.REX.REER`; how trade weights are built; ledger: IMF/World Bank definition).

**Exercises** (12): ★ $NX$ from $S$ and $I$ (C); ★ real exchange rate from $e$, $P$, $P^*$ (C); ★ read the mean gap of three
countries from the table (R, data); ★ predict the effect of a home fiscal expansion on $\varepsilon_r$ in the long-run model (P).
★★ the small open economy with $S = 400$, $I = 500 - 20r$, $r^* = 4$ and $NX = 100 - 50\varepsilon_r$ (C); ★★ Mundell--Fleming
under floating: a rise in $G$ of 50 (C); ★★ under a peg: a rise in $M$ (C, P); ★★ the Marshall--Lerner condition with given
elasticities (C); ★★ count the years each country was pegged and its gap in those years (R, C, data). ★★★ derive the
Mundell--Fleming multipliers under both regimes (C); ★★★ with expected devaluation $\Delta e^e$, show the peg needs $r = r^* +
\Delta e^e$ and compute the Swedish 1992 rate implied by a 10\% expected devaluation within a week (C, P); ★★★ what evidence
would refute the trilemma (F).

**Weekend problem**: *Brenland pegs to the kest.* `trade.csv` gives the dalen--kest rate. Part I open-economy accounts and
the current account, Part II the long-run model with the world rate, Part III Mundell--Fleming under the float and the peg,
Part IV a speculative attack: the interest rate needed to hold the peg, and the reserves it costs. Named result: "holding
the peg against a 5\% expected devaluation in one month needs an annualised rate of 80\%". 26 questions.

**Ledger**: b1:open-economy:obstfeld2005, :feldstein1980, :riksbank-1992, :boe-erm-exit-1992.

---
## Part VII --- Data and statistics, in Python

Common to chapters 28--32: the reader knows Python, functions, lists, dictionaries, files and a first use of tables from the
computer science series (recalled in prose in ch. 28's `recall` box, never re-taught). Listings use pandas, numpy, scipy and
statsmodels only, read data through `econdata` / `country` (`from econdata import pwt`, `from country import load` --- check
the `country` loader's name at writing), fit 88 columns, at most 40 printed lines per `\omcode`. Every listing has a test in
`tests/` (estimates to a tolerance). Outputs only from `tools/capture_output.py`. Listing stems below are the planned file
names (`listings/<stem>.py`, `outputs/<stem>.txt`). The micro-data of Part VII are the NSW/LaLonde samples (approved, CC
BY-NC 2.0): the PSID comparison sample (2,490 men aged 18--55, earnings in 1974, 1975 and 1978, not top-coded) and the CPS
comparison sample (15,992 men, earnings top-coded at about \$25,565 --- a quarter of the sample at the cap, a trap the book
uses), plus the experimental sample (445 men). Brenland's household survey (2,000 households) is the invented survey for
weights and sampling.

### 28. Economic Data with Python (`28-economic-data-python`)

**Programme items**: computing for economists (B S1 "foundations of computing", A S2 "digital culture" --- economics use
only); statistics S1 data handling; the outline's "every number comes from a script that can be rerun".

**Hook**: two analysts compute "growth in the euro area since 2000" and get 1.2\% and 1.6\% a year. Both are right: one used
GDP, the other GDP per person, one chained, one current prices.

**Sections**
1. Three shapes of data --- cross-section, time series, panel; long and wide tables; the unit of observation; keys.
2. Loading and joining --- `econdata` loaders; selecting rows and columns; merging two sources on `(iso3, year)`; checking
   what did not match (anti-join) --- the commonest silent error.
3. Units and frequencies --- levels, shares, per person; monthly to yearly (average, end of period, sum for flows);
   twelve-month and month-on-month changes, annualised.
4. Seasonal adjustment --- why monthly series need it; a ratio-to-moving-average method by hand (centred 12-month moving
   average, seasonal factors, adjusted series), compared with the official adjusted series; the official method named
   (X-13ARIMA-SEATS, ledger: BLS page) and not taught.
5. Deflating, indexing, logarithms and growth rates --- real series from a deflator; rebasing an index; log growth and its
   average; per-person values; chained-index caution (ch. 7 recalled).
6. A chart is a table a script wrote --- the book's own pipeline: a script writes a CSV that the chart reads; rerunning
   gives the same bytes; why nothing is typed.

**Definitions owned**: cross-section, time series, panel data (as a data structure; Y3 `panel-data` owns the estimators),
unit of observation, merge key, seasonal adjustment, seasonal factor, annualised rate, reproducible computation.

**Models**: none in the frame (a method chapter); one `measure[Seasonal adjustment]` box.

**Recalls**: Python, lists, dictionaries, functions, reading a file, tables (computer science series, school years);
growth rates and logarithms (ch. 1); price indices and deflators (ch. 7, g10).

**Opening chart**: *US consumer prices, month-on-month change, 2015--2024, not seasonally adjusted and seasonally adjusted*
--- BLS `bls_cpi("CUUR0000SA0")` and `bls_cpi("CUSR0000SA0")` (values to numeric: the loader returns padded strings ---
reported). Test: 120 rows each, the NSA series has a larger standard deviation.

**Other charts**: (2) *The by-hand adjustment against the official one*, 2015--2024 (from listing `seasonal_by_hand`, the
CSV it writes is the figdata table: the figdata script imports the listing's function, so the chart and the listing cannot
drift).

**Listings** (`code/bachelor-1/28-economic-data-python/listings/`):
1. `first_look.py` --- `pwt(["FRA", "DEU"], since=2015)`, `.head()`, `.shape`, `.dtypes`; output: the first rows.
2. `long_and_wide.py` --- pivot GDP per person of five countries to wide and back (`pivot`, `melt`).
3. `join_sources.py` --- merge WDI `NY.GDP.PCAP.PP.KD` with PWT `rgdpe/pop` on `(iso3, year)` with `indicator=True`; count
   unmatched rows by side; output: the counts and three unmatched codes (aggregates such as `WLD`).
4. `join_trap.py` --- the same merge without `countries_only=True`: duplicated rows appear; the fix.
5. `monthly_to_yearly.py` --- CPI monthly to annual average; compares with the published annual average (M13).
6. `changes.py` --- month-on-month, twelve-month and annualised changes; the June 2022 figure.
7. `seasonal_by_hand.py` --- the ratio-to-moving-average adjustment, function `adjust(series)`; output: the seasonal factors
   by month.
8. `deflate_and_index.py` --- Brenland `accounts.csv`: nominal GDP to real with the deflator, rebased to 2020 = 100; log
   growth and its mean.
9. `per_person_growth.py` --- euro-area-like comparison (Eurostat `nama_10_gdp` volumes, and population from WDI): growth of
   GDP and of GDP per person, 2000--2023 (the hook's two numbers).
10. `write_chart_table.py` --- writes a CSV and prints its first lines; shows that rerunning gives the same bytes (prints a
    hash).

**Tests** (`tests/`): `test_join.py` (unmatched counts > 0, no duplicates after the fix), `test_seasonal.py` (factors
average 1, the by-hand series correlates above 0.9 with the official one), `test_changes.py` (June 2022 twelve-month change
of the NSA index between 8.9 and 9.2), `test_deflate.py` (real GDP 2020 = nominal 2020 after rebasing), `test_reproducible.py`
(two runs, same hash), and one test per data exercise.

**Diagrams**: (a) long and wide tables side by side with arrows; (b) a merge with matched and unmatched keys (a Venn-like
schematic).

**Boxes**: `measure[Seasonal adjustment]` (what X-13 does in one paragraph, why revisions follow; ledger: BLS seasonal
adjustment page); `record[A spreadsheet error]` (the Reinhart--Rogoff spreadsheet episode: ledger: Herndon, Ash and Pollin
2014, Cambridge Journal of Economics 38(2); the authors named only as the source --- check whether naming the episode is a
"person as label" breach; if so, describe it without names) --- **flagged for the sync**.

**Photograph**: none.

**Exercises** (12, each data exercise with `exercises/exo_NN.py`): ★ shape and keys of three tables (R); ★ twelve-month CPI
change in a given month from the output (R, data); ★ annualise a 0.4\% monthly rate (C); ★ which aggregation (mean, last,
sum) for five series (R). ★★ merge PWT and Maddison GDP per person, count unmatched countries (C, data); ★★ rebase an index
and compute average log growth (C, data); ★★ seasonal factors of a toy series by hand (C); ★★ predict the sign of the gap
between GDP and GDP-per-person growth in a country whose population falls (P); ★★ the euro-area hook numbers recomputed (C,
data). ★★★ write `adjust()` for quarterly data and test it on a series with a known season (C, data); ★★★ find the silent
error in a given merge (an `iso3` lower-case mismatch) (C, F); ★★★ what check would catch a deflator in the wrong base year
(F).

**Weekend problem**: *Brenland's open-data portal.* Part I loading and checking `accounts.csv`, `trade.csv`, `basket.csv`,
Part II joining them and finding the year that does not match, Part III a monthly series built from the yearly CPI with a
seeded season (from figdata), adjusted by hand, Part IV the published growth numbers recomputed and one corrected. Named
result: "the corrected real growth of Brenland, 2015--2025: 1.9\% a year, not the portal's 2.4\%". 24 questions.

**Ledger**: b1:economic-data-python:bls-x13, :herndon2014 (pending the sync).

### 29. Describing Data (`29-describing-data`)

**Programme items**: descriptive statistics (A S1, Universities B--D statistics 1): distributions, central tendency,
dispersion, two-variable description; traps of aggregation.

**Hook**: in a sample of 2,490 American men in 1978, average earnings were higher than what most of them earned.

**Sections**
1. Histograms and quantiles --- bins and densities; the empirical distribution function; quantiles and percentiles; on an
   ordinary and on a logarithmic axis (opening chart).
2. Mean, variance and skewness --- recalled definitions (mathematics series) applied; skewness; incomes are right-skewed; the
   log of income is closer to symmetric.
3. Covariance and correlation --- the sample covariance, the correlation coefficient, its range (proved by Cauchy--Schwarz),
   what it misses (non-linear relations: an example).
4. Conditional means --- means by group (`groupby`); a first conditional expectation function in data (earnings by years of
   schooling; prepares ch. 32).
5. Traps --- composition effects; Simpson's paradox (a real example and a Brenland one); top-coding and censoring (the CPS
   sample's cap); outliers: the median and trimmed means against the mean.

**Definitions owned**: histogram (as a density estimate; the mathematics series owns frequency tables --- check at writing),
empirical distribution function, quantile (percentile; *quartile* is the mathematics series'), skewness, sample covariance,
correlation coefficient, conditional mean (in data), composition effect, Simpson's paradox, top-coding (*censoring* in the
same definition), outlier, trimmed mean.

**Models**: none in the frame (description); `record[Admissions by department]` for Simpson's paradox (ledger: Bickel,
Hammel and O'Connell 1975, Science 187(4175)).

**Recalls**: mean, median, quartiles, variance, standard deviation (mathematics g9--g11); Lorenz curve, Gini, top shares
(g11 `inequality`); logarithms; Python and pandas (ch. 28).

**Opening chart**: *The distribution of household income, United States, 2022, by hundredth of the population, on an ordinary
and on a logarithmic axis* --- PIP `pip_percentiles(["USA"], [2022])`, `avg_welfare` (2021 PPP \$ a day, income), two panels.
(If 2022 is missing, the latest year; the script asserts which.) Test: 100 rows, monotone, top percentile above 10 times the
median.

**Other charts**: (2) *Earnings in 1978: the PSID and the CPS samples, histograms* (NSW `psid_controls`, `cps_controls`
`re78`): the CPS cap visible as a spike. (3) *Mean earnings by years of schooling, PSID sample* (bars with counts).

**Listings**:
1. `histogram.py` --- `numpy.histogram` of PSID `re78`; densities; output: the bin table.
2. `quantiles.py` --- quantiles and the share of the sample below the mean.
3. `moments.py` --- mean, variance, skewness of earnings and of log earnings (scipy.stats.skew).
4. `top_coding.py` --- the CPS cap: share at the maximum; mean with and without the capped rows; a lower bound.
5. `covariance.py` --- covariance and correlation of earnings in 1975 and 1978, by hand and with pandas.
6. `nonlinear.py` --- a seeded $y = x^2$ example with correlation near zero.
7. `group_means.py` --- `groupby("education")` mean, median and count.
8. `simpson.py` --- a Simpson's paradox in Brenland's survey: home-owners' mean income against renters' overall and within
   age groups (the survey must show it: check at writing; if not, a seeded table in `listings/`, labelled invented).
9. `trimmed.py` --- the mean, median and 5\% trimmed mean with and without the largest observation.

**Tests**: moments to tolerance; share of CPS at cap between 0.25 and 0.27; correlation in $[-1, 1]$; group means match a
direct computation; Simpson reversal present.

**Diagrams**: (a) a histogram with bins and density labels; (b) correlation of 0 with a parabola, of 1 with a line, of 0.6
with a cloud (seeded); (c) Simpson's paradox as two within-group lines and a reversed pooled line.

**Boxes**: `record[Admissions by department]`; `measure[Income in a survey]` (what PIP's income is: per capita, household
surveys, top under-coverage; ledger: PIP methodology page).

**Exercises** (12): ★ read the median and the 90th percentile from the opening chart table (R, data); ★ mean against median
for five numbers (C); ★ correlation from a covariance and two standard deviations (C); ★ which aggregation trap in a
described case (R). ★★ skewness of log against level earnings (C, data); ★★ the CPS mean with capped values replaced by the
cap times 1.5 --- how sensitive (C, data); ★★ conditional means of earnings by schooling, and the step from 11 to 12 years
(R, C, data); ★★ prove $|r| \le 1$ (C); ★★ predict the effect on mean and median of adding one billionaire to a town of 10,000
(P). ★★★ build a Simpson's paradox with two groups and given counts (C); ★★★ show the mean minimises the sum of squared
deviations and the median the sum of absolute deviations (C); ★★★ what observation would show that a correlation of 0.1
hides a strong relation (F).

**Weekend problem**: *Brenland's household survey, described.* Part I the income distribution, histograms on both axes,
Part II moments and quantiles, the share of the top tenth, Part III income and schooling: conditional means and correlation,
Part IV the home-ownership paradox resolved by age. Named result: "within every age group owners earn more, yet overall
renters' mean is higher by \dal{...}" (from the survey; else a statement fitted to what the survey shows). 25 questions.

**Ledger**: b1:describing-data:bickel1975, :pip-methods, :lalonde1986 (sample definitions: LaLonde 1986, AER 76(4)),
:dehejia1999 (JASA 94(448)).

### 30. Random Variables for Econometrics (`30-random-variables-for-econometrics`)

**Programme items**: statistics 2 (Universities B--D): random variables, laws, sampling distributions; the econometrics texts'
"review of probability".

**Hook**: draw five men at random from the PSID sample and average their earnings; do it again. The averages jump around
the true mean, and less so with thirty, and less again with two hundred.

**Sections**
1. Expectation, variance, covariance --- recalled from the mathematics series (expectation, variance) with the rules;
   covariance of two random variables in a `notation` box (the mathematics series defines it in Year 2; pointer); variance of
   a sum.
2. Joint and conditional distributions --- joint table, marginals, conditional distribution; independence recalled.
3. Conditional expectation --- $\E[Y \mid X = x]$ as a function of $x$; the law of iterated expectations (proved, discrete
   case); $\E[Y \mid X]$ is the best predictor in mean square (proved, discrete case); mean independence against independence.
4. The tools --- the normal law recalled; chi-square, Student's $t$ and $F$ as constructions from normal variables (defined);
   their shapes; `scipy.stats` quantiles.
5. The law of large numbers and the central limit theorem --- the LLN recalled (mathematics g12); the CLT stated, admitted
   (proved in the Year 3 mathematics volume); seen by simulation from the skewed PSID earnings (opening chart).

**Definitions owned**: joint distribution (of two discrete random variables; check the mathematics harvest at writing),
conditional distribution, conditional expectation, law of iterated expectations (`theorem`), mean independence,
chi-square distribution, Student's $t$ distribution, $F$ distribution, sampling distribution.

**Models**: `model{Random sampling}` --- assumes observations drawn independently from one population; predicts sample means
centred on the population mean with variance $\sigma^2/n$ and an approximately normal shape for large $n$; tested: by
simulation from a real skewed population (opening chart); breaks: dependent draws (time series, clusters: Y2), very
heavy tails (the variance does not exist: a seeded Pareto example with $\alpha < 2$).

**Recalls**: random variables, expectation, variance, independence, the binomial and normal laws, the law of large numbers
(mathematics g11--g12, Year 2 pointer for covariance); the central limit theorem (mathematics Year 3, admitted); describing
data (ch. 29).

**Opening chart**: *Sample means of 1978 earnings, 10,000 samples of 5, 30 and 200 men drawn from the PSID sample* (with
replacement, seeded; histograms of the means, the population mean marked) --- NSW `psid_controls` `re78`, simulated in
figdata with a fixed seed. Test: the standard deviation of the means within 3\% of $\sigma/\sqrt n$ for each $n$.

**Other charts**: (2) *The $t$ distribution with 2, 5 and 30 degrees of freedom against the normal* (a function plot: a
diagram, `omfigure`, not data). (3) *Sample means from a Pareto population with $\alpha = 1.5$*: no convergence of the
variance (seeded).

**Listings**:
1. `joint_table.py` --- a joint distribution of schooling (grouped) and earnings bracket from the PSID, marginals and a
   conditional distribution.
2. `iterated.py` --- checks $\E[\E[Y \mid X]] = \E[Y]$ on the PSID with `groupby` and weights.
3. `best_predictor.py` --- mean squared error of three predictors of earnings: the overall mean, a line, the conditional mean.
4. `distributions.py` --- `scipy.stats` quantiles of $N(0,1)$, $\chi^2_k$, $t_k$, $F_{k,m}$ that the next chapters use; output: a
   table of 5\% and 2.5\% critical values.
5. `build_t.py` --- simulate $Z/\sqrt{V/k}$ and compare its quantiles with `scipy.stats.t`.
6. `lln.py` --- running mean of PSID earnings draws.
7. `clt.py` --- sample means for $n = 5, 30, 200$; their standard deviations against $\sigma/\sqrt n$ (the opening chart's
   numbers).
8. `heavy_tails.py` --- Pareto means that do not settle.

**Tests**: iterated expectations to $10^{-9}$; simulated $t$ quantiles within 0.05 of the exact ones; CLT standard deviations
within 3\%; seeds fixed.

**Diagrams**: (a) a joint table with marginals in the margins (a TikZ table schematic); (b) the conditional expectation as a
line through conditional means of a cloud.

**Boxes**: `measure[Drawing a sample in a computer]` (pseudo-random numbers, seeds, why a seed makes a result
reproducible).

**Exercises** (12): ★ $\E[2X + 3]$ and $\Var(2X + 3)$ (C); ★ a conditional distribution from a joint table (C); ★ read the
standard deviation of the means for $n = 30$ from the output (R, data); ★ predict the standard deviation for $n = 120$ (P).
★★ law of iterated expectations on a two-group example (C); ★★ $\Var(X + Y)$ with a covariance (C); ★★ a 95\% interval for a
sample mean with $n = 200$ using the CLT (C, data); ★★ chi-square as a sum of squares: mean and variance (C); ★★ predict the
effect of clustering (pairs of brothers) on the variance of a mean (P). ★★★ prove that $\E[Y \mid X]$ minimises mean squared
error among functions of $X$ (discrete) (C); ★★★ show mean independence implies zero covariance and give a counterexample to
the converse (C); ★★★ what simulation result would show that the CLT approximation fails for $n = 30$ for a given population (F).

**Weekend problem**: *The Brenland lottery of surveys.* Part I a joint distribution of household size and income from
`households.csv`, Part II conditional expectations and the law of iterated expectations, Part III sampling 100 households:
the sampling distribution of the mean income by simulation, Part IV a $t$ statistic built and its distribution checked.
Named result: "with 100 households, the mean income is within \dal{...} of the truth in 95\% of surveys" (from the
script). 25 questions.

**Ledger**: none needed beyond the shared NSW rows (ch. 29).

### 31. Sampling and Inference (`31-sampling-and-inference`)

**Programme items**: statistics 2 (Universities B--D): estimation, confidence intervals, tests; how an unemployment rate
is estimated.

**Hook**: the US unemployment rate is estimated each month from a survey of about 60,000 households. A change of 0.1
point from one month to the next is not distinguishable from sampling noise (ledger: BLS).

**Sections**
1. Population and sample --- parameters and statistics; random sampling (recalled); estimators.
2. Estimators: bias, variance, consistency --- definitions; the sample mean is unbiased and consistent (proved); the
   $n - 1$ in the sample variance (proved); mean squared error and the bias--variance trade-off.
3. The standard error and confidence intervals --- $\widehat{\mathrm{se}} = s/\sqrt n$; a 95\% interval; its meaning (coverage
   over repeated samples, shown by simulation); difference of two means.
4. Tests --- null and alternative; the test statistic; size and the significance level; the $p$-value and what it is not
   (not the probability the null is true; ledger: the American Statistical Association's 2016 statement); power and sample
   size; a test of the job-training experiment's effect (the NSW sample: treated against controls).
5. Many tests at once --- the family-wise error rate; Bonferroni; specification search (Y3 `credible-empirical-work`
   continues).
6. Survey design and weights --- stratified sampling; weights as inverse probabilities; design effects; how an
   unemployment rate is estimated (the survey's design; ledger) and its standard error.

**Definitions owned**: population (statistical; check the mathematics harvest), parameter (statistical; distinct from ch.
1's model parameter --- the definition names it *population parameter*), estimator, unbiased estimator, consistent
estimator, mean squared error, standard error, confidence interval, null hypothesis (and alternative), test statistic,
significance level (*size*), $p$-value, power (of a test), family-wise error rate, sampling weight, design effect,
stratified sample.

**Models**: `model{The randomised comparison}` --- assumes random assignment to a job-training programme, no interference;
predicts the difference in mean earnings estimates the average effect without bias; tested: the NSW experiment's estimate of
about \$1,800 in 1978 earnings (computed from the approved sample by the listing; ledger: Dehejia and Wahba 1999 for the
published number); breaks: attrition, small samples (wide interval), effects that do not travel (Y2
`causality-and-experiments`, named in prose).

**Recalls**: sampling distribution, $t$ and normal laws, the CLT admitted (ch. 30); the unemployment survey (g8, g11);
conditional means (ch. 29).

**Opening chart**: *A monthly unemployment rate with its confidence band* --- **Data to approve** (BLS series LNS14000000 with
the published standard error, ledger). Fallback meanwhile: *Twenty-four simulated monthly surveys of Brenland's labour force
with 95\% intervals around the true rate* --- the true monthly path interpolated from `accounts.csv` `unemp_rate`, 60,000
simulated households a month, seeded; labelled "simulated". Test: about 95\% of intervals cover the truth over 1,000 seeded
replications (checked in the test, not printed).

**Other charts**: (2) *Coverage of 100 confidence intervals* (seeded, from listing `coverage`): intervals as horizontal
segments, the ones that miss in another colour. (3) *Power against effect size for $n$ = 100, 445 and 2,000* (a computed
function: a diagram via pgfplots in `omfigure`).

**Listings**:
1. `bias_variance.py` --- simulate two estimators of a mean (sample mean and a shrunk mean) from PSID earnings; bias,
   variance, MSE.
2. `sample_variance.py` --- dividing by $n$ against $n - 1$, by simulation.
3. `interval.py` --- mean earnings of the NSW controls with a 95\% interval.
4. `coverage.py` --- 100 seeded intervals, the count that miss (the second chart's table).
5. `nsw_effect.py` --- the experimental estimate: difference in mean 1978 earnings, its standard error, the $t$ statistic,
   the $p$-value (`scipy.stats.ttest_ind` with `equal_var=False`, and by hand); output printed in full.
6. `power.py` --- power by simulation and by the formula for the NSW sample size.
7. `many_tests.py` --- 20 placebo tests on random splits of the control group; how many reject at 5\%; Bonferroni.
8. `weights.py` --- a stratified sample of Brenland households (over-sampling owners); the unweighted and weighted mean
   income against the truth; the design effect.
9. `unemployment_survey.py` --- a simulated survey estimate of an unemployment rate with its standard error; the change from
   one month to the next and its standard error.

**Tests**: NSW difference within \$1 of a direct computation and between \$1,600 and \$2,000; coverage in the replication test
between 93\% and 97\%; Bonferroni threshold; weighted mean closer to the truth than the unweighted.

**Diagrams**: (a) sampling from a population, an estimator, its sampling distribution (a schematic); (b) a two-sided test:
the null density with rejection regions and the observed statistic; (c) size and power: null and alternative densities.

**Boxes**: `record[The job-training experiment]` (the NSW programme, the randomised estimate, and why non-experimental
estimates with the CPS and PSID samples missed it: LaLonde 1986 --- the econometric lesson, not a history); `measure[The
monthly unemployment survey]` (sample size, rotation, standard error of a monthly change; ledger: BLS technical note);
`record[What a p-value is not]` (ASA 2016 statement: Wasserstein and Lazar 2016, The American Statistician 70(2)).

**Exercises** (12): ★ standard error of a mean with $s = 9{,}000$, $n = 400$ (C); ★ read the NSW estimate and its $p$-value
from the output (R, data); ★ which of four statements about a $p$-value is right (R); ★ predict the interval width when $n$ is
multiplied by 4 (P). ★★ bias of a proposed estimator (C); ★★ a test of a difference of two proportions (C); ★★ the sample size
for 80\% power to detect a \$1,000 effect with the NSW standard deviations (C, data); ★★ expected false rejections in 50 tests
at 5\% and the Bonferroni threshold (C); ★★ predict whether the weighted or unweighted mean is closer to the truth in a given
design (P). ★★★ prove the sample variance with $n - 1$ is unbiased (C); ★★★ show an estimator can be biased and consistent,
and give an example from the chapter (C); ★★★ what pattern of published results would show many tests were run but one was
reported (F).

**Weekend problem**: *The Brenland labour-force survey.* Part I design: strata by region (invented within the chapter's
script), weights, Part II the estimate and its standard error, Part III the month-on-month change: a test, Part IV the sample
size needed to detect a 0.2-point change with 80\% power. Named result: "to detect a 0.2-point monthly change, Brenland's
survey needs 41,000 households, not 12,000". 26 questions.

**Ledger**: b1:sampling-and-inference:bls-cps-design, :bls-se-change, :asa2016, :dehejia1999 (shared with ch. 29).

### 32. Simple Regression (`32-simple-regression`)

**Programme items**: statistics 2 (regression line, least squares) and the econometrics texts' first regression chapters;
the outline's "a regression is not a cause".

**Hook**: in the PSID sample, each extra year of schooling goes with about 9\% higher earnings in 1978. Does a year of school
raise earnings by 9\%?

**Sections**
1. The conditional expectation function --- recalled from ch. 30; the best linear approximation to it; the population
   regression line $\beta_1 = \Cov(X, Y)/\Var(X)$ (derived).
2. Least squares --- the estimator $\hat\beta_1 = \sum (x_i - \bar x)(y_i - \bar y)/\sum (x_i - \bar x)^2$ (derived by
   minimising the sum of squares); residuals sum to zero and are uncorrelated with $x$ (proved); fitted values.
3. Reading a slope --- level--level, log--level ($100\beta_1$ per cent), level--log, log--log (an elasticity); units.
4. Fit --- $R^2$ as the share of variance explained; what a low $R^2$ does and does not mean.
5. When is the slope unbiased --- the conditions (random sample, variation in $x$, zero conditional mean of the error); proof of
   unbiasedness; the standard error of the slope under constant variance (formula, derivation in the Year 2 volume named in
   prose); a $t$ test of the slope.
6. Regression toward the mean --- earnings in 1975 and 1978 (the PSID): the slope below one and why; the fallacy it
   creates.
7. A regression is not a cause --- omitted variables (ability: a seeded simulation where the slope is biased); reverse
   causation; what the next volumes do about it (named in prose: experiments, instruments, panels).

**Definitions owned**: population regression line (*best linear predictor*), ordinary least squares estimator, fitted value,
residual, error term (with the series' notation $u_i$), coefficient of determination ($R^2$), zero conditional mean
assumption (the standard error of the slope is a `proposition`: *standard error* is ch. 31's), regression
toward the mean, omitted variable (*confounder* in the same definition), reverse causation.

**Models**: `model{The simple linear regression model}` --- assumes $Y = \beta_0 + \beta_1 X + u$ with $\E[u \mid X] = 0$, a random
sample; predicts an unbiased slope and the stated standard error; tested: the log earnings slope of about 0.09 matches the
range of published returns to schooling (ledger: Card 1999, Handbook of Labor Economics 3A, ch. 30); breaks: when ability
or family background enter $u$ (Y3 `human-capital` with instruments), when $X$ is measured with error (Y2 `specification`).

**Recalls**: correlation and covariance, conditional means (ch. 29); conditional expectation, sampling distributions (ch.
30); standard errors and tests (ch. 31); establishing a cause, correlation and cause (g10 `economic-models`); the
regression line in the mathematics series' statistics, if it has one (check harvest at writing: none found in Phase A).

**Opening chart**: *Log earnings in 1978 against years of schooling, PSID sample of 2,490 men, with the least-squares line*
--- NSW `psid_controls` (`re78 > 0`, `education`), binned means by year of schooling with their counts, and the fitted line
(slope about 0.089 on the probe; the table governs). Test: slope between 0.07 and 0.11; n of positive earners about 2,200.

**Other charts**: (2) *Earnings in 1978 against earnings in 1975, PSID: the slope below one* (binned scatter and the
45-degree line). (3) *A simulated omitted-variable bias*: slopes from 1,000 seeded samples with and without the omitted
ability, histograms.

**Listings**:
1. `ols_by_hand.py` --- the slope and intercept from sums with numpy; residuals sum to zero.
2. `ols_statsmodels.py` --- `smf.ols("np.log(re78) ~ education", data=psid)` and the summary table, printed with
   `.summary().tables[1]` to stay under 40 lines.
3. `reading_slopes.py` --- the four functional forms on one pair of variables (level and log), with the reading of each slope.
4. `r_squared.py` --- $R^2$ three ways (squared correlation, explained over total, $1 -$ residual over total).
5. `slope_se.py` --- the standard error by the formula against statsmodels' value; the $t$ statistic.
6. `toward_mean.py` --- re75 against re78: slope below one; the same regression reversed.
7. `omitted.py` --- seeded simulation: ability raises both schooling and earnings; the biased slope against the truth.
8. `reverse.py` --- seeded simulation of reverse causation (price and quantity from ch. 1's model): the regression slope is
   neither curve's (ties Part VII back to ch. 1).
9. `cps_cap.py` --- the same regression on the top-coded CPS sample: the slope falls by half (the trap of ch. 29).

**Tests**: by-hand and statsmodels slopes equal to $10^{-10}$; PSID slope in the stated range; three $R^2$ equal; toward-mean
slope below one; omitted-variable bias of the expected sign and size within 10\%; CPS slope below the PSID slope.

**Diagrams**: (a) least squares: points, the line, vertical residuals; (b) the four functional forms' shapes; (c) regression
toward the mean: an ellipse, the 45-degree line and the two regression lines; (d) an omitted variable as a causal diagram (a
triangle of arrows: ability $\to$ schooling, ability $\to$ earnings, schooling $\to$ earnings).

**Boxes**: `record[Returns to schooling]` (the cross-sectional slope against estimates from natural experiments; Card 1999;
the Year 3 volume continues); `record[The regression fallacy]` (ledger: Friedman 1992, JEL 30(4), "Do old fallacies ever
die?", on convergence regressions --- named as the source only); `measure[Earnings in the PSID and CPS samples]` (what the
samples are, the cap; ledger: Dehejia--Wahba 1999 and LaLonde 1986).

**Exercises** (12): ★ slope and intercept from five points (C); ★ read the slope, its standard error and $R^2$ from the output
(R, data); ★ interpret a log--level slope of 0.06 (R); ★ predict the fitted log earnings at 16 years of schooling (P). ★★ prove
residuals are uncorrelated with $x$ (C); ★★ the same regression for men under 30 and over 40 in the PSID (C, data); ★★ an
elasticity from a log--log regression of energy on income (ch. 3's table, recomputed in Python) (C, data); ★★ predict the
direction of the omitted-variable bias for a stated confounder (P); ★★ a $t$ test of the slope against 0.10 (C). ★★★ derive the
OLS estimator and prove its unbiasedness under the zero-conditional-mean assumption (C); ★★★ show the slopes of $y$ on $x$ and
of $x$ on $y$ multiply to $r^2$, and use it to explain regression toward the mean (C); ★★★ what evidence would refute a causal
reading of the 0.09 slope (F).

**Weekend problem**: *Schooling and earnings in Brenland.* `households.csv` (`school_years`, `gross_income`). Part I the
regression of log income on schooling, Part II reading, fit and the standard error, Part III a hidden ability variable in a
seeded extension: the bias, Part IV the head's age as a second variable shows why Year 2 needs multiple regression (told, not
solved: the slope changes when age enters, computed by the script and only reported). Named result: "the Brenland return to
a year of schooling: 7.4\% (standard error 0.3)" (from the script). 26 questions.

**Ledger**: b1:simple-regression:card1999, :friedman1992, :dehejia1999 and :lalonde1986 (ch. 29's rows).

---

## Ledger budget and fetch plan

About 120 rows for the book (an average of four per chapter), each from the primary source (DOI page, agency page, law),
read and dated; 200--250 fetches including the photographs' licence pages. Running count in `PROGRESS.md`. Every row named
above is "to verify": a study whose page does not give the number cited is replaced or dropped, never filled from memory.
