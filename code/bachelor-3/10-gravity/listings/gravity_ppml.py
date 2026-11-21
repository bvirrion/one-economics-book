"""Gravity by Poisson pseudo-maximum likelihood with the same fixed effects, 2019."""
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from econdata import gravity

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "dist", "contig",
        "comlang_off", "col45", "fta_wto"]
d = gravity(since=2019, until=2019, columns=COLS).dropna()
d["x"] = d.tradeflow_baci / 1e3  # millions of dollars, in levels: no log
d["ln_dist"] = np.log(d.dist)

f = "x ~ ln_dist + contig + comlang_off + col45 + fta_wto + C(iso3_o) + C(iso3_d)"
r = smf.glm(f, data=d, family=sm.families.Poisson()).fit(cov_type="HC1")
print(f"pairs {int(r.nobs):,}, converged {r.converged}")
for name in ["ln_dist", "contig", "comlang_off", "col45", "fta_wto"]:
    print(f"{name:12s} {r.params[name]:7.3f}  ({r.bse[name]:.3f})")
