"""Weak instruments: 2SLS drifts toward OLS and its t-test lies (2,000 draws)."""
import numpy as np

rng = np.random.default_rng(7)
n, reps, rho = 200, 2000, 0.8           # rho: correlation of the two errors
print("target F   mean F   median 2SLS   mean OLS   rejects b = 0")
for target in (2, 10, 50):
    pi = np.sqrt((target - 1) / n)      # first stage giving E[F] about target
    b_iv, b_ols, f_stat, reject = [], [], [], 0
    for _ in range(reps):
        z = rng.normal(size=n)
        v = rng.normal(size=n)
        u = rho * v + np.sqrt(1 - rho**2) * rng.normal(size=n)
        x = pi * z + v
        y = 0.0 * x + u                 # the true effect is zero
        zc, xc, yc = z - z.mean(), x - x.mean(), y - y.mean()
        b = (zc @ yc) / (zc @ xc)
        e = yc - b * xc
        se = np.sqrt(e @ e / (n - 2) * (zc @ zc)) / abs(zc @ xc)
        p = (zc @ xc) / (zc @ zc)
        r = xc - p * zc
        f_stat.append(p**2 * (zc @ zc) / (r @ r / (n - 2)))
        b_iv.append(b)
        b_ols.append((xc @ yc) / (xc @ xc))
        reject += abs(b / se) > 1.96
    print(f"{target:8d}   {np.mean(f_stat):6.1f}   {np.median(b_iv):11.3f}"
          f"   {np.mean(b_ols):8.3f}   {reject / reps:12.3f}")
