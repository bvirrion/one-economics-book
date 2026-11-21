import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_earnings_rise_with_education():
    e = pd.read_csv(OUT / "edpays.csv")
    assert e.earnings.is_monotonic_increasing and e.unemp.is_monotonic_decreasing


def test_uneduc_complete():
    u = pd.read_csv(OUT / "uneduc.csv")
    assert u[["basic", "intermediate", "advanced"]].notna().all().all()
