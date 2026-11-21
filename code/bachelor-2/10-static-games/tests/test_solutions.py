"""The numbers the text and solutions of b2 ch. 10 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol10", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_dominance():
    out = subprocess.run(
        [sys.executable, "dominance.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "survivors: ['U'] ['L']" in out
    assert "[('U', 'L')]" in out
    assert (HERE / "outputs" / "dominance.txt").read_text().endswith(out)


def test_games():
    assert sol.iesds(*sol.EX1) == ([0], [1])
    assert sol.pure_nash(*sol.EX2) == [(0, 0), (1, 1), (2, 2)]
    assert sol.pure_nash(*sol.PENNIES) == []


def test_cournot_public_good():
    assert [sol.cournot(n)[2] for n in (1, 2, 4, 9)] == [55, 40, 28, 19]
    assert [sol.cournot(n)[0] for n in (1, 2, 4, 9)] == [45, 30, 18, 9]
    assert sol.public_good(2)[:3] == (4, 8, 12)
    assert sol.public_good(3)[:3] == (3, 9, 18)
    assert [r(sol.public_good(n)[3], 2) for n in (2, 4, 10)] == [0.67, 0.4, 0.18]
    assert sol.vcm() == (20, 32, 0.4, 1.6)


def test_commons():
    c2 = sol.commons(2)
    assert r(c2["E"], 2) == 53.33 and r(c2["over"], 2) == 0.33 and c2["fee"] == 20
    c5 = sol.commons(5)
    assert r(c5["e"], 2) == 13.33 and r(c5["E"], 2) == 66.67
    assert r(c5["value"], 2) == 33.33 and r(c5["profit_boat"], 2) == 177.78
    assert r(c5["profit_total"], 2) == 888.89 and c5["profit_star"] == 1600
    assert r(c5["over"], 3) == 0.667 and c5["fee"] == 32
    f = sol.commons(5, fee=32)
    assert f["E"] == 40 and f["profit_boat"] == 64
    assert sol.quota_deviation() == (24, 576, 320, 256)
    assert [r(x, 2) for x in sol.hotelling()] == [0.45, 0.55, 0.5]
