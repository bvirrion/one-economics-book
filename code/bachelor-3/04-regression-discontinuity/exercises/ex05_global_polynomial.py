"""Exercise 5: global polynomials against a local linear fit, on 300 small samples
(800 elections each) of the chapter's simulated elections; true jump 0.077."""
import numpy as np
from rdtools import local_linear

from elections import draw


def global_poly(m, y, order):
    X = np.column_stack([m**p for p in range(order + 1)]
                        + [(m >= 0) * m**p for p in range(order + 1)])
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    return b[order + 1]                       # the jump in the intercept at 0


est = {k: [] for k in ("poly 1", "poly 2", "poly 4", "poly 6", "local linear 0.25")}
for s in range(300):
    m, y, _ = draw(n=800, seed=s)
    for p in (1, 2, 4, 6):
        est[f"poly {p}"].append(global_poly(m, y, p))
    est["local linear 0.25"].append(local_linear(m, y, 0, 0.25)["jump"])
print("fit                  bias    s.d.")
for k, v in est.items():
    e = np.array(v) - 0.077
    print(f"{k:18s} {e.mean():7.3f} {e.std():7.3f}")
