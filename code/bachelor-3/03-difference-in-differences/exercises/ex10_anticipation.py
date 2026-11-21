"""Exercise 10: an event study when units react one period before adoption.
Same design as the chapter's chart (100 units adopt in period 6, 100 in 11, 100 never),
but the effect starts at k = -1 with 0.3. Two reference periods are compared."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

rng = np.random.default_rng(2021)
rows = []
for c, s in (("A", 6), ("B", 11), ("N", None)):
    for i in range(100):
        a = rng.normal()
        for t in range(1, 17):
            k = None if s is None else t - s
            eff = 0.0 if k is None or k < -1 else (0.3 if k == -1 else 0.5 + 0.1 * k)
            rows.append((f"{c}{i}", t, -99 if k is None else k,
                         a + 0.1 * t + eff + rng.normal(0, 0.5)))
d = pd.DataFrame(rows, columns=["unit", "t", "k", "y"])


def event_study(ref):
    names = {}
    for k in range(-10, 11):
        if k != ref:
            names[k] = f"k{k + 10}"
            d[names[k]] = (d.k == k).astype(float)
    f = smf.ols("y ~ " + " + ".join(names.values()) + " + C(unit) + C(t)", d).fit()
    return {k: f.params[n] for k, n in names.items()}


for ref in (-1, -2):
    b = event_study(ref)
    shown = [k for k in (-3, -2, -1, 0, 1, 2) if k != ref]
    print(f"reference {ref}: " + "  ".join(f"k={k}: {b[k]:5.2f}" for k in shown))
