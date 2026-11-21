"""Facts the charts of b1 ch. 29 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_pip():
    p = pd.read_csv(OUT / "pip_usa.csv")
    assert len(p) == 100 and p.avg_welfare.is_monotonic_increasing
    assert pd.read_csv(OUT / "pip_stats.csv").top_over_median.iloc[0] > 5


def test_simpson():
    s = pd.read_csv(OUT / "simpson.csv").set_index("group")
    assert (s.loc[["Not working", "Working"], "old"] > s.loc[["Not working", "Working"], "young"]).all()
    assert s.loc["All", "old"] < s.loc["All", "young"]
