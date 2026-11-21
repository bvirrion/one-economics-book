"""The numbers the text and solutions of b2 ch. 7 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol07", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(x, n)


def test_listing_second_theorem():
    out = subprocess.run(
        [sys.executable, "second_theorem.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "transfer A -> B    2.000 units of good 2" in out
    assert "A gets (4.000, 5.714)" in out
    assert (HERE / "outputs" / "second_theorem.txt").read_text().endswith(out)


def test_text():
    c = sol.crusoe()
    assert r(c["L"], 3) == 5.333 and r(c["c"], 3) == 9.238
    assert r(c["w"], 3) == 0.866 and r(c["profit"], 3) == 4.619
    n = sol.nonconvex()
    assert r(n["L"], 3) == 6.667 and r(n["c"], 3) == 4.444
    assert r(n["w"], 3) == 1.333 and r(n["profit"], 3) == -4.444


def test_exercises():
    g = sol.ex_gap()
    assert r(g["share"], 2) == 0.28
    assert sol.ex_profit() == {"L": 9.0, "y": 6.0, "profit": 9.0}
    c = sol.crusoe(a=2 / 3)
    assert r(c["L"], 6) == 8 and r(c["c"], 2) == 11.31 and r(c["w"], 3) == 0.707
    t = sol.ex_tech()
    assert r(t["after"]["c"] / t["before"]["c"], 6) == 1.25
    assert t["after"]["L"] == t["before"]["L"]
    e = sol.ex_transfer()
    assert r(e["x2"], 6) == 7.5 and r(e["p"], 6) == 1.25 and r(e["T"], 6) == 3
    assert [r(x, 6) for x in e["xb"]] == [4, 2.5]


def test_problem():
    p = sol.problem()
    road, rail = p["road"], p["rail"]
    assert (road["pa"], road["pb"], road["x"], road["q"]) == (8, 14, 60, 80)
    assert p["labour"] == 320 and road["ps"] == 320 and road["total"] == 520
    assert [r(rail[k], 2) for k in ("pa", "pb", "x", "q", "q_a")] == [
        9.33,
        11.33,
        86.67,
        93.33,
        6.67,
    ]
    assert r(rail["total"], 2) == 813.33 and r(p["gain"], 2) == 293.33
    assert p["pe"] == 0.5 and p["xa_e"] == (50, 25)
    tr = p["transfer"]
    assert r(tr["x2"], 2) == 18.18 and r(tr["p"], 4) == 0.4545 and r(tr["T"], 6) == -10
