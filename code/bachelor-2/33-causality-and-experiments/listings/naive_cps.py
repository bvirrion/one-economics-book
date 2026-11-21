"""The treated men against the CPS comparison sample: a naive 'effect'."""

import pandas as pd
import statsmodels.formula.api as smf
from econdata import nsw

treated = nsw("nsw_dw").query("treat == 1")
others = nsw("cps_controls")  # treat = 0 for all of them
d = pd.concat([treated, others])

fit = smf.ols("re78 ~ treat", d).fit(cov_type="HC1")
print(f"men: {len(treated)} trained, {len(others)} in the survey")
print(f"naive difference {fit.params.treat:.1f} (s.e. {fit.bse.treat:.1f})")
for col in ["age", "education", "married", "re75"]:
    a, b = treated[col].mean(), others[col].mean()
    print(f"mean {col:9s} trained {a:9.2f}, survey {b:9.2f}")
