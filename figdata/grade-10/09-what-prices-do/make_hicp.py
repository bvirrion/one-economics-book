"""Fuel prices and hairdressing prices in five euro-area countries: monthly 12-month rates of change, 2001-2024.

Grade 10, chapter 9 (what-prices-do): a traded good's price moves together across countries (arbitrage);
a local service's price does not. Eurostat HICP, prc_hicp_manr (annual rate of change, %), COICOP CP0722
(fuels and lubricants for personal transport equipment) and CP1211 (hairdressing salons and personal
grooming establishments).
Writes:
  out/fuel_rates.csv   t (decimal year), DE, FR, IT, ES, NL
  out/hair_rates.csv   t, DE, FR, IT, ES, NL
  out/hicp_summary.csv item, mean_corr (mean of the 10 pairwise correlations), mean_spread (mean over months of
                       the gap between the highest and lowest rate, percentage points), n_months
"""
import itertools

import numpy as np
import pandas as pd

from econdata import eurostat
from figout import write_table

GEOS = ["DE", "FR", "IT", "ES", "NL"]
ITEMS = {"fuel": "CP0722", "hair": "CP1211"}
SINCE, UNTIL = "2001-01", "2024-12"


def wide(m, code):
    d = m[(m.coicop == code) & m.geo.isin(GEOS) & (m.time >= SINCE) & (m.time <= UNTIL)]
    w = d.pivot(index="time", columns="geo", values="value")[GEOS].dropna().sort_index()
    t = [int(s[:4]) + (int(s[5:7]) - 0.5) / 12 for s in w.index]
    out = w.reset_index(drop=True).round(1)
    out.insert(0, "t", np.round(t, 3))
    return out


def tables():
    m = eurostat("prc_hicp_manr")
    m = m[m.unit == "RCH_A"]
    res, rows = {}, []
    for name, code in ITEMS.items():
        w = wide(m, code)
        res[name] = w
        c = [np.corrcoef(w[a], w[b])[0, 1] for a, b in itertools.combinations(GEOS, 2)]
        spread = (w[GEOS].max(axis=1) - w[GEOS].min(axis=1)).mean()
        rows.append({"item": name, "mean_corr": round(float(np.mean(c)), 2),
                     "mean_spread": round(float(spread), 1), "n_months": len(w)})
    return res["fuel"], res["hair"], pd.DataFrame(rows)


if __name__ == "__main__":
    f, h, s = tables()
    write_table(f, __file__, "fuel_rates")
    write_table(h, __file__, "hair_rates")
    write_table(s, __file__, "hicp_summary")
