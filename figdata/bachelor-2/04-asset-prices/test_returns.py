from make_returns import autocorr, cumulative, riskreturn, summary


def test_complete_panel():
    rr = riskreturn()
    assert rr.groupby("asset").size().nunique() == 1 and len(rr) % 3 == 0
    assert cumulative().iloc[0, 1:].eq(1).all()


def test_equities_beat_bills_everywhere():
    p = riskreturn().pivot(index="iso3", columns="asset", values="mean")
    assert (p.equity > p.bill).all() and (p.equity > p.bond).all()


def test_weak_autocorrelation():
    s = summary().iloc[0]
    assert autocorr().rho1.abs().max() < 0.3 and s.n_outside_band <= 3


def test_puzzle_sizes():
    s = summary().iloc[0]
    assert s.usa_gamma_bound > 10 and s.usa_gamma > s.usa_gamma_bound
