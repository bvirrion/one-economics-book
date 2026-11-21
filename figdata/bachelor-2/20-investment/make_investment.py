"""Investment, chapter 20.

Opening chart: Grunfeld's eleven US firms, 1935-1954 (statsmodels grunfeld, public
domain): gross investment against market value, each divided by the firm's own
1935-1954 mean. Chart 2: gross investment as a share of GDP, per cent, United
States, Germany and Japan, 1870-2020 (JST Macrohistory, iy). Record: US real house
prices (JST hpnom deflated by the BLS CPI-U, all items, annual average of the twelve
months) and investment, 1996-2012.
Writes
  out/grunfeld.csv         firm, year, i_rel, v_rel
  out/grunfeld_summary.csv one row: n, firms, corr, slope, fe_value, fe_capital,
                           fe_value_se, fe_capital_se, fe_r2, pooled_value,
                           pooled_capital, pooled_r2
  out/iy.csv               year, USA, DEU, JPN (per cent; gaps left empty)
  out/iy_summary.csv       one row per country: iso3, mean 1870-1913, mean 1950-2020,
                           peak, peak year
  out/house_summary.csv    one row: real house price change 1996-2006 and
                           2006-2012 (per cent), US investment share 2006 and 2010
  out/recession.csv        one row: change in US real private investment and real
                           consumption, 2007Q4-2009Q2, per cent (statsmodels macrodata)
"""

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from econdata import bls_cpi, jst, sm_dataset
from figout import write_table

ISOS = ["USA", "DEU", "JPN"]


def grunfeld():
    d = sm_dataset("grunfeld").copy()
    mean = d.groupby("firm")[["invest", "value"]].transform("mean")
    d["i_rel"] = (d.invest / mean.invest).round(3)
    d["v_rel"] = (d.value / mean.value).round(3)
    d["year"] = d.year.astype(int)
    return d[["firm", "year", "i_rel", "v_rel"]]


def grunfeld_summary():
    d = sm_dataset("grunfeld")
    g = grunfeld()
    fe = smf.ols("invest ~ value + capital + C(firm)", d).fit()
    po = smf.ols("invest ~ value + capital", d).fit()
    return pd.DataFrame(
        [
            {
                "n": len(g),
                "firms": g.firm.nunique(),
                "corr": round(np.corrcoef(g.v_rel, g.i_rel)[0, 1], 2),
                "slope": round(np.polyfit(g.v_rel, g.i_rel, 1)[0], 2),
                "fe_value": round(fe.params["value"], 3),
                "fe_capital": round(fe.params["capital"], 3),
                "fe_value_se": round(fe.bse["value"], 3),
                "fe_capital_se": round(fe.bse["capital"], 3),
                "fe_r2": round(fe.rsquared, 2),
                "pooled_value": round(po.params["value"], 3),
                "pooled_capital": round(po.params["capital"], 3),
                "pooled_r2": round(po.rsquared, 2),
            }
        ]
    )


def iy():
    j = jst(isos=ISOS, cols=["iy"])
    p = (100 * j.pivot(index="year", columns="iso3", values="iy"))[ISOS]
    return p.round(2).reset_index()


def iy_summary():
    p = iy().set_index("year")
    rows = []
    for iso in ISOS:
        s = p[iso].dropna()
        rows.append(
            {
                "iso3": iso,
                "early": round(s.loc[:1913].mean(), 1),
                "late": round(s.loc[1950:].mean(), 1),
                "peak": round(s.max(), 1),
                "peak_year": int(s.idxmax()),
            }
        )
    return pd.DataFrame(rows)


def house_summary():
    u = jst(isos=["USA"], cols=["hpnom", "iy"]).set_index("year")
    c = bls_cpi("CUUR0000SA0")
    c = c[c.period.str.match(r"M(0[1-9]|1[0-2])$")]
    cpi = c.groupby("year").value.agg(["mean", "count"])
    cpi = cpi.loc[cpi["count"] == 12, "mean"]
    real = u.hpnom / cpi
    return pd.DataFrame(
        [
            {
                "rise_96_06": round(100 * (real[2006] / real[1996] - 1), 1),
                "fall_06_12": round(100 * (real[2012] / real[2006] - 1), 1),
                "iy_2006": round(100 * u.iy[2006], 1),
                "iy_2010": round(100 * u.iy[2010], 1),
            }
        ]
    )


def recession():
    d = sm_dataset("macrodata")
    d = d.set_index(d.year + (d.quarter - 1) / 4)
    a, b = d.loc[2007.75], d.loc[2009.25]
    return pd.DataFrame(
        [
            {
                "inv": round(100 * (b.realinv / a.realinv - 1), 1),
                "cons": round(100 * (b.realcons / a.realcons - 1), 1),
            }
        ]
    )


if __name__ == "__main__":
    write_table(recession(), __file__, "recession")
    write_table(grunfeld(), __file__, "grunfeld")
    write_table(grunfeld_summary(), __file__, "grunfeld_summary")
    write_table(iy(), __file__, "iy")
    write_table(iy_summary(), __file__, "iy_summary")
    write_table(house_summary(), __file__, "house_summary")
