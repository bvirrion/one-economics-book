"""The NSW experiment: the difference in mean 1978 earnings and its standard error."""

import numpy as np
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("nsw_dw")  # 185 men assigned to training, 260 to control
t, c = d[d.treat == 1].re78, d[d.treat == 0].re78
diff = t.mean() - c.mean()
se = np.sqrt(t.var() / len(t) + c.var() / len(c))
print(f"treated {t.mean():8.1f} (n = {len(t)}), control {c.mean():8.1f} (n = {len(c)})")
print(f"difference {diff:.1f}, s.e. {se:.1f}")
print(f"95 % interval {diff - 1.96 * se:.1f} to {diff + 1.96 * se:.1f}")

fit = smf.ols("re78 ~ treat", d).fit(cov_type="HC1")
print(f"regression on treat: {fit.params.treat:.1f} (robust s.e. {fit.bse.treat:.1f})")
