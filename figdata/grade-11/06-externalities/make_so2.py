"""Sulphur dioxide emissions per person against GDP per person, six countries, 1850-2022; US SO2 emissions 1970-2023.

Grade 11, chapter 6 (externalities). CEDS SO2 emissions by country (kt a year) divided by Maddison population (thousands),
in kg per person; Maddison GDP per person (2011 international dollars). Each country's path is plotted every fifth year
from 1850 (and 2022). Cited: the dates of the US Acid Rain Program (src/arp_dates.csv).
Writes:
  out/so2_<ISO>.csv   year, gdppc, so2pc  (ISO in USA, GBR, DEU, JPN, CHN, IND)
  out/so2_peaks.csv   iso3, peak_year, peak_so2pc, gdppc_at_peak, so2pc_2022, gdppc_2022
  out/so2_usa.csv     year, mt (million tonnes)
  out/arp_dates.csv   event, year, top (a height for the guide line)
"""
import pandas as pd

from cited import load_cited
from econdata import ceds, maddison
from figout import write_table

ISOS = ["USA", "GBR", "DEU", "JPN", "CHN", "IND"]


def paths():
    c = ceds("so2", isos=ISOS, since=1850, until=2022)[["iso3", "year", "value"]]
    m = maddison(isos=ISOS, since=1850, until=2022)[["iso3", "year", "gdppc", "pop"]]
    d = c.merge(m, on=["iso3", "year"]).dropna()
    d["so2pc"] = (d.value * 1000 / d["pop"]).round(2)
    d["gdppc"] = d.gdppc.round(0)
    out, peaks = {}, []
    for iso in ISOS:
        x = d[d.iso3 == iso].sort_values("year")
        pk = x.loc[x.so2pc.idxmax()]
        last = x[x.year == 2022].iloc[0]
        peaks.append({"iso3": iso, "peak_year": int(pk.year), "peak_so2pc": pk.so2pc, "gdppc_at_peak": pk.gdppc,
                      "so2pc_2022": last.so2pc, "gdppc_2022": last.gdppc})
        x = x[(x.year % 5 == 0) | (x.year == 2022)]
        out[iso] = x[["year", "gdppc", "so2pc"]].reset_index(drop=True)
    return out, pd.DataFrame(peaks)


def usa():
    c = ceds("so2", isos=["USA"], since=1970)[["year", "value"]]
    return pd.DataFrame({"year": c.year, "mt": (c.value / 1000).round(2)}).reset_index(drop=True)


if __name__ == "__main__":
    out, peaks = paths()
    for iso, x in out.items():
        write_table(x, __file__, f"so2_{iso}")
    write_table(peaks, __file__, "so2_peaks")
    u = usa()
    write_table(u, __file__, "so2_usa")
    a = load_cited(__file__, "arp_dates").drop(columns="ledger")
    a["top"] = 32
    write_table(a, __file__, "arp_dates")
