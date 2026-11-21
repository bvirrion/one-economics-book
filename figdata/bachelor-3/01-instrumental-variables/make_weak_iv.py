"""Weak instruments, simulated: the sampling distribution of 2SLS and the size of its t-test.

Model (the same as listing weak_iv.py): n = 200, z ~ N(0,1), x = pi z + v, y = 0 x + u,
corr(u, v) = 0.8, pi chosen so that the expected first-stage F is the target.
Writes
  out/weak_iv_density.csv  mid, f2, f10, f50: histogram densities of 2SLS over 4,000 draws
                           (bins of width 0.05 on [-1, 1.5])
  out/weak_iv_size.csv     F, reject: share of draws whose nominal 5% t-test rejects the
                           true value, for targets F from 1.5 to 100
  out/weak_iv_ols.csv      ols: the mean OLS estimate at target F = 10 (the bias it points to)
Book 5, chapter 1, charts 2 and 3.
"""
import numpy as np
import pandas as pd
from figout import write_table

N, RHO = 200, 0.8
EDGES = np.round(np.arange(-1.0, 1.5001, 0.05), 2)
TARGETS = [1.5, 2, 3, 5, 7, 10, 15, 20, 30, 50, 100]


def simulate(target, reps, seed):
    rng = np.random.default_rng(seed)
    pi = np.sqrt((target - 1) / N)
    z = rng.normal(size=(reps, N))
    v = rng.normal(size=(reps, N))
    u = RHO * v + np.sqrt(1 - RHO**2) * rng.normal(size=(reps, N))
    x = pi * z + v
    y = u
    zc = z - z.mean(1, keepdims=True)
    xc = x - x.mean(1, keepdims=True)
    yc = y - y.mean(1, keepdims=True)
    zx, zy, zz = (zc * xc).sum(1), (zc * yc).sum(1), (zc * zc).sum(1)
    b = zy / zx
    e = yc - b[:, None] * xc
    se = np.sqrt((e * e).sum(1) / (N - 2) * zz) / np.abs(zx)
    ols = (xc * yc).sum(1) / (xc * xc).sum(1)
    return b, se, ols


def tables():
    dens = {"mid": np.round((EDGES[:-1] + EDGES[1:]) / 2, 3)}
    for t, seed in ((2, 21), (10, 22), (50, 23)):
        b, _, _ = simulate(t, 4000, seed)
        h, _ = np.histogram(b, bins=EDGES)
        dens[f"f{t}"] = h / (4000 * 0.05)
    size = []
    for i, t in enumerate(TARGETS):
        b, se, _ = simulate(t, 4000, 100 + i)
        size.append((t, np.mean(np.abs(b / se) > 1.96)))
    _, _, ols = simulate(10, 4000, 22)
    return (pd.DataFrame(dens), pd.DataFrame(size, columns=["F", "reject"]),
            pd.DataFrame({"ols": [ols.mean()]}))


if __name__ == "__main__":
    dens, size, ols = tables()
    write_table(dens, __file__, "weak_iv_density")
    write_table(size, __file__, "weak_iv_size")
    write_table(ols, __file__, "weak_iv_ols")
