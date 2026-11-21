"""Difference-in-differences on the NSW job-training data: the trainees against
a survey sample, earnings in 1975 (before) and 1978 (after), in dollars."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from econdata import nsw

trainees = nsw("nsw_dw").query("treat == 1")
survey = nsw("cps_controls").assign(treat=0)
d = pd.concat([trainees, survey], ignore_index=True)
d["person"] = np.arange(len(d))

means = d.groupby("treat")[["re75", "re78"]].mean()
print("                       1975      1978")
for g, label in ((1, "trainees"), (0, "survey")):
    print(f"{label:16s}{means.re75[g]:10.0f}{means.re78[g]:10.0f}")
change = means.re78 - means.re75
print(f"change, trainees   {change[1]:9.0f}")
print(f"change, survey     {change[0]:9.0f}")
print(f"DiD                {change[1] - change[0]:9.0f}")

# the same number by OLS: stack the two years, interact group and period
long = pd.concat([d.assign(after=0, earn=d.re75), d.assign(after=1, earn=d.re78)])
fit = smf.ols("earn ~ treat * after", long).fit(
    cov_type="cluster", cov_kwds={"groups": long.person})
print(f"OLS interaction    {fit.params['treat:after']:9.0f}"
      f"   (clustered s.e. {fit.bse['treat:after']:.0f})")
