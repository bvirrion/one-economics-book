"""Worked numbers of the exercises and weekend problem of b1 ch. 1 (Models and Data).

Each function returns the numbers a solution prints, computed along the rounded
path the solution follows.
"""

import math

import numpy as np
import pandas as pd
from country import load


def ex_growth_per_worker(gy=0.03, gl=0.01):
    """Exercise 2: growth of Y/L, continuous (difference) and discrete (exact ratio)."""
    return {"continuous": gy - gl, "discrete": (1 + gy) / (1 + gl) - 1}


def ex_brenland_real_growth():
    """Exercise 3: Brenland real GDP 2015-2025 from nominal GDP and the deflator."""
    a = load("accounts").set_index("year")
    real_2025 = a.loc[2025, "gdp"] / (a.loc[2025, "deflator"] / 100)
    g_nom = math.log(a.loc[2025, "gdp"] / a.loc[2015, "gdp"]) / 10
    g_real = math.log(real_2025 / a.loc[2015, "gdp"]) / 10
    g_defl = math.log(a.loc[2025, "deflator"] / 100) / 10
    return {
        "gdp_2015": a.loc[2015, "gdp"],
        "gdp_2025": a.loc[2025, "gdp"],
        "deflator_2025": a.loc[2025, "deflator"],
        "real_2025": round(real_2025),
        "table_real_2025": a.loc[2025, "real_gdp"],
        "g_nom": round(100 * g_nom, 2),
        "g_real": round(100 * g_real, 2),
        "g_defl": round(100 * g_defl, 2),
    }


def ex_real_growth_high_inflation(gn=0.50, pi=0.40):
    """Exercise 5: exact and approximate real growth."""
    return {
        "exact": (1 + gn) / (1 + pi) - 1,
        "approx": gn - pi,
        "log": math.log(1 + gn) - math.log(1 + pi),
    }


def ex_doubling(g=0.02):
    """Exercise 6: doubling time at a continuous rate g and at a yearly rate g."""
    return {
        "continuous": math.log(2) / g,
        "yearly": math.log(2) / math.log(1 + g),
        "rule70": 70 / (100 * g),
    }


def cloud_slope(b, d, vd, vs, cov=0.0):
    """Least-squares slope of q on p, shifting-curves model (exercises 7, 10)."""
    return (d * vd - b * vs + (b - d) * cov) / (vd + vs - 2 * cov)


def simulate_cloud_slope(b, d, vd, vs, cov, n=400_000, seed=7):
    """Check of exercise 10 by simulation."""
    rng = np.random.default_rng(seed)
    u = rng.multivariate_normal([0, 0], [[vd, cov], [cov, vs]], n)
    p = (u[:, 0] - u[:, 1]) / (b + d)
    q = d * p + u[:, 1]
    return np.polyfit(p, q, 1)[0]


def ex_shifter_both(alpha, gamma, b, d):
    """Exercise 11: a shifter moves demand by alpha and supply by gamma."""
    dp = (alpha - gamma) / (b + d)
    dq = (d * alpha + b * gamma) / (b + d)
    return {"dp": dp, "dq": dq, "ratio": dq / dp}


def problem_cold_store(s1=50.0, catch=(110, 95, 120), sold=(99, 99, 80), delta=0.02):
    """Weekend problem, part I: the cold store S_{t+1} = (1 - delta) S_t + C_t - Q_t."""
    s = [s1]
    for c, q in zip(catch, sold):
        s.append(round((1 - delta) * s[-1] + c - q, 1))
    return s


def problem_real_price(p_now=8.50, p_before=7.90, cpi_before=None, cpi_now=None):
    """Weekend problem, part II: fish price, nominal and real change, 2024 to 2025."""
    a = load("accounts").set_index("year")
    cpi_before = cpi_before or a.loc[2024, "cpi"]
    cpi_now = cpi_now or a.loc[2025, "cpi"]
    nominal = p_now / p_before - 1
    inflation = cpi_now / cpi_before - 1
    real_price_2025 = p_now / (cpi_now / cpi_before)
    return {
        "cpi_2024": cpi_before,
        "cpi_2025": cpi_now,
        "nominal": round(100 * nominal, 1),
        "inflation": round(100 * inflation, 1),
        "real_exact": round(100 * ((1 + nominal) / (1 + inflation) - 1), 1),
        "real_approx": round(100 * nominal, 1) - round(100 * inflation, 1),
        "real_price_2025_in_2024_dalens": round(real_price_2025, 2),
    }


def problem_fish():
    """Weekend problem, parts III-IV: means from the printed sums (prices to 4 decimals,
    crates to 2), then the ratios of differences and the elasticity at the means."""
    root = __file__.split("/code/")[0]
    g = pd.read_csv(f"{root}/figdata/bachelor-1/01-models-and-data/out/fish_groups.csv")
    m = {
        k: (round(r.sum_price / r.days, 4), round(r.sum_crates / r.days, 2))
        for k, (_, r) in zip(["calm", "storm", "fest"], g.iterrows())
    }
    n = g.days.sum()
    m["all"] = (round(g.sum_price.sum() / n, 4), round(g.sum_crates.sum() / n, 2))
    (pc, qc), (ps, qs), (pf, qf) = m["calm"], m["storm"], m["fest"]
    slope_storm = round((qs - qc) / (ps - pc), 2)
    return {
        "means": m,
        "dp_storm": round(ps - pc, 4),
        "dq_storm": round(qs - qc, 2),
        "slope_storm": slope_storm,
        "slope_fest": round((qf - qc) / (pf - pc), 2),
        "elasticity": round(slope_storm * m["all"][0] / m["all"][1], 2),
        "elasticity_true": round(-10 * m["all"][0] / m["all"][1], 2),
        "elasticity_cloud": round(-5.32 * m["all"][0] / m["all"][1], 2),
        "arc_storm": round(math.log(qs / qc) / math.log(ps / pc), 2),
        "revenue_calm": round(10 * pc * qc),
        "revenue_storm": round(10 * ps * qs),
    }


if __name__ == "__main__":
    for f in (
        ex_growth_per_worker,
        ex_brenland_real_growth,
        ex_real_growth_high_inflation,
        ex_doubling,
        problem_cold_store,
        problem_real_price,
        problem_fish,
    ):
        print(f.__name__, f())
    print("ex7", cloud_slope(2, 1, 1, 3))
    print("ex10", cloud_slope(2, 1, 1, 3, 1), simulate_cloud_slope(2, 1, 1, 3, 1))
    print("ex11", ex_shifter_both(-10, -30, 10, 10))
