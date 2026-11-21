"""The numbers the solutions of b1 ch. 4 print."""

import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "sol04", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_rankings():
    r = sol.rankings()
    assert r["R"][0] > r["P"][0] == r["Q"][0] > r["S"][0]
    assert r["Q"][1] > r["R"][1] > r["P"][1] > r["S"][1]
    assert r["Q"][1] == 10.318 and r["R"][1] == 9.592 and r["P"][1] == 8.159


def test_trade():
    t = sol.trade()
    assert t["r"] == 1.4 and t["t"] == 2.714 and t["milk"] == 3.8
    assert t["ana"] == (5.2, 3.714) and t["ben"] == (4.8, 4.286)
    assert t["mrs_a"] == t["mrs_b"] == 1.4
    assert (t["u_a0"], t["u_a1"]) == (3.0, 4.395)
    assert (t["u_b0"], t["u_b1"]) == (12.675, 13.532)
    assert (t["swap_a"], t["swap_b"]) == (3.742, 13.751)
    assert t["mrs_a0"] == 9 and t["mrs_b0"] == 0.857
    assert sol.ex_mrs_cd() == pytest.approx(3 / 7)
