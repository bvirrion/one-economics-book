"""Charts of b1 ch. 29.

pip_usa: United States, 2022 (PIP, 2021 PPP, income per person per day, national), average
income of each hundredth of the population.
earn_hist: earnings in 1978, PSID (2,490 men) and CPS (15,992 men) comparison samples of the
NSW data, as densities over bins of 2,000 dollars (CPS capped at 25,564.70).
school: PSID mean earnings in 1978 by years of schooling, 8 to 17, with counts.
clouds: three seeded samples of 200 points with correlation about 1, 0.6 and 0 (a parabola).
simpson: Brenland's household survey, mean disposable income of households with heads under
50 and aged 50 or more, overall and within working and non-working households.
"""
import numpy as np
import pandas as pd
from country import load
from econdata import nsw, pip_percentiles
from figout import write_table

p = pip_percentiles(["USA"], [2022])
p = p[(p.reporting_level == "national") & (p.welfare_type == "income")].sort_values("percentile")
assert len(p) == 100
write_table(p[["percentile", "avg_welfare"]].round(3), __file__, "pip_usa")
med = p.set_index("percentile").avg_welfare
write_table(pd.DataFrame([{"year": 2022, "p10": round(med[10], 2), "p50": round(med[50], 2),
                           "p90": round(med[90], 2), "p100": round(med[100], 2),
                           "top_over_median": round(med[100] / med[50], 2)}]), __file__, "pip_stats")

edges = np.arange(0, 60_001, 2_000)
rows = []
for name in ["psid_controls", "cps_controls"]:
    e = nsw(name).re78
    c, _ = np.histogram(e.clip(upper=59_999), bins=edges)
    rows.append(c / (len(e) * 2_000) * 1e5)  # density per 100,000 dollars
write_table(pd.DataFrame({"lo": edges[:-1] + 1_000, "psid": rows[0].round(4), "cps": rows[1].round(4)}),
            __file__, "earn_hist")

d = nsw("psid_controls")
d = d[d.education.between(8, 17)]
g = d.groupby("education").re78.agg(["count", "mean"]).round(0).reset_index()
write_table(g, __file__, "school")

rng = np.random.default_rng(2026)
x = rng.normal(0, 1, 200)
u = rng.uniform(-1, 1, 200)
cl = pd.DataFrame({"x1": x.round(3), "y1": (x + rng.normal(0, 0.1, 200)).round(3),
                   "x2": x.round(3), "y2": (0.6 * x + 0.8 * rng.normal(0, 1, 200)).round(3),
                   "x3": u.round(3), "y3": (u**2).round(3)})
write_table(cl, __file__, "clouds")
write_table(pd.DataFrame([{"r1": round(np.corrcoef(cl.x1, cl.y1)[0, 1], 3),
                           "r2": round(np.corrcoef(cl.x2, cl.y2)[0, 1], 2),
                           "r3": round(np.corrcoef(cl.x3, cl.y3)[0, 1], 2)}]), __file__, "clouds_r")

h = load("households")
h["older"] = (h.age_head >= 50).astype(int)
h["works"] = (h.hours > 0).astype(int)
s = []
for lab, sub in [("Not working", h[h.works == 0]), ("Working", h[h.works == 1]), ("All", h)]:
    m = sub.groupby("older").disposable.mean().round(0)
    s.append({"group": lab, "young": m[0], "old": m[1]})
s = pd.DataFrame(s)
s["pos"] = [1, 2, 3]
write_table(s, __file__, "simpson")
