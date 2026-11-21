import numpy as np
from make_loglik import counts, tables as loglik
from make_work import tables as work


def test_lpm_leaves_the_unit_interval_and_logit_does_not():
    _, fits = work()
    assert fits.lpm.max() > 1 and fits.logit.max() < 0.98 and fits.probit.max() < 0.98


def test_newton_reaches_the_log_odds_of_the_share():
    n1, n = counts()
    _, steps = loglik()
    assert abs(steps.b.iloc[-1] - np.log(n1 / (n - n1))) < 1e-6
    assert (np.diff(steps.ll) >= 0).all()
