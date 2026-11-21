"""Exercise 11: industry productivity before and after opening (Melitz, simulated).

sigma = 4, Pareto shape k = 5 (minimum 1), f = 1, f_e = 0.5, tau = 1.3, f_x = 1.5.
Industry productivity is the revenue-weighted mean of firms' productivity.
"""
import numpy as np

SIGMA, K, F, F_E, TAU, F_X = 4.0, 5.0, 1.0, 0.5, 1.3, 1.5
phi = np.random.default_rng(11).pareto(K, 100_000) + 1.0


def cutoff(trade):
    """Domestic cut-off from free entry (Pareto closed form)."""
    extra = TAU**-K * (F / F_X) ** (K / (SIGMA - 1) - 1) if trade else 0.0
    return (F * (SIGMA - 1) / ((K - SIGMA + 1) * F_E) * (1 + extra)) ** (1 / K)


def revenue(d, x=None):
    """Revenue of every entrant: zero below the cut-off, plus exports above x."""
    r = np.where(phi >= d, SIGMA * F * (phi / d) ** (SIGMA - 1), 0.0)
    if x is not None:
        r = r * np.where(phi >= x, 1 + TAU ** (1 - SIGMA), 1.0)
    return r


dc, do = cutoff(False), cutoff(True)
dx = do * TAU * (F_X / F) ** (1 / (SIGMA - 1))
rc, ro = revenue(dc), revenue(do, dx)
pc, po = (rc * phi).sum() / rc.sum(), (ro * phi).sum() / ro.sum()
survivors = phi >= do  # firms that produce in both regimes
ps = (rc[survivors] * phi[survivors]).sum() / rc[survivors].sum()
print(f"cut-offs: closed {dc:.3f}, open {do:.3f}, export {dx:.3f}")
print(f"industry productivity: closed {pc:.3f}, open {po:.3f} (+{po / pc - 1:.1%})")
share_exit = (ps - pc) / (po - pc)
print(f"  closed, survivors only {ps:.3f}: exit accounts for {share_exit:.0%}")
print(f"  the rest, {1 - share_exit:.0%}, is market share moving to exporters")
