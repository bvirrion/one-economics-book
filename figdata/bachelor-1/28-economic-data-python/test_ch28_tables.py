"""Facts the charts of b1 ch. 28 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_cpi():
    s = pd.read_csv(OUT / "cpi_stats.csv").iloc[0]
    assert s.n == 120 and s.sd_nsa > s.sd_sa and s.corr_hand > 0.9
