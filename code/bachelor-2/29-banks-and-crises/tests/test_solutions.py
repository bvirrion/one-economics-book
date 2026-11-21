"""The numbers the text and solutions of b2 ch. 29 print, recomputed.

The listing and the solutions file both use the closed-form contract; the tests check
it against the budget constraint and first-order condition directly, and against hand
values.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "code" / "shared"), str(ROOT / "figdata" / "lib")]
spec = importlib.util.spec_from_file_location(
    "sol29", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)
B = sol.BRENLAND


def r(x, n):
    return round(float(x), n)


def test_listing_dd():
    out = subprocess.run(
        [sys.executable, "dd.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    rows = [line.split() for line in out.splitlines()[1:4]]
    assert rows[1] == ["2", "1.282", "1.812", "0.561", "0.780"]
    assert rows[2] == ["4", "1.437", "1.709", "0.392", "0.696"]
    assert "withdrawals 0.60: waiting pays 1.155, running 1.282" in out
    assert (HERE / "outputs" / "dd.txt").read_text().endswith(out)


def test_contract_from_first_principles():
    pi, rr, g = B["pi"], B["r"], B["g"]
    c1, c2 = sol.contract(pi, rr, g)
    assert abs(pi * c1 + (1 - pi) * c2 / rr - 1) < 1e-12  # budget
    assert abs(c1 ** (-g) - rr * c2 ** (-g)) < 1e-12  # first-order condition
    # by hand: c1 = 1 / (0.25 + 0.75 / sqrt(2)) = 1.2815
    assert (r(c1, 4), r(c2, 4)) == (1.2815, 1.8123)
    assert sol.expected_utility(pi, 1, 2, g) == -0.625
    assert r(sol.expected_utility(pi, c1, c2, g), 4) == -0.6089
    assert (r(sol.run_threshold(c1, rr), 4), r(sol.bank_empty(c1), 4)) == (
        0.5607,
        0.7803,
    )
    assert r(sol.wait_payoff(c1, rr, 0.25), 4) == r(c2, 4)
    # what a run loses: resources paid in the good equilibrium, by hand 0.3204 + 1.3592
    assert r(pi * c1 + (1 - pi) * c2, 3) == 1.680
    assert (r(sol.wait_payoff(c1, rr, 0.5), 3), r(sol.wait_payoff(c1, rr, 0.6), 3)) == (
        1.437,
        1.155,
    )
    assert tuple(r(x, 3) for x in sol.contract(pi, 1.5, g)) == (1.160, 1.420)
    assert r(sol.run_threshold(1.1596, 1.5), 3) == 0.587
    assert sol.contract(pi, rr, 1) == (1.0, 2.0)
    assert tuple(r(x, 4) for x in sol.contract(0.5, 2, 2)) == (1.1716, 1.6569)
    assert r(sol.run_threshold(1.1716, 2), 3) == 0.707
    assert (sol.leverage_loss(4, 100, 0.02), sol.leverage_loss(10, 100, 0.02)) == (
        0.5,
        0.2,
    )


def test_d_exercise():
    per, mean, n = sol.crises_and_credit()
    assert sum(per.values()) == 88 and per[1930] == 14
    assert (float(mean), n) == (13.35, 63)
