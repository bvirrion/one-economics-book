import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_hie_levels():
    h = pd.read_csv(OUT / "hie.csv").set_index("plan")
    assert h.loc["free", "spend"] == 2170 and h.loc["c95", "spend"] == 1325
    assert h.loc["c25", "spend"] == 1522 and h.loc["c50", "spend"] == 1635


def test_lemons_settle():
    e = pd.read_csv(OUT / "lemons_end.csv").set_index("case")
    assert abs(e.loc["floor", "price"] - 6000) < 300
    assert e.loc["nofloor", "price"] < 400 and e.loc["nofloor", "share_traded"] < 0.05
