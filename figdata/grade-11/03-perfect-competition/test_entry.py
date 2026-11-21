import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_entry_rates():
    d = pd.read_csv(OUT / "entry.csv")
    assert len(d) == 11 and (d.n >= 25).all()
    assert (d.birth > 0).all() and (d.death > 0).all() and (d.birth < 30).all()
