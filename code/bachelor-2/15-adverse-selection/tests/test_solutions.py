"""The numbers the text and solutions of b2 ch. 15 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol15", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_unravelling():
    out = subprocess.run(
        [sys.executable, "unravelling.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "year 3: premium  596.0, share insured 0.608" in out
    assert "welfare lost per person 87.50 dalens a year" in out
    assert (HERE / "outputs" / "unravelling.txt").read_text().endswith(out)


def test_lemons_and_types():
    assert sol.lemons(6000) == (0.6, 3000.0, 3600.0)
    assert sol.two_types() == (2000.0, False, 3000.0, True)
    assert sol.pooling_threshold() == 0.75


def test_curves():
    assert sol.linear_market(900, 500, 800, 600) == (0.5, 650.0, 1.0, 87.5)
    q, premium, q_eff, loss = sol.linear_market(900, 500, 300, -200)
    assert (q, premium, r(q_eff, 3), r(loss, 2)) == (1.0, 400.0, 0.857, 7.14)
    steps = sol.spiral(900, 500, 800, 600, 5)
    assert [(r(p, 1), r(s, 3)) for p, s in steps[3:]] == [
        (617.6, 0.565),
        (630.6, 0.539),
    ]


def test_coop():
    c = sol.coop()
    assert (c["avg"], c["surplus"], c["healthy_lost"], c["sick_surplus"]) == (
        880.0,
        240000,
        120000,
        120000,
    )
    assert (c["q"], c["premium"], c["loss_total"]) == (0.75, 1050.0, 118750.0)
    assert [(r(p, 1), r(s, 3)) for p, s in c["steps"]] == [
        (900.0, 0.9),
        (960.0, 0.84),
        (996.0, 0.804),
    ]
    assert (c["mandate_premium"], c["loser_rank"], c["penalty"]) == (900.0, 0.9, 100)
