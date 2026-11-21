"""Facts the charts and exercises of b1 ch. 10 use."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_pv():
    d = pd.read_csv(OUT / "pv_costs.csv")
    assert ((d.silicon + d.nonsilicon + d.scale - d.total).abs() <= 0.011).all()
    f = pd.read_csv(OUT / "pv_falls.csv")
    assert f.iloc[2].fall_pct == 96.3


def test_census():
    c = pd.read_csv(OUT / "census_extremes.csv")
    assert len(c) == 6 and (c.ac > 0.4).all()
