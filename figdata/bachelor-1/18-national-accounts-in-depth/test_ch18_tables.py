"""Facts the charts of b1 ch. 18 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_gap():
    s = pd.read_csv(OUT / "growth_gap_stats.csv").iloc[0]
    assert s.n > 150 and s.median_abs_gap < 0.3


def test_balances():
    b = pd.read_csv(OUT / "balances_de.csv")
    assert len(b) == 25
    assert ((b.private + b.gov + b.row).abs() < 1e-6).all()
