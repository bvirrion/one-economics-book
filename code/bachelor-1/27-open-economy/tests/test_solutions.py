"""Check the printed numbers of b1 ch. 27."""

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_accounts():
    a = sol.accounts()
    assert a["nx"] == a["S_minus_I"] == 1113


def test_models():
    assert sol.long_run(4)["eps"] == 1.1 and sol.long_run(3, 10)["eps"] == 0.8
    assert sol.mf(dG=10)["e"] == 0.8 and sol.mf(dG=10, peg=True)["Y"] - 393.264 > 24.9
    assert sol.attack()["premium"] == 79.6
