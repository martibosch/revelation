# Makefile

######################################

PROJECT    := $(shell basename $(PWD))
PACKAGE    := "revelation"
BUILD_TIME := $(shell date +%FT%T%z)

######################################

.PHONY: install
install: # system-wide standard python installation
	pip install .

.PHONY: install.hack
install.hack: # install development requirements
	pip install -r requirements.txt
	pip install -e .[test]

.PHONY: build
build: # build package for distribuition
	rm -rf dist
	python setup.py sdist
	python setup.py bdist_wheel --universal

.PHONY: publish
publish: # publish package to the pypi
	twine upload dist/*

.PHONY: it
it:
	@echo "Any color you want, as long as it's Black"

.PHONY: black
black:
	black -l 79 .

.PHONY: clean
clean: # remove temporary files and artifacts
	rm -rf site/
	rm -rf *.egg-info dist build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '.coverage' -exec rm -f {} +
	find . -name '__pycache__' -exec rmdir {} +
