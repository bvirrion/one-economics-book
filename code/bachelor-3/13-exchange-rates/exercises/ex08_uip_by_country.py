"""Exercise 8: the UIP regression country by country, 1974--2019 (JST data).

Depreciation against the dollar over the next year (percent, log change) on the
short-term interest differential with the United States this year. UIP: slope 1.
"""
import numpy as np
import statsmodels.api as sm
from econdata import jst

j = jst(cols=["xrusd", "stir"], since=1974, until=2020).sort_values(["iso3", "year"])
us = j[j.iso3 == "USA"].set_index("year").stir
j = j[j.iso3 != "USA"].copy()
j["dep"] = j.groupby("iso3").xrusd.transform(
    lambda s: 100 * np.log(s).diff().shift(-1))
j["diff"] = j.stir - j.year.map(us)
j = j.dropna(subset=["dep", "diff"])

slopes = []
for iso, g in j.groupby("iso3"):
    r = sm.OLS(g.dep, sm.add_constant(g["diff"])).fit()
    b, se = r.params["diff"], r.bse["diff"]
    slopes.append(b)
    print(f"{iso}: slope {b:6.2f} (s.e. {se:.2f}), rejects 1 at 5 %: "
          f"{'yes' if abs(b - 1) > 1.96 * se else 'no'}")
slopes = np.array(slopes)
neg = (slopes < 0).sum()
print(f"mean slope {slopes.mean():.2f}; negative in {neg} of {len(slopes)}")
