"""The trilemma test on JST data: the yearly change in a country's short-term rate
against the change in its base country's rate (the database's peg_base: GBR, USA or
DEU), for pegs and for floats."""
import numpy as np
import statsmodels.formula.api as smf
from econdata import jst

ERAS = {"1870-1913": (1870, 1913), "1950-1972": (1950, 1972),
        "1973-1998": (1973, 1998), "1999-2020": (1999, 2020)}


def changes():
    j = jst(cols=["peg_type", "peg_base", "stir"]).sort_values(["iso3", "year"])
    j["d"] = j.groupby("iso3").stir.diff()
    base = j.set_index(["iso3", "year"]).d
    j = j[j.peg_base.isin(["GBR", "USA", "DEU"]) & j.peg_type.isin(["PEG", "FLOAT"])]
    j = j.copy()
    j["db"] = [base.get((b, y), np.nan) for b, y in zip(j.peg_base, j.year)]
    return j.dropna(subset=["d", "db"]).reset_index(drop=True)


def slope(g):
    r = smf.ols("d ~ db", g).fit()
    return r.params["db"], r.bse["db"], r.rsquared, len(g)
