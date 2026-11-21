from make_scholarship import data, tables


def test_design():
    d = data()
    moved = (d.score == 70) & (d.true < 70)
    assert moved.sum() > 20 and (d.teacher[moved]).all()
    assert (d.award[d.score >= 70].mean() > 0.6) and d.award[d.score < 70].mean() < 0.1


def test_density_flags_the_school_and_only_it():
    _, dens = tables()
    t = dict(zip(dens["sample"], dens.theta / dens.se))
    assert t["all"] > 2.5 and abs(t["without the school"]) < 2


def test_fuzzy_ratio_covers_the_truth():
    est, _ = tables()
    r = est[(est.quantity == "earnings") & (est.window == 10)].iloc[0]
    f = est[(est.quantity == "award") & (est.window == 10)].iloc[0]
    assert abs(r.est_all / f.est_all - 0.15) < 2 * r.se_all / f.est_all
