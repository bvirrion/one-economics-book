"""The Kestrian border tax (invented): a panel of shops for the chapter's weekend problem.

Twelve provinces of Kestria, 50 shops each, years 2014-2024. Kestria raises its sales tax in
the three western provinces W1-W3 from 2019 and in the three eastern ones E1-E3 from 2021;
the six northern provinces N1-N6 never. Log sales of shop i in province p, year t:
    y = s_i + g_t + e_pt + effect + u_it,
s_i ~ N(level_p, 0.3) with level_p ~ U(4.5, 5.5); g_t a common path; e_pt an AR(1) province
shock (0.5, sd 0.015); u_it ~ N(0, 0.05). The effect k years after the rise is -0.04, -0.08,
then -0.12 (W1, on the border with Brenland: 1.5 times as large). Seed 2019.
Writes out/kestria_means.csv, out/kestria_event.csv, out/kestria_estimates.csv,
out/kestria_synth.csv (W1, weights over N1-N6) and out/kestria_synth_gap.csv.
Book 5, chapter 3, weekend problem.
"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from figout import write_table
from scipy.optimize import minimize

YEARS = np.arange(2014, 2025)
PROV = {**{f"W{j}": 2019 for j in (1, 2, 3)}, **{f"E{j}": 2021 for j in (1, 2, 3)},
        **{f"N{j}": None for j in range(1, 7)}}
PATH = (-0.04, -0.08, -0.12)


def effect(p, t):
    s = PROV[p]
    if s is None or t < s:
        return 0.0
    e = PATH[min(t - s, 2)]
    return 1.5 * e if p == "W1" else e


def panel():
    rng = np.random.default_rng(2019)
    g = np.cumsum(rng.normal(0.02, 0.02, len(YEARS)))
    rows = []
    for p in PROV:
        level = rng.uniform(4.5, 5.5)
        e, shock = 0.0, []
        for _ in YEARS:
            e = 0.5 * e + rng.normal(0, 0.015)
            shock.append(e)
        for i in range(50):
            s = rng.normal(level, 0.3)
            for j, t in enumerate(YEARS):
                rows.append((f"{p}-{i}", p, p[0], t, s + g[j] + shock[j] + effect(p, t)
                             + rng.normal(0, 0.05)))
    d = pd.DataFrame(rows, columns=["shop", "prov", "group", "year", "y"])
    d["d"] = [int(PROV[p] is not None and t >= PROV[p]) for p, t in zip(d.prov, d.year)]
    d["true"] = [effect(p, t) for p, t in zip(d.prov, d.year)]
    return d


def cl(d):
    return {"cov_type": "cluster", "cov_kwds": {"groups": pd.factorize(d.prov)[0]}}


def slsqp(y1, Y0):
    n = Y0.shape[1]
    r = minimize(lambda w: (y1 - Y0 @ w) @ (y1 - Y0 @ w), np.full(n, 1 / n),
                 jac=lambda w: -2 * Y0.T @ (y1 - Y0 @ w), method="SLSQP",
                 bounds=[(0, 1)] * n,
                 constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1}],
                 options={"ftol": 1e-14, "maxiter": 1000})
    w = np.clip(r.x, 0, None)
    return w / w.sum()


def tables():
    d = panel()
    wn = d[d.group.isin(["W", "N"])].copy()
    means = (wn[wn.year.isin([2018, 2020])].groupby(["group", "year"]).y.mean()
             .unstack().reset_index())
    means.columns = ["group", "y2018", "y2020"]
    means["group"] = means.group.map({"N": "north", "W": "west"})

    wn["k"] = np.where(wn.group == "W", wn.year - 2019, -99)
    names = []
    for k in range(-5, 6):
        if k != -1:
            n = f"k{k + 5}"
            wn[n] = (wn.k == k).astype(float)
            names.append((k, n))
    f = smf.ols("y ~ " + " + ".join(n for _, n in names) + " + C(shop) + C(year)",
                wn).fit(**cl(wn))
    event = pd.DataFrame([(k, f.params[n], f.bse[n]) for k, n in names],
                         columns=["k", "est", "se"])

    two = wn[wn.year.isin([2018, 2020])].assign(post=lambda x: (x.year == 2020) * 1,
                                                 west=lambda x: (x.group == "W") * 1)
    did = smf.ols("y ~ west * post", two).fit(**cl(two))
    twfe = smf.ols("y ~ d + C(shop) + C(year)", d).fit(**cl(d))
    cells = []
    nm = d[d.group == "N"].groupby("year").y.mean()
    for p, s in PROV.items():
        if s is None:
            continue
        pm = d[d.prov == p].groupby("year").y.mean()
        for t in YEARS[YEARS >= s]:
            cells.append((pm[t] - pm[s - 1]) - (nm[t] - nm[s - 1]))
    att = d.loc[d.d == 1, "true"].mean()
    est = pd.DataFrame({
        "estimator": ["two by two (2018 and 2020)", "two-way fixed effects (all provinces)",
                      "clean comparisons with the north", "true average effect"],
        "est": [did.params["west:post"], twfe.params["d"], np.mean(cells), att],
        "se": [did.bse["west:post"], twfe.bse["d"], np.nan, np.nan]})

    pm = d.groupby(["prov", "year"]).y.mean().unstack()
    donors = [f"N{j}" for j in range(1, 7)]
    pre = YEARS < 2019
    w = slsqp(pm.loc["W1"].values[pre], pm.loc[donors].values.T[pre])
    synth = pm.loc[donors].values.T @ w
    gap = pm.loc["W1"].values - synth
    sw = pd.DataFrame({"donor": donors, "weight": w})
    sg = pd.DataFrame({"year": YEARS, "gap": gap})
    return means, event, est, sw, sg


if __name__ == "__main__":
    for t, n in zip(tables(), ["kestria_means", "kestria_event", "kestria_estimates",
                               "kestria_synth", "kestria_synth_gap"]):
        write_table(t, __file__, n)
