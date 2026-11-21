.PHONY: all clean distclean venv test test-fast gates country derive figdata scan

PY := .venv/bin/python
TL := PATH=$(HOME)/texlive/2026/bin/x86_64-linux:$$PATH

all:
	$(TL) latexmk

clean:
	$(TL) latexmk -c

distclean:
	$(TL) latexmk -C

# System python3 has no ensurepip, hence the bootstrap through the user's pip.
venv:
	python3 -m venv --without-pip .venv
	pip --python $(PY) install -r requirements.txt

# Every code test (Y=<year> or Y=<year>/<chapter> to scope it): ruff, pytest, C, C++, Rust,
# listing ranges, and every printed output rerun byte for byte.
test:
	bash tools/test_code.sh $(Y)

# The same without rerunning outputs (they are exact only on the machine that captured them).
test-fast:
	OCS_TESTS=fast bash tools/test_code.sh $(Y)

# Every chapter-level gate over every year (tools/gates.sh <year> for one).
gates:
	@for y in parts/*/; do bash tools/gates.sh $$(basename $$y) || exit 1; done

# Rewrite data/country/*.csv (Brenland and Kestria) from the seed; must leave no diff.
country:
	cd code/shared && ../../$(PY) -m country

# Rebuild data/derived/ from data/raw/ (main session only; data/raw/ comes from
# tools/fetch_data.py, which fetches only the approved sources).
derive:
	$(PY) -I tools/derive_data.py

# Rebuild and test the chart tables of one year: make figdata Y=grade-7
figdata:
	bash tools/figdata.sh $(Y)

# Scan data/raw/ with Windows Defender (WSL only).
scan:
	bash tools/scan_data.sh
