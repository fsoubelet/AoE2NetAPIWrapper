<h1 style="text-align:center">
  <b>aoe2netwrapper</b>
</h1>

<p style="text-align:center">
  <!-- PyPi Version -->
  <a href="https://pypi.org/project/aoe2netwrapper">
    <img alt="PyPI Version" src="https://img.shields.io/pypi/v/aoe2netwrapper?label=PyPI&logo=PyPI">
  </a>

  <!-- Github Release -->
  <a href="https://github.com/fsoubelet/AoE2NetAPIWrapper/releases">
    <img alt="Github Release" src="https://img.shields.io/github/v/release/fsoubelet/AoE2NetAPIWrapper?color=orange&label=Release&logo=Github">
  </a>

  <br/>

  <!-- Github Actions Build -->
  <a href="https://github.com/fsoubelet/AoE2NetAPIWrapper/actions?query=workflow%3A%22Cron+Testing%22">
    <img alt="Github Actions" src="https://github.com/fsoubelet/AoE2NetAPIWrapper/workflows/Cron%20Testing/badge.svg">
  </a>

  <!-- Code Coverage -->
  <a href="https://codeclimate.com/github/fsoubelet/AoE2NetAPIWrapper/maintainability">
    <img alt="Code Coverage" src="https://img.shields.io/codeclimate/maintainability/fsoubelet/AoE2NetAPIWrapper?label=Maintainability&logo=Code%20Climate">
  </a>

  <br/>

  <!-- Code style -->
  <a href="https://github.com/psf/Black">
    <img alt="Code Style" src="https://img.shields.io/badge/Code%20Style-Black-9cf.svg">
  </a>

  <!-- Linter -->
  <a href="https://github.com/PyCQA/pylint">
    <img alt="Linter" src="https://img.shields.io/badge/Linter-Pylint-ce963f.svg">
  </a>

  <!-- Build tool -->
  <a href="https://github.com/python-poetry/poetry">
    <img alt="Build tool" src="https://img.shields.io/badge/Build%20Tool-Poetry-4e5dc8.svg">
  </a>

  <!-- Test runner -->
  <a href="https://github.com/pytest-dev/pytest">
    <img alt="Test runner" src="https://img.shields.io/badge/Test%20Runner-Pytest-ce963f.svg">
  </a>

  <!-- License -->
  <a href="https://github.com/fsoubelet/AoE2NetAPIWrapper/blob/master/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/fsoubelet/AoE2NetAPIWrapper?color=9cf&label=License">
  </a>
</p>

<p style="text-align:center">
  A simple typed wrapper to interact with the https://aoe2.net APIs
</p>

<p style="text-align:center">
  <a href="https://www.python.org/">
    <img alt="Made With Python" src="https://forthebadge.com/images/badges/made-with-python.svg">
  </a>
</p>

## Install

This package is compatible with `Python 3.6+`, and can be installed in your virtual enrivonment from PyPI with:
```bash
pip install aoe2netwrapper
```

## Quick Start

The package provides a simple, fully-typed high-level object to interact with each API provided by `aoe2.net`.
Each exposed endpoint from the APIs can be queried with a method named after it:

* __Complete data API__
```python
from aoe2netwrapper import AoE2NetAPI

client = AoE2NetAPI(timeout=10)

# Get the first 100 ranked accounts in 1v1 Random Map
top_accounts = client.leaderboard(game="aoe2de", leaderboard_id=3, start=1, count=100)

# Get the list of currently open lobbies
open_lobbies = client.lobbies(game="aoe2de")
```

* __Nightbot API__
```python
from aoe2netwrapper import AoE2NightbotAPI

nightbot = AoE2NightbotAPI(timeout=10)

# Get quick rank information on a specific player in 1v1 Random Map
viper_details = nightbot.rank(leaderboard_id=3, search="GL.TheViper")
print(viper_details)
# '🇳🇴 GL.TheViper (2501) Rank #1, has played 762 games with a 69% winrate, -1 streak, and 2 drops'
```

The full documentation for the API endpoints can be found at https://aoe2.net/#api and https://aoe2.net/#nightbot, but is also included in the methods' docstrings for convenience.

## License

Copyright &copy; 2021 Felix Soubelet. [MIT License](LICENSE)