"""Real annual returns from the JST Macrohistory Database, for this chapter's scripts.

real return = (1 + nominal) / (1 + inflation) - 1, with inflation from the CPI, for
equities (eq_tr), long government bonds (bond_tr) and bills (bill_rate); real
consumption growth per person from rconsbarro.
"""

from econdata import jst

ASSETS = {"equity": "eq_tr", "bond": "bond_tr", "bill": "bill_rate"}


def real_returns(since=1950, until=2020):
    d = jst(cols=[*ASSETS.values(), "cpi", "rconsbarro"]).sort_values(["iso3", "year"])
    g = d.groupby("iso3")
    d["infl"] = g.cpi.pct_change()
    d["dc"] = g.rconsbarro.pct_change()
    for name, col in ASSETS.items():
        d[name] = (1 + d[col]) / (1 + d.infl) - 1
    d = d[d.year.between(since, until)]
    has = d.groupby("iso3")[list(ASSETS)].count().min(axis=1)
    keep = has[has == until - since + 1].index
    return d[d.iso3.isin(keep)][["iso3", "year", *ASSETS, "dc"]].reset_index(drop=True)
