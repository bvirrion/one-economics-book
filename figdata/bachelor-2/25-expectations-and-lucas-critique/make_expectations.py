"""Expectations, credibility and central banks, chapter 25.

Opening chart: average inflation 1955-1988 (JST cpi, annual per cent change, mean of
1955-1988) against the Alesina-Summers (1993, Table A1) index of central-bank
independence, for the 15 of their 16 countries that JST covers (New Zealand is not in
JST). The United States uses the BLS CPI-U (annual average of monthly values) instead of
JST, whose US CPI differs in 1980 (11.2 against BLS 13.5). The index values are ledger
rows b2:as1993-cbi-*.
Chart 2: US inflation against unemployment, annual means of the quarterly macrodata
(statsmodels), 1960-2008, coloured by decade (2009 has three quarters only).
Chart 3: median CPI inflation (WDI FP.CPI.TOTL.ZG) in the years around the adoption of
an inflation target, for the 27 inflation targeters of the Bank of England's 2012
handbook (adoption years are ledger rows b2:it-adopt-*); event years -5 to +10.
Writes
  out/cbi.csv          iso3, index, infl (JST), infl_as (the paper's own average)
  out/cbi_lab.csv      iso3, index, infl for the points labelled one by one (the others
                       share an index value and are labelled as a group in the chart)
  out/cbi_fit.csv      one row: slope, intercept, corr, n
  out/phillips.csv     year, infl, unemp, decade
  out/phillips_dec.csv decade, infl, unemp (decade means)
  out/it_event.csv     k, median, n
  out/it_summary.csv   one row: median at k=-5, -1, 0, +5, +10
"""

import numpy as np
import pandas as pd
from econdata import bls_cpi, jst, sm_dataset, wdi
from figout import write_table

# Alesina and Summers (1993), Table A1: independence index, average inflation 1955-88.
AS1993 = {
    "ESP": (1.5, 8.5),
    "AUS": (2.0, 6.4),
    "ITA": (1.75, 7.3),
    "GBR": (2.0, 6.7),
    "FRA": (2.0, 6.1),
    "DNK": (2.5, 6.5),
    "BEL": (2.0, 4.1),
    "NOR": (2.0, 6.1),
    "SWE": (2.0, 6.1),
    "CAN": (2.5, 4.5),
    "NLD": (2.5, 4.2),
    "JPN": (2.5, 4.9),
    "USA": (3.5, 4.1),
    "DEU": (4.0, 3.0),
    "CHE": (4.0, 3.2),
}

# Bank of England, State of the art of inflation targeting (2012): year of formal
# adoption (Israel: fully fledged 1997; Ghana: formal 2007; Serbia: formal 2009;
# Sweden: announced 1993).
ADOPT = {
    "ARM": 2006, "AUS": 1993, "BRA": 1999, "CAN": 1991, "CHL": 1999, "COL": 1999,
    "CZE": 1997, "GHA": 2007, "GTM": 2005, "HUN": 2001, "ISL": 2001, "IDN": 2005,
    "ISR": 1997, "MEX": 2001, "NZL": 1989, "NOR": 2001, "PER": 2002, "PHL": 2002,
    "POL": 1998, "ROU": 2005, "SRB": 2009, "ZAF": 2000, "KOR": 1998, "SWE": 1993,
    "THA": 2000, "TUR": 2006, "GBR": 1992,
}  # fmt: skip


def cbi():
    j = jst(isos=list(AS1993), since=1954, until=1988, cols=["cpi"])
    j = j.sort_values(["iso3", "year"])
    j["infl"] = 100 * j.groupby("iso3").cpi.pct_change()
    m = j[j.year >= 1955].groupby("iso3").infl.mean()
    b = bls_cpi()
    b = b[b.period.str.match(r"M(0[1-9]|1[0-2])")].groupby("year").value.mean()
    m["USA"] = (100 * b.pct_change()).loc[1955:1988].mean()
    rows = [
        {"iso3": c, "index": v[0], "infl": round(m[c], 2), "infl_as": v[1]}
        for c, v in AS1993.items()
    ]
    return pd.DataFrame(rows)


GROUPED = ["AUS", "FRA", "GBR", "NOR", "SWE", "CAN", "JPN", "CHE", "DEU"]


def cbi_lab():
    d = cbi()
    return d[~d.iso3.isin(GROUPED)][["iso3", "index", "infl"]]


def cbi_fit():
    d = cbi()
    slope, icept = np.polyfit(d["index"], d.infl, 1)
    corr = np.corrcoef(d["index"], d.infl)[0, 1]
    return pd.DataFrame(
        [{"slope": round(slope, 2), "intercept": round(icept, 2),
          "corr": round(corr, 2), "n": len(d)}]
    )  # fmt: skip


def phillips():
    m = sm_dataset("macrodata")
    m = m[(m.year >= 1960) & (m.year <= 2008)]
    a = m.groupby("year")[["infl", "unemp"]].mean().round(2).reset_index()
    a["year"] = a.year.astype(int)
    a["decade"] = (a.year // 10) * 10
    return a


def phillips_dec():
    a = phillips()
    return a.groupby("decade")[["infl", "unemp"]].mean().round(2).reset_index()


def it_event():
    w = wdi("FP.CPI.TOTL.ZG", isos=list(ADOPT))
    w = w.dropna(subset=["value"])
    w["k"] = w.year - w.iso3.map(ADOPT)
    w = w[(w.k >= -5) & (w.k <= 10)]
    g = w.groupby("k").value
    return pd.DataFrame(
        {"k": g.median().index, "median": g.median().round(2).values,
         "n": g.count().values}
    )  # fmt: skip


def it_summary():
    e = it_event().set_index("k")["median"]
    return pd.DataFrame([{f"k{'m' if k < 0 else 'p'}{abs(k)}": e[k] for k in
                          (-5, -1, 0, 5, 10)}])  # fmt: skip


if __name__ == "__main__":
    write_table(cbi(), __file__, "cbi")
    write_table(cbi_lab(), __file__, "cbi_lab")
    write_table(cbi_fit(), __file__, "cbi_fit")
    write_table(phillips(), __file__, "phillips")
    write_table(phillips_dec(), __file__, "phillips_dec")
    write_table(it_event(), __file__, "it_event")
    write_table(it_summary(), __file__, "it_summary")
