import numpy as np
from brenland import stats
from make_estimates import tables as est
from make_mincer import tables as mincer


def test_iv_mostly_above_ols():
    _, st = est()
    assert st.set_index("stat").value["iv_above"] >= 8


def test_mincer_concave():
    _, _, st = mincer()
    v = st.set_index("stat").value
    assert v["b_exp"] > 0 > v["b_exp2"] and 0.03 < v["b_school"] < 0.12


def test_wald_is_ratio():
    s = stats()
    assert np.isclose(s["first_stage"],
                      s["complier_share"] / 100 * s["complier_gain"])
    assert s["social"] < s["private"]


def test_adjusted_means_sit_on_the_fit_on_average():
    means, fit, st = mincer()
    m = means.merge(fit.rename(columns={"lw": "fit"}), on="education")
    gap = ((m.adj - m.fit) * m.n).sum() / m.n.sum()
    assert abs(gap) < 0.05
    s = st.set_index("stat").value
    assert s["jump12"] > 10 * s["median_step"] and s["p_linear"] < 0.001
