# one-economics-book

One Economics Book: five free textbooks forming one coherent course in economics, from Grade 6 to the end of the bachelor's degree: the long-run facts first, then the models that work (each with what it assumes, predicts, where it was tested and where it breaks), with charts redrawn from public data, Python for data and econometrics from Year 1, graded exercises and full solutions. Part of the One Course project (one-course.com).

## Build

```sh
make venv                                              # .venv: pandas, statsmodels, pytest, ruff
PATH=~/texlive/2026/bin/x86_64-linux:$PATH latexmk one_economics_book_1_middle_school.tex
tools/test_code.sh                                     # every listing, output and test
```

## License

- **How to credit**: One Economics Book, One Course (one-course.com).
- **Book content** — the LaTeX sources, figures, and the PDF and HTML editions — is licensed under
  [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
  (CC BY-NC-SA 4.0): you may share and adapt it, including translating it, with credit to
  One Economics Book, for non-commercial purposes, and adaptations must use the same licence. See [`LICENSE`](LICENSE).
- **Software** — `code/`, `tools/`, `.github/`, the `Makefile` and the build scripts — is licensed under the MIT licence: see [`LICENSE-CODE`](LICENSE-CODE).
- **Third-party material** (photographs, public-domain images, bundled fonts) keeps its own licence, as listed in
  the books' image-credit pages.
- **Names and logos**: "One Course" and "One Economics Book" are not covered by these licences.
- **Commercial use** (print editions, licences for schools, publishers or companies): contact One Course via [one-course.com/contact](https://one-course.com/contact).
