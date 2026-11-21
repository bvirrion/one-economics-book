"""Worked numbers of the exercises and weekend problem of b1 ch. 25.

Weekend problem: Kestria's disinflation. pi_t = pi_e - beta (u_t - un), beta = 0.5,
un = 5, adaptive expectations pi_e = pi_{t-1}; Okun: output gap = -2 (u - un), in per
cent. Inflation is brought from 10 to 4.
"""

BETA, UN, OKUN = 0.5, 5.0, 2.0


def path(targets, pi0=10.0, credible_jump=0.0):
    """Unemployment needed each year to reach the inflation targets; a credible
    announcement lowers expected inflation by credible_jump in the first year."""
    pis, us = [], []
    prev = pi0
    for k, tgt in enumerate(targets):
        pe = prev - (credible_jump if k == 0 else 0.0)
        u = UN + (pe - tgt) / BETA
        us.append(round(u, 3))
        pis.append(tgt)
        prev = tgt
    excess = sum(u - UN for u in us)
    return {
        "u": us,
        "pi": pis,
        "excess": round(excess, 3),
        "output_loss": round(OKUN * excess, 3),
    }


def problem():
    cold = path([4, 4, 4])
    grad = path([9, 8, 7, 6, 5, 4])
    two = path([7, 4])
    cred = path([4], credible_jump=4.0)
    return {
        "cold": cold,
        "grad": grad,
        "two": two,
        "cred": cred,
        "sacrifice": round(cold["output_loss"] / 6, 3),
        "saving": round(cold["excess"] - cred["excess"], 3),
        "hold7": [round(10 + BETA * 2 * k, 1) for k in range(1, 6)],
        "un_check": UN,
    }


def exercises():
    y = 10000 + 2000 * (1.05 - 1)
    pi = 3 - 0.5 * (4 - 5)
    p5 = []
    prev = 3.0
    for _ in range(5):
        prev = prev - 0.5 * (-1)
        p5.append(prev)
    return {
        "y": y,
        "pi": pi,
        "gap": -2 * 1,
        "path": p5,
        "excess": (10 - 4) / 0.5,
        "loss": 2 * (10 - 4) / 0.5,
        "ratio": 2 * (10 - 4) / 0.5 / 6,
        "un_hat": round(2.853 / 0.47, 2),
        "supply_u": 2 / 0.5,
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())
