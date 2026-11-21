"""Dynamic panel bias, simulated: the within estimate of persistence against the panel length.

y_it = a_i + rho y_i,t-1 + u_it, rho = 0.5, 500 units, a_i ~ N(0,1), u ~ N(0,1), a burn-in
of 50 periods; the within (fixed-effects) estimate of rho, averaged over 200 panels, for
T = 3, ..., 30 periods used. The approximation rho - (1 + rho)/(T - 1) is written beside it.
Writes out/nickell.csv: T, estimate, approx.
Book 5, chapter 2, chart 2.
"""
import numpy as np
import pandas as pd
from figout import write_table

RHO, N, REPS, BURN = 0.5, 500, 200, 50
TS = [3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30]


def within_rho(T, rng):
    a = rng.normal(size=N)
    y = a / (1 - RHO) + rng.normal(size=N) / np.sqrt(1 - RHO**2)
    path = []
    for s in range(BURN + T + 1):
        y = a + RHO * y + rng.normal(size=N)
        if s >= BURN:
            path.append(y)
    Y = np.array(path).T                    # N x (T + 1)
    yt, yl = Y[:, 1:], Y[:, :-1]
    yt = yt - yt.mean(1, keepdims=True)
    yl = yl - yl.mean(1, keepdims=True)
    return (yl * yt).sum() / (yl * yl).sum()


def table():
    rng = np.random.default_rng(81)
    rows = []
    for T in TS:
        est = np.mean([within_rho(T, rng) for _ in range(REPS)])
        rows.append((T, est, RHO - (1 + RHO) / (T - 1)))
    return pd.DataFrame(rows, columns=["T", "estimate", "approx"])


if __name__ == "__main__":
    write_table(table(), __file__, "nickell")
