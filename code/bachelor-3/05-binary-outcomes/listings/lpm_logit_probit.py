"""Who had earnings in 1978? A linear probability model, a logit and a probit on the
survey sample of men from the NSW files; average marginal effects side by side."""
import numpy as np
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("cps_controls")
d["work"] = (d.re78 > 0).astype(int)
d["earn75"] = d.re75 / 1000                        # thousands of dollars
f = "work ~ earn75 + age + education + married"

lpm = smf.ols(f, d).fit(cov_type="HC1")
logit = smf.logit(f, d).fit(disp=0)
probit = smf.probit(f, d).fit(disp=0)
ame_l = logit.get_margeff().margeff
ame_p = probit.get_margeff().margeff

print(f"men {len(d)}, share with earnings in 1978 {d.work.mean():.3f}")
print("              LPM     logit   probit |  AME logit  AME probit")
for k, name in enumerate(["earn75", "age", "education", "married"]):
    print(f"{name:10s} {lpm.params[name]:7.4f} {logit.params[name]:8.4f}"
          f" {probit.params[name]:8.4f} | {ame_l[k]:9.4f} {ame_p[k]:10.4f}")
fitted = lpm.fittedvalues
print(f"LPM fitted values above 1: {np.mean(fitted > 1):.3f} of the sample,"
      f" largest {fitted.max():.3f}")
