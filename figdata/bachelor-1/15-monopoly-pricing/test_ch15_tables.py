"""Facts the opening chart of b1 ch. 15 shows."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_spreads():
    d = pd.read_csv(OUT / "spreads_2019.csv")
    assert len(d) > 80
    assert (d.spread > 0).mean() > 0.95
