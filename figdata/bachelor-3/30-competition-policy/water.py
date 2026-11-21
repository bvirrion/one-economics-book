"""Brenland's water company (weekend problem). Daily demand Q = 100 - P (thousand
cubic metres a day; P in dalens per cubic metre, so revenue is in thousand dalens).
Output Q = sqrt(K L) with capital and labour each costing 10 a unit, so marginal cost
is 20; fixed cost 600. Under rate-of-return regulation the firm must supply 60 at the
demand price and may earn revenue up to labour and fixed costs plus s = 12 per unit of
capital. A price cap starts at the average-cost price; the firm can lower its
marginal cost from 20 to 16 by an effort costing 150 a day."""
import numpy as np
from scipy.optimize import brentq

A, F, C, W, R, S = 100.0, 600.0, 20.0, 10.0, 10.0, 12.0


def monopoly(c=C):
    q = (A - c) / 2
    p = A - q
    return {"q": q, "p": p, "profit": (p - c) * q - F, "cs": q * q / 2}


def average_cost(c=C):
    q = ((A - c) + np.sqrt((A - c) ** 2 - 4 * F)) / 2
    return {"q": q, "p": A - q, "cs": q * q / 2, "dwl": (A - c - q) ** 2 / 2}


def marginal_cost(c=C):
    q = A - c
    return {"q": q, "p": c, "cs": q * q / 2, "loss": F}


def aj(q=60.0):
    """Rate-of-return regulation with output fixed at q, sold at the demand price.
    Allowed revenue is labour plus fixed cost plus S per unit of capital; profit is
    then (S - R) K, so the firm takes the largest K for which revenue covers
    W L + F + S K with L = q^2 / K."""
    rev = (A - q) * q
    # S K^2 - (rev - F) K + W q^2 <= 0: the larger root
    b = rev - F
    k = (b + np.sqrt(b * b - 4 * S * W * q * q)) / (2 * S)
    lab = q * q / k
    return {"q": q, "p": A - q, "k": k, "l": lab, "kl": k / lab,
            "cost": W * lab + R * k, "mincost": 2 * np.sqrt(W * R) * q,
            "profit": rev - W * lab - R * k - F,
            "profit_min": rev - 2 * np.sqrt(W * R) * q - F}


def cap(x, c, effort):
    p = average_cost()["p"] - x
    q = A - p
    return {"p": p, "q": q, "profit": (p - c) * q - F - effort, "cs": q * q / 2}


def sharing_x():
    """The X at which consumers and the firm gain equally from the cost cut, measured
    against the average-cost price with the old cost (effort cost counted)."""
    base = average_cost()

    def gap(x):
        s = cap(x, 16.0, 150.0)
        return (s["cs"] - base["cs"]) - s["profit"]
    return brentq(gap, 0.0, 10.0)
