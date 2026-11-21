"""Worked numbers for the text, exercises and problem of Book 4, chapter 26.

Matching m = A u**ETA v**(1 - ETA); theta = v / u; f = A theta**(1 - ETA),
q = A theta**-ETA; job creation and Nash wage give
(1 - beta) (p - z) / (r + s + beta f) = c / q.
"""

from math import sqrt


def steady_u(s, f):
    return s / (s + f)


def matches(a, u, v, eta=0.5):
    m = a * u**eta * v ** (1 - eta)
    return m, v / u, m / u, m / v


def wage(beta, z, p, c, theta):
    return (1 - beta) * z + beta * (p + c * theta)


def tightness(p, z, a, beta, c, r, s):
    """Closed form for eta = 0.5: c beta a x**2 + c (r + s) x - (1 - beta)(p - z) a = 0,
    with x = theta**0.5."""
    qa, qb, qc = c * beta * a, c * (r + s), -(1 - beta) * (p - z) * a
    x = (-qb + sqrt(qb**2 - 4 * qa * qc)) / (2 * qa)
    return x**2


def outcome(p, z, a, beta, c, r, s):
    theta = tightness(p, z, a, beta, c, r, s)
    f, q = a * theta**0.5, a * theta**-0.5
    u = steady_u(s, f)
    return {
        "theta": theta,
        "f": f,
        "q": q,
        "u": u,
        "v": theta * u,
        "w": wage(beta, z, p, c, theta),
        "x": theta**0.5,
    }


def elasticity(p, z, beta, f, r, s, eta=0.5):
    """d ln theta / d ln p from the job-creation condition."""
    return (p / (p - z)) / (eta + (1 - eta) * beta * f / (r + s + beta * f))


LISTING = {"a": 0.7, "c": 1.0, "r": 0.004, "s": 0.03}
BRENLAND = {"p": 1.0, "z": 0.6, "a": 0.6, "beta": 0.5, "c": 0.5, "r": 0.01, "s": 0.05}
