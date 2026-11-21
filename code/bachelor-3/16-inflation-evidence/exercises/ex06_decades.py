"""Exercise 6: money growth and inflation by decade, 17 economies, JST data.

Decade averages of log growth of broad money (`money`) and of the CPI, 1870s to
2010s; regression of inflation on money growth before and after 1970.
"""
import numpy as np
import statsmodels.api as sm
from econdata import jst

j = jst(cols=["money", "cpi"]).sort_values(["iso3", "year"])
j = j[j.iso3 != "DEU"]  # the 1923 currency reform breaks both series
for col in ("money", "cpi"):
    j["g_" + col] = j.groupby("iso3")[col].transform(lambda s: np.log(s).diff())
j["decade"] = 10 * (j.year // 10)
d = j.groupby(["iso3", "decade"]).agg(m=("g_money", "mean"), p=("g_cpi", "mean"),
                                      n=("g_cpi", "count")).dropna()
d = 100 * d[d.n >= 8][["m", "p"]]
d = d.reset_index()
print(f"economy-decades: {len(d)}, economies: {d.iso3.nunique()}")
for name, g in (("before 1970", d[d.decade < 1970]), ("1970 on", d[d.decade >= 1970])):
    r = sm.OLS(g.p, sm.add_constant(g.m)).fit()
    print(f"{name}: slope {r.params['m']:.2f} (s.e. {r.bse['m']:.2f}), "
          f"R-squared {r.rsquared:.2f}, n = {len(g)}")
