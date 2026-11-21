"""Covariate balance: pre-treatment means of the treated and control men."""

import numpy as np
from econdata import nsw

d = nsw("nsw_dw")
cols = ["age", "education", "black", "hispanic", "married", "nodegree", "re74", "re75"]
print("variable     treated   control   difference      t")
for col in cols:
    t, c = d[d.treat == 1][col], d[d.treat == 0][col]
    se = np.sqrt(t.var() / len(t) + c.var() / len(c))
    diff = t.mean() - c.mean()
    print(f"{col:10s} {t.mean():9.2f} {c.mean():9.2f} {diff:12.2f} {diff / se:6.2f}")
