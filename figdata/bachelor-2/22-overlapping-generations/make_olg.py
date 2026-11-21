"""Overlapping generations, chapter 22.

Opening chart: people aged 65 and over per 100 people aged 15-64, 1960-2025, Japan,
Italy, Korea, United States, Nigeria and the world (WDI SP.POP.DPND.OL).
Chart 2: the dynamic-efficiency test across countries, 2019: capital income (one minus
the labour share, Penn World Table labsh, a share of GDP at current national prices)
against gross capital formation as a share of GDP at current national prices (WDI
NE.GDI.TOTL.ZS), so that both flows use the same prices. Countries in both sources.
Writes
  out/oadr.csv          year, JPN, ITA, KOR, USA, NGA, WLD
  out/oadr_summary.csv  one row per series: iso3, 1960, 2025
  out/efficiency.csv    iso3, cap, inv (per cent of GDP)
  out/eff_summary.csv   one row: n, n_above (capital income above investment),
                        below (the iso3 codes below), median cap, median inv, and
                        cap and inv for CHN and USA
"""

import pandas as pd
from econdata import pwt, wdi
from figout import write_table

ISOS = ["JPN", "ITA", "KOR", "USA", "NGA", "WLD"]


def oadr():
    w = wdi("SP.POP.DPND.OL", isos=ISOS, since=1960, until=2025)
    return (
        w.pivot(index="year", columns="iso3", values="value")[ISOS]
        .round(2)
        .reset_index()
    )


def oadr_summary():
    p = oadr().set_index("year")
    return pd.DataFrame(
        [
            {"iso3": c, "y1960": round(p[c][1960], 1), "y2025": round(p[c][2025], 1)}
            for c in ISOS
        ]
    )


def efficiency():
    p = pwt(since=2019, until=2019).dropna(subset=["labsh"])
    w = wdi("NE.GDI.TOTL.ZS", since=2019, until=2019).dropna(subset=["value"])
    m = p.merge(w[["iso3", "value"]], on="iso3")
    return pd.DataFrame(
        {
            "iso3": m.iso3.values,
            "cap": (100 * (1 - m.labsh)).round(1).values,
            "inv": m.value.round(1).values,
        }
    )


def eff_summary():
    e = efficiency()
    below = e[e.cap <= e.inv]
    s = e.set_index("iso3")
    return pd.DataFrame(
        [
            {
                "n": len(e),
                "n_above": int((e.cap > e.inv).sum()),
                "below": " ".join(sorted(below.iso3)),
                "median_cap": round(e.cap.median(), 1),
                "median_inv": round(e.inv.median(), 1),
                "chn_cap": s.cap["CHN"],
                "chn_inv": s.inv["CHN"],
                "usa_cap": s.cap["USA"],
                "usa_inv": s.inv["USA"],
            }
        ]
    )


if __name__ == "__main__":
    write_table(oadr(), __file__, "oadr")
    write_table(oadr_summary(), __file__, "oadr_summary")
    write_table(efficiency(), __file__, "efficiency")
    write_table(eff_summary(), __file__, "eff_summary")
