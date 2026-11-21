"""Fish captures of Peru (1960-2000) and of Iceland and New Zealand (1960-2022), thousand tonnes a year.

Grade 11, chapter 7 (public goods and common resources). World Bank WDI ER.FSH.CAPT.MT (capture fisheries production,
metric tons). Cited: the years New Zealand (1986) and Iceland (1990) made fishing quotas transferable (src/itq_dates.csv).
Writes:
  out/peru.csv       year, kt
  out/peru_key.csv   year, kt  (1970, 1972, 1973, 1974, 1994)
  out/itq.csv        year, ISL, NZL  (thousand tonnes)
  out/itq_key.csv    year, ISL, NZL  (1980, 1985, 1986, 1990, 2000, 2010, 2020)
  out/itq_dates.csv  event, year, top
"""
import pandas as pd

from cited import load_cited
from econdata import wdi
from figout import write_table

CODE = "ER.FSH.CAPT.MT"


def peru():
    d = wdi(CODE, isos=["PER"])
    d = d[(d.year >= 1960) & (d.year <= 2000)].sort_values("year")
    return pd.DataFrame({"year": d.year.values, "kt": (d.value / 1000).round(0).astype(int).values})


def itq():
    d = wdi(CODE, isos=["ISL", "NZL"])
    x = d.pivot_table(index="year", columns="iso3", values="value").loc[1960:2022] / 1000
    return x.round(0).astype(int).reset_index()[["year", "ISL", "NZL"]]


if __name__ == "__main__":
    p = peru()
    write_table(p, __file__, "peru")
    write_table(p[p.year.isin([1970, 1972, 1973, 1974, 1994])], __file__, "peru_key")
    i = itq()
    write_table(i, __file__, "itq")
    write_table(i[i.year.isin([1980, 1985, 1986, 1990, 2000, 2010, 2020])], __file__, "itq_key")
    a = load_cited(__file__, "itq_dates").drop(columns="ledger")
    a["top"] = 2500
    write_table(a, __file__, "itq_dates")
