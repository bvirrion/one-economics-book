"""Charts and tables of b1 ch. 11 (FAOSTAT crops; BLS average prices).

crop_area: area harvested of maize and soya beans, Brazil and the United States,
1961-2024, millions of hectares; crop_area_points: selected years.
cereal_yield: cereal yield (Cereals, primary) in tonnes per hectare, five regions,
1961-2024; yield_growth: 1961 and 2024 values and the yearly growth rate.
flour: US city-average retail price of white flour, dollars per pound, annual means.
"""
import numpy as np
import pandas as pd
from econdata import bls_ap, faostat_crops
from figout import write_table

AREAS = {"Brazil": "bra", "United States of America": "usa"}
cols = {}
for item, tag in [("Maize (corn)", "maize"), ("Soya beans", "soya")]:
    d = faostat_crops(item, "Area harvested")
    d = d[d.Area.isin(AREAS)]
    for area, iso in AREAS.items():
        s = d[d.Area == area].set_index("Year").Value / 1e6
        cols[f"{tag}_{iso}"] = s.round(3)
area = pd.DataFrame(cols).rename_axis("year").reset_index()
write_table(area, __file__, "crop_area")
write_table(area[area.year.isin([1961, 1970, 1990, 2005, 2006, 2007, 2008, 2024])], __file__,
            "crop_area_points")

REG = {"World": "world", "Africa": "africa", "Americas": "americas", "Asia": "asia",
       "Europe": "europe"}
y = faostat_crops("Cereals, primary", "Yield")
y = y[y.Area.isin(REG)]
w = y.pivot(index="Year", columns="Area", values="Value").rename(columns=REG) / 1000
w = w.round(3).rename_axis("year").reset_index()
write_table(w, __file__, "cereal_yield")
rows = []
for r in REG.values():
    a, b = w.loc[w.year == 1961, r].item(), w.loc[w.year == 2024, r].item()
    rows.append({"region": r, "y1961": a, "y2024": b, "ratio": round(b / a, 3),
                 "growth_pct": round(100 * ((b / a) ** (1 / 63) - 1), 2)})
write_table(pd.DataFrame(rows), __file__, "yield_growth")

f = bls_ap("Flour, white", annual=True)
f = f[f.year.between(2000, 2015)][["year", "value"]].round(3)
write_table(f.rename(columns={"value": "flour"}), __file__, "flour")
