"""Exercise 12: Wagner's law within countries, JST data, 1870-2020.

Central-government expenditure over GDP (percent) on log real GDP per person
(rgdpmad), with country fixed effects, then with country and year fixed effects;
standard errors clustered by country.
"""
import numpy as np
import statsmodels.formula.api as smf
from econdata import jst

j = jst(cols=["expenditure", "gdp", "rgdpmad"])
j = j[j.year.between(1870, 2020)].copy()
j["s"] = 100 * j.expenditure / j.gdp
j["ly"] = np.log(j.rgdpmad)
d = j.dropna(subset=["s", "ly"])
print(f"observations: {len(d)}, economies: {d.iso3.nunique()}")
for label, f in (("country effects", "s ~ ly + C(iso3)"),
                 ("country and year effects", "s ~ ly + C(iso3) + C(year)")):
    r = smf.ols(f, d).fit(cov_type="cluster", cov_kwds={"groups": d.iso3})
    print(f"{label}: slope {r.params['ly']:.2f} (s.e. {r.bse['ly']:.2f})")
