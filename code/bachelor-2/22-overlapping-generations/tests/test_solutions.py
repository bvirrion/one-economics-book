"""The numbers the text and solutions of b2 ch. 22 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol22", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_olg():
    out = subprocess.run(
        [sys.executable, "olg.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert (
        "contribution 0.0: k = 3.059, wage 9.790, gross return 1.371 (1 + n = 1.2)"
        in out
    )
    assert (
        "contribution 1.0: k = 2.059, wage 8.693, gross return 1.810 (1 + n = 1.2)"
        in out
    )
    assert (HERE / "outputs" / "olg.txt").read_text().endswith(out)


def test_exercises():
    assert r(sol.steady_k(1 / 3, 1, 0), 3) == 0.192
    assert r(sol.ratio_r_to_growth(1 / 3, 1), 6) == 1.0
    assert r(sol.ratio_r_to_growth(0.3, 1), 3) == 0.857
    assert r(sol.ratio_r_to_growth(0.3, 0.6), 3) == 1.143
    assert r(100 * sol.per_year(1.01**30 * 1.015**30), 2) == 2.52
    c = sol.contributions_2025()
    assert [r(100 * c[k], 2) for k in ("JPN", "ITA", "KOR", "USA", "NGA")] == [
        25.5,
        19.85,
        14.65,
        14.25,
        2.7,
    ]


def test_brenland():
    b = sol.brenland()
    assert (r(b["k"], 3), r(b["w"], 3), r(b["R"], 3)) == (3.059, 9.79, 1.371)
    assert (r(b["s"], 3), r(b["c_young"], 3), r(b["c_old"], 3)) == (
        3.671,
        6.119,
        5.035,
    )
    assert (r(100 * b["r_year"], 2), r(100 * b["n_year"], 2)) == (1.06, 0.61)
    assert r(b["k_golden"], 3) == 3.702
    assert (r(b["w_payg"], 3), r(b["R_payg"], 3), r(b["s_payg"], 3)) == (
        8.694,
        1.81,
        2.471,
    )
    assert (b["pension"], r(b["implicit_tax"], 3)) == (1.2, 0.337)
    assert (r(b["tau_now"], 3), r(b["tau_2050"], 3)) == (0.15, 0.225)
    assert (r(b["repl_kept"], 3), r(b["tau_later_retire"], 3)) == (0.333, 0.175)
