"""Worked numbers of the exercises and weekend problem of b1 ch. 5 (consumer choice).

The weekend problem uses the printed, rounded fit of the Brenland survey (figdata
05-consumer-choice/out/brenland_fit.csv): food = 3334 + 0.056 c, log slope 0.31,
aggregate food share 0.199; the poorest tenth spends 11639 in all and 3726 on food,
the richest 42736 and 5594.
"""

A, B, SHARE, LOGSLOPE = 3334, 0.056, 0.199, 0.31
POOR, RICH = (11639, 3726), (42736, 5594)


def cd_demand(a, p1, p2, m):
    return a * m / p1, (1 - a) * m / p2


def complements(p1, p2, m):
    """u = min(x1, 3 x2): x1 = 3 x2 on the budget line."""
    x2 = m / (3 * p1 + p2)
    return 3 * x2, x2


def quasi(p1, m):
    """u = 4 sqrt(x1) + x2, p2 = 1: interior x1 = 4 / p1**2 if affordable."""
    x1 = 4 / p1**2
    if p1 * x1 <= m:
        return x1, m - p1 * x1
    return m / p1, 0.0


def gamma():
    return round(A / (1 - B))


def sg_food(c):
    return round(A + B * c)


def problem():
    c_poor, f_poor = POOR
    c_rich, f_rich = RICH
    c_new = round(1.1 * c_poor)
    f_log = round(f_poor * (1 + LOGSLOPE * 0.10))
    out = {
        "cd_poor": round(SHARE * c_poor),
        "cd_rich": round(SHARE * c_rich),
        "sg_poor": sg_food(c_poor),
        "sg_rich": sg_food(c_rich),
        "c_new": c_new,
        "f_log": f_log,
        "s_log": round(f_log / c_new, 3),
        "sg_new": sg_food(c_new),
        "f_cd": round(f_poor * 1.1),
        "f_sg_obs": round(f_poor + B * (c_new - c_poor)),
    }
    out["s_sg_poor"] = round(out["sg_poor"] / c_poor, 3)
    out["s_sg_rich"] = round(out["sg_rich"] / c_rich, 3)
    out["eta_poor"] = round(B * c_poor / out["sg_poor"], 3)
    out["eta_rich"] = round(B * c_rich / out["sg_rich"], 3)
    out["s_sg_new"] = round(out["sg_new"] / c_new, 3)
    out["s_sg_obs"] = round(out["f_sg_obs"] / c_new, 3)
    return out


if __name__ == "__main__":
    print(
        cd_demand(0.25, 2, 5, 100), complements(2, 1, 70), quasi(0.5, 20), quasi(0.5, 5)
    )
    print(gamma(), problem())
