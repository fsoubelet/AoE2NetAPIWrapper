import pandas as pd

from aoe2netwrapper.models import (
    LastMatchResponse,
    LeaderBoardResponse,
    MatchLobby,
    NumOnlineResponse,
    RatingTimePoint,
    StringsResponse,
)
from loguru import logger


class Convert:
    """
    This is a convenience class providing methods to convert the outputs from the AoE2NetAPI query methods
    into pandas DataFrame objects.
    """

    @staticmethod
    def leaderboard(leaderboard_response: LeaderBoardResponse) -> pd.DataFrame:
        logger.debug("Converting LeaderBoardResponse leadrboard to DataFrame")
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
    def num_online(num_online_response: NumOnlineResponse) -> pd.DataFrame:
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
