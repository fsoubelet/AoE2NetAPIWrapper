<h1 align="center">
  <b>aoe2netwrapper</b>
</h1>

A simple typed wrapper to interact with the APIs provided by `https://aoe2.net`.

## Install

This package is compatible with `Python 3.6+`, and can be installed in your virtual enrivonment from PyPI with:
```bash
pip install aoe2netwrapper
```

## Quick Start

The package provides a simple, fully-typed high-level object to interact with each API provided by `aoe2.net`.
Each exposed endpoint from the APIs can be queried with a method named after it:

Complete data API:
```python
from aoe2netwrapper import AoE2NetAPI

client = AoE2NetAPI()

# Get the first 100 ranked accounts in 1v1 Random Map
top_accounts = client.leaderboard(game="aoe2de", leaderboard_id=3, start=1, count=100)

# Get the list of currently open lobbies
open_lobbies = client.lobbies(game="aoe2de")
```

Nightbot API:
```python
from aoe2netwrapper import AoE2NightbotAPI

nightbot = AoE2NightbotAPI()

# Get quick rank information on a specific player in 1v1 Random Map
viper_details = nightbot.rank(leaderboard_id=3, search="GL.TheViper")
print(viper_details) # -> '🇳🇴 GL.TheViper (2501) Rank #1, has played 762 games with a 69% winrate, -1 streak, and 2 drops'
```

The full documentation for the API endpoints can be found at `https://aoe2.net/#api` and `https://aoe2.net/#nightbot`, but is also included in the methods' docstrings for convenience.

## License

Copyright &copy; 2021 Felix Soubelet. [MIT License](LICENSE)