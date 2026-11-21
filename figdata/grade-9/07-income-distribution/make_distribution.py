"""g9-07 Who Earns What: Income Distribution.

world_distribution.csv  logmid, mid, y1990, y2019: the world distribution of income or consumption per person per day
                        (2021 PPP dollars), people in millions per bin of a tenth of a power of ten.
                        Method: for each target year (1990, 2019) and each country, the PIP survey (percentiles, 2021
                        PPP) whose year is nearest the target, within 3 years (ties: the later survey); the national
                        table, or urban and rural together where PIP has no national table that year. Each percentile
                        stands for 1 % of the country's population in the target year (WDI SP.POP.TOTL). Countries
                        with no survey within 3 years are left out; the covered share of the world's population is in
                        facts.csv and the caption.
top_fifth_share.csv     year, USA, CHN, IND, BRA, SWE, GBR: income or consumption share of the richest fifth, percent
                        (WDI SI.DST.05TH.20), survey years since 1980 (missing years nan)
brenland_fifths.csv     fifth, gross, disposable: shares of total household income by fifths of households ranked by
                        that income (frozen invented survey of 2,000 households)
town.csv                fifth, income: the chapter's invented town (shares by fifths)
facts.csv               name, value
"""
import math

import numpy as np
import pandas as pd

from country import load
from econdata import pip_percentiles, wdi
from figout import write_table

TARGETS = (1990, 2019)
WINDOW = 3
LINE = 3.00  # dollars a day, 2021 PPP (the line of the grade 6 chapter on poverty)
BIN = 0.1    # bin width in powers of ten
TOP_ISOS = ["USA", "CHN", "IND", "BRA", "SWE", "GBR"]
TOWN = [6, 10, 15, 22, 47]  # the invented town's fifths, percent


def _choose(pip, target):
    """One table per country: rows of percentiles with weights (share of the country's population)."""
    out = []
    for iso, d in pip.groupby("iso3"):
        years = sorted(set(d.year))
        cands = [y for y in years if abs(y - target) <= WINDOW]
        if not cands:
            continue
        y = min(cands, key=lambda v: (abs(v - target), -v))
        dy = d[d.year == y]
        if "national" in set(dy.reporting_level):
            t = dy[dy.reporting_level == "national"].copy()
            t["w"] = 0.01
        elif {"urban", "rural"} <= set(dy.reporting_level):
            t = dy[dy.reporting_level.isin(["urban", "rural"])].copy()
            tot = t.groupby("reporting_level").pop.sum()
            t["w"] = 0.01 * t.reporting_level.map(tot / tot.sum())
        else:
            continue
        t["survey_year"] = y
        out.append(t[["iso3", "survey_year", "welfare_type", "avg_welfare", "w"]])
    return pd.concat(out, ignore_index=True)


def world_tables():
    pip = pip_percentiles()
    pop = wdi("SP.POP.TOTL", since=min(TARGETS), until=max(TARGETS))
    world = pop[pop.iso3 == "WLD"].set_index("year").value
    tables, cover = {}, {}
    for t in TARGETS:
        c = _choose(pip, t)
        p = pop[pop.year == t].set_index("iso3").value
        c = c[c.iso3.isin(p.index)].copy()
        c["people"] = c.w * c.iso3.map(p)
        tables[t] = c
        cover[t] = c.groupby("iso3").people.sum().sum() / world[t]
    return tables, cover


def world_distribution():
    tables, _ = world_tables()
    edges = np.round(np.arange(-1.0, 3.0 + BIN / 2, BIN), 2)
    out = pd.DataFrame({"logmid": np.round(edges[:-1] + BIN / 2, 2)})
    out["mid"] = (10 ** out.logmid).round(2)
    for t, c in tables.items():
        lw = np.log10(c.avg_welfare.clip(lower=10 ** -0.999, upper=10 ** 2.999))
        h, _ = np.histogram(lw, bins=edges, weights=c.people)
        out[f"y{t}"] = (h / 1e6).round(1)
    return out


def top_fifth_share():
    t = wdi("SI.DST.05TH.20", isos=TOP_ISOS, since=1980).dropna(subset=["value"])
    t = t.pivot(index="year", columns="iso3", values="value")[TOP_ISOS].round(1)
    return t.astype(object).where(t.notna(), "nan").reset_index()


def fifths(values):
    v = np.sort(np.asarray(values, dtype=float))
    n = len(v)
    parts = [v[i * n // 5:(i + 1) * n // 5].sum() for i in range(5)]
    return [round(100 * x / v.sum(), 1) for x in parts]


def brenland_fifths():
    h = load("households")
    return pd.DataFrame({"fifth": [1, 2, 3, 4, 5], "gross": fifths(h.gross_income),
                         "disposable": fifths(h.disposable)})


def town():
    return pd.DataFrame({"fifth": [1, 2, 3, 4, 5], "income": TOWN})


def facts():
    tables, cover = world_tables()
    rows = []
    for t, c in tables.items():
        tot = c.people.sum()
        rows += [(f"cover_{t}", round(100 * cover[t], 1)), (f"countries_{t}", c.iso3.nunique()),
                 (f"below_line_{t}", round(100 * c[c.avg_welfare < LINE].people.sum() / tot, 1)),
                 (f"median_{t}", round(float(_wmedian(c.avg_welfare, c.people)), 2))]
        below = c[c.avg_welfare < LINE]
        rows.append((f"chn_ind_share_of_below_{t}",
                     round(100 * below[below.iso3.isin(["CHN", "IND"])].people.sum() / below.people.sum(), 1)))
        for iso in ["CHN", "IND"]:
            x = c[c.iso3 == iso]
            rows += [(f"{iso.lower()}_survey_{t}", int(x.survey_year.iloc[0])),
                     (f"{iso.lower()}_median_{t}", round(float(_wmedian(x.avg_welfare, x.people)), 2))]
    w = world_distribution()
    for t in TARGETS:
        rows.append((f"peak_{t}", float(w.loc[w[f"y{t}"].idxmax(), "mid"])))
    s = wdi("SI.DST.05TH.20", isos=TOP_ISOS, since=1980).dropna(subset=["value"])
    for iso in TOP_ISOS:
        d = s[s.iso3 == iso].sort_values("year")
        rows += [(f"top_{iso}_first_year", int(d.year.iloc[0])), (f"top_{iso}_first", round(d.value.iloc[0], 1)),
                 (f"top_{iso}_last_year", int(d.year.iloc[-1])), (f"top_{iso}_last", round(d.value.iloc[-1], 1))]
    h = load("households")
    rows += [("bren_mean_disp", round(h.disposable.mean())), ("bren_median_disp", round(h.disposable.median())),
             ("bren_mean_gross", round(h.gross_income.mean())), ("bren_median_gross", round(h.gross_income.median())),
             ("bren_n", len(h))]
    b = brenland_fifths()
    rows += [(f"bren_gross_q{q}", v) for q, v in zip(b.fifth, b.gross)]
    rows += [(f"bren_disp_q{q}", v) for q, v in zip(b.fifth, b.disposable)]
    q1 = np.sort(h.disposable.values)[: len(h) // 5]
    rows += [("bren_q1_mean_disp", round(q1.mean())), ("bren_q1_max_disp", round(q1.max()))]
    return pd.DataFrame(rows, columns=["name", "value"])


def _wmedian(x, w):
    o = np.argsort(x.values)
    xs, ws = x.values[o], w.values[o]
    cw = np.cumsum(ws)
    return xs[np.searchsorted(cw, cw[-1] / 2)]


if __name__ == "__main__":
    write_table(world_distribution(), __file__, "world_distribution")
    write_table(top_fifth_share(), __file__, "top_fifth_share")
    write_table(brenland_fifths(), __file__, "brenland_fifths")
    write_table(town(), __file__, "town")
    write_table(facts(), __file__, "facts")
