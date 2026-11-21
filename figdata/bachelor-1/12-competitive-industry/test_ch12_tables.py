"""Facts the opening chart of b1 ch. 12 shows."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_up_since_1950():
    p = pd.read_csv(OUT / "house_points.csv")
    assert (p.v2020 > p.v1950).all()
