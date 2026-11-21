#!/usr/bin/env bash
# Chapter-level gates for one year:  bash tools/gates.sh grade-11
# The build-log gate is separate (bash tools/gates.sh --log <book number>, after a fresh latexmk).
# The code gates are tools/test_code.sh <year>; the chart tables tools/figdata.sh <year>. Exit 1 on any failure.
set -u
cd "$(dirname "$0")/.."
if [ "${1:-}" = "--log" ]; then
  n=${2:?usage: tools/gates.sh --log <book number>}
  L=$(ls build/one_economics_book_${n}_*.log 2>/dev/null | grep -v '_[a-z][a-z]\.log$' | head -1)
  [ -f "$L" ] || { echo "no log for book $n in build/"; exit 2; }
  e=$(grep -ac '^!' "$L"); u=$(grep -aci 'undefined' "$L"); o=$(grep -ac 'Overfull' "$L")
  echo "  [book $n] $L: errors $e, undefined $u, overfull $o"
  [ "$e" = 0 ] && [ "$u" = 0 ] && [ "$o" = 0 ] && exit 0 || exit 1
fi
y=${1:?usage: tools/gates.sh <year>}
d=parts/$y
[ -d "$d" ] || { echo "no such year: $d"; exit 2; }
case $y in
  grade-1[0-2]) pfx=g${y#grade-};    book=2 ;;
  grade-*)      pfx=g${y#grade-};    book=1 ;;
  bachelor-*)   pfx=b${y#bachelor-}; book=$(( ${y#bachelor-} + 2 )) ;;
esac
fail=0
say() { echo "  [$y] $*"; }

# 1. every exo:/pb: label has exactly one solution, in the same order
if [ -d "$d/solutions" ]; then
for f in "$d"/[0-9]*.tex; do
  s="$d/solutions/$(basename "$f")"
  if ! diff -q <(grep -o 'label{\(exo\|pb\):[^}]*}' "$f" | sed 's/label{//;s/}//') \
               <(grep -o 'begin{solution}{[^}]*}' "$s" | sed 's/begin{solution}{//;s/}//') >/dev/null; then
    say "exercise/solution mismatch: $(basename "$f")"; fail=1
  fi
done
fi
# 2. duplicate labels across the whole English tree (reported for this year's prefix only)
dups=$(find parts -name '*.tex' -not -path '*/fr/*' -not -path '*/nl/*' -not -path '*/es/*' \
         -not -path '*/pt/*' -not -path '*/hi/*' -not -path '*/ar/*' -not -path '*/id/*' -not -path '*/zh/*' -print0 \
       | xargs -0 grep -ho 'label{[^}]*}' | sort | uniq -d | grep ":$pfx:")
[ -n "$dups" ] && { say "duplicate labels: $dups"; fail=1; }
# 3. typo classes
grep -rn 'end{[a-z]*>' "$d" && { say "\\end{...> typo"; fail=1; }
grep -rn '\.\.\.' "$d" --include='*.tex' | grep -v '\\dots\|\\foreach\|^\S*:\s*%\|,\s*\.\.\.\s*,\|\\code{[^}]*\.\.\.' \
  && { say 'drafty "..." (use \dots; inside \code{} it is fine)'; fail=1; }
# 4. prose: straight quotes, curriculum names, e-mail, pasted code, cross-book refs, dated boxes,
#    schools and history of thought, prescriptive titles, history boxes
python3 tools/check_prose.py "$d" >/dev/null || { python3 tools/check_prose.py "$d"; fail=1; }
# 4b. boxes and charts: model boxes with their four fields, titled debate/record/measure boxes,
#     one opening chart per chapter (grade 6: three charts or more), every chart from a figdata table
python3 tools/check_boxes.py "$d" >/dev/null || { python3 tools/check_boxes.py "$d"; fail=1; }
# 4c. chapters still standing as stubs: a warning, not a failure
ns=$(grep -l '% STUB' "$d"/[0-9]*.tex 2>/dev/null | wc -l)
[ "$ns" -gt 0 ] && say "WARNING: $ns chapter(s) still stubs"
# 5. weekend-problem answers numbered 1..k
python3 tools/check_problem_numbering.py "$d" >/dev/null || { python3 tools/check_problem_numbering.py "$d"; fail=1; }
# 6. pics in a scaled picture carry [transform shape]
python3 tools/check_pic_scaling.py "$d" >/dev/null || { python3 tools/check_pic_scaling.py "$d"; fail=1; }
# 7. AI images must be JPEG (this year's book)
ls images/book$book/ai/*.png 2>/dev/null && { say "PNG illustrations: transcode to JPEG"; fail=1; }
# 7b. grey stubs still standing in for AI illustrations: a warning, not a failure
n=$(python3 tools/ai_stubs.py --book $book --list 2>/dev/null | grep -c "images/book$book/ai/$pfx-")
[ "$n" -gt 0 ] && say "WARNING: $n grey stub illustration(s) still to generate (tools/ai_stubs.py --book $book --list)"
# 8. every % ledger: id has a row; ledger ids unique, sourced and dated
python3 tools/check_ledger.py "$d" >/dev/null || { python3 tools/check_ledger.py "$d"; fail=1; }
# 9. the band's exercise count, star ramp and weekend-problem length
python3 tools/check_exercise_calibration.py "$d" >/dev/null || { python3 tools/check_exercise_calibration.py "$d"; fail=1; }
# 10. every \omcode / \omcodes of this year names an existing file and a range of at most 40 lines
python3 tools/check_omcode.py "$d/" >/dev/null || { python3 tools/check_omcode.py "$d/"; fail=1; }
# 11. every \omoutput of this year names an output file whose listing exists (rerun: tools/test_code.sh)
python3 tools/check_outputs.py --no-run "$y/" >/dev/null || { python3 tools/check_outputs.py --no-run "$y/"; fail=1; }

[ $fail = 0 ] && echo "  [$y] gates OK"
exit $fail
