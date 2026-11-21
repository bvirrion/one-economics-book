"""Exercise 8: relative yields against relative areas across countries, FAOSTAT
2020-2022 averages, countries with at least 10,000 ha of both crops every year."""
import numpy as np
from econdata import faostat_crops

AGG = {"001", "002", "005", "009", "011", "013", "014", "015", "017", "018", "019",
       "021", "029", "030", "034", "035", "039", "053", "054", "057", "061", "097",
       "142", "143", "145", "150", "151", "154", "155", "159", "199", "432", "722",
       "901", "902"}


def table(crop):
    out = {}
    for el in ["Yield", "Area harvested"]:
        d = faostat_crops(crop, el)
        d = d[d.Year.between(2020, 2022) & ~d.m49.isin(AGG)]
        g = d.groupby("Area").Value
        floor = 10_000 if el != "Yield" else 0
        out[el] = g.mean()[(g.count() == 3) & (g.min() >= floor)]
    return out


wheat = table("Wheat")
for other in ["Maize (corn)", "Barley"]:
    o = table(other)
    keep = (wheat["Area harvested"].index.intersection(o["Area harvested"].index)
            .intersection(wheat["Yield"].index).intersection(o["Yield"].index))
    x = np.log(wheat["Yield"][keep] / o["Yield"][keep])
    y = np.log(wheat["Area harvested"][keep] / o["Area harvested"][keep])
    print(f"wheat against {other}: {len(keep)} countries,"
          f" correlation {np.corrcoef(x, y)[0, 1]:.2f}")
