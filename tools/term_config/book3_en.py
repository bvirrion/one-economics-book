"""Book 3 -- en. Curation only; the rules live in tools/termlink/.

The book's writer curates this file in Phase C. Economics homographs to check
against each target: a market (the idea vs a market square), demand and supply
(the curves vs everyday "demand"), a good (a product vs "good"), a cost, a price,
a rate (interest, exchange, unemployment, tax, growth), capital (physical,
human, financial, a capital city), interest (a rate vs "of interest"), a return,
a share (an equity vs "a share of"), a margin (at the margin vs a profit margin),
a premium, a bond, a firm (a company vs "firm"), a model, a shock, a surplus
(consumer surplus vs a budget surplus), a deficit, a balance, an account (the
current account vs a bank account), a policy, a utility (preferences vs a power
company), an equilibrium, a game, a strategy, a signal, a contract, a trend, a
cycle, a lag, a sample, an estimate, a bias (statistical vs behavioural), a
weight, a basket, an index, inflation, a reserve, money, a bank, a union.
Use STOP (ordinary word outside its defining chapter), DROP (never a link),
NO_CAPITAL (skip sentence-initial matches), EXTRA (manual term -> label),
EXTRA_PROTECT (regex phrases in another sense; multi-word patterns use \\s+).
Watch the capitalised-harvest trap: a display opening its sentence is harvested
capitalised, and STOP/DROP match case-sensitively.
"""
# Everyday or overloaded words: linked in their defining chapters only. "population" and
# "power" are statistical terms in ch. 31 but ordinary words elsewhere (Brenland's
# population, market power, purchasing power); "residual" is the regression residual
# but also the Solow residual; "normal" is also the normal distribution; "convex" and
# "stable" have their mathematical senses; "local" and "neutral" are everyday words.
STOP = {
    "population", "power", "residual", "residuals", "stock", "stocks", "flow", "flows",
    "stable", "stability", "normal", "local", "neutral", "adaptive", "binding", "convex",
    "monotone", "rational", "parameter", "parameters", "participation", "size",
}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
EXTRA_PROTECT = [
    # source lines and captions of charts are not prose to link
    r"\\begin\{(?:omchart|openingchart)\}\{[^{}]*\}\{[^{}]*\}",
]
