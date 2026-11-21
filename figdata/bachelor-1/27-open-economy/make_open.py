"""Charts of b1 ch. 27.

pegs: short-term interest rate (JST R6 stir) minus Germany's, 1979-1998, for seven countries
JST codes as pegged to the Deutsche Mark (peg == 1, peg_base == DEU) in most of those years.
peg_stats: years pegged and mean gap in the pegged years, by country.
fh: saving (NY.GNS.ICTR.ZS) and investment (NE.GDI.TOTL.ZS), per cent of GDP, mean
2000-2019, high-income countries with all 20 years of both; least-squares slope of
investment on saving; fh21_stats: the same for the 21 OECD countries of Feldstein and
Horioka's Table 1.
"""
import numpy as np
import pandas as pd
from econdata import jst, wdi, wdi_countries
from figout import write_table

C = ["NLD", "BEL", "DNK", "FRA", "ITA", "ESP", "SWE"]
d = jst(C + ["DEU"], 1979, 1998, ["stir", "peg", "peg_base"])
s = d.pivot(index="year", columns="iso3", values="stir")
gap = s[C].sub(s.DEU, axis=0).round(2).reset_index()
write_table(gap, __file__, "pegs")
rows = []
for c in C:
    x = d[d.iso3 == c].set_index("year")
    on = x[(x.peg == 1) & (x.peg_base == "DEU")].index
    g = gap.set_index("year").loc[on, c]
    rows.append({"iso3": c, "years": len(on), "first": int(on.min()), "last": int(on.max()),
                 "mean_gap": round(g.mean(), 2), "max_gap": round(g.max(), 2)})
write_table(pd.DataFrame(rows), __file__, "peg_stats")

hi = wdi_countries()
hi = set(hi[hi["Income Group"] == "High income"]["Country Code"])
sv = wdi("NY.GNS.ICTR.ZS", since=2000, until=2019, countries_only=True)
iv = wdi("NE.GDI.TOTL.ZS", since=2000, until=2019, countries_only=True)
m = sv.merge(iv, on=["iso3", "country", "year"], suffixes=("_s", "_i")).dropna()
m = m[m.iso3.isin(hi)]
full = m.groupby("iso3").year.count()
m = m[m.iso3.isin(full[full == 20].index)]
a = m.groupby(["iso3", "country"])[["value_s", "value_i"]].mean().round(2).reset_index()
a = a.rename(columns={"value_s": "saving", "value_i": "invest"})
a = a.drop(columns="country")  # names such as "Bahamas, The" hold commas
write_table(a, __file__, "fh")
b, c0 = np.polyfit(a.saving, a.invest, 1)
xs = np.array([a.saving.min(), a.saving.max()]).round(1)
write_table(pd.DataFrame({"s": xs, "fit": (c0 + b * xs).round(3)}), __file__, "fh_fit")
write_table(pd.DataFrame([{"n": len(a), "slope": round(b, 3), "corr": round(a.saving.corr(a.invest), 3)}]),
            __file__, "fh_stats")
FH21 = ["AUS", "AUT", "BEL", "CAN", "DNK", "FIN", "FRA", "DEU", "GRC", "IRL", "ITA", "JPN", "LUX",
        "NLD", "NZL", "NOR", "ESP", "SWE", "CHE", "GBR", "USA"]
f = a[a.iso3.isin(FH21)]
b21 = np.polyfit(f.saving, f.invest, 1)[0]
write_table(pd.DataFrame([{"n": len(f), "slope": round(b21, 3), "corr": round(f.saving.corr(f.invest), 3)}]),
            __file__, "fh21_stats")
lab = ["NOR", "SGP", "CHE", "USA", "GBR", "JPN"]
write_table(a[a.iso3.isin(lab)], __file__, "fh_labels")
