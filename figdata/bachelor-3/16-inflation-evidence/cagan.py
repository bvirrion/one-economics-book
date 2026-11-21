"""The Cagan model of the weekend problem (Kestria). Real money balances, in percent
of GDP, are m = A exp(-alpha pi), with pi the continuous inflation rate per year;
in a steady state money grows at mu = pi, and seigniorage is s = mu m."""
import numpy as np
from scipy.optimize import brentq

A, ALPHA, DEFICIT = 20.0, 2.0, 3.0


def balances(pi, a=A, alpha=ALPHA):
    return a * np.exp(-alpha * pi)


def seigniorage(mu, a=A, alpha=ALPHA):
    return mu * balances(mu, a, alpha)


def peak(a=A, alpha=ALPHA):
    """Revenue-maximising money growth 1/alpha and the maximum revenue."""
    mu = 1 / alpha
    return mu, seigniorage(mu, a, alpha)


def financing_rates(deficit=DEFICIT, a=A, alpha=ALPHA):
    """The two money-growth rates that raise `deficit` (percent of GDP)."""
    mu_star, s_max = peak(a, alpha)
    if deficit > s_max:
        return None
    f = lambda m: seigniorage(m, a, alpha) - deficit  # noqa: E731
    return brentq(f, 1e-9, mu_star), brentq(f, mu_star, 20 / alpha)


def annual(mu):
    """Continuous rate per year to the annual percent change."""
    return 100 * np.expm1(mu)
