PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: verify pdf submission-flat title-page reproducibility-package packages clean all

verify:
	$(PYTHON) code/verify_symbolic.py
	$(PYTHON) code/verify_numerical.py

pdf:
	cd paper && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex
	cp paper/main.pdf output/manuscript.pdf

submission-flat:
	$(PYTHON) submission/build_flat_package.py
	cd output/international-economics-flat && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex

reproducibility-package:
	$(PYTHON) submission/build_reproducibility_package.py

title-page:
	cd submission && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error title_page.tex

packages: submission-flat reproducibility-package

clean:
	cd paper && $(LATEXMK) -C main.tex || true
	cd submission && $(LATEXMK) -C title_page.tex || true
	rm -f output/manuscript.pdf output/international-economics-submission-source.zip output/reproducibility-supplement.zip
	rm -rf output/international-economics-flat

all: verify pdf packages title-page
