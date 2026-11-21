#!/usr/bin/env bash
# Rebuild and test the chart tables of one year or one chapter:
#   bash tools/figdata.sh grade-6            (every chapter of the year)
#   bash tools/figdata.sh grade-6/02-living-standards
# Runs every make_*.py of the chapter(s) twice (capped at 3 GB, niced) and fails
# if the second run changes a byte (scripts must be deterministic), then runs the
# chapter(s)' pytest files. Needs data/derived/ (tools/derive_data.py).
set -u
cd "$(dirname "$0")/.."
t=${1:?usage: tools/figdata.sh <year>[/NN-slug]}
PY=.venv/bin/python
export PYTHONPATH=figdata/lib:code/shared OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
fail=0

for d in $(ls -d figdata/$t/ figdata/$t/[0-9]*/ 2>/dev/null | sort -u); do
  ls "$d"/make_*.py >/dev/null 2>&1 || continue
  for s in "$d"/make_*.py; do
    systemd-run --user --scope -q -p MemoryMax=3G -p MemorySwapMax=0 nice -n 10 $PY "$s" \
      || { echo "  FAIL $s"; fail=1; continue; }
  done
  [ -d "$d/out" ] || continue
  before=$(cat "$d"/out/* 2>/dev/null | sha256sum)
  for s in "$d"/make_*.py; do
    systemd-run --user --scope -q -p MemoryMax=3G -p MemorySwapMax=0 nice -n 10 $PY "$s" >/dev/null 2>&1
  done
  after=$(cat "$d"/out/* 2>/dev/null | sha256sum)
  [ "$before" = "$after" ] || { echo "  NOT DETERMINISTIC: $d"; fail=1; }
done
# Tests run one chapter directory at a time (each in its own process), so that two chapters' make_*.py modules
# of the same name never collide. (Before 2026-11-20 21:00 an `ls` with an unmatched glob skipped this step.)
for d in $(ls -d figdata/$t/ figdata/$t/[0-9]*/ 2>/dev/null | sort -u); do
  compgen -G "$d/test_*.py" >/dev/null || continue
  systemd-run --user --scope -q -p MemoryMax=3G -p MemorySwapMax=0 nice -n 10 \
    $PY -m pytest -q "$d" >/tmp/figdata_pytest.$$ 2>&1 \
    || { echo "  TEST FAIL $d"; tail -15 /tmp/figdata_pytest.$$; fail=1; }
done
rm -f /tmp/figdata_pytest.$$
[ $fail = 0 ] && echo "  [figdata $t] OK"
exit $fail
