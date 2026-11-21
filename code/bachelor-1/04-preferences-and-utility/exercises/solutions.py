"""Worked numbers of the exercises and weekend problem of b1 ch. 4 (preferences and
utility): two flatmates trading milk (litres) and bread (loaves)."""

import math

from scipy.optimize import brentq


def u_ana(m, b):
    return math.sqrt(m * b)


def u_ben(m, b):
    return m + 6 * math.log(b)


def mrs_ana(m, b):
    """Litres of milk per loaf: u_b / u_m."""
    return m / b


def mrs_ben(m, b):
    return 6 / b


BUNDLES = {"P": (4, 2), "Q": (2, 4), "R": (3, 3), "S": (6, 1)}


def rankings():
    return {k: (round(u_ana(*v), 3), round(u_ben(*v), 3)) for k, v in BUNDLES.items()}


def trade(endow_a=(9.0, 1.0), endow_b=(1.0, 7.0)):
    """At a fixed rate r (litres per loaf) Ana buys bread until her MRS is r and Ben
    sells until his is r; the rate at which the two amounts agree."""

    def t_ana(r):
        return (endow_a[0] - r * endow_a[1]) / (2 * r)

    def t_ben(r):
        return endow_b[1] - 6 / r

    r = brentq(lambda x: t_ana(x) - t_ben(x), 0.5, 8.0)
    t = t_ana(r)
    a = (endow_a[0] - r * t, endow_a[1] + t)
    b = (endow_b[0] + r * t, endow_b[1] - t)
    return {
        "r": round(r, 4),
        "t": round(t, 3),
        "milk": round(r * t, 3),
        "ana": tuple(round(v, 3) for v in a),
        "ben": tuple(round(v, 3) for v in b),
        "mrs_a": round(mrs_ana(*a), 4),
        "mrs_b": round(mrs_ben(*b), 4),
        "u_a0": round(u_ana(*endow_a), 3),
        "u_a1": round(u_ana(*a), 3),
        "u_b0": round(u_ben(*endow_b), 3),
        "u_b1": round(u_ben(*b), 3),
        "mrs_a0": mrs_ana(*endow_a),
        "mrs_b0": round(mrs_ben(*endow_b), 3),
        "swap_a": round(u_ana(7, 2), 3),
        "swap_b": round(u_ben(3, 6), 3),
    }


def ex_mrs_cd(x1=1.0, x2=1.0, a=0.3):
    return (a / (1 - a)) * (x2 / x1)


if __name__ == "__main__":
    print(rankings())
    print(trade())
    print(ex_mrs_cd())
