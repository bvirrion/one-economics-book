"""Weekend problem: Brenland's borrowing years. Net exports (X - M) and GDP from the
country accounts, 2000--2025; the problem's assumptions: net external debt of 45,000
million dalens at the end of 1999 (about 30 % of GDP), an interest rate on it equal
to the policy rate plus one point, no valuation changes and no transfers. Then CA =
NX - i D(-1) and D = D(-1) - CA. Writes out/borrow.csv (every year),
out/borrow_points.csv (selected years) and out/borrow_stats.csv (averages and the
stabilising trade balance)."""
import pandas as pd
from country import load
from figout import write_table

D0, SPREAD = 45_000.0, 1.0
POINTS = [2000, 2008, 2009, 2010, 2019, 2020, 2025]


def table():
    a = load("accounts")
    d_prev = D0
    rows = []
    for _, r in a.iterrows():
        i = (r.policy_rate + SPREAD) / 100
        nx = r.X - r.M
        ca = nx - i * d_prev
        d = d_prev - ca
        rows.append({"year": int(r.year), "gdp": r.gdp, "nx": nx, "i": 100 * i,
                     "interest": i * d_prev, "ca": ca, "debt": d,
                     "nx_pct": 100 * nx / r.gdp, "ca_pct": 100 * ca / r.gdp,
                     "debt_pct": 100 * d / r.gdp})
        d_prev = d
    return pd.DataFrame(rows)


def stats(t):
    g = t.gdp.pct_change().iloc[1:]
    last = t.iloc[-1]
    r_avg = t.i.iloc[-5:].mean() / 100  # average rate over the last five years
    g_avg = g.iloc[-10:].mean()  # nominal growth over the last ten years
    d = last.debt_pct / 100
    nx_star = (r_avg - g_avg) / (1 + g_avg) * d
    stop = last.interest / last.gdp  # NX needed for CA = 0 at 2025 interest
    return pd.DataFrame({"stat": ["debt_2025_pct", "r_avg_pct", "g_avg_pct",
                                  "nx_star_pct", "nx_2025_pct", "nx_stop_pct"],
                         "value": [100 * d, 100 * r_avg, 100 * g_avg, 100 * nx_star,
                                   last.nx_pct, 100 * stop]})


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "borrow")
    pts = t[t.year.isin(POINTS)].reset_index(drop=True)
    write_table(pts, __file__, "borrow_points")
    write_table(stats(t), __file__, "borrow_stats")
