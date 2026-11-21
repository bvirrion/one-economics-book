"""Random effects against fixed effects, when the unit effect is and is not
correlated with the regressor (a simulated panel, true slope 1)."""
import numpy as np

rng = np.random.default_rng(3)
n, t = 500, 6


def estimates(link):
    a = rng.normal(0, 1, n)                        # unit effect
    x = link * a[:, None] + rng.normal(0, 1, (n, t))
    y = 1.0 * x + a[:, None] + rng.normal(0, 1, (n, t))
    xw = x - x.mean(1, keepdims=True)              # within transform
    yw = y - y.mean(1, keepdims=True)
    fe = (xw * yw).sum() / (xw * xw).sum()
    e = yw - fe * xw
    s2_u = (e * e).sum() / (n * (t - 1) - 1)       # variance of u
    xb, yb = x.mean(1), y.mean(1)
    bb = np.cov(xb, yb)[0, 1] / np.var(xb, ddof=1)
    s2_bar = np.var(yb - bb * xb, ddof=2)          # variance of a + mean u
    theta = 1 - np.sqrt(s2_u / (t * s2_bar))
    xq = x - theta * x.mean(1, keepdims=True)      # quasi-demeaning
    yq = y - theta * y.mean(1, keepdims=True)
    xq, yq = xq - xq.mean(), yq - yq.mean()
    re = (xq * yq).sum() / (xq * xq).sum()
    return fe, re, theta


print("corr(a, x)   FE      RE      theta")
for link in (0.0, 0.5):
    fe, re, theta = estimates(link)
    corr = link / np.sqrt(link**2 + 1)
    print(f"{corr:8.2f}   {fe:.3f}   {re:.3f}   {theta:.3f}")
