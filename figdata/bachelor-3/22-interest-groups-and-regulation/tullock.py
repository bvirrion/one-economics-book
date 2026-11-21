"""Tullock contests. Symmetric: n risk-neutral players bid for a rent V with win
probability x_i / sum x; each bids (n - 1) V / n^2 and the total is (n - 1) V / n.
Two players with stakes V1, V2: bids V1^2 V2 / (V1 + V2)^2 and V1 V2^2 / (V1 + V2)^2."""


def symmetric_bid(n, v=1.0):
    return (n - 1) * v / n**2


def dissipation(n):
    return (n - 1) / n


def two_player(v1, v2):
    s = (v1 + v2) ** 2
    return v1**2 * v2 / s, v1 * v2**2 / s
