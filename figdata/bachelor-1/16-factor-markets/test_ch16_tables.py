"""Facts the charts of b1 ch. 16 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_labsh():
    d = pd.read_csv(OUT / "labsh_2019.csv")
    assert len(d) > 120
    assert d.labsh.between(0, 1).all()
    assert 0.45 < d.labsh.median() < 0.6
