# Getting Started

## Installation

This code is compatible with `Python 3.6+`.
This package is installable from PyPI with [pip]{target=_blank} in a virtual environment with:

```bash
> pip install aoe2netwrapper
```

!!! tip "Installation in a virtual environment"
    Don't know what a **virtual environment** is or how to set it up? Here is a good
    [primer on virtual environments][virtual_env_primer]{target=_blank} by RealPython.

??? question "How about a development environment?"

    Sure thing. This repository uses [Poetry]{target=_blank} as a packaging and build tool. 
    To set yourself up, get a local copy through VCS and run:
    
    ```bash
    poetry install
    ```
    
    This repository follows the `Google` docstring format, uses [Black][black_formatter] as a code formatter with a default enforced line length of 100 characters, and [Pylint][pylint_ref] as a linter.
    You can format the code with `make format` and lint it (which will format first) with `make lint`.
    
    Testing builds are ensured after each commit through Github Actions.
    You can run tests locally with the predefined `make tests`, or through `poetry run pytest <options>` for customized options.


[virtual_env_primer]: https://realpython.com/python-virtual-environments-a-primer/
[black_formatter]: https://github.com/psf/black
[pip]: https://pip.pypa.io/en/stable/
[Poetry]: https://python-poetry.org/
[pylint_ref]: https://www.pylint.org/
