"""Selection in the Melitz model: 20,000 entrants, before and after opening."""
import numpy as np

SIGMA, K, F, F_E = 3.0, 4.0, 40.0, 2.5  # demand, Pareto shape, fixed costs
TAU, F_X = 1.2, 90.0  # iceberg cost, fixed export cost
phi = np.random.default_rng(2003).pareto(K, 20_000) + 1.0  # productivity


def cutoff(trade):
    """Domestic cut-off: an entrant's expected profit equals the entry cost."""
    extra = TAU**-K * (F / F_X) ** (K / (SIGMA - 1) - 1) if trade else 0.0
    return (F * (SIGMA - 1) / ((K - SIGMA + 1) * F_E) * (1 + extra)) ** (1 / K)


d_closed, d_open = cutoff(False), cutoff(True)
d_export = d_open * TAU * (F_X / F) ** (1 / (SIGMA - 1))
closed, opened = phi >= d_closed, phi >= d_open
exporters = phi >= d_export

print(f"cut-offs: closed {d_closed:.3f}, open {d_open:.3f}, export {d_export:.3f}")
print(f"entrants that produce: closed {closed.mean():.4f} "
      f"(formula {d_closed**-K:.4f}), open {opened.mean():.4f}")
print(f"producers that exit on opening: {1 - opened.sum() / closed.sum():.3f}")
print(f"producers that export: {exporters.sum() / opened.sum():.3f}")
print(f"mean productivity of producers: closed {phi[closed].mean():.3f}, "
      f"open {phi[opened].mean():.3f}")
