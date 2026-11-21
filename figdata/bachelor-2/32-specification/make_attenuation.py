"""Attenuation: a simulated slope as measurement noise grows, chapter 32 (illustrative).

True model y = 1 + 2 x* + u, with x* and u standard normal, n = 1000. The regressor is
observed with classical error, x = x* + e, Var(e) = s2 from 0 to 3 in steps of 0.1. One
seeded sample per noise level. The curve is the probability limit 2 / (1 + s2).
Writes
  out/attenuation.csv   s2, slope (estimated), plim (2 lambda), lam (reliability ratio)
"""

import numpy as np
import pandas as pd
from figout import write_table

BETA, N, SEED = 2.0, 1000, 32


def table():
    rng = np.random.default_rng(SEED)
    rows = []
    for s2 in np.round(np.arange(0, 3.01, 0.1), 1):
        xs = rng.standard_normal(N)
        y = 1 + BETA * xs + rng.standard_normal(N)
        x = xs + np.sqrt(s2) * rng.standard_normal(N)
        slope = np.cov(x, y)[0, 1] / np.var(x, ddof=1)
        lam = 1 / (1 + s2)
        rows.append({"s2": s2, "slope": round(slope, 3), "plim": round(BETA * lam, 3),
                     "lam": round(lam, 3)})  # fmt: skip
    return pd.DataFrame(rows)


if __name__ == "__main__":
    write_table(table(), __file__, "attenuation")
