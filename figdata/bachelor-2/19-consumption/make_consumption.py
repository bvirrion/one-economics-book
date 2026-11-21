"""Consumption against income, chapter 19.

Opening chart: quarterly growth of real personal consumption and of real disposable
income in the United States, 1959Q2-2009Q3, per cent (statsmodels macrodata, public
domain). Chart 2: household final consumption expenditure as a share of GDP, per
cent, United States, Japan, Korea and Germany, 1970 to the last WDI year
(NE.CON.PRVT.ZS); Germany from 1991 only, since earlier values are not data for the
Germany of the time (unified-territory estimates or the former Federal Republic).
Writes
  out/growth.csv         t (year + (quarter - 1) / 4), dc, dy
  out/growth_summary.csv one row: n, sd_dc, sd_dy, corr, mean_dc, mean_dy
  out/share.csv          year, USA, JPN, KOR, DEU
  out/share_summary.csv  one row per country: iso3, first (1970), last value, last year,
                         first_year, and gdp_ratio: GDP per person (NY.GDP.PCAP.KD,
                         constant dollars) in the last year over the first year
"""

import numpy as np
import pandas as pd
from econdata import sm_dataset, wdi
from figout import write_table

ISOS = ["USA", "JPN", "KOR", "DEU"]
START = {"USA": 1970, "JPN": 1970, "KOR": 1970, "DEU": 1991}


def growth():
    d = sm_dataset("macrodata")
    t = d.year + (d.quarter - 1) / 4
    out = pd.DataFrame(
        {
            "t": t,
            "dc": 100 * np.log(d.realcons).diff(),
            "dy": 100 * np.log(d.realdpi).diff(),
        }
    ).dropna()
    return out.round(3)


def growth_summary():
    g = growth()
    return pd.DataFrame(
        [
            {
                "n": len(g),
                "sd_dc": round(g.dc.std(), 2),
                "sd_dy": round(g.dy.std(), 2),
                "corr": round(g.dc.corr(g.dy), 2),
                "mean_dc": round(g.dc.mean(), 2),
                "mean_dy": round(g.dy.mean(), 2),
            }
        ]
    )


def share():
    w = wdi("NE.CON.PRVT.ZS", isos=ISOS, since=1970)
    p = w.pivot(index="year", columns="iso3", values="value")[ISOS]
    p.loc[p.index < START["DEU"], "DEU"] = np.nan
    return p.reset_index().round(2)


def share_summary():
    w = wdi("NE.CON.PRVT.ZS", isos=ISOS, since=1970).dropna(subset=["value"])
    rows = []
    for iso in ISOS:
        s = w[(w.iso3 == iso) & (w.year >= START[iso])].sort_values("year")
        g = wdi("NY.GDP.PCAP.KD", isos=[iso], since=1970).dropna(subset=["value"])
        g = g.set_index("year").value
        last = int(s.year.iloc[-1])
        rows.append(
            {
                "iso3": iso,
                "first": round(s.value.iloc[0], 1),
                "last": round(s.value.iloc[-1], 1),
                "last_year": last,
                "first_year": START[iso],
                "gdp_ratio": round(g[min(last, g.index.max())] / g[START[iso]], 1),
            }
        )
    return pd.DataFrame(rows)


if __name__ == "__main__":
    write_table(growth(), __file__, "growth")
    write_table(growth_summary(), __file__, "growth_summary")
    write_table(share(), __file__, "share")
    write_table(share_summary(), __file__, "share_summary")
