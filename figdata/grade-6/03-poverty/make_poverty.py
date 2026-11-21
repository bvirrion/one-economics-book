"""g6-03 Poverty and How It Is Counted: three World Bank charts and the Brenland problem tables.

poverty_share_world.csv  year, share   (% of world population below $3.00 a day, 2021 PPP; WDI SI.POV.DDAY, WLD)
poverty_count_world.csv  year, poor, not_poor (billions; share x SP.POP.TOTL, WLD); years with a share only
poverty_by_region.csv    year + seven columns (% below $3.00 a day; World Bank regions and the world; blank = no estimate)
lines_2024.csv           line, share   (% of world population below $3.00, $4.20, $8.30 a day, 2024)
ssa_count.csv            year, ssa_poor, world_poor, ssa_share_of_poor (1990 and 2024)
brenland_basket.csv      good, qty, price, cost (a basket of needs for one person for one year, 2025 prices)
brenland_bands.csv       band, households, people (2025 survey, disposable income per person)
"""
import pandas as pd

from country import load
from econdata import wdi
from figout import write_table

REG = {"EAS": "eas", "ECS": "ecs", "LCN": "lcn", "MEA": "mea", "SAS": "sas", "SSF": "ssf", "WLD": "wld"}
NEEDS = {"bread": 200, "rent": 3, "transport": 50, "clothing": 5, "energy": 1000}
BANDS = [(0, 4000), (4000, 5000), (5000, 6000), (6000, 8000), (8000, None)]


def _share(isos):
    d = wdi("SI.POV.DDAY", isos=isos, since=1981)
    return d.pivot(index="year", columns="iso3", values="value")


def world():
    s = _share(["WLD"])["WLD"].dropna().rename("share")
    pop = wdi("SP.POP.TOTL", isos="WLD").set_index("year")["value"]
    share = s.round(1).reset_index()
    share["year"] = share.year.astype(int)
    c = pd.DataFrame({"share": s, "pop": pop.reindex(s.index)})
    count = pd.DataFrame({"year": c.index.astype(int),
                          "poor": (c.share / 100 * c["pop"] / 1e9).round(3).values,
                          "not_poor": ((1 - c.share / 100) * c["pop"] / 1e9).round(3).values})
    return share, count


def regions():
    p = _share(list(REG)).rename(columns=REG)[list(REG.values())].round(1)
    p.index = p.index.astype(int)
    return p.reset_index()


def lines_2024():
    rows = []
    for line, code in (("3.00", "SI.POV.DDAY"), ("4.20", "SI.POV.LMIC"), ("8.30", "SI.POV.UMIC")):
        v = wdi(code, isos="WLD").set_index("year")["value"]
        rows.append(dict(line=line, share=round(float(v[2024]), 1)))
    return pd.DataFrame(rows)


def ssa_count():
    s = _share(["SSF", "WLD"])
    pop = wdi("SP.POP.TOTL", isos=["SSF", "WLD"]).pivot(index="year", columns="iso3", values="value")
    rows = []
    for y in (1990, 2024):
        ssa = s.loc[y, "SSF"] / 100 * pop.loc[y, "SSF"] / 1e6
        wld = s.loc[y, "WLD"] / 100 * pop.loc[y, "WLD"] / 1e6
        rows.append(dict(year=y, ssa_poor=round(ssa), world_poor=round(wld), ssa_share_of_poor=round(100 * ssa / wld, 1)))
    return pd.DataFrame(rows)


def brenland():
    b = load("basket")
    b = b[b.year == 2025].set_index("good")
    basket = pd.DataFrame({"good": list(NEEDS), "qty": list(NEEDS.values()),
                           "price": [b.loc[g, "price"] for g in NEEDS]})
    basket["cost"] = (basket.qty * basket.price).round(2)
    h = load("households")
    pp = h.disposable / h["size"]
    rows = []
    for lo, hi in BANDS:
        m = (pp >= lo) & (pp < hi) if hi else (pp >= lo)
        rows.append(dict(band=f"{lo}-{hi}" if hi else f"{lo}+", households=int(m.sum()), people=int(h["size"][m].sum())))
    return basket, pd.DataFrame(rows)


if __name__ == "__main__":
    share, count = world()
    write_table(share, __file__, "poverty_share_world")
    write_table(count, __file__, "poverty_count_world")
    write_table(regions(), __file__, "poverty_by_region")
    write_table(ssa_count(), __file__, "ssa_count")
    write_table(lines_2024(), __file__, "lines_2024")
    basket, bands = brenland()
    write_table(basket, __file__, "brenland_basket")
    write_table(bands, __file__, "brenland_bands")
