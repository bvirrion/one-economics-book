from make_income import tables


def test_long_run():
    a, _, _ = tables()
    g = a.set_index("year")
    assert g.gbr[1300] == 1159 and g.gbr[1700] == 2412 and g.gbr[2000] == 31946
    assert g.gbr.loc[1300:1700].max() < 3000          # under 3,000 dollars for centuries
    assert g.nld.first_valid_index() == 1348
    assert g.world.first_valid_index() == 1820 and g.world[1820] == 1128 and g.world[2022] == 16677


def test_regions():
    _, b, _ = tables()
    r = b.set_index("year")
    assert r.loc[1820].idxmax() == "western_offshoots" and r.loc[2022].idxmax() == "western_offshoots"
    assert r.loc[2022].idxmin() == "ssa"
    assert r.east_asia[2022] / r.east_asia[1950] > 15


def test_six():
    _, _, c = tables()
    s = c.set_index("year")
    assert s.index.min() == 1950 and s.index.max() == 2022 and not s.isna().any().any()
    assert (s.kor > s.arg).idxmax() == 1988
    assert s.ven.idxmax() == 2012 and s.ven[2022] == 5267
    assert s.bwa[1950] == 489 and s.bwa[2022] == 16352
