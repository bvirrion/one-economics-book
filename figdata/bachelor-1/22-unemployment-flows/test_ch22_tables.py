"""Facts the charts of b1 ch. 22 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_unemp():
    u = pd.read_csv(OUT / "us_unemp.csv")
    assert u[u.year == 1933].unemp.iloc[0] > 20
    assert u[u.year >= 1948].unemp.notna().all()


def test_flows():
    f = pd.read_csv(OUT / "jolts_flows.csv")
    assert len(f) >= 290 and (f.HI > 3).all()
