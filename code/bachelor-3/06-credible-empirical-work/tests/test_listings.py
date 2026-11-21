def test_exaggeration_falls_with_power(run):
    out, _ = run("significance_filter")
    rows = [line.split() for line in out.splitlines()[1:7]]
    ratios = [float(r[4]) for r in rows]
    assert ratios == sorted(ratios, reverse=True) and ratios[0] > 4
    for r in rows:
        assert abs(float(r[4]) - float(r[5])) < 0.06     # simulation = formula


def test_forking_paths_inflate_false_positives(run):
    out, _ = run("forking_paths")
    lines = out.splitlines()
    first = float(lines[3].split()[-1])
    anyp = float(lines[4].split()[-1])
    assert first < 0.08 and 0.15 < anyp < 0.56


def test_fat_significant_only_with_filter(run):
    out, _ = run("funnel")
    lines = out.splitlines()
    fat_all = float(lines[1].split("FAT (slope on s.e.)")[1].split()[0])
    fat_se_all = float(lines[1].split("(s.e. ")[1].split(")")[0])
    fat_pub = float(lines[3].split("FAT (slope on s.e.)")[1].split()[0])
    fat_se_pub = float(lines[3].split("(s.e. ")[1].split(")")[0])
    assert abs(fat_all / fat_se_all) < 1.96 and fat_pub / fat_se_pub > 1.96


def test_reading_table(run):
    out, _ = run("reading_table")
    assert "1.794***" in out and "445" in out
