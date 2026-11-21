"""The CPS comparison sample: men with positive earnings in 1975 and 1978."""

import numpy as np
from econdata import nsw

d = nsw("cps_controls")
cap = d.re78.max()
print(f"men in the file: {len(d)}")
print(f"share at the 1978 maximum of {cap:,.1f}: {(d.re78 == cap).mean():.1%}")

d = d[(d.re78 > 0) & (d.re75 > 0)].copy()
d["lre78"] = np.log(d.re78)
d["lre75"] = np.log(d.re75)
print(f"men with positive earnings in 1975 and 1978: {len(d)}")

cols = ["lre78", "education", "age", "black", "hispanic", "married", "lre75"]
table = d[cols].describe().loc[["mean", "std", "min", "max"]].T
print(table.round(2).to_string())
