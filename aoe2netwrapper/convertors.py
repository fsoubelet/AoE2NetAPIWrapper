from typing import List

from loguru import logger

from aoe2netwrapper.models import (
    LastMatchResponse,
    LeaderBoardResponse,
    MatchLobby,
    NumOnlineResponse,
    RatingTimePoint,
    StringsResponse,
)

try:
    import pandas as pd
except ImportError:
    logger.error(
        "The 'aoe2netwrapper.convertors' module exports results to 'pandas.DataFrame' objects and "
        "needs the 'pandas' library installed to function."
    )
    raise NotImplementedError("The 'pandas' library is required but not installed.")


class Convert:
    """
    This is a convenience class providing methods to convert the outputs from the AoE2NetAPI query methods
    into pandas DataFrame objects. Every method below is a staticmethod, so no object has to be instantiated.
    """

    @staticmethod
    def leaderboard(leaderboard_response: LeaderBoardResponse) -> pd.DataFrame:
        """
        Convert the result given by a call to AoE2NetAPI().leaderboard to a pandas DataFrame.

        Args:
            leaderboard_response (LeaderBoardResponse): the response directly returned by your AoE2NetAPI
                client.

        Returns:
            A pandas DataFrame from the LeaderBoardResponse, each row being an entry in the leaderboard.
            Top level attributes such as 'start' or 'total' are broadcast to an entire array the size of
            the dataframe.
        """
        logger.debug("Converting LeaderBoardResponse leaderboard to DataFrame")
        dframe = pd.DataFrame(leaderboard_response.leaderboard)

        logger.trace("Exporting attributes to columns and removing duplicate data")
        for i in range(19):
            attribute = dframe[i][0][0]
            dframe[attribute] = dframe[i].apply(lambda x: x[1])
            del dframe[i]

        logger.trace("Inserting LeaderBoardResponse attributes as column")
        dframe["leaderboard_id"] = leaderboard_response.leaderboard_id
        dframe["start"] = leaderboard_response.start
        dframe["count"] = leaderboard_response.count
        dframe["total"] = leaderboard_response.total

        logger.trace("Converting datetimes")
        dframe["last_match"] = pd.to_datetime(dframe["last_match"], unit="s")
        dframe["last_match_time"] = pd.to_datetime(dframe["last_match_time"], unit="s")
        return dframe

    @staticmethod
    def lobbies(lobbies_response: List[MatchLobby]) -> pd.DataFrame:
        """
        Convert the result given by a call to AoE2NetAPI().lobbies to a pandas DataFrame.

        Args:
            lobbies_response (List[MatchLobby]): the response directly returned by your AoE2NetAPI
                client.

        Returns:
            A pandas DataFrame from the list of MatchLobby elements, each row being the information from
            one MatchLobby in the list. Beware: the 'players' column is directly the content of the
            'MatchLobby.players' attribute and as such holds a list of LobbyMember objects.
        """
        logger.debug("Converting Lobbies response to DataFrame")
        dframe = pd.DataFrame(lobbies_response)

        logger.trace("Exporting attributes to columns and removing duplicate data")
        for i in range(41):
            attribute = dframe[i][0][0]
            dframe[attribute] = dframe[i].apply(lambda x: x[1])
            del dframe[i]

        return dframe

    @staticmethod
    def num_online(num_online_response: NumOnlineResponse) -> pd.DataFrame:
        """
        Convert the result given by a call to AoE2NetAPI().num_online to a pandas DataFrame.

        Args:
            num_online_response (NumOnlineResponse): the response directly returned by your AoE2NetAPI
                client.

        Returns:
            A pandas DataFrame from the NumOnlineResponse, each row being an entry in the leaderboard.
            Top level attributes such as 'app_id' are broadcast to an entire array the size of the
            dataframe, and timestamps are converted to datetime objects.
        """
        logger.debug("Converting NumOnlineResponse to DataFrame")
        dframe = pd.DataFrame(num_online_response.dict())

        logger.trace("Exporting 'player_stats' attribute contents to columns")
        dframe["time"] = dframe.player_stats.apply(lambda x: x["time"]).apply(pd.to_datetime)
        dframe["steam"] = dframe.player_stats.apply(lambda x: x["num_players"]["steam"])
        dframe["looking"] = dframe.player_stats.apply(lambda x: x["num_players"]["looking"])
        dframe["in_game"] = dframe.player_stats.apply(lambda x: x["num_players"]["in_game"])
        dframe["multiplayer"] = dframe.player_stats.apply(lambda x: x["num_players"]["multiplayer"])
        dframe["multiplayer_1h"] = dframe.player_stats.apply(lambda x: x["num_players"]["multiplayer_1h"])
        dframe["multiplayer_24h"] = dframe.player_stats.apply(lambda x: x["num_players"]["multiplayer_24h"])

        logger.trace("Removing 'player_stats' column to avoid nested & duplicate data")
        del dframe["player_stats"]
        return dframe
