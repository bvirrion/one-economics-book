"""Exercise 5: add a common official language to the gravity equation of the listing."""
import numpy as np
import statsmodels.formula.api as smf
from econdata import gravity

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "gdp_o", "gdp_d", "dist",
        "contig", "comlang_off", "col45", "fta_wto"]
d = gravity(since=2019, until=2019, columns=COLS).dropna()
d["ln_x"], d["ln_dist"] = np.log(d.tradeflow_baci), np.log(d.dist)
d["ln_gdp_o"], d["ln_gdp_d"] = np.log(d.gdp_o), np.log(d.gdp_d)

base = "ln_x ~ ln_gdp_o + ln_gdp_d + ln_dist + contig + col45 + fta_wto"
for f in (base, base + " + comlang_off"):
    r = smf.ols(f, data=d).fit(cov_type="HC1")
    lang = r.params.get("comlang_off")
    extra = "" if lang is None else f", language {lang:.3f}"
    print(f"pairs {int(r.nobs):,}: distance {r.params['ln_dist']:.3f}, "
          f"colony {r.params['col45']:.3f}{extra}")
print(f"a common language multiplies trade by {np.exp(lang):.2f}")
