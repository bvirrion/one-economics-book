"""The numbers the text and solutions of b2 ch. 19 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol19", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_lambda():
    out = subprocess.run(
        [sys.executable, "lambda_iv.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "quarters used 198; first-stage R2 0.072, F 2.46" in out
    assert "OLS slope 0.342" in out
    assert "lambda (instrumented) 0.617, standard error 0.200" in out
    assert (HERE / "outputs" / "lambda_iv.txt").read_text().endswith(out)


def test_life_cycle_and_precaution():
    assert sol.life_cycle() == {"c": 20.0, "saving": 10.0, "peak": 400.0}
    s, _ = sol.precautionary()
    assert r(s, 2) == 11.24
    assert r((-100 + (10000 + 5000) ** 0.5) / 2, 2) == 11.24
    assert r(sol.precautionary(y2=(25.0, 175.0))[0], 2) == 22.89
    assert r(sol.precautionary(y2=(100.0, 100.0))[0], 6) == 0.0
    mean_mu, mu_mean = sol.prudence_gap()
    assert (r(mean_mu, 4), mu_mean) == (0.0133, 0.01)


def test_constraint_and_household():
    assert [sol.constrained(bonus=b) for b in (0, 6, 10, 30)] == [20, 26, 30, 45]
    h = sol.household()
    assert (h["resources"], h["c"], h["saving"], h["wealth_retire"]) == (
        1000.0,
        20.0,
        10.0,
        500.0,
    )
    assert (h["bonus_dc"], h["raise_work_dc"], h["raise_life_dc"]) == (0.2, 1.0, 2.0)
    p = sol.population()
    assert (p["q"], r(p["h"], 3), p["spent"]) == (0.005, 0.296, 360000.0)
    assert (r(p["h_low"], 3), r(p["h_high"], 3), p["mpc_half"]) == (
        0.196,
        0.397,
        0.5025,
    )
    assert r(sol.hand_to_mouth(0.12, 0.005), 3) == 0.116


def test_lambda_variant_and_exercise_two():
    full = sol.lambda_iv()
    assert (r(full["lambda"], 3), r(full["f"], 2)) == (0.617, 2.46)
    only_y = sol.lambda_iv(use_consumption_lags=False)
    assert (r(only_y["lambda"], 2), r(only_y["se"], 2), r(only_y["f"], 2)) == (
        1.05,
        0.51,
        1.27,
    )
    assert r(only_y["r2"], 3) == 0.019
    assert sol.life_cycle(30, 15, 36.0, 90.0) == {
        "c": 26.0,
        "saving": 10.0,
        "peak": 390.0,
    }
