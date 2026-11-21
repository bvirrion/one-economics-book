# CLAUDE.md — one-economics-book

Five LaTeX books: grades 6–9, grades 10–12, and University Years 1–3. 172 chapters, English first. The outline of record is
`OUTLINE.md`, approved 2026-11-20. The editorial line is in `../economics_series.md`, the conventions in `CONTRIBUTING.md`,
and the family style in `../book_style.md`.

- **State (2026-11-21): all five English books are written and closed "verified and read".** There are 172 chapters and
  2,017 pp: Book 1, grades 6–9, 280 pp; Book 2, grades 10–12, 416 pp; Books 3–5, University Years 1–3, 396, 455 and 470 pp.
  Every book is 0/0/0, with its gates, figdata tests and `test_code.sh` green. They were written 2026-11-20/21 under
  `sources/BATCH_BOOKS_1-5.md`: one Opus 5.5 writer per book, all five at once, then one fresh Opus reader per book. The
  readers found 32/114/136/49/85 defects, all fixed. The data comes from 20 approved datasets from 14 providers (USGS was dropped: no file
  with a macro or binary part). Nothing is committed; there are no translations and no HTML reader yet.
- **Closing standard: "verified and read"** (user, 2026-11-20). The writer re-checks its solutions, the main session
  verifies the book, and then a fresh Opus reader reads the whole book and recomputes every solution. The reader starts only
  once the writer is idle.
- **Build** with TeX Live 2026 only: `PATH=~/texlive/2026/bin/x86_64-linux:$PATH latexmk <entry>.tex`.
- **Data:** only the approved sources in `sources/data_ledger.md` ("Approved datasets"). `tools/fetch_data.py` fetches them
  (official hosts only; macros, executables and unsafe archives are rejected) and `tools/derive_data.py` reduces them to
  `data/derived/`. Chart scripts read them through `figdata/lib/econdata.py` only. **No other download without the user's
  yes.**
- **Charts:** every chart is pgfplots over a CSV written by a tested script in `figdata/<year>/NN-slug/`; run
  `tools/figdata.sh <year>`. Invented data come from Brenland and Kestria (`code/shared/country/`, frozen).
- **Code (Years 1–3 only):** `\omcode` / `\omoutput` from `code/<year>/NN-slug/`; `tools/capture_output.py` is the only
  writer of outputs; check with `tools/test_code.sh <year>`.
- **Gates:** `tools/gates.sh <year>` covers prose (it bans schools of thought, the history of thought and prescriptive
  titles), boxes and charts, calibration, the ledger and code references. Then `tools/gates.sh --log <N>`.
- **Weekly limit:** the file `sources/PAUSE` stops the writers. For this run it is created at **97 %** of the week (user,
  2026-11-20).
- **Never** commit; download a dataset without approval; name a curriculum or a university in print; print anything
  personal; mention a school of economic thought.
