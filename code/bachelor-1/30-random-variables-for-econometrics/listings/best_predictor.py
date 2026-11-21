"""Three predictors of earnings from schooling: mean squared errors."""

import numpy as np
from econdata import nsw

d = nsw("psid_controls")
x, y = d.education, d.re78
pred = {
    "overall mean": np.full(len(y), y.mean()),
    "a line": np.polyval(np.polyfit(x, y, 1), x),
    "conditional mean": d.groupby("education").re78.transform("mean"),
}
for name, p in pred.items():
    print(f"{name:17s} MSE {((y - p) ** 2).mean() / 1e6:8.2f} million")
