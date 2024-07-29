# Getting Started

## Installation

This package is compatible with all currently supported Python versions.
It is installable from `PyPI` with [pip]{target=_blank} in your virtual environment with:

```bash
python -m pip install aoe2netwrapper
```

The package is also accessible from the `conda-forge` channel, and can be installed in a `conda` environment with:

```bash
conda install -c conda-forge aoe2netwrapper
```

!!! tip "Installation in a virtual environment"
    Don't know what a **virtual environment** is or how to set it up? Here is a good
    [primer on virtual environments][virtual_env_primer]{target=_blank} by RealPython.

??? info "Extra Dependencies"
    It is also possible to install with extra dependencies to access export functionnality from the package, with:
    ```bash
    python -m pip install aoe2netwrapper[dataframe]
    ```

??? question "How about a development environment?"
    Sure thing. This repository uses [Hatch](https://github.com/pypa/hatch/){target=_blank} as a packaging and build tool, though it is not strictly necessary.
    To set yourself up, get a local copy through VCS and run:

    ```bash
    python -m pip install --editable ".[all]"
    ```
    
    The package will be installed in editable mode, alongside all dependencies (tests, docs).
    This repository follows the `Google` docstring format, uses [Black](https://github.com/psf/black/){target=_blank} as a code formatter with a default enforced line length of 110 characters, and [Ruff](https://github.com/astral-sh/ruff/){target=_blank} as a linter.
    A Makefile is included with some useful commands, which one can list with `make help`.
    
    Testing builds are ensured after each commit through Github Actions.
    You can run tests locally with the predefined `make tests`.

## Quick Start

The package provides a simple, fully-typed high-level object to interact with each API provided by [aoe2.net](https://aoe2.net/){target=_blank}.
Each exposed endpoint from the APIs can be queried with a dedicated method named after it:

* **Complete Data API**

```python
from aoe2netwrapper import AoE2NetAPI

# Specify timeout limit for ALL requests at instantiation
client = AoE2NetAPI(timeout=10)

# Get the first 100 ranked accounts in 1v1 Random Map
top_accounts = client.leaderboard(
    game="aoe2de", leaderboard_id=3, start=1, count=100
)

# Get the list of currently open lobbies
open_lobbies = client.lobbies(game="aoe2de")
```

* **Nightbot API**

```python
from aoe2netwrapper import AoE2NightbotAPI

# Specify timeout limit for ALL requests at instantiation
nightbot = AoE2NightbotAPI(timeout=10)

# Get quick rank information on a specific player in 1v1 Random Map
viper_details = nightbot.rank(leaderboard_id=3, search="GL.TheViper")
print(viper_details)
# '🇳🇴 GL.TheViper (2501) Rank #1, has played 762 games with a 69% winrate, -1 streak, and 2 drops'
```

* **Converting Results to Pandas DataFrames**

```python
from aoe2netwrapper import AoE2NetAPI
from aoe2netwrapper.converters import Convert

client = AoE2NetAPI(timeout=10)

# Get the list of currently open lobbies, as a pandas dataframe
open_lobbies = client.lobbies(game="aoe2de")
lobbies_dframe = Convert.lobbies(open_lobbies)
```

The full documentation for the API endpoints can be found at https://aoe2.net/#api and https://aoe2.net/#nightbot.
For convenience, it is also included in the methods' docstrings, and can be accessed in the `Reference` section.

[pip]: https://pip.pypa.io/en/stable/
[virtual_env_primer]: https://realpython.com/python-virtual-environments-a-primer/