from make_jobs import brenland, real_wages, unemployment


def test_spain_highest():
    u = unemployment()
    assert u.esp.max() > 25 and u.esp.max() == u[["usa", "gbr", "deu", "esp", "jpn"]].max().max()


def test_real_wages_rise():
    r = real_wages().set_index("year")
    assert r.w_usa[1913] == 100 and r.w_usa[2020] > 300 and r.y_usa[2020] > 400


def test_brenland_counts():
    b = brenland()
    assert (b.employed + b.unemployed == b.labour_force).all()


def test_us_2019_patched():
    u = unemployment().set_index("year")
    assert 3 < u.usa[2019] < 4.5


def test_brenland_split():
    b = brenland()
    assert (b.under15 + b.outside + b.labour_force == b["pop"]).all()
