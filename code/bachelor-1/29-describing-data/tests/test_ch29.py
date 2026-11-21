"""Tests of the listings and exercises of b1 ch. 29."""

import importlib.util
from pathlib import Path

import numpy as np
from econdata import nsw
from scipy.stats import skew

EX = Path(__file__).resolve().parents[1] / "exercises"


def load(name):
    spec = importlib.util.spec_from_file_location(name, EX / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_moments_and_cap():
    e = nsw("psid_controls").re78
    assert abs(skew(e[e > 0]) - 1.645) < 0.01
    c = nsw("cps_controls").re78
    assert 0.25 < (c == c.max()).mean() < 0.27


def test_correlation_and_groups():
    d = nsw("psid_controls")
    r = d.re75.corr(d.re78)
    assert -1 <= r <= 1 and abs(r - 0.7315) < 1e-3
    g = d.groupby("education").re78.mean()
    assert abs(g[12] - d[d.education == 12].re78.mean()) < 1e-9


def test_problem():
    p = load("solutions").problem()
    w = p["within"]
    assert w[(True, True)] > w[(True, False)] and w[(False, True)] > w[(False, False)]
    assert p["overall"][True] < p["overall"][False]
    assert abs(p["rebuilt"][True] - p["overall"][True]) < 1


def test_exercises():
    assert load("exo_06").result["alt"] > load("exo_06").result["recorded"]
    assert load("exo_07").step > 0
    assert np.isclose(load("solutions").exercises()["r"], 0.8)
