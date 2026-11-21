"""LaLonde's test: the experiment's answer against non-experimental estimators
that replace the randomised controls with a survey sample (earnings in 1978, $)."""
import pandas as pd
import statsmodels.formula.api as smf
from econdata import nsw

exp = nsw("nsw_dw")
trainees = exp.query("treat == 1")
bench = smf.ols("re78 ~ treat", exp).fit(cov_type="HC1")
print(f"experiment                  {bench.params.treat:7.0f} ({bench.bse.treat:.0f})")

X = "age + I(age**2) + education + black + hispanic + married + nodegree"
for name in ("cps_controls", "psid_controls"):
    d = pd.concat([trainees, nsw(name).assign(treat=0)], ignore_index=True)
    d["gain"] = d.re78 - d.re75
    est = {
        "difference in means": smf.ols("re78 ~ treat", d),
        "regression, controls": smf.ols(f"re78 ~ treat + {X} + re74 + re75", d),
        "DiD": smf.ols("gain ~ treat", d),
        "DiD, controls": smf.ols(f"gain ~ treat + {X}", d),
    }
    print(name)
    for label, model in est.items():
        f = model.fit(cov_type="HC1")
        print(f"  {label:26s}{f.params.treat:7.0f} ({f.bse.treat:.0f})")
