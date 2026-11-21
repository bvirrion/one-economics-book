import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_ranges_fit_the_chart_axes():
    d = pd.read_csv(OUT / "yield_fert.csv")
    assert d.fert.between(1, 1000).all()
    assert d.yld.between(300, 20000).all()
    assert len(d) > 100


def test_correlation_is_positive_and_groups_rise():
    d = pd.read_csv(OUT / "yield_fert.csv")
    assert np.corrcoef(np.log10(d.fert), np.log10(d.yld))[0, 1] > 0.5
    g = pd.read_csv(OUT / "yield_groups.csv")
    assert list(g.median_yld) == sorted(g.median_yld) and g.n.sum() == len(d)
