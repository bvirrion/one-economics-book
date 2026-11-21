"""Relative yields and relative areas, wheat against maize, across countries: the
average of 2020--2022 of FAOSTAT's yield (kg/ha) and area harvested (ha). Countries
with at least 10,000 ha of each crop in every one of the three years; aggregates and
China (total) dropped. x = ln(wheat yield / maize yield), y = ln(wheat area / maize
area); an OLS line. These are actual yields, not the potential yields of the published
test. Writes out/crops.csv, out/crops_fit.csv (x, y on the line), out/crops_stats.csv."""
import numpy as np
import pandas as pd
from econdata import faostat_crops
from figout import write_table

AGG = {"001", "002", "005", "009", "011", "013", "014", "015", "017", "018", "019", "021",
       "029", "030", "034", "035", "039", "053", "054", "057", "061", "097", "142", "143",
       "145", "150", "151", "154", "155", "159", "199", "432", "722", "901", "902"}
YEARS = [2020, 2021, 2022]


def panel():
    parts = []
    for crop, tag in [("Wheat", "w"), ("Maize (corn)", "m")]:
        for el, e in [("Yield", "yield"), ("Area harvested", "area")]:
            d = faostat_crops(crop, el)
            d = d[d.Year.isin(YEARS) & ~d.m49.isin(AGG)]
            parts.append(d.pivot_table(index="Area", columns="Year", values="Value")
                         .rename(columns=lambda y, c=f"{e}_{tag}": f"{c}_{y}"))
    p = pd.concat(parts, axis=1).dropna()
    area_ok = np.ones(len(p), bool)
    for y in YEARS:
        area_ok &= (p[f"area_w_{y}"] >= 10_000) & (p[f"area_m_{y}"] >= 10_000)
    p = p[area_ok]
    out = pd.DataFrame(index=p.index)
    for v in ["yield_w", "yield_m", "area_w", "area_m"]:
        out[v] = p[[f"{v}_{y}" for y in YEARS]].mean(axis=1)
    out["x"] = np.log(out.yield_w / out.yield_m)
    out["y"] = np.log(out.area_w / out.area_m)
    return out.reset_index()


def tables():
    d = panel()
    b, a = np.polyfit(d.x, d.y, 1)
    xs = np.array([d.x.min(), d.x.max()])
    fit = pd.DataFrame({"x": xs, "y": a + b * xs})
    stats = pd.DataFrame({"stat": ["countries", "slope", "intercept", "corr"],
                          "value": [len(d), b, a, np.corrcoef(d.x, d.y)[0, 1]]})
    return d[["Area", "x", "y"]].rename(columns={"Area": "country"}), fit, stats


if __name__ == "__main__":
    d, fit, stats = tables()
    d["country"] = d.country.str.replace(",", "", regex=False)
    write_table(d, __file__, "crops")
    write_table(fit, __file__, "crops_fit")
    write_table(stats, __file__, "crops_stats")
