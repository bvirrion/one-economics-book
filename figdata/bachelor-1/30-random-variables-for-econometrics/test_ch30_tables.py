"""Facts the charts of b1 ch. 30 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_clt():
    s = pd.read_csv(OUT / "means_stats.csv")
    assert ((s.sd / s.se - 1).abs() < 0.03).all()
