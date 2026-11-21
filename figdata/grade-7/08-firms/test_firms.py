from make_firms import bakery, brenland_sectors, survival, survival_sector


def test_survival_falls():
    s = survival()
    for c in ["eu", "nl", "it", "de", "fr"]:
        assert s[c].is_monotonic_decreasing and s[c].iloc[0] == 100
    assert len(survival_sector()) == 11


def test_bakery_break_even():
    b = bakery().set_index("q")
    assert b.profit[2500] == 0 and b.profit[0] == -3000


def test_brenland_services_most_losses():
    b = brenland_sectors().set_index("sector")
    assert b.loss_share.idxmax() == "services" and b.firms.sum() == 500
