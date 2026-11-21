"""The numbers the text and solutions of b2 ch. 12 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol12", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_bargaining():
    out = subprocess.run(
        [sys.executable, "bargaining.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "  2 rounds: player 1 gets 0.1000" in out
    assert "infinite horizon:  0.6897" in out
    assert (HERE / "outputs" / "bargaining.txt").read_text().endswith(out)


def test_bargaining():
    assert r(sol.rubinstein(0.95, 0.90), 4) == 0.6897
    assert r(sol.rubinstein(0.9, 0.9), 4) == 0.5263
    assert r(sol.finite(0.9, 0.9, 3), 2) == 0.91
    assert r(sol.finite(0.95, 0.90, 200), 4) == 0.6897


def test_trees():
    assert sol.backward_three() == (2, 2)
    assert sol.entry_game() == (True, "accommodate")
    assert sol.ultimatum_coins() == [(10, 0), (9, 1)]


def test_deterrence():
    d = sol.deterrence(4)
    assert (d["q_deter"], d["deter"], d["accommodate"], d["choice"]) == (
        8.0,
        32.0,
        18.0,
        "deter",
    )
    assert sol.deterrence(1)["deter"] == 20.0
    assert sol.deterrence(0.25)["choice"] == "accommodate"
    assert sol.deterrence(9)["blockaded"] and sol.deterrence(9)["deter"] == 36.0
    assert r(sol.deterrence_threshold(), 3) == 0.772
    assert sol.follower(6, 4) == (3.0, 5.0)


def test_harbour():
    h = sol.harbour()
    assert (r(h["employer"], 1), r(h["union"], 1)) == (724.6, 275.4)
    t = sol.harbour_two_rounds()
    assert (r(t["employer"], 1), r(t["union"], 1)) == (50.0, 950.0)
    s = sol.harbour(beta_u=0.97)
    assert (r(s["employer"], 1), r(s["union"], 1)) == (607.3, 392.7)
    assert r(sol.harbour(outside=200)["union"], 1) == 275.4
    assert r(sol.harbour(outside=350)["union"], 1) == 350.0
    u = sol.harbour_union_first()
    assert (r(u["union"], 1), r(u["employer"], 1)) == (289.9, 710.1)
    assert r(sol.harbour(beta_u=0.90)["union"], 1) == 152.5
