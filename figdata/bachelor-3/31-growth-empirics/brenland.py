"""Brenland's fifty years (weekend problem).

Real GDP per person (2015 dalens): 2000--2025 from accounts.csv; 1975--1999 invented
here, backwards from 2000, with annual log growth of 0.5 % in 1976--1981, 4.0 % in
1982--1995 and 2.0 % in 1996--2000. Twenty invented peers have 1975 incomes drawn
lognormal around 9,000 dalens (seed 31) and grow from 1975 to 2025 at
2.5 % - 1.2 x ln(y75 / 9,000) % a year plus noise of 0.4 points. The acceleration
filter: year t qualifies if mean growth over t+1..t+8 is at least 3.5 %, at least
2 points above the mean over t-4..t, and income in t+8 exceeds every earlier year's;
a run of qualifying years is one episode, dated at the year with the largest rise in
mean growth. Sectors: farming had 20 % of workers in 1975 and 5 % in 2025, with
output per worker of 6 and 12 thousand dalens; the rest had 16 and 36 thousand."""
import numpy as np
import pandas as pd
from country import load

PEERS, SEED = 20, 31
RATES = [(1976, 1981, 0.005), (1982, 1995, 0.04), (1996, 2000, 0.02)]


def series():
    a = load("accounts")
    y = (a.real_gdp / a["pop"] * 1000).to_numpy()
    s = {int(yr): v for yr, v in zip(a.year, y)}
    level = s[2000]
    for year in range(2000, 1975, -1):
        g = next(r for a0, a1, r in RATES if a0 <= year <= a1)
        level = level / np.exp(g)
        s[year - 1] = level
    return pd.Series(s).sort_index()


def peers():
    rng = np.random.default_rng(SEED)
    y75 = 9000 * np.exp(rng.normal(0, 0.6, PEERS))
    g = 0.025 - 0.012 * np.log(y75 / 9000) + rng.normal(0, 0.004, PEERS)
    return pd.DataFrame({"y75": y75, "growth": 100 * g})


def beta_hat(y75, growth):
    X = np.column_stack([np.ones(len(y75)), np.log(y75)])
    b = np.linalg.lstsq(X, np.asarray(growth) / 100, rcond=None)[0]
    return b


def accelerations(s):
    g = 100 * np.log(s / s.shift(1))
    ok = []
    for t in s.index:
        after, before = g.loc[t + 1:t + 8], g.loc[t - 4:t]
        if len(after) < 8 or len(before) < 5 or before.isna().any():
            continue
        rise = after.mean() - before.mean()
        if (after.mean() >= 3.5 and rise >= 2
                and s.loc[t + 8] > s.loc[:t + 7].max()):
            ok.append((t, before.mean(), after.mean(), rise))
    episodes, run = [], []
    for row in ok:
        if run and row[0] != run[-1][0] + 1:
            episodes.append(max(run, key=lambda r: r[3]))
            run = []
        run.append(row)
    if run:
        episodes.append(max(run, key=lambda r: r[3]))
    return episodes


def sectors():
    shares = {1975: (0.20, 0.80), 2025: (0.05, 0.95)}
    prod = {1975: (6.0, 16.0), 2025: (12.0, 36.0)}
    agg = {t: sum(s * p for s, p in zip(shares[t], prod[t])) for t in shares}
    within = sum(s0 * (p1 - p0) for s0, p0, p1 in
                 zip(shares[1975], prod[1975], prod[2025]))
    between = sum((s1 - s0) * p0 for s0, s1, p0 in
                  zip(shares[1975], shares[2025], prod[1975]))
    cross = agg[2025] - agg[1975] - within - between
    return {"agg75": agg[1975], "agg25": agg[2025], "within": within,
            "between": between, "cross": cross,
            "gap75": prod[1975][1] / prod[1975][0],
            "gap25": prod[2025][1] / prod[2025][0]}


def stats():
    s = series()
    g = lambda a, b: 100 * np.log(s[b] / s[a]) / (b - a)  # noqa: E731
    p = peers()
    allp = pd.concat([p, pd.DataFrame({"y75": [s[1975]], "growth": [g(1975, 2025)]})])
    b = beta_hat(allp.y75, allp.growth)
    speed = -np.log(1 + 50 * b[1]) / 50
    acc = accelerations(s)
    sec = sectors()
    ln75 = np.log(p.y75)
    ln25 = ln75 + 50 * p.growth / 100
    return {"sigma75": ln75.std(ddof=0), "sigma25": ln25.std(ddof=0),
            "y75": s[1975], "y2000": s[2000], "y25": s[2025],
            "g75_00": g(1975, 2000), "g00_25": g(2000, 2025), "g75_25": g(1975, 2025),
            "double_00_25": 70 / g(2000, 2025), "beta": b[1], "alpha": b[0],
            "speed": 100 * speed,
            "pred_brenland": 100 * (b[0] + b[1] * np.log(s[1975])),
            "acc_year": acc[0][0] if acc else np.nan,
            "acc_before": acc[0][1] if acc else np.nan,
            "acc_after": acc[0][2] if acc else np.nan, "n_acc": len(acc), **sec,
            "static_share": 100 * sec["between"] / (sec["agg25"] - sec["agg75"]),
            "realloc_share": 100 * (sec["between"] + sec["cross"])
            / (sec["agg25"] - sec["agg75"])}
