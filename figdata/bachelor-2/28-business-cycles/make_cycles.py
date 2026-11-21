"""Business cycles, chapter 28.

Opening chart: standard deviation of the growth of real GDP per person over the ten
years ending in each year, 1880-2020 (JST rgdpmad, log differences, per cent), for the
USA, GBR and DEU, and the median across the 17 JST countries with data from 1870
(Ireland, from 1922, is left out).
Chart 2: HP cyclical components (smoothing 1600) of log real GDP, consumption and
investment, quarterly 1959-Q1 to 2009-Q3 (statsmodels macrodata), with NBER recessions
(peak quarter to trough quarter; ledger rows b2:nber-*).
Table: moments of the HP cycles of output, consumption, investment, government
purchases, real disposable income (log, per cent) and the unemployment rate (points).
Great Moderation: standard deviation of annual growth of real GDP (annual averages of
the quarterly series), 1960-1983 and 1984-2001 (Stock and Watson's periods), 2002-2008.
Writes
  out/vol.csv          year, USA, GBR, DEU, median
  out/vol_summary.csv  the rows of vol.csv for 1913, 1950, 1975, 2000, 2007, 2019, 2020
  out/hp.csv           t, gdp, cons, inv
  out/recessions.csv   start, end (decimal years)
  out/moments.csv      var, sd, rel, corr, ac1
  out/moderation.csv   period, sd
"""

import numpy as np
import pandas as pd
from econdata import jst, sm_dataset
from figout import write_table
from statsmodels.tsa.filters.hp_filter import hpfilter

# NBER peak and trough quarters, 1957-2009 (ledger b2:nber-dates)
NBER = [
    (1960, 2, 1961, 1), (1969, 4, 1970, 4), (1973, 4, 1975, 1), (1980, 1, 1980, 3),
    (1981, 3, 1982, 4), (1990, 3, 1991, 1), (2001, 1, 2001, 4), (2007, 4, 2009, 2),
]  # fmt: skip
SHOW = ["USA", "GBR", "DEU"]


def vol():
    j = jst(cols=["rgdpmad"]).sort_values(["iso3", "year"])
    j = j[j.iso3 != "IRL"]
    j["g"] = 100 * np.log(j.rgdpmad).groupby(j.iso3).diff()
    w = j.pivot(index="year", columns="iso3", values="g")
    sd = w.rolling(10).std()
    out = sd[SHOW].copy()
    out["median"] = sd.median(axis=1)
    return out.loc[1880:2020].round(2).reset_index()


def vol_summary():
    v = vol().set_index("year")
    return v.loc[[1913, 1950, 1975, 2000, 2007, 2019, 2020]].reset_index()


def _macro():
    m = sm_dataset("macrodata").copy()
    m["t"] = m.year + (m.quarter - 1) / 4
    return m


def hp():
    m = _macro()
    out = pd.DataFrame({"t": m.t})
    for c, name in (("realgdp", "gdp"), ("realcons", "cons"), ("realinv", "inv")):
        out[name] = 100 * hpfilter(np.log(m[c]), lamb=1600)[0]
    return out.round(3)


def recessions():
    rows = [{"start": a + (b - 1) / 4, "end": c + (d - 1) / 4} for a, b, c, d in NBER]
    return pd.DataFrame(rows)


def moments():
    m = _macro()
    cyc = {}
    for c, name in (("realgdp", "output"), ("realcons", "consumption"),
                    ("realinv", "investment"), ("realgovt", "government"),
                    ("realdpi", "income")):  # fmt: skip
        cyc[name] = 100 * hpfilter(np.log(m[c]), lamb=1600)[0]
    cyc["unemployment"] = hpfilter(m.unemp, lamb=1600)[0]
    rows = []
    for k, s in cyc.items():
        rows.append(
            {"var": k, "sd": round(s.std(), 2),
             "rel": round(s.std() / cyc["output"].std(), 2),
             "corr": round(np.corrcoef(s, cyc["output"])[0, 1], 2),
             "ac1": round(s.autocorr(1), 2)}
        )  # fmt: skip
    return pd.DataFrame(rows)


def moderation():
    m = _macro()
    a = m.groupby("year").realgdp.mean()
    g = 100 * a.pct_change()
    spans = (("1960--1983", 1960, 1983), ("1984--2001", 1984, 2001),
             ("2002--2008", 2002, 2008))  # fmt: skip
    rows = [(p, g.loc[a:b].std()) for p, a, b in spans]
    return pd.DataFrame([{"period": p, "sd": round(s, 2)} for p, s in rows])


if __name__ == "__main__":
    write_table(vol(), __file__, "vol")
    write_table(vol_summary(), __file__, "vol_summary")
    write_table(hp(), __file__, "hp")
    write_table(recessions(), __file__, "recessions")
    write_table(moments(), __file__, "moments")
    write_table(moderation(), __file__, "moderation")
