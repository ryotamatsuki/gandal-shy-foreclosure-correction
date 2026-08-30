PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: verify pdf clean all

verify:
	$(PYTHON) code/verify_symbolic.py
	$(PYTHON) code/verify_numerical.py

pdf:
	cd paper && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex
	cp paper/main.pdf output/manuscript.pdf

clean:
	cd paper && $(LATEXMK) -C main.tex || true
	rm -f output/manuscript.pdf

all: verify pdf
