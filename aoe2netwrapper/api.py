"""
aoe2netwrapper.api
------------------

This module implements a high-level client to query the API at https://aoe2.net/#api.
"""

from typing import Any, Dict, List, Tuple, Union

import requests

from loguru import logger

from aoe2netwrapper.exceptions import Aoe2NetException


class AoE2NetAPI:
    """
    The 'AoE2NetAPI' class is a client that encompasses the https://aoe2.net/#api API  functions.
    """

    API_BASE_URL: str = "https://aoe2.net/api"
    STRINGS_ENDPOINT: str = API_BASE_URL + "/strings"
    LEADERBOARD_ENDPOINT: str = API_BASE_URL + "/leaderboard"
    LOBBIES_ENDPOINT: str = API_BASE_URL + "/lobbies"
    LAST_MATCH_ENDPOINT: str = API_BASE_URL + "/player/lastmatch"
    MATCH_HISTORY_ENDPOINT: str = API_BASE_URL + "/player/matches"
    RATING_HISTORY_ENDPOINT: str = API_BASE_URL + "/player/ratinghistory"
    MATCHES_ENDPOINT: str = API_BASE_URL + "/matches"
    MATCH_ENDPOINT: str = API_BASE_URL + "/match"
    NUMBER_ONLINE_ENDPOINT: str = API_BASE_URL + "/stats/players"

    def __init__(self, timeout: Union[float, Tuple[float, float]] = 5):
        """Creating a Session for connection pooling since we're always querying the same host."""
        self.session = requests.Session()
        self.timeout = timeout

    def __repr__(self) -> str:
        return f"Client for <{self.API_BASE_URL}>"

    def strings(self, game: str = "aoe2de") -> dict:
        """
        Requests a list of strings used by the API.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).

        Returns:
            A dictionnary with different strings used by the API, each with their list of possible
            values (also a dict each).
        """
        logger.debug("Preparing parameters for strings query")
        query_params = {"game": game}

        return _get_request_response_json(
            session=self.session,
            url=self.STRINGS_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def leaderboard(
        self,
        game: str = "aoe2de",
        leaderboard_id: int = 3,
        start: int = 1,
        count: int = 10,
        search: str = None,
        steam_id: int = None,
        profile_id: int = None,
    ) -> dict:
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
            search (str): To perform the search for a specific player, from their name.
            steam_id (int): To perform the search for a specific player, from their steamID64
                (ex: 76561199003184910).
            profile_id (int): To perform the search for a specific player, from their profile ID
                (ex: 459658).

        Raises:
            Aoe2NetException: if the 'count' parameter exceeds 10 000.

        Returns:
            A dictionnary with the different parameters used for the query, the 'total' amount of
            hits, and the leaderboard as a list profile entries for each ranking (a dict each).
        """
        if count > 10_000:
            logger.error(f"'count' has to be 10000 or less, but {count} was provided.")
            raise Aoe2NetException("Invalid value for parameter 'count'.")

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

        return _get_request_response_json(
            session=self.session,
            url=self.LEADERBOARD_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def lobbies(self, game: str = "aoe2de") -> List[dict]:
        """
        Request all open lobbies.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).

        Returns:
            A list of dictionaries, each one encapsulating the data for a currently open lobby.
        """
        logger.debug("Preparing parameters for open lobbies query")
        query_params = {"game": game}

        return _get_request_response_json(
            session=self.session,
            url=self.LOBBIES_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def last_match(
        self, game: str = "aoe2de", steam_id: int = None, profile_id: int = None
    ) -> dict:
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
            Aoe2NetException: if the not one of 'steam_id' or 'profile_id' are provided.

        Returns:
            A dictionary with the information of the game, including the following keys:
            'profile_id', 'steam_id', 'name', 'clan', 'country' & 'last_match', with 'last_match'
            being a dictionary with the match's information.
        """
        if not steam_id and not profile_id:
            logger.error("Missing one of 'steam_id', 'profile_id'.")
            raise Aoe2NetException(
                "Either 'steam_id' or 'profile_id' required, please provide one."
            )

        logger.debug("Preparing parameters for last match query")
        query_params = {"game": game, "steam_id": steam_id, "profile_id": profile_id}

        return _get_request_response_json(
            session=self.session,
            url=self.LAST_MATCH_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def match_history(
        self,
        game: str = "aoe2de",
        start: int = 0,
        count: int = 10,
        steam_id: int = None,
        profile_id: int = None,
    ) -> List[dict]:
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
            Aoe2NetException: if the 'count' parameter exceeds 1000.
            Aoe2NetException: if the not one of 'steam_id' or 'profile_id' are provided.

        Returns:
            A list of dictionaries, each one encapsulating the data for one of the player's
            previous matches.
        """
        if count > 1_000:
            logger.error(f"'count' has to be 1000 or less, but {count} was provided.")
            raise Aoe2NetException("Invalid value for parameter 'count'.")

        if not steam_id and not profile_id:
            logger.error("Missing one of 'steam_id', 'profile_id'.")
            raise Aoe2NetException(
                "Either 'steam_id' or 'profile_id' required, please provide one."
            )

        logger.debug("Preparing parameters for match history query")
        query_params = {
            "game": game,
            "start": start,
            "count": count,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        return _get_request_response_json(
            session=self.session,
            url=self.MATCH_HISTORY_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def rating_history(
        self,
        game: str = "aoe2de",
        leaderboard_id: int = 3,
        start: int = 0,
        count: int = 100,
        steam_id: int = None,
        profile_id: int = None,
    ) -> List[dict]:
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
            Aoe2NetException: if the 'count' parameter exceeds 10 000.
            Aoe2NetException: if the not one of 'steam_id' or 'profile_id' are provided.

        Returns:
            A list of dictionaries, each one encapsulating data at a certain point in time
            corresponding to a match played by the player, including the rating, timestamp of the
            match, streak etc.
        """
        if count > 10_000:
            logger.error(f"'count' has to be 10 000 or less, but {count} was provided.")
            raise Aoe2NetException("Invalid value for parameter 'count'.")

        if not steam_id and not profile_id:
            logger.error("Missing one of 'steam_id', 'profile_id'.")
            raise Aoe2NetException(
                "Either 'steam_id' or 'profile_id' required, please provide one."
            )

        logger.debug("Preparing parameters for rating history query")
        query_params = {
            "game": game,
            "leaderboard_id": leaderboard_id,
            "start": start,
            "count": count,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        return _get_request_response_json(
            session=self.session,
            url=self.RATING_HISTORY_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def matches(self, game: str = "aoe2de", count: int = 10, since: int = None) -> List[dict]:
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
            Aoe2NetException: if the 'count' parameter exceeds 1000.

        Returns:
            A list of dictionaries, each one encapsulating the data for one of the played matches
            during the time window queried for.
        """
        if count > 1000:
            logger.error(f"'count' has to be 1000 or less, but {count} was provided.")
            raise Aoe2NetException("Invalid value for parameter 'count'.")

        logger.debug("Preparing parameters for matches query")
        query_params = {
            "game": game,
            "count": count,
            "since": since,
        }

        return _get_request_response_json(
            session=self.session,
            url=self.MATCHES_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def match(self, game: str = "aoe2de", uuid: str = None, match_id: int = None) -> dict:
        """
        Request details about a match. Either 'uuid' or 'match_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            uuid (str): match UUID (ex: '66ec2575-5ee4-d241-a1fc-d7ffeffb48b6').
            match_id (int): match ID.

        Raises:
            Aoe2NetException: if the not one of 'uuid' or 'match_id' are provided.

        Returns:
            A dictionary with the information of the specific match, including.
        """
        if not uuid and not match_id:
            logger.error("Missing one of 'uuid', 'match_id'.")
            raise Aoe2NetException("Either 'uuid' or 'match_id' required, please provide one.")

        logger.debug("Preparing parameters for single match query")
        query_params = {
            "game": game,
            "uuid": uuid,
            "match_id": match_id,
        }

        return _get_request_response_json(
            session=self.session,
            url=self.MATCH_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def num_online(self, game: str = "aoe2de") -> dict:
        """
        Number of players in game and an estimate of the number current playing multiplayer.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).

        Returns:
            A dictionary with the app id and a list of the estimated 'num_players' metrics at
            different timestamps ('steam', 'multiplayer', 'looking', 'in_game', 'multiplayer_1h' &
            'multiplayer_24h').
        """
        logger.debug("Preparing parameters for number of online players query")
        query_params = {"game": game}

        return _get_request_response_json(
            session=self.session,
            url=self.NUMBER_ONLINE_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )


# ----- Helpers ----- #


def _get_request_response_json(
    session: requests.Session,
    url: str,
    params: Dict[str, Any] = None,
    timeout: Union[float, Tuple[float, float]] = None,
) -> dict:
    """
    Helper function to handle a GET request to an endpoint and return the response JSON content
    as a dictionary.

    Args:
        session (requests.Session): Session object to use, for connection pooling and performance.
        url (str): API endpoint to send the request to.
        params (dict): A dictionary of parameters for the GET request.

    Raises:
        Aoe2NetException: if the status code returned is not 200.

    Returns:
        The request's JSON response as a dictionary.
    """
    default_headers = {"content-type": "application/json;charset=UTF-8"}
    logger.debug(f"Sending GET request at '{url}'")
    logger.trace(f"Parameters are: {str(params)}")

    response = session.get(url, params=params, headers=default_headers, timeout=timeout)
    if response.status_code != 200:
        logger.error(
            f"GET request at '{response.url}' returned a {response.status_code} status code"
        )
        raise Aoe2NetException(f"Expected status code 200 - got {response.status_code} instead.")
    return response.json()
