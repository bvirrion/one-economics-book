"""Book 5 -- en. Curation only; the rules live in tools/termlink/.

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
STOP = {
    # ordinary words outside their defining chapter, or a second sense elsewhere
    "institutions", "Institutions",   # "financial institutions", "the institutions of a currency union"
    "poverty trap",                   # ch. 18's participation-tax sense vs ch. 34's development model
    "cutoff",                         # the RD threshold vs any cut-off
    "reproduction",                   # reproducing a study vs demographic reproduction (ch. 33)
    "scale effect",                   # labour demand vs scale effects in trade and growth
    "monotonicity",                   # the IV assumption vs monotone functions
}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
EXTRA_PROTECT = [
    # source lines and captions of charts are not prose to link
    r"\\begin\{(?:omchart|openingchart)\}\{[^{}]*\}\{[^{}]*\}",
    # a present-value factor, not ch. 19's insurance product
    r"annuity\s+factor",
    # ch. 15's market event study (prices around an announcement), not ch. 3's dynamic DiD
    r"event\s+study\s+sees",
    r"an\s+event\s+study\s+then",
]
