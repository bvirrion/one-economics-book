"""Worked numbers of the exercises and weekend problem of b1 ch. 16.

Weekend problem: the mill town. Labour supply from the valley w = 5 + L/15 (dalens an
hour, L workers); the mill's marginal revenue product 25 - L/15. A second, identical
mill opens in Part IV.
"""


def supply_l(w):
    return 15 * (w - 5)


def demand_l(w):
    return 15 * (25 - w)


def floor_l(wf):
    """Employment under a wage floor wf with one mill."""
    wm = 5 + 100 / 15
    if wf <= wm:
        return 100.0
    return min(supply_l(wf), demand_l(wf))


def problem():
    lc, wc = 150.0, 15.0
    lm = 100.0
    wm = 5 + lm / 15
    mrp_m = 25 - lm / 15
    prof_m = 25 * lm - lm**2 / 30 - wm * lm
    rent_m = 0.5 * lm * (wm - 5)
    total_c = 0.5 * lc * (25 - 5)
    # two mills, each MRP 25 - L_i/15, Cournot in employment
    li = 75.0
    w2 = 5 + 2 * li / 15
    mrp2 = 25 - li / 15
    return {
        "comp": {
            "L": lc,
            "w": wc,
            "elast": 15 * wc / lc,
            "rent": 0.5 * lc * 10,
            "profit": 0.5 * lc * 10,
            "total": total_c,
        },
        "mono": {
            "L": lm,
            "w": round(wm, 2),
            "mrp": round(mrp_m, 2),
            "markdown": round(mrp_m / wm - 1, 3),
            "elast": round(15 * wm / lm, 2),
            "profit": round(prof_m, 1),
            "rent": round(rent_m, 1),
            "dwl": round(total_c - prof_m - rent_m, 1),
        },
        "floors": {w: floor_l(w) for w in (13, 15, 17, 20)},
        "upper": round(25 - 100 / 15, 2),
        "two": {
            "Li": li,
            "L": 2 * li,
            "w": w2,
            "mrp": mrp2,
            "markdown": round(mrp2 / w2 - 1, 4),
            "elast_i": 15 * w2 / li,
            "comp_w": round(55 / 3, 2),
            "comp_L": 200.0,
        },
    }


def exercises():
    return {
        "vmp16": 4 * 5 / 16**0.5,
        "mono": {"L": 60, "w": 2 + 0.1 * 60, "Lc": 90, "wc": 2 + 0.1 * 90},
        "floor12": (20 - 12) / 0.1,
        "floor13": (20 - 13) / 0.1,
        "markdown4": (0.25, round(1 / 1.25, 2)),
        "derived": -(0.3 * 1 + 0.7 * 2),
        "rental": round(10000 * (0.04 + 0.10) + 0.02 * 10000, 2),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())
