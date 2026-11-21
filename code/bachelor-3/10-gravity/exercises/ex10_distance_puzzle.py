"""Exercise 10: is there a trend in the distance elasticity, 1996--2020?"""
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from econdata import gravity

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "dist", "contig",
        "comlang_off", "col45", "fta_wto"]
RHS = "ln_dist + contig + comlang_off + col45 + fta_wto + C(iso3_o) + C(iso3_d)"
years, elast = list(range(1996, 2021, 4)), []
for year in years:
    d = gravity(since=year, until=year, columns=COLS).dropna()
    d["ln_x"], d["ln_dist"] = np.log(d.tradeflow_baci), np.log(d.dist)
    elast.append(smf.ols("ln_x ~ " + RHS, data=d).fit().params["ln_dist"])
    print(f"{year} distance elasticity {elast[-1]:.3f}")
t = sm.OLS(elast, sm.add_constant(np.array(years) - 2008.0)).fit()
print(f"trend per decade {10 * t.params[1]:.3f} (s.e. {10 * t.bse[1]:.3f}), "
      f"t = {t.tvalues[1]:.2f}")
