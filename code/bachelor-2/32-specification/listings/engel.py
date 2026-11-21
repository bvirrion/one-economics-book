"""An Engel curve for food: levels, logs and the budget share."""

import numpy as np
import statsmodels.formula.api as smf
from econdata import sm_dataset

d = sm_dataset("engel")  # 235 households, income and food spending
d["lfood"] = np.log(d.foodexp)
d["linc"] = np.log(d.income)

loglog = smf.ols("lfood ~ linc", d).fit()
b, se = loglog.params.linc, loglog.bse.linc
print(f"log-log: elasticity {b:.3f} (s.e. {se:.3f}), R2 {loglog.rsquared:.3f}")

levels = smf.ols("foodexp ~ income", d).fit()
slope = levels.params.income
at_means = slope * d.income.mean() / d.foodexp.mean()
print(
    f"levels: {slope:.3f} francs of food per franc; elasticity at means {at_means:.3f}"
)

share = smf.ols("I(foodexp / income) ~ linc", d).fit()
print(f"budget share on log income: slope {share.params.linc:.3f}")
print(f"mean budget share {(d.foodexp / d.income).mean():.3f}")
