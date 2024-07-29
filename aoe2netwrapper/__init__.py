"""
aoe2netwrapper library
----------------------

aoe2netwrapper is a utility library, written in Python 3, that provides high level clients to
query the APIs provided by aoe2.net, and get data about the Age of Empires II video game.

:copyright: (c) 2021 by Felix Soubelet.
:license: MIT, see LICENSE file for more details.
"""

from .api import AoE2NetAPI  # noqa: TID252
from .nightbot import AoE2NightbotAPI  # noqa: TID252

__version__ = "0.4.0"

__all__ = ["AoE2NetAPI", "AoE2NightbotAPI"]
