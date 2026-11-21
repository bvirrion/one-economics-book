"""Brenland's unemployment fund (weekend problem). Assumptions of the problem: the
consumption drop on becoming unemployed falls with the replacement rate r as
drop(r) = 0.24 - 0.28 r; relative risk aversion 3; elasticity of unemployment
duration with respect to the benefit 0.4; a balanced fund."""
import numpy as np
from scipy.optimize import brentq

DROP0, DROP_SLOPE = 0.24, 0.28
GAMMA, ELASTICITY = 3.0, 0.4
R_NOW = 0.60


def drop(r):
    return DROP0 - DROP_SLOPE * r


def contribution(r, u):
    """Balanced fund: t (1 - u) = r u, contributions and benefits as shares of
    the wage."""
    return r * u / (1 - u)


def gain(r, gamma=GAMMA):
    """Left side of the Baily-Chetty condition, CRRA marginal utilities exact."""
    return (1 - drop(r)) ** (-gamma) - 1


def cost(u, eps=ELASTICITY):
    return eps / (1 - u)


def optimum(u, gamma=GAMMA, eps=ELASTICITY, exact=False):
    if exact:
        return brentq(lambda r: gain(r, gamma) - cost(u, eps), 0, DROP0 / DROP_SLOPE)
    return (DROP0 - cost(u, eps) / gamma) / DROP_SLOPE


def curve(u):
    r = np.linspace(0, 0.85, 86)
    return r, gamma_drop(r), np.full_like(r, cost(u))


def gamma_drop(r, gamma=GAMMA):
    return gamma * drop(r)
