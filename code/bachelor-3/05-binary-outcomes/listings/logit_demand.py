"""Logit demand on a simulated market: 300 towns, four products and an outside option.
Shares come from utility delta_j = 1 + 0.5 x_j - 2 p_j + xi_j and logit taste shocks;
the log-share inversion recovers the price coefficient by OLS."""
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(1994)
T, J, alpha = 300, 4, -2.0
x = rng.uniform(0, 2, (T, J))                 # an observed quality
p = 1 + 0.3 * x + rng.uniform(0, 0.5, (T, J))  # prices, unrelated to xi here
xi = rng.normal(0, 0.3, (T, J))               # quality the economist does not see
delta = 1 + 0.5 * x + alpha * p + xi
s = np.exp(delta) / (1 + np.exp(delta).sum(1, keepdims=True))
s0 = 1 - s.sum(1)

y = (np.log(s) - np.log(s0)[:, None]).ravel()  # ln s_j - ln s_0 = delta_j
fit = sm.OLS(y, sm.add_constant(np.column_stack([x.ravel(), p.ravel()]))).fit()
print(f"price coefficient: true {alpha}, estimated {fit.params[2]:.3f}"
      f" (s.e. {fit.bse[2]:.3f})")

a = fit.params[2]                              # elasticities in town 1
print("shares in town 1:", np.round(s[0], 3), " outside", round(s0[0], 3))
for j in range(J):
    own = a * p[0, j] * (1 - s[0, j])
    cross = [-a * p[0, k] * s[0, k] for k in range(J) if k != j]
    print(f"product {j + 1}: own {own:6.2f}  with respect to each other price",
          " ".join(f"{c:5.2f}" for c in cross))
