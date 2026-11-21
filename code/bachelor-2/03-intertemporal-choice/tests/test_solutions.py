"""The numbers the solutions and the listing of b2 ch. 3 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol03", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_listing_plans():
    out = subprocess.run(
        [sys.executable, "life_plan.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "beta(1+r) = 1.00" in out and "beta(1+r) = 0.74" in out
    assert out.count("28.3") == 6
    assert (HERE / "outputs" / "life_plan.txt").read_text().endswith(out)


def test_one_star():
    assert round(sol.ex_pv(), 1) == 114689.3
    e = sol.ex_euler_log()
    assert round(e["c0"], 1) == 41025.6 and round(e["c1"], 1) == 40923.1
    assert round(e["save"], 1) == -1025.6


def test_growth_and_rates():
    g = sol.ex_crra_growth()
    assert g["approx"] == 0.01 and round(100 * g["exact"], 3) == 0.976
    r = sol.ex_rate_rise()
    assert [round(x) for x in r[2.0]] == [50880, 51238]
    assert [round(x) for x in r[1.0]] == [51020, 51020]
    assert [round(x) for x in r[0.5]] == [51302, 50584]


def test_borrowing():
    b = sol.ex_borrowing()
    assert round(b["c0"]) == 39560 and b["mrs"] == 3.0
    assert round(b["lam"], 4) == 0.8645 and round(b["cost"]) == 10456


def test_cake():
    c = sol.ex_cake()
    assert (c["c0"], c["c1"], c["c2"], c["c1_planned"]) == (45000, 30000, 15000, 22500)


def test_problem():
    p = sol.problem()
    assert p["pv"] == 75840 and round(p["c"]) == 31082
    assert round(p["b0"]) == -7082 and round(p["b1"]) == 20066
    assert abs(p["check"]) < 1e-6
    assert round(p["c05"]) == 27322 and round(p["c1_lim"]) == 36000
    assert round(p["cbar"]) == 30488 and round(p["cost_per"]) == 594
    assert round(p["cost_pv"]) == 1448
    assert round(p["s0"]) == 37769 and round(p["s1"]) == 30506
    assert round(p["s2"]) == 21354 and round(p["commit"]) == 26438
    assert round(p["value"]) == 740 and p["lr_c"] > p["lr_no"]
