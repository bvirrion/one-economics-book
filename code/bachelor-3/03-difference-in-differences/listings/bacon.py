"""Staggered adoption: two-way fixed effects against a clean comparison.
Cohort E is treated from period 4, cohort L from period 8, cohort N never;
the effect grows by 1 per period of exposure."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

rng = np.random.default_rng(5)
rows = []
for cohort, start, size in (("E", 4, 100), ("L", 8, 100), ("N", 99, 100)):
    for i in range(size):
        a = rng.normal()
        for t in range(1, 13):
            exposure = max(0, t - start + 1)
            rows.append((f"{cohort}{i}", cohort, t, int(t >= start), exposure,
                         a + 0.2 * t + exposure + rng.normal(0, 0.5)))
d = pd.DataFrame(rows, columns=["unit", "cohort", "t", "d", "exposure", "y"])

twfe = smf.ols("y ~ d + C(unit) + C(t)", d).fit().params["d"]
att = d.loc[d.d == 1, "exposure"].mean()       # true average effect on treated
print(f"true average effect on the treated   {att:.3f}")
print(f"two-way fixed effects                {twfe:.3f}")

# clean: each treated cell against the never-treated, relative to the
# cohort's last untreated period (one 2x2 comparison per cell)
gaps = []
for cohort, start in (("E", 4), ("L", 8)):
    g = d[d.cohort.isin([cohort, "N"])].groupby(["cohort", "t"]).y.mean()
    base = g[cohort, start - 1] - g["N", start - 1]
    for t in range(start, 13):
        gaps.append((g[cohort, t] - g["N", t] - base, 100))
est = sum(v * w for v, w in gaps) / sum(w for _, w in gaps)
print(f"clean comparisons, averaged          {est:.3f}")
