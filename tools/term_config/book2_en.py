"""Book 2 -- en. Curation only; the rules live in tools/termlink/.

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
# Everyday words that are also defined terms: linked only in their defining chapters. "normal" and "inferior" (goods),
# "idea" (a non-rival good), "share" (in a company vs "a share of"), "reserves" (a bank's vs foreign-currency reserves),
# "expansion" (the cycle phase vs any growth), "strategy"/"dominant" (games vs plans), "loading" and "prevention"
# (insurance), "pooling" and "screening" (information), "anchored" and "sustainable" (bare), "depreciation" (bare: capital
# vs currency, the homograph rule of SERIES_DEFINITIONS), "investment" (national accounts vs investment in schooling),
# "long run" and "short run" (a firm's fixed input vs the macroeconomic long and short run of grade 12); "short-run supply"
# and "long-run supply" (a market's supply in grade 10 vs aggregate supply in the AD-AS chapters of grade 12).
STOP = {"normal", "Normal", "normally", "inferior", "idea", "ideas", "Ideas", "share", "Share", "shares", "reserves",
        "expansion", "strategy", "strategies", "dominant", "loading", "prevention", "pooling", "screening", "anchored",
        "sustainable", "sustainability", "speculation", "depreciation", "investment", "long run", "short run",
        "short-run supply", "Short-run supply", "long-run supply", "Long-run supply"}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
EXTRA_PROTECT = [
    # source lines and captions of charts are not prose to link
    r"\\begin\{(?:omchart|openingchart)\}\{[^{}]*\}\{[^{}]*\}",
    # the verb, not shares in a company
    r"shares\s+the\s+risk",
]
