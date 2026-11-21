"""Exercise 7: the closed-economy cut-off found from a sample, against the formula.

sigma = 3, Pareto shape k = 6 (minimum 1), fixed cost f = 10, entry cost f_e = 1.
A firm with productivity phi >= phi* earns f ((phi/phi*)^(sigma-1) - 1).
"""
import numpy as np

SIGMA, K, F, F_E = 3.0, 6.0, 10.0, 1.0
phi = np.random.default_rng(7).pareto(K, 1_000_000) + 1.0


def expected_profit(cut):
    """Mean profit of an entrant when firms below `cut` exit."""
    p = np.where(phi >= cut, F * ((phi / cut) ** (SIGMA - 1) - 1), 0.0)
    return p.mean()


lo, hi = 1.0, 10.0
for _ in range(60):  # expected profit falls as the cut-off rises
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if expected_profit(mid) > F_E else (lo, mid)
formula = (F * (SIGMA - 1) / ((K - SIGMA + 1) * F_E)) ** (1 / K)
print(f"cut-off from the sample {lo:.4f}, formula {formula:.4f}")
print(f"share of entrants that produce: sample {np.mean(phi >= lo):.4f}, "
      f"formula {formula**-K:.4f}")
