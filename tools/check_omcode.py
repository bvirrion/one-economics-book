#!/usr/bin/env python3
"""Every \\omcode{path}{first}{last}{...} must name an existing file whose
line count covers first..last, and a printed listing is at most 40 lines.
With an argument, only listings whose code path or chapter file contains it."""
import glob
import re
import sys

sel = sys.argv[1] if len(sys.argv) > 1 else ""
bad = 0
n = 0
for tex in sorted(glob.glob("parts/**/*.tex", recursive=True)):
    src = open(tex, encoding="utf8").read()
    for m in re.finditer(r"\\omcode\{([^}]*)\}\{(\d+)\}\{(\d+)\}", src):
        path, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        if sel and sel not in path and sel not in tex:
            continue
        n += 1
        try:
            lines = sum(1 for _ in open(path, encoding="utf8"))
        except OSError:
            print(f"MISSING  {tex}: {path}")
            bad += 1
            continue
        if not (1 <= a <= b <= lines):
            print(f"RANGE    {tex}: {path} {a}-{b} (file has {lines} lines)")
            bad += 1
        if b - a + 1 > 40:
            print(f"TOO LONG {tex}: {path} {a}-{b} ({b - a + 1} lines > 40)")
            bad += 1
for tex in sorted(glob.glob("parts/**/*.tex", recursive=True)):
    for m in re.finditer(r"\\omcodes\{([^}]*)\}\{([^}]*)\}", open(tex, encoding="utf8").read()):
        path = m.group(1)
        if sel and sel not in path and sel not in tex:
            continue
        n += 1
        try:
            lines = sum(1 for _ in open(path, encoding="utf8"))
        except OSError:
            print(f"MISSING  {tex}: {path}")
            bad += 1
            continue
        total = 0
        for part in m.group(2).split(","):
            a, b = (int(x) for x in part.split("-"))
            total += b - a + 1
            if not (1 <= a <= b <= lines):
                print(f"RANGE    {tex}: {path} {a}-{b} (file has {lines} lines)")
                bad += 1
        if total > 40:
            print(f"TOO LONG {tex}: {path} {m.group(2)} ({total} lines > 40)")
            bad += 1
print(f"{n} listings checked, {bad} problems")
sys.exit(1 if bad else 0)
