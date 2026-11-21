"""The gravity equation by OLS on logs, 2019."""
import numpy as np
import statsmodels.formula.api as smf
from econdata import gravity

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "gdp_o", "gdp_d", "dist",
        "contig", "col45", "fta_wto"]
d = gravity(since=2019, until=2019, columns=COLS).dropna()
d["ln_x"] = np.log(d.tradeflow_baci)  # positive flows only: zeros have no log
d["ln_gdp_o"], d["ln_gdp_d"] = np.log(d.gdp_o), np.log(d.gdp_d)
d["ln_dist"] = np.log(d.dist)

f = "ln_x ~ ln_gdp_o + ln_gdp_d + ln_dist + contig + col45 + fta_wto"
r = smf.ols(f, data=d).fit(cov_type="HC1")  # robust standard errors
print(f"pairs {int(r.nobs):,}, R-squared {r.rsquared:.3f}")
for name in r.params.index[1:]:
    print(f"{name:10s} {r.params[name]:7.3f}  ({r.bse[name]:.3f})")
