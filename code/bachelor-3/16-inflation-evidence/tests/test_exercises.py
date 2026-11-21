from pathlib import Path

import numpy as np
import pandas as pd
from econdata import jst, wdi, wdi_countries

SRC = Path(__file__).resolve().parents[4] / "figdata/bachelor-3/16-inflation-evidence/src"


def test_ex06_two_periods(run_exercise):
    out, _ = run_exercise("ex06_decades")
    lines = out.splitlines()
    slopes = [float(x.split("slope ")[1].split()[0]) for x in lines[1:]]
    # independent route: decade means economy by economy with numpy, then polyfit
    j = jst(cols=["money", "cpi"])
    pts = {"early": [], "late": []}
    for _iso, g in j[j.iso3 != "DEU"].groupby("iso3"):
        g = g.sort_values("year").set_index("year")
        gm, gp = np.log(g.money).diff(), np.log(g.cpi).diff()
        for dec in range(1870, 2030, 10):
            yrs = [y for y in range(dec, dec + 10) if y in g.index]
            m, p = gm.reindex(yrs), gp.reindex(yrs)
            if p.notna().sum() >= 8 and m.notna().any():
                pts["early" if dec < 1970 else "late"].append(
                    (100 * m[m.notna()].mean(), 100 * p[p.notna()].mean()))
    for got, key in zip(slopes, ("early", "late")):
        x, y = np.array(pts[key]).T
        assert abs(got - np.polyfit(x, y, 1)[0]) < 0.006


def test_ex11_targeters_fall(run_exercise):
    out, _ = run_exercise("ex11_targeting_did")
    lines = out.splitlines()
    nums = [float(v) for line in lines[:2] for v in line.replace("%", "").split()
            if v.replace(".", "").isdigit()]
    it_b, it_a, ot_b, ot_a = nums
    did = float(lines[2].split()[-2])
    assert abs(did - ((it_a - it_b) - (ot_a - ot_b))) <= 0.11
    # independent check of one median: the targeters' inflation before adoption
    t = pd.read_csv(SRC / "targeters.csv")
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    p = wdi("FP.CPI.TOTL.ZG", since=1980, until=2024).dropna()
    p = p[p.iso3.isin(real)]
    before = [p[(p.iso3 == r.iso3) & p.year.between(r.adoption - 5, r.adoption - 1)].value.mean()
              for r in t.itertuples()]
    assert abs(np.nanmedian(before) - it_b) < 0.051 and did < 0
