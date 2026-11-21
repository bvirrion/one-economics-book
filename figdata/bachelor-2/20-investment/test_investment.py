from make_investment import grunfeld_summary, house_summary, iy_summary, recession


def test_grunfeld():
    s = grunfeld_summary().iloc[0]
    assert (s.n, s.firms, s["corr"], s.slope) == (220, 11, 0.57, 0.93)
    assert (s.fe_value, s.fe_capital, s.fe_r2) == (0.11, 0.31, 0.95)
    assert (s.pooled_value, s.pooled_capital, s.pooled_r2) == (0.115, 0.228, 0.82)


def test_iy_and_house():
    s = iy_summary().set_index("iso3")
    assert list(s.late) == [20.3, 23.4, 27.7]
    assert (s.loc["JPN", "peak"], s.loc["JPN", "peak_year"]) == (36.5, 1973)
    h = house_summary().iloc[0]
    assert (h.rise_96_06, h.fall_06_12, h.iy_2006, h.iy_2010) == (
        49.4,
        -25.8,
        22.9,
        18.0,
    )


def test_house_deflator_by_hand():
    # the BLS annual average (M13) as a second route to the twelve-month mean
    from econdata import bls_cpi, jst

    c = bls_cpi("CUUR0000SA0")
    m13 = c[c.period == "M13"].set_index("year").value
    hp = jst(isos=["USA"], cols=["hpnom"]).set_index("year").hpnom
    rise = 100 * (hp[2006] / m13[2006]) / (hp[1996] / m13[1996]) - 100
    assert round(rise) == 49


def test_recession():
    s = recession().iloc[0]
    assert (s.inv, s.cons) == (-31.4, -1.9)
