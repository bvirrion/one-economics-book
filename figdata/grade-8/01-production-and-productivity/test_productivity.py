from make_productivity import brenland_sectors, capital_per_worker, facts, output_per_hour


def test_samples():
    assert len(output_per_hour()) >= 120 and len(capital_per_worker()) >= 150
    assert "VEN" not in set(output_per_hour().iso3)


def test_rank_correlation_strong():
    f = facts().set_index("name").value
    assert f.corr_log > 0.85


def test_brenland():
    b = brenland_sectors()
    assert b.firms.sum() == 500 and (b.opw > 0).all()
