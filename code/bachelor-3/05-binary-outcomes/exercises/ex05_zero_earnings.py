"""Exercise 5: men with no earnings in 1975 are a group of their own. Add a dummy for
them to the logit and compare the fitted share at zero with the observed one."""
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("cps_controls")
d["work"] = (d.re78 > 0).astype(int)
d["earn75"] = d.re75 / 1000
d["zero75"] = (d.re75 == 0).astype(int)
zero = d.zero75 == 1
for f in ("work ~ earn75", "work ~ earn75 + zero75"):
    m = smf.logit(f, d).fit(disp=0)
    print(f"{f:24s} log-likelihood {m.llf:10.1f}   mean fitted share of zero"
          f" earners {m.predict(d[zero]).mean():.3f}")
print(f"observed share of zero earners with earnings in 1978 {d.work[zero].mean():.3f}")
m = smf.logit("work ~ earn75 + zero75 + age + education + married", d).fit(disp=0)
ame = dict(zip(m.params.index[1:], m.get_margeff().margeff))
print(f"with controls: AME of zero75 {ame['zero75']:.3f},"
      f" of earn75 {ame['earn75']:.4f}")
