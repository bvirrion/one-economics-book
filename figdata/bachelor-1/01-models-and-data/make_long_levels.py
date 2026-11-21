"""GDP per person of the United Kingdom and Japan, 1870-2022 (Maddison), for a
logarithmic axis; plus average growth per period, the slopes a reader reads off it."""
import numpy as np
import pandas as pd
from econdata import maddison
from figout import write_table

d = maddison(["GBR", "JPN"], 1870, 2022).pivot(index="year", columns="iso3", values="gdppc")
d = d.dropna().reset_index()
write_table(d[["year", "GBR", "JPN"]].round(0), __file__, "gbr_jpn")

rows = []
for a, b in [(1870, 1913), (1913, 1950), (1950, 1973), (1973, 2000), (2000, 2022)]:
    for c in ["GBR", "JPN"]:
        x0 = d.loc[d.year == a, c].iloc[0]
        x1 = d.loc[d.year == b, c].iloc[0]
        rows.append({"start": a, "end": b, "iso3": c, "x0": round(x0), "x1": round(x1),
                     "growth": round(100 * np.log(x1 / x0) / (b - a), 2)})
write_table(pd.DataFrame(rows), __file__, "gbr_jpn_growth")
