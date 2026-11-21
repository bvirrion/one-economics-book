#!/usr/bin/env python3
"""Prose gates of the economics series, for one year directory.

    python3 tools/check_prose.py parts/grade-8

Checked in every chapter and solutions file of the year (comments ignored; the
arguments of \\code, \\texttt, \\key, \\url, \\omcode, \\omoutput masked, since
code may hold straight quotes and any word):
  1. no straight " in prose (write ``...'');
  2. no curriculum, exam, school-system or university name in printed text;
  3. no e-mail address other than an example.org / example.com one, and nothing
     of the author's own (account name);
  4. no code pasted into a chapter: lstlisting, verbatim and \\lstinline are
     forbidden (code comes from a tested file through \\omcode, output through
     \\omoutput, a short token through \\code{...});
  5. no \\cref / \\ref / \\pageref into another book (cross-volume references
     are prose only);
  6. a dated box carries its year: \\begin{dated}{2026};
  7. no school of thought and no history of thought (user rulings, 2026-11-19):
     Marx/Marxist/Marxian, the regulation school, post-Keynesian, degrowth, the
     economy of conventions, "history of economic thought", "school(s) of thought";
  8. no prescriptive title: no "should" or "ought" in a \\chapter, \\section or
     \\subsection title;
  9. no history box (\\begin{history}): the series has none.
Exit 1 on any finding.
"""
import getpass
import re
import sys
from pathlib import Path

BOOK_OF = {}
for i in range(1, 10):
    BOOK_OF[f"g{i}"] = 1
for i in range(10, 13):
    BOOK_OF[f"g{i}"] = 2
BOOK_OF.update({"b1": 3, "b2": 4, "b3": 5})

CURRIC = re.compile(
    r"\b(SES|ECG|ESH|B/L|sciences [ée]conomiques et sociales|licence d'[ée]conomie|AP Macro\w*|AP Micro\w*|A-level|IB\b(?= (economics|diploma|course))|NSI|SNT|MP2I|MPI|MPSI|PCSI|BCPST|Parcoursup|baccalaur\w*|brevet|coll[eè]ge(?= (class|year|student|pupil|level))|collège|lyc[eé]e|"
    r"terminale|premi[eè]re|seconde\b(?= (class|year))|licence (?:informatique|de)|L[123]\b(?= (course|year|student))|"
    r"(?:French|France'?s?|Eduscol|[ÉE]ducation nationale)\s+(?:school|education|programme|program|curricul\w*|"
    r"syllabus|exam\w*|national|teaching|system|universit\w*)|classes? pr[ée]paratoires?|"
    r"preparatory class(?:es)?|grandes? [ée]coles?|concours)\b", re.I)
THOUGHT = re.compile(
    r"\b(Marx\w*|regulation school|[ée]cole de la r[ée]gulation|post-?Keynesian\w*|degrowth|d[ée]croissance|"
    r"economy of conventions|[ée]conomie des conventions|history of (?:economic )?thought|"
    r"schools? of (?:economic )?thought)\b", re.I)
TITLE = re.compile(r"\\(?:chapter|section|subsection)\*?\{([^}]*)\}")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
GROUP = r"(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*"
MASK = re.compile(r"\\(?:code|texttt|url|path|omcode|omcodes|href|label|ref|cref|Cref|pageref|"
                  r"index|input|includegraphics|omimg)\s*(?:\[[^\]]*\])?\{" + GROUP + r"\}"
                  r"|\\omoutput(?:\[[^\]]*\])?\{[^{}]*\}")


def strip_comments(src):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in src.splitlines())


def check_file(path, book):
    raw = path.read_text(encoding="utf8")
    src = strip_comments(raw)
    out = []
    lines = src.splitlines()
    masked = [MASK.sub(lambda m: " " * len(m.group(0)), ln) for ln in lines]
    user = getpass.getuser()
    for n, (ln, ml) in enumerate(zip(lines, masked, strict=True), start=1):
        if '"' in re.sub(r'\\"[A-Za-z{]', "", ml):
            out.append(f"{path}:{n}: straight \" in prose (write ``...'')")
        m = CURRIC.search(ml)
        if m:
            out.append(f"{path}:{n}: curriculum or school-system name {m.group(0)!r}")
        for e in EMAIL.findall(ln):
            if not re.search(r"@example\.(org|com|net)$", e):
                out.append(f"{path}:{n}: e-mail address {e!r} (only example.org/com/net addresses)")
        if user and re.search(r"\b" + re.escape(user) + r"\b", ln):
            out.append(f"{path}:{n}: the author's account name")
        if re.search(r"\\begin\{(lstlisting|verbatim|Verbatim)\}|\\lstinline|\\verb\b", ln):
            out.append(f"{path}:{n}: pasted code (use \\omcode from a tested file, or \\code{{...}})")
        m = THOUGHT.search(ml)
        if m:
            out.append(f"{path}:{n}: school or history of thought {m.group(0)!r} (user ruling: not in the series)")
        for t in TITLE.findall(ln):
            if re.search(r"\b(should|ought)\b", t, re.I):
                out.append(f"{path}:{n}: prescriptive title {t!r} (titles describe, never prescribe)")
        if "\\begin{history}" in ln:
            out.append(f"{path}:{n}: history box (the series has none)")
        if re.search(r"\\begin\{dated\}(?!\{[^}]+\})", ln):
            out.append(f"{path}:{n}: dated box without its year: \\begin{{dated}}{{<year>}}")
    for m in re.finditer(r"\\(?:cref|Cref|ref|pageref|nameref|hyperref\[)\{?([^}\]]*)", src):
        for key in m.group(1).split(","):
            parts = key.strip().split(":")
            if len(parts) >= 3 and parts[1] in BOOK_OF and BOOK_OF[parts[1]] != book:
                n = src[:m.start()].count("\n") + 1
                out.append(f"{path}:{n}: reference into another book ({key.strip()}): write it in prose")
    return out


def book_of_year(year):
    kind, n = year.split("-")
    n = int(n)
    if kind == "grade":
        return 1 if n <= 9 else 2
    return n + 2


def main(argv):
    if len(argv) != 2 or not Path(argv[1]).is_dir():
        print(__doc__)
        return 2
    d = Path(argv[1])
    book = book_of_year(d.name)
    files = sorted(d.glob("[0-9]*.tex")) + sorted((d / "solutions").glob("[0-9]*.tex"))
    bad = []
    for f in files:
        bad += check_file(f, book)
    for b in bad:
        print(b)
    print(f"check_prose: {len(files)} files, {len(bad)} finding(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
