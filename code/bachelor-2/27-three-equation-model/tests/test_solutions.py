"""The numbers the text and solutions of b2 ch. 27 print, recomputed.

The listing iterates period by period; the solutions file uses closed forms; the tests
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
    "sol27", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)
B = sol.BRENLAND


def r(x, n):
    return round(float(x), n)


def test_listing_three_eq():
    out = subprocess.run(
        [sys.executable, "three_eq.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    rows = [line.split() for line in out.splitlines()[1:7]]
    assert rows[0] == ["0", "5.00", "6.00", "11.00"]
    assert rows[1] == ["1", "4.00", "4.67", "8.67"]
    assert rows[5] == ["5", "2.40", "2.53", "4.92"]
    assert "cumulated output loss 6.00, sacrifice ratio 2.00" in out
    assert (HERE / "outputs" / "three_eq.txt").read_text().endswith(out)


def test_closed_forms():
    assert (r(sol.ws_ps(1.1, 5, 0.8), 4), r(sol.ws_ps(1.1, 5, 0.75), 4)) == (0.06, 0.07)
    assert r(sol.ws_ps(1.2, 4, 0.8), 4) == 0.1
    assert sol.taylor1993(4, -1) == 6.5
    assert (sol.decay(1, 1), sol.rule_coef(1, 1, 1)) == (0.5, 0.5)
    assert r(sol.rule_coef(0.5, 0.5, 0.5), 4) == 1.3333
    step = sol.first_step(
        B["pi0"], B["target"], B["alpha"], B["lam"], B["a"], B["r_star"]
    )
    assert tuple(r(v, 4) for v in step) == (4.0, -2.0, 6.0, 11.0)
    step = sol.first_step(5, 2, 0.5, 2, 0.5, 2)
    assert tuple(r(v, 3) for v in step) == (4.667, -0.667, 3.333, 8.333)
    step = sol.first_step(3, 2, 0.5, 0.5, 0.5, 2)
    assert tuple(r(v, 3) for v in step) == (2.667, -0.667, 3.333, 6.333)
    assert (sol.periods_below(3, 0.5, 0.5, 0.5), sol.cumulated_loss(3, 0.5)) == (5, 6.0)
    assert r(sol.stability_factor(0.5, 0.5, 0.5), 3) == 1.125
    assert r(sol.stability_factor(1 + 4 / 3, 0.5, 0.5), 4) == 0.6667
    z = sol.zlb(0.5, 2, 0.5, 0.5, 0.5, 1)
    assert tuple(r(v, 3) for v in z) == (-0.5, 0.0, 1.0, 0.75)


def test_residuals():
    mean, mad = sol.residuals_by_decade()
    assert list(mean) == [-0.49, -4.74, 0.88, -0.21, -2.13]
    assert list(mad) == [1.05, 4.74, 2.52, 1.2, 2.29]
