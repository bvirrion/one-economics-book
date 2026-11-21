"""The numbers the text and solutions of b2 ch. 11 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol11", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_penalty_play():
    out = subprocess.run(
        [sys.executable, "penalty_play.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "kick left 0.3636, cover left 0.4545, scoring rate 0.7909" in out
    assert (HERE / "outputs" / "penalty_play.txt").read_text().endswith(out)


def test_games():
    assert [r(x, 4) for x in sol.zero_sum_value(sol.PK)] == [0.3636, 0.4545, 0.7909]
    _, after = sol.better_goalie()
    assert [r(x, 3) for x in after] == [0.308, 0.385, 0.777]
    assert [r(x, 3) for x in sol.battle()] == [0.667, 0.333, 0.667, 0.667]
    assert [r(x, 3) for x in sol.serve_game()] == [0.533, 0.667, 0.65]
    assert r(sol.pearson(33, 26, 20, 22), 2) == 4.09


def test_inspection():
    a = sol.inspection()
    assert (a["audit"], a["evade"], a["mixed"], a["commit"]) == (0.4, 0.2, 800, 820)
    assert a["threshold"] == 1000 and a["revenue"] == 1000
    b = sol.inspection(fine=4000)
    assert (b["audit"], b["evade"], b["commit"]) == (0.2, 0.2, 860)
    c = sol.inspection(fine=500)
    assert r(c["audit"], 4) == 0.6667 and r(c["commit"], 2) == 766.67
