"""Facts the charts of b1 ch. 9 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_cross_section():
    s = pd.read_csv(OUT / "capital_wage_stats.csv").iloc[0]
    assert 100 <= s.n <= 130 and 0.7 < s.slope < 1.2


def test_paths():
    s = pd.read_csv(OUT / "kl_wr_slopes.csv").set_index("iso3")
    assert set(s.index) == {"USA", "KOR"}
    assert (s.kl2019 > 1).all() and (s.wr2019 > 1).all()
