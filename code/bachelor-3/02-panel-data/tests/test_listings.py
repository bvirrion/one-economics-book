def test_co2_slopes_within_equals_dummies(run):
    out, r = run("pooled_vs_within")
    v = {line[:18].strip(): float(line[18:]) for line in out.splitlines()[1:6]}
    assert v["within"] == v["country dummies"]
    assert v["between"] > 2 * v["within"]
    assert v["country and year"] > v["within"]
    assert float(r["share of the variance of log income that is within:"]) < 0.05


def test_random_effects_biased_only_with_correlation(run):
    out, _ = run("random_effects")
    rows = [list(map(float, line.split())) for line in out.splitlines()[1:]]
    (c0, fe0, re0, _), (c1, fe1, re1, _) = rows
    assert c0 == 0 and abs(fe0 - 1) < 0.03 and abs(re0 - 1) < 0.03
    assert c1 > 0.4 and abs(fe1 - 1) < 0.03 and re1 > 1.1


def test_clustering_restores_size(run):
    out, _ = run("cluster_sim")
    rate = {line.split()[0]: float(line.split()[-4]) for line in out.splitlines()}
    assert rate["se_iid"] > 0.3 and rate["se_hc1"] > 0.3
    assert abs(rate["se_cluster"] - 0.05) < 0.03
