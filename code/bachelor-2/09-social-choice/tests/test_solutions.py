"""The numbers the text and solutions of b2 ch. 9 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol09", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_listing_condorcet_random():
    out = subprocess.run(
        [sys.executable, "condorcet_random.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "3 candidates, no winner: random 0.092" in out
    assert out.count("single-peaked 0.000") == 3
    assert (HERE / "outputs" / "condorcet_random.txt").read_text().endswith(out)


def test_exercises():
    assert sol.condorcet_winner(sol.EX1) is None
    pw = sol.pairwise(sol.EX1)
    assert (pw["A", "B"], pw["B", "C"], pw["C", "A"]) == (3, 4, 3)
    assert sol.condorcet_winner(sol.EX5) == "A"
    assert sol.borda(sol.EX5) == {"A": 6, "B": 7, "C": 2}
    assert sol.borda(sol.EX5_BURY) == {"A": 6, "C": 5, "B": 4}
    s = sol.STATES
    assert sol.pareto_better(s["y"], s["x"])
    assert not sol.pareto_better(s["z"], s["x"])
    assert not sol.pareto_better(s["z"], s["y"])
    on_a, on_b, ab, b_val, a_val, ba = sol.ex8()
    assert on_a and on_b and ab and ba and round(b_val, 2) == 2.83
    t = [round(x, 2) for x in sol.transfers()]
    assert t == [27.5, 52.5, 42.0, 33.33, 46.67, 46.67]
    assert sol.median_shift() == (30.0, 40.0)
    assert [sol.single_peaked(r, "LMR") for r in ["LMR", "MRL", "RLM"]] == [
        True,
        True,
        False,
    ]


def test_problem():
    p = sol.problem()
    assert p["plurality"] == {200: 1, 400: 2, 600: 3, 800: 1}
    assert p["borda"] == {200: 6, 400: 13, 600: 15, 800: 8}
    assert p["winner"] == 600 and p["single_peaked"]
    assert p["pairwise_600"] == {200: 5, 400: 4, 800: 6}
    assert p["median"] == 520 and p["median_swap"] == 640
    assert p["winner_swap"] == 600
    assert p["borda_bury_one"][600] == 14 and p["borda_bury_one"][400] == 13
    assert p["borda_bury_two"] == {200: 7, 400: 13, 600: 12, 800: 10}
    pairs, a1, a2, a3 = sol.part4()
    assert pairs == {"XY": 5, "XZ": 3, "YZ": 5}
    assert (a1, a2, a3) == ("Z", "X", "Y")
