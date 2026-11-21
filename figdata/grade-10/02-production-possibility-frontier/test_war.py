import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def load(c):
    return pd.read_csv(OUT / f"war_{c}.csv").set_index("year")


def test_base_year_and_span():
    for c in ("usa", "gbr"):
        d = load(c)
        assert list(d.index) == list(range(1929, 1951))
        assert d.loc[1939, "gdp_pp"] == 100 and d.loc[1939, "cons_pp"] == 100


def test_the_two_wartime_paths():
    us, uk = load("usa"), load("gbr")
    assert us.loc[1944, "gdp_pp"] > 175 and us.loc[1944, "cons_pp"] > 100   # both rose
    assert uk.loc[1943, "cons_pp"] < 85                                      # consumption fell
    assert us.loc[1939, "unemp"] > 15 and uk.loc[1939, "unemp"] < 7
