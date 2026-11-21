from make_work import facts, hours, literacy, sectors


def test_literacy():
    d = literacy().set_index("year")
    assert d.wld[1975] == 65.4 and d.wld[2024] == 87.7
    assert d.loc[2024].idxmin() == "ssf"


def test_hours():
    d = hours().set_index("year")
    assert d.deu[1950] == 2427 and d.deu[2023] == 1335
    assert d.loc[2023].idxmax() == "kor"
    assert (d.loc[2023] < d.loc[1960]).all()


def test_sectors():
    s = sectors().set_index("year")
    assert s.index.min() == 1991 and s.agriculture[1991] == 59.6
    assert ((s.agriculture + s.industry + s.services) - 100).abs().max() < 0.3
    assert s.agriculture.iloc[-1] < 25


def test_facts():
    f = facts().set_index("name").value
    assert f.women_lfp_1990 == 51.2 and f.women_lfp_2025 == 48.9 and f.china_services_pass_year == 2011
