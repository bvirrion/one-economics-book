"""Facts the charts of b1 ch. 27 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_pegs():
    s = pd.read_csv(OUT / "peg_stats.csv").set_index("iso3")
    assert s.loc["NLD", "mean_gap"] < s.loc["FRA", "mean_gap"] < s.loc["ITA", "mean_gap"]


def test_fh():
    s = pd.read_csv(OUT / "fh_stats.csv").iloc[0]
    assert s.n > 30 and 0 < s.slope < 1
