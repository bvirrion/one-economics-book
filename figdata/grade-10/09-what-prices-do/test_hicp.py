import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_fuel_moves_together_hair_does_not():
    s = pd.read_csv(OUT / "hicp_summary.csv").set_index("item")
    assert s.loc["fuel", "mean_corr"] > 0.8
    assert s.loc["hair", "mean_corr"] < s.loc["fuel", "mean_corr"] - 0.3
    assert s.loc["fuel", "n_months"] == 288
