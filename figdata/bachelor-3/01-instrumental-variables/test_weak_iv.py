import numpy as np
from make_weak_iv import EDGES, tables


def test_densities_integrate_to_the_share_inside_the_window():
    dens, _, _ = tables()
    # 2SLS with one instrument has no finite mean: at F near 2 a large share of the
    # estimates falls outside the window, and the share inside rises with F.
    mass = {c: dens[c].sum() * 0.05 for c in ("f2", "f10", "f50")}
    assert all(m <= 1.0 + 1e-9 for m in mass.values())
    assert 0.6 < mass["f2"] < mass["f10"] < mass["f50"] and mass["f50"] > 0.99
    assert len(dens) == len(EDGES) - 1


def test_weak_case_is_centred_toward_ols_strong_case_at_zero():
    dens, _, ols = tables()
    mode = lambda c: dens.mid[dens[c].idxmax()]  # noqa: E731
    assert abs(mode("f50")) < 0.1
    assert mode("f2") > 0.2
    assert 0.7 < ols.ols[0] < 0.85


def test_size_falls_toward_five_percent():
    _, size, _ = tables()
    r = size.set_index("F").reject
    assert r[1.5] > 0.10 and abs(r[100] - 0.05) < 0.015
    assert np.all(np.diff(r.loc[[1.5, 3, 10, 50]].values) < 0.01)
