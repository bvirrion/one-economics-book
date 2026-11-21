import numpy as np
from make_boom_firms import firms, results
from make_exporters import tables
from make_home_market import share, table
from melitz import cutoffs


def test_exporters_sorted_and_aggregate():
    d, agg = tables()
    assert len(d) == 21 and d.exporting.is_monotonic_decreasing
    assert agg.exporting[0] == 18 and abs(d.firms.sum() - 100) < 0.6


def test_closed_cutoff_and_regimes():
    r = results().set_index("regime")
    assert np.isclose(r.cutoff["closed"], 2.0)
    assert np.isclose(r.export_cutoff["open"] / r.cutoff["open"], 1.8)
    assert r.cutoff["agreement"] > r.cutoff["open"] > r.cutoff["closed"]
    assert np.isclose(r.export_share["open"], 1.8 ** -4)


def test_cutoff_solves_free_entry_on_a_sample():
    sigma, k, f, f_e, tau, fx = 3.0, 4.0, 40.0, 2.5, 1.2, 90.0
    d, x = cutoffs(sigma, k, f, f_e, tau, fx)
    phi = np.random.default_rng(1).pareto(k, 2_000_000) + 1
    prof = np.where(phi >= d, f * ((phi / d) ** 2 - 1), 0)
    prof += np.where(phi >= x, fx * ((phi / x) ** 2 - 1), 0)
    assert abs(prof.mean() / f_e - 1) < 0.03


def test_firms_exit_and_jump():
    d = firms()
    assert d.open.isna().any() and (d.open > d.closed).any()


def test_home_market_magnifies():
    assert share(0.6, 0.5) > 0.6 and np.isclose(share(0.5, 0.2), 0.5)
    assert (table().lam5.diff().dropna() >= 0).all()
