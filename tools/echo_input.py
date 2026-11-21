#!/usr/bin/env python3
"""Run a Python listing so that what input() reads is echoed, as on a terminal.

    python tools/echo_input.py program.py [args...] < program.stdin

On a terminal the reader's answer appears after the prompt because the terminal
echoes it; with a file on standard input nothing echoes. This wrapper replaces
input() by one that prints the line it read, so a captured output shows the
session exactly as the reader sees it. The program itself is unchanged and runs
as __main__ (sys.argv[0] is its own name). Used only by tools/capture_output.py.
"""
import builtins
import os
import runpy
import sys
import traceback

_real_input = builtins.input


def _echo_input(prompt=""):
    sys.stdout.write(str(prompt))
    sys.stdout.flush()
    line = sys.stdin.readline()
    if not line:
        raise EOFError
    line = line.rstrip("\n")
    sys.stdout.write(line + "\n")
    sys.stdout.flush()
    return line


if not sys.stdin.isatty():
    builtins.input = _echo_input
script = sys.argv[1]
sys.argv = sys.argv[1:]
sys.path.insert(0, ".")
try:
    runpy.run_path(script, run_name="__main__")
except SystemExit:
    raise
except BaseException as exc:  # print the traceback as `python script.py` would: no runner frames
    target = os.path.abspath(script)
    tb = exc.__traceback__
    while tb is not None and os.path.abspath(tb.tb_frame.f_code.co_filename) != target:
        tb = tb.tb_next
    if isinstance(exc, SyntaxError):
        tb = None
    sys.stdout.flush()
    traceback.print_exception(type(exc), exc, tb)
    sys.exit(1)
