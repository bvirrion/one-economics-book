def test_did_by_means_equals_ols_interaction(run):
    out, _ = run("did_nsw")
    did = [line for line in out.splitlines() if line.startswith("DiD")][0].split()[-1]
    ols = [line for line in out.splitlines() if line.startswith("OLS")][0].split()[2]
    assert did == ols == "3621"


def test_benchmark_is_the_published_experimental_estimate(run):
    out, _ = run("lalonde_benchmark")
    assert out.splitlines()[0].split()[1] == "1794"
    rows = {line[:28].strip(): float(line[28:].split()[0]) for line in out.splitlines()
            if line.startswith("  ")}
    assert rows["difference in means"] < -8000      # the last PSID row overwrites CPS
    assert rows["DiD"] > 0


def test_twfe_misses_and_clean_comparisons_recover(run):
    _, r = run("bacon")
    true, twfe = float(r["true average effect on the treated"]), float(
        r["two-way fixed effects"])
    clean = float(r["clean comparisons, averaged"])
    assert twfe < 0.7 * true and abs(clean - true) < 0.15


def test_synthetic_control_finds_the_effect_and_ranks_first(run):
    out, r = run("synth_demo")
    assert abs(float(r["mean gap after"]) + 2) < 0.5
    assert "rank 1 of 21" in out
