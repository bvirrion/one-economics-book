"""Worked numbers of the exercises and weekend problem of b1 ch. 26.

Weekend problem: Brenland's finance minister and a forecast. The output gap without
policy follows y_t = rho y_{t-1} + e_t (quarters, per cent of potential); a shock
e_1 = -5 hits in quarter 1. Policy adds p_t = -theta y_{t-k} to the gap of quarter t,
responding to the gap seen k quarters earlier. Loss: sum of squared gaps, quarters 1-8.
Part III uses Brenland's household survey and its 2025 tax and transfer schedule.
"""

import math

import numpy as np
from country import TAX_BANDS, _tax, load

Q = 8


def gaps(rho, e1=-5.0):
    y = [e1]
    for _ in range(Q - 1):
        y.append(rho * y[-1])
    return [round(v, 4) for v in y]


def with_policy(rho, theta=0.5, k=2):
    y = gaps(rho)
    z = [y[t] - (theta * y[t - k] if t >= k else 0.0) for t in range(Q)]
    return [round(v, 4) for v in z]


def loss(path):
    return round(sum(v * v for v in path), 3)


def disposable(gross, size):
    tax = np.array([_tax(g) for g in gross])
    low = np.where(gross < 12000, 6000 + 1500 * (size - 1), 0)
    tr = low + 1200 * np.maximum(size - 2, 0)
    return gross - tax + tr, tax, tr


def stabilisers(cut=0.10):
    h = load("households")
    g0 = h.gross_income.to_numpy(float)
    s = h["size"].to_numpy()
    work = h.hours.to_numpy() > 0
    g1 = np.where(work, g0 * (1 - cut), g0)
    d0, t0, r0 = disposable(g0, s)
    d1, t1, r1 = disposable(g1, s)
    fall = (g0 - g1).sum()
    return {
        "n_work": int(work.sum()),
        "market_fall": round(fall / len(h), 1),
        "disp_fall": round((d0 - d1).sum() / len(h), 1),
        "offset": round(1 - (d0 - d1).sum() / fall, 3),
        "tax_part": round((t0 - t1).sum() / fall, 3),
        "transfer_part": round((r1 - r0).sum() / fall, 3),
        "bands": TAX_BANDS,
    }


def lagged_cycle(theta, k, period=8):
    """Variance of x_t - theta x_{t-k} relative to x_t for a sine cycle."""
    return round(1 + theta**2 - 2 * theta * math.cos(2 * math.pi * k / period), 3)


def problem():
    out = {}
    for rho in (0.9, 0.6, 0.0):
        y = gaps(rho)
        z2 = with_policy(rho, k=2)
        z1 = with_policy(rho, k=1)
        out[rho] = {
            "none": y,
            "lag2": z2,
            "lag1": z1,
            "loss_none": loss(y),
            "loss_lag2": loss(z2),
            "loss_lag1": loss(z1),
        }
    out["forecast"] = gaps(0.6, e1=-2.0)
    out["stab"] = stabilisers()
    return out


def exercises():
    x, mu, var = -4.0, 1.0, 0.5
    p_ce = -x / mu
    p_opt = -mu * x / (mu**2 + var)

    def el(p):
        return round((x + mu * p) ** 2 + var * p**2, 3)

    return {
        "taylor": 4 + 0.5 * (-1) + 0.5 * (4 - 2) + 2,
        "cycle_k4": lagged_cycle(0.5, 4),
        "cycle_k1": lagged_cycle(0.5, 1),
        "cycle_k2": lagged_cycle(0.5, 2),
        "p_ce": p_ce,
        "p_opt": round(p_opt, 3),
        "loss_ce": el(p_ce),
        "loss_opt": el(p_opt),
        "loss_0": el(0.0),
        "rule": {"rule_q02": 0.2 * 9, "rule_q05": 0.5 * 9, "disc": 4},
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem(), width=100)
    pprint.pprint(exercises())
