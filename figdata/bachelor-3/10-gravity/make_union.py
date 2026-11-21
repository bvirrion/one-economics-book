"""Weekend problem: Brenland joins a customs union (invented world of world.py).

Observed flows are expected flows times heteroskedastic noise (larger for small
flows, mean one), and flows below 0.05 billion are not recorded (zeros). Estimates:
OLS on log positive flows with log GDPs; OLS with exporter and importer dummies;
PPML with the dummies on all pairs, zeros included. The union's effect on Brenland's
trade with members and non-members is then computed with the PPML estimates, with
and without the union, resistance terms re-solved. Writes out/union_countries.csv,
out/union_estimates.csv, out/union_brenland.csv, out/union_stats.csv and
out/union_table.csv (members and the two largest non-members, distance from Brenland)."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from figout import write_table
from world import N, countries, distances, flows

THRESHOLD = 0.05


def panel():
    c = countries()
    rng = np.random.default_rng(2004)
    X = flows(c)
    s2 = 0.04 + 1.0 / (1 + X / np.median(X))
    obs = X * np.exp(rng.normal(-s2 / 2, np.sqrt(s2)))
    obs = np.where(obs < THRESHOLD, 0.0, np.round(obs, 3))
    D, m, y = distances(c), c.member.to_numpy(), c.gdp.to_numpy()
    rows = [{"o": c.name[i], "d": c.name[j], "x": obs[i, j], "ln_dist": np.log(D[i, j]),
             "ln_gdp_o": np.log(y[i]), "ln_gdp_d": np.log(y[j]),
             "union": int(m[i] and m[j])}
            for i in range(N) for j in range(N) if i != j]
    return c, pd.DataFrame(rows)


def estimates(p):
    pos = p[p.x > 0].assign(ln_x=lambda d: np.log(d.x))
    fe = " + C(o) + C(d)"
    fits = {"OLS": smf.ols("ln_x ~ ln_gdp_o + ln_gdp_d + ln_dist + union", pos),
            "OLS with fixed effects": smf.ols("ln_x ~ ln_dist + union" + fe, pos),
            "PPML with fixed effects": smf.glm("x ~ ln_dist + union" + fe, p,
                                           family=sm.families.Poisson())}
    rows = []
    for name, model in fits.items():
        r = model.fit(cov_type="HC1")
        gdp = r.params.get("ln_gdp_o", np.nan), r.params.get("ln_gdp_d", np.nan)
        rows.append({"method": name, "pairs": int(r.nobs),
                     "gdp_o": gdp[0], "gdp_d": gdp[1],
                     "dist": r.params["ln_dist"], "dist_se": r.bse["ln_dist"],
                     "union": r.params["union"], "union_se": r.bse["union"]})
    return pd.DataFrame(rows)


def brenland(c, delta, union):
    """Brenland's exports plus imports with members and non-members, without and
    with the union, from the model with the given coefficients."""
    m = c.member.to_numpy().astype(bool)
    out = []
    for with_union in (False, True):
        X = flows(c, delta, union, with_union)
        trade = X[0] + X[:, 0]
        out.append((trade[1:][m[1:]].sum(), trade[1:][~m[1:]].sum(), X[0, 0]))
    (m0, n0, h0), (m1, n1, h1) = out
    return pd.DataFrame({"partners": ["members", "non-members", "home sales"],
                         "before": [m0, n0, h0], "after": [m1, n1, h1],
                         "change": [100 * (m1 / m0 - 1), 100 * (n1 / n0 - 1),
                                    100 * (h1 / h0 - 1)]})


if __name__ == "__main__":
    c, p = panel()
    e = estimates(p)
    ppml = e.set_index("method").loc["PPML with fixed effects"]
    write_table(c, __file__, "union_countries")
    dist0 = distances(c)[0]
    show = c.assign(dist=dist0)[((c.member == 1) | c.name.isin(["N02", "N10"]))
                               & (c.name != "Brenland")]
    write_table(show[["name", "gdp", "dist", "member"]], __file__, "union_table")
    write_table(e, __file__, "union_estimates")
    write_table(brenland(c, -ppml.dist, ppml.union), __file__, "union_brenland")
    stats = pd.DataFrame({"stat": ["pairs", "zeros", "union_pairs", "recorded_total"],
                          "value": [len(p), int((p.x == 0).sum()), int(p.union.sum()),
                                    p.x.sum()]})
    write_table(stats, __file__, "union_stats")
