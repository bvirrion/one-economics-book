"""Brenland's graduates (weekend problem). Invented data, seeded: 1990-2025, the log
relative supply of graduates grows 4.5 % a year to 2005 and 2 % after, from -1.2;
log relative demand grows 3 % a year from -0.6; the premium is
(demand - supply) / 1.6 plus noise (s.d. 0.01). Part IV: invented group means and
coefficients for a gap decomposition."""
import numpy as np
import pandas as pd
import statsmodels.api as sm

SIGMA, G_DEMAND, SEED = 1.6, 0.03, 25
YEARS = np.arange(1990, 2026)
# Part IV: group A and B means (schooling, experience) and A's coefficients
MEANS_A, MEANS_B, COEF_A, GAP = (13.0, 18.0), (12.0, 20.0), (0.08, 0.02), 0.15


def series():
    rng = np.random.default_rng(SEED)
    t = YEARS - 1990
    growth = np.where(YEARS <= 2005, 0.045, 0.02)
    supply = -1.2 + np.concatenate([[0], np.cumsum(growth[1:])])
    supply = supply + rng.normal(0, 0.01, len(t))
    demand = -0.6 + G_DEMAND * t
    premium = (demand - supply) / SIGMA + rng.normal(0, 0.01, len(t))
    return pd.DataFrame({"year": YEARS, "supply": supply, "premium": premium})


def estimate(d):
    x = sm.add_constant(pd.DataFrame({"t": d.year - 1990, "s": d.supply}))
    return sm.OLS(d.premium, x).fit()


def stats():
    d = series()
    r = estimate(d)
    b_s, b_t = r.params["s"], r.params["t"]
    sigma = -1 / b_s
    g = b_t * sigma
    last = d.iloc[-1]
    fitted_2025 = r.params["const"] + b_t * 35 + b_s * last.supply
    supply_2035 = last.supply + 0.02 * 10
    p2035 = r.params["const"] + b_t * 45 + b_s * supply_2035
    explained = sum(c * (a - b) for c, a, b in zip(COEF_A, MEANS_A, MEANS_B))
    first, mid = d.iloc[0], d[d.year == 2005].iloc[0]
    return {"p1990": first.premium, "p2005": mid.premium, "p2025": last.premium,
            "s1990": first.supply, "s2005": mid.supply, "s2025": last.supply,
            "b_supply": b_s, "se_supply": r.bse["s"], "b_t": b_t, "sigma": sigma,
            "demand_growth": 100 * g, "fit2025": fitted_2025, "s2035": supply_2035,
            "p2035": p2035, "ratio2035": np.exp(p2035), "explained": explained,
            "unexplained": GAP - explained}
