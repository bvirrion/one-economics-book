"""Exercise 8: the binding overhang, bound minus applied tariff (simple means, all
products; WDI TM.TAX.MRCH.BR.ZS and TM.TAX.MRCH.SM.AR.ZS), each country's latest year
from 2017 to 2021 with both, and its relation to income (WDI NY.GDP.PCAP.PP.KD, the
same year). The European Union's members share one schedule and count once."""
import numpy as np
from econdata import wdi

EU_OTHERS = ["AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "DEU",
             "GRC", "HUN", "IRL", "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "POL",
             "PRT", "ROU", "SVK", "SVN", "ESP", "SWE"]
b = wdi("TM.TAX.MRCH.BR.ZS", countries_only=True)
a = wdi("TM.TAX.MRCH.SM.AR.ZS", countries_only=True)
m = b.merge(a, on=["iso3", "country", "year"], suffixes=("_b", "_a"))
m = m[m.year.between(2017, 2021)].sort_values("year").groupby("iso3").tail(1)
m = m[~m.iso3.isin(EU_OTHERS)]
g = wdi("NY.GDP.PCAP.PP.KD", countries_only=True)[["iso3", "year", "value"]]
m = m.merge(g.rename(columns={"value": "gdp"}), on=["iso3", "year"]).dropna()
over = m.value_b - m.value_a
print(f"countries {len(m)}; median overhang {over.median():.1f} points")
double = (m.value_b >= 2 * m.value_a).mean()
print(f"share that could double the applied tariff: {double:.2f}")
r = np.corrcoef(np.log(m.gdp), over)[0, 1]
print(f"correlation of the overhang with log income per head: {r:.2f}")
poor = m.gdp < m.gdp.median()
print(f"median overhang, poorer half {over[poor].median():.1f}, "
      f"richer half {over[~poor].median():.1f}")
