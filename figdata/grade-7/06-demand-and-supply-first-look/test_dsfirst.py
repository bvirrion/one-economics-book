from make_dsfirst import facts, shift, strawberry_months, tables


def test_strawberries_seasonal():
    m = strawberry_months()
    assert len(m) == 12 and m.notna().all().all()
    f = facts().set_index("name").value
    for y in (2022, 2023, 2024):
        assert f[f"y{y}_min_month"] in (5, 6, 7, 8) and f[f"y{y}_max"] > 1.2 * f[f"y{y}_min"]


def test_equilibria():
    t = tables().set_index("price")
    assert t.demanded[3] == t.supplied[3] == 600
    s = shift().set_index("price")
    assert s.demanded_after[4] == t.supplied[4] == 800
