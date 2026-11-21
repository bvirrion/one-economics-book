"""Worked numbers of the exercises and weekend problem of b1 ch. 14.

Weekend problem: the grain store of Brenmoor. Harvest price 200 dalens a tonne in
September; interest 0.5% a month; storage 2 dalens a tonne a month. July demand
Q = 400 - P (thousand tonnes). Kestria trade: Brenland import demand 2 (220 - P_B),
Kestria export supply 2 (P_K - 160), transport cost c.
"""


def carry_path(p0=200.0, i=0.005, s=2.0, months=11):
    path = [p0]
    for _ in range(months):
        path.append(path[-1] * (1 + i) + s)
    return path


def trade(c):
    if c >= 60:
        return {"P_K": 160.0, "P_B": 220.0, "Q": 0.0}
    pk = (380 - c) / 2
    return {"P_K": pk, "P_B": pk + c, "Q": 2 * (pk - 160)}


def problem():
    path = carry_path()
    july = path[10]
    q_july = 400 - july
    ceiling = 210.0
    return {
        "path": [round(p, 2) for p in path],
        "premium_july": round(100 * (july / 200 - 1), 2),
        "carry_1pct": round(100 * (1.015**10 - 1), 2),
        "conv_yield": round(1.005 * 200 + 2 - 202, 2),
        "trade10": trade(10),
        "trade30": trade(30),
        "q_july": round(q_july, 2),
        "shortage": round((400 - ceiling) - q_july, 2),
        "queue_cost": round(july - ceiling, 2),
        "queue_hours": round((july - ceiling) / 10, 2),
        "store_loss": round((july - ceiling) * q_july, 1),
        "rent_year": 0.8 * 10000 * 12,
        "value_5": 0.8 * 10000 * 12 / 0.05,
        "value_4": 0.8 * 10000 * 12 / 0.04,
        "value_6": 0.8 * 10000 * 12 / 0.06,
    }


def exercises():
    # ceiling: D = 80 - p, S = p, ceiling 20
    q_c = 20
    dwl = 0.5 * (40 - q_c) * ((80 - q_c) - q_c)
    queue_waste = ((80 - q_c) - 20) * q_c
    # random rationing: the 20 units go to random buyers among the 60 who want one
    value_random = q_c * (80 + 20) / 2
    value_best = q_c * (80 + 60) / 2
    # tariff and quota: D = 120 - 5p, S = 2p, world price 10, tariff 2
    imports_free = (120 - 50) - 20
    imports_tariff = (120 - 60) - 24
    return {
        "full": 4 + 2 * 15,
        "quota_rent": 40 * (14 - 10),
        "ceiling": {"shortage": (80 - 20) - 20, "dwl": dwl, "queue": queue_waste},
        "random_extra": value_best - value_random,
        "tariff": {
            "free": imports_free,
            "imports": imports_tariff,
            "revenue": 2 * imports_tariff,
        },
        "monthly": [round(100 * 1.015**t, 2) for t in range(7)],
        "ratio": (round(1 / 0.06, 2), round(1 / 0.04, 2)),
        "price_change": round(100 * (0.06 / 0.04 - 1), 1),
        "years": [round(100 / y, 2) for y in (6.79, 2.49, 4.23, 2.22)],
    }


if __name__ == "__main__":
    print(problem())
    print(exercises())
