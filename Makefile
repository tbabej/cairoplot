# Makefile

# The MIT License (MIT)

# Copyright (c) 2013 Cairoplot team

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

BUILDDIR = build
PYTHON_VER := $(word 1,$(wordlist 2,4,$(subst ., ,$(shell python --version 2>&1))))
PYTHON=python
ifeq ($(PYTHON_VER),3)
	PYTHON = python2
endif

.PHONY : all test test-series install clean

define HELPTEXT
Please use 'make <target>' where <target> is one of
  GENERAL TARGETS
    help         show this help message.
    all          to build source, default doc (man target) and run all tests.
    clean        clean all built files.

  SOURCE TARGETS
    build        build all source file to the $(BUILDDIR).
    install      install CairoPlot.

  TEST TARGETS
    test         run all test with $(PYTHON).
    test-series  test only the series module.

  DOCS TARGETS
    html         to make standalone HTML files
    dirhtml      to make HTML files named index.html in directories
    singlehtml   to make a single large HTML file
    pickle       to make pickle files
    json         to make JSON files
    htmlhelp     to make HTML files and a HTML help project
    qthelp       to make HTML files and a qthelp project
    devhelp      to make HTML files and a Devhelp project
    epub         to make an epub
    latex        to make LaTeX files, you can set PAPER=a4 or PAPER=letter
    latexpdf     to make LaTeX files and run them through pdflatex
    text         to make text files
    man          to make manual pages
    texinfo      to make Texinfo files
    info         to make Texinfo files and run them through makeinfo
    gettext      to make PO message catalogs
    changes      to make an overview of all changed/added/deprecated items
    linkcheck    to check all external links for integrity
    doctest      to run all doctests embedded in the documentation (if enabled)
endef
export HELPTEXT

help:
	@echo "$$HELPTEXT"

include docs/Makefile
all: build test
test: test-series

build:
	@echo "»»» Building cairoplot..."
	@$(PYTHON) setup.py build

test-series:
	@echo "»»» Testing cairoplot with the series module..."
	@$(PYTHON) test/series_tests.py

install:
	@echo "»»» Installing cairoplot..."
	@$(PYTHON) setup.py install

clean:
	@echo "»»» Cleaning..."
	@rm -rf $(BUILDDIR)

