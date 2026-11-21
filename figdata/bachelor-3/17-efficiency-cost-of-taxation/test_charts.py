import numpy as np
from brenland_tax import mcpf_upper, pareto_a, tax
from make_composition import table as comp
from make_laffer import peak, revenue
from make_revenue import table as rev


def test_laffer_peak():
    for e in (0.25, 0.5):
        t = peak(e)
        assert revenue(t, e) > revenue(t - 0.01, e)
        assert revenue(t, e) > revenue(t + 0.01, e)


def test_tax_schedule():
    assert tax(12_000) == 0 and np.isclose(tax(40_000), 5_600)


def test_mcpf_above_one_then_past_the_peak():
    # with e = 0.25 the top rates are below the Laffer peak 1 / (1 + a e) and the
    # marginal cost of public funds exceeds one; with e = 0.5 the peak falls below
    # the lowest top rate, 35 %, and raising the rates loses revenue
    assert mcpf_upper(0.25)[2] > 1
    mech, beh, _ = mcpf_upper(0.5)
    assert beh > mech and 1 / (1 + pareto_a() * 0.5) < 0.35


def test_composition_sums():
    c = comp()
    s = c[["income", "goods", "social", "trade", "other"]].sum(axis=1)
    assert np.allclose(s, 100) and len(c) == 10


def test_revenue_positive():
    v = rev().drop(columns="year").stack().dropna()
    assert len(v) > 800 and (v > 0).all()
