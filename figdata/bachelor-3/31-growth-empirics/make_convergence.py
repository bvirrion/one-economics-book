"""Chart 2: absolute convergence. Annual growth of real GDP per person 1960--2019
(rgdpna / pop) against GDP per person in 1960 (rgdpe / pop, log scale), all countries
with both years in PWT 11.0, and those of Western Europe and its offshoots
(Maddison's regions, a group fixed by geography, not by later income). Writes
out/convergence.csv (lx = log10 of
1960 income, growth, club flag), out/convergence_fit_all.csv,
out/convergence_fit_rich.csv and out/convergence_stats.csv (slope per unit of
ln income, standard error, n, implied speed of convergence)."""
import numpy as np
import pandas as pd
from econdata import maddison
from figout import write_table
from growthdata import growth, income, income_na

T = 59


def ols(x, y):
    X = np.column_stack([np.ones(len(x)), x])
    b, res, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ b
    s2 = (e @ e) / (len(x) - 2)
    se = np.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])
    return b, se


def tables():
    w = income()
    g = growth(income_na(), 1960, 2019)
    g = g[g.index.isin(w.columns[w.loc[1960].notna()])]
    y0 = w.loc[1960, g.index]
    d = pd.DataFrame({"iso3": g.index, "lx": np.log10(y0.to_numpy()),
                      "growth": g.to_numpy()})
    reg = maddison(since=2000, until=2000)[["iso3", "region"]].drop_duplicates()
    d = d.merge(reg, on="iso3", how="left")
    d["rich"] = d.region.isin(["Western Europe", "Western Offshoots"])
    d = d.drop(columns="region")
    rows, fits = [], {}
    for name, sub in [("all", d), ("rich", d[d.rich])]:
        b, se = ols(np.log(10 ** sub.lx), sub.growth / 100)
        beta = b[1]
        speed = -np.log(1 + beta * T) / T
        rows.append({"sample": name, "slope": beta, "se": se, "n": len(sub),
                     "speed": 100 * speed})
        xs = np.array([sub.lx.min(), sub.lx.max()])
        fits[name] = pd.DataFrame({"lx": xs,
                                   "growth": 100 * (b[0] + beta * np.log(10 ** xs))})
    return d, fits, pd.DataFrame(rows)


if __name__ == "__main__":
    d, fits, st = tables()
    write_table(d, __file__, "convergence")
    write_table(fits["all"], __file__, "convergence_fit_all")
    write_table(fits["rich"], __file__, "convergence_fit_rich")
    write_table(st, __file__, "convergence_stats")
