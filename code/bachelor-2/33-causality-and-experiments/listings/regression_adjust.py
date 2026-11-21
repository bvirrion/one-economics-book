"""Adding pre-treatment controls: in the experiment, and in the survey comparison."""

import pandas as pd
import statsmodels.formula.api as smf
from econdata import nsw

controls = (
    "age + I(age**2) + education + black + hispanic + married + nodegree + re74 + re75"
)
exp = nsw("nsw_dw")
obs = pd.concat([exp.query("treat == 1"), nsw("cps_controls")])

for name, d in (("experiment", exp), ("survey comparison", obs)):
    raw = smf.ols("re78 ~ treat", d).fit(cov_type="HC1")
    adj = smf.ols("re78 ~ treat + " + controls, d).fit(cov_type="HC1")
    print(f"{name:18s} raw {raw.params.treat:9.1f} ({raw.bse.treat:5.1f})"
          f"   adjusted {adj.params.treat:8.1f} ({adj.bse.treat:5.1f})")  # fmt: skip
