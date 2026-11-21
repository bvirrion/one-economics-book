"""Tests of the exercises and weekend problem of b1 ch. 28."""

import importlib.util
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "exercises"


def load(name):
    spec = importlib.util.spec_from_file_location(name, EX / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_problem():
    p = load("solutions").problem()
    assert p["missing"] == [2021] and p["dup"] == 1
    assert p["max_err"] < 0.002 and p["real"] < p["nominal"]


def test_exercises():
    e = load("solutions").exercises()
    assert e["toy"] == [2.0, -1.0, -2.0, 1.0]
    assert abs(e["annualise"] - 4.91) < 0.01


def test_data_exercises():
    assert load("exo_05").counts["both"] > 150
    assert load("exo_06").rebased.loc[2025] == 100
    r = load("exo_09").rates
    assert r["per_person"] < r["real"] < r["nominal"]
    f, _ = load("exo_10").adjust_q(load("exo_10").known_series()[0])
    assert abs(f[3] - 1.03 / 1.0) < 0.01
    assert load("exo_11").bad.rgdpe.notna().sum() == 0
