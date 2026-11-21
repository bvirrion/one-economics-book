"""Synthetic control on simulated data: the same region and twenty donors as the
chapter's listing synth_demo.py (seed 12; two common factors; effect -2 from period 21).
Weights solve min ||y1 - Y0 w||^2 over the pre-periods, w >= 0, sum w = 1 (SLSQP; the
listing's helper is inlined, since chart scripts cannot import the code library).
Writes out/synth.csv (t, treated, synthetic, gap) and out/synth_stats.csv.
Book 5, chapter 3, chart 3.
"""
import numpy as np
import pandas as pd
from figout import write_table
from scipy.optimize import minimize

T, T0, J = 30, 20, 20


def data():
    rng = np.random.default_rng(12)
    f = rng.normal(size=(T, 2)).cumsum(0)
    load = rng.uniform(0, 1, size=(J + 1, 2))
    Y = 10 + f @ load.T + rng.normal(0, 0.3, size=(T, J + 1))
    Y[T0:, 0] -= 2.0
    return Y


def weights(y1, Y0):
    n = Y0.shape[1]
    res = minimize(lambda w: (y1 - Y0 @ w) @ (y1 - Y0 @ w), np.full(n, 1 / n),
                   jac=lambda w: -2 * Y0.T @ (y1 - Y0 @ w), method="SLSQP",
                   bounds=[(0, 1)] * n,
                   constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1,
                                 "jac": lambda w: np.ones(n)}],
                   options={"ftol": 1e-12, "maxiter": 500})
    w = np.clip(res.x, 0, None)
    return w / w.sum()


def tables():
    Y = data()
    w = weights(Y[:T0, 0], Y[:T0, 1:])
    synth = Y[:, 1:] @ w
    chart = pd.DataFrame({"t": np.arange(1, T + 1), "treated": Y[:, 0],
                          "synthetic": synth, "gap": Y[:, 0] - synth})
    pre = chart.gap[:T0]
    stats = pd.DataFrame({"stat": ["rmspe_pre", "gap_post", "donors_used"],
                          "value": [np.sqrt((pre**2).mean()), chart.gap[T0:].mean(),
                                    int((w > 0.005).sum())]})
    return chart, stats


if __name__ == "__main__":
    chart, stats = tables()
    write_table(chart, __file__, "synth")
    write_table(stats, __file__, "synth_stats")
