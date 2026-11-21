from make_ramsey import K_STAR, initial_share, ky_summary, paths, saving_summary


def test_saving_and_ky():
    s = saving_summary().set_index("iso3")
    assert (s.loc["KOR", "first"], s.loc["KOR", "peak"], s.loc["KOR", "peak_year"]) == (
        1.0,
        41.7,
        1988,
    )
    assert (s.loc["CHN", "peak"], s.loc["CHN", "peak_year"]) == (50.6, 2010)
    k = ky_summary().iloc[0]
    assert (k.y1980, k["min"], k.min_year, k.y2023) == (3.09, 2.98, 1988, 5.11)


def test_initial_stock_by_hand():
    # perpetual inventory by hand: K_t = (1 - delta_t) K_{t-1} + I_t, so the 1953 stock
    # alone, depreciated year by year, is what remains of the starting guess
    from econdata import pwt

    p = pwt(isos=["KOR"]).set_index("year")
    rest = p.rnna[1953]
    for y in range(1954, 1981):
        rest *= 1 - p.delta[y]
        if y in (1960, 1970, 1980):
            got = initial_share().set_index("year").share[y]
            assert abs(rest / p.rnna[y] - got) < 1e-3
    assert rest / p.rnna[1980] < 0.11


def test_model_paths():
    assert round(K_STAR, 3) == 8.505
    p = paths().set_index("t")
    assert (p.s2[0], p.s2[10], p.s6[0], p.s6[10]) == (0.3425, 0.294, 0.2092, 0.2214)
    assert p.k2[60] > 0.97 and p.k6[60] < p.k2[60]
