"""Facts the charts of b1 ch. 32 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_fit():
    f = pd.read_csv(OUT / "fit.csv").iloc[0]
    assert 0.07 < f.slope < 0.11 and 2_100 < f.n < 2_300


def test_toward_and_omitted():
    t = pd.read_csv(OUT / "toward.csv")
    top = t.iloc[-1]
    assert top.re78 < top.re75 and t.iloc[0].re78 > t.iloc[0].re75
    m = pd.read_csv(OUT / "omitted_means.csv").iloc[0]
    assert abs((m.short - 0.06) / 0.024 - 1) < 0.1 and abs(m.long - 0.06) < 0.002
