"""The RAND Health Insurance Experiment by plan (cited) and an invented lemons market (seeded simulation).

Grade 11, chapter 8 (asymmetric information).
Cited (src/hie.csv): Aron-Dine, Einav and Finkelstein (2012), Table 2: the free-care plan's mean spending and share with any
spending, and each coinsurance plan's difference from it (2011 dollars). Levels are free-care mean plus difference.
Invented: 1000 car qualities drawn with a fixed seed, uniform on [2000, 10000] dalens ("floor") and on [0, 10000]
("nofloor"); sellers value a car at its quality, buyers at 1.5 times it; each round buyers offer 1.5 times the average
quality of the cars offered at the last round's price.
Writes:
  out/hie.csv      plan, label, x, spend, anyuse_pct
  out/lemons.csv   round, floor, nofloor  (price, dalens)
  out/lemons_end.csv  case, price, share_traded
"""
import numpy as np
import pandas as pd

from cited import load_cited
from figout import write_table

LABELS = {"free": "free", "c25": "25\\,\\%", "c50": "50\\,\\%", "c95": "95\\,\\%"}


def hie():
    d = load_cited(__file__, "hie")
    free = d[d.plan == "free"].iloc[0]
    spend = [free.spend if p == "free" else free.spend + s for p, s in zip(d.plan, d.spend)]
    anyu = [free.anyuse if p == "free" else free.anyuse + a for p, a in zip(d.plan, d.anyuse)]
    return pd.DataFrame({"plan": d.plan, "label": [LABELS[p] for p in d.plan], "x": range(len(d)),
                         "spend": [int(round(v)) for v in spend], "anyuse_pct": [round(100 * v, 1) for v in anyu]})


def lemons(low, rounds=15, seed=11):
    q = np.random.default_rng(seed).uniform(low, 10000, 1000)
    p = 1.5 * q.mean()
    prices = [p]
    for _ in range(rounds):
        offered = q[q <= p]
        p = 1.5 * offered.mean() if len(offered) else 0.0
        prices.append(p)
    return prices, float((q <= p).mean())


if __name__ == "__main__":
    write_table(hie(), __file__, "hie")
    a, sa = lemons(2000)
    b, sb = lemons(0)
    write_table(pd.DataFrame({"round": range(len(a)), "floor": np.round(a, 0), "nofloor": np.round(b, 0)}), __file__, "lemons")
    write_table(pd.DataFrame({"case": ["floor", "nofloor"], "price": [round(a[-1]), round(b[-1])],
                              "share_traded": [round(sa, 3), round(sb, 3)]}), __file__, "lemons_end")
