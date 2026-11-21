# Contributing to One Economics Book

These are the authoritative conventions of the series. The cross-subject rules (chapter anatomy, labels, visuals, quality
gates) are in the workspace's `book_style.md`. The editorial line is in `../economics_series.md`. What follows adds to them, or
overrides them, for economics.

## Project structure

```
one_economics_book_<N>_<slug>.tex           one entry file per book (5)
styles/oneeconomics.sty                     every package and macro; chapter files define nothing
styles/lang/en.tex                          UI strings, box names, part titles
parts/<year>/NN-<slug>.tex                  a chapter (grade-6 ... grade-12, bachelor-1 ... bachelor-3)
parts/<year>/solutions/NN-<slug>.tex        its solutions
parts/<year>/part.tex                       the frozen \ominput list of the year (do not reorder)
figdata/lib/econdata.py                     loaders of the approved datasets (the only way to read data/derived/)
figdata/lib/figout.py                       write_table(): how every chart table is written
figdata/<year>/NN-<slug>/make_<what>.py     a script that writes figdata/<year>/NN-<slug>/out/<table>.csv
figdata/<year>/NN-<slug>/test_<what>.py     its test (pytest)
code/<year>/NN-<slug>/{listings,outputs,exercises,tests}   Years 1-3 only: printed Python, captured output, tests
code/shared/country/                        Brenland and Kestria, the invented economies (COUNTRY.md), frozen
data/raw/                                   approved downloads (gitignored; tools/fetch_data.py)
data/derived/                               compact tables (gitignored; tools/derive_data.py)
data/country/                               the invented countries' tables (python -m country)
images/book<N>/                             photographs + CREDITS.md; ai/ illustrations (JPEG) + PROMPTS.md
sources/                                    outline provenance, ledgers, definition map, run files
tools/                                      gates, capture, term linker, ledger and calibration checks
```

Years map to books as follows: `grade-6` to `grade-9` are Book 1 (`g6`–`g9`); `grade-10` to `grade-12` are Book 2
(`g10`–`g12`); `bachelor-1/2/3` are Books 3/4/5 (`b1`–`b3`).

## Building and testing

```sh
PATH=~/texlive/2026/bin/x86_64-linux:$PATH latexmk one_economics_book_2_high_school.tex
bash tools/gates.sh grade-11           # prose, boxes and charts, calibration, ledger, structure
bash tools/gates.sh --log 2            # 0 errors / 0 undefined / 0 overfull in the last build of Book 2
bash tools/figdata.sh grade-11         # every chart table rebuilt twice (deterministic) and tested
bash tools/test_code.sh bachelor-1     # Years 1-3: ruff, pytest, listing ranges, outputs rerun
python3 tools/capture_output.py code/bachelor-1/30-regression-in-python
python3 tools/link_defined_terms.py --book 2 --unwrap --apply && python3 tools/link_defined_terms.py --book 2 --apply
```

## The economic frame

- **Every model gets a `model` box**, with four fields in this order: what it assumes, what it predicts, where it was tested,
  where it breaks. `tools/check_boxes.py` checks it.

  ```latex
  \begin{model}{Supply and demand}
  \assumes  Many buyers and sellers of one homogeneous good; prices free to move.
  \predicts A tax raises the price buyers pay by less than the tax, when both curves slope.
  \tested   Laboratory markets; the pass-through of fuel and cigarette taxes.
  \breaks   A market with a few sellers, or one where quality is hidden from buyers.
  \end{model}
  ```

  The box sums up the model. The model itself is taught in the chapter: its definition, its equations or diagram, a
  derivation, worked examples. The *tested* field cites real evidence, through a ledger row or a figdata table. The *breaks*
  field names real cases.
- **`debate[Title]`** holds an open **empirical** question: the competing estimates, each with its best study and its
  weaknesses. Use it for the employment effect of a minimum wage, the size of fiscal multipliers, trade and wages. It never
  holds a normative debate and never a school of thought.
- **`record[Title]`** is a dated episode used as a test: what happened, what the model said, and what that tells us. Examples
  are the stagflation of the 1970s, the Volcker disinflation, 2008 and the inflation of 2021–23. What the record refuted is
  taught as refuted.
- **`measure[Title]`** explains how a number is made: a price index, a poverty line, the unemployment survey, purchasing-power
  conversion, what GDP leaves out.
- **`recall`** is the *You already know* box, 3–5 lines; **`dated{2026}`** holds volatile facts, each with a ledger row.
  **There is no `history` box**, and nothing like one.
- **Names.** A person appears only as the name of a model or a result (Ricardo's model, the Solow model, the Lucas critique),
  as Pythagoras does in the mathematics books. Never write a biography, a "school" or a "tradition". Countries and dated
  episodes are named, because they are the evidence. A firm is named only with a public source.
- **No prescriptive titles** ("should", "ought"). A chapter says what a policy does, to whom and by how much. It shows private
  and contractual answers next to taxes and regulation, each with its evidence, and government failure next to market
  failure.
- **Neutral vocabulary.** A term that carries a verdict is never used as if it were neutral. Write "a tax on X", not "a
  penalty on X"; write "a transfer", not "a handout"; write "a price floor", not "a fair price".
- **Facts before models.** Every chapter from grade 7 opens with one `openingchart` before its first `\section`, and the
  chapter explains it. Grade 6 chapters have three or more `omchart`s and no model.

## Charts and data

- **Every chart is drawn from data.** pgfplots reads a CSV table that a tested script wrote. No chart image is copied, and no
  data point is typed into a chart (`tools/check_boxes.py` rejects `coordinates` inside a chart).

  ```latex
  \begin{openingchart}{Income per person, 1820--2022, in 2011 dollars at purchasing-power parity.}
                      {Maddison Project Database 2023}
  \begin{tikzpicture}
  \begin{semilogyaxis}[omtimesten, xlabel={Year}, ylabel={Dollars per person}]
    \addplot table[x=year, y=WLD] {figdata/grade-7/01-scarcity-and-opportunity-cost/out/world_gdppc.csv};
    \addplot table[x=year, y=GBR] {figdata/grade-7/01-scarcity-and-opportunity-cost/out/world_gdppc.csv};
    \legend{World, United Kingdom}
  \end{semilogyaxis}
  \end{tikzpicture}
  \end{openingchart}
  ```
- **Styles** in `styles/oneeconomics.sty`:

  | Style | Use it for | Axis environment |
  |---|---|---|
  | `omrecord` | the base style | any axis |
  | `omtime` | a time series | `axis` |
  | `omtimesten` | the times-ten scale before grade 12, the log scale after | `semilogyaxis` |
  | `omscatter` | a scatter plot (cycle list with marks) | `axis` |
  | `omincomex` | a scatter plot against income per person | `semilogxaxis` |

  **pgfplots cannot set `xmode`/`ymode` inside a style**, so choose the axis environment as shown. Before grade 12, a log
  axis is called a *times-ten scale*: ticks at 100, 1,000, 10,000, and no word "logarithm".
- **A figdata script** (`figdata/<year>/NN-<slug>/make_<what>.py`):
  - reads data only through `econdata` (approved datasets) or `country` (Brenland/Kestria);
  - writes with `figout.write_table(df, __file__, "<name>")`;
  - is deterministic;
  - has a pytest test beside it, `test_<what>.py`, that checks a fact the chart shows (the table's years, a value against
    the source, a sum).

  `tools/figdata.sh <year>` reruns and tests the scripts. The source line of a chart names the dataset as the Data Credits page
  does, and says which variable it shows: `econdata.SOURCE[...]` gives the dataset's name. When the prose quotes a number from
  a table, a `% figdata: <table>` comment goes next to it, and the number is copied exactly as the table rounds it.
- **Approved datasets only** (`sources/data_ledger.md`, "Approved datasets"). The licence filters are already applied:
  - WDI holds only the CC BY 4.0 indicators;
  - Gravity holds only the BACI flows;
  - Gapminder covers only the years before 1950. For later years use WDI, Maddison or PWT.

  JST is CC BY-NC-SA, like the books. A new dataset needs the user's yes: report it, never fetch it.
- **Invented data**: exercises with invented numbers use Brenland (dalens, `\dal{}`) and Kestria (kests, `\kst{}`), from
  `code/shared/country/`, or the chapter's own seeded script. Real and invented data are never mixed in one table.
- **Diagrams** are TikZ with the `econ` styles:
  - axes and curves: `econ axes`, `demand`, `supply`, `curve`, `shifted`, `guide`, `eqpoint`;
  - areas: `cs area`, `ps area`, `dwl area`, `tax area`;
  - other diagrams: `ppf`, `phase arrow`, `payoff`, and `forest` for game trees.

  A diagram's geometry must match the chapter's numbers: if the text says the equilibrium is $(4, 6)$, the drawn curves cross
  there. Check every figure on its own rendered page.

## Code in the books (Years 1–3 only)

Books 1–2 print no code. From Year 1, the data and econometrics chapters print Python from tested files, and the mechanics are
those of the computer science series:

- Print a listing with `\omcode{code/<year>/NN-<slug>/listings/<file>.py}{first}{last}{Caption}\label{lst:...}`, at most 40
  lines. Print an output with `\omoutput{code/.../outputs/<stem>.txt}{Caption}\label{out:...}`.
- **Never type an output.** Run `python3 tools/capture_output.py code/<year>/NN-<slug>`, which is the only writer of
  `outputs/`.
- A listing reads approved data through `econdata` and invented data through `country`. Both are on the path: `from econdata
  import pwt`, `from country import load`.
- Allowed libraries: pandas, numpy, statsmodels and scipy (versions in `requirements.txt`). No other packages, and no network.
- Every listing that is meant to work is exercised by a test in `tests/`. Every data exercise's solution is a tested file in
  `exercises/`.
- A regression output that prints many digits is fine, because it reruns byte for byte. The prose quotes it rounded, and says
  so.

## Statement environments

`definition`, `theorem`, `proposition`, `lemma`, `corollary`, `method`, `example`, `remark`, `notation`, `exercise`,
`problem`, `solution`, `proof`, `\admitted`, as in the family. A model's equilibrium, comparative statics and welfare results
are propositions with proofs at the level the mathematics allows. Money is written with the macros: `\usd{1.90}`, `\eur{120}`,
`\dal{120}`, `\kst{80}`. Never write a currency sign in math mode. The series notation is in `sources/SERIES_DEFINITIONS.md`.

## Labels

Labels have the form `<type>:<prefix>:<chapter-slug>:<name>`, with these types: `ch:`, `def:`, `thm:`, `prop:`, `lem:`,
`cor:`, `met:`, `ex:`, `rem:`, `not:`, `exo:`, `pb:`, `sec:`, `fig:`, `tab:`, `lst:`, `out:`. Reference with `\cref` inside a
book. Across books, reference in prose only.

## Licensing of contributions

One Economics Book is free for everyone under the licences in the [README](README.md#license). Contributing means agreeing to
the following.

1. **Same licence in as out.** Your contribution is licensed under the same terms as the part of the repository it changes:
   CC BY-NC-SA 4.0 for book content ([`LICENSE`](LICENSE)), MIT for the software — `code/`, `figdata/`, `tools/`, the
   `Makefile` and the build scripts ([`LICENSE-CODE`](LICENSE-CODE)).
2. **Sign off every commit** with `git commit -s`, which adds a line such as `Signed-off-by: Your Name <you@example.com>`. It
   certifies the [Developer Certificate of Origin 1.1](https://developercertificate.org): you wrote the change or have the
   right to submit it. For this project, "the open source license indicated in the file" in the certificate means the licences
   named in point 1.
3. **Relicensing grant.** You grant Benjamin Virrion a perpetual, worldwide, non-exclusive, royalty-free and irrevocable right
   to use, modify and relicense your contribution under other terms, including commercial ones (print editions, licences for
   schools, publishers or companies, paid app versions). You keep the copyright in your contribution and may use it as you
   wish.

**By signing off your commits you certify the DCO and agree to this whole section, including the relicensing grant in point
3.** Why the grant exists: the books stay free under CC BY-NC-SA for every reader. The grant only lets the author fund the
project through commercial editions without having to trace and ask every past contributor. Commits without a sign-off cannot
be merged.
