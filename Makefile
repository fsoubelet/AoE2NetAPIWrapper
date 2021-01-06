# Copyright 2019 Felix Soubelet <felix.soubelet@cern.ch>
# MIT License

# Documentation for most of what you will see here can be found at the following links:
# for the GNU make special targets: https://www.gnu.org/software/make/manual/html_node/Special-Targets.html
# for python packaging: https://docs.python.org/3/distutils/introduction.html

# ANSI escape sequences for bold, cyan, dark blue, end, pink and red.
B = \033[1m
C = \033[96m
D = \033[34m
E = \033[0m
P = \033[95m
R = \033[31m

.PHONY : help clean format install lines lint tests type

all: install

help:
	@echo "Please use 'make $(R)<target>$(E)' where $(R)<target>$(E) is one of:"
	@echo "  $(R) clean $(E)  \t  to recursively remove build, run, and bitecode files/dirs."
	@echo "  $(R) format $(E)  \t  to recursively apply PEP8 formatting through the $(P)Black$(E) cli tool."
	@echo "  $(R) install $(E)  \t  to $(D)poetry install$(E) this package into the project's virtual environment."
	@echo "  $(R) lines $(E)  \t  to count lines of code with the $(P)tokei$(E) tool."
	@echo "  $(R) lint $(E)  \t  to lint the code though $(P)Pylint$(E)."
	@echo "  $(R) tests $(E)  \t  to run tests with the $(P)pytest$(E) package."
	@echo "  $(R) type $(E)  \t  to run type checking with the $(P)mypy$(E) package."

clean:
	@echo "Cleaning up distutils remains."
	@rm -rf build
	@rm -rf dist
	@rm -rf aoe2netwrapper.egg-info
	@rm -rf .eggs
	@echo "Cleaning up bitecode files and python cache."
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	@echo "Cleaning up pytest cache."
	@find . -type d -name '*.pytest_cache' -exec rm -rf {} + -o -type f -name '*.pytest_cache' -exec rm -rf {} +
	@echo "Cleaning up mypy cache."
	@find . -type d -name "*.mypy_cache" -exec rm -rf {} +
	@echo "Cleaning up coverage reports."
	@find . -type f -name '.coverage' -exec rm -rf {} + -o -type f -name 'coverage.xml' -delete
	@echo "All cleaned up!\n"

format:
	@echo "Sorting imports and formatting code to PEP8, default line length is 100 characters."
	@poetry run isort . && black .

install: format clean
	@echo "Installing through $(D)poetry$(E), with dev dependencies but no extras."
	@poetry install

lines: format
	@tokei .

lint: format
	@echo "Linting code"
	@poetry run pylint aoe2netwrapper/

tests: format clean
	@poetry run pytest --cov=aoe2netwrapper --cov-report term-missing
	@make clean

type: format
	@echo "Checking code typing with mypy"
	@poetry run mypy --pretty --no-strict-optional --show-error-codes --warn-redundant-casts --ignore-missing-imports --follow-imports skip aoe2netwrapper
	@make clean

# Catch-all unknow targets without returning an error. This is a POSIX-compliant syntax.
.DEFAULT:
	@echo "Make caught an invalid target! See help output below for available targets."
	@make help
