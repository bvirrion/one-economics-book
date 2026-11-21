"""Worked numbers of the non-data exercises and the weekend problem of b1 ch. 28.

Weekend problem: Brenland's open-data portal (invented). The portal's tables are
Brenland's accounts, trade and basket files; its trade file has one year mistyped
(2021 written as 2012); its monthly CPI is built here from the yearly CPI with a
known season and a little seeded noise; its headline "real growth" was computed from
nominal GDP.
"""

import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from country import load

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "listings"))
from seasonal_by_hand import adjust  # noqa: E402


def toy_quarterly():
    season = [2, -1, -2, 1]
    x = pd.Series([100 + t + season[t % 4] for t in range(12)], dtype=float)
    trend = (x.rolling(4).mean().shift(-2) + x.rolling(4).mean().shift(-1)) / 2
    diff = (x - trend).dropna()
    comp = diff.groupby(diff.index % 4).mean()
    return [round(v, 3) for v in comp]


def portal_trade():
    t = load("trade").copy()
    t.loc[t.year == 2021, "year"] = 2012
    return t


def portal_cpi():
    a = load("accounts").set_index("year").cpi
    rng = np.random.default_rng(2026)
    rows = []
    for y in range(2015, 2025):
        g = a[y + 1] / a[y]
        for m in range(1, 13):
            trend = a[y] * g ** ((m - 6.5) / 12)
            f = 1 + 0.004 * math.sin(2 * math.pi * (m - 3) / 12)
            rows.append((y, m, trend * f * (1 + rng.normal(0, 0.0005)), f))
    d = pd.DataFrame(rows, columns=["year", "month", "cpi", "true_factor"])
    return d.set_index(["year", "month"])


def problem():
    a = load("accounts").set_index("year")
    t = load("trade")
    b = load("basket")
    ident = (a.gdp - (a.C + a.I + a.G + a.X - a.M)).abs().max()
    deficit = (a.deficit - (a.spending - a.revenue)).abs().max()
    m = a.reset_index().merge(portal_trade(), on="year", how="outer", indicator=True)
    missing = m.loc[m["_merge"] == "left_only", "year"].tolist()
    dup = int(portal_trade().year.duplicated().sum())
    share = t.set_index("year").loc[2025, "exports_to_kestria"] / a.X[2025]
    in_kests = (
        t.set_index("year").loc[2025, "exports_to_kestria"]
        / t.set_index("year").loc[2025, "rate"]
    )
    p = portal_cpi()
    factors, adj = adjust(p.cpi)
    yoy_dec = 100 * (p.cpi.loc[(2024, 12)] / p.cpi.loc[(2023, 12)] - 1)
    avg = p.cpi.groupby(level="year").mean()

    def cagr(x):
        return 100 * ((x[2025] / x[2015]) ** 0.1 - 1)

    real = a.gdp / a.deflator * 100
    return {
        "rows": len(a),
        "ident": ident,
        "deficit": deficit,
        "trade_rows": len(t),
        "basket_rows": len(b),
        "cpi2015": a.cpi[2015],
        "missing": missing,
        "dup": dup,
        "share": round(100 * share, 1),
        "in_kests": round(in_kests, 0),
        "f_true_dec": round(p.true_factor.loc[(2024, 12)], 4),
        "f_hand_dec": round(factors[12], 4),
        "f_true_jun": round(p.true_factor.loc[(2024, 6)], 4),
        "f_hand_jun": round(factors[6], 4),
        "max_err": round((factors - p.true_factor.loc[2024]).abs().max(), 4),
        "yoy_dec2024": round(yoy_dec, 2),
        "avg_2024": round(100 * (avg[2024] / avg[2023] - 1), 2),
        "nominal": round(cagr(a.gdp), 2),
        "real": round(cagr(real), 2),
        "log_mean": round(100 * np.log(real).diff().loc[2016:2025].mean(), 2),
        "per_person": round(cagr(real / a["pop"]), 2),
        "cpi_deflated": round(cagr(a.gdp / a.cpi), 2),
    }


def exercises():
    return {
        "annualise": round(100 * (1.004**12 - 1), 2),
        "toy": toy_quarterly(),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())
