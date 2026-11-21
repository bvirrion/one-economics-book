"""Facts the charts of b1 ch. 20 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_counts():
    s = pd.read_csv(OUT / "solow_stats.csv").iloc[0]
    assert s.n > 150
    assert s.corr_lny_s > 0
    assert 0 < s.alpha < 1
