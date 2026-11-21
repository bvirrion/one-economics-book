"""Gravity with exporter and importer fixed effects (OLS on logs), 2019."""
import numpy as np
import statsmodels.formula.api as smf
from econdata import gravity

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "dist", "contig",
        "comlang_off", "col45", "fta_wto"]
d = gravity(since=2019, until=2019, columns=COLS).dropna()
d["ln_x"], d["ln_dist"] = np.log(d.tradeflow_baci), np.log(d.dist)

# C(...) adds one dummy per exporter and per importer: they absorb GDPs and
# multilateral resistance, so GDPs are no longer in the equation
f = "ln_x ~ ln_dist + contig + comlang_off + col45 + fta_wto + C(iso3_o) + C(iso3_d)"
r = smf.ols(f, data=d).fit(cov_type="HC1")
print(f"pairs {int(r.nobs):,}, parameters {len(r.params)}")
for name in ["ln_dist", "contig", "comlang_off", "col45", "fta_wto"]:
    print(f"{name:12s} {r.params[name]:7.3f}  ({r.bse[name]:.3f})")
