"""Earnings and unemployment by education (US, 2025, cited) and unemployment by education across countries (WDI).

Grade 11, chapter 10 (the labour market).
Cited (src/edpays.csv): BLS Employment Projections Table 5.1, 2025: median usual weekly earnings (full-time wage and
salary workers) and unemployment rate, persons 25 and over, by highest attainment.
WDI: SL.UEM.BASC.ZS, SL.UEM.INTM.ZS, SL.UEM.ADVN.ZS (unemployment, % of the labour force with basic, intermediate,
advanced education), 2024, eight countries.
Writes:
  out/edpays.csv   y, level, earnings, unemp
  out/uneduc.csv   x, iso3, basic, intermediate, advanced
"""
import pandas as pd

from cited import load_cited
from econdata import wdi
from figout import write_table

ISOS = ["USA", "GBR", "DEU", "FRA", "ESP", "ZAF", "MEX", "IND"]
CODES = {"basic": "SL.UEM.BASC.ZS", "intermediate": "SL.UEM.INTM.ZS", "advanced": "SL.UEM.ADVN.ZS"}


def edpays():
    d = load_cited(__file__, "edpays").drop(columns="ledger")
    d["earnings"] = d.earnings.astype(str).str.replace(",", "").astype(int)
    d.insert(0, "y", range(len(d)))
    return d


def uneduc(year=2024):
    out = pd.DataFrame({"iso3": ISOS})
    for k, c in CODES.items():
        d = wdi(c, isos=ISOS)
        d = d[d.year == year].set_index("iso3").value.round(1)
        out[k] = out.iso3.map(d)
    out.insert(0, "x", range(len(out)))
    return out


if __name__ == "__main__":
    write_table(edpays(), __file__, "edpays")
    write_table(uneduc(), __file__, "uneduc")
