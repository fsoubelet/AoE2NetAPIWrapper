# Getting Started

## Installation

This code is compatible with `Python 3.6+`.
This package is installable from PyPI with [pip]{target=_blank} in a virtual environment with:

```bash
pip install aoe2netwrapper
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
    
    This repository follows the `Google` docstring format, uses [Black][black_formatter] as a code formatter with a default enforced line length of 110 characters, and [Pylint][pylint_ref] as a linter.
    You can format the code with `make format` and lint it (which will format first) with `make lint`.
    
    Testing builds are ensured after each commit through Github Actions.
    You can run tests locally with the predefined `make tests`, or through `poetry run pytest <options>` for customized options.

## Quick Start

The package provides a simple, fully-typed high-level object to interact with each API provided by `aoe2.net`.
Each exposed endpoint from the APIs can be queried with a dedicated method named after it:

* __Complete Data API__

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

* __Nightbot API__

```python
from aoe2netwrapper import AoE2NightbotAPI

# Specify timeout limit for ALL requests at instantiation
nightbot = AoE2NightbotAPI(timeout=10)

# Get quick rank information on a specific player in 1v1 Random Map
viper_details = nightbot.rank(leaderboard_id=3, search="GL.TheViper")
print(viper_details)
# '🇳🇴 GL.TheViper (2501) Rank #1, has played 762 games with a 69% winrate, -1 streak, and 2 drops'
```

The full documentation for the API endpoints can be found at https://aoe2.net/#api and https://aoe2.net/#nightbot.
For convenience, it is also included in the methods' docstrings, and can be accessed in the `Reference` section.


[virtual_env_primer]: https://realpython.com/python-virtual-environments-a-primer/
[black_formatter]: https://github.com/psf/black
[pip]: https://pip.pypa.io/en/stable/
[Poetry]: https://python-poetry.org/
[pylint_ref]: https://www.pylint.org/
