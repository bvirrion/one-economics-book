"""Earnings in 1978 on earnings in 1975, and the reverse regression."""

import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("psid_controls")
forward = smf.ols("re78 ~ re75", data=d).fit().params["re75"]
backward = smf.ols("re75 ~ re78", data=d).fit().params["re78"]
r = d.re75.corr(d.re78)
print(f"1978 on 1975: slope {forward:.4f}")
print(f"1975 on 1978: slope {backward:.4f}")
print(f"product {forward * backward:.4f}; r squared {r**2:.4f}")
top = d.re75 >= d.re75.quantile(0.9)
print(
    f"top tenth in 1975: mean {d.re75[top].mean():,.0f} then {d.re78[top].mean():,.0f}"
)
