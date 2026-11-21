import numpy as np
from make_first_stage import built_share, tables


def test_gravity_fit_has_the_usual_signs():
    _, fit = built_share()
    assert -1.6 < fit.params["ldist"] < -1.2          # distance elasticity near -1.4
    assert fit.params["contig"] > 0.5
    assert fit.params["lpd"] > 0.6


def test_first_stage_is_strong_with_population():
    pts, line, stats = tables()
    s = stats.iloc[0]
    assert s.n == len(pts) == 157
    assert 10 < s.F < 25 and s.F_pop > 30
    assert 0.15 < s.slope < 0.35


def test_line_passes_through_the_cloud():
    pts, line, _ = tables()
    lt = np.log(pts.trade).mean()
    lb = np.log(pts.built).mean()
    b = (np.log(line.trade[1]) - np.log(line.trade[0])) / (np.log(line.built[1]) - np.log(line.built[0]))
    a = np.log(line.trade[0]) - b * np.log(line.built[0])
    assert abs(a + b * lb - lt) < 1e-9


def test_congo_brazzaville_is_the_geographic_outlier():
    pts, _, _ = tables()
    assert pts.sort_values("built").iso3.iloc[-1] == "COG"
