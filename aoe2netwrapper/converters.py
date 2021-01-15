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
        "The 'aoe2netwrapper.converters' module exports results to 'pandas.DataFrame' objects and "
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
            the dataframe, and timestamps are converted to datetime objects.
        """
        logger.debug("Converting LeaderBoardResponse leaderboard to DataFrame")
        dframe = pd.DataFrame(leaderboard_response.leaderboard)
        dframe = _export_tuple_elements_to_column_values_format(dframe)

        logger.trace("Inserting LeaderBoardResponse attributes as columns")
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
            'MatchLobby.players' attribute and as such holds lists of LobbyMember objects.
        """
        logger.debug("Converting Lobbies response to DataFrame")
        dframe = pd.DataFrame(lobbies_response)
        return _export_tuple_elements_to_column_values_format(dframe)

    @staticmethod
    def last_match(last_match_response: LastMatchResponse) -> pd.DataFrame:
        """
        Convert the result given by a call to AoE2NetAPI().last_match to a pandas DataFrame. There is not
        much use to this as the DataFrame will only have one row, but the method is provided nonetheless in
        case users want to concatenate several of these results in a DataFrame.

        Args:
            last_match_response (LastMatchResponse): the response directly returned by your AoE2NetAPI
                client.

        Returns:
            A pandas DataFrame from the list of LastMatchResponse attributes. Beware: the 'players'
            column is directly the content of the 'LastMatchResponse.last_match.players' attribute and as
            such holds a list of LobbyMember objects.
        """
        logger.debug("Converting LastMatchResponse last_match to DataFrame")
        dframe = pd.DataFrame(last_match_response.last_match).transpose()
        dframe.columns = dframe.iloc[0]
        dframe = dframe.drop(0).reset_index()

        logger.trace("Inserting LastMatchResponse attributes as columns")
        dframe["profile_id"] = last_match_response.profile_id
        dframe["steam_id"] = last_match_response.steam_id
        dframe["name"] = last_match_response.name
        dframe["country"] = last_match_response.country
        return dframe

    @staticmethod
    def match_history(match_history_response: List[MatchLobby]) -> pd.DataFrame:
        """
        Convert the result given by a call to AoE2NetAPI().match_history to a pandas DataFrame.

        Args:
            match_history_response (List[MatchLobby]): the response directly returned by your AoE2NetAPI
                client.

        Returns:
            A pandas DataFrame from the list of MatchLobby elements, each row being the information from
            one MatchLobby in the list. Beware: the 'players' column is directly the content of the
            'MatchLobby.players' attribute and as such holds lists of LobbyMember objects.
        """
        logger.debug("Converting Match History response to DataFrame")
        dframe = pd.DataFrame(match_history_response)
        return _export_tuple_elements_to_column_values_format(dframe)

    @staticmethod
    def rating_history(rating_history_response: List[RatingTimePoint]) -> pd.DataFrame:
        """
        Convert the result given by a call to AoE2NetAPI().leaderboard to a pandas DataFrame.

        Args:
            rating_history_response (List[RatingTimePoint]): the response directly returned by your AoE2NetAPI
                client.

        Returns:
            A pandas DataFrame from the list of RatingTimePoint elements, each row being the information from
            one RatingTimePoint in the list. Timestamps are converted to datetime objects.
        """
        logger.debug("Converting Rating History rsponse to DataFrame")
        dframe = pd.DataFrame(rating_history_response)
        dframe = _export_tuple_elements_to_column_values_format(dframe)

        logger.trace("Converting timestamps to datetime objects")
        dframe["time"] = pd.to_datetime(dframe["timestamp"], unit="s")
        dframe = dframe.drop(columns=["timestamp"])
        return dframe

    @staticmethod
    def matches(matches_response: List[MatchLobby]) -> pd.DataFrame:
        """
        Convert the result given by a call to AoE2NetAPI().match_history to a pandas DataFrame.

        Args:
            matches_response (List[MatchLobby]): the response directly returned by your AoE2NetAPI
                client.

        Returns:
            A pandas DataFrame from the list of MatchLobby elements, each row being the information from
            one MatchLobby in the list. Beware: the 'players' column is directly the content of the
            'MatchLobby.players' attribute and as such holds lists of LobbyMember objects.
        """
        logger.debug("Converting Match History response to DataFrame")
        dframe = pd.DataFrame(match_history_response)
        return _export_tuple_elements_to_column_values_format(dframe)

    @staticmethod
    def match(match_response: MatchLobby) -> pd.DataFrame:
        """
        Convert the content of a MatchLobby to a pandas DataFrame. The resulting DataFrame will have as many
        rows as there are players in the lobby, and all global attributes will be broadcasted to columns of
        the same length, making them duplicates.

        Args:
            match_response (MatchLobby): a MatchLobby object.

        Returns:
            A pandas DataFrame from the MatchLobby attributes, each row being global information from the
            MatchLobby as well as one of the players in the lobby.
        """
        return _unfold_match_lobby_to_dataframe(match_response)

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
        dframe = dframe.drop(columns=["player_stats"])
        return dframe


# ----- Helpers ----- #


def _export_tuple_elements_to_column_values_format(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Take in a pandas DataFrame with simple int values as columns, and elements being a tuple of
    (attribute_name, value) and cast it to have the attribute_name as column names, and the values as values.
    The original columns will be dropped in the process.

    Args:
        dataframe (pd.DataFrame): your pandas DataFrame.

    Returns:
        The refactored pandas DataFrame.
    """
    dframe = dataframe.copy(deep=True)
    logger.trace("Exporting attributes to columns and removing duplicate data")
    for _, col_index in enumerate(dframe.columns):
        attribute = dframe[col_index][0][0]
        dframe[attribute] = dframe[col_index].apply(lambda x: x[1])
        dframe = dframe.drop(columns=[col_index])
    return dframe


def _unfold_match_lobby_to_dataframe(match_lobby: MatchLobby) -> pd.DataFrame:
    """
    Convert the content of a MatchLobby to a pandas DataFrame. The resulting DataFrame will have as many
    rows as there are players in the lobby, and all global attributes will be broadcasted to columns of the
    same length, making them duplicates.

    Args:
        match_lobby (MatchLobby): a MatchLobby object.

    Returns:
        A pandas DataFrame from the MatchLobby attributes, each row being global information from the
        MatchLobby as well as one of the players in the lobby.
    """
    logger.trace("Unfolding MatchLobby.players contents to DataFrame")
    dframe = pd.DataFrame(match_lobby.players)
    dframe = _export_tuple_elements_to_column_values_format(dframe)

    logger.trace("Broadcasting global MatchLobby attributes")
    for attribute, value in match_lobby.dict().items():
        if attribute != "players":
            dframe[attribute] = value

    logger.trace("Converting timestamps to datetime objects")
    dframe["opened"] = pd.to_datetime(dframe["opened"], unit="s")
    dframe["started"] = pd.to_datetime(dframe["started"], unit="s")
    dframe["finished"] = pd.to_datetime(dframe["finished"], unit="s")

    return dframe
