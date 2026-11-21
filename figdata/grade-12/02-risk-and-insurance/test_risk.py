import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_common_shock_2020():
    d = pd.read_csv(OUT / "death_rates.csv").set_index("year")
    assert d.loc[2020, "USA"] > d.loc[2019, "USA"] + 1
    assert all(d.loc[2020, c] >= d.loc[2019, c] for c in ["FRA", "SWE", "USA"])


def test_spread_shrinks():
    p = pd.read_csv(OUT / "pool_spread.csv")
    width = (p.p95 - p.p05).tolist()
    assert width[0] > 5 * width[-1]
    assert p.p05.iloc[-1] < 50 < p.p95.iloc[-1]
    assert abs(p.sd_theory.iloc[0] - 68.92) < 0.01
