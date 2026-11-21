"""Charts of b1 ch. 14.

rent_yield: JST housing rental yield (per cent) and the real long-term rate, France,
United Kingdom, United States, 1950-2020. Real rate = ltrate minus CPI inflation averaged
over the current and two previous years. rent_points: 1950, 1980, 2000, 2020; and the
correlation of yield and real rate by country.
seasonal: BLS U.S. city-average retail prices, 2000-2019: the average log deviation (per
cent) of each calendar month's price from its year's mean, for strawberries (perishable),
white potatoes (stored through the crop year) and long-grain rice (stored for years).
"""
import numpy as np
import pandas as pd
from econdata import bls_ap, jst
from figout import write_table

d = jst(["FRA", "GBR", "USA"], 1945, 2020, ["housing_rent_yd", "ltrate", "cpi"])
d = d.sort_values(["iso3", "year"])
d["infl"] = 100 * d.groupby("iso3").cpi.pct_change()
d["infl3"] = d.groupby("iso3").infl.transform(lambda s: s.rolling(3).mean())
d["yield"] = 100 * d.housing_rent_yd
d["real"] = d.ltrate - d.infl3
d = d[d.year >= 1950]
w = d.pivot(index="year", columns="iso3", values=["yield", "real"]).round(2)
w.columns = [f"{v}_{i.lower()}" for v, i in w.columns]
write_table(w.reset_index(), __file__, "rent_yield")
pts = d[d.year.isin([1950, 1980, 2000, 2020])][["iso3", "year", "yield", "real"]].round(2)
write_table(pts, __file__, "rent_points")
corr = [{"iso3": i, "corr": round(g["yield"].corr(g["real"]), 2)} for i, g in d.groupby("iso3")]
write_table(pd.DataFrame(corr), __file__, "rent_corr")

rows = {}
for pat, tag in [("Strawberries", "strawberries"), ("Potatoes, white, per lb", "potatoes"),
                 ("Rice, white, long grain, uncooked", "rice")]:
    b = bls_ap(pat)
    b = b[b.year.between(2000, 2019)].copy()
    b["lv"] = np.log(b.value)
    b["dev"] = 100 * (b.lv - b.groupby("year").lv.transform("mean"))
    rows[tag] = b.groupby("month").dev.mean().round(2)
s = pd.DataFrame(rows).rename_axis("month").reset_index()
write_table(s, __file__, "seasonal")
rng = pd.DataFrame([{"item": c, "range": round(s[c].max() - s[c].min(), 1),
                     "low_month": int(s.month[s[c].idxmin()]), "high_month": int(s.month[s[c].idxmax()])}
                    for c in ["strawberries", "potatoes", "rice"]])
write_table(rng, __file__, "seasonal_range")
