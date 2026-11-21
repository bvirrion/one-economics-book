"""Facts the opening chart of b1 ch. 2 shows."""
from pathlib import Path

import numpy as np
import pandas as pd
from econdata import pwt

OUT = Path(__file__).resolve().parent / "out"


def test_table():
    t = pd.read_csv(OUT / "hours_wage.csv")
    assert len(t) == 111 and (t.wage > 0).all() and (t.hours > 0).all()
    assert "VEN" not in set(t.iso3)
    s = pd.read_csv(OUT / "hours_wage_stats.csv").iloc[0]
    assert round(np.corrcoef(np.log(t.wage), t.hours)[0, 1], 2) == s.corr_logwage_hours


def test_usa_matches_pwt():
    u = pwt(["USA"], 2019, 2019, ["emp", "avh", "labsh", "cgdpo"]).iloc[0]
    t = pd.read_csv(OUT / "hours_wage.csv").set_index("iso3")
    assert abs(t.loc["USA", "wage"] - u.labsh * u.cgdpo / (u.emp * u.avh)) < 0.01
    assert t.loc["USA", "hours"] == round(u.avh)


def test_tenths():
    g = pd.read_csv(OUT / "hours_wage_tenths.csv")
    assert g.n.sum() == 111 and len(g) == 10
    assert g.hours.iloc[-1] < g.hours.iloc[0]
