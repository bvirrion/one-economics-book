"""Second chart and weekend problem of b1 ch. 5: food spending against total consumption in the
Brenland household survey of 2025 (invented, 2,000 households), with means by tenth of
consumption; the log-log slope, the Cobb--Douglas share and the straight-line (Stone--Geary)
fit food = a + b * consumption, and the subsistence food spending it implies, a / (1 - b)."""
import numpy as np
import pandas as pd
from figout import write_table

import country

h = country.load("households")[["hh", "food", "consumption"]]
write_table(h, __file__, "brenland_food")
h["tenth"] = pd.qcut(h.consumption, 10, labels=range(1, 11)).astype(int)
g = h.groupby("tenth")[["consumption", "food"]].mean().reset_index()
g["share"] = g.food / g.consumption
write_table(g.round({"consumption": 0, "food": 0, "share": 3}), __file__, "brenland_tenths")

slope, icept = np.polyfit(np.log(h.consumption), np.log(h.food), 1)
b, a = np.polyfit(h.consumption, h.food, 1)
fit = pd.DataFrame([{
    "households": len(h),
    "mean_food": round(h.food.mean()), "mean_cons": round(h.consumption.mean()),
    "agg_share": round(h.food.sum() / h.consumption.sum(), 3),
    "log_slope": round(slope, 2), "a": round(a), "b": round(b, 3),
}])
fit["gamma"] = round(fit.a / (1 - fit.b))
fit["below_gamma"] = int((h.food < fit.gamma[0]).sum())
write_table(fit, __file__, "brenland_fit")
x = np.round(np.geomspace(5000, 80000, 40))
write_table(pd.DataFrame({"consumption": x, "line": (fit.a[0] + fit.b[0] * x).round(),
                          "cd": (fit.agg_share[0] * x).round()}), __file__, "brenland_lines")
