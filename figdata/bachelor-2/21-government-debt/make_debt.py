"""Government debt, chapter 21.

Opening chart: general government debt as a share of GDP, per cent, 1870-2020, United
Kingdom, United States, France, Japan and Italy (JST Macrohistory, debtgdp).
Chart 2: the offset test across countries: change in gross national saving (per cent of
GNI, NY.GNS.ICTR.ZS) against change in general government net lending (per cent of
GDP, GC.NLD.TOTL.GD.ZS), averages 2010-2017 minus averages 2000-2007, countries with at
least 3 years in each window for both series (WDI).
Record: the United Kingdom, 1946-1975 (JST: debtgdp, gdp, cpi, ltrate, rgdpmad).
Writes
  out/debt.csv            year, GBR, USA, FRA, JPN, ITA (per cent)
  out/debt_summary.csv    one row per country: iso3, value in 1913, peak, peak year,
                          value in 2020
  out/offset.csv          iso3, dn, ds (percentage points)
  out/offset_summary.csv  one row: n, slope, se, intercept, corr
  out/uk_summary.csv      one row: debt 1946 and 1975, average nominal GDP growth,
                          inflation, real growth (per cent a year, 1946-1975), mean
                          long-term rate 1947-1975
"""

import numpy as np
import pandas as pd
from econdata import jst, wdi
from figout import write_table

ISOS = ["GBR", "USA", "FRA", "JPN", "ITA"]
WINDOWS = ((2000, 2007), (2010, 2017))


def debt():
    j = jst(isos=ISOS, cols=["debtgdp"])
    p = 100 * j.pivot(index="year", columns="iso3", values="debtgdp")[ISOS]
    return p.round(1).reset_index()


def debt_summary():
    p = debt().set_index("year")
    rows = []
    for iso in ISOS:
        s = p[iso].dropna()
        rows.append(
            {
                "iso3": iso,
                "y1913": round(s[1913], 0),
                "peak": round(s.max(), 0),
                "peak_year": int(s.idxmax()),
                "y2020": round(s[2020], 0),
            }
        )
    return pd.DataFrame(rows)


def _window_means(code):
    w = wdi(code, countries_only=True, since=2000, until=2017)
    w = w.dropna(subset=["value"])
    out = {}
    for k, (a, b) in enumerate(WINDOWS):
        x = w[(w.year >= a) & (w.year <= b)].groupby("iso3").value
        out[f"m{k}"], out[f"c{k}"] = x.mean(), x.count()
    return pd.concat(out, axis=1)


def offset():
    s, n = _window_means("NY.GNS.ICTR.ZS"), _window_means("GC.NLD.TOTL.GD.ZS")
    d = pd.concat({"s": s, "n": n}, axis=1).dropna()
    counts = d[[(v, c) for v in ("s", "n") for c in ("c0", "c1")]]
    d = d[counts.min(axis=1) >= 3]
    out = pd.DataFrame(
        {
            "iso3": d.index,
            "dn": (d[("n", "m1")] - d[("n", "m0")]).round(2).values,
            "ds": (d[("s", "m1")] - d[("s", "m0")]).round(2).values,
        }
    )
    return out


def offset_summary():
    o = offset()
    x, y = o.dn.to_numpy(), o.ds.to_numpy()
    b, a = np.polyfit(x, y, 1)
    resid = y - a - b * x
    se = np.sqrt(resid @ resid / (len(x) - 2) / ((x - x.mean()) @ (x - x.mean())))
    return pd.DataFrame(
        [
            {
                "n": len(o),
                "slope": round(b, 2),
                "se": round(se, 2),
                "intercept": round(a, 2),
                "corr": round(np.corrcoef(x, y)[0, 1], 2),
            }
        ]
    )


def uk_summary():
    j = jst(isos=["GBR"], cols=["debtgdp", "gdp", "cpi", "ltrate", "rgdpmad", "pop"])
    j = j.set_index("year")
    j["rgdp"] = j.rgdpmad * j["pop"]  # real GDP per person times population
    j["deflator"] = j.gdp / j.rgdp  # implied GDP deflator (any base)
    a, b = 1946, 1975

    def rate(c):
        return round(100 * ((j[c][b] / j[c][a]) ** (1 / (b - a)) - 1), 1)

    return pd.DataFrame(
        [
            {
                "debt1946": round(100 * j.debtgdp[a], 0),
                "debt1975": round(100 * j.debtgdp[b], 0),
                "nominal": rate("gdp"),
                "inflation": rate("cpi"),
                "real": rate("rgdpmad"),
                "pop": rate("pop"),
                "real_total": rate("rgdp"),
                "deflator": rate("deflator"),
                "ltrate": round(j.ltrate.loc[a + 1 : b].mean(), 1),
            }
        ]
    )


if __name__ == "__main__":
    write_table(debt(), __file__, "debt")
    write_table(debt_summary(), __file__, "debt_summary")
    write_table(offset(), __file__, "offset")
    write_table(offset_summary(), __file__, "offset_summary")
    write_table(uk_summary(), __file__, "uk_summary")
