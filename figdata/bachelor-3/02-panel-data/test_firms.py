from make_firms import panel, tables


def test_panel_shape_and_subsidy():
    d = panel()
    assert len(d) == 4500 and d.firm.nunique() == 300
    assert d.groupby("firm").treated.first().sum() == 100
    assert d[d.year < 2018].s.sum() == 0


def test_estimates_tell_the_story():
    res, facts = tables()
    r = res.set_index(["model", "coef"])
    assert r.loc[("pooled", "k"), "estimate"] > 0.8          # management bias
    for m in ("within", "first difference", "two-way"):
        assert abs(r.loc[(m, "k"), "estimate"] - 0.30) < 0.06
    tw = r.loc[("two-way", "s")]
    assert abs(tw.estimate - 0.10) < 2 * tw.se_cluster
    assert tw.se_cluster > 1.4 * tw.se_iid                     # serial correlation
    f = facts.iloc[0]
    assert abs(0.30 + 0.5 * f.cov_km / f.var_k - r.loc[("pooled", "k"), "estimate"]) < 0.05
