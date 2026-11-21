"""The market model with shifting curves (b1 ch. 1, section 5), simulated.

Demand Q = a - b p + ud, supply Q = c + d p + us, with a = 10, b = 1, c = 2, d = 1
and independent shocks ud, us ~ N(0, 1) (seed 101). Writes
  - curves.csv: three demand-supply pairs (the first three draws), as the quantity of
    each line at p = 1 and p = 9, for the diagram;
  - cloud.csv: the 30 equilibria (p, q) of 30 draws;
  - cloud_stats.csv: the cloud's least-squares slope of q on p, and the model's value
    (d s_d^2 - b s_s^2) / (s_d^2 + s_s^2) with the sample variances of the shocks.
"""
import numpy as np
import pandas as pd
from figout import write_table

a, b, c, d = 10.0, 1.0, 2.0, 1.0
rng = np.random.default_rng(101)
ud = rng.normal(0, 1, 30)
us = rng.normal(0, 1, 30)
p = (a - c + ud - us) / (b + d)
q = c + d * p + us
write_table(pd.DataFrame({"p": p.round(3), "q": q.round(3)}), __file__, "cloud")

ends = np.array([1.0, 9.0])
cur = {"p": ends}
for k in range(3):
    cur[f"qd{k + 1}"] = (a - b * ends + ud[k]).round(3)
    cur[f"qs{k + 1}"] = (c + d * ends + us[k]).round(3)
write_table(pd.DataFrame(cur), __file__, "curves")

vd, vs = ud.var(ddof=1), us.var(ddof=1)
cv = np.cov(ud, us)[0, 1]
model = (d * vd - b * vs) / (vd + vs)
full = (d * vd - b * vs + (b - d) * cv) / (vd + vs - 2 * cv)
ols = np.polyfit(p, q, 1)[0]
write_table(pd.DataFrame({"var_ud": [round(vd, 3)], "var_us": [round(vs, 3)],
                          "cov_uds": [round(cv, 3)], "model_slope": [round(model, 3)],
                          "full_slope": [round(full, 3)], "ols_slope": [round(ols, 3)]}),
            __file__, "cloud_stats")
