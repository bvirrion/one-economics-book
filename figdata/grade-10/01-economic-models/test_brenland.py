import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_years_and_the_two_falls():
    d = pd.read_csv(OUT / "brenland_gdppc.csv").set_index("year").gdppc
    assert list(d.index) == list(range(2000, 2026))
    assert d[2009] < d[2008] < d[2007] and d[2020] < d[2019]
    assert d[2000] == 24675 and d[2025] == 31470
