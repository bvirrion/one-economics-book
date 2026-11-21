import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_collapse():
    p = pd.read_csv(OUT / "peru.csv").set_index("year").kt
    assert p.loc[1970] > 12000 and p.loc[1973] < 0.25 * p.loc[1970]


def test_itq_columns():
    i = pd.read_csv(OUT / "itq.csv")
    assert list(i.columns) == ["year", "ISL", "NZL"] and i.year.max() >= 2020
