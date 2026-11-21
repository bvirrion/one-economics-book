"""The numbers the text and solutions of b1 ch. 3 print."""

import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "sol03", Path(__file__).resolve().parents[1] / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_text_and_exercises():
    assert sol.linear_tax() == {"p": 20, "q": 60, "pass": 0.6}
    assert sol.linear_tax(tau=5)["q"] == 54
    f = sol.tax_figure()
    assert f["inelastic"]["p1"] == pytest.approx(24.2857, abs=1e-4)
    assert f["inelastic"]["q1"] == pytest.approx(57.857, abs=1e-3)
    assert f["elastic"]["eps_d"] == pytest.approx(-2 / 3)
    assert sol.pass_through(-0.3, 1.2) == pytest.approx(0.8)
    assert sol.ex_ce()["q4"] == 25 and round(sol.ex_ce()["q4_4"], 2) == 23.84
    assert sol.ex_envelope() == {"x": 2, "V": 4, "dV": 2}
    m = sol.monopoly_pass()
    assert (m["p0"], m["p1"], m["pass"]) == (20, 22, 2)


def test_cement():
    c = sol.cement()
    assert c["pass"] == 0.7059 and c["dp_first"] == 7.06
    assert (c["p_exact"], c["q_exact"], c["ps_exact"]) == (107.16, 966.0, 97.16)
    assert (c["p_lin"], c["q_lin"]) == (107.06, 964.7) == (c["p_first"], c["q_first"])
    assert (c["profit_loss_first"], c["profit_loss_exact"]) == (2940, 2792)
    assert c["levy_revenue_exact"] == 9660 and c["spend_after_exact"] == 103517
    assert c["buyers_loss_first"] == 7060
    assert c["dq_first_pct"] == -3.53 and c["spend_first_pct"] == 3.53
