"""Cereal yield against fertiliser use (WDI, 2018-2020 means) and the Kenya fertiliser trials (cited table).

Grade 11, chapter 2 (production-and-costs). World Bank WDI AG.YLD.CREL.KG (cereal yield, kg per hectare) and
AG.CON.FERT.ZS (fertiliser consumption, kg per hectare of arable land), countries only, means over 2018-2020 of
the years available. Fit: yield = a + b log10(fertiliser); the marginal product of fertiliser is then
b / (f ln 10) kg of grain per kg of fertiliser. Cited: Duflo, Kremer and Robinson (2008), Table 1 (src/fertilizer.csv).
Writes:
  out/cereal.csv       iso3, fert, yield
  out/cereal_fit.csv   n, a, b, mp20, mp200 (kg of grain per extra kg of fertiliser at 20 and 200 kg/ha)
  out/cereal_curve.csv fert, yield (the fitted curve)
  out/cereal_marked.csv iso3, fert, yield (KEN, IND, USA, NLD, CHN)
  out/fertilizer.csv   dose, yield_pct, return_pct, plots, step_yield (extra yield of each step, points) with a 0 row
"""
import numpy as np
import pandas as pd

from cited import load_cited
from econdata import wdi
from figout import write_table

MARK = ["KEN", "IND", "USA", "NLD", "CHN"]


def cereal():
    y = wdi("AG.YLD.CREL.KG", countries_only=True)
    f = wdi("AG.CON.FERT.ZS", countries_only=True)
    y = y[y.year.between(2018, 2020)].groupby("iso3").value.mean().rename("yield")
    f = f[f.year.between(2018, 2020)].groupby("iso3").value.mean().rename("fert")
    d = pd.concat([f, y], axis=1).dropna()
    d = d[d.fert > 0].reset_index().sort_values("iso3").reset_index(drop=True)
    d["fert"] = d.fert.round(1)
    d["yield"] = d["yield"].round(0)
    b, a = np.polyfit(np.log10(d.fert), d["yield"], 1)
    fit = pd.DataFrame({"n": [len(d)], "a": [round(a, 0)], "b": [round(b, 0)],
                        "mp20": [round(b / (20 * np.log(10)), 1)], "mp200": [round(b / (200 * np.log(10)), 1)]})
    xs = np.round(np.logspace(np.log10(1), np.log10(1500), 40), 2)
    curve = pd.DataFrame({"fert": xs, "yield": np.round(a + b * np.log10(xs), 0)})
    curve = curve[curve["yield"] > 0]
    return d, fit, curve, d[d.iso3.isin(MARK)]


def fertilizer():
    c = load_cited(__file__, "fertilizer").drop(columns="ledger")
    c = pd.concat([pd.DataFrame({"dose": [0.0], "yield_pct": [0.0], "return_pct": [np.nan], "plots": [np.nan]}), c],
                  ignore_index=True)
    c["step_yield"] = c.yield_pct.diff().round(1)
    return c


if __name__ == "__main__":
    d, fit, curve, marked = cereal()
    write_table(d, __file__, "cereal")
    write_table(fit, __file__, "cereal_fit")
    write_table(curve, __file__, "cereal_curve")
    write_table(marked, __file__, "cereal_marked")
    write_table(fertilizer(), __file__, "fertilizer")
