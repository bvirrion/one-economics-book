import numpy as np
from make_bandwidth import table as bandwidth
from make_elections import tables as elections
from make_maimonides import rule, tables as maimonides
from make_scores import table as scores


def test_opening_fit_jumps_by_about_the_calibration():
    _, fit = elections()
    left = fit[(fit.side == "left") & (fit.margin == 0)].fit.iloc[0]
    right = fit[(fit.side == "right") & (fit.margin == 0)].fit.iloc[0]
    assert abs(right - left - 0.077) < 0.015


def test_bandwidth_tradeoff():
    t = bandwidth().set_index("h")
    assert t.const_mean.is_monotonic_increasing          # bias grows with the window
    assert (t.lin_sd.diff().dropna() < 0).all()          # noise falls with the window
    assert abs(t.lin_mean[0.1] - 0.077) < 0.003


def test_rule_values():
    assert rule(np.array([40, 41, 80, 81]))[0] == 40
    assert np.allclose(rule(np.array([41, 80, 81])), [20.5, 40, 27])
    _, schools = maimonides()
    assert schools.enrol.min() == 15 and schools.enrol.max() == 130


def test_scores_moved_only_onto_70():
    t = scores().set_index("score")
    assert (t.clean.sum() - t.remarked.sum()) >= 0
    diff = (t.remarked - t.clean)
    assert diff[70] > 0 and (diff[66:69] <= 0).all() and (diff.drop(range(66, 71)) == 0).all()
