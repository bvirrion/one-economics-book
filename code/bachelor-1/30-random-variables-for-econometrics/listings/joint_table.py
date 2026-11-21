"""A joint distribution: schooling and earnings bracket, PSID sample, 1978."""

import pandas as pd
from econdata import nsw

d = nsw("psid_controls")
school = pd.cut(d.education, [0, 11, 12, 20], labels=["<12", "12", ">12"])
bracket = pd.cut(d.re78, [-1, 10_000, 30_000, 1e9], labels=["<10k", "10-30k", ">30k"])
joint = pd.crosstab(school, bracket, normalize=True, margins=True).round(3)
print("joint distribution, with marginals:")
print(joint)
cond = pd.crosstab(school, bracket, normalize="index").round(3)  # rows sum to 1
print("earnings bracket given schooling:")
print(cond)
