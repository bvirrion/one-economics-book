"""Event study on a simulated staggered roll-out.

300 units, periods 1-16: 100 adopt in period 6, 100 in period 11, 100 never. Unit effects
N(0,1), a common trend 0.1 per period, errors N(0, 0.5). The effect k periods after
adoption is 0.5 + 0.1 k (k >= 0), the same for both cohorts; nothing happens before.
Regression: unit and period effects plus a dummy for every relative period except -1,
standard errors clustered by unit. Writes out/event_study.csv (k, est, lo, hi, true) for
k = -5..5. Book 5, chapter 3, chart 2.
"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from figout import write_table

START = {"A": 6, "B": 11, "N": None}


def panel(seed=2021):
    rng = np.random.default_rng(seed)
    rows = []
    for c, s in START.items():
        for i in range(100):
            a = rng.normal()
            for t in range(1, 17):
                k = None if s is None else t - s
                eff = 0.5 + 0.1 * k if k is not None and k >= 0 else 0.0
                rows.append((f"{c}{i}", t, k, a + 0.1 * t + eff + rng.normal(0, 0.5)))
    return pd.DataFrame(rows, columns=["unit", "t", "k", "y"])


def table():
    d = panel()
    names = []
    for k in range(-10, 11):
        if k == -1:
            continue
        n = f"k_m{-k}" if k < 0 else f"k_{k}"
        d[n] = (d.k == k).astype(float)
        names.append(n)
    f = smf.ols("y ~ " + " + ".join(names) + " + C(unit) + C(t)", d).fit(
        cov_type="cluster", cov_kwds={"groups": pd.factorize(d.unit)[0]})
    rows = []
    for k in range(-5, 6):
        if k == -1:
            rows.append((k, 0.0, 0.0, 0.0, 0.0))
            continue
        n = f"k_m{-k}" if k < 0 else f"k_{k}"
        b, se = f.params[n], f.bse[n]
        rows.append((k, b, b - 1.96 * se, b + 1.96 * se, 0.5 + 0.1 * k if k >= 0 else 0.0))
    return pd.DataFrame(rows, columns=["k", "est", "lo", "hi", "true"])


if __name__ == "__main__":
    write_table(table(), __file__, "event_study")
