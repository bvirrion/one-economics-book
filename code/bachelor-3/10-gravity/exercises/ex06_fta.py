"""Exercise 6: a trade agreement's effect, OLS on logs against PPML, 2005 and 2019."""
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from econdata import gravity

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "dist", "contig",
        "comlang_off", "col45", "fta_wto"]
RHS = "ln_dist + contig + comlang_off + col45 + fta_wto + C(iso3_o) + C(iso3_d)"
for year in (2005, 2019):
    d = gravity(since=year, until=year, columns=COLS).dropna()
    d["ln_x"], d["ln_dist"] = np.log(d.tradeflow_baci), np.log(d.dist)
    d["x"] = d.tradeflow_baci / 1e3
    o = smf.ols("ln_x ~ " + RHS, data=d).fit(cov_type="HC1")
    p = smf.glm("x ~ " + RHS, data=d, family=sm.families.Poisson()).fit(cov_type="HC1")
    for name, r in (("OLS ", o), ("PPML", p)):
        b, s = r.params["fta_wto"], r.bse["fta_wto"]
        print(f"{year} {name} agreement {b:.3f} ({s:.3f}), "
              f"trade x {np.exp(b):.2f}")
