"""Exercise 5: the trilemma regression on JST data, by era.

Yearly change in the short-term rate on the change in the base country's rate
(peg_base: GBR, USA or DEU), separately for pegs and floats.
"""
import numpy as np
import statsmodels.formula.api as smf
from econdata import jst

j = jst(cols=["peg_type", "peg_base", "stir"]).sort_values(["iso3", "year"])
j["d"] = j.groupby("iso3").stir.diff()
base = j.set_index(["iso3", "year"]).d
j = j[j.peg_base.isin(["GBR", "USA", "DEU"]) & j.peg_type.isin(["PEG", "FLOAT"])].copy()
j["db"] = [base.get((b, y), np.nan) for b, y in zip(j.peg_base, j.year)]
j = j.dropna(subset=["d", "db"])

eras = {"1870-1913": (1870, 1913), "1950-1972": (1950, 1972),
        "1973-1998": (1973, 1998), "1999-2020": (1999, 2020)}
for era, (a, b) in eras.items():
    line = []
    for regime in ("PEG", "FLOAT"):
        g = j[(j.peg_type == regime) & j.year.between(a, b)]
        r = smf.ols("d ~ db", g).fit()
        b_, se = r.params["db"], r.bse["db"]
        line.append(f"{regime.lower()} {b_:.2f} ({se:.2f}, n={len(g)})")
    print(f"{era}: " + "; ".join(line))
