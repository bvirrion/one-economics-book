from make_defaults import table


def test_numbers_from_the_paper():
    t = table()
    assert t.window.tolist() == [37, 1] and t.new.tolist() == [86, 61]
