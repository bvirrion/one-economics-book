"""Facts the chart of b1 ch. 24 shows."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_zlb():
    s = pd.read_csv(OUT / "zlb_stats.csv").iloc[0]
    assert s.zlb_months == 84 and s.zlb_max < 0.25


def test_rates_2015():
    w = pd.read_csv(OUT / "jst_rates.csv").set_index("year")
    assert (w.loc[2015] < 1).all()
