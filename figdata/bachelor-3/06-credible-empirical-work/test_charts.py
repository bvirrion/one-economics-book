import numpy as np
from make_exaggeration import ratio, table
from make_filter import tables
from make_funnel import table as funnel


def test_filter_published_heap_above_196():
    h, m = tables()
    below = h[(h.z > 1.5) & (h.z < 1.96)].published.sum()
    above = h[(h.z > 1.96) & (h.z < 2.5)].published.sum()
    assert above > 2 * below
    assert (h.published <= h["all"]).all()


def test_exaggeration_known_values():
    assert abs(ratio(0.2) - 2.25) < 0.01
    assert table().ratio.is_monotonic_decreasing


def test_funnel_matches_listing():
    f = funnel()
    assert f.published.sum() == 138
    assert np.isclose(f[f.published == 1].est.mean(), 0.145, atol=0.0005)


def test_studies_literature_is_selected():
    from make_studies import tables as st
    d, s = st()
    assert len(d) == 20 and (d.est / d.se > 1.96).mean() > 0.3
    s = s.set_index("stat")
    assert s.est["simple mean"] > s.est["inverse-variance mean"] > s.est["PET (effect at s.e. 0)"]
