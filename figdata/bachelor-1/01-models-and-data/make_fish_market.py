"""The weekend problem of b1 ch. 1: forty days of the Brenmoor fish market (invented).

Demand  Q = 180 - 10 p + 30 F + ud   (F = 1 on the four festival days)
Supply  Q =  20 + 10 p - 30 W + us   (W = 1 on the ten storm days)
p in dalens per kilogram, Q in crates sold; ud, us ~ N(0, 4^2), seed 2026.
Writes fish.csv (day, storm, festival, price, crates) and fish_stats.csv: the means
on calm ordinary days and on storm days, the demand slope recovered from storm days
(the ratio of the two differences, festival days left out), the least-squares slope
of crates on price over all forty days, and the demand elasticity at the forty-day
means implied by the recovered slope.
"""
import numpy as np
import pandas as pd
from figout import write_table

rng = np.random.default_rng(2026)
days = np.arange(1, 41)
storm = np.isin(days, [3, 7, 8, 14, 19, 22, 23, 29, 33, 38]).astype(int)
fest = np.isin(days, [16, 17, 30, 31]).astype(int)
ud = rng.normal(0, 4, 40)
us = rng.normal(0, 4, 40)
price = (160 + 30 * fest + 30 * storm + ud - us) / 20
crates = 20 + 10 * price - 30 * storm + us
t = pd.DataFrame({"day": days, "storm": storm, "festival": fest,
                  "price": price.round(2), "crates": crates.round(0).astype(int)})
write_table(t, __file__, "fish")

# every statistic below is computed from the printed means: prices to 4 decimals,
# crates to 2 (the sums of fish_groups.csv divided exactly, so no rounding tie)
def means(g):
    return round(g.price.sum() / len(g), 4), round(g.crates.sum() / len(g), 2)


calm = t[(t.storm == 0) & (t.festival == 0)]
stormy = t[(t.storm == 1) & (t.festival == 0)]
fest = t[t.festival == 1]
(pc, qc), (ps, qs), (pf, qf), (pa, qa) = means(calm), means(stormy), means(fest), means(t)
slope = round((qs - qc) / (ps - pc), 2)
s = pd.DataFrame({
    "p_calm": [pc], "q_calm": [qc], "p_storm": [ps], "q_storm": [qs],
    "p_fest": [pf], "q_fest": [qf], "p_mean": [pa], "q_mean": [qa],
    "slope_storm": [slope], "slope_fest": [round((qf - qc) / (pf - pc), 2)],
    "ols_all": [round(np.polyfit(t.price, t.crates, 1)[0], 2)],
    "elasticity": [round(slope * pa / qa, 2)],
    "elasticity_true": [round(-10 * pa / qa, 2)],
})
write_table(s, __file__, "fish_stats")

# the chart of the problem, one table per kind of day; and the sums the problem prints
groups = {"calm": calm, "storm": stormy, "fest": fest}
for k, g in groups.items():
    write_table(g[["day", "price", "crates"]], __file__, f"fish_{k}")
write_table(pd.DataFrame({
    "days": [len(g) for g in groups.values()],
    "sum_price": [round(g.price.sum(), 2) for g in groups.values()],
    "sum_crates": [int(g.crates.sum()) for g in groups.values()],
}, index=["Calm ordinary days", "Storm days", "Festival days"]).reset_index(names="kind"),
    __file__, "fish_groups")
