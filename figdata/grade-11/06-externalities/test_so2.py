import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_rise_and_fall():
    p = pd.read_csv(OUT / "so2_peaks.csv").set_index("iso3")
    for iso in ["USA", "GBR", "DEU", "JPN"]:
        assert p.loc[iso, "so2pc_2022"] < 0.3 * p.loc[iso, "peak_so2pc"]


def test_usa_fall_after_1990():
    u = pd.read_csv(OUT / "so2_usa.csv").set_index("year").mt
    assert u.loc[2010] < 0.5 * u.loc[1990]
