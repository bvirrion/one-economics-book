"""Published estimates of the government-spending multiplier; Brenland's propensities.

Grade 12, chapter 9 (the Keynesian cross and the multiplier).
src/multipliers.csv: Ramey (2019, NBER WP 25531) Table 1, government spending multipliers using aggregate data with no
state dependence, typed from the table and checked against the ledger by cited.py; a single estimate has lo = hi.
Brenland (invented, code/shared/country): marginal propensity to consume out of disposable income (GDP minus revenue), the
tax share and the marginal propensity to import, each the slope of a least-squares line over 2001-2025, rounded to two
decimals; multipliers computed from the rounded values; a spending rise of 1 % of 2025 GDP.
Writes:
  out/multipliers.csv   pos, label, lo, hi, mid, em, ep, method
  out/brenland_key.csv  c, t, m, gdp2025, dG, k_c, k_ct, k_ctm, gain_ctm, k_offset, gain_offset
"""
import numpy as np
import pandas as pd

import country
from cited import load_cited
from figout import write_table


def estimates():
    d = load_cited(__file__, "multipliers").drop(columns="ledger")
    d = d.reset_index(drop=True)
    d["pos"] = len(d) - d.index
    d["mid"] = ((d.lo + d.hi) / 2).round(3)
    d["em"] = (d.mid - d.lo).round(3)
    d["ep"] = (d.hi - d.mid).round(3)
    return d[["pos", "label", "lo", "hi", "mid", "em", "ep", "method"]]


def brenland():
    a = country.load("accounts").set_index("year")
    c = round(float(np.polyfit(a.gdp - a.revenue, a.C, 1)[0]), 2)
    t = round(float(np.polyfit(a.gdp, a.revenue, 1)[0]), 2)
    m = round(float(np.polyfit(a.gdp, a.M, 1)[0]), 2)
    y = int(a.loc[2025, "gdp"])
    dg = round(0.01 * y)
    k_ctm = 1 / (1 - c * (1 - t) + m)
    offset = 0.5                     # the central bank's response cuts other spending by half the rise (given)
    return pd.DataFrame([{"c": c, "t": t, "m": m, "gdp2025": y, "dG": dg,
                          "k_c": round(1 / (1 - c), 2), "k_ct": round(1 / (1 - c * (1 - t)), 3),
                          "k_ctm": round(k_ctm, 3), "gain_ctm": round(k_ctm * dg),
                          "k_offset": round(k_ctm * (1 - offset), 3), "gain_offset": round(k_ctm * (1 - offset) * dg)}])


if __name__ == "__main__":
    write_table(estimates(), __file__, "multipliers")
    write_table(brenland(), __file__, "brenland_key")
