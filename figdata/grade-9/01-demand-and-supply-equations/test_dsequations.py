from make_dsequations import equilibrium, phones


def test_equilibria():
    assert equilibrium(120, 4, 20, 6) == (10, 80)
    p, q = equilibrium(1000, 50, 175, 75)
    assert abs(p - 6.6) < 1e-9 and abs(q - 670) < 1e-9


def test_phones_direction():
    ph = phones().set_index("year")
    assert ph.price[2010] < 15 and ph.subs[2010] > ph.subs[2000]
