"""The first stage of a geographic instrument for trade, 2019.

A gravity regression that sees only geography and size (log population-weighted
distance, contiguity, log populations) predicts each pair's trade relative to the
origin's GDP; summing a country's predicted pairs gives its *built* trade share.
Plotted against the actual trade share (WDI NE.TRD.GNFS.ZS, goods and services).

Writes
  out/first_stage.csv       iso3, built, trade (both percent of GDP), countries in PWT 2019
  out/first_stage_line.csv  built, trade: the log-log least-squares line at the two ends
  out/first_stage_stats.csv slope, se, F (bivariate), F_pop and slope_pop (with log population),
                            n; the gravity fit's distance and contiguity coefficients, R2, pairs
Book 5, chapter 1, opening chart.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import gravity, pwt, wdi
from figout import write_table

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "distw_harmonic", "contig",
        "pop_o", "pop_d", "gdp_o"]


def built_share():
    g = gravity(2019, 2019, columns=COLS)
    back = g.rename(columns={"iso3_o": "iso3_d", "iso3_d": "iso3_o",
                             "tradeflow_baci": "back"})[["iso3_o", "iso3_d", "back"]]
    g = g.merge(back, on=["iso3_o", "iso3_d"], how="left").fillna({"back": 0})
    g["share"] = (g.tradeflow_baci + g.back) / g.gdp_o
    g = g.dropna(subset=["share", "pop_o", "pop_d", "distw_harmonic"])
    g = g[g.share > 0]
    G = sm.add_constant(pd.DataFrame({"ldist": np.log(g.distw_harmonic),
                                      "lpo": np.log(g.pop_o), "lpd": np.log(g.pop_d),
                                      "contig": g.contig}))
    fit = sm.OLS(np.log(g.share), G).fit()
    g["fit"] = np.exp(fit.fittedvalues)
    return g.groupby("iso3_o").fit.sum().mul(100).rename("built"), fit


def tables():
    built, grav = built_share()
    w = wdi("NE.TRD.GNFS.ZS", since=2019, until=2019, countries_only=True)
    p = pwt(since=2019, until=2019, cols=["rgdpo", "emp", "pop"]).set_index("iso3")
    d = pd.concat([built, w.set_index("iso3").value.rename("trade"), p], axis=1,
                  join="inner").dropna()
    d.index.name = "iso3"
    lb, lt, lpop = np.log(d.built), np.log(d.trade), np.log(d["pop"])
    f1 = sm.OLS(lt, sm.add_constant(lb)).fit()
    f2 = sm.OLS(lt, sm.add_constant(pd.DataFrame({"lb": lb, "lpop": lpop}))).fit()
    ends = np.array([d.built.min(), d.built.max()])
    line = pd.DataFrame({"built": ends,
                         "trade": np.exp(f1.params.iloc[0] + f1.params.iloc[1] * np.log(ends))})
    stats = pd.DataFrame({"slope": [f1.params.iloc[1]], "se": [f1.bse.iloc[1]],
                          "F": [f1.tvalues.iloc[1] ** 2], "F_pop": [f2.tvalues["lb"] ** 2],
                          "slope_pop": [f2.params["lb"]], "n": [len(d)],
                          "dist": [grav.params["ldist"]], "contig": [grav.params["contig"]],
                          "r2": [grav.rsquared], "pairs": [int(grav.nobs)]})
    pts = d[["built", "trade"]].reset_index()
    return pts, line, stats


if __name__ == "__main__":
    pts, line, stats = tables()
    write_table(pts, __file__, "first_stage")
    write_table(line, __file__, "first_stage_line")
    write_table(stats, __file__, "first_stage_stats")
