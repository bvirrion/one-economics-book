# One Economics Book — outline of the five books

Status: **outline written 2026-11-20; nothing is scaffolded or written yet.** The
user set the editorial line on 2026-11-19 (`../economics_series.md`) and, on
2026-11-20, the shape (five books, from grade 6), the sequence, the place of code
and the handling of open questions, then approved the chapter list in summary
form. The per-chapter descriptions below are the first full draft and await
review. Provenance of every chapter is in `sources/outline_sources.md`.

## The series

| Book | Years (parts) | Covers | Chapters |
|---|---|---|---|
| 1 | Grades 6–9 (`grade-6` … `grade-9`) | the world in twenty charts; then choice, trade, money, prices, firms, the whole economy, markets with a first algebra, the world economy | 30 |
| 2 | Grades 10–12 (`grade-10` … `grade-12`) | the economics of the high-school course, on the international *principles* sequence: markets, firms, market failure and government failure, labour, money, growth, the short run, the open economy | 40 |
| 3 | University Year 1 (`bachelor-1`) | first-year economics degree ∪ the economics of the business preparatory class: intermediate microeconomics and macroeconomics, statistics and data in Python | 32 |
| 4 | University Year 2 (`bachelor-2`) | second-year degree: uncertainty, general equilibrium, game theory, information; macroeconomic dynamics; econometrics I | 34 |
| 5 | University Year 3 (`bachelor-3`) | third-year degree: econometrics II and the fields (trade, international macroeconomics, money, public economics and public choice, labour, industrial organisation, growth, development, environment) | 36 |
| | | | **172** |

(The column "Covers" names the source programmes for this file only. The
printed books never name a programme, a country or a university.)

There is no volume for grades 1–5: the series starts in grade 6, so Book 1 has
four parts. Estimated sizes: about 300, 420, 430, 460 and 490 pages, 2,100 in
all.

Rules this outline already obeys:

- **Models that work** (user, 2026-11-19). The series teaches mathematical
  models, with microeconomics and macroeconomics at the centre, and the data
  that test them. It is pure economics: no sociology and no political science.
- **Every model gets the same frame.** A `model` box states four things: what
  the model assumes, what it predicts, where it was tested, and where it breaks.
  Supply and demand, Ricardo's model, the Solow model, the Keynesian cross,
  IS–LM and the three-equation model all get it. Book 1 uses the frame in plain
  words from grade 7; grade 10 `economic-models` owns the notion of a model.
- **Facts before models.** Book 1 opens with a part of twenty-one charts and no
  model (grade 6). Every later chapter opens with one chart, named below as
  *Opening chart*, and the chapter explains it. Description is kept apart from
  cause: the charts show what happened, and the econometrics parts (Years 1–3)
  teach how a cause is established. The selection is not limited to the
  comfortable facts: falling world poverty and rising inequality inside some
  countries both go in.
- **The books teach how the numbers are made**: price indices, real and nominal
  values, purchasing-power adjustment, what income per person leaves out, how a
  poverty line and an unemployment rate are defined.
- **Ricardo and comparative advantage get real weight**: opportunity cost and
  gains from trade open grade 7, Ricardo's model is the first full model of
  grade 10, and Year 3 gives it a part of its own with the tests.
- **Keynesian models are toy models with their limits stated.** The Keynesian
  cross (grade 12), IS–LM (Year 1) and the three-equation model (Year 2) are
  taught next to the long-run model and the record: the stagflation of the
  1970s, the Volcker disinflation, 2008, and the inflation of 2021–23. What the
  record refuted is taught as refuted: a large fixed multiplier, the Phillips
  curve as a stable trade-off, fine-tuning, and "deficits don't matter".
- **No history of economic thought and no schools of thought.** A person's name
  appears only as the name of a model or a result, as Pythagoras does in the
  mathematics books. There are no `history` boxes. Marxist economics, the
  regulation school, post-Keynesian economics, the economy of conventions and
  degrowth do not appear.
- **No prescriptive chapters.** No title or section asks what "should" be done.
  The economics that such chapters carry stays: tax incidence, externalities,
  labour-market models.
- **The state is not the default fix.** A market-failure chapter shows private
  and contractual answers (bargaining, property rights, clubs, warranties,
  community rules) next to taxes and regulation, each with its evidence.
  Government failure has its own chapters beside them: grade 11
  `public-choice-first-look`, then Year 3 Part V.
- **Two results kept without the theory they answered** (user, 2026-11-19).
  That prices carry information nobody could gather centrally is taught as a
  positive result (g7 `markets-and-prices`, g10 `what-prices-do`, Y2
  `prices-as-information`). Planned and market economies are compared as data:
  the two Germanys, the two Koreas, China before and after 1978 (g9
  `institutions-and-prosperity`, Y3 `institutions`).
- **The international sequence** (user, 2026-11-20): principles (Books 1–2),
  intermediate microeconomics and macroeconomics (Years 1–2), econometrics
  (Years 1–3), then the fields (Year 3). Strengthened, each with chapters of its
  own: price theory, public choice, monetarism and rational expectations with
  the Lucas critique, and the incentive effects of taxes and transfers.
- **Open questions go in `debate` boxes, on evidence only** (user, 2026-11-20).
  A `debate` box is used where the evidence leaves a question open: the
  employment effect of a minimum wage, the size of fiscal multipliers, trade and
  wages. It gives the competing estimates, each with its best study and its
  weaknesses. It never holds a normative debate.
- **Code: Python from Year 1** (user, 2026-11-20). Books 1–2 print charts and
  tables and no code. From Year 1 the data and econometrics chapters print
  Python from tested files, with captured output, as the quant and computer
  science series do.
- **Data rules.** Every chart is redrawn from a tested script; no chart image is
  copied. Every external fact goes through a source ledger with its URL and
  access date. Volatile facts go in `dated` boxes. **No dataset is downloaded
  without the user's approval**; the proposed sources are listed near the end of
  this file. Exercises use invented data from a seeded script.
- **Books 1 and 2 never repeat themselves.** Every notion has one owner chapter,
  the earliest year where it fits. A later chapter that needs it opens with a
  3–5 line *You already know* recall box and adds only what is new (ownership
  map at the end). The university books may re-found a school notion with
  calculus, but never re-teach it at the school level.
- **Overlaps: recall, then build.** Where *One Math Book* or another series owns
  a notion (cross-series table at the end), that series stays the owner. A
  chapter here opens with a `recall` box that names it in prose, never with a
  `\cref`.
- **Level guard.** No chapter uses mathematics that the same year of the
  mathematics series has not reached. Percentages and charts from grade 6;
  powers in grade 8; affine functions and one-unknown equations in grade 9;
  linear systems in grade 10; derivatives and sequences in grade 11; limits,
  exponential, logarithm, integral and continuous distributions in grade 12;
  partial derivatives in Year 1; matrices for regression from Year 2. Long-run
  charts before grade 12 use a *times-ten scale*, taught as chart reading with
  no logarithm. Lagrange's method is used in Year 1 as an admitted method (the
  mathematics book proves it in Year 2). The central limit theorem is used as
  admitted.
- **Family chapter style**: definitions, methods, propositions with proofs,
  examples, starred exercises and a weekend problem, as in the mathematics and
  physics books.
- Printed text never names a curriculum, a country's school system or a
  university. Provenance lives in `sources/outline_sources.md` and in source
  comments only.

Chapter slugs below are the future file names (`parts/<year>/NN-<slug>.tex`)
and label stems (`ch:<g7|b1…>:<slug>`).

---

## Book 1 — Grades 6–9

### Grade 6 — The world in twenty charts

This part has no model. Each chapter reads three charts, says how each number is
made, and states what the chart shows and what it cannot show.

1. **Reading Economic Charts** — `reading-economic-charts`
   A quantity followed over time; a total and the same total per person; a share
   in percent; a rate of change; the *times-ten scale*, where each gridline is
   ten times the one below and equal steps mean equal ratios; the source line
   under a chart; a chart shows what happened, not why.
   *Charts:* world population over two centuries; the same series by region as
   shares; one series drawn on an ordinary scale and on a times-ten scale.
2. **Two Hundred Years of Living Standards** — `living-standards`
   Income per person: almost flat for centuries, then a take-off; who took off
   first, who caught up later, who has not yet; what an hour of work buys
   (bread, light) then and now; an average hides differences inside a country.
   *Charts:* world income per person over the long run; income per person by
   region since 1820; six countries that caught up, or did not, since 1950.
3. **Poverty and How It Is Counted** — `poverty`
   A poverty line as the cost of a basket of needs; the extreme-poverty line used
   for world comparisons and the higher lines countries set for themselves; the
   share of people below the line and the number of people, which can move in
   opposite directions when population grows; where the poorest live.
   *Charts:* share of the world in extreme poverty over two centuries; number of
   people in and out of extreme poverty; the share by region since 1990.
4. **Longer Lives, Smaller Families** — `health-and-population`
   Life expectancy at birth and what it averages; child mortality; births per
   woman; why population grew fast and why its growth is slowing; an ageing
   population: fewer workers for each retired person.
   *Charts:* life expectancy by region since 1800; child mortality against
   income per person; births per woman by region since 1950.
5. **School and Work** — `school-and-work`
   Literacy and years of schooling; hours worked in a year; the move from farms
   to factories to services; women in paid work; child labour then and now.
   *Charts:* literacy over two centuries; yearly hours per worker since 1870;
   shares of workers in farming, industry and services in one country over two
   centuries.
6. **Food and Energy** — `food-and-energy`
   Crop yields per hectare; the decline of famine; the share of a household's
   spending that goes to food falls as income rises; energy used per person
   against income; air pollution and carbon dioxide emissions as countries get
   richer.
   *Charts:* cereal yields since 1900; food share of spending against income per
   person; energy use per person against income per person.
7. **A Connected World** — `a-connected-world`
   Trade as a share of world output and its two waves; the falling cost of
   moving goods and information; goods that became thousands of times cheaper
   (light, computing, a solar panel); a first look at prices over time, taken up
   in a later year.
   *Charts:* trade as a share of world output since 1870; cost of sea freight
   and of a long-distance call over a century; the cost of light, or of
   computing, on a times-ten scale.

### Grade 7 — Choice, exchange and prices

1. **Scarcity and Opportunity Cost** — `scarcity-and-opportunity-cost`
   Wants exceed means: time, money, resources; to choose is to give something
   up; the opportunity cost of a choice is the best alternative given up; costs
   that are not money; a cost already paid does not count in the next decision;
   the same reasoning for a person, a firm and a country.
   *Opening chart:* how the 24 hours of a day are spent, in several countries.
2. **Specialisation and the Division of Labour** — `specialisation`
   Doing everything oneself against doing one thing well; splitting a task into
   steps raises output per worker (a workshop example with numbers); practice,
   tools and saved time; specialisation needs exchange; a larger market allows
   finer specialisation.
   *Opening chart:* the share of workers in farming over two centuries, with the
   number of people one farmer feeds.
3. **Gains from Trade: Comparative Advantage** — `comparative-advantage`
   Two people and two tasks, with a table of hours; absolute advantage;
   comparative advantage as the lower opportunity cost; both gain from trade
   even when one is better at everything; the range of exchange ratios that
   leaves both better off; the same for two regions. The series' first `model`
   frame, in plain words.
   *Opening chart:* exports as a share of output against country size: small
   countries trade more.
4. **Money** — `money`
   Barter and the double coincidence of wants; money as a means of payment, a
   unit of account and a store of value; what has served as money (shells,
   metal, coins, notes, bank deposits, electronic payments); what makes good
   money: scarce, durable, divisible, hard to forge; a price is an amount of
   money.
   *Opening chart:* how people pay, cash against electronic payments, in several
   countries (`dated`).
5. **Markets and Prices** — `markets-and-prices`
   A market brings buyers and sellers together (a stall, an auction, a
   platform); the price both accept; a rising price tells buyers to use less and
   sellers to bring more; a price sums up what thousands of people know, with
   nobody collecting it; what happens when a price cannot move: a shortage or a
   surplus.
   *Opening chart:* the world price of a crop before and after a failed harvest
   in its main growing region.
6. **Demand and Supply: A First Look** — `demand-and-supply-first-look`
   A demand table and its curve, drawn point by point; a supply table and its
   curve; the price at which the two quantities match, found in the table and on
   the graph; what happens above and below it; a change in tastes, incomes or
   costs moves a curve.
   *Opening chart:* the price of a seasonal fruit through one year, with the
   quantity sold.
7. **Households: Income, Spending and Saving** — `households`
   Where income comes from (wages, a business, rent, interest, transfers); the
   budget and its shares; saving as spending moved to later; how budget shares
   change as income rises (food recalled from the charts of the first year).
   Economics only: the chapter gives no advice.
   *Opening chart:* household budget shares (food, housing, transport, leisure)
   at four income levels.
8. **Firms: Costs, Revenue and Profit** — `firms`
   A firm buys inputs and sells output; revenue; fixed and variable costs;
   profit and loss; the break-even quantity by arithmetic; the owner bears the
   risk; profit draws new firms in, losses tell resources to move elsewhere.
   *Opening chart:* of 100 firms created in one year, how many are still open
   after one, three and five years.

### Grade 8 — The economy as a whole

1. **Production and Productivity** — `production-and-productivity`
   The factors of production: labour, capital (tools, machines, buildings), land
   and natural resources, knowledge; output per worker and per hour; capital per
   worker; better methods; why productivity sets the living standard of a
   country.
   *Opening chart:* output per hour worked against income per person, across
   countries.
2. **Measuring an Economy: GDP** — `gdp`
   Value added, and why sales are not added up; gross domestic product as total
   production, equal to total income and total spending (told); GDP per person;
   what it leaves out: work at home, leisure, the state of nature, who gets
   what.
   *Opening chart:* the GDP of the ten largest economies, in total and per
   person.
3. **Inflation and Price Indices** — `inflation-and-price-indices`
   A basket priced year after year; an index with base 100; the inflation rate;
   nominal and real values, and how a wage is corrected for prices; very high
   inflation; falling prices.
   *Opening chart:* yearly consumer-price inflation over a century in four
   countries, with one hyperinflation on a times-ten scale.
4. **Growth and Compounding** — `growth-and-compounding`
   The growth rate of real GDP per person; growth on growth, computed with
   powers; the doubling time and the rule of 70 (admitted); a small difference
   kept for decades makes a large gap.
   *Opening chart:* income per person since 1960 in countries that grew at about
   1 %, 2 % and 6 % a year.
5. **Jobs, Wages and Unemployment** — `jobs-wages-unemployment`
   The labour market; employed, unemployed, and outside the labour force; the
   unemployment rate and the participation rate, and how a survey measures
   them; why wages differ: skills, productivity, conditions of work; wages and
   productivity over long periods.
   *Opening chart:* the unemployment rate over fifty years in five countries.
6. **Banks, Saving and Interest** — `banks-saving-interest`
   A bank takes deposits and makes loans; interest as the price of borrowing;
   simple and compound interest; why rates differ: risk and duration; the
   interest rate after inflation (first look); a bank keeps only part of its
   deposits at hand (told).
   *Opening chart:* long-term interest rates over two centuries.
7. **Taxes and Public Spending** — `taxes-and-public-spending`
   What governments spend on; the main taxes (on income, on purchases, on
   wages, on property, on profits); budget, deficit and debt; a tax changes what
   people buy, sell and do (first look).
   *Opening chart:* public spending as a share of output since 1880, in six
   countries.
8. **Competition and Monopoly: A First Look** — `competition-and-monopoly-first-look`
   Many sellers and one seller; competition pushes the price toward cost and
   rewards a better product; a single seller sells less at a higher price; where
   a monopoly comes from: a patent, a licence, a network, large fixed costs; the
   threat of entry.
   *Opening chart:* the real price of a long-distance call, or of an air ticket,
   before and after new firms were allowed in.

### Grade 9 — Markets with algebra, and the world economy

1. **Demand and Supply with Equations** — `demand-and-supply-equations`
   Demand and supply as affine functions of the price; the equilibrium found by
   solving one equation; a shift as a change of intercept; the predicted
   direction of price and quantity for each shift; the prediction checked on a
   real episode. The `model` frame applied to supply and demand.
   *Opening chart:* price and quantity of a good over ten years in which its
   cost of production fell.
2. **Elasticity: A First Look** — `elasticity-first-look`
   The percentage change in quantity for a one per cent change in price;
   elastic and inelastic demand; what happens to revenue when the price rises;
   necessities and luxuries; more response in the long run than in the short.
   *Opening chart:* measured price elasticities of demand for ten goods.
3. **Price Controls, Taxes and Subsidies** — `price-controls-taxes-subsidies`
   A maximum price below equilibrium: shortage, queues, lower quality; a
   minimum price above it: unsold surplus; a tax per unit: the buyer's price
   rises by less than the tax and the seller's falls; who bears it; a subsidy as
   a negative tax. Each prediction with a documented episode.
   *Opening chart:* a documented episode of a price ceiling: quantities offered
   and queues before, during and after.
4. **International Trade** — `international-trade`
   Comparative advantage between countries (recalled); exports, imports and the
   trade balance; what countries sell each other and how it changes; a tariff
   as a tax on imports: who gains and who loses (first look); distance and
   transport costs.
   *Opening chart:* the exports of one country by product, in 1965 and today.
5. **Exchange Rates and Purchasing Power** — `exchange-rates-and-purchasing-power`
   The price of one currency in another; converting an amount; a currency that
   rises or falls and what it does to the prices of imports and exports; one
   basket costs different amounts in different countries; the purchasing-power
   conversion behind every international comparison of incomes.
   *Opening chart:* income per person of ten countries, converted at market
   exchange rates and at purchasing-power rates.
6. **Why Some Countries Are Rich: Institutions** — `institutions-and-prosperity`
   Three natural experiments, as data: East and West Germany, North and South
   Korea, China before and after 1978; what differs: who owns, who decides what
   is produced, whether prices are free to move, whether contracts are enforced;
   income against measures of property rights and of corruption; a correlation
   across countries is not yet a cause.
   *Opening chart:* income per person in North and South Korea since 1950.
7. **Who Earns What: Income Distribution** — `income-distribution`
   Mean and median income; shares of income by fifths of the population;
   inequality inside a country and between countries; the world distribution of
   income over time; two facts together: world poverty fell while inequality
   rose inside some countries.
   *Opening chart:* the world distribution of income in 1975 and today.

## Book 2 — Grades 10–12

### Grade 10 — Markets

1. **Economic Models** — `economic-models`
   A model as a simplified description built on stated assumptions; the
   variables it explains and the ones it takes as given; *other things equal*;
   the four-point frame (assumes, predicts, tested, breaks); statements of fact
   and statements of value; correlation and cause; an experiment and a natural
   experiment (first look).
   *Opening chart:* a model's prediction drawn against what was then observed.
2. **The Production Possibility Frontier** — `production-possibility-frontier`
   Two goods and fixed resources; points on, inside and outside the frontier;
   opportunity cost as its slope; a straight and a bowed frontier; growth moves
   it outward.
   *Opening chart:* civilian and military output of one economy, year by year,
   through a war.
3. **Ricardo's Model of Comparative Advantage** — `ricardo-model`
   Two countries, two goods, labour only; unit labour requirements; relative
   prices without trade; who exports what; the terms of trade lie between the
   two no-trade ratios; the gains, measured in goods; wages follow productivity,
   so a low-wage country does not undersell everything. Tested: relative exports
   against relative productivity. Breaks: one factor, nobody loses inside a
   country, complete specialisation.
   *Opening chart:* relative exports against relative labour productivity,
   industry by industry, for two countries.
4. **Demand** — `demand`
   From one buyer to the market; the law of demand; income, tastes, prices of
   other goods, expectations; substitutes and complements; normal and inferior
   goods; moving along the curve and moving the curve.
   *Opening chart:* consumption of one good per person against its real price
   over fifty years.
5. **Supply** — `supply`
   The quantity offered at each price; costs, technology, input prices, the
   number of sellers; moving along and moving the curve; supply responds more
   when sellers have time to adjust.
   *Opening chart:* the number of active oil rigs against the price of oil.
6. **Market Equilibrium** — `market-equilibrium`
   Equilibrium as the solution of a linear system; excess demand and excess
   supply, and how the price adjusts; two shifts at once; markets linked by
   substitutes and by inputs. Tested: laboratory markets converge to the
   predicted price. Breaks: few traders, prices that are slow to move.
   *Opening chart:* trade prices, round after round, in a laboratory market,
   against the predicted equilibrium price.
7. **Elasticities** — `elasticities`
   Price elasticity of demand at a point and between two points; how it changes
   along a straight demand line; income and cross-price elasticities;
   elasticity of supply; what makes a demand elastic; elasticity and revenue.
   *Opening chart:* cars per 1,000 people against income per person, across
   countries.
8. **Surplus and Efficiency** — `surplus-and-efficiency`
   Willingness to pay and consumer surplus; cost and producer surplus; total
   surplus as an area; under the model's assumptions the competitive
   equilibrium makes it largest; what the result does not cover: who gets the
   surplus, and people outside the market.
   *Opening chart:* the willingness to pay of 100 buyers for one good, ranked,
   with the market price.
9. **What Prices Do** — `what-prices-do`
   Three jobs of a price: to inform, to give a reason to act, to ration; how a
   price change spreads knowledge that no single person holds; arbitrage and the
   single price; storage and speculation move goods through time; price
   ceilings and floors analysed with surplus: deadweight loss, queues, quality,
   side payments; the record of price controls.
   *Opening chart:* the spread of the price of one good between neighbouring
   markets, before and after sellers could learn all the prices by telephone.
10. **Tax Incidence and Deadweight Loss** — `tax-incidence`
    The wedge between the buyer's price and the seller's; the burden does not
    depend on who hands over the tax; the less elastic side bears more; the
    deadweight loss and why it grows faster than the rate; revenue against the
    rate; a subsidy.
    *Opening chart:* consumer prices before and after a change in the tax on one
    good: how much was passed on.
11. **National Accounts** — `national-accounts`
    Production, income and expenditure give the same total, and why;
    consumption, investment, government purchases, net exports; GDP and
    national income; nominal GDP, real GDP and the deflator; how a
    purchasing-power comparison is built; the limits of the accounts.
    *Opening chart:* GDP by type of expenditure in five countries.
12. **Price Indices and the Cost of Living** — `price-indices`
    A fixed basket and a current basket; substitution, new goods and quality
    change; the consumer price index and the GDP deflator; indexing a wage or a
    contract; the real interest rate.
    *Opening chart:* the price of a computer of constant quality against the
    general price index.

### Grade 11 — Firms, market failure, government failure, labour

1. **Marginal Reasoning** — `marginal-reasoning`
   A marginal quantity as a derivative (recalled from the mathematics book);
   the rule *marginal benefit equals marginal cost*; average and marginal; the
   maximum of a profit function; sunk costs once more.
   *Opening chart:* the cost of the next unit of electricity as demand rises,
   plant by plant.
2. **Production and Costs** — `production-and-costs`
   The production function with one variable input; diminishing marginal
   product; total, average and marginal cost; marginal cost cuts average cost at
   its lowest point; short run and long run; economies of scale.
   *Opening chart:* cost per unit against the size of the plant, in one
   industry.
3. **Perfect Competition** — `perfect-competition`
   The price-taking firm; output where price equals marginal cost; when to shut
   down; the supply curve of the firm and of the industry; entry, exit and zero
   economic profit in the long run; economic and accounting profit.
   *Opening chart:* the price and the number of producers in one market in the
   years after demand rose.
4. **Monopoly** — `monopoly`
   Marginal revenue below price; the monopoly output and price; the markup and
   the elasticity of demand; deadweight loss; sources of monopoly; natural
   monopoly; different prices for different buyers (first look); how entry and
   new products erode a monopoly.
   *Opening chart:* the price of a medicine before and after its patent expired.
5. **Oligopoly and a First Look at Games** — `oligopoly-and-games`
   A few sellers; many sellers of differentiated products; a game as players,
   strategies and payoffs; dominant strategy; Nash equilibrium; the prisoner's
   dilemma; why cartels are unstable; repeated play (first look).
   *Opening chart:* the production quotas of a cartel's members against what
   each produced.
6. **Externalities** — `externalities`
   Private and social cost, private and social benefit; too much or too little
   is produced; bargaining when rights are clear and bargaining is cheap; a
   corrective tax; tradable permits; rules and standards; the evidence on each;
   positive externalities: knowledge, vaccination.
   *Opening chart:* sulphur dioxide emissions against income per person, over
   time, in several countries.
7. **Public Goods and Common Resources** — `public-goods-and-commons`
   Rival or not, excludable or not: four kinds of goods; free riding; how public
   goods get provided: taxes, clubs, bundling, technology that excludes;
   overuse of a common resource; answers and their record: property rights,
   quotas, community rules.
   *Opening chart:* the yearly catch of one fishery, through its collapse.
8. **Asymmetric Information** — `asymmetric-information`
   Hidden quality: the used-car market can unravel; hidden action: insurance
   changes behaviour; answers on both sides: warranties, reputation,
   certification, signals, deductibles, screening; compulsory and voluntary
   cover.
   *Opening chart:* the resale price of a car by age: the drop in the first
   year.
9. **Public Choice: A First Look** — `public-choice-first-look`
   The same assumption about incentives, applied to voters, elected officials
   and agencies; why a voter stays uninformed; concentrated benefits and
   dispersed costs; lobbying and rent seeking; capture of a regulator by the
   regulated; the comparison that matters: an imperfect market against an
   imperfect government.
   *Opening chart:* one protection programme: its cost per household and its
   gain per protected producer.
10. **The Labour Market** — `labour-market`
    Labour demand from the value of the marginal product; labour supply: work
    against free time; the wage; wage differences: human capital and
    compensating differences; the return to a year of schooling; one large
    employer (first look); the minimum wage: what two models predict, and a
    `debate` box on the measured effect.
    *Opening chart:* earnings by years of schooling.
11. **Inequality** — `inequality`
    The Lorenz curve and the Gini coefficient; income before and after taxes and
    transfers; income, consumption and wealth; top shares; inequality between
    countries and inside them; mobility from one generation to the next; what
    the measures miss: household size, age, in-kind benefits.
    *Opening chart:* the Gini coefficient before and after taxes and transfers,
    across countries.
12. **Unemployment** — `unemployment`
    The survey definitions in detail; flows into and out of unemployment;
    frictional, structural and cyclical unemployment; the natural rate; how
    long spells last; why wages do not fall to clear the market; what the
    evidence says about benefits and hiring rules.
    *Opening chart:* unemployed people and vacant jobs over thirty years.
13. **Money and Banking** — `money-and-banking`
    A bank's balance sheet; reserves; loans create deposits; the money
    multiplier as a toy model (it broke after 2008, when banks held large
    reserves); measures of money; the central bank: banker to the banks, setter
    of the policy rate; bank runs and deposit insurance (first look).
    *Opening chart:* central-bank money and broad money, 2000–2020.

### Grade 12 — Time, growth, the short run, the open economy

1. **Present Value** — `present-value`
   Compounding, yearly and continuous (the exponential recalled from the
   mathematics book); discounting; the present value of a stream as a geometric
   sum; perpetuity and annuity; a bond's price falls when its yield rises; the
   net present value of an investment; real and nominal rates.
   *Opening chart:* the yield and the price of a long government bond over
   forty years.
2. **Risk and Insurance** — `risk-and-insurance`
   Expected value; risk aversion from a concave utility; the certainty
   equivalent; a fair premium and a loaded one; pooling and the law of large
   numbers; spreading risk across assets (first look); hidden quality and hidden
   action recalled.
   *Opening chart:* claims per 1,000 policies year after year: stable in the
   pool, unpredictable for one person.
3. **Inflation and the Quantity of Money** — `inflation-and-money`
   The quantity equation and its growth-rate form; across countries and decades,
   high money growth and high inflation go together; hyperinflations and how
   they ended; the costs of inflation; nominal and real interest rates;
   expected and unexpected inflation. Tested: high and long inflations. Breaks:
   low inflation, when velocity moves.
   *Opening chart:* average money growth against average inflation over thirty
   years, across countries, on logarithmic scales.
4. **Growth and the Production Function** — `growth-and-production-function`
   The aggregate production function with capital, labour and technology;
   constant returns to scale and diminishing returns to capital; output per
   worker; the shares of income going to labour and capital; growth accounting
   with logarithms.
   *Opening chart:* output per worker against capital per worker, across
   countries.
5. **The Solow Model: A First Look** — `solow-first-look`
   Saving, depreciation and the accumulation of capital as a recurrence; the
   steady state; a higher saving rate raises the level of income, not its
   long-run growth; convergence; sustained growth needs better technology.
   Tested: recovery after wartime destruction, convergence among similar
   countries. Breaks: it does not explain technology, and capital explains
   little of the gap between rich and poor countries.
   *Opening chart:* growth since 1960 against income in 1960, for similar
   countries and for all countries.
6. **Ideas, Institutions and Growth** — `ideas-institutions-growth`
   An idea can be used by everyone at once; the incentives to invent: patents,
   prizes, competition; institutions recalled, then measured: indices of
   property rights and economic freedom against income; why the best methods do
   not spread everywhere.
   *Opening chart:* income per person against an index of protection of
   property rights.
7. **Saving, Investment and the Financial System** — `saving-and-investment`
   Saving equals investment in a closed economy; the market for loanable funds
   and the real interest rate; a government deficit and crowding out; banks and
   markets, shares and bonds (told).
   *Opening chart:* national saving rates against investment rates, across
   countries.
8. **Aggregate Demand and Supply** — `aggregate-demand-and-supply`
   The facts of the business cycle; the long-run model: output set by factors
   and technology, money changes only prices; the short-run model: prices and
   wages slow to move; demand shocks and supply shocks; the return to the long
   run. The two models side by side, each in its frame.
   *Opening chart:* real GDP of one country over sixty years against its trend,
   with the recessions marked.
9. **The Keynesian Cross and the Multiplier** — `keynesian-cross`
   The consumption function; planned spending and equilibrium output; the
   multiplier as a geometric series. A toy model: fixed prices, a fixed interest
   rate, no imports, households that do not look ahead. What shrinks the
   multiplier: taxes, imports, the interest rate, expectations, full capacity.
   A `debate` box on measured multipliers; the large fixed multiplier is taught
   as refuted.
   *Opening chart:* the range of fiscal multipliers estimated by published
   studies.
10. **Monetary Policy** — `monetary-policy`
    What a central bank aims at and what it controls; from the policy rate to
    market rates, spending and the exchange rate; delays; rules and discretion;
    credibility and independence, with the evidence; the record: the Volcker
    disinflation, the zero lower bound after 2008, 2021–23.
    *Opening chart:* the policy rate and inflation in one country, 1965 to
    today.
11. **Fiscal Policy and Public Debt** — `fiscal-policy-and-debt`
    Budget balance and primary balance; automatic stabilisers; the debt ratio as
    a recurrence in the interest rate and the growth rate; when a debt is
    sustainable; crowding out; do households expect the future taxes (first
    look); how large debts ended: growth, surpluses, inflation, default.
    "Deficits don't matter" against the record.
    *Opening chart:* public debt as a share of output over two centuries, in two
    countries.
12. **The Phillips Curve and Its Breakdown** — `phillips-curve`
    The relation seen in the 1950s and 1960s; the claim of a stable trade-off;
    the stagflation of the 1970s; expectations; the natural rate and the absence
    of a long-run trade-off; the cost of bringing inflation down; anchored
    expectations; 2021–23.
    *Opening chart:* inflation against unemployment in one country, 1960–69 and
    1970–83.
13. **Trade beyond Ricardo, and Trade Policy** — `trade-and-trade-policy`
    Trade from different endowments, from scale and from variety (told);
    winners and losers inside a country; a tariff and a quota analysed with
    surplus; the arguments for protection, each with its evidence; trade
    agreements; a `debate` box on trade and wages.
    *Opening chart:* average tariff rates over two centuries.
14. **Exchange Rates and the Balance of Payments** — `exchange-rates-and-balance-of-payments`
    The current account and the financial account; saving minus investment
    equals the current account; purchasing-power parity as a long-run anchor;
    interest parity (first look); fixed and floating rates; the three aims that
    cannot all be met (told); currency crises (first look).
    *Opening chart:* current-account balances of the six largest economies since
    1980.
15. **Income and Wellbeing** — `income-and-wellbeing`
    Life satisfaction against income, across countries and inside them; a
    relation in the logarithm of income; what GDP leaves out, with numbers:
    free time, health, the distribution, nature; other indicators and how
    closely they follow income per person; what economics measures and what it
    does not.
    *Opening chart:* average life satisfaction against income per person, on a
    logarithmic scale.

## Book 3 — University Year 1 (`bachelor-1`)

Intermediate microeconomics and macroeconomics with one- and two-variable
calculus, then a first part on data. Chapters are numbered through the book.

### Part I — Method

1. **Models and Data** — `models-and-data`
   The four-point frame for a reader who has calculus; given and explained
   variables; equilibrium and comparative statics; stocks and flows; levels,
   logarithms and growth rates; real and nominal; a first look at
   identification: observed prices and quantities trace neither a demand curve
   nor a supply curve.
   *Opening chart:* yearly price and quantity in one market over forty years: a
   cloud of points.
2. **Optimisation under Constraint** — `constrained-optimisation`
   Functions of two variables and their level curves (recalled from the
   mathematics book); a maximum under one equality constraint: substitution,
   tangency; Lagrange's method (admitted); the multiplier as a shadow price;
   corner solutions; the second-order check (told).
   *Opening chart:* hours worked and consumption of households at different
   wages: the choices a constrained optimum has to explain.
3. **Comparative Statics** — `comparative-statics`
   How a solution moves when a parameter moves; implicit differentiation;
   elasticities as logarithmic derivatives; the envelope theorem (proved in the
   one-constraint case); sign predictions as what a test can refute.
   *Opening chart:* the fall in quantity after the same tax rise, in markets of
   different elasticities.

### Part II — The consumer

4. **Preferences and Utility** — `preferences-and-utility`
   A preference relation: complete, transitive, monotone, convex; indifference
   curves and the marginal rate of substitution; a utility function represents
   an ordering and nothing more; the standard forms (Cobb–Douglas, perfect
   substitutes, perfect complements, quasi-linear). Tested: consistency of
   observed choices with the axioms.
   *Opening chart:* budget shares of broad categories across household incomes.
5. **Consumer Choice** — `consumer-choice`
   The budget set; the optimum where the marginal rate of substitution equals
   the price ratio; demand functions for the standard forms; corner solutions;
   indirect utility; revealed preference.
   *Opening chart:* spending on food against total spending in a household
   survey.
6. **Income and Substitution Effects** — `income-and-substitution-effects`
   A price change split in two, in the Slutsky and the Hicks way; the Slutsky
   equation; compensated demand slopes down; Giffen goods and where one was
   found; adding-up relations between elasticities.
   *Opening chart:* fuel use before and after a fuel tax whose revenue was
   handed back to households.
7. **Consumer Welfare** — `consumer-welfare`
   Compensating and equivalent variation; consumer surplus as an approximation,
   exact for quasi-linear utility; the true cost-of-living index between the
   fixed-basket and current-basket indices; the value of a new good.
   *Opening chart:* a fixed-basket price index against a chained index over
   thirty years.
8. **Labour Supply and Saving** — `labour-supply-and-saving`
   The choice between consumption and free time; income and substitution
   effects of the wage; taxes and transfers bend the budget line: kinks and
   implicit marginal rates; consumption over two periods and the interest rate;
   measured elasticities of labour supply.
   *Opening chart:* yearly hours worked against the real wage over a century.

### Part III — The firm

9. **Technology** — `technology`
   Production functions and isoquants; the marginal rate of technical
   substitution; returns to scale; the elasticity of substitution;
   Cobb–Douglas, fixed proportions, constant elasticity of substitution;
   technical progress.
   *Opening chart:* capital per worker against the relative price of labour, in
   one industry across countries.
10. **Cost Minimisation** — `cost-minimisation`
    Isocost lines; conditional factor demands; the cost function and its
    properties; Shephard's lemma from the envelope theorem; short-run and
    long-run cost curves; economies of scale; learning by doing.
    *Opening chart:* the unit cost of solar modules against cumulative
    production.
11. **Profit Maximisation and Supply** — `profit-maximisation`
    The price-taking firm's problem; the supply function and the factor demands;
    Hotelling's lemma; the shut-down condition; the evidence on whether firms
    maximise profit.
    *Opening chart:* area planted with one crop against its expected price.
12. **The Competitive Industry** — `competitive-industry`
    Short-run industry supply; long-run supply with free entry; constant- and
    increasing-cost industries; rents and quasi-rents; who gains from a subsidy
    or a licence in the long run: capitalisation.
    *Opening chart:* the price of a taxi licence in one city over forty years.

### Part IV — Markets and price theory

13. **Partial Equilibrium and Welfare** — `partial-equilibrium-welfare`
    Equilibrium with general demand and supply functions; stability; surplus as
    an integral; the deadweight-loss triangle in terms of elasticities; the
    incidence formula; when one market can be studied alone.
    *Opening chart:* estimated deadweight loss against the tax rate, for one
    taxed good.
14. **Price Theory at Work** — `price-theory-at-work`
    Supply and demand reasoning on real problems: the full price, with time and
    quality; how sellers and buyers adjust around a controlled price; quota
    against tariff; arbitrage over space and over time; storage and futures;
    buying against renting; future gains capitalised into today's price. Each
    prediction with its test.
    *Opening chart:* the price of a storable crop through the crop year, against
    the cost of storing it.
15. **Monopoly and Pricing** — `monopoly-pricing`
    The Lerner index; price discrimination of the first, second and third
    degree; two-part tariffs; bundling; how a natural monopoly is priced under
    average-cost and price-cap rules; measuring market power.
    *Opening chart:* price–cost margins across industries.
16. **Factor Markets** — `factor-markets`
    Derived demand; the marginal revenue product; the single-buyer model: a
    wage below the marginal product, and what a wage floor then does; economic
    rent; the rental price of capital; factor shares.
    *Opening chart:* wages against the concentration of employers in local
    labour markets.
17. **Oligopoly: Cournot and Bertrand** — `cournot-and-bertrand`
    Cournot competition with $n$ firms and its competitive limit; Bertrand
    competition and its paradox; capacities and differentiation; the
    leader–follower model; margins against the number of competitors.
    *Opening chart:* prices against the number of sellers in isolated local
    markets.

### Part V — Macroeconomics: the long run

18. **National Accounts in Depth** — `national-accounts-in-depth`
    Sectors; the sequence from production to income to use; saving, investment
    and net lending; chain-linked volumes; how purchasing-power parities are
    built; revisions; what the accounts estimate rather than observe.
    *Opening chart:* first estimates of quarterly GDP growth against the final
    figures.
19. **The Long-Run Model** — `long-run-model`
    Output from the supplies of factors; factor prices equal marginal products;
    the division of income (Euler's theorem); the market for loanable funds;
    government purchases and crowding out; real variables separate from money.
    Tested: stable factor shares. Breaks: the short run.
    *Opening chart:* labour's share of national income over a century.
20. **The Solow Model** — `solow-model`
    The model in continuous time; the steady state and its stability; the golden
    rule; the speed of convergence; technical progress and balanced growth; the
    model taken to cross-country data, with human capital added.
    *Opening chart:* income per person against the investment rate, across
    countries.
21. **Growth and Development Accounting** — `growth-accounting`
    The Solow residual; the sources of growth in fast-growing economies; levels
    accounting: capital, schooling and productivity; misallocation; planned
    economies: high investment, low productivity growth; institutions as a
    deeper cause.
    *Opening chart:* growth of output split into capital, labour and
    productivity, for eight economies.
22. **Unemployment: Stocks and Flows** — `unemployment-flows`
    Separation and job-finding rates give the steady-state rate; duration; why
    wages stay above the market-clearing level: efficiency wages, bargaining;
    the Beveridge curve; benefits and hiring rules across countries, as
    evidence.
    *Opening chart:* the job-finding rate and the separation rate through four
    business cycles.
23. **Money and Inflation** — `money-and-inflation`
    Money demand; the quantity theory; the monetarist propositions scored
    against the data: the long-run link holds, the delays are long and variable,
    money-growth targets failed when velocity moved; the inflation tax; money
    demand in a hyperinflation; the Fisher effect.
    *Opening chart:* the velocity of money over sixty years: stable, then not.

### Part VI — The short run

24. **The IS–LM Model** — `is-lm`
    Goods-market and money-market equilibrium; fiscal and monetary shifts; the
    liquidity trap; the version with an interest-rate rule. A toy model: a fixed
    price level, a closed economy, no expectations. Tested on signs. Breaks
    wherever prices or expectations move.
    *Opening chart:* short-term interest rates and central-bank money,
    2007–2015.
25. **Aggregate Supply and the Phillips Curve** — `aggregate-supply`
    Sticky wages, sticky prices, imperfect information; the short-run supply
    curve; the expectations-augmented Phillips curve; adaptive expectations and
    accelerating inflation; the sacrifice ratio; the record.
    *Opening chart:* the change in inflation against the unemployment gap.
26. **Stabilisation Policy and Its Limits** — `stabilisation-policy`
    Delays in recognising, deciding and acting; uncertainty about the model;
    the record of fine-tuning; automatic stabilisers; rules and discretion; how
    multipliers are measured, with a `debate` box; fiscal policy at the zero
    lower bound; 2020–23.
    *Opening chart:* forecasts of GDP growth made a year ahead against the
    outcome, around recessions.
27. **The Open Economy** — `open-economy`
    Open-economy accounts; the real exchange rate and net exports; the small
    open economy in the long run; the Mundell–Fleming model under floating and
    fixed rates; the trilemma. A toy model, in its frame.
    *Opening chart:* interest-rate gaps between pegged currencies and their
    anchor.

### Part VII — Data and statistics, in Python

28. **Economic Data with Python** — `economic-data-python`
    Cross-sections, time series and panels; loading and joining tables; units
    and frequencies; seasonal adjustment; deflating, indexing, per-person
    values, logarithms, growth rates; plotting; every number comes from a
    script that can be rerun.
    *Opening chart:* one monthly series, raw and seasonally adjusted.
29. **Describing Data** — `describing-data`
    Histograms and quantiles; mean, variance and skewness: incomes are skewed;
    covariance and correlation; conditional means; traps of aggregation
    (composition effects, Simpson's paradox); outliers.
    *Opening chart:* the distribution of household income, on an ordinary and a
    logarithmic axis.
30. **Random Variables for Econometrics** — `random-variables-for-econometrics`
    Expectation, variance and covariance (recalled from the mathematics book);
    joint and conditional distributions; conditional expectation and the law of
    iterated expectations; the normal, chi-square, $t$ and $F$ distributions as
    tools; the law of large numbers and the central limit theorem (admitted),
    seen by simulation.
    *Opening chart:* simulated sample means of a skewed variable, for samples of
    5, 30 and 200.
31. **Sampling and Inference** — `sampling-and-inference`
    Population and sample; estimators: bias, variance, consistency; the standard
    error; confidence intervals; tests, and what a $p$-value is not; power;
    many tests at once; survey design and weights: how an unemployment rate is
    estimated.
    *Opening chart:* a monthly unemployment rate with its confidence band.
32. **Simple Regression** — `simple-regression`
    The conditional expectation function; the least-squares line; reading a
    slope in levels and in logarithms; fit; the conditions for an unbiased
    slope; its standard error; regression toward the mean; a regression is not
    a cause: omitted variables, reverse causation.
    *Opening chart:* earnings against years of schooling, with the fitted line.

## Book 4 — University Year 2 (`bachelor-2`)

### Part I — Uncertainty and time

1. **Expected Utility** — `expected-utility`
   Lotteries; the axioms and the representation theorem; risk aversion and its
   measures; the certainty equivalent and the risk premium; constant absolute
   and constant relative risk aversion. Tested in the laboratory and in
   insurance choices. Breaks: the Allais pairs, small stakes.
   *Opening chart:* choices of subjects in the two Allais pairs.
2. **Insurance and Risk Sharing** — `insurance-and-risk-sharing`
   The demand for insurance: full cover at a fair price, partial cover with a
   loading; state-contingent goods; efficient risk sharing; a first portfolio
   choice; the test of full risk sharing on village data.
   *Opening chart:* household consumption against household income shocks in a
   village survey.
3. **Intertemporal Choice** — `intertemporal-choice`
   Exponential discounting; the Euler equation; smoothing consumption; the
   interest rate; borrowing limits; time consistency. Breaks: measured present
   bias.
   *Opening chart:* consumption and income by age.
4. **Asset Prices: A First Model** — `asset-prices`
   No arbitrage; a price as an expected discounted payoff; a risk premium from
   covariance; the mean–variance model and its tests; the efficient-markets
   hypothesis: its forms, its tests, its anomalies. The depth belongs to the
   quantitative finance series.
   *Opening chart:* cumulated real returns on shares, bonds and bills over a
   century, in several countries.
5. **Behavioural Evidence: Where Rational Choice Breaks** — `behavioural-evidence`
   The deviations that held up in large replications: reference dependence and
   loss aversion, present bias, the pull of a default, limited attention; the
   findings that did not replicate; prospect theory in the model frame; what
   remains among experienced traders and at high stakes.
   *Opening chart:* original effect sizes against the sizes found on
   replication.

### Part II — General equilibrium and welfare

6. **Exchange Economies** — `exchange-economies`
   The Edgeworth box; Pareto-efficient allocations and the contract curve;
   competitive equilibrium; Walras' law; existence (told); when equilibrium is
   not unique.
   *Opening chart:* prices in a laboratory economy with several goods, round by
   round, against the equilibrium prices.
7. **The Two Welfare Theorems** — `welfare-theorems`
   Production added; the first theorem, proved; the second, stated, with the
   role of convexity; which assumption carries the result: complete markets,
   price taking, no external effects; the theorems are silent on distribution.
   *Opening chart:* the price gap for grain between cities before and after a
   railway joined them.
8. **Prices as Information** — `prices-as-information`
   What a planner would need to know to compute an efficient allocation; prices
   as the short message that is enough; equilibrium when traders learn from
   prices; prediction markets and their record; the limit: if prices revealed
   everything, nobody would pay to learn; planned economies' internal prices,
   as data.
   *Opening chart:* prediction-market prices against the frequency of the
   events they priced.
9. **Social Choice** — `social-choice`
   The Pareto criterion and compensation tests; social welfare functions as
   tools; voting cycles; Arrow's theorem, proved; single-peaked preferences
   and the median voter; strategic voting (told).
   *Opening chart:* in ranked ballots from real elections, how often one option
   beats every other.

### Part III — Game theory

10. **Static Games** — `static-games`
    The normal form; dominance and its iteration; best responses; Nash
    equilibrium; applications: quantity competition, contributions to a public
    good, a common resource, location.
    *Opening chart:* contributions in a public-goods experiment, round after
    round.
11. **Mixed Strategies** — `mixed-strategies`
    Randomised strategies; the indifference condition; existence of equilibrium
    (admitted); zero-sum games and the minimax theorem. Tested on professional
    sport.
    *Opening chart:* penalty kicks: sides chosen by kickers and keepers, and
    scoring rates.
12. **Dynamic Games** — `dynamic-games`
    The extensive form; backward induction; subgame-perfect equilibrium;
    commitment and credible threats; entry deterrence; alternating-offers
    bargaining. Breaks: offers in ultimatum experiments.
    *Opening chart:* offers and rejections in ultimatum experiments across
    societies.
13. **Repeated Games** — `repeated-games`
    Finite and infinite repetition; discounting; trigger strategies; the folk
    theorem (stated, proved in a simple case); when collusion can be sustained;
    reputation.
    *Opening chart:* how long discovered cartels had lasted.
14. **Games of Incomplete Information** — `bayesian-games`
    Types and beliefs; Bayesian Nash equilibrium; first-price and second-price
    auctions; revenue equivalence (stated); the winner's curse; a first look at
    perfect Bayesian equilibrium.
    *Opening chart:* bids against values in auction experiments.

### Part IV — Information and incentives

15. **Adverse Selection** — `adverse-selection`
    The lemons model; insurance with hidden types; unravelling; the test on
    insurance data (cover chosen against claims) and its mixed results;
    selection that runs the other way; private and compulsory answers, with
    their evidence.
    *Opening chart:* claims against the level of cover chosen, in one insurance
    market.
16. **Signalling and Screening** — `signalling-and-screening`
    The education-signal model: separating and pooling equilibria; screening by
    a menu of contracts; price discrimination as screening; diplomas: signal or
    skill, and the evidence.
    *Opening chart:* earnings by years of schooling, with the jumps at diploma
    years.
17. **Moral Hazard and Contracts** — `moral-hazard`
    Principal and agent; the trade-off between insurance and incentives; linear
    contracts; several tasks; teams and relative performance; field evidence:
    piece rates, sharecropping; incomplete contracts and the boundary of the
    firm (told).
    *Opening chart:* output per worker in one firm before and after a move to
    piece rates.
18. **Externalities and Public Goods: The Formal Theory** — `externalities-and-public-goods-theory`
    An external effect in general equilibrium; the corrective tax; the Coase
    theorem and transaction costs; prices against quantities under uncertainty;
    the Samuelson condition; voluntary provision falls short; personalised
    prices; a first mechanism that makes people reveal their valuations.
    *Opening chart:* the price of an emission permit over fifteen years.

### Part V — Macroeconomic dynamics

19. **Consumption** — `consumption`
    The simple consumption function against long-run data; the life-cycle and
    permanent-income models; the Euler equation and the random walk;
    precautionary saving and borrowing limits. Breaks: households spend much of
    a transitory payment.
    *Opening chart:* household spending in the weeks before and after a tax
    rebate arrived.
20. **Investment** — `investment`
    The user cost of capital; adjustment costs and Tobin's $q$; irreversible
    investment under uncertainty; financing constraints; stocks; housing.
    *Opening chart:* the investment rate against $q$ over fifty years.
21. **Government Debt and Ricardian Equivalence** — `government-debt`
    The government's budget constraint over time; debt dynamics and tests of
    sustainability; Ricardian equivalence: statement, assumptions, evidence;
    tax smoothing; how large debts ended; a `debate` box on debt and growth.
    *Opening chart:* private saving against the public deficit over time, in
    several countries.
22. **Overlapping Generations** — `overlapping-generations`
    The two-period model; the steady state; too much capital is possible;
    pay-as-you-go and funded pensions: the return on each; the arithmetic of
    ageing; debt across generations.
    *Opening chart:* people of 65 and over per 100 people of working age, 1950
    to the projections for 2100.
23. **The Ramsey Model** — `ramsey-model`
    The household with an infinite horizon; the Euler equation with capital
    accumulation; the phase diagram and the saddle path; the modified golden
    rule; the market outcome equals the planner's; a change in government
    purchases. A toy model: one representative household.
    *Opening chart:* the saving rate of one country along sixty years of
    catching up.
24. **Ideas and Endogenous Growth** — `endogenous-growth`
    Constant returns to capital; ideas used by all at once, and increasing
    returns; the research sector model; the scale effect it predicts, and its
    refutation; the semi-endogenous version; growth through replacement of old
    products (told); are ideas getting harder to find.
    *Opening chart:* the number of researchers against productivity growth over
    seventy years.
25. **Expectations and the Lucas Critique** — `expectations-and-lucas-critique`
    Adaptive and rational expectations; the critique: an estimated relation
    shifts when the policy changes, with the Phillips curve as the case; the
    policy-ineffectiveness result and its limits; time inconsistency;
    credibility, central-bank independence and inflation targets, with the
    evidence; survey measures of expectations.
    *Opening chart:* average inflation against an index of central-bank
    independence.
26. **Search and Unemployment** — `search-and-unemployment`
    The matching function; job creation; wage bargaining; equilibrium
    unemployment and the Beveridge curve; the effects of benefits and
    productivity. Breaks: the model moves unemployment too little over the
    cycle.
    *Opening chart:* the Beveridge curve of one country, 2000–2023.
27. **The Three-Equation Model** — `three-equation-model`
    A demand curve with expectations, a Phillips curve, a monetary rule; shocks
    and responses; the rule must react more than one for one; the zero lower
    bound. A toy model. Tested: 1985–2007. Breaks: 2008 (no financial sector),
    the flat Phillips curve, 2021.
    *Opening chart:* the policy rate against the rate a simple rule gives.
28. **Business Cycles and Shocks** — `business-cycles`
    The facts: volatility, co-movement, persistence; separating trend and
    cycle; the real-business-cycle model as a toy model; technology, demand,
    financial and oil shocks; how a shock is identified (told); the fall in
    volatility after 1985 and its end.
    *Opening chart:* the volatility of GDP growth over rolling ten-year
    windows.
29. **Banks, Runs and Financial Crises** — `banks-and-crises`
    Short deposits, long loans; the bank-run model; deposit insurance and the
    lender of last resort, with the risk-taking they invite; leverage and forced
    sales; 2008 step by step; banks and government debt; 150 years of crises:
    credit booms before, slow recoveries after.
    *Opening chart:* banking crises per decade since 1870.

### Part VI — Econometrics I, in Python

30. **Multiple Regression** — `multiple-regression`
    The model in matrix form; the least-squares estimator; partialling out; the
    omitted-variable bias formula; near-collinear regressors.
    *Opening chart:* the estimated return to schooling as controls are added one
    by one.
31. **Inference in Regression** — `regression-inference`
    The Gauss–Markov theorem; $t$ and $F$ tests; unequal error variances and
    robust standard errors; clustered errors; large-sample results (the central
    limit theorem admitted); the bootstrap (told).
    *Opening chart:* classical and robust confidence intervals for the same ten
    coefficients.
32. **Specification** — `specification`
    Logarithms and elasticities; polynomials, dummy variables and interactions;
    measurement error and attenuation; proxies and bad controls; why searching
    over specifications voids the tests.
    *Opening chart:* a simulated slope estimate shrinking as measurement noise
    grows.
33. **Causality and the Experimental Ideal** — `causality-and-experiments`
    Potential outcomes; average effects; selection bias; what randomisation
    buys; regression as adjustment; classic experiments (class size, job
    training); whether a result travels; the idea of a natural experiment.
    *Opening chart:* outcomes of treated and control groups in one randomised
    programme.
34. **Time Series: A First Course** — `time-series`
    Trend and season; autocorrelation; stationarity; autoregressive and
    moving-average models; unit roots and spurious regression, by simulation;
    distributed lags; forecasting and how to score a forecast; what Granger
    causality does and does not mean.
    *Opening chart:* two independent random walks that look related.

## Book 5 — University Year 3 (`bachelor-3`)

### Part I — Econometrics II: establishing cause

1. **Instrumental Variables** — `instrumental-variables`
   Endogenous regressors; relevance and exclusion; two-stage least squares;
   weak instruments; the local average treatment effect; classic instruments
   and what was later found wrong with some.
   *Opening chart:* years of schooling and earnings by quarter of birth.
2. **Panel Data** — `panel-data`
   Pooled regression; fixed effects and first differences; random effects;
   what variation identifies the coefficient; clustered errors; the bias of
   dynamic panels (told).
   *Opening chart:* one relation across countries and inside countries over
   time: two different slopes.
3. **Difference-in-Differences** — `difference-in-differences`
   Two groups, two periods; parallel trends; event-study plots; the pitfalls of
   staggered adoption; the synthetic control method.
   *Opening chart:* employment in two neighbouring regions before and after a
   policy change in one.
4. **Regression Discontinuity** — `regression-discontinuity`
   Sharp and fuzzy designs; the choice of window; tests for manipulation of the
   running variable; classic applications: class-size rules, score thresholds.
   *Opening chart:* an outcome against a score, with the jump at the threshold.
5. **Binary Outcomes and Maximum Likelihood** — `binary-outcomes`
   The linear probability model, logit and probit; the likelihood and its
   maximum; marginal effects; discrete choice from random utility, and the
   logit model of demand.
   *Opening chart:* participation in the labour force against age, fitted three
   ways.
6. **Credible Empirical Work** — `credible-empirical-work`
   Publication bias, specification search, low power; the replication record of
   economics; pre-registration; meta-analysis and funnel plots; effect size
   against significance; reading a results table; the evidence scale used in
   this series' `debate` boxes.
   *Opening chart:* the distribution of published test statistics, with its
   heap just above 1.96.

### Part II — International trade

7. **Ricardian Trade in Full** — `ricardian-trade`
   Many goods and the chain of comparative advantage; a continuum of goods:
   relative wages, the range each country makes, transport costs and
   non-traded goods, a productivity gain abroad; many countries (told); the
   tests: a country opened to trade by force, crop yields and what regions
   grow; the gains from trade in one formula (told).
   *Opening chart:* relative prices before opening against net exports after,
   product by product, for one newly opened economy.
8. **Factor Endowments** — `factor-endowments`
   Specific factors; the two-factor model: who exports what, the effect on
   factor prices, on outputs; tests: the Leontief result, the missing trade in
   factor content.
   *Opening chart:* predicted against measured factor content of trade, across
   countries.
9. **Scale, Variety and Firms** — `scale-variety-firms`
   Trade inside industries; the monopolistic-competition model of trade; the
   home-market effect; firms that differ in productivity (told, with its
   predictions); exporters are few, large and productive; gains from
   reallocation after a trade agreement.
   *Opening chart:* the share of firms that export, and their size, in one
   manufacturing census.
10. **Gravity and the Trade Data** — `gravity`
    The gravity equation; estimating it in Python; distance, borders, common
    currency, agreements; measured trade costs; the container and the two waves
    of globalisation.
    *Opening chart:* trade between country pairs against the product of their
    GDPs divided by distance.
11. **Trade Policy** — `trade-policy`
    A tariff in a large country and the terms of trade; retaliation; quotas and
    export restraints; effective protection; the political economy of
    protection (public choice recalled); evidence: who paid recent tariffs,
    local labour markets after a surge of imports, infant industries; a
    `debate` box on trade and wages.
    *Opening chart:* import prices before and after a tariff: the pass-through.

### Part III — International macroeconomics

12. **The Current Account** — `current-account`
    Balance-of-payments accounting in depth; the current account as a choice
    over time; sustainability; sudden stops; saving and investment across
    countries; why capital does not flow to poor countries.
    *Opening chart:* current-account balances as a share of world output, by
    region, since 1980.
13. **Exchange Rates** — `exchange-rates`
    Tests of purchasing-power parity; productivity and price levels; uncovered
    interest parity and its failure; the monetary model; overshooting; in
    forecasting, a random walk beats the models: where they break.
    *Opening chart:* price levels against income per person, across countries.
14. **Exchange-Rate Regimes and Currency Unions** — `exchange-rate-regimes`
    The gold standard, pegged rates, floating: each regime in the data; the
    trilemma tested; three generations of currency-crisis models; the criteria
    for a common currency and the record of one; currency boards and
    dollarisation.
    *Opening chart:* countries by exchange-rate regime since 1870.

### Part IV — Money and banking

15. **Central Banking in Practice** — `central-banking`
    The central bank's balance sheet; how the policy rate is implemented;
    inflation targeting; guidance about the future; asset purchases and their
    measured effects; financial stability; a `debate` box on the sources of the
    2021–23 inflation.
    *Opening chart:* central-bank balance sheets as a share of output,
    2005–2025.
16. **Inflation: The Evidence across Time and Countries** — `inflation-evidence`
    Prices under metallic and paper standards; hyperinflations: their fiscal
    origin and their end; disinflations and what they cost; measured
    expectations; fiscal and monetary explanations set against the same
    episodes.
    *Opening chart:* the price level of one country over three centuries.

### Part V — Public economics and public choice

17. **The Efficiency Cost of Taxation** — `efficiency-cost-of-taxation`
    The excess-burden formula; the marginal cost of public funds; the
    inverse-elasticity rule; incidence beyond one market: payroll, profit and
    value-added taxes; the elasticity of taxable income; revenue against the
    rate, where it was measured; taxes people do not notice.
    *Opening chart:* tax revenue as a share of output, by type of tax, over a
    century.
18. **Transfers, Incentives and Redistribution** — `transfers-and-incentives`
    Budget sets under a benefit system: implicit marginal rates and poverty
    traps; measured responses: income-guarantee experiments, in-work credits;
    the optimal-tax formula as a trade-off between elasticities and weights,
    and the inputs it needs; redistribution measured across countries.
    *Opening chart:* the implicit marginal tax rate faced by a low-income
    household as its earnings rise.
19. **Social Insurance** — `social-insurance`
    Why private markets for some risks stay thin; unemployment insurance: the
    trade-off between smoothing and search; health insurance: the randomised
    evidence; pensions, saving and ageing; disability insurance.
    *Opening chart:* weeks of unemployment against weeks of benefit entitlement.
20. **Cost–Benefit Analysis** — `cost-benefit-analysis`
    Willingness to pay and shadow prices; discounting; the value of a
    statistical life; risk; revealed and stated preferences; forecasts against
    outcomes for large projects.
    *Opening chart:* forecast against final cost for large public projects.
21. **Public Choice: Voting** — `public-choice-voting`
    The median-voter result and its tests; turnout and the uninformed voter;
    vote trading; agenda setting; models of the size of government, each
    tested; fiscal rules; local governments and people who move between them.
    *Opening chart:* public spending as a share of output against the date the
    vote was extended, across countries.
22. **Interest Groups, Bureaucracy and Regulation** — `interest-groups-and-regulation`
    The logic of collective action; rent seeking and its cost; the capture
    model of regulation; the budget-maximising bureau; evidence: occupational
    licences, farm programmes; measured costs and benefits of regulation; the
    record of privatisation and deregulation.
    *Opening chart:* the share of workers who need a licence to do their job,
    over sixty years.

### Part VI — Labour economics

23. **Labour Supply and Demand in the Data** — `labour-supply-and-demand`
    Elasticities at the hours and the participation margin; hours of work over
    150 years; women's participation and its causes; the elasticity of labour
    demand; technology and tasks; retirement.
    *Opening chart:* women's participation in the labour force over a century,
    in six countries.
24. **Human Capital and the Returns to Schooling** — `human-capital`
    The schooling decision; the earnings equation; ability bias and the natural
    experiments that address it; signal or skill, again, with the tests; school
    resources; training on the job.
    *Opening chart:* estimated returns to a year of schooling, by method of
    estimation.
25. **The Wage Structure** — `wage-structure`
    Compensating differences; the skill premium as a race between the supply
    and the demand for skills; models of discrimination and the evidence from
    audit studies and decompositions; unions; migration and local wages, with
    a `debate` box.
    *Opening chart:* the wage premium of university graduates against their
    share of the workforce, over sixty years.
26. **Minimum Wages and Monopsony** — `minimum-wage`
    The competitive prediction; the single-buyer and search predictions; the
    first natural experiment and the replies; border-pair and bunching
    estimates; other margins: hours, prices, entry, machines; small and large
    increases. The series' model `debate` box.
    *Opening chart:* published estimates of the employment elasticity, by year
    of publication.

### Part VII — Industrial organisation

27. **Oligopoly and Collusion** — `oligopoly-and-collusion`
    Differentiated products: location and logit demand; entry and market
    structure; estimating market power; tacit collusion; detecting cartels;
    mergers and what retrospectives found.
    *Opening chart:* prices before and after a set of completed mergers.
28. **Auctions and Market Design** — `auctions-and-market-design`
    Auction formats; revenue equivalence, proved; reserve prices; common
    values; multi-unit auctions and the record of spectrum sales; matching:
    deferred acceptance, school choice, kidney exchange.
    *Opening chart:* revenue per person from the same kind of auction run under
    different rules.
29. **Platforms and Innovation** — `platforms-and-innovation`
    Network effects and tipping; pricing on two sides; switching costs;
    patents: the incentive and the deadweight loss; patent races; competition
    and innovation; firm entry and exit as the source of productivity growth.
    *Opening chart:* the share of productivity growth that comes from entry and
    exit of firms.
30. **Competition Policy and Regulation** — `competition-policy`
    Defining a market and measuring concentration; vertical restraints:
    efficiency and foreclosure, with the evidence; pricing rules for natural
    monopolies and how firms respond to them; the record of deregulation;
    errors of both kinds.
    *Opening chart:* real prices in one industry before and after deregulation.

### Part VIII — Growth, development and environment

31. **Growth Empirics and Convergence** — `growth-empirics`
    Cross-country growth regressions and their fragility; conditional
    convergence; growth miracles and disasters; growth that stops; the move out
    of agriculture.
    *Opening chart:* the world's growth rates, country by country, decade by
    decade.
32. **Institutions and Long-Run Prosperity** — `institutions`
    Defining and measuring institutions; the natural experiments treated with
    the methods of Part I: the two Koreas, the two Germanys, China's reforms
    from 1978; instruments for institutions and their critics; planned
    economies in the data; the transitions of the 1990s; a `debate` box on
    geography, institutions and culture.
    *Opening chart:* income per person in East and West Germany, 1950 to today.
33. **Population and the Demographic Transition** — `demographic-transition`
    The Malthusian model in its frame: tested on wages and population before
    1800, broken after; the demographic transition; the trade-off between the
    number of children and their schooling; ageing and the dependency ratio.
    *Opening chart:* real wages and population in one country, 1250–1850.
34. **Development Microeconomics** — `development-microeconomics`
    Measuring poverty in depth; health and nutrition; schooling programmes;
    credit and microfinance: the randomised evidence; cash transfers; property
    titles; a `debate` box on aid and growth; whether a result travels.
    *Opening chart:* measured effects of microcredit on household income in
    seven randomised studies.
35. **Environmental and Resource Economics** — `environmental-and-resource-economics`
    Valuing damages; taxes, permits and standards compared on the evidence;
    pollution against income: a hump for local pollutants, none for carbon
    dioxide; the social cost of carbon as a calculation, and what discounting
    does to it; exhaustible resources: the rule for their price, and its
    failure in the data; learning curves in energy.
    *Opening chart:* real prices of twelve minerals over a century.
36. **Income, Wellbeing and What Economics Measures** — `income-and-wellbeing-evidence`
    Life satisfaction and income, between and inside countries and over time,
    with a `debate` box on whether the relation flattens; welfare measures
    beyond GDP, built from consumption, leisure, mortality and inequality; a
    return to the twenty charts of the first volume: what the models of the
    series explained, and what stays open.
    *Opening chart:* life satisfaction against income over time inside
    countries.

---

## The data strand

The thirteen themes of `../economics_series.md`, each with the chapter that
first shows the facts and the chapters that later explain them.

| Theme | First shown | Explained in |
|---|---|---|
| Living standards | g6 `living-standards` | g8 `growth-and-compounding`, g12 `solow-first-look`, Y1 `solow-model`, `growth-accounting`, Y3 `growth-empirics` |
| Poverty | g6 `poverty` | g9 `income-distribution`, Y3 `development-microeconomics` |
| Inequality | g9 `income-distribution` | g11 `inequality`, Y3 `transfers-and-incentives`, `wage-structure` |
| Health and population | g6 `health-and-population` | Y2 `overlapping-generations`, Y3 `demographic-transition`, `social-insurance` |
| Education | g6 `school-and-work` | g11 `labour-market`, Y2 `signalling-and-screening`, Y3 `human-capital` |
| Work | g6 `school-and-work` | g8 `jobs-wages-unemployment`, g11 `unemployment`, Y1 `labour-supply-and-saving`, Y3 `labour-supply-and-demand` |
| Food | g6 `food-and-energy` | g7 `households`, g10 `elasticities`, Y1 `consumer-choice` |
| Trade | g6 `a-connected-world` | g7 `comparative-advantage`, g9 `international-trade`, g10 `ricardo-model`, g12 `trade-and-trade-policy`, Y3 Part II |
| Prices and money | g6 `a-connected-world`, g8 `inflation-and-price-indices` | g10 `price-indices`, g12 `inflation-and-money`, Y1 `money-and-inflation`, Y3 `inflation-evidence` |
| Government | g8 `taxes-and-public-spending` | g10 `tax-incidence`, g11 `public-choice-first-look`, g12 `fiscal-policy-and-debt`, Y3 Part V |
| Energy and environment | g6 `food-and-energy` | g11 `externalities`, Y2 `externalities-and-public-goods-theory`, Y3 `environmental-and-resource-economics` |
| Institutions | g9 `institutions-and-prosperity` | g12 `ideas-institutions-growth`, Y1 `growth-accounting`, Y3 `institutions` |
| Wellbeing | g12 `income-and-wellbeing` | Y3 `income-and-wellbeing-evidence` |

How the numbers are made is owned by: g6 `reading-economic-charts` (per person,
shares, scales), g6 `poverty` (a poverty line), g8 `gdp` and
`inflation-and-price-indices`, g8 `jobs-wages-unemployment` (the survey), g9
`exchange-rates-and-purchasing-power`, g10 `national-accounts` and
`price-indices`, Y1 `national-accounts-in-depth` and `sampling-and-inference`.

## Notion-ownership map

The **owner** teaches the notion; the chapters listed under *recalled in* open
with a short *You already know* box and build on it.

### Books 1–2 (one owner each; a later chapter recalls and adds)

| Notion | Owner | Recalled in |
|---|---|---|
| per-person value, share, the times-ten scale | g6 `reading-economic-charts` | every later chapter; from g12 the logarithmic scale replaces the times-ten scale |
| income per person over the long run | g6 `living-standards` | g8 `growth-and-compounding`, g12 `growth-and-production-function` |
| poverty line, poverty rate | g6 `poverty` | g9 `income-distribution`, g11 `inequality` |
| life expectancy, births per woman, ageing | g6 `health-and-population` | g12 `fiscal-policy-and-debt` |
| sectors of employment, hours worked | g6 `school-and-work` | g7 `specialisation`, g8 `jobs-wages-unemployment` |
| food share of spending | g6 `food-and-energy` | g7 `households`, g10 `elasticities` |
| trade as a share of output | g6 `a-connected-world` | g9 `international-trade` |
| opportunity cost | g7 `scarcity-and-opportunity-cost` | g7 `comparative-advantage`, g10 `production-possibility-frontier` |
| division of labour | g7 `specialisation` | g8 `production-and-productivity` |
| comparative advantage (two people, a table) | g7 `comparative-advantage` | g9 `international-trade`, g10 `ricardo-model` |
| money and its three functions | g7 `money` | g8 `banks-saving-interest`, g11 `money-and-banking` |
| the price as a signal; shortage and surplus | g7 `markets-and-prices` | g9 `price-controls-taxes-subsidies`, g10 `what-prices-do` |
| demand and supply tables and curves, equilibrium | g7 `demand-and-supply-first-look` | g9 `demand-and-supply-equations`, g10 `demand`, `supply` |
| household income, budget, saving | g7 `households` | g8 `banks-saving-interest`, g12 `saving-and-investment` |
| revenue, fixed and variable cost, profit | g7 `firms` | g8 `competition-and-monopoly-first-look`, g11 `production-and-costs` |
| factors of production, productivity | g8 `production-and-productivity` | g12 `growth-and-production-function` |
| GDP, value added | g8 `gdp` | g10 `national-accounts` |
| price index, inflation rate, real and nominal | g8 `inflation-and-price-indices` | g10 `price-indices`, g12 `inflation-and-money` |
| growth rate, compounding, doubling time | g8 `growth-and-compounding` | g12 `present-value`, `solow-first-look` |
| unemployment rate, participation rate | g8 `jobs-wages-unemployment` | g11 `labour-market`, `unemployment` |
| bank, deposit, loan, interest | g8 `banks-saving-interest` | g11 `money-and-banking`, g12 `present-value` |
| taxes, budget, deficit, debt | g8 `taxes-and-public-spending` | g10 `tax-incidence`, g12 `fiscal-policy-and-debt` |
| competition and monopoly, in words | g8 `competition-and-monopoly-first-look` | g11 `perfect-competition`, `monopoly` |
| affine demand and supply, shifts | g9 `demand-and-supply-equations` | g10 `market-equilibrium` |
| elasticity as a ratio of percentages | g9 `elasticity-first-look` | g10 `elasticities` |
| price ceiling, price floor, tax per unit | g9 `price-controls-taxes-subsidies` | g10 `what-prices-do`, `tax-incidence` |
| exports, imports, tariff | g9 `international-trade` | g12 `trade-and-trade-policy` |
| exchange rate, purchasing-power conversion | g9 `exchange-rates-and-purchasing-power` | g10 `national-accounts`, g12 `exchange-rates-and-balance-of-payments` |
| institutions; the three natural experiments | g9 `institutions-and-prosperity` | g12 `ideas-institutions-growth` |
| mean and median income, shares by fifths | g9 `income-distribution` | g11 `inequality` |
| model, the four-point frame, fact and value | g10 `economic-models` | every later chapter |
| production possibility frontier | g10 `production-possibility-frontier` | g10 `ricardo-model` |
| Ricardo's model, terms of trade | g10 `ricardo-model` | g12 `trade-and-trade-policy` |
| law of demand, substitutes, complements | g10 `demand` | g10 `elasticities` |
| point and arc elasticities | g10 `elasticities` | g10 `tax-incidence`, g11 `monopoly` |
| consumer and producer surplus | g10 `surplus-and-efficiency` | g10 `what-prices-do`, g11 `monopoly`, `externalities`, g12 `trade-and-trade-policy` |
| deadweight loss | g10 `what-prices-do` | g10 `tax-incidence`, g11 `monopoly` |
| tax incidence | g10 `tax-incidence` | g11 `labour-market`, g12 `trade-and-trade-policy` |
| the accounting identities | g10 `national-accounts` | g12 `saving-and-investment`, `aggregate-demand-and-supply` |
| marginal cost, marginal revenue | g11 `marginal-reasoning` | g11 `production-and-costs`, `perfect-competition`, `monopoly` |
| economic profit, entry and exit | g11 `perfect-competition` | g11 `monopoly`, `oligopoly-and-games` |
| Nash equilibrium, prisoner's dilemma | g11 `oligopoly-and-games` | g11 `public-goods-and-commons` |
| externality | g11 `externalities` | g11 `public-goods-and-commons` |
| hidden quality, hidden action | g11 `asymmetric-information` | g12 `risk-and-insurance` |
| rent seeking, capture | g11 `public-choice-first-look` | g12 `trade-and-trade-policy` |
| human capital | g11 `labour-market` | g12 `growth-and-production-function` |
| Lorenz curve, Gini coefficient | g11 `inequality` | g12 `income-and-wellbeing` |
| natural rate of unemployment | g11 `unemployment` | g12 `phillips-curve` |
| money creation, central bank | g11 `money-and-banking` | g12 `inflation-and-money`, `monetary-policy` |
| present value, real interest rate | g12 `present-value` | g12 `saving-and-investment`, `fiscal-policy-and-debt` |
| quantity equation | g12 `inflation-and-money` | g12 `aggregate-demand-and-supply`, `monetary-policy` |
| aggregate production function | g12 `growth-and-production-function` | g12 `solow-first-look` |
| long-run and short-run aggregate models | g12 `aggregate-demand-and-supply` | g12 `keynesian-cross`, `monetary-policy`, `fiscal-policy-and-debt`, `phillips-curve` |
| multiplier | g12 `keynesian-cross` | g12 `fiscal-policy-and-debt` |
| balance of payments | g12 `exchange-rates-and-balance-of-payments` | — |

### From school to university (the university chapter re-founds with calculus)

| Topic | First look | Re-founded and extended |
|---|---|---|
| supply, demand, surplus, incidence | g9, g10 | Y1 `partial-equilibrium-welfare`, `price-theory-at-work` → Y3 `efficiency-cost-of-taxation` |
| consumer and firm | g10 `demand`, g11 `production-and-costs` | Y1 Parts II–III |
| comparative advantage | g7, g10 `ricardo-model` | Y3 `ricardian-trade` |
| what prices do | g7, g10 `what-prices-do` | Y1 `price-theory-at-work` → Y2 `prices-as-information` |
| games | g11 `oligopoly-and-games` | Y1 `cournot-and-bertrand` → Y2 Part III → Y3 Part VII |
| hidden information | g11 `asymmetric-information` | Y2 Part IV → Y3 `social-insurance` |
| externalities, public goods | g11 | Y2 `externalities-and-public-goods-theory` → Y3 `environmental-and-resource-economics`, `cost-benefit-analysis` |
| public choice | g11 `public-choice-first-look` | Y2 `social-choice` → Y3 `public-choice-voting`, `interest-groups-and-regulation` |
| minimum wage | g11 `labour-market` | Y1 `factor-markets` → Y3 `minimum-wage` |
| growth | g8, g12 `solow-first-look` | Y1 `solow-model`, `growth-accounting` → Y2 `ramsey-model`, `endogenous-growth` → Y3 `growth-empirics` |
| institutions | g9, g12 | Y1 `growth-accounting` → Y3 `institutions` |
| the short-run toy models | g12 `keynesian-cross` | Y1 `is-lm` → Y2 `three-equation-model` |
| Phillips curve, expectations | g12 `phillips-curve` | Y1 `aggregate-supply` → Y2 `expectations-and-lucas-critique` |
| money and inflation | g11, g12 `inflation-and-money` | Y1 `money-and-inflation` → Y3 `central-banking`, `inflation-evidence` |
| unemployment | g8, g11 `unemployment` | Y1 `unemployment-flows` → Y2 `search-and-unemployment` |
| public debt | g8, g12 `fiscal-policy-and-debt` | Y2 `government-debt`, `overlapping-generations` |
| risk and insurance | g12 `risk-and-insurance` | Y2 Part I |
| open economy | g9, g12 | Y1 `open-economy` → Y3 Part III |
| establishing a cause | g10 `economic-models` | Y1 `simple-regression` → Y2 Part VI → Y3 Part I |
| wellbeing | g12 `income-and-wellbeing` | Y3 `income-and-wellbeing-evidence` |

No notion is owned by two university books: Year 1 owns the consumer, the firm,
partial equilibrium, the long-run and IS–LM models and simple regression; Year 2
owns uncertainty, general equilibrium, games, contracts, the dynamic models and
multiple regression; Year 3 owns the causal designs and the fields.

### Owned by another series (recall, then build)

| Notion | Owner (series, year, file) | Recalled here in | What this series adds |
|---|---|---|---|
| percentages, reading a chart | mathematics g6 `proportionality-and-data` | g6 `reading-economic-charts` | per-person values, shares, the times-ten scale |
| powers | mathematics g8 `powers` | g8 `growth-and-compounding` | compound growth, doubling time |
| weighted average | mathematics g8 `proportionality-and-speed` | g8 `inflation-and-price-indices` | the price index |
| affine functions, a percentage change as a multiplier | mathematics g9 `linear-and-affine-functions` | g9 `demand-and-supply-equations`, `elasticity-first-look` | demand and supply lines, elasticity |
| mean and median | mathematics g9 `statistics-and-probability` | g9 `income-distribution` | the two read on incomes |
| linear systems | mathematics g10 `lines-and-systems` | g10 `market-equilibrium` | equilibrium and its shifts |
| quadratic functions | mathematics g11 `quadratic-functions` | g11 `monopoly` | revenue and profit parabolas |
| derivative | mathematics g11 `differentiation` | g11 `marginal-reasoning` | marginal quantities |
| geometric sequences, recurrences | mathematics g11 `sequences`, g12 `sequences` | g12 `present-value`, `keynesian-cross`, `solow-first-look`, `fiscal-policy-and-debt` | discounting, the multiplier, accumulation, debt dynamics |
| quartiles, standard deviation | mathematics g11 `descriptive-statistics` | g11 `inequality` | Lorenz curve and Gini coefficient (areas by trapezoids, no integral) |
| expectation of a random variable | mathematics g11 `probability-random-variables` | g12 `risk-and-insurance` | expected utility, premiums |
| exponential and logarithm | mathematics g12 `exponential-logarithm` | g12 `present-value`, `inflation-and-money`, `growth-and-production-function` | continuous compounding, growth rates as differences of logarithms |
| convexity | mathematics g12 `differentiation-convexity` | g12 `risk-and-insurance` | risk aversion |
| law of large numbers | mathematics g12 `sums-lln` | g12 `risk-and-insurance` | pooling of risks |
| integral | mathematics g12 `integration` | Y1 `partial-equilibrium-welfare` | surplus with general curves |
| differential equations | mathematics g12 `differential-equations`, b1 `differential-equations` | Y1 `solow-model`, Y2 `ramsey-model` | steady states, phase diagrams |
| partial derivatives, local extrema | mathematics b1 `two-variable-functions` (the last chapter of that year) | Y1 `constrained-optimisation` (self-contained on what it uses) | the constrained optimum, the shadow price |
| extrema under constraint | mathematics b2 `differential-calculus` | Y1 `constrained-optimisation` (admitted), used freely from Y2 | — |
| matrices | mathematics b1 `matrices` | Y2 `multiple-regression` | least squares in matrix form |
| random variables, covariance | mathematics g12 `random-variables-binomial`, b2 `discrete-random-variables` | Y1 `random-variables-for-econometrics` | conditional expectation, the sampling distributions |
| central limit theorem | mathematics b3 `clt-gaussian` | Y1 `random-variables-for-econometrics`, Y2 `regression-inference` (admitted) | large-sample inference |
| Python | computer science g6 onward | Y1 `economic-data-python` | data tables, charts, regressions |
| the physical science of climate change | Earth and space sciences g12 `climate-change` | g11 `externalities`, Y3 `environmental-and-resource-economics` | the external cost and the instruments; no climate science is re-taught |
| natural resources | Earth and space sciences g9 `earth-resources` | Y3 `environmental-and-resource-economics` | prices of exhaustible resources |

Three other series overlap and are named in prose only:

- **One Quant Book** owns financial markets, derivatives and asset pricing in
  depth. This series keeps g12 `present-value`, Y2 `asset-prices` and Y2
  `banks-and-crises`, and stops there.
- **The personal finance book** (planned) owns household decisions and advice.
  This series describes households (g7 `households`, g8
  `banks-saving-interest`) and gives no advice.
- **One Artificial Intelligence Book** owns machine learning. The econometrics
  parts teach inference and causal designs, not prediction.

## Proposed data sources (for approval in one go; nothing has been fetched)

Under the workspace rule, no dataset is downloaded, probed or mirrored before the
user says yes. This table is the request. **Licences are given as recalled and
must be verified on the host's page before any download**; a source whose licence
does not allow a redrawn chart in a CC BY-NC-SA book is dropped. A source that
asks for an account or an e-mail address is not used.

| Source | Host | Used for | Licence (as recalled, to verify) |
|---|---|---|---|
| Our World in Data | ourworldindata.org | finding each long-run series and its original source; its own processed series where it is the only compiler | CC BY 4.0 for its own work; third-party series keep their own terms |
| Maddison Project Database | rug.nl/ggdc | income per person since year 1; population | CC BY 4.0 |
| Penn World Table | rug.nl/ggdc | purchasing-power GDP, capital, hours, productivity since 1950 | CC BY 4.0 |
| World Development Indicators | data.worldbank.org | cross-country series since 1960 | CC BY 4.0 for most series |
| Poverty and Inequality Platform | pip.worldbank.org | poverty rates and counts, Gini coefficients | CC BY 4.0 |
| Worldwide Governance Indicators | worldbank.org | rule of law, control of corruption | CC BY 4.0 |
| World Population Prospects | population.un.org | population, fertility, life expectancy, age structure, projections | CC BY 3.0 IGO |
| Gapminder | gapminder.org/data | life expectancy, child mortality and fertility before 1950 | CC BY 4.0 |
| Macrohistory Database | macrohistory.net | 18 economies since 1870: output, prices, interest rates, credit, crises, returns, public debt | CC BY-NC-SA 4.0 |
| A Millennium of Macroeconomic Data | bankofengland.co.uk | one country's prices, wages, population and interest rates over centuries | open government-style licence |
| OECD data | oecd.org | hours worked, tax revenue by type, public spending, Gini before and after transfers, benefit systems | CC BY 4.0 since 2024 |
| IMF: World Economic Outlook, Historical Public Debt, Public Finances in Modern History | imf.org | debt, deficits, current accounts, central-bank data | IMF terms |
| BIS statistics | bis.org | policy rates, exchange rates, credit | BIS terms |
| National statistical agencies of the United States (BEA, BLS, Census) | bea.gov, bls.gov, census.gov | national accounts, consumer prices, labour-force flows, public-use survey samples for the econometrics chapters | public domain |
| Eurostat | ec.europa.eu/eurostat | European series | reuse allowed with attribution |
| ILOSTAT | ilostat.ilo.org | employment by sector, participation | CC BY 4.0 |
| FAOSTAT | fao.org/faostat | crop yields, food supply | CC BY 4.0 |
| Barro–Lee | barrolee.com | years of schooling since 1950 | terms to check |
| World Inequality Database | wid.world | top income shares, world distribution | terms to check |
| Global Carbon Budget | globalcarbonbudget.org | carbon dioxide emissions | CC BY 4.0 |
| Community Emissions Data System | github.com/JGCRI/CEDS | sulphur dioxide and other air pollutants | CC BY 4.0 |
| US Energy Information Administration | eia.gov | energy use, energy prices | public domain |
| CEPII Gravity | cepii.fr | bilateral trade, distance, borders | open licence |
| Federico–Tena World Trade Historical Database | e-archivo.uc3m.es | world trade 1800–1938 | terms to check |
| Economic freedom indices | fraserinstitute.org | economic freedom against income | terms to check |
| World Happiness Report tables | worldhappiness.report | average life satisfaction by country | terms to check; the underlying survey is proprietary |

Not proposed: the Energy Institute's *Statistical Review* (restricted); mortality
and income microdata that require registration; trade microdata whose terms
forbid redistribution (small derived tables only, if at all). Numbers read from a
published paper (laboratory markets, a study's estimates, the price of light) go
through the source ledger as cited facts, not as datasets. Where a published
study's microdata has no clear licence, the econometrics chapter uses simulated
data calibrated on the study's published moments, and says so.

## Conventions for the writing step (proposed, to confirm at the scaffold)

- **Exercise calibration**, as in chemistry, Earth and computer science:
  - grades 6–9: 12 exercises and a weekend problem of 10–14 questions
    (Parts I–III);
  - grades 10–12: exactly 15 exercises (5★/6★★/4★★★) and a problem of 18–22
    questions (Parts I–IV) ending on a named result;
  - university years: exactly 12 exercises (4★/5★★/3★★★) and one problem of
    22–28 questions.
- **Kinds of exercise.** Each chapter mixes four kinds: read a chart or a
  table; compute; use a model to predict a direction and a size; say what
  observation would contradict the model. From Year 1, data exercises have a
  tested Python solution.
- **Boxes.** `model{name}` with its four fields (Assumes, Predicts, Tested,
  Breaks); `debate[title]` (an open empirical question, the estimates, how
  solid each is); `record[title]` (a dated episode used as a test: what
  happened, what the model said); `measure[title]` (how a number is made);
  `recall`; `dated{<year>}`. No `history` box.
- **Charts.** One opening chart per chapter (`\omopeningchart`, with its source
  line), 21 charts in grade 6. Every chart is a pgfplots figure fed by a CSV
  that a tested script under `figdata/<year>/NN-<slug>/` writes from a file in
  `data/`. Diagrams (supply and demand, Edgeworth box, game tree, phase
  diagram) are TikZ with shared styles in `styles/oneeconomics.sty`.
- **Ledgers.** A source ledger per chapter for every checkable external fact
  (URL, access date), as in the quant series; a data ledger for every dataset
  (host, version, licence, date of approval, date of download), checked by a
  script.
- **Code mechanics** (Year 1 on), ported from the computer science series:
  `\omcode` and `\omoutput`, `tools/capture_output.py` as the only writer of
  printed output, `tools/test_code.sh`. Python with pandas and statsmodels,
  versions pinned.
- **Invented data for exercises.** One invented country with its national
  accounts, a household survey, a census of firms and a trading neighbour,
  generated by a seeded, tested script, so that exercise numbers are clean and
  owned by the series. It could be the country around the computer science
  series' invented town.
- **Real names.** Countries and dated episodes are named, because they are the
  evidence. A firm is named only with a public source. A person is named only
  as the label of a model or a result.
- **Neutral vocabulary.** Terms that carry a verdict are not used as if
  neutral; a chapter states what a policy does, to whom and by how much.
- **Before release**: the verification first pass of `../book_style.md` (every
  solution recomputed by a fresh reader); a neutrality review read once from the
  left and once from the right (`../future_books.md`, rule 5); fresh expert
  readers are proposed and not yet decided.

## Open points

- **Size.** 172 chapters is seven more than computer science, the largest
  school series so far. First places to cut: g12 `risk-and-insurance`, Y2
  `ramsey-model` and `business-cycles`, Y3 `binary-outcomes`.
- **Starting at Book 2.** The twenty-one charts are owned by grade 6 and Book 2
  does not repeat them. A reader who starts in grade 10 meets them only through
  recall boxes. Book 2 could reprint them as a short appendix.
- **The Malthusian model** appears in Y3 `demographic-transition` as a model in
  its frame: it fits the data before 1800 and fails after. To confirm, given the
  rule against teaching past mistakes.
- **Behavioural economics.** One chapter (Y2 `behavioural-evidence`), limited to
  findings that replicated. It can be removed.
- **Finance.** g12 `present-value`, Y2 `asset-prices` and Y2 `banks-and-crises`
  are all the finance in the series. The quant series is the place for more.
- **Photographs and AI illustrations.** `../book_style.md` scopes them per
  series. Proposed: charts and TikZ diagrams first; free-licence photographs of
  specific real things (a hyperinflation banknote, a container port); AI
  illustrations for everyday scenes in grades 6–9 only.
- **Currency in exercises.** Real currencies for real data; for invented
  exercises, either an invented currency or a bare symbol. To settle at the
  scaffold.
- **Series notation.** A notation table ($p$, $q$, $Y$, $C$, $I$, $G$, $K$, $L$,
  $A$, $r$, $i$, $\pi$, $u$, $w$) is fixed at the scaffold and printed in
  Year 1.
- **Data sources.** The table above needs a yes, source by source or as a whole,
  after the licences are verified.
- **Pilots.** Three pilot chapters before any batch, as in the other series:
  proposed g6 `living-standards`, g10 `ricardo-model` and b1 `is-lm`.
- **Still open from `../economics_series.md`**: whether the series moves up the
  order; whether the personal finance book is written first; fresh expert
  readers before release.
- **Chapter lists against the programme texts.** The lists were written from
  knowledge of the programmes and of the international sequence, not from the
  official texts. Each book's list is checked against them before it is
  written (`sources/outline_sources.md`).
