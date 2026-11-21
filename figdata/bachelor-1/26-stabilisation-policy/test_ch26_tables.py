"""Facts the charts of b1 ch. 26 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_budget():
    s = pd.read_csv(OUT / "budget_stats.csv").iloc[0]
    assert s.n == 27 and s.fell >= 20 and s.slope > 0


def test_cpi():
    c = pd.read_csv(OUT / "cpi.csv")
    assert len(c) == 72 and c.yoy.max() == 9.1
