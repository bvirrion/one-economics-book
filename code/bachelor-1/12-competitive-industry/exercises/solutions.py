"""Worked numbers of the exercises and weekend problem of b1 ch. 12.

Weekend problem: a Brenland fishery. Each boat has C(q) = 50 + 2 q**2 (thousand
dalens a year, q tonnes); demand for fish Q = 3000 - 50 p (p in thousand dalens a
tonne).
"""


def capped(n, a=3000.0, b=50.0):
    p = a / (n / 4 + b)
    q = p / 4
    profit = p * q - 50 - 2 * q**2
    return {
        "p": p,
        "q": q,
        "Q": n * q,
        "profit": profit,
        "ac": 50 / q + 2 * q,
        "quasi_rent": p * q - 2 * q**2,
    }


def r(d, k=2):
    return {key: round(val, k) for key, val in d.items()}


def problem():
    cap = capped(200)
    rent = cap["profit"]
    annuity = (1 - 1.04**-10) / 0.04
    cs_cap = 0.5 * cap["Q"] * (60 - cap["p"])
    cs_free = 0.5 * 2000 * (60 - 20)
    return {
        "free_p": 20.0,
        "free_Q": 3000 - 50 * 20,
        "free_boats": (3000 - 50 * 20) / 5,
        "boats_high_demand": (3500 - 50 * 20) / 5,
        "cap": r(cap),
        "licence_4": round(rent / 0.04, 1),
        "licence_25": round(rent / 0.025, 1),
        "annuity": round(annuity, 4),
        "licence_10y": round(rent * annuity, 2),
        "cs_cap": cs_cap,
        "cs_free": cs_free,
        "rents_total": 200 * rent,
        "net_gain": cs_free - cs_cap - 200 * rent,
    }


def exercises():
    n240 = capped(240)
    return {
        "lr_firms": (1000 - 10 * 20) / 10,
        "land_rent": 0.5 * 1000 * 10,
        "quasi": (24 * 6 - 2 * 36, 24 * 6 - 2 * 36 - 50),
        "licence": 40000 / 0.05,
        "n240": r(n240),
        "licence_240": round(n240["profit"] / 0.04, 1),
        "fall_240": round(1 - n240["profit"] / capped(200)["profit"], 3),
    }


if __name__ == "__main__":
    print(problem())
    print(exercises())
