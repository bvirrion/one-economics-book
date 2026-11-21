"""Exercise 6: a placebo DiD before training began. Both years, 1974 and 1975, come
before the programme; a non-zero DiD measures the gap in trends, not an effect."""
import pandas as pd
import statsmodels.formula.api as smf
from econdata import nsw

trainees = nsw("nsw_dw").query("treat == 1")
print("1974 to 1975 change, trainees", f"{(trainees.re75 - trainees.re74).mean():8.0f}")
for name in ("cps_controls", "psid_controls"):
    d = pd.concat([trainees, nsw(name).assign(treat=0)], ignore_index=True)
    d["gain"] = d.re75 - d.re74
    f = smf.ols("gain ~ treat", d).fit(cov_type="HC1")
    change = d.loc[d.treat == 0, "gain"].mean()
    print(f"{name:14s} change {change:7.0f}   placebo DiD {f.params.treat:6.0f}"
          f" ({f.bse.treat:.0f})")
