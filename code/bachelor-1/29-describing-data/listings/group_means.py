"""Conditional means: earnings in 1978 by years of schooling (PSID sample)."""

from econdata import nsw

d = nsw("psid_controls")
d = d[d.education.between(8, 17)]
g = d.groupby("education").re78.agg(["count", "mean", "median"]).round(0)
print(g.to_string())
