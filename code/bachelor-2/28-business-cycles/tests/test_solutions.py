"""The numbers the text and solutions of b2 ch. 28 print, recomputed.

The listing iterates the model; the solutions file uses the closed form; the tests
compare both with values worked by hand.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "code" / "shared"), str(ROOT / "figdata" / "lib")]
spec = importlib.util.spec_from_file_location(
    "sol28", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)
B = sol.BRENLAND


def r(x, n):
    return round(float(x), n)


def test_listing_rbc():
    out = subprocess.run(
        [sys.executable, "rbc.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "rho 0.0: output 1.00 0.33 0.11 0.04 0.01 0.00 0.00 0.00" in out
    assert "rho 0.9: output 1.00 1.23 1.22 1.14 1.03 0.94 0.84 0.76" in out
    assert "sd of c / sd of y 1.00, sd of i / sd of y 1.00" in out
    assert "first-order autocorrelation of output 0.95" in out
    assert (HERE / "outputs" / "rbc.txt").read_text().endswith(out)


def test_closed_form_matches_listing():
    out = (HERE / "outputs" / "rbc.txt").read_text().splitlines()
    row = next(x for x in out if x.startswith("rho 0.9"))
    printed = [float(v) for v in row.split("output")[1].split()]
    assert printed == [r(sol.irf(t, 0.9, 1 / 3), 2) for t in range(8)]
    # by hand: (0.81 - 1/9) / (0.9 - 1/3) = 1.2333
    assert r(sol.irf(1, 0.9, 1 / 3), 4) == 1.2333


def test_brenland():
    a, rho = B["alpha"], B["rho"]
    # by hand: y1 = (0.64 - 0.09) / 0.5 = 1.1, y2 = (0.512 - 0.027) / 0.5 = 0.97
    assert (r(sol.irf(1, rho, a), 4), r(sol.irf(2, rho, a), 4)) == (1.1, 0.97)
    assert [r(sol.irf(t, rho, a), 2) for t in range(3, 7)] == [0.8, 0.65, 0.52, 0.42]
    assert sol.half_life(rho, a)[0] == 5
    total = sum(sol.irf(t, rho, a) for t in range(400))
    assert r(total, 2) == r(1 / ((1 - rho) * (1 - a)), 2) == 7.14
    assert r(sol.steady_k(a, B["beta"]), 4) == 0.1664
    assert tuple(r(x, 3) for x in sol.shares(a, B["beta"])) == (0.285, 0.715)
    assert r(sol.iid_half_life(a), 2) == 0.58
    assert sol.half_life(0.95, a)[:2] == (17, 2)


def test_growth_moments():
    g = sol.growth_moments()
    assert g["consumption"] == (0.79, 0.66) and g["investment"] == (5.33, 0.82)
