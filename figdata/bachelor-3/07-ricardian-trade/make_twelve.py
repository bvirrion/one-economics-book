"""Brenland and Kestria with twelve goods (invented): the weekend problem of chapter 7.

Hours of labour per unit in each country; cloth and grain are the series' ricardo.csv
values (data/country/ricardo.csv), the other ten goods are added here. Equal expenditure
shares (1/12 each); equal labour forces (r = 1). Solved with twelve.py: free trade,
a 10 % iceberg cost (kappa = 1.1), and free trade after Kestria's labour requirements
all fall by a sixth (productivity up 20 %).
Writes out/twelve_goods.csv (good, hours_B, hours_K) and out/twelve_results.csv."""
from pathlib import Path

import pandas as pd
from figout import write_table
from twelve import equilibrium, real_gain, real_gain_foreign

ROOT = Path(__file__).resolve().parents[3]
EXTRA = [("timber", 3, 12), ("fish", 2, 6), ("wool", 5, 12), ("cheese", 3, 6),
         ("paper", 4, 7), ("glass", 5, 6.9), ("tools", 4, 5), ("shoes", 6, 6),
         ("clocks", 10, 8), ("radios", 10, 6)]


def goods():
    r = pd.read_csv(ROOT / "data" / "country" / "ricardo.csv")
    h = r.pivot(index="good", columns="country", values="hours_per_unit")
    base = [(g, float(h.loc[g, "Brenland"]), float(h.loc[g, "Kestria"]))
            for g in ["grain", "cloth"]]
    d = pd.DataFrame(base + [(g, float(b), float(k)) for g, b, k in EXTRA],
                     columns=["good", "hours_B", "hours_K"])
    d["A"] = d.hours_K / d.hours_B
    return d.sort_values("A", ascending=False).reset_index(drop=True)


def tables():
    d = goods()
    A = list(d.A)
    rows = []
    for name, AA, kappa in [("free trade", A, 1.0), ("iceberg 10 %", A, 1.1),
                            ("Kestria +20 %", [a / 1.2 for a in A], 1.0)]:
        w, e, m, nt = equilibrium(AA, 1.0, kappa)
        rows.append((name, w, e, m, nt, real_gain(AA, w, kappa),
                     real_gain_foreign(AA, w, kappa)))
    res = pd.DataFrame(rows, columns=["case", "omega", "exported", "imported",
                                      "nontraded", "gain_B", "gain_K"])
    return d[["good", "hours_B", "hours_K"]], res


if __name__ == "__main__":
    g, r = tables()
    write_table(g, __file__, "twelve_goods")
    write_table(r, __file__, "twelve_results")
