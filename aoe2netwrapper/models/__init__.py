"""
aoe2netwrapper.models
---------------------

This subpackage contains the model objects used to encapsulate responses from the API.
Each module therein contains the models for a specific API endpoint.
"""
from .last_match import LastMatchResponse
from .leaderboard import LeaderBoardResponse
from .lobbies import MatchLobby
from .strings import StringsResponse
