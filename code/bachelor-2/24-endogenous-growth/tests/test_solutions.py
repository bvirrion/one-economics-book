"""The numbers the text and solutions of b2 ch. 24 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol24", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_ideas():
    out = subprocess.run(
        [sys.executable, "ideas.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    rows = [line.split() for line in out.splitlines()[1:7]]
    assert rows[0] == ["0", "4.00", "0.980"]
    assert rows[3] == ["50", "2.87", "1.902"]
    assert rows[5] == ["200", "2.15", "3.406"]
    assert "long run: growth 2.00%, level ratio 3.918" in out
    assert (HERE / "outputs" / "ideas.txt").read_text().endswith(out)


def test_exercises():
    assert (
        r(sol.ak_growth(0.2, 0.5, 0.05), 3),
        r(sol.ak_growth(0.25, 0.5, 0.05), 3),
    ) == (
        0.05,
        0.075,
    )
    assert r(sol.semi_growth(0.01, 0.75), 3) == 0.04
    assert r(sol.level_gain(0.5, 0.02, 0.03), 3) == 2.227
    assert r(sol.research_productivity(0.02, 0.01, 4), 3) == 0.125


def test_brenland():
    b = sol.brenland()
    assert (b["g"], b["jump"], b["level_a"]) == (0.02, 0.04, 4.0)
    assert (r(b["level_y"], 3), r(b["drop"], 3)) == (3.918, 0.98)
    assert (r(b["t_half"], 1), r(100 * b["z50"], 2)) == (40.5, 2.87)
    assert (b["g_n0"], r(b["g_phi_075"], 3), r(b["level_phi_075"], 2)) == (
        0.0,
        0.04,
        15.67,
    )


def test_exercise8_phi_075_closed_form():
    # with L = e^{nt}, dA/dt = s L A^phi has the exact solution
    # A^{1-phi}(t) = A0^{1-phi} + (1-phi) s (e^{nt} - 1)/n; no Euler steps involved
    from math import exp, log

    phi, n = 0.75, 0.01
    a0 = (0.02 * (1 - phi) / n) ** (1 / (1 - phi))
    assert a0 == 0.0625

    def a(share, t):
        return (a0 ** (1 - phi) + (1 - phi) * share * (exp(n * t) - 1) / n) ** (
            1 / (1 - phi)
        )

    def growth(share, t):
        return share * exp(n * t) * a(share, t) ** (phi - 1)

    assert r(100 * growth(0.04, 0), 2) == 8.0
    assert abs(100 * growth(0.02, 150) - 4.0) < 1e-9  # baseline stays balanced
    assert abs(100 * growth(0.04, 200) - 4.29) < 0.01
    ratio = [a(0.04, t) * 0.96 / (a(0.02, t) * 0.98) for t in (50, 200)]
    assert abs(ratio[0] - 3.692) < 0.01 and abs(ratio[1] - 11.84) < 0.03
    share50 = log(ratio[0] / 0.98) / log(2**4 * 0.96 / 0.98 / 0.98)
    assert r(share50, 2) == 0.48
