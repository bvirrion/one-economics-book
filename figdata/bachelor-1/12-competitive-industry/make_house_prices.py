"""Opening chart of b1 ch. 12: real house prices (JST hpnom / cpi), 1990 = 100,
Australia, Canada, France, United Kingdom and United States, 1870-2020; and the
ratio 2020/1950 (or the first year after 1950 with data) with its yearly growth.
"""
import numpy as np
import pandas as pd
from econdata import jst
from figout import write_table

ISOS = ["AUS", "CAN", "FRA", "GBR", "USA"]
d = jst(ISOS, 1870, 2020, ["hpnom", "cpi"]).dropna()
d["real"] = d.hpnom / d.cpi
out, pts = {}, []
for iso, g in d.groupby("iso3"):
    g = g.set_index("year").real
    s = 100 * g / g.loc[1990]
    out[iso.lower()] = s.round(2)
    first = int(s.index.min())
    base = int(s.index[s.index >= 1950].min())
    pts.append({"iso3": iso, "first": first, "v_first": round(s.loc[first], 1),
                "base": base, "v1950": round(s.loc[base], 1), "v2020": round(s.loc[2020], 1),
                "ratio_2020_1950": round(s.loc[2020] / s.loc[base], 2),
                "growth_pct": round(100 * ((s.loc[2020] / s.loc[base]) ** (1 / (2020 - base)) - 1), 2)})
w = pd.DataFrame(out).rename_axis("year").reset_index()
write_table(w, __file__, "real_house_prices")
write_table(pd.DataFrame(pts), __file__, "house_points")
