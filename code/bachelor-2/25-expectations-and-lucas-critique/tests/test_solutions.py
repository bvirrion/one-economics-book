"""The numbers the text and solutions of b2 ch. 25 print, recomputed."""

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "code" / "shared"), str(ROOT / "figdata" / "lib")]
spec = importlib.util.spec_from_file_location(
    "sol25", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)
B = sol.BRENLAND
A, K, LAM, S2 = B["a"], B["k"], B["lam"], B["sigma2"]


def r(x, n):
    return round(float(x), n)


def test_listing_lucas():
    env = {**os.environ}
    out = subprocess.run(
        [sys.executable, "lucas.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
        env=env,
    ).stdout
    assert "u = 8.92 -1.91 x inflation" in out
    assert "promises u = 1.27 at 4% inflation" in out
    assert "inflation 3.81%, unemployment 5.38%" in out
    assert "re-estimated: u = 13.25 -2.06 x inflation" in out
    assert (HERE / "outputs" / "lucas.txt").read_text().endswith(out)


def test_bias_model():
    assert sol.bias(LAM, A, K) == 1.0
    assert tuple(r(x, 2) for x in sol.responses(LAM, A)) == (0.4, 0.8)
    assert r(sol.expected_loss(LAM, LAM, A, K, S2), 2) == 4.1
    assert r(sol.commitment_loss(LAM, A, K, S2), 2) == 3.6
    assert r(sol.expected_loss(0, LAM, A, K, S2), 2) == 4.0
    assert (
        r(sol.expected_loss(1, 1, A, K, 0), 2),
        sol.commitment_loss(1, A, K, 0),
    ) == (
        2.5,
        2.0,
    )
    w = sol.best_weight(LAM, A, K, S2)
    assert r(w, 3) == 0.425
    assert r(sol.expected_loss(w, LAM, A, K, S2), 3) == 3.798
    assert tuple(r(x, 2) for x in sol.responses(w, A)) == (0.19, 0.9)
    assert r(sol.expected_loss(0.5, LAM, A, K, S2), 3) == 3.804


def test_decades():
    med, top, who = sol.decade_inflation()
    assert list(med) == [3.8, 3.6, 9.0, 7.1, 2.4, 2.1, 1.3]
    assert (top[1970], who[1970], top[1980]) == (18.9, "PRT", 17.4)


def test_best_weight_moves():
    assert r(sol.best_weight(LAM, A, K, 16), 2) == 0.71
    assert r(sol.best_weight(LAM, A, 4, S2), 2) == 0.18
