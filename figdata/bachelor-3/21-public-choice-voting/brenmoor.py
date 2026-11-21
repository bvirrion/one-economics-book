"""Brenmoor votes on a pool (weekend problem). Assumptions of the problem: a pool of
q lanes costs each household 20 q dalens a year; a household of n members values it
at 60 n ln(q); the reversion point of the council's proposal is the old pool of 2
lanes; a linear income tax t finances an equal transfer with a deadweight cost
(a/2) t^2 mean income, a = 0.5; the neighbouring town's tax is 500 dalens a year
higher for the same services, capitalised at 4 %."""
import numpy as np
from scipy.optimize import brentq

COST, VALUE, REVERSION = 20.0, 60.0, 2.0
A_DWL = 0.5
TAX_GAP, RATE = 500.0, 0.04


def ideal(n):
    return VALUE * n / COST


def utility(q, n):
    return VALUE * n * np.log(q) - COST * q


def setter(n, q0=REVERSION):
    """Largest pool the voter with n members accepts against the reversion q0."""
    u0 = utility(q0, n)
    return brentq(lambda q: utility(q, n) - u0, ideal(n), 100 * ideal(n))


def mr_rate(median, mean, a=A_DWL):
    return max(0.0, (1 - median / mean) / a)


def capitalisation(gap=TAX_GAP, rate=RATE):
    return gap / rate
