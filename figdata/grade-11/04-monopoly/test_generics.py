import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_generics():
    d = pd.read_csv(OUT / "generics.csv")
    assert len(d) == 10 and (d.amp_p25 <= d.amp_median).all() and (d.amp_median <= d.amp_p75).all()
    assert d.amp_median.iloc[0] > d.amp_median.iloc[1] > d.amp_median.iloc[3] > d.amp_median.iloc[-1]
