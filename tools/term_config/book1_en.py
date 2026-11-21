"""Book 1 -- en. Curation only; the rules live in tools/termlink/.

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
# Books 1-2 recall school notions across chapters: an ambiguous term links to the nearest
# preceding definition.
AMBIG_POLICY = "nearest-preceding"
# "share" and "exchange" are everyday words in most of their uses ("shared out", "share one currency",
# "in exchange for", "a currency exchange counter"): linked in their defining chapters only.
STOP = {"share", "Share", "shares", "exchange", "Exchange"}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
EXTRA_PROTECT = [
    # source lines and captions of charts are not prose to link
    r"\\begin\{(?:omchart|openingchart)\}\{[^{}]*\}\{[^{}]*\}",
    # the capital city of Brenland, not physical capital
    r"the\s+capital\s+of", r"near\s+its\s+capital",
    # a loss in another sense than a firm's loss
    r"loss\s+of\s+laying\s+hens", r"not\s+a\s+loss", r"two\s+losses",
]
