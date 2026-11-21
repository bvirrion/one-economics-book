"""Tests of the listings and exercises of b1 ch. 30."""

import importlib.util
import sys
from pathlib import Path

import numpy as np
from econdata import nsw
from scipy import stats

HERE = Path(__file__).resolve().parents[1]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_iterated():
    d = nsw("psid_controls")
    cond = d.groupby("education").re78.mean()
    w = d.education.value_counts(normalize=True)
    assert abs((cond * w).sum() - d.re78.mean()) < 1e-9


def test_t_quantiles():
    rng = np.random.default_rng(2026)
    z = rng.standard_normal(200_000)
    v = (rng.standard_normal((200_000, 5)) ** 2).sum(axis=1)
    t = z / np.sqrt(v / 5)
    for p in (0.9, 0.95, 0.975):
        assert abs(np.quantile(t, p) - stats.t.ppf(p, 5)) < 0.05


def test_clt():
    y = nsw("psid_controls").re78.to_numpy()
    rng = np.random.default_rng(2026)
    for n in (5, 30, 200):
        m = rng.choice(y, size=(10_000, n)).mean(axis=1)
        assert abs(m.std() / (y.std() / np.sqrt(n)) - 1) < 0.03


def test_problem():
    sys.modules.pop("sol", None)
    p = load(HERE / "exercises" / "solutions.py", "sol").problem()
    assert abs(p["lie"] - p["mu"]) < 1e-6
    assert 0.04 < p["t_share"] < 0.07
