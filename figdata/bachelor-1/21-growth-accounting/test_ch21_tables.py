"""Facts the charts of b1 ch. 21 show."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "out"


def test_parts_sum():
    s = pd.read_csv(OUT / "sources.csv")
    assert len(s) == 8
    tot = s.capital + s.labour + s.human + s.tfp
    assert ((tot - s.output).abs() <= 0.02).all()


def test_devacc():
    st = pd.read_csv(OUT / "devacc_stats.csv").iloc[0]
    assert st.n > 100 and 0 < st.success < 1
