"""Inequality: Gini before and after social transfers in Europe (2025), Lorenz curves of four countries, Brenland's survey.

Grade 11, chapter 11 (inequality).
Eurostat ilc_di12 (Gini of equivalised disposable income, all ages) and ilc_di12b (before social transfers, pensions
counted as social transfers), survey year 2025, twelve countries and the EU.
PIP percentiles (2021 PPP): Lorenz curves at the latest year, national; South Africa's survey measures consumption.
Brenland (invented): code/shared/country households.csv, income per household divided by the square root of its size;
households ranked by that income; shares by fifths rounded to 0.1 and made to add to 100 by adjusting the top fifth;
Gini by trapezoids over the rounded fifths.
Writes:
  out/eu_gini.csv      x, geo, before, after, cut
  out/lorenz_<ISO>.csv  pop, cum   (0..100)
  out/lorenz_gini.csv   iso3, year, welfare, gini
  out/bren_fifths.csv   fifth, market, disposable, cum_market, cum_disposable
  out/bren_lorenz.csv   pop, market, disposable (cumulative, 0..100)
  out/bren_key.csv      gini_m, gini_d, p10_m, p90_m, ratio_m, p10_d, p90_d, ratio_d, top10_m, top10_d
"""
import numpy as np
import pandas as pd

import country
from econdata import eurostat, pip_percentiles
from figout import write_table

GEOS = ["SK", "BE", "SI", "PL", "NL", "SE", "DE", "FR", "IT", "ES", "LT", "BG", "EU27_2020"]
LORENZ = ["SWE", "USA", "BRA", "ZAF"]


def eu(year=2025):
    a = eurostat("ilc_di12")
    a = a[(a.age == "TOTAL") & (a.time == year)].set_index("geo").value
    b = eurostat("ilc_di12b")
    b = b[b.time == year].set_index("geo").value
    d = pd.DataFrame({"geo": GEOS, "before": [b[g] for g in GEOS], "after": [a[g] for g in GEOS]})
    d["cut"] = (d.before - d.after).round(1)
    d.insert(0, "x", range(len(d)))
    return d


def lorenz():
    p = pip_percentiles(isos=LORENZ)
    p = p[p.reporting_level == "national"]
    curves, ginis = {}, []
    for iso in LORENZ:
        x = p[p.iso3 == iso]
        x = x[x.year == x.year.max()].sort_values("percentile")
        cum = np.r_[0, np.cumsum(x.welfare_share.values) / x.welfare_share.sum()]
        pop = np.r_[0, np.cumsum(x.pop_share.values) / x.pop_share.sum()]
        g = 1 - np.sum((pop[1:] - pop[:-1]) * (cum[1:] + cum[:-1]))
        curves[iso] = pd.DataFrame({"pop": np.round(100 * pop, 2), "cum": np.round(100 * cum, 2)})
        ginis.append({"iso3": iso, "year": int(x.year.iloc[0]), "welfare": x.welfare_type.iloc[0], "gini": round(g, 2)})
    return curves, pd.DataFrame(ginis)


def fifths(e):
    e = np.sort(e)
    n = len(e)
    sh = np.array([e[i * n // 5:(i + 1) * n // 5].sum() for i in range(5)]) / e.sum() * 100
    sh = np.round(sh, 1)
    sh[-1] = round(100 - sh[:-1].sum(), 1)
    return sh


def gini_fifths(sh):
    L = np.cumsum(sh) / 100
    return 1 - np.sum(0.2 * (np.r_[0, L[:-1]] + L))


def brenland():
    h = country.load("households")
    out, key = {}, {}
    for col, tag in [("gross_income", "m"), ("disposable", "d")]:
        e = (h[col] / np.sqrt(h["size"])).values
        sh = fifths(e)
        out[tag] = sh
        key[f"gini_{tag}"] = round(gini_fifths(sh), 3)
        p10, p90 = np.percentile(e, 10), np.percentile(e, 90)
        key[f"p10_{tag}"], key[f"p90_{tag}"] = int(round(p10, -2)), int(round(p90, -2))
        key[f"ratio_{tag}"] = round(round(p90, -2) / round(p10, -2), 1)
        es = np.sort(e)
        key[f"top10_{tag}"] = round(100 * es[int(0.9 * len(es)):].sum() / es.sum(), 1)
    f = pd.DataFrame({"fifth": range(1, 6), "market": out["m"], "disposable": out["d"],
                      "cum_market": np.round(np.cumsum(out["m"]), 1), "cum_disposable": np.round(np.cumsum(out["d"]), 1)})
    return f, pd.DataFrame([key])


if __name__ == "__main__":
    write_table(eu(), __file__, "eu_gini")
    c, g = lorenz()
    for iso, x in c.items():
        write_table(x, __file__, f"lorenz_{iso}")
    write_table(g, __file__, "lorenz_gini")
    f, k = brenland()
    write_table(f, __file__, "bren_fifths")
    write_table(pd.DataFrame({"pop": [0, 20, 40, 60, 80, 100], "market": [0] + list(f.cum_market),
                              "disposable": [0] + list(f.cum_disposable)}), __file__, "bren_lorenz")
    write_table(k, __file__, "bren_key")
