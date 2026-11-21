"""Charts of b1 ch. 19.

labsh: PWT labour share (labsh), France, Germany, Japan, United Kingdom, United States,
1950-2023. PWT fills the years before a country's first observation with that first value;
those back-filled years are dropped (the first real year is the last year of the opening
flat run: Germany 1980, Japan and the United Kingdom 1970), and so are the years after the
last one filled forward (Japan 2023). Points in each country's first and last real years,
1980 and 2000; the trend 1980-2023 (least-squares slope, points per decade).
us_invest: JST, United States, 1950-2020: investment as a share of GDP (iy, per cent) and
the real long rate (ltrate minus CPI inflation averaged over three years).
"""
import numpy as np
import pandas as pd
from econdata import jst, pwt
from figout import write_table

isos = ["FRA", "DEU", "JPN", "GBR", "USA"]


def drop_backfill(df, col):
    """Drop, country by country, the years PWT filled with a neighbouring
    observation's value: the opening run of identical values except its last
    year, and the closing run except its first year."""
    keep = []
    for _, g in df.dropna(subset=[col]).sort_values("year").groupby("iso3"):
        v = g[col].to_numpy()
        k = 0
        while k + 1 < len(v) and v[k + 1] == v[0]:
            k += 1
        m = len(v) - 1
        while m > k and v[m - 1] == v[-1]:
            m -= 1
        keep.append(g.iloc[k : m + 1])
    return pd.concat(keep)


p = drop_backfill(pwt(isos, 1950, 2023, ["labsh"]), "labsh")
first = p.groupby("iso3").year.agg(first="min", last="max").reset_index()
w = p.pivot(index="year", columns="iso3", values="labsh").round(3)
w.columns = [c.lower() for c in w.columns]
write_table(w.reset_index(), __file__, "labsh")
p = p.merge(first, on="iso3")
pts = p[(p.year == p["first"]) | (p.year == p["last"]) | p.year.isin([1980, 2000])][["iso3", "year", "labsh"]].round(3)
write_table(pts, __file__, "labsh_points")
tr = []
for i, g in p[p.year >= 1980].groupby("iso3"):
    tr.append({"iso3": i, "per_decade": round(10 * 100 * np.polyfit(g.year, g.labsh, 1)[0], 2)})
write_table(pd.DataFrame(tr), __file__, "labsh_trend")

j = jst(["USA"], 1947, 2020, ["iy", "ltrate", "cpi"]).sort_values("year")
j["infl"] = 100 * j.cpi.pct_change()
j["real"] = j.ltrate - j.infl.rolling(3).mean()
j["inv"] = 100 * j.iy
j = j[j.year >= 1950][["year", "inv", "real"]].round(2)
write_table(j, __file__, "us_invest")
write_table(pd.DataFrame([{"n": len(j), "corr": round(j.inv.corr(j.real), 2),
                           "inv_min": j.inv.min(), "inv_max": j.inv.max()}]), __file__, "us_invest_stats")
