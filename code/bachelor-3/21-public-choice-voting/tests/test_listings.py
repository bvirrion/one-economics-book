import math


def test_condorcet(run):
    out, _ = run("condorcet")
    rows = [line.split() for line in out.splitlines()]
    any3, any301 = float(rows[0][4].rstrip(",")), float(rows[2][4].rstrip(","))
    # by counting: with 3 voters, 12 of the 6^3 = 216 profiles cycle
    assert abs(any3 - 12 / 216) < 0.006
    # Guilbaud's limit for many voters: 1/4 - (3 / (2 pi)) arcsin(1/3) = 0.0877
    assert abs(any301 - (0.25 - 1.5 / math.pi * math.asin(1 / 3))) < 0.008
    # single-peaked preferences never cycle (the median-voter theorem)
    assert all(float(r[7].rstrip(",")) == 0 for r in rows)
