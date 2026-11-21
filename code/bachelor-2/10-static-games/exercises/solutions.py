"""Worked numbers for the exercises and the problem of Book 4, chapter 10."""

import numpy as np


def iesds(a, b):
    """Surviving row and column indices after iterated strict dominance."""
    r, c = list(range(a.shape[0])), list(range(a.shape[1]))
    changed = True
    while changed:
        changed = False
        for s in r[:]:
            if any(all(a[t, k] > a[s, k] for k in c) for t in r if t != s):
                r.remove(s)
                changed = True
        for s in c[:]:
            if any(all(b[k, t] > b[k, s] for k in r) for t in c if t != s):
                c.remove(s)
                changed = True
    return r, c


def pure_nash(a, b):
    return [
        (i, j)
        for i in range(a.shape[0])
        for j in range(a.shape[1])
        if a[i, j] == a[:, j].max() and b[i, j] == b[i, :].max()
    ]


EX1 = (np.array([[1, 1, 0], [0, 0, 2]]), np.array([[0, 2, 1], [3, 1, 0]]))
EX2 = (
    np.array([[3, 0, 1], [2, 2, 0], [0, 1, 4]]),
    np.array([[3, 2, 0], [0, 2, 1], [1, 0, 4]]),
)
PENNIES = (np.array([[1, -1], [-1, 1]]), np.array([[-1, 1], [1, -1]]))


def cournot(n, big_a=100, c=10):
    q = (big_a - c) / (n + 1)
    return q, n * q, big_a - n * q, (big_a - n * q - c) * q


def public_good(n, y=12):
    """Cobb-Douglas u = ln x + ln G: Nash and efficient totals."""
    g = y / (n + 1)
    return g, n * g, n * y / 2, (n * g) / (n * y / 2)


def vcm(n=4, y=20, a=0.4):
    """Linear public-goods game: payoffs if nobody and if everybody contributes."""
    return y, y - y + a * n * y, a, n * a


def commons(n, big_a=100, c=20, fee=0.0):
    """Effort e_i, value per unit (A - E), cost c + fee: Nash and efficient effort."""
    e = (big_a - c - fee) / (n + 1)
    big_e = n * e
    value = big_a - big_e
    profit_boat = e * (value - c - fee)
    star = (big_a - c) / 2
    return {
        "e": e,
        "E": big_e,
        "value": value,
        "profit_boat": profit_boat,
        "profit_total": big_e * (value - c),
        "E_star": star,
        "profit_star": star * (big_a - star - c),
        "over": big_e / star - 1,
        "fee": (big_a - c) * (n - 1) / (2 * n),
    }


def quota_deviation(n=5, quota=8, big_a=100, c=20):
    """Best effort of one boat when the others keep the quota, and its gain."""
    others = (n - 1) * quota
    e = (big_a - others - c) / 2
    dev = e * (big_a - others - e - c)
    keep = quota * (big_a - n * quota - c)
    return e, dev, keep, dev - keep


def hotelling():
    """Two sellers on [0, 1], uniform buyers: shares at (0.3, 0.6) and at the median."""
    a, b = 0.3, 0.6
    return (a + b) / 2, 1 - (a + b) / 2, 0.5


if __name__ == "__main__":
    print(iesds(*EX1), pure_nash(*EX2), pure_nash(*PENNIES))
    print([cournot(n) for n in (1, 2, 4, 9)])
    print([public_good(n) for n in (2, 3, 4, 10)])
    print(vcm())
    print(commons(2))
    for k, v in commons(5).items():
        print(k, v)
    print(commons(5, fee=32))
    print(quota_deviation(), hotelling())
