"""The Grossman--Stiglitz equilibrium as the cost of information varies, chapter 8.

A model chart, no data. Asset value v = theta + eps; informed traders see theta;
noise supply z. Variances s_theta^2 = s_eps^2 = 1, risk aversion a = 1, noise
standard deviation s_z = 0.25. With informed share phi the price reveals
w = theta - (a s_eps^2 / phi) z; the equilibrium share makes informed and
uninformed traders equally well off: Var(theta | w) = (exp(2 a c) - 1) s_eps^2.
Writes
  out/gs.csv          cost c, informed share phi (capped at 1), residual variance
                      of theta given the price, as a share of its prior variance
  out/gs_points.csv   the same at c = 0.05, 0.1116 and 0.2
"""

import numpy as np
import pandas as pd
from figout import write_table

S_THETA2, S_EPS2, A, S_Z = 1.0, 1.0, 1.0, 0.25


def residual_var(phi):
    """Var(theta | price) when a share phi of traders is informed."""
    if phi == 0:
        return S_THETA2
    su2 = (A * S_EPS2 / phi) ** 2 * S_Z**2
    return S_THETA2 * su2 / (S_THETA2 + su2)


def share(c):
    """Equilibrium informed share at cost c (1 if everyone buys, 0 if no one)."""
    k = np.exp(2 * A * c) - 1
    target = k * S_EPS2
    if target >= S_THETA2:
        return 0.0
    su2 = target * S_THETA2 / (S_THETA2 - target)
    return float(min(1.0, A * S_EPS2 * S_Z / np.sqrt(su2)))


def table():
    cs = np.round(np.arange(0.01, 0.401, 0.005), 3)
    phis = [share(c) for c in cs]
    return pd.DataFrame(
        {
            "c": cs,
            "phi": np.round(phis, 4),
            "resid": [round(residual_var(p) / S_THETA2, 4) for p in phis],
        }
    )


def points():
    cs = [0.05, 0.1116, 0.2]
    phis = [share(c) for c in cs]
    return pd.DataFrame(
        {
            "c": cs,
            "phi": np.round(phis, 4),
            "resid": [round(residual_var(p), 4) for p in phis],
        }
    )


if __name__ == "__main__":
    write_table(table(), __file__, "gs")
    write_table(points(), __file__, "gs_points")
