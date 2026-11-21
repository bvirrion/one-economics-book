# Series definition map and notation --- One Economics Book

Which book and chapter **owns** each defined term, meaning the chapter that carries its `\emph{term}\index{term}` pair inside a
`definition`. The main session owns this file. Book writers read it and never edit it; they report at their sync.

Term links are generated **per book**, so a book can link only a term it defines itself. The rules are these.

1. **Books 1 and 2 (grades 6–12) never repeat themselves.** Together they follow the outline's "Notion-ownership map,
   Books 1–2": one owner chapter for each notion across the seven school years. A later chapter, in the same book or in
   Book 2, opens with a `recall` box and uses the word without a new `\emph{}\index{}` pair. In Book 2, Book 1's notions are
   named in prose ("as the grades 6–9 volume showed"). Book 2 therefore does not link the Book 1 words it recalls.
2. **Books 3–5 (Years 1–3).** Each notion has exactly **one owner across the three university books**. A university book may
   **re-found** a school notion: it defines the notion again, with calculus, in the chapter the outline names in its table
   "From school to university". It never defines a notion owned by another university book. It uses the owner's word with a
   prose pointer ("defined in the Year 1 volume"), never a `\cref`.
3. **Notions owned by another series** (the outline's "Owned by another series") are never defined here. A `recall` box names
   the series in prose ("the mathematics books show that…") and states what is used, and the chapter takes the economic angle.
   Watch for terms that sound like mathematics or statistics, such as derivative, partial derivative, Lagrange multiplier,
   expectation, variance, regression line, matrix, exponential or logarithm, and grep the sister series' harvest before
   defining one.
4. **A term in no map** goes to the **earliest chapter** that needs it: by grade in Books 1–2, and in the lowest-numbered
   university book across Books 3–5. The main session settles contested terms at a sync and writes the ruling below.
5. **Harvester rule.** `\index{}` appears only beside the `\emph{}` of a term the chapter owns, inside a `definition`, and
   nowhere else. A model this series owns (Ricardo's model, the Solow model, IS–LM, the three-equation model) is indexed in its
   `model` box or its `definition`, in the owner chapter only.
6. **One sense per word in a book.** Economics reuses everyday words. For example:
   - a *market*, a *good*, *capital* (physical, human or financial);
   - *interest* (the rate, or "of interest"), a *return*, a *share* (an equity, or "a share of");
   - a *margin*, a *surplus* (consumer surplus, or a budget surplus), a *deficit*, an *account* (the current account, or a bank
     account);
   - a *bias* (statistical or behavioural), an *index* (a price index, or the book's index), *utility* (preferences, or a
     power company).

   When a book needs two senses, the definition names the qualified form (*consumer surplus*, *budget deficit*, *current
   account*, *human capital*, *price index*). The writer then adds the bare word to its term config's `STOP` or
   `EXTRA_PROTECT` in Phase C, so that a link never lands on the wrong sense.

## Series notation (fixed at the scaffold, 2026-11-20; Year 1 prints it in `b1` ch. 1's notation table)

Every book uses these symbols. Books 1–2 use only the ones their mathematics allows, and write words where a symbol would come
too early. A chapter that needs another symbol defines it locally in a `notation` box. It never reuses a symbol below for
something else.

| Symbol | Meaning | Remarks |
|---|---|---|
| $p$, $q$ | price, quantity of one good | $p_1, q_1$… for several goods; $P$ the price level |
| $Q^d$, $Q^s$ | quantity demanded, supplied | $D$, $S$ name the curves in diagrams |
| $x_1, x_2$; $u(x_1,x_2)$ | consumer's quantities; utility | $m$ income (Years 1–3), $\lambda$ a Lagrange multiplier |
| $\varepsilon$ | an elasticity | $\varepsilon_d$, $\varepsilon_s$; an error term is $u_i$ or $e_t$ in econometrics, never $\varepsilon$ |
| $Y$ | output, real GDP, real income | $y = Y/L$ output per worker; $Y^*$ or $\bar Y$ potential output |
| $C$, $I$, $G$, $X$, $M$, $NX$ | consumption, investment, government purchases, exports, imports, net exports | $T$ taxes net of transfers; $S$ saving |
| $K$, $L$, $A$, $H$ | capital, labour, productivity (technology), human capital | $k = K/L$; $\delta$ depreciation rate; $s$ saving rate; $n$ population growth; $g$ growth of $A$ |
| $\alpha$ | capital's share in a Cobb–Douglas function | $Y = A K^{\alpha} L^{1-\alpha}$ |
| $w$, $W$ | real wage, nominal wage | $r$ rental rate of capital in the firm's problem |
| $i$, $r$ | nominal interest rate, real interest rate | $r \approx i - \pi^e$ (Fisher); $i^*$ foreign rate |
| $\pi$, $\pi^e$ | inflation, expected inflation | profit is $\Pi$ (capital pi), never $\pi$ |
| $u$, $u^n$ | unemployment rate, natural rate | |
| $M$ (money) | money supply in monetary chapters | where $M$ (imports) would clash, the chapter writes $M^s$ for money and says so |
| $e$, $\varepsilon_r$ | nominal exchange rate (domestic per foreign), real exchange rate | the series' convention: a rise of $e$ is a depreciation of the home currency |
| $\beta$ | discount factor (Years 2–3) | regression coefficients are $\beta_0, \beta_1$…, hats for estimates |
| $t$ | time (an index); $\tau$ a tax rate | |
| $MC$, $AC$, $AVC$, $MR$, $TR$, $TC$, $FC$ | marginal cost, average cost, average variable cost, marginal revenue, total revenue, total cost, fixed cost | upright in display: `$\mathit{MC}$` is wrong, write `$MC$` |
| $CS$, $PS$, $DWL$ | consumer surplus, producer surplus, deadweight loss | |

Money: real currencies print as `\usd{12.5}` and `\eur{40}`. Brenland's dalens print as `\dal{120}` and Kestria's kests as
`\kst{80}`, never as a bare `$`.

## Seed (2026-11-20)

The binding seed is the outline's three ownership tables, approved by the user. They are not copied here, so that they cannot
drift. The sync below adds only what the tables leave unsaid.

What the outline already settles, and every writer must know:

- **The mathematics series owns** (recall, never define): percentages and chart reading (g6); powers (g8); weighted averages
  (g8); affine functions (g9); mean and median (g9); linear systems (g10); quadratics (g11); the derivative (g11); sequences
  (g11–g12); quartiles and standard deviation (g11); the logarithm, the exponential and the integral (g12); partial
  derivatives (Y1); Lagrange's method (used as admitted in Y1, proved in the mathematics Y2); matrices (Y2); expectation,
  variance and the normal law (Y1–Y2); the central limit theorem (admitted).
- **The economics series owns** the economic objects built on these. Examples: the times-ten scale (g6), compound growth and
  doubling time (g8), the price index (g8), elasticity (g9), the Lorenz curve and the Gini coefficient (g11), marginal
  quantities (g11), and discounting and the multiplier (g12).
- **The Earth and space sciences series owns** the physical climate. This series takes the economics of emissions and
  resources.
- **The quant series** is named in prose only, as further reading on finance.

## Harvest commands

```sh
perl -0777 -ne 'while(/\\emph\{([^}]*)\}\s*\\index\{([^}]*)\}/g){($t=$2)=~s/\s+/ /g; print "$ARGV\t$t\n"}' parts/grade-*/[0-9]*.tex
perl -0777 -ne 'while(/\\emph\{([^}]*)\}\s*\\index\{([^}]*)\}/g){($t=$2)=~s/\s+/ /g; print "$ARGV\t$t\n"}' parts/bachelor-*/[0-9]*.tex
for s in math physics; do
  perl -0777 -ne 'while(/\\emph\{([^}]*)\}\s*\\index\{([^}]*)\}/g){($t=$2)=~s/\s+/ /g; print "$ARGV\t$t\n"}' \
    ../one-$s-book/parts/*/[0-9]*.tex
done | grep -i '<term>'
```

## Sync decisions (2026-11-20)

The five `sources/book<N>/DEFINITIONS.md` files of Phase A are the detailed lists. **Book 1's list is frozen for
Book 2; Book 3's list is frozen for Books 4 and 5; Book 4's list is frozen for Book 5.** A later book recalls every
term on an earlier frozen list (in prose, with no definition pair), except where a ruling below says otherwise. A
writer whose list contradicts a ruling corrects its `DEFINITIONS.md` before the chapter concerned.

### R1. Re-founding at university (clarifies rule 2)

A university book may define a school notion again **when it gives the notion its formal definition** (an equation, a
derivation, a model) in the chapter where the year's treatment lives, because the school books' links do not reach a
university book. It never re-teaches the school treatment. Book 3 chooses, term by term, between re-founding and
recalling; Book 3's own proposal to recall several Book 2 terms (automatic stabiliser, output gap, supply and demand
shocks, velocity, real exchange rate, substitution bias, chained index, sacrifice ratio, deflator) is accepted.
**Among the three university books, each term still has exactly one owner** (the rulings below).

### R2. Books 1 and 2: one owner each

| Term | Owner | The other book |
|---|---|---|
| average tax rate, marginal tax rate | g8 `taxes-and-public-spending` | g11 `marginal-reasoning` recalls |
| barrier to entry, monopoly, natural monopoly | g8 `competition-and-monopoly-first-look` | g11 `monopoly` recalls; may state the cost condition as a proposition |
| capital per worker, physical capital | g8 `production-and-productivity` | g12 recalls; Book 2 owns *human capital* (g11) |
| consumer price index, basket, base year | g8 `inflation-and-price-indices` | g10 `price-indices` owns Laspeyres index, deflator, substitution bias, chained index |
| real GDP | g8 | g10 `national-accounts` recalls; owns nominal GDP, the GDP deflator and the expenditure identity |
| disposable income (of a household) | g7 `households` | g11 recalls |
| hyperinflation | g8 | g12 recalls |
| import quota, tariff, trade balance | g9 `international-trade` | g12 recalls; g11's *individual transferable quota* is a different, qualified term |
| export, import | g6 `a-connected-world` | everyone recalls |
| growth rate, average annual growth rate | g8 `growth-and-compounding` | g12 recalls (`average-growth-rate` is dropped from Book 2) |
| patent | g8 | g12 recalls |
| correlation (the notion), natural experiment | g9 `institutions-and-prosperity` | g10 `economic-models` recalls |
| price elasticity of demand, elastic, inelastic, **unit-elastic** | g9 `elasticity-first-look` | g10 `elasticities` owns arc, point, income, cross-price elasticities and supply elasticity |
| shortage, (market) surplus | g7 `markets-and-prices` | g10 owns *excess demand* and *excess supply* as the quantities $Q^d - Q^s$ |
| price floor, price ceiling | g9 | g10, g11 recall; g11 `labour-market` owns *minimum wage* |
| sunk cost, gains from trade, property rights, opportunity cost | Book 1 (g7, g7, g9, g7) | Book 2 recalls |
| real interest rate | g10 `price-indices` | g12 `present-value` recalls; Book 1 says it in words only |
| purchasing-power conversion (a measurement) | g9 | g12 owns *purchasing-power parity* (a hypothesis) |
| wage, household income | g7 | everyone recalls |
| Engel's law | g7 `households` | recall |
| model | g10 `economic-models` | Book 1 uses `model` boxes without defining the word |

**Two homographs.**
- *Depreciation*: Book 1 g9 defines *depreciation (of a currency)*; Book 2 g10 defines *depreciation (of capital)*. Each
  `\index{}` carries its qualifier, and each book puts the bare word in `STOP` in Phase C.
- *Share*: Book 1 g6 defines *share (of a total)*; Book 2 g12 defines *share (in a company)*.

### R3. Books 3, 4 and 5: one owner each

| Term | Owner | Others |
|---|---|---|
| best-response function (oligopoly), Cournot, Bertrand and Stackelberg equilibria | Y1 ch. 17 | Y2 recalls |
| best response (general), Nash equilibrium (general, at university), Bayesian Nash equilibrium | Y2 `static-games`, `bayesian-games` | Y1 names Nash from school in prose; Y3 recalls |
| intertemporal budget constraint, intensive and extensive margins | Y1 ch. 8 | Y2 and Y3 recall |
| discount factor, rate of time preference, Euler equation | Y2 `intertemporal-choice` | Y1 does not define them |
| arbitrage, arbitrage condition | Y1 ch. 14 | Y2 ch. 4 defines *no-arbitrage pricing* and the *stochastic discount factor* |
| law of one price | Y2 ch. 4 | Y3 `exchange-rates` recalls; Y3 owns *purchasing-power parity (the theory)*; Y1 defines only the *PPP conversion factor* (a measurement) |
| Pareto efficiency, Pareto improvement | Y2 ch. 6 and 9 | Y1 uses "efficient" in the surplus sense, without the Pareto pair |
| rental price of capital | Y1 ch. 16 | Y2 owns *user cost of capital* |
| policy rule, discretion, adaptive expectations, IS, MP, trilemma | Y1 | Y2 owns *Taylor rule*, *Taylor principle*, *rational expectations*, *time inconsistency*; Y3 recalls the trilemma |
| Beveridge curve, job-finding rate, separation rate, efficiency wage | Y1 ch. 22 | Y2 owns *matching function* and *vacancy-filling rate* |
| ordinary least squares estimator (the name, simple regression), omitted variable (confounder), correlation coefficient | Y1 ch. 29–32 | Y2 owns the *normal equations*, the matrix form, *omitted-variable bias*, *semi-elasticity*, *weak stationarity*, *selection bias*; Y3 owns *fixed effects* and the causal designs |
| cross-section, time series, panel data (as data structures) | Y1 ch. 28 | Y2 and Y3 recall |
| phase diagram | Y2 ch. 23 | Y1's Solow diagram does not define the term |
| seigniorage, inflation tax, hyperinflation, velocity, quantity theory | Y1 ch. 23 | Y3 `inflation-evidence` recalls (it drops its seigniorage and hyperinflation pairs) |
| markup | Y1 ch. 15 | Y3 recalls |
| quota rent | Y1 ch. 14 | Y3 `trade-policy` owns *import quota* (at university) and its trade terms |
| collusion, collusive equilibrium, tacit collusion | Y2 ch. 13 | Y3 ch. 27 recalls; Y3 owns *cartel* at university and *HHI* |
| first-price and second-price auctions, common-value auction, independent private values, revenue equivalence theorem (stated) | Y2 ch. 14 | Y3 ch. 28 recalls, proves revenue equivalence as a proposition, and owns *English* and *Dutch auctions* and *optimal reserve price* |
| old-age dependency ratio, PAYG pension, replacement rate | Y2 ch. 22 | Y3 recalls |
| median voter theorem, inflation targeting, central-bank independence, specification search | Y2 | Y3 recalls; Y3 owns *publication bias* and *pre-registration* |
| adverse selection, moral hazard, externality, public good, club good, transaction cost, actuarially fair premium, bank run, lender of last resort, primary balance | Y2 (re-founding the school notions) | Y3 recalls |
| uncovered interest parity, exchange-rate regime, peg, macroprudential policy, marginal abatement cost, Hotelling rule | Y3 | — |
| deadweight loss (Harberger triangle) | Y1 ch. 13 | Y3 recalls it; *excess burden* is used in prose as its synonym for a tax, and Y3 owns the *marginal cost of public funds* |

**AI series overlap.** Y3 defines *logit model*, *maximum likelihood estimator* and *optimal reserve price* for economics,
and may name the AI books in prose; this is allowed.

**Names in Book 5.** Y3 defines *accounting price*, not "shadow price" (Y1's Lagrange multiplier), and it keeps *Ramsey
rule (taxation)* and *Ramsey formula (discounting)* apart from Y2's Ramsey model.

**Words with two senses.** Each book's own list (Book 4: risk premium/equity premium, selection bias/adverse
selection, and the others) gets `STOP`/`EXTRA_PROTECT` entries in Phase C.
