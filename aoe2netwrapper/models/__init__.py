"""
aoe2netwrapper.models
---------------------

This subpackage contains the model objects used to encapsulate responses from the API.
Each module therein contains the models for a specific API endpoint.
"""
from .last_match import LastMatchResponse
from .leaderboard import LeaderBoardResponse
from .lobbies import MatchLobby
from .match import MatchLobby
from .match_history import MatchLobby
from .matches import MatchLobby
from .num_online import NumOnlineResponse
from .rating_history import RatingTimePoint
from .strings import StringsResponse
