"""
aoe2netwrapper.models
---------------------

This subpackage contains the model objects used to encapsulate responses from the API.
Each module therein contains the models for a specific API endpoint.
"""

from .last_match import LastMatchResponse  # noqa: TID252
from .leaderboard import LeaderBoardResponse  # noqa: TID252
from .lobbies import MatchLobby  # noqa: TID252
from .num_online import NumOnlineResponse  # noqa: TID252
from .rating_history import RatingTimePoint  # noqa: TID252
from .strings import StringsResponse  # noqa: TID252

__all__ = [
    "LastMatchResponse",
    "LeaderBoardResponse",
    "MatchLobby",
    "NumOnlineResponse",
    "RatingTimePoint",
    "StringsResponse",
]
