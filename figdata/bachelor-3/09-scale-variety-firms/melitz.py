"""Melitz model with Pareto productivity (minimum 1, shape k): closed-form cut-offs.

Free entry: f_e = sum over markets of f_m (phi*/phi_m)^k (sigma-1)/(k-sigma+1) phi*^-k.
Export cut-off: phi_x = phi* tau (f_x/f)^(1/(sigma-1)).
"""


def cutoffs(sigma, k, f, f_e, tau=None, f_x=None):
    """Return (domestic cut-off, export cut-off or None)."""
    extra = 0.0 if tau is None else tau ** -k * (f / f_x) ** (k / (sigma - 1) - 1)
    d = (f * (sigma - 1) / ((k - sigma + 1) * f_e) * (1 + extra)) ** (1 / k)
    x = None if tau is None else d * tau * (f_x / f) ** (1 / (sigma - 1))
    return d, x


def revenue(phi, sigma, f, d, tau=None, x=None):
    """Revenue of a firm of productivity phi >= d; exporters add tau^(1-sigma)."""
    r = sigma * f * (phi / d) ** (sigma - 1)
    if x is not None and phi >= x:
        r *= 1 + tau ** (1 - sigma)
    return r
