"""Opening chart of b1 ch. 8: average annual hours per worker against real labour
compensation per hour, 1950-2023, six countries (PWT 11.0: avh; labsh * rgdpna /
(emp * avh), 2021 dollars at constant national prices). PWT fills the years before a
country's first labour-share observation with that value; those years are dropped
(Germany starts in 1980, Japan, the Netherlands and the United Kingdom in 1970). Also
the 1950, 2019 and 2023 values and each country's first year."""
import pandas as pd
from econdata import pwt
from figout import write_table

ISOS = ["FRA", "DEU", "JPN", "NLD", "GBR", "USA"]


def drop_backfill(df, col):
    """Drop, country by country, the opening run of identical values of col
    except its last year: the years PWT filled with the first observation."""
    keep = []
    for _, g in df.dropna(subset=[col]).sort_values("year").groupby("iso3"):
        v = g[col].to_numpy()
        k = 0
        while k + 1 < len(v) and v[k + 1] == v[0]:
            k += 1
        keep.append(g.iloc[k:])
    return pd.concat(keep)


raw = pwt(ISOS, 1950, 2023, ["avh", "labsh", "rgdpna", "emp"]).dropna()
d = drop_backfill(raw, "labsh")
d["wage"] = d.labsh * d.rgdpna / (d.emp * d.avh)
d = d[["iso3", "year", "avh", "wage"]].round({"avh": 0, "wage": 2})
# Points: hours in every year asked for; pay only where the labour share is observed.
allh = raw[["iso3", "year", "avh"]].round({"avh": 0}).merge(
    d[["iso3", "year", "wage"]], on=["iso3", "year"], how="left"
)
w = d.pivot(index="year", columns="iso3")
w.columns = [f"{c}_{i.lower()}" for c, i in w.columns]
write_table(w.reset_index(), __file__, "hours_paths")
pts = allh[allh.year.isin([1950, 2019, 2023])].sort_values(["iso3", "year"])
write_table(pts, __file__, "hours_points")
first = d.sort_values("year").groupby("iso3").first().reset_index()
write_table(first, __file__, "hours_first")
