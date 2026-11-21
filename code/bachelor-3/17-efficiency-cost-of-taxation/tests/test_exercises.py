from econdata import wdi


def test_ex08_changes(run_exercise):
    out, _ = run_exercise("ex08_composition")
    lines = out.splitlines()
    table = {ln.split()[0]: ln.split()[1:] for ln in lines[3:8]}
    # independent route: read two values straight from WDI and subtract
    kor = wdi("GC.REV.SOCL.ZS", isos=["KOR"]).set_index("year").value
    assert abs(float(table["KOR"][2]) - (kor[2024] - kor[1990])) < 0.06
    fra = wdi("GC.TAX.YPKG.RV.ZS", isos=["FRA"]).set_index("year").value
    assert abs(float(table["FRA"][0]) - (fra[2024] - fra[1990])) < 0.06
    assert table["DEU"][2] == "NaN"
    best = max((float(v), iso, k) for iso, vals in table.items()
               for k, v in zip(("income", "goods", "social", "trade"), vals) if v != "NaN")
    assert lines[-1] == f"largest gain: {best[2]} in {best[1]}, {best[0]:+.1f} points"
