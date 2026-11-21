#!/usr/bin/env python3
"""Run listings and write what they print: the ONLY writer of code/<year>/<chapter>/outputs/*.txt.

    tools/capture_output.py code/grade-8/04-searching-and-sorting               # every runnable listing
    tools/capture_output.py code/grade-8/04-searching-and-sorting binary linear # listings whose stem starts so
    tools/capture_output.py code/bachelor-2/12-caches --measured                # only its measured listings

A chapter keeps the files it prints in listings/. Every file there with a runnable suffix is run, unless its
name (or stem) is in listings/NORUN.txt (a module that others import, a header, a file shown but never run). The output
of listings/<stem>.<ext> goes to outputs/<stem>.txt, so stems are unique within a chapter. The first line of an
output file is the command a reader would type, then stdout and stderr merged, as the reader would see them.

How each suffix runs (cwd = listings/, environment pinned below):
  .py    python <file>; input() echoes what it reads, so a session with typed answers reads as on a terminal
         (the answers come from listings/<stem>.stdin)
  .c     gcc -std=c17 -O2 -Wall -Wextra -o <stem> <file> -lm && ./<stem>
  .cpp   g++ -std=c++20 -O2 -Wall -Wextra -o <stem> <file> && ./<stem>
  .rs    rustc --edition 2021 -O -o <stem> <file> && ./<stem>
  .sql   python sqlrun.py <file>            (code/shared/sqlrun: Python's sqlite3, the book's runner)
  .toy   python -m toymachine run <file>    (code/shared/toymachine)
  .S     python -m rv run <file>            (code/shared/rv)
  .sh    bash <file>; with a first-lines comment `# capture: session` every command line is printed
         after "$ " before it runs, in a fresh empty directory, as a terminal session
A compiler's error is the listing's output, so a staged compile failure can be printed.

Directives, in a comment in the first five lines of a listing (`# capture: ...` or `// capture: ...`):
  cflags=<flags>        replace the C/C++ optimisation and warning flags (e.g. cflags=-O0 -g -fsanitize=address)
  args=<words>          command-line arguments for the program
  timeout=<seconds>     default 120
  session               (.sh only) the terminal-session mode above
  copy=a.c,b.h          (.sh session only) copy these files of listings/ (or, if not there, of data/country/)
                        into the session directory first, so the session uses them by their bare names
  with=a.c,b.c          (.c/.cpp) compile these files of listings/ together with the listing (list the
                        library files in NORUN.txt); the shown command names them
  A session line ending in `# hidden` runs but is not shown (setup; silence its output yourself).
  rv=asm|dis            (.S only) python -m rv asm|dis instead of run
  scratch               run in a temporary copy of listings/ (for a listing that writes files)
  fixtimes              (.sh session only) files get a fixed date after each command, for `ls -l`
  exit                  print "[exit status N]" after the output when it is not 0
listings/<stem>.stdin, if present, is the program's standard input.

listings/MEASURED.txt lists the listings that print timings, one stem per line: check_outputs.py checks their
structure, not their digits (mask()), and they are recaptured on a quiet machine with --measured.

Determinism: TZ=UTC, LC_ALL=C.UTF-8, PYTHONHASHSEED=0, fixed git author/committer names and dates, HOME and
the session directory replaced in the output by ~ and ~/session, compiled programs run without address
randomisation (setarch -R), a sanitizer's process number printed as 1000. Privacy: the account name prints
as `ada` and the machine name as `laptop`. Every run is capped at 4 GB with no swap.
"""
import getpass
import os
import re
import socket
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "code" / "shared"
PY = ROOT / ".venv" / "bin" / "python"
PINNED = {
    "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "PYTHONHASHSEED": "0", "PYTHONUNBUFFERED": "1",
    "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC", "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8",
    "GIT_AUTHOR_NAME": "Ada Lovelace", "GIT_AUTHOR_EMAIL": "ada@example.org",
    "GIT_COMMITTER_NAME": "Ada Lovelace", "GIT_COMMITTER_EMAIL": "ada@example.org",
    "GIT_AUTHOR_DATE": "2026-01-05T09:00:00+00:00", "GIT_COMMITTER_DATE": "2026-01-05T09:00:00+00:00",
    "GIT_CONFIG_NOSYSTEM": "1", "GIT_PAGER": "cat", "PAGER": "cat", "TERM": "dumb", "NO_COLOR": "1",
    "CARGO_NET_OFFLINE": "true", "ASAN_OPTIONS": "detect_leaks=1:abort_on_error=0",
}
CAP = ["systemd-run", "--user", "--scope", "-q", "-p", "MemoryMax=4G", "-p", "MemorySwapMax=0"]
RUNNABLE = (".py", ".c", ".cpp", ".rs", ".sql", ".toy", ".S", ".sh")
ECHO_INPUT = ROOT / "tools" / "echo_input.py"


def listings_dir(chapter: Path) -> Path:
    return chapter / "listings"


def _norun(chapter: Path) -> set[str]:
    f = listings_dir(chapter) / "NORUN.txt"
    if not f.exists():
        return set()
    return {w for line in f.read_text(encoding="utf8").splitlines() for w in line.split("#")[0].split()}


def find_listings(chapter: Path) -> list[Path]:
    """Every runnable listing of a chapter, in name order."""
    d = listings_dir(chapter)
    if not d.is_dir():
        return []
    skip = _norun(chapter)
    return sorted(p for p in d.iterdir()
                  if p.is_file() and p.suffix in RUNNABLE and p.name not in skip and p.stem not in skip
                  and not p.name.startswith("_"))


def find_listing(chapter: Path, stem: str) -> Path | None:
    return next((p for p in find_listings(chapter) if p.stem == stem), None)


def _measured(chapter: Path) -> list[list[str]]:
    f = listings_dir(chapter) / "MEASURED.txt"
    if not f.exists():
        return []
    lines = (line.split("#")[0].split() for line in f.read_text(encoding="utf8").splitlines())
    return [words for words in lines if words]


def measured_stems(chapter: Path) -> set[str]:
    return {Path(words[0]).stem for words in _measured(chapter)}


def mask(text: str) -> str:
    """A measured output without its digits or its column widths: what must stay the same from one run to another."""
    text = re.sub(r"[-+]?\d[\d,]*(?:\.\d+)?(?:[eE][-+]?\d+)?", "#", text)
    return re.sub(r"[ \t]+", " ", text)


def directives(path: Path) -> dict:
    out = {}
    try:
        head = path.read_text(encoding="utf8", errors="replace").splitlines()[:5]
    except OSError:
        return out
    for line in head:
        m = re.search(r"(?:#|//|--|;)\s*capture:\s*(.*)$", line)
        if not m:
            continue
        rest = m.group(1).strip()
        for key in ("cflags", "args", "timeout", "rv", "copy", "with"):
            mm = re.search(r"(?:^|\s)" + key + r"=(.*?)(?=\s+\w+=|\s+session\b|\s+exit\b|\s+fixtimes\b|$)", rest)
            if mm:
                out[key] = mm.group(1).strip()
        for flag in ("session", "exit", "fixtimes", "scratch"):
            if re.search(r"(?:^|\s)" + flag + r"(?:\s|$)", rest):
                out[flag] = True
    return out


def _run(cmd, cwd: Path, env: dict, timeout: int, stdin_path: Path | None = None) -> subprocess.CompletedProcess:
    capped = CAP + cmd if shutil.which("systemd-run") and "XDG_RUNTIME_DIR" in os.environ else cmd
    stdin = open(stdin_path, "rb") if stdin_path else subprocess.DEVNULL
    try:
        return subprocess.run(capped, cwd=cwd, env=env, stdin=stdin, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, timeout=timeout)
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or b"") + f"\n[killed after {timeout} s]\n".encode()
        return subprocess.CompletedProcess(cmd, -9, out, None)
    finally:
        if stdin_path:
            stdin.close()


def _decode(b: bytes) -> str:
    return b.decode("utf8", errors="replace")


def _session_script(src: str, fixtimes: bool = False) -> str:
    """Each top-level command line becomes: print it after "$ ", then run it. Comments and blank lines are
    dropped; a line ending in a backslash continues the command. With fixtimes, every file under the
    session directory gets the fixed date 2026-01-05 09:00 after each command (so `ls -l` is the same
    every run; never use it in a session that teaches make, which reads those dates)."""
    out, buf = ["set +e", 'S0="$PWD"'], []
    touch = ('find "$S0" -exec touch -h -d "2026-01-05 09:00:00" {} + 2>/dev/null' if fixtimes else None)
    for line in src.splitlines():
        if not buf and (not line.strip() or line.lstrip().startswith("#")):
            continue
        buf.append(line)
        if line.endswith("\\"):
            continue
        cmd = "\n".join(buf)
        buf = []
        hidden = re.search(r"\s#\s*hidden\s*$", cmd)
        if hidden:  # a setup line: it runs, but is not shown (its own output still is: send it to /dev/null)
            out.append(cmd[:hidden.start()])
            continue
        shown = cmd.replace("'", "'\\''")
        out.append(f"printf '%s\\n' '$ {shown}'")
        out.append(cmd)
        if touch:
            out.append(touch)
    return "\n".join(out) + "\n"


def run_listing(chapter: Path, src: Path) -> str:
    """Return the file contents a capture of this listing should have."""
    d = directives(src)
    timeout = int(d.get("timeout", 120))
    cwd = listings_dir(chapter)
    rel = src.name
    stdin = cwd / (src.stem + ".stdin")
    stdin = stdin if stdin.exists() else None
    args = d.get("args", "").split()
    with tempfile.TemporaryDirectory(prefix="ocs-") as tmp:
        tmp = Path(tmp)
        home = tmp / "home"
        home.mkdir()
        lib = cwd.parent.parent / "lib"  # code/<year>/lib: modules shared by the year's chapters, never printed
        if d.get("scratch"):
            # the listing writes files: run it in a copy of listings/, so nothing is left behind
            work = tmp / "work"
            shutil.copytree(cwd, work)
            cwd = work
        real_home = os.path.expanduser("~")
        # A fixed environment, not the caller's: a sanitizer report prints stack addresses that move with
        # the size of the environment, so an agent's shell and test_code.sh would otherwise disagree.
        env = {**PINNED, "HOME": str(home), "USER": "ada", "LOGNAME": "ada", "SHELL": "/bin/bash",
               "PATH": os.pathsep.join([os.path.join(real_home, ".cargo", "bin"), "/usr/local/bin", "/usr/bin",
                                        "/bin"]),
               "RUSTUP_HOME": os.path.join(real_home, ".rustup"), "CARGO_HOME": os.path.join(real_home, ".cargo")}
        for key in ("XDG_RUNTIME_DIR", "DBUS_SESSION_BUS_ADDRESS"):  # systemd-run --user needs them
            if key in os.environ:
                env[key] = os.environ[key]
        env["PYTHONPATH"] = os.pathsep.join([str(SHARED), str(lib), str(ROOT / "figdata" / "lib"), str(cwd)])
        env["PATH"] = f"{ROOT / '.venv/bin'}{os.pathsep}{env['PATH']}"
        text = ""
        if src.suffix == ".py":
            command = " ".join(["python", rel] + args)
            r = _run([str(PY), str(ECHO_INPUT), rel] + args, cwd, env, timeout, stdin)
            text = _decode(r.stdout)
        elif src.suffix in (".c", ".cpp", ".rs"):
            exe = tmp / src.stem
            if src.suffix == ".c":
                flags = d.get("cflags", "-O2 -Wall -Wextra").split()
                build = ["gcc", "-std=c17"] + flags + ["-o", str(exe), rel, "-lm"]
                shown = " ".join(["gcc", "-std=c17"] + flags + ["-o", src.stem, rel, "-lm"])
            elif src.suffix == ".cpp":
                flags = d.get("cflags", "-O2 -Wall -Wextra").split()
                build = ["g++", "-std=c++20"] + flags + ["-o", str(exe), rel]
                shown = " ".join(["g++", "-std=c++20"] + flags + ["-o", src.stem, rel])
            else:
                flags = d.get("cflags", "-O").split()
                build = ["rustc", "--edition", "2021"] + flags + ["-o", str(exe), rel]
                shown = " ".join(["rustc", "--edition", "2021"] + flags + ["-o", src.stem, rel])
            extra = list(filter(None, d.get("with", "").replace(",", " ").split()))
            if extra and src.suffix in (".c", ".cpp"):
                lm = build[-1:] if build[-1] == "-lm" else []
                build = build[:len(build) - len(lm)] + extra + lm
                shown = " ".join(shown.split(" -lm")[0].split() + extra + (["-lm"] if lm else []))
            command = f"{shown} && ./{' '.join([src.stem] + args)}"
            built = _run(build, cwd, {**env, "LC_ALL": "C"}, timeout)  # plain ASCII quotes in compiler errors
            text = _decode(built.stdout)
            r = built
            if built.returncode == 0:
                # no address randomisation: a sanitizer report or a printed pointer is the same every run
                norand = ["setarch", os.uname().machine, "-R"] if shutil.which("setarch") else []
                r = _run(norand + [str(exe)] + args, cwd, env, timeout, stdin)
                text += _decode(r.stdout)
            text = text.replace(str(exe), f"./{src.stem}")
        elif src.suffix == ".sql":
            command = " ".join(["python", "sqlrun.py", rel] + args)
            r = _run([str(PY), str(SHARED / "sqlrun" / "sqlrun.py"), rel] + args, cwd, env, timeout, stdin)
            text = _decode(r.stdout)
        elif src.suffix == ".toy":
            command = " ".join(["python", "-m", "toymachine", "run", rel] + args)
            r = _run([str(PY), "-m", "toymachine", "run", rel] + args, cwd, env, timeout, stdin)
            text = _decode(r.stdout)
        elif src.suffix == ".S":
            mode = d.get("rv", "run")
            if mode not in ("run", "asm", "dis"):
                raise ValueError(f"{src}: rv= must be run, asm or dis")
            command = " ".join(["python", "-m", "rv", mode, rel] + args)
            r = _run([str(PY), "-m", "rv", mode, rel] + args, cwd, env, timeout, stdin)
            text = _decode(r.stdout)
        else:  # .sh
            if d.get("session"):
                sess = tmp / "session"
                sess.mkdir()
                for name in filter(None, d.get("copy", "").replace(",", " ").split()):
                    origin = cwd / name if (cwd / name).exists() else ROOT / "data" / "country" / name
                    shutil.copy2(origin, sess / name)
                script = tmp / "session.sh"
                script.write_text(_session_script(src.read_text(encoding="utf8"), d.get("fixtimes", False)),
                                  encoding="utf8")
                env["CH"] = str(cwd)
                r = _run(["bash", str(script)], sess, env, timeout, stdin)
                text = _decode(r.stdout)
                text = text.replace(str(sess), "~/session")
                command = None
            else:
                command = " ".join(["bash", rel] + args)
                r = _run(["bash", rel] + args, cwd, env, timeout, stdin)
                text = _decode(r.stdout)
        if not d.get("exit") and not d.get("session") and r.returncode not in (0, None):
            print(f"WARNING {src.name}: exited with status {r.returncode} but has no `capture: exit` directive "
                  "(a staged crash? add `exit`; otherwise fix the listing)", file=sys.stderr)
        if d.get("exit") and r.returncode not in (0, None):
            if not text.endswith("\n"):
                text += "\n"
            text += f"[exit status {r.returncode}]\n"
        text = text.replace(str(home), "~").replace(str(tmp), "/tmp/build")
        # a sanitizer report starts every line with the process number, which changes each run
        text = re.sub(r"==\d+==", "==1000==", text)
    text = text.replace(str(cwd.resolve()) + "/", "")
    text = re.sub(r"[^\s\"]*/site-packages/", "site-packages/", text)
    text = text.replace(str(ROOT) + "/", "")
    # nothing personal in print: the account and machine names become the series' own
    for real, shown in ((getpass.getuser(), "ada"), (socket.gethostname(), "laptop")):
        if real:
            text = re.sub(r"\b" + re.escape(real) + r"\b", shown, text)
    return text if command is None else f"$ {command}\n{text}"


def output_path(chapter: Path, src: Path) -> Path:
    return chapter / "outputs" / (src.stem + ".txt")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    chapter = (ROOT / sys.argv[1]).resolve()
    wanted = sys.argv[2:]
    found = find_listings(chapter)
    stems = [p.stem for p in found]
    dup = {s for s in stems if stems.count(s) > 1}
    if dup:
        print(f"two listings share a stem (outputs would collide): {sorted(dup)}")
        return 1
    if "--measured" in wanted:
        ms = measured_stems(chapter)
        found = [s for s in found if s.stem in ms]
    elif wanted:
        found = [s for s in found if any(s.stem.startswith(w) for w in wanted)]
    (chapter / "outputs").mkdir(exist_ok=True)
    for src in found:
        if src.suffix == ".py" and src.stem in sys.stdlib_module_names:
            print(f"WARNING {src.name}: named like a standard-library module; imports will pick it up instead "
                  "of the real module (rename it)", file=sys.stderr)
        out = run_listing(chapter, src)
        output_path(chapter, src).write_text(out, encoding="utf8")
        print(f"captured {src.name}: {len(out.splitlines())} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
