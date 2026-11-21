from make_comparative import exports_size, facts, ricardo


def test_small_countries_export_more():
    f = facts().set_index("name").value
    assert f.small_median > 2 * f.large_median and len(exports_size()) > 150


def test_ricardo_pattern():
    r = ricardo().set_index("good")
    assert (r.brenland < r.kestria).all()            # absolute advantage in both goods
    f = facts().set_index("name").value
    assert f.kestria_cloth_in_grain < f.brenland_cloth_in_grain   # Kestria: comparative advantage in cloth
