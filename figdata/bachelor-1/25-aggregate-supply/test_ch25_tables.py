"""Facts the charts of b1 ch. 25 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_accel():
    s = pd.read_csv(OUT / "accel_stats.csv").iloc[0]
    assert s.n == 59 and s.slope < 0


def test_euro():
    e = pd.read_csv(OUT / "euro.csv")
    assert len(e) == 16 and e.year.min() == 2009


def test_accel_uses_bls_inflation():
    # BLS publishes CPI-U annual-average inflation of 13.5% for 1980 and 3.2% for 1983.
    a = pd.read_csv(OUT / "accel.csv").set_index("year")
    assert round(a.pi[1980], 1) == 13.5 and round(a.pi[1983], 1) == 3.2
    # The change in inflation is recomputed from the printed inflation column.
    assert abs(a.dpi[1983] - (a.pi[1983] - a.pi[1982])) < 0.002
