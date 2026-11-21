import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_health_more_than_proportional():
    f = pd.read_csv(OUT / "health_fit.csv").iloc[0]
    assert f.n >= 180 and 1.0 < f.slope < 1.3
    assert abs(10 ** f.slope - f.times) < 0.1


def test_food_less_than_proportional():
    f = pd.read_csv(OUT / "food_fit.csv").iloc[0]
    assert 0 < f.slope < 1 and 0 < f.arc < 1
    assert f.share_low > f.share_high
