"""Exercise 10: the weak-instrument experiment at a first-stage F of 5."""
import numpy as np

rng = np.random.default_rng(10)
n, reps, rho, target = 200, 4000, 0.8, 5
pi = np.sqrt((target - 1) / n)
z = rng.normal(size=(reps, n))
v = rng.normal(size=(reps, n))
u = rho * v + np.sqrt(1 - rho**2) * rng.normal(size=(reps, n))
x = pi * z + v
y = u                                       # true effect zero
zc, xc, yc = (a - a.mean(1, keepdims=True) for a in (z, x, y))
zx, zy, zz = (zc * xc).sum(1), (zc * yc).sum(1), (zc * zc).sum(1)
b = zy / zx
e = yc - b[:, None] * xc
se = np.sqrt((e * e).sum(1) / (n - 2) * zz) / np.abs(zx)
p = zx / zz
r = xc - p[:, None] * zc
f = p**2 * zz / ((r * r).sum(1) / (n - 2))
ols = (xc * yc).sum(1) / (xc * xc).sum(1)
print(f"mean first-stage F        {f.mean():.2f}")
print(f"median 2SLS               {np.median(b):.3f}")
print(f"mean OLS                  {ols.mean():.3f}")
print(f"median 2SLS / mean OLS    {np.median(b) / ols.mean():.3f}")
print(f"rejects b = 0 at 5%       {np.mean(np.abs(b / se) > 1.96):.3f}")
print(f"share of draws with F>10  {np.mean(f > 10):.3f}")
strong = f > 10
print(f"median 2SLS if F>10       {np.median(b[strong]):.3f}")
print(f"median 2SLS if F<=10      {np.median(b[~strong]):.3f}")
