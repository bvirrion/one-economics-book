import numpy as np
from brenland import accelerations, beta_hat, sectors, series
from make_agri import table as agri
from make_convergence import tables as conv
from make_decades import tables as decades
from make_paths import table as paths


def test_brenland_series_by_hand():
    s = series()
    # 2000 back to 1975: 5 years at 2 %, 14 at 4 %, 6 at 0.5 %
    assert np.isclose(s[1975], s[2000] * np.exp(-(5 * 0.02 + 14 * 0.04 + 6 * 0.005)))
    assert len(s) == 51 and [a[0] for a in accelerations(s)] == [1981]


def test_beta_recovers_a_known_line():
    y = np.array([1000.0, 2000, 4000, 8000])
    g = 100 * (0.1 - 0.01 * np.log(y))
    assert np.allclose(beta_hat(y, g), [0.1, -0.01])


def test_sector_identity_by_hand():
    s = sectors()
    # 0.2 x 6 + 0.8 x 16 = 14 and 0.05 x 12 + 0.95 x 36 = 34.8
    assert np.isclose(s["agg75"], 14) and np.isclose(s["agg25"], 34.8)
    assert np.isclose(s["within"] + s["between"] + s["cross"], 20.8)


def test_data_charts():
    d, med, st = decades()
    assert list(st.n) == sorted(st.n) and len(med) == 6
    c, fits, cs = conv()
    assert cs.set_index("sample").loc["rich", "slope"] < 0 and len(c) > 100
    assert agri().agri.between(0, 100).all()
    assert paths().year.min() == 1900
