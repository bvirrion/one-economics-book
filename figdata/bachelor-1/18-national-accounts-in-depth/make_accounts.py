"""Charts of b1 ch. 18.

growth_gap: average yearly growth of real GDP per person 1990-2019 (log points per year,
in per cent) from WDI (NY.GDP.PCAP.KD) and from PWT (rgdpna / pop), countries in both
with both endpoints; gap = PWT - WDI.
balances_de: Germany, net lending of general government (Eurostat gov_10dd_edpt1, B9, S13,
per cent of GDP), the current account (WDI BN.CAB.XOKA.GD.ZS, per cent of GDP), and the
private sectors' net lending computed as the difference (capital account ignored).
pli: price level of household consumption (WDI PA.NUS.PRVT.PLI, US = 1) against GDP per
person at PPP (WDI NY.GDP.PCAP.PP.KD), 2021.
"""
import numpy as np
import pandas as pd
from econdata import eurostat, pwt, wdi
from figout import write_table

w = wdi("NY.GDP.PCAP.KD", since=1990, until=2019, countries_only=True)
w = w[w.year.isin([1990, 2019])].pivot(index="iso3", columns="year", values="value").dropna()
w["wdi"] = 100 * np.log(w[2019] / w[1990]) / 29
p = pwt(since=1990, until=2019, cols=["rgdpna", "pop"])
p = p[p.year.isin([1990, 2019])].dropna()
p["y"] = p.rgdpna / p["pop"]
p = p.pivot(index="iso3", columns="year", values="y").dropna()
p["pwt"] = 100 * np.log(p[2019] / p[1990]) / 29
g = w[["wdi"]].join(p[["pwt"]], how="inner").dropna().reset_index()
g["gap"] = g.pwt - g.wdi
g = g.round(3)
write_table(g, __file__, "growth_gap")
big = g.reindex(g.gap.abs().sort_values(ascending=False).index).head(5)
write_table(big, __file__, "growth_gap_largest")
st = pd.DataFrame([{"n": len(g), "median_abs_gap": round(g.gap.abs().median(), 2),
                    "share_over_half": round(100 * (g.gap.abs() > 0.5).mean(), 1),
                    "share_over_one": round(100 * (g.gap.abs() > 1).mean(), 1),
                    "corr": round(g.wdi.corr(g.pwt), 3)}])
write_table(st, __file__, "growth_gap_stats")

e = eurostat("gov_10dd_edpt1")
e = e[(e.geo == "DE") & (e.unit == "PC_GDP") & (e.sector == "S13") & (e.na_item == "B9")]
e = e[e.time.between(1999, 2023)][["time", "value"]].rename(columns={"time": "year", "value": "gov"})
ca = wdi("BN.CAB.XOKA.GD.ZS", ["DEU"], 1999, 2023)[["year", "value"]].rename(columns={"value": "ca"})
b = e.merge(ca, on="year")
b["private"] = b.ca - b.gov
b["row"] = -b.ca
write_table(b.round(2), __file__, "balances_de")

pl = wdi("PA.NUS.PRVT.PLI", since=2021, until=2021, countries_only=True)
gd = wdi("NY.GDP.PCAP.PP.KD", since=2021, until=2021, countries_only=True)
m = pl[["iso3", "country", "value"]].merge(gd[["iso3", "value"]], on="iso3", suffixes=("_pli", "_gdp")).dropna()
m = m.rename(columns={"value_pli": "pli", "value_gdp": "gdp"})
m["country"] = m.country.str.replace(",", "", regex=False)
m = m.round({"pli": 3, "gdp": 0})
write_table(m, __file__, "pli_2021")
fit = np.polyfit(np.log10(m.gdp), m.pli, 1)
write_table(pd.DataFrame({"gdp": [800, 150000], "fit": (fit[1] + fit[0] * np.log10([800, 150000])).round(3)}),
            __file__, "pli_fit")
write_table(m[m.iso3.isin(["IND", "CHE", "USA", "NOR", "CHN"])], __file__, "pli_points")
write_table(pd.DataFrame([{"n": len(m), "corr_log": round(np.corrcoef(np.log10(m.gdp), m.pli)[0, 1], 2),
                           "slope_per_decade": round(fit[0], 3)}]), __file__, "pli_stats")
