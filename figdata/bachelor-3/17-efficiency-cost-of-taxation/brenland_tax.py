"""Brenland's income tax and the weekend problem. Households of country.load
("households"), 2025 tax bands of country.TAX_BANDS. The upper bands are the
income above 40,000 dalens (taxed at 35 % to 100,000 and 45 % above)."""
import numpy as np
from country import TAX_BANDS, load

THRESHOLD = 40_000
ETI = 0.25
VAT_RATE, VAT_MCPF = 0.18, 1.25
PROJECT_RETURN = 1.5


def tax(g):
    t = 0.0
    for (lo, r), nxt in zip(TAX_BANDS, TAX_BANDS[1:] + [(float("inf"), 0)]):
        if g > lo:
            t += (min(g, nxt[0]) - lo) * r
    return t


def marginal(g):
    m = 0.0
    for lo, r in TAX_BANDS:
        if g > lo:
            m = r
    return m


def upper():
    h = load("households")
    z = h.gross_income[h.gross_income > THRESHOLD].to_numpy(dtype=float)
    return z, np.array([marginal(x) for x in z])


def mcpf_upper(e=ETI, z=None, rates=None):
    """Raise every marginal rate above the threshold by d tau: the mechanical gain
    is d tau sum(z - T); the behavioural loss is e d tau sum(tau z / (1 - tau))."""
    if z is None:
        z, rates = upper()
    mech = (z - THRESHOLD).sum()
    beh = e * (rates * z / (1 - rates)).sum()
    return mech, beh, mech / (mech - beh)


def pareto_a(z=None):
    if z is None:
        z, _ = upper()
    return z.mean() / (z.mean() - THRESHOLD)
