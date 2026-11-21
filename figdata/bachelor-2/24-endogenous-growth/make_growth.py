"""Ideas and growth, chapter 24.

Opening chart, left: average annual growth of US total factor productivity by decade,
1954-2023 (PWT rtfpna, log points per year, decades ending 1963, 1973, ..., 2023).
Right: researchers in R&D per million people, 1996 to the last year, USA, DEU, JPN,
KOR, CHN (WDI SP.POP.SCIE.RD.P6).
Writes
  out/tfp.csv            pos, label, growth (per cent a year)
  out/researchers.csv    year, USA, DEU, JPN, KOR, CHN
  out/res_summary.csv    one row per country: iso3, 1996, last value, last year, ratio
"""

import numpy as np
import pandas as pd
from econdata import pwt, wdi
from figout import write_table

ENDS = [1954, 1963, 1973, 1983, 1993, 2003, 2013, 2023]
ISOS = ["USA", "DEU", "JPN", "KOR", "CHN"]


def tfp():
    t = pwt(isos=["USA"]).set_index("year").rtfpna
    rows = []
    for i, (a, b) in enumerate(zip(ENDS[:-1], ENDS[1:])):
        g = 100 * (np.log(t[b]) - np.log(t[a])) / (b - a)
        rows.append(
            {"pos": i + 1, "label": f"{a}--{str(b)[2:]}", "growth": round(g, 2)}
        )
    return pd.DataFrame(rows)


def researchers():
    w = wdi("SP.POP.SCIE.RD.P6", isos=ISOS, since=1996)
    return (
        w.pivot(index="year", columns="iso3", values="value")[ISOS]
        .round(0)
        .reset_index()
    )


def res_summary():
    p = researchers().set_index("year")
    rows = []
    for c in ISOS:
        s = p[c].dropna()
        rows.append(
            {
                "iso3": c,
                "y1996": int(s[1996]),
                "last": int(s.iloc[-1]),
                "last_year": int(s.index[-1]),
                "ratio": round(s.iloc[-1] / s[1996], 2),
            }
        )
    return pd.DataFrame(rows)


if __name__ == "__main__":
    write_table(tfp(), __file__, "tfp")
    write_table(researchers(), __file__, "researchers")
    write_table(res_summary(), __file__, "res_summary")
