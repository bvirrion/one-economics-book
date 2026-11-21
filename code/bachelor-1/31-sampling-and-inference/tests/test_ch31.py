"""Tests of the listings and exercises of b1 ch. 31."""

import importlib.util
from pathlib import Path

import numpy as np
from country import load
from econdata import nsw

HERE = Path(__file__).resolve().parents[1]


def load_mod(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_nsw_difference():
    d = nsw("nsw_dw")
    diff = d[d.treat == 1].re78.mean() - d[d.treat == 0].re78.mean()
    assert 1_600 < diff < 2_000 and abs(diff - 1794.3) < 1


def test_bonferroni_and_weights():
    assert 0.05 / 20 == 0.0025
    h = load("households")
    rng = np.random.default_rng(2026)
    parts = [h[h.owner == k].sample(150, random_state=rng) for k in (1, 0)]
    s = np.concatenate([p.disposable for p in parts])
    w = np.repeat([h.owner.sum() / 150, (1 - h.owner).sum() / 150], 150)
    truth = h.disposable.mean()
    assert abs((w * s).sum() / w.sum() - truth) < abs(s.mean() - truth)


def test_problem():
    p = load_mod(HERE / "exercises" / "solutions.py", "sol31").problem()
    assert abs(p["true"] - 6.0) < 1e-9
    assert p["n_need"] > 3 * 12_000
