"""
aoe2netwrapper.api
------------------

This module implements a high-level client to query the API at https://aoe2.net/#api.
"""

from __future__ import annotations

from typing import Any

import requests

from loguru import logger
from pydantic import TypeAdapter

from aoe2netwrapper.exceptions import Aoe2NetError, RemovedApiEndpointError
from aoe2netwrapper.models import (
    LastMatchResponse,
    LeaderBoardResponse,
    MatchLobby,
    NumOnlineResponse,
    RatingTimePoint,
    StringsResponse,
)

_MAX_LEADERBOARD_COUNT: int = 10_000
_MAX_MATCH_HISTORY_COUNT: int = 1_000
_MAX_RATING_HISTORY_COUNT: int = 10_000
_MAX_MATCHES_COUNT: int = 1_000
_OK_STATUS_CODE: int = 200

_LIST_MATCHLOBBY_ADAPTER = TypeAdapter(list[MatchLobby])
_LIST_RATINGTIMEPOINT_ADAPTER = TypeAdapter(list[RatingTimePoint])


class AoE2NetAPI:
    """
    The 'AoE2NetAPI' class is a client that encompasses the https://aoe2.net/#api API endpoints.
    Each method in this class corresponds name for name to an endpoint, and will do the work in querying then
    parsing and validating the response before returning it.
    """

    _API_BASE_URL: str = "https://aoe2.net/api"
    _STRINGS_ENDPOINT: str = _API_BASE_URL + "/strings"
    _LEADERBOARD_ENDPOINT: str = _API_BASE_URL + "/leaderboard"
    _LOBBIES_ENDPOINT: str = _API_BASE_URL + "/lobbies"
    _LAST_MATCH_ENDPOINT: str = _API_BASE_URL + "/player/lastmatch"
    _MATCH_HISTORY_ENDPOINT: str = _API_BASE_URL + "/player/matches"
    _RATING_HISTORY_ENDPOINT: str = _API_BASE_URL + "/player/ratinghistory"
    _MATCHES_ENDPOINT: str = _API_BASE_URL + "/matches"
    _MATCH_ENDPOINT: str = _API_BASE_URL + "/match"
    _NUMBER_ONLINE_ENDPOINT: str = _API_BASE_URL + "/stats/players"

    def __init__(self, timeout: float | tuple[float, float] = 5):
        """Creating a Session for connection pooling since we're always querying the same host."""
        self.session = requests.Session()
        self.timeout = timeout

    def __repr__(self) -> str:
        return f"Client for <{self._API_BASE_URL}>"

    def strings(self, game: str = "aoe2de") -> StringsResponse:
        """
        Requests a list of strings used by the API.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).

        Returns:
            A StringsResponse validated object encapsulating the strings used by the API.
        """
        logger.debug("Preparing parameters for strings query")
        query_params = {"game": game}

        processed_response = _get_request_response_json(
            session=self.session,
            url=self._STRINGS_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )
        logger.trace(f"Validating response from '{self._STRINGS_ENDPOINT}'")
        return StringsResponse(**processed_response)

    def leaderboard(
        self,
        game: str = "aoe2de",
        leaderboard_id: int = 3,
        start: int = 1,
        count: int = 10,
        search: str | None = None,
        steam_id: int | None = None,
        profile_id: int | None = None,
    ) -> LeaderBoardResponse:
        """
        Request the current leaderboards.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            leaderboard_id (int): Leaderboard to extract the data for (Unranked=0,
                1v1 Deathmatch=1, Team Deathmatch=2, 1v1 Random Map=3, Team Random Map=4).
                Defaults to 3.
            start (int): Starting rank (ignored if search, steam_id, or profile_id are defined).
                Defaults to 1.
            count (int): Number of leaderboard entries to get (warning: must be 10000 or less).
                Defaults to 10.
            search (str): Optional. To perform the search for a specific player, from their name.
            steam_id (int): Optional. To perform the search for a specific player, from their
                steamID64 (ex: 76561199003184910).
            profile_id (int): Optional. To perform the search for a specific player, from their
                profile ID (ex: 459658).

        Raises:
            Aoe2NetError: if the 'count' parameter exceeds 10 000.

        Returns:
            A LeaderBoardResponse validated object with the different parameters used for the
            query, the total amount of hits, and the leaderboard as a list profile entries for
            each ranking.
        """
        if count > _MAX_LEADERBOARD_COUNT:
            logger.error(f"'count' has to be 10000 or less, but {count} was provided.")
            msg = "Invalid value for parameter 'count'."
            raise Aoe2NetError(msg)

        logger.debug("Preparing parameters for leaderboard query")
        query_params = {
            "game": game,
            "leaderboard_id": leaderboard_id,
            "start": start,
            "count": count,
            "search": search,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        processed_response = _get_request_response_json(
            session=self.session,
            url=self._LEADERBOARD_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )
        logger.trace(f"Validating response from '{self._LEADERBOARD_ENDPOINT}'")
        return LeaderBoardResponse(**processed_response)

    def lobbies(self, game: str = "aoe2de") -> list[MatchLobby]:
        """
        Request all open lobbies.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).

        Returns:
            A list of MatchLobby valideted objects, each one encapsulating the data for a currently
            open lobby.
        """
        # logger.debug("Preparing parameters for open lobbies query")
        # query_params = {"game": game}

        # processed_response = _get_request_response_json(
        #     session=self.session,
        #     url=self._LOBBIES_ENDPOINT,
        #     params=query_params,
        #     timeout=self.timeout,
        # )
        # logger.trace(f"Validating response from '{self._LOBBIES_ENDPOINT}'")
        # return _LIST_MATCHLOBBY_ADAPTER.validate_python(processed_response)
        logger.error(f"Tried to query {self._LOBBIES_ENDPOINT} endpoint, which was removed by aoe2.net")
        raise RemovedApiEndpointError(self._LOBBIES_ENDPOINT)

    def last_match(
        self, game: str = "aoe2de", steam_id: int | None = None, profile_id: int | None = None
    ) -> LastMatchResponse:
        """
        Request the last match the player started playing, this will be the current match if they
        are still in game. Either 'steam_id' or 'profile_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            steam_id (int): The player's steamID64 (ex: 76561199003184910).
            profile_id (int): The player's profile ID (ex: 459658).

        Raises:
            Aoe2NetError: if the not one of 'steam_id' or 'profile_id' are provided.

        Returns:
            A LastMatchResponse validated object with the information of the game, including the
            following attributes: 'profile_id', 'steam_id', 'name', 'clan', 'country' and
            'last_match'.
        """
        # if not steam_id and not profile_id:
        #     logger.error("Missing one of 'steam_id', 'profile_id'.")
        #     msg = "Either 'steam_id' or 'profile_id' required, please provide one."
        #     raise Aoe2NetError(msg)

        # logger.debug("Preparing parameters for last match query")
        # query_params = {"game": game, "steam_id": steam_id, "profile_id": profile_id}

        # processed_response = _get_request_response_json(
        #     session=self.session,
        #     url=self._LAST_MATCH_ENDPOINT,
        #     params=query_params,
        #     timeout=self.timeout,
        # )
        # logger.trace(f"Validating response from '{self._LAST_MATCH_ENDPOINT}'")
        # return LastMatchResponse(**processed_response)
        logger.error(f"Tried to query {self._LAST_MATCH_ENDPOINT} endpoint, which was removed by aoe2.net")
        raise RemovedApiEndpointError(self._LAST_MATCH_ENDPOINT)

    def match_history(
        self,
        game: str = "aoe2de",
        start: int = 0,
        count: int = 10,
        steam_id: int | None = None,
        profile_id: int | None = None,
    ) -> list[MatchLobby]:
        """
        Request the match history for a player. Either 'steam_id' or 'profile_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            start (int): starting match (0 is the most recent match). Defaults to 0.
            count (int): number of matches to get (must be 1000 or less). Defaults to 10.
            steam_id (int): The player's steamID64 (ex: 76561199003184910).
            profile_id (int): The player's profile ID (ex: 459658).

        Raises:
            Aoe2NetError: if the 'count' parameter exceeds 1000.
            Aoe2NetError: if the not one of 'steam_id' or 'profile_id' are provided.

        Returns:
            A list of MatchLobby validated objects, each one encapsulating the data for one of the
            player's previous matches.
        """
        if count > _MAX_MATCH_HISTORY_COUNT:
            logger.error(f"'count' has to be 1000 or less, but {count} was provided.")
            msg = "Invalid value for parameter 'count'."
            raise Aoe2NetError(msg)

        if not steam_id and not profile_id:
            logger.error("Missing one of 'steam_id', 'profile_id'.")
            msg = "Either 'steam_id' or 'profile_id' required, please provide one."
            raise Aoe2NetError(msg)

        logger.debug("Preparing parameters for match history query")
        query_params = {
            "game": game,
            "start": start,
            "count": count,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        processed_response = _get_request_response_json(
            session=self.session,
            url=self._MATCH_HISTORY_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )
        logger.trace(f"Validating response from '{self._MATCH_HISTORY_ENDPOINT}'")
        return _LIST_MATCHLOBBY_ADAPTER.validate_python(processed_response)

    def rating_history(
        self,
        game: str = "aoe2de",
        leaderboard_id: int = 3,
        start: int = 0,
        count: int = 20,
        steam_id: int | None = None,
        profile_id: int | None = None,
    ) -> list[RatingTimePoint]:
        """
        Requests the rating history for a player. Either 'steam_id' or 'profile_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            leaderboard_id (int): Leaderboard to extract the data for (Unranked=0,
                1v1 Deathmatch=1, Team Deathmatch=2, 1v1 Random Map=3, Team Random Map=4).
                Defaults to 3.
            start (int): starting match (0 is the most recent match). Defaults to 0.
            count (int): number of matches to get the rating for (must be 1000 or less). Defaults
                to 100.
            steam_id (int): The player's steamID64 (ex: 76561199003184910).
            profile_id (int): The player's profile ID (ex: 459658).

        Raises:
            Aoe2NetError: if the 'count' parameter exceeds 10 000.
            Aoe2NetError: if the not one of 'steam_id' or 'profile_id' are provided.

        Returns:
            A list of RatingTimePoint validated objects, each one encapsulating data at a certain
            point in time corresponding to a match played by the player, including the rating,
            timestamp of the match, streaks etc.
        """
        if count > _MAX_RATING_HISTORY_COUNT:
            logger.error(f"'count' has to be 10 000 or less, but {count} was provided.")
            msg = "Invalid value for parameter 'count'."
            raise Aoe2NetError(msg)

        if not steam_id and not profile_id:
            logger.error("Missing one of 'steam_id', 'profile_id'.")
            msg = "Either 'steam_id' or 'profile_id' required, please provide one."
            raise Aoe2NetError(msg)

        logger.debug("Preparing parameters for rating history query")
        query_params = {
            "game": game,
            "leaderboard_id": leaderboard_id,
            "start": start,
            "count": count,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        processed_response = _get_request_response_json(
            session=self.session,
            url=self._RATING_HISTORY_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )
        logger.trace(f"Validating response from '{self._RATING_HISTORY_ENDPOINT}'")
        return _LIST_RATINGTIMEPOINT_ADAPTER.validate_python(processed_response)

    def matches(self, game: str = "aoe2de", count: int = 10, since: int | None = None) -> list[MatchLobby]:
        """
        Request matches after a specific time: the match history in an optionally given time
        window.

        If 'since' is not set, only the X amount of current past matches (specified by 'count')
        will be returned.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            count (int): number of matches to get (must be 1000 or less). Defaults to 10.
            since (int): only show matches starting after 'since' timestamp (epoch).

        Raises:
            Aoe2NetError: if the 'count' parameter exceeds 1000.

        Returns:
            A list of MatchLobby validated objects, each one encapsulating the data for one of the
            played matches during the time window queried for.
        """
        # if count > _MAX_MATCHES_COUNT:
        #     logger.error(f"'count' has to be 1000 or less, but {count} was provided.")
        #     msg = "Invalid value for parameter 'count'."
        #     raise Aoe2NetError(msg)

        # logger.debug("Preparing parameters for matches query")
        # query_params = {
        #     "game": game,
        #     "count": count,
        #     "since": since,
        # }

        # processed_response = _get_request_response_json(
        #     session=self.session,
        #     url=self._MATCHES_ENDPOINT,
        #     params=query_params,
        #     timeout=self.timeout,
        # )
        # logger.trace(f"Validating response from '{self._MATCHES_ENDPOINT}'")
        # return _LIST_MATCHLOBBY_ADAPTER.validate_python(processed_response)
        logger.error(f"Tried to query {self._MATCHES_ENDPOINT} endpoint, which was removed by aoe2.net")
        raise RemovedApiEndpointError(self._MATCHES_ENDPOINT)

    def match(self, game: str = "aoe2de", uuid: str | None = None, match_id: int | None = None) -> MatchLobby:
        """
        Request details about a match. Either 'uuid' or 'match_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            uuid (str): match UUID (ex: '66ec2575-5ee4-d241-a1fc-d7ffeffb48b6').
            match_id (int): match ID.

        Raises:
            Aoe2NetError: if the not one of 'uuid' or 'match_id' are provided.

        Returns:
            A MatchLobby validated object with the information of the specific match, including.
        """
        # if not uuid and not match_id:
        #     logger.error("Missing one of 'uuid', 'match_id'.")
        #     msg = "Either 'uuid' or 'match_id' required, please provide one."
        #     raise Aoe2NetError(msg)

        # logger.debug("Preparing parameters for single match query")
        # query_params = {
        #     "game": game,
        #     "uuid": uuid,
        #     "match_id": match_id,
        # }

        # processed_response = _get_request_response_json(
        #     session=self.session,
        #     url=self._MATCH_ENDPOINT,
        #     params=query_params,
        #     timeout=self.timeout,
        # )
        # logger.trace(f"Validating response from '{self._MATCH_ENDPOINT}'")
        # return MatchLobby(**processed_response)
        logger.error(f"Tried to query {self._MATCH_ENDPOINT} endpoint, which was removed by aoe2.net")
        raise RemovedApiEndpointError(self._MATCH_ENDPOINT)

    def num_online(self, game: str = "aoe2de") -> NumOnlineResponse:
        """
        Number of players in game and an estimate of the number current playing multiplayer.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).

        Returns:
            A NumOnlineResponse validated object with the app id and a list of PlayerCountTimePoint
            validated objects encapsulating estimated metrics at different timestamps ('steam',
            'multiplayer', 'looking', 'in_game', 'multiplayer_1h' & 'multiplayer_24h').
        """
        # logger.debug("Preparing parameters for number of online players query")
        # query_params = {"game": game}

        # processed_response = _get_request_response_json(
        #     session=self.session,
        #     url=self._NUMBER_ONLINE_ENDPOINT,
        #     params=query_params,
        #     timeout=self.timeout,
        # )
        # logger.trace(f"Validating response from '{self._NUMBER_ONLINE_ENDPOINT}'")
        # return NumOnlineResponse(**processed_response)
        logger.error(f"Tried to query {self._NUMBER_ONLINE_ENDPOINT} endpoint, which was removed by aoe2.net")
        raise RemovedApiEndpointError(self._NUMBER_ONLINE_ENDPOINT)


# ----- Helpers ----- #


def _get_request_response_json(
    session: requests.Session,
    url: str,
    params: dict[str, Any] | None = None,
    timeout: float | tuple[float, float] | None = None,
) -> dict:
    """
    Helper function to handle a GET request to an endpoint and return the response JSON content
    as a dictionary.

    Args:
        session (requests.Session): Session object to use, for connection pooling and performance.
        url (str): API endpoint to send the request to.
        params (dict): A dictionary of parameters for the GET request.

    Raises:
        Aoe2NetError: if the status code returned is not 200.

    Returns:
        The request's JSON response as a dictionary.
    """
    default_headers = {"content-type": "application/json;charset=UTF-8"}
    logger.debug(f"Sending GET request at '{url}'")
    logger.trace(f"Parameters are: {params!s}")

    response = session.get(url, params=params, headers=default_headers, timeout=timeout)
    if response.status_code != _OK_STATUS_CODE:
        logger.error(f"GET request at '{response.url}' returned a {response.status_code} status code")
        msg = f"Expected status code 200 - got {response.status_code} instead"
        raise Aoe2NetError(msg)
    return response.json()
