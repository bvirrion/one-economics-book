#!/usr/bin/env python3
"""The output gate: no printed output is typed by hand.

Every \\omoutput{path}{...} in parts/ must name a file under outputs/ whose listing still exists (same stem
under listings/), and rerunning that listing must reproduce the file byte for byte. Every output file must be
printed somewhere, or listed in listings/NOPRINT.txt (an output kept only for a test or a solution).

    tools/check_outputs.py                     every chapter, rerun
    tools/check_outputs.py grade-8/04          only the outputs under code/grade-8/04* (a prefix)
    tools/check_outputs.py --no-run            only check that the files exist

A step listed in steps/MEASURED.txt prints timings: its rerun must match with the digits masked, and the caption of
its \\omoutput must say ``laptop'', so that a reader knows what machine the timings describe.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from capture_output import find_listing, mask, measured_stems, run_listing  # noqa: E402


def caption_after(src: str, pos: int) -> str:
    """The balanced {...} group that starts at src[pos]."""
    depth = 0
    for i in range(pos, len(src)):
        if src[i] == "{":
            depth += 1
        elif src[i] == "}":
            depth -= 1
            if depth == 0:
                return src[pos + 1:i]
    return ""


def main() -> int:
    # Real argument parsing: before it, `--help` was ignored and started a rerun of every chapter.
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("selector", nargs="?", default="",
                    help="a prefix under code/, such as grade-8 or bachelor-1/04")
    ap.add_argument("--no-run", action="store_true", help="check files and captions only, rerun nothing")
    opts = ap.parse_args()
    sel = "code/" + opts.selector.removeprefix("code/") if opts.selector else ""
    run = not opts.no_run
    bad = n = 0
    seen = set()
    for tex in sorted((ROOT / "parts").rglob("*.tex")):
        src = tex.read_text(encoding="utf8")
        for m in re.finditer(r"\\omoutput(?:\[[^\]]*\])?\{([^}]*)\}", src):
            path = ROOT / m.group(1)
            if sel and not m.group(1).startswith(sel):
                continue
            n += 1
            chapter = path.parent.parent
            measured = path.stem in measured_stems(chapter)
            if measured and "laptop" not in caption_after(src, m.end()):
                print(f"NO LAPTOP {tex.relative_to(ROOT)}: {m.group(1)} is measured, and its caption must say on what")
                bad += 1
            if path in seen:
                continue
            seen.add(path)
            step = find_listing(chapter, path.stem)
            if path.parent.name != "outputs" or not path.exists() or step is None:
                print(f"MISSING  {tex.relative_to(ROOT)}: {m.group(1)} (needs the output file and its listing)")
                bad += 1
                continue
            if run:
                want = run_listing(chapter, step)
                have = path.read_text(encoding="utf8")
                if measured:
                    want, have = mask(want), mask(have)
                if want != have:
                    bad += 1
                    print(f"DIFFERS  {m.group(1)}")
                    for a, b in zip(have.splitlines(), want.splitlines(), strict=False):
                        if a != b:
                            print(f"   printed: {a}\n   rerun:   {b}")
                            break
                    else:
                        print(f"   {len(have.splitlines())} printed lines against {len(want.splitlines())} on rerun")
    # an output file that nothing prints is an output typed for nobody: print it or list it in NOPRINT.txt
    for out in sorted((ROOT / "code").glob("*/*/outputs/*.txt")):
        rel = out.relative_to(ROOT).as_posix()
        if sel and not rel.startswith(sel):
            continue
        if out in seen:
            continue
        noprint = out.parent.parent / "listings" / "NOPRINT.txt"
        names = set(noprint.read_text(encoding="utf8").split()) if noprint.exists() else set()
        if out.stem not in names and out.name not in names:
            print(f"UNPRINTED {rel} (print it with \\omoutput, or list its stem in listings/NOPRINT.txt)")
            bad += 1
    print(f"{n} outputs checked ({len(seen)} files{', rerun' if run else ''}), {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
