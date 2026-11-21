# Book 3 (University Year 1, `b1`) --- defined terms

Phase A, 2026-11-20. Every term Book 3 will define with `\emph{term}\index{term}` inside a `definition` (or a `theorem`,
`proposition` or `model` where the column says so), its owner chapter and its label. **Frozen at the sync for Books 4--5**:
they recall these terms in prose ("defined in the Year 1 volume") and never define them again.

Status column:
- **new**: first defined anywhere in the series here;
- **re-founded**: a school notion (Books 1--2) defined again with calculus, as the outline's table "From school to
  university" allows; the school owner is named;
- **contested**: another book's outline could also claim it; the proposed ruling is in the Phase A report.

Labels follow `<type>:b1:<chapter-slug>:<name>`. Several terms may share one definition (and one label) when the brief says
"in one definition"; the indexed words are listed together.

Not defined here (recalled only): every notion the mathematics series owns (partial derivative, gradient, level curve,
Lagrange's method as a theorem, expectation, variance, covariance of random variables (Year 2 mathematics), independence,
the normal law, the law of large numbers, the central limit theorem, mean, median, quartiles, standard deviation, logarithm,
exponential, integral, differential equation); Nash equilibrium, prisoner's dilemma, externality, public good, rent seeking
(Books 1--2 and Year 2/3); the multiplier, the quantity equation, the natural rate in words, the policy rate (Book 2).

## Part I --- Method

| Term(s) indexed | Label | Ch. | Status |
|---|---|---|---|
| endogenous variable, exogenous variable, parameter | `def:b1:models-and-data:variables` | 1 | new (g10 `economic-models` uses "variables it explains / takes as given" in words: contested, see report) |
| equilibrium (of a model) | `def:b1:models-and-data:equilibrium` | 1 | new as a general notion (g7/g10 own market equilibrium) |
| stock, flow | `def:b1:models-and-data:stock-flow` | 1 | new |
| continuous growth rate | `def:b1:models-and-data:growth-rate` | 1 | re-founded (g8 `growth-and-compounding`) |
| ~~deflator~~ | (dropped at sync: recalled from g10 per R1) | 1 | recalled |
| identification problem | `def:b1:models-and-data:identification` | 1 | new |
| shifter (demand shifter, supply shifter) | `def:b1:models-and-data:shifter` | 1 | new |
| constrained maximum, constrained minimum | `def:b1:constrained-optimisation:constrained-max` | 2 | new (economic use; extrema under constraint are the mathematics series') |
| tangency condition | `def:b1:constrained-optimisation:tangency` | 2 | new |
| Lagrangian | `def:b1:constrained-optimisation:lagrangian` | 2 | new as used here (the method is admitted) |
| shadow price (Lagrange multiplier, economic reading) | `def:b1:constrained-optimisation:shadow-price` | 2 | new |
| value function | `def:b1:constrained-optimisation:value-function` | 2 | new |
| corner solution, interior solution | `def:b1:constrained-optimisation:corner` | 2 | new |
| binding constraint | `def:b1:constrained-optimisation:binding` | 2 | new |
| comparative statics | `def:b1:comparative-statics:comparative-statics` | 3 | new |
| point elasticity (elasticity as $\dd\ln y/\dd\ln x$) | `def:b1:comparative-statics:point-elasticity` | 3 | re-founded (g9 `elasticity-first-look`, g10 `elasticities`) |
| constant-elasticity function | `def:b1:comparative-statics:constant-elasticity` | 3 | new |
| envelope theorem | `thm:b1:comparative-statics:envelope` | 3 | new (`theorem`; the mathematics series' "envelope" of a family of curves is a different sense: `EXTRA_PROTECT` in Phase C) |
| sign prediction | `def:b1:comparative-statics:sign-prediction` | 3 | new |

## Part II --- The consumer

| Term(s) indexed | Label | Ch. | Status |
|---|---|---|---|
| preference relation (weak preference, strict preference, indifference) | `def:b1:preferences-and-utility:preference` | 4 | new |
| completeness, transitivity, rational preferences | `def:b1:preferences-and-utility:rational` | 4 | new |
| monotonicity (of preferences) | `def:b1:preferences-and-utility:monotone` | 4 | new |
| convex preferences | `def:b1:preferences-and-utility:convex` | 4 | new |
| indifference curve | `def:b1:preferences-and-utility:indifference-curve` | 4 | new (check Book 2's g10 `demand` Phase A list: not in the outline) |
| marginal rate of substitution | `def:b1:preferences-and-utility:mrs` | 4 | new |
| utility function, ordinal utility | `def:b1:preferences-and-utility:utility` | 4 | new (g12 `risk-and-insurance` uses a concave utility in words: contested, see report) |
| Cobb--Douglas utility | `def:b1:preferences-and-utility:cobb-douglas` | 4 | new |
| perfect substitutes, perfect complements | `def:b1:preferences-and-utility:perfect` | 4 | new |
| quasi-linear utility | `def:b1:preferences-and-utility:quasi-linear` | 4 | new |
| budget set, budget line | `def:b1:consumer-choice:budget` | 5 | new (g7 `households` owns the household budget in words) |
| demand function (Marshallian demand) | `def:b1:consumer-choice:demand-function` | 5 | new |
| Engel curve | `def:b1:consumer-choice:engel-curve` | 5 | new |
| normal good, inferior good | `def:b1:consumer-choice:normal-inferior` | 5 | re-founded (g10 `demand`) |
| indirect utility function | `def:b1:consumer-choice:indirect-utility` | 5 | new |
| Roy's identity | `thm:b1:consumer-choice:roy` | 5 | new (`theorem`) |
| revealed preference, weak axiom of revealed preference | `def:b1:consumer-choice:warp` | 5 | new |
| market demand | `def:b1:consumer-choice:market-demand` | 5 | re-founded (g10 `demand`: "from one buyer to the market") |
| endowment (of goods) | `def:b1:consumer-choice:endowment` | 5 | new |
| substitution effect, income effect | `def:b1:income-and-substitution-effects:effects` | 6 | new |
| compensated demand (Hicksian demand) | `def:b1:income-and-substitution-effects:compensated` | 6 | new |
| expenditure function | `def:b1:income-and-substitution-effects:expenditure` | 6 | new |
| Slutsky equation | `thm:b1:income-and-substitution-effects:slutsky` | 6 | new (`theorem`) |
| Giffen good | `def:b1:income-and-substitution-effects:giffen` | 6 | new |
| Engel aggregation, Cournot aggregation | `prop:b1:income-and-substitution-effects:aggregation` | 6 | new (`proposition`) |
| net substitutes, net complements | `def:b1:income-and-substitution-effects:net` | 6 | new |
| compensating variation | `def:b1:consumer-welfare:cv` | 7 | new |
| equivalent variation | `def:b1:consumer-welfare:ev` | 7 | new |
| consumer surplus | `def:b1:consumer-welfare:consumer-surplus` | 7 | re-founded (g10 `surplus-and-efficiency`) |
| true cost-of-living index | `def:b1:consumer-welfare:col-index` | 7 | new |
| substitution bias | `def:b1:consumer-welfare:substitution-bias` | 7 | contested (g10 `price-indices` covers "substitution": see report) |
| chained index | `def:b1:consumer-welfare:chained` | 7 | contested (g10 `price-indices`) |
| virtual price | `def:b1:consumer-welfare:virtual-price` | 7 | new |
| time endowment, full income | `def:b1:labour-supply-and-saving:full-income` | 8 | new |
| reservation wage | `def:b1:labour-supply-and-saving:reservation-wage` | 8 | new |
| labour supply function | `def:b1:labour-supply-and-saving:labour-supply` | 8 | re-founded (g11 `labour-market`: labour supply in words) |
| intensive margin, extensive margin | `def:b1:labour-supply-and-saving:margins` | 8 | new (Y3 `labour-supply-and-demand` recalls) |
| implicit marginal tax rate | `def:b1:labour-supply-and-saving:implicit-rate` | 8 | new (Y3 `transfers-and-incentives` recalls; Y3 owns *poverty trap*) |
| intertemporal budget constraint | `def:b1:labour-supply-and-saving:intertemporal-budget` | 8 | new (Y2 `intertemporal-choice` recalls; Y2 owns the Euler equation and discounting of utility) |
| household saving (two-period) | `def:b1:labour-supply-and-saving:household-saving` | 8 | new (national saving is ch. 19's) |

## Part III --- The firm

| Term(s) indexed | Label | Ch. | Status |
|---|---|---|---|
| production function, technically efficient | `def:b1:technology:production-function` | 9 | re-founded (g11 `production-and-costs`, one input; g12 aggregate) |
| isoquant | `def:b1:technology:isoquant` | 9 | new |
| marginal product | `def:b1:technology:marginal-product` | 9 | re-founded (g11 `production-and-costs`) |
| marginal rate of technical substitution | `def:b1:technology:mrts` | 9 | new |
| returns to scale (constant, increasing, decreasing) | `def:b1:technology:returns-to-scale` | 9 | re-founded (g12 `growth-and-production-function`: constant returns in words) |
| elasticity of substitution | `def:b1:technology:sigma` | 9 | new |
| Cobb--Douglas production function | `def:b1:technology:cobb-douglas` | 9 | re-founded (g12) |
| fixed-proportions production function | `def:b1:technology:leontief` | 9 | new |
| CES production function | `def:b1:technology:ces` | 9 | new |
| technical progress (Hicks-neutral, labour-augmenting, capital-augmenting) | `def:b1:technology:technical-progress` | 9 | new |
| isocost line | `def:b1:cost-minimisation:isocost` | 10 | new |
| conditional factor demand | `def:b1:cost-minimisation:conditional-demand` | 10 | new |
| cost function | `def:b1:cost-minimisation:cost-function` | 10 | new |
| Shephard's lemma | `thm:b1:cost-minimisation:shephard` | 10 | new (`theorem`; ch. 6 proves the consumer version, indexed there as part of the expenditure function's properties, not as a second term) |
| short-run cost function, long-run cost function | `def:b1:cost-minimisation:sr-lr` | 10 | re-founded (g11) |
| economies of scale | `def:b1:cost-minimisation:economies-of-scale` | 10 | re-founded (g11) |
| minimum efficient scale | `def:b1:cost-minimisation:mes` | 10 | new |
| learning curve, learning rate | `def:b1:cost-minimisation:learning-curve` | 10 | new (Y3 `environmental-and-resource-economics` recalls) |
| profit function | `def:b1:profit-maximisation:profit-function` | 11 | new |
| supply function (of a firm) | `def:b1:profit-maximisation:supply-function` | 11 | re-founded (g11 `perfect-competition`) |
| unconditional factor demand | `def:b1:profit-maximisation:factor-demand` | 11 | new |
| Hotelling's lemma | `thm:b1:profit-maximisation:hotelling` | 11 | new (`theorem`; Y3's Hotelling rule for resource prices is another result: `EXTRA_PROTECT` in Phase C, and Y3 should name it "the Hotelling rule") |
| shut-down price | `def:b1:profit-maximisation:shut-down` | 11 | re-founded (g11) |
| law of supply | `prop:b1:profit-maximisation:law-of-supply` | 11 | new (`proposition`) |
| industry supply | `def:b1:competitive-industry:industry-supply` | 12 | re-founded (g11) |
| free entry | `def:b1:competitive-industry:free-entry` | 12 | re-founded (g11 `perfect-competition`: entry and exit) |
| long-run industry supply | `def:b1:competitive-industry:lr-supply` | 12 | new |
| constant-cost industry, increasing-cost industry | `def:b1:competitive-industry:cost-industry` | 12 | new |
| economic rent | `def:b1:competitive-industry:rent` | 12 | new (one sense; "rent" of a flat is ordinary language: `STOP`/`EXTRA_PROTECT`) |
| quasi-rent | `def:b1:competitive-industry:quasi-rent` | 12 | new |
| capitalisation | `def:b1:competitive-industry:capitalisation` | 12 | new |

## Part IV --- Markets and price theory

| Term(s) indexed | Label | Ch. | Status |
|---|---|---|---|
| partial equilibrium | `def:b1:partial-equilibrium-welfare:partial` | 13 | new |
| stable equilibrium (of price adjustment) | `def:b1:partial-equilibrium-welfare:stable` | 13 | new |
| producer surplus, total surplus | `def:b1:partial-equilibrium-welfare:surplus` | 13 | re-founded (g10 `surplus-and-efficiency`) |
| deadweight loss (Harberger triangle) | `def:b1:partial-equilibrium-welfare:dwl` | 13 | re-founded (g10 `what-prices-do`); Y3 `efficiency-cost-of-taxation` should recall it and own *excess burden* only if it means something else (see report) |
| statutory incidence, economic incidence | `def:b1:partial-equilibrium-welfare:incidence` | 13 | re-founded (g10 `tax-incidence`) |
| pass-through rate | `def:b1:partial-equilibrium-welfare:pass-through` | 13 | new (Y3 `trade-policy` recalls for tariffs) |
| full price | `def:b1:price-theory-at-work:full-price` | 14 | new |
| parallel market | `def:b1:price-theory-at-work:parallel-market` | 14 | new |
| quota rent | `def:b1:price-theory-at-work:quota-rent` | 14 | new (Y3 `trade-policy` recalls) |
| arbitrage condition (spatial, intertemporal) | `def:b1:price-theory-at-work:arbitrage` | 14 | contested (g10 `what-prices-do` has "arbitrage and the single price": if Book 2 defines *arbitrage*, this becomes *arbitrage condition* only) |
| cost of carry, convenience yield | `def:b1:price-theory-at-work:carry` | 14 | new (the quant series defines futures terms; named in prose) |
| rental yield, rent--price arbitrage condition | `def:b1:price-theory-at-work:rental-yield` | 14 | new |
| Lerner index | `def:b1:monopoly-pricing:lerner` | 15 | new |
| markup | `def:b1:monopoly-pricing:markup` | 15 | re-founded (g11 `monopoly`: "the markup and the elasticity of demand") |
| price discrimination (first, second, third degree) | `def:b1:monopoly-pricing:discrimination` | 15 | re-founded (g11 `monopoly`, first look) |
| two-part tariff | `def:b1:monopoly-pricing:two-part` | 15 | new |
| bundling | `def:b1:monopoly-pricing:bundling` | 15 | new (g11 `public-goods-and-commons` uses "bundling" as a way to provide public goods: one sense? see report) |
| natural monopoly | `def:b1:monopoly-pricing:natural-monopoly` | 15 | re-founded (g11 `monopoly`) |
| average-cost pricing, price-cap regulation | `def:b1:monopoly-pricing:regulation` | 15 | new (Y3 `competition-policy` recalls) |
| derived demand | `def:b1:factor-markets:derived-demand` | 16 | new |
| marginal revenue product | `def:b1:factor-markets:mrp` | 16 | new |
| value of the marginal product | `def:b1:factor-markets:vmp` | 16 | re-founded (g11 `labour-market`) |
| monopsony (single buyer) | `def:b1:factor-markets:monopsony` | 16 | re-founded (g11 `labour-market`: "one large employer (first look)"); Y3 `minimum-wage` recalls |
| marginal cost of labour | `def:b1:factor-markets:mcl` | 16 | new |
| markdown | `def:b1:factor-markets:markdown` | 16 | new |
| rental price of capital | `def:b1:factor-markets:rental-price` | 16 | new (Y2 `investment` owns *user cost of capital*: see report) |
| factor share, labour share | `def:b1:factor-markets:factor-share` | 16 | re-founded (g12 `growth-and-production-function`: "the shares of income") |
| best-response function | `def:b1:cournot-and-bertrand:best-response` | 17 | contested (Y2 `static-games` defines *best response* in general: proposed that Y1 owns *best-response function* for oligopoly and Y2 recalls it) |
| Cournot equilibrium | `def:b1:cournot-and-bertrand:cournot` | 17 | new |
| Bertrand equilibrium, Bertrand paradox | `def:b1:cournot-and-bertrand:bertrand` | 17 | new |
| Stackelberg equilibrium (leader--follower) | `def:b1:cournot-and-bertrand:stackelberg` | 17 | new (Y2 `dynamic-games` recalls) |
| strategic substitutes, strategic complements | `def:b1:cournot-and-bertrand:strategic` | 17 | new |
| entry threshold | `def:b1:cournot-and-bertrand:entry-threshold` | 17 | new |

## Part V --- Macroeconomics: the long run

| Term(s) indexed | Label | Ch. | Status |
|---|---|---|---|
| institutional sector | `def:b1:national-accounts-in-depth:sector` | 18 | new |
| gross national income, disposable income | `def:b1:national-accounts-in-depth:gni` | 18 | re-founded (g10 `national-accounts`: national income) |
| net lending, net borrowing | `def:b1:national-accounts-in-depth:net-lending` | 18 | new |
| chain-linked volume | `def:b1:national-accounts-in-depth:chain-linked` | 18 | new |
| purchasing-power parity (of a basket) | `def:b1:national-accounts-in-depth:ppp` | 18 | contested (g9 `exchange-rates-and-purchasing-power`, g10 `national-accounts`; Y3 `exchange-rates` tests PPP as a theory: proposed that Y1 defines the *PPP conversion factor* as a measurement and Y3 owns *purchasing-power parity* as a theory) |
| statistical revision, benchmark revision | `def:b1:national-accounts-in-depth:revision` | 18 | new |
| long-run equilibrium (the long-run model) | `def:b1:long-run-model:long-run` | 19 | re-founded (g12 `aggregate-demand-and-supply`) |
| national saving, private saving, public saving | `def:b1:long-run-model:saving` | 19 | re-founded (g12 `saving-and-investment`) |
| loanable funds market | `def:b1:long-run-model:loanable-funds` | 19 | re-founded (g12) |
| crowding out | `def:b1:long-run-model:crowding-out` | 19 | re-founded (g12) |
| neutrality of money (monetary neutrality) | `def:b1:long-run-model:neutrality` | 19 | new |
| Solow model | `model` box in ch. 20 | 20 | re-founded (g12 `solow-first-look`) |
| steady state | `def:b1:solow-model:steady-state` | 20 | re-founded (g12) |
| Inada conditions | `def:b1:solow-model:inada` | 20 | new |
| golden-rule capital stock | `def:b1:solow-model:golden-rule` | 20 | new (Y2 `ramsey-model` owns the *modified golden rule*) |
| dynamic inefficiency | `def:b1:solow-model:dynamic-inefficiency` | 20 | new (Y2 `overlapping-generations` recalls) |
| speed of convergence, half-life | `def:b1:solow-model:speed` | 20 | new |
| capital per effective worker, balanced growth path | `def:b1:solow-model:balanced` | 20 | new |
| conditional convergence | `def:b1:solow-model:conditional-convergence` | 20 | re-founded (g12 "convergence"; Y3 `growth-empirics` recalls) |
| growth accounting | `def:b1:growth-accounting:growth-accounting` | 21 | re-founded (g12 `growth-and-production-function`) |
| Solow residual, total factor productivity | `def:b1:growth-accounting:tfp` | 21 | re-founded or new (g12 may define *total factor productivity*: see report) |
| development accounting (levels accounting) | `def:b1:growth-accounting:development-accounting` | 21 | new |
| misallocation | `def:b1:growth-accounting:misallocation` | 21 | new |
| separation rate, job-finding rate | `def:b1:unemployment-flows:rates` | 22 | contested (g11 `unemployment`: "flows into and out of unemployment") |
| steady-state unemployment rate | `def:b1:unemployment-flows:steady-state-rate` | 22 | re-founded (g11 natural rate) |
| expected unemployment duration | `def:b1:unemployment-flows:duration` | 22 | new |
| efficiency wage, no-shirking condition | `def:b1:unemployment-flows:efficiency-wage` | 22 | new |
| Beveridge curve | `def:b1:unemployment-flows:beveridge` | 22 | contested (Y2 `search-and-unemployment` also lists it: proposed Y1 owns it, Y2 recalls and owns the *matching function*) |
| money demand function | `def:b1:money-and-inflation:money-demand` | 23 | new |
| velocity of money | `def:b1:money-and-inflation:velocity` | 23 | contested (g12 `inflation-and-money` owns the quantity equation and probably velocity: then recalled here) |
| quantity theory of money | `def:b1:money-and-inflation:quantity-theory` | 23 | new as a theory (the *quantity equation* stays g12's) |
| seigniorage, inflation tax | `def:b1:money-and-inflation:seigniorage` | 23 | new (Y3 `inflation-evidence` recalls) |
| hyperinflation | `def:b1:money-and-inflation:hyperinflation` | 23 | contested (g12 `inflation-and-money` discusses hyperinflations: if it defines the term, recalled here) |
| Fisher effect | `def:b1:money-and-inflation:fisher` | 23 | new (the Fisher *relation* $r \approx i - \pi^e$ is in the notation table and g12) |

## Part VI --- The short run

| Term(s) indexed | Label | Ch. | Status |
|---|---|---|---|
| IS curve | `def:b1:is-lm:is` | 24 | new (Y2 `three-equation-model` recalls) |
| LM curve | `def:b1:is-lm:lm` | 24 | new |
| IS--LM model | `model` box in ch. 24 | 24 | new (re-founds g12's short-run toy model) |
| liquidity trap, zero lower bound | `def:b1:is-lm:liquidity-trap` | 24 | new (g12 `monetary-policy` names the zero lower bound in words: contested; Y2 `three-equation-model` recalls) |
| MP curve, interest-rate rule | `def:b1:is-lm:mp` | 24 | new (Y2 recalls) |
| fiscal multiplier (in IS--LM) | `def:b1:is-lm:fiscal-multiplier` | 24 | re-founded (g12 `keynesian-cross` owns the multiplier) |
| short-run aggregate supply curve | `def:b1:aggregate-supply:sras` | 25 | re-founded (g12 `aggregate-demand-and-supply`) |
| aggregate demand curve | `def:b1:aggregate-supply:ad` | 25 | re-founded (g12) |
| Okun's law | `def:b1:aggregate-supply:okun` | 25 | new (label of an empirical regularity) |
| expectations-augmented Phillips curve | `def:b1:aggregate-supply:phillips` | 25 | re-founded (g12 `phillips-curve`) |
| adaptive expectations | `def:b1:aggregate-supply:adaptive` | 25 | new (Y2 `expectations-and-lucas-critique` recalls and owns *rational expectations*) |
| sacrifice ratio | `def:b1:aggregate-supply:sacrifice-ratio` | 25 | new (g12 `phillips-curve` covers "the cost of bringing inflation down": contested if it defines the term) |
| supply shock, demand shock | `def:b1:aggregate-supply:shocks` | 25 | contested (g12 `aggregate-demand-and-supply`: probably owner; then recalled) |
| policy lag (inside lag, outside lag) | `def:b1:stabilisation-policy:lags` | 26 | new |
| policy rule, discretion (Taylor rule) | `def:b1:stabilisation-policy:rule` | 26 | contested (g12 `monetary-policy`: "rules and discretion"; Y2 owns time inconsistency) |
| output gap | `def:b1:stabilisation-policy:output-gap` | 26 | contested (g12 `aggregate-demand-and-supply` likely; then recalled) |
| automatic stabiliser | `def:b1:stabilisation-policy:automatic-stabiliser` | 26 | contested (g12 `fiscal-policy-and-debt` owns it in the outline: then recalled, no definition here) |
| local multiplier (relative multiplier) | `def:b1:stabilisation-policy:local-multiplier` | 26 | new |
| net foreign asset position | `def:b1:open-economy:nfa` | 27 | new (Y3 `current-account` recalls) |
| real exchange rate | `def:b1:open-economy:real-exchange-rate` | 27 | contested (g12 `exchange-rates-and-balance-of-payments`) |
| Marshall--Lerner condition | `def:b1:open-economy:marshall-lerner` | 27 | new |
| small open economy | `def:b1:open-economy:small-open` | 27 | new |
| Mundell--Fleming model | `model` box in ch. 27 | 27 | new (Y3 Part III recalls) |
| trilemma (impossible trinity) | `def:b1:open-economy:trilemma` | 27 | contested (g12 "the three aims that cannot all be met (told)"; Y3 `exchange-rate-regimes` tests it: proposed Y1 owns, Y3 recalls) |

## Part VII --- Data and statistics, in Python

| Term(s) indexed | Label | Ch. | Status |
|---|---|---|---|
| cross-section, time series, panel data (as data structures) | `def:b1:economic-data-python:shapes` | 28 | contested (Y3 `panel-data` and Y2 `time-series`: proposed Y1 owns the data structures, Y2 owns *stationarity* and the time-series models, Y3 owns *fixed effects* etc.) |
| unit of observation | `def:b1:economic-data-python:unit` | 28 | new |
| merge key | `def:b1:economic-data-python:key` | 28 | new (the computer science series defines database keys: economics use only; `EXTRA_PROTECT` if a collision appears) |
| seasonal adjustment, seasonal factor | `def:b1:economic-data-python:seasonal` | 28 | new (Y2 `time-series` recalls) |
| annualised rate | `def:b1:economic-data-python:annualised` | 28 | new |
| reproducible computation | `def:b1:economic-data-python:reproducible` | 28 | new |
| histogram (as a density estimate) | `def:b1:describing-data:histogram` | 29 | check the mathematics harvest at writing (none found in Phase A) |
| empirical distribution function | `def:b1:describing-data:edf` | 29 | new |
| quantile, percentile | `def:b1:describing-data:quantile` | 29 | new (quartile and median are the mathematics series') |
| skewness | `def:b1:describing-data:skewness` | 29 | new |
| sample covariance, correlation coefficient | `def:b1:describing-data:correlation` | 29 | new (descriptive; covariance of random variables is the mathematics series', Year 2) |
| conditional mean (in data) | `def:b1:describing-data:conditional-mean` | 29 | new |
| composition effect, Simpson's paradox | `def:b1:describing-data:simpson` | 29 | new |
| top-coding, censoring | `def:b1:describing-data:top-coding` | 29 | new |
| outlier, trimmed mean | `def:b1:describing-data:outlier` | 29 | new |
| joint distribution, conditional distribution | `def:b1:random-variables-for-econometrics:joint` | 30 | check the mathematics harvest at writing (none found in Phase A; Year 2 mathematics has random vectors?) |
| conditional expectation | `def:b1:random-variables-for-econometrics:conditional-expectation` | 30 | new (the quant series defines it too: no conflict, links are per book) |
| law of iterated expectations | `thm:b1:random-variables-for-econometrics:lie` | 30 | new (`theorem`) |
| mean independence | `def:b1:random-variables-for-econometrics:mean-independence` | 30 | new |
| chi-square distribution, Student's $t$ distribution, $F$ distribution | `def:b1:random-variables-for-econometrics:laws` | 30 | new |
| sampling distribution | `def:b1:random-variables-for-econometrics:sampling-distribution` | 30 | new |
| population parameter | `def:b1:sampling-and-inference:population` | 31 | new (the mathematics series' *sample* (g10) is recalled) |
| estimator, unbiased estimator, consistent estimator | `def:b1:sampling-and-inference:estimator` | 31 | new (Y2 `regression-inference` recalls) |
| mean squared error | `def:b1:sampling-and-inference:mse` | 31 | new |
| standard error | `def:b1:sampling-and-inference:standard-error` | 31 | new |
| confidence interval | `def:b1:sampling-and-inference:confidence-interval` | 31 | new (check the mathematics g10--g12 sampling chapters at writing: "fluctuation interval" exists there, a different object) |
| null hypothesis, alternative hypothesis, test statistic | `def:b1:sampling-and-inference:test` | 31 | new |
| significance level (size), $p$-value | `def:b1:sampling-and-inference:p-value` | 31 | new |
| power (of a test) | `def:b1:sampling-and-inference:power` | 31 | new |
| family-wise error rate | `def:b1:sampling-and-inference:fwer` | 31 | new (Y3 `credible-empirical-work` recalls) |
| stratified sample, sampling weight, design effect | `def:b1:sampling-and-inference:weights` | 31 | new |
| population regression line (best linear predictor) | `def:b1:simple-regression:population-line` | 32 | new |
| ordinary least squares estimator | `def:b1:simple-regression:ols` | 32 | new (Y2 `multiple-regression` owns the matrix form and recalls the name) |
| fitted value, residual | `def:b1:simple-regression:residual` | 32 | new |
| error term | `def:b1:simple-regression:error` | 32 | new |
| coefficient of determination ($R^2$) | `def:b1:simple-regression:r2` | 32 | new |
| zero conditional mean assumption | `def:b1:simple-regression:zcm` | 32 | new |
| regression toward the mean | `def:b1:simple-regression:toward-mean` | 32 | new |
| omitted variable (confounder) | `def:b1:simple-regression:omitted` | 32 | new (Y2 owns the *omitted-variable bias formula*) |
| reverse causation | `def:b1:simple-regression:reverse` | 32 | new |

About 210 indexed terms in about 165 definitions. One sense per word (`SERIES_DEFINITIONS.md` rule 6): *rent* (economic
rent against the rent of a flat), *margin* (intensive margin, price--cost margin), *surplus* (consumer surplus; no budget
surplus is defined here), *index* (price index, Lerner index), *bias* (substitution bias, statistical bias), *parameter*
(model parameter in ch. 1, population parameter in ch. 31: both definitions name the qualified form), *capital* (physical
here; human capital recalled from g11), *power* (of a test only), *population* (statistical, against people). Each goes to
`STOP` or `EXTRA_PROTECT` in Phase C.
