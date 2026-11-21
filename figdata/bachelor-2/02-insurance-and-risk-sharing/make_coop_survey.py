"""The Kestrian fishing cooperative: a simulated survey and the risk-sharing test.

Kestria is an invented economy. 100 fishing households are observed for 8 years
(seed 4202). Log income is a common (aggregate) part plus an idiosyncratic part;
log consumption keeps a share KEPT of the idiosyncratic part (the rest is shared),
plus measurement error. The pooled regression of the problem,
    d ln c_it = b0 + b1 d ln cbar_t + b2 d ln m_it + u_it,
with cbar_t the cooperative's average consumption (geometric mean), is run by OLS.

Writes out/coop_regression.csv: term, coef, se, t (rounded to 3 decimals), and
out/coop_meta.csv: households, years, observations, kept (the simulation's true share).
Book 4, chapter 2, weekend problem part IV.
"""

import numpy as np
import pandas as pd
from figout import write_table

SEED, N, T = 4202, 100, 8
KEPT = 0.15  # share of the idiosyncratic income shock that stays with the household
SD_AGG, SD_IDIO, SD_MEAS = 0.10, 0.30, 0.05


def survey():
    rng = np.random.default_rng(SEED)
    agg = np.cumsum(rng.normal(0.0, SD_AGG, T))
    idio = rng.normal(0.0, SD_IDIO, (N, T))
    level = rng.normal(np.log(20_000), 0.2, (N, 1))
    ln_m = level + agg + idio
    ln_c = level + agg + KEPT * idio + rng.normal(0.0, SD_MEAS, (N, T))
    return ln_m, ln_c


def regression():
    ln_m, ln_c = survey()
    cbar = ln_c.mean(axis=0)
    dc = np.diff(ln_c, axis=1).ravel()
    dm = np.diff(ln_m, axis=1).ravel()
    dcbar = np.tile(np.diff(cbar), N)
    x = np.column_stack([np.ones_like(dc), dcbar, dm])
    coef, *_ = np.linalg.lstsq(x, dc, rcond=None)
    resid = dc - x @ coef
    s2 = resid @ resid / (len(dc) - x.shape[1])
    se = np.sqrt(np.diag(s2 * np.linalg.inv(x.T @ x)))
    reg = pd.DataFrame(
        {"term": ["const", "dlncbar", "dlnm"], "coef": coef, "se": se, "t": coef / se}
    ).round(3)
    meta = pd.DataFrame(
        [{"households": N, "years": T, "observations": len(dc), "kept": KEPT}]
    )
    return reg, meta


if __name__ == "__main__":
    reg, meta = regression()
    write_table(reg, __file__, "coop_regression")
    write_table(meta, __file__, "coop_meta")
