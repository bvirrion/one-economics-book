import io

import country


def test_files_match_seed():
    for name, df in country.generate().items():
        buf = io.StringIO()
        df.to_csv(buf, index=False, lineterminator="\n")
        assert (country.OUT / f"{name}.csv").read_text() == buf.getvalue(), name


def test_identities():
    a = country.load("accounts")
    assert (a.gdp == a.C + a.I + a.G + a.X - a.M).all()
    assert (a.deficit == a.spending - a.revenue).all()
    assert (a.debt.diff().iloc[1:] == a.deficit.iloc[1:]).all()
    assert a.loc[a.year == 2015, "deflator"].iloc[0] == 100.0
    assert a.loc[a.year == 2015, "cpi"].iloc[0] == 100.0
    assert (a.employed < a.labour_force).all() and a.unemp_rate.between(3, 12).all()
    assert (a.M > 0).all() and (a.C > 0.5 * a.gdp).all()


def test_households():
    h = country.load("households")
    assert len(h) == 2000
    assert (h.disposable == h.gross_income - h.tax + h.transfers).all()
    assert (h.food <= h.consumption).all() and (h.food > 0).all()
    poor = h[h.disposable < h.disposable.quantile(0.2)]
    rich = h[h.disposable > h.disposable.quantile(0.8)]
    assert (poor.food / poor.consumption).mean() > (rich.food / rich.consumption).mean()


def test_firms_and_ricardo():
    f = country.load("firms")
    assert (f.profit == f.output - f.wage_bill - f.other_costs).all()
    r = country.load("ricardo").set_index(["country", "good"]).hours_per_unit
    # Brenland: absolute advantage in both goods, comparative advantage in grain
    assert r["Brenland", "cloth"] < r["Kestria", "cloth"] and r["Brenland", "grain"] < r["Kestria", "grain"]
    assert r["Brenland", "grain"] / r["Brenland", "cloth"] < r["Kestria", "grain"] / r["Kestria", "cloth"]


def test_tax_schedule():
    assert country._tax(12_000) == 0
    assert country._tax(40_000) == 0.20 * 28_000
