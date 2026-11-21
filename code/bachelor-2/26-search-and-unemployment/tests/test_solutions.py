"""The numbers the text and solutions of b2 ch. 26 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol26", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)
L, B = sol.LISTING, sol.BRENLAND


def r(x, n):
    return round(float(x), n)


def test_listing_dmp():
    out = subprocess.run(
        [sys.executable, "dmp.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "tightness 0.529, job finding 0.509, unemployment 5.56%, wage 0.9647" in out
    assert "tightness 0.436, job finding 0.462, unemployment 6.10%, wage 0.9679" in out
    assert "z 0.4: a 1% rise in p raises tightness by 1.8%" in out
    assert "z 0.9: a 1% rise in p raises tightness by 11.6%" in out
    assert (HERE / "outputs" / "dmp.txt").read_text().endswith(out)


def test_exercises():
    assert r(sol.steady_u(0.03, 0.5), 4) == 0.0566
    m, theta, f, q = sol.matches(0.7, 0.06, 0.03)
    assert (r(m, 4), theta, r(f, 3), r(q, 3)) == (0.0297, 0.5, 0.495, 0.99)
    assert r(sol.wage(0.5, 0.4, 1, 1, 0.529), 4) == 0.9645
    o = sol.outcome(1, 0.4, L["a"], 0.7, L["c"], L["r"], L["s"])
    assert (r(o["theta"], 3), r(100 * o["u"], 2), r(o["w"], 4)) == (0.224, 8.3, 0.977)
    o = sol.outcome(1, 0.4, L["a"], 0.5, L["c"], L["r"], L["s"])
    assert r(sol.elasticity(1, 0.4, 0.5, o["f"], L["r"], L["s"]), 2) == 1.77
    o = sol.outcome(1, 0.9, L["a"], 0.5, L["c"], L["r"], L["s"])
    assert r(sol.elasticity(1, 0.9, 0.5, o["f"], L["r"], L["s"]), 1) == 11.5


def test_brenland():
    o = sol.outcome(**B)
    assert (r(o["x"], 6), r(o["theta"], 6), r(o["f"], 6), r(o["q"], 6)) == (
        0.8,
        0.64,
        0.48,
        0.75,
    )
    assert (r(100 * o["u"], 2), r(100 * o["v"], 2), r(o["w"], 4)) == (9.43, 6.04, 0.96)
    o = sol.outcome(**dict(B, z=0.7))
    assert (r(o["theta"], 3), r(o["f"], 3), r(100 * o["u"], 1), r(o["w"], 3)) == (
        0.464,
        0.409,
        10.9,
        0.966,
    )
    o = sol.outcome(**dict(B, p=1.02))
    assert (r(o["theta"], 3), r(100 * o["u"], 2)) == (0.676, 9.21)
    assert r(sol.elasticity(1, 0.6, 0.5, 0.48, 0.01, 0.05), 2) == 2.78


def test_bisection_matches_closed_form():
    """The listing solves by bisection; the solutions file by the quadratic formula."""
    out = (HERE / "outputs" / "dmp.txt").read_text()
    for z, line in (
        (0.4, "p 1.00 z 0.4"),
        (0.5, "p 1.00 z 0.5"),
        (0.9, "p 1.00 z 0.9"),
    ):
        o = sol.outcome(1.0, z, L["a"], 0.5, L["c"], L["r"], L["s"])
        row = next(x for x in out.splitlines() if x.startswith(line))
        assert f"tightness {o['theta']:.3f}" in row
        assert f"unemployment {100 * o['u']:.2f}%" in row
