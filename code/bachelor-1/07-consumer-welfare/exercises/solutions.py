"""Worked numbers of the exercises and weekend problem of b1 ch. 7.

The weekend problem uses the printed Brenland basket (figdata 07-consumer-welfare,
brenland_basket.csv and brenland_indices.csv): 2015 spending by good, the price
relatives 2015-2025 to four decimals, and the indices to two decimals.
"""

import math

SPEND = {"bread": 600, "clothing": 800, "energy": 750, "rent": 8400, "transport": 300}
QTY = {"bread": 300, "clothing": 20, "energy": 3000, "rent": 12, "transport": 100}
P25 = {
    "bread": 2.71,
    "clothing": 49.0,
    "energy": 0.46,
    "rent": 1000.14,
    "transport": 3.91,
}
REL = {
    "bread": 1.355,
    "clothing": 1.225,
    "energy": 1.84,
    "rent": 1.4288,
    "transport": 1.3033,
}
# printed indices, 2016..2025: laspeyres, geometric
LASP = [102.78, 104.91, 107.25, 109.32, 111.66, 115.91, 127.68, 134.93, 139.97, 143.46]
GEOM = [102.78, 104.9, 107.24, 109.31, 111.63, 115.87, 127.31, 134.54, 139.51, 142.97]
CHAIN25 = 143.27
PENSION = 15000


def indices():
    total = sum(SPEND.values())
    cost25 = sum(QTY[g] * P25[g] for g in QTY)
    harm = sum(SPEND[g] / REL[g] for g in SPEND)
    geo = math.exp(sum(SPEND[g] / total * math.log(REL[g]) for g in SPEND))
    return {
        "total": total,
        "cost25": round(cost25, 2),
        "lasp": round(100 * cost25 / total, 2),
        "harm": round(harm, 2),
        "paasche": round(100 * total / round(harm, 2), 2),
        "geo": round(100 * geo, 2),
    }


def growth(level, years=10):
    return round(100 * ((level / 100) ** (1 / years) - 1), 2)


def new_good(a=60, b=2, p25=10, p20=20):
    """Linear demand q = a - b p for phone data; consumer surplus at two prices."""
    choke = a / b
    cs25 = (choke - p25) * (a - b * p25) / 2
    cs20 = (choke - p20) * (a - b * p20) / 2
    e_old = round(10850 * GEOM[-1] / 100, 2)
    e_new = round(e_old - cs25, 2)
    idx = round(100 * e_new / 10850, 2)
    return {
        "choke": choke,
        "q25": a - b * p25,
        "cs25": cs25,
        "cs20": cs20,
        "share": round(100 * cs25 / 15565.68, 2),
        "e_old": e_old,
        "e_new": e_new,
        "idx": idx,
        "g_new": growth(idx),
        "g_geo": growth(GEOM[-1]),
    }


def pension():
    over = [round(PENSION * (la - ge) / 100, 2) for la, ge in zip(LASP, GEOM)]
    return {
        "lasp": round(PENSION * LASP[-1] / 100, 2),
        "geo": round(PENSION * GEOM[-1] / 100, 2),
        "gap25": over[-1],
        "cum": round(sum(over), 2),
        "chain": round(PENSION * CHAIN25 / 100, 2),
        "chain_gap": round(PENSION * (LASP[-1] - CHAIN25) / 100, 2),
    }


def exercises():
    m, a = 1000, 0.5
    return {
        "cs_loss": 5 * (80 + 70) / 2,
        "cv": round(m * (2**a - 1), 2),
        "ev": round(m * (1 - 2**-a), 2),
        "cs": round(a * m * math.log(2), 2),
        "true": round(2**a, 4),
        "lasp": (2 * 500 + 500) / 1000,
        "L2": (2 * 10 + 1 * 10) / 20,
        "P2": (2 * 6 + 1 * 12) / (6 + 12),
    }


if __name__ == "__main__":
    print(indices())
    print(new_good())
    print(pension())
    print(exercises())
