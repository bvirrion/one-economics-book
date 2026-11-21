import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_island_diverged():
    t = pd.read_csv(OUT / "island.csv").set_index("year")
    assert abs(t.loc[1950, "HTI"] - t.loc[1950, "DOM"]) < 300
    assert t.loc[2022, "DOM"] > 10 * t.loc[2022, "HTI"]


def test_intensity_fell_energy_rose():
    k = pd.read_csv(OUT / "intensity_key.csv").iloc[0]
    assert k.wld2021 < k.wld2000 and k.energy_ratio > 1


def test_patent():
    k = pd.read_csv(OUT / "patent_key.csv").iloc[0]
    assert k.profit == 1600 and k.dwl == 800 and k.cs_c == 3200
    assert abs(k.pv_patent - 1600 * k.af20) < 0.1
