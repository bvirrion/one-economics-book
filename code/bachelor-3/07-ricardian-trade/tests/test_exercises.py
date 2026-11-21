def test_ex08_runs_and_matches_chart(run_exercise):
    out, _ = run_exercise("ex08_crops")
    first = out.splitlines()[0]
    assert "73 countries" in first and "correlation -0.30" in first
