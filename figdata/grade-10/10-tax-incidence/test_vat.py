import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_steps():
    s = pd.read_csv(OUT / "vat_steps.csv").set_index("step")
    assert s.loc["cut", "d_all"] < 0 and s.loc["end", "d_all"] > 0
    assert len(pd.read_csv(OUT / "vat_de.csv")) == 36
