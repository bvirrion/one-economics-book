"""Book 4 -- en. Curation only; the rules live in tools/termlink/.

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
# ordinary words outside their defining chapter: "value" (of a zero-sum game) vs every
# other value; "type" (of a player) vs "a type of"; "support" (of a mixed strategy) vs
# policy support; "complete" (markets) vs "a complete record"; "feasible" (allocation)
# vs "feasible payoffs" and everyday use; "credible" (policy) vs "a credible estimate".
STOP = {"value", "values", "type", "types", "support", "supports", "Support", "complete",
        "feasible", "credible"}  # fmt: skip
NO_CAPITAL = set()
EXTRA = {}
# hyphenated compounds the morphology attaches to the wrong head: a p-value and an
# option value are not the value of a game; private and common values are auction
# terms; "two-type" is a model size; a bare "rational" is not rational expectations.
DROP = {"p-value", "option-value", "private-values", "common-value", "two-type", "rational"}
DERIVED = {}
EXTRA_PROTECT = [
    # source lines and captions of charts are not prose to link
    r"\\begin\{(?:omchart|openingchart)\}\{[^{}]*\}\{[^{}]*\}",
    # loading data into memory, not an insurance loading (ch. 30 listing caption)
    r"Loading\s+the\s+comparison",
    # random assignment, not a lottery in the expected-utility sense
    r"by\s+lottery",
    r"a\s+lottery\s+decided",
    # cash flow as information, not a signal of a signalling game
    r"today\s+signals",
    # in the chapter that defines the value of a game: statistics and a verb
    r"p-value",
    r"critical\s+value",
    r"inspector\s+values",
]
