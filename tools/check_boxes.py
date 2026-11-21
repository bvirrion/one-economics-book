#!/usr/bin/env python3
"""Box and chart gates of the economics series, for one year directory.

    python3 tools/check_boxes.py parts/grade-10

Checked in every chapter file of the year (solutions are not checked; a stub
chapter -- one carrying "% STUB" -- is skipped):
  1. every model box has its four fields, once each and in order:
     \\assumes, \\predicts, \\tested, \\breaks; and a non-empty name;
  2. debate, record and measure boxes carry a title: \\begin{debate}[Title];
  3. grades 7-12 and the university years: exactly one openingchart per chapter,
     and it comes before the first \\section; grade 6: no openingchart and at
     least three omchart environments;
  4. every omchart / openingchart has a non-empty source line, and draws its data
     from a table under figdata/ (\\addplot table ... {figdata/...}); no inline
     "coordinates" inside a chart (data are never typed by hand);
  5. every figdata table a chapter reads exists.
Exit 1 on any finding.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GROUP = r"\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}"
MODEL = re.compile(r"\\begin\{model\}" + GROUP + r"(.*?)\\end\{model\}", re.S)
CHART = re.compile(r"\\begin\{(omchart|openingchart)\}" + GROUP + r"\s*" + GROUP + r"(.*?)\\end\{\1\}", re.S)
TABLE = re.compile(r"\{(figdata/[^}]+\.(?:csv|dat))\}")
FIELDS = ["\\assumes", "\\predicts", "\\tested", "\\breaks"]


def strip_comments(src):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in src.splitlines())


def check_file(path, year):
    raw = path.read_text(encoding="utf8")
    if "% STUB" in raw:
        return []
    src = strip_comments(raw)
    out = []

    def at(pos):
        return f"{path}:{src[:pos].count(chr(10)) + 1}"

    for m in MODEL.finditer(src):
        name, body = m.group(1).strip(), m.group(2)
        if not name:
            out.append(f"{at(m.start())}: model box without a name")
        found = [(body.find(f), f) for f in FIELDS]
        counts = [len(re.findall(re.escape(f) + r"(?![A-Za-z])", body)) for f in FIELDS]
        if counts != [1, 1, 1, 1]:
            out.append(f"{at(m.start())}: model box {name!r} needs \\assumes \\predicts \\tested "
                       f"\\breaks once each (counts {counts})")
        elif [p for p, _ in found] != sorted(p for p, _ in found):
            out.append(f"{at(m.start())}: model box {name!r}: fields out of order")
    for env in ("debate", "record", "measure"):
        for m in re.finditer(r"\\begin\{" + env + r"\}(\[[^\]]*\])?", src):
            if not m.group(1) or not m.group(1)[1:-1].strip():
                out.append(f"{at(m.start())}: {env} box without a [Title]")
    charts = list(CHART.finditer(src))
    opening = [c for c in charts if c.group(1) == "openingchart"]
    if year == "grade-6":
        if opening:
            out.append(f"{path}: grade 6 has no opening chart (its chapters are charts)")
        if len(charts) < 3:
            out.append(f"{path}: grade 6 chapter with {len(charts)} chart(s), wants at least 3")
    else:
        if len(opening) != 1:
            out.append(f"{path}: {len(opening)} opening chart(s), wants exactly 1")
        else:
            sec = src.find("\\section")
            if sec != -1 and opening[0].start() > sec:
                out.append(f"{at(opening[0].start())}: the opening chart comes before the first \\section")
    for c in charts:
        kind, cap, source, body = c.groups()
        if not source.strip():
            out.append(f"{at(c.start())}: {kind} without a source line")
        if re.search(r"\\addplot[^;]*?coordinates", body, re.S):
            out.append(f"{at(c.start())}: {kind} with typed coordinates (read a figdata table)")
        tables = TABLE.findall(body)
        if not tables:
            out.append(f"{at(c.start())}: {kind} reads no figdata/ table")
    for t in TABLE.findall(src):
        if not (ROOT / t).exists():
            out.append(f"{path}: missing figdata table {t} (run its make_*.py)")
    return out


def main(argv):
    if len(argv) != 2 or not Path(argv[1]).is_dir():
        print(__doc__)
        return 2
    d = Path(argv[1])
    files = sorted(d.glob("[0-9]*.tex"))
    bad = []
    for f in files:
        bad += check_file(f, d.name)
    for b in bad:
        print(b)
    print(f"check_boxes: {len(files)} files, {len(bad)} finding(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
