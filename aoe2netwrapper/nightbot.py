"""
aoe2netwrapper.nightbot
-----------------------

This module implements a high-level client to query the API at https://aoe2.net/#nightbot.
"""

from __future__ import annotations

from typing import Any

import requests

from loguru import logger

from aoe2netwrapper.exceptions import NightBotError

_OK_STATUS_CODE: int = 200


class AoE2NightbotAPI:
    """
    The 'AoE2NightbotAPI' class is a client that encompasses the https://aoe2.net/#nightbot API endpoints,
    which only return their requested data as plain text.
    """

    NIGHTBOT_BASE_URL: str = "https://aoe2.net/api/nightbot"
    RANK_DETAILS_ENDPOINT = NIGHTBOT_BASE_URL + "/rank"
    RECENT_OPPONENT_ENDPOINT = NIGHTBOT_BASE_URL + "/opponent"
    CURRENT_MATCH_ENDPOINT = NIGHTBOT_BASE_URL + "/match"
    CURRENT_CIVS_ENDPOINT = NIGHTBOT_BASE_URL + "/civs"
    CURRENT_MAP_ENDPOINT = NIGHTBOT_BASE_URL + "/map"

    def __init__(self, timeout: float | tuple[float, float] = 5):
        """Creating a Session for connection pooling since we're always querying the same host."""
        self.session = requests.Session()
        self.timeout = timeout

    def __repr__(self) -> str:
        return f"Client for <{self.NIGHTBOT_BASE_URL}>"

    def rank(
        self,
        game: str = "aoe2de",
        leaderboard_id: int = 3,
        language: str = "en",
        flag: str = "true",
        search: str | None = None,
        steam_id: int | None = None,
        profile_id: int | None = None,
    ) -> str:
        """
        Request rank details about a player. Either 'search', 'steam_id' or 'profile_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            leaderboard_id (int): Leaderboard to extract the data for (Unranked=0,
                1v1 Deathmatch=1, Team Deathmatch=2, 1v1 Random Map=3, Team Random Map=4).
                Defaults to 3.
            language (str): language for the returned response ('en', 'de', 'el', 'es', 'es-MX',
                'fr', 'hi', 'it', 'ja', 'ko', 'ms', 'nl', 'pt', 'ru', 'tr', 'vi', 'zh', 'zh-TW').
                Defaults to 'en'.
            flag (str): boolean to show the player flag. Defaults to 'true'. Needs to be a string
                for now since requests transforms True boolean to 'True' and the API rejects that.
            search (str): To perform the search for a specific player, from their name. Will
                return the highest rated player that matches the search.
            steam_id (int): To perform the search for a specific player, from their steamID64
                (ex: 76561199003184910).
            profile_id (int): To perform the search for a specific player, from their profile ID
                (ex: 459658).

        Raises:
            NightBotError: if the not one of 'search', 'steam_id' or 'profile_id' are provided.

        Returns:
            The text content of the response, as a decoded unicode string, with a quick sentence
            of information about the player.
        """
        if not any((search, steam_id, profile_id)):
            logger.error("Missing one of 'search', 'steam_id', 'profile_id'.")
            msg = "Either 'search', 'steam_id' or 'profile_id' required, please provide one."
            raise NightBotError(msg)

        logger.debug("Preparing parameters for rank details query")
        query_params = {
            "game": game,
            "leaderboard_id": leaderboard_id,
            "language": language,
            "flag": flag,
            "search": search,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        return _get_request_text_response_decoded(
            session=self.session,
            url=self.RANK_DETAILS_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def opponent(
        self,
        game: str = "aoe2de",
        leaderboard_id: int = 3,
        language: str = "en",
        flag: str = "true",
        search: str | None = None,
        steam_id: int | None = None,
        profile_id: int | None = None,
    ) -> str:
        """
        Request rank details about a player's most recent opponent (1v1 only). Either 'search',
        'steam_id' or 'profile_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            leaderboard_id (int): Leaderboard to extract the data for (Unranked=0,
                1v1 Deathmatch=1, Team Deathmatch=2, 1v1 Random Map=3, Team Random Map=4).
                Defaults to 3.
            language (str): language for the returned response ('en', 'de', 'el', 'es', 'es-MX',
                'fr', 'hi', 'it', 'ja', 'ko', 'ms', 'nl', 'pt', 'ru', 'tr', 'vi', 'zh', 'zh-TW').
                Defaults to 'en'.
            flag (str): boolean to show the player flag. Defaults to 'true'. Needs to be a string
                for now since requests transforms True boolean to 'True' and the API rejects that.
            search (str): To perform the search for a specific player, from their name. Will
                return the highest rated player that matches the search.
            steam_id (int): To perform the search for a specific player, from their steamID64
                (ex: 76561199003184910).
            profile_id (int): To perform the search for a specific player, from their profile ID
                (ex: 459658).

        Raises:
            NightBotError: if the not one of 'search', 'steam_id' or 'profile_id' are provided.

        Returns:
            The text content of the response, as a decoded unicode string, with a quick sentence
            of information about the player's last opponent.
        """
        if not any((search, steam_id, profile_id)):
            logger.error("Missing one of 'search', 'steam_id', 'profile_id'.")
            msg = "Either 'search', 'steam_id' or 'profile_id' required, please provide one."
            raise NightBotError(msg)

        logger.debug("Preparing parameters for opponent details query")
        query_params = {
            "game": game,
            "leaderboard_id": leaderboard_id,
            "language": language,
            "flag": flag,
            "search": search,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        return _get_request_text_response_decoded(
            session=self.session,
            url=self.RECENT_OPPONENT_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def match(
        self,
        game: str = "aoe2de",
        leaderboard_id: int = 3,
        language: str = "en",
        color: str = "true",
        flag: str = "true",
        search: str | None = None,
        steam_id: int | None = None,
        profile_id: int | None = None,
    ) -> str:
        """
        Request details about the current or last match. Either 'search', 'steam_id' or
        'profile_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            leaderboard_id (int): Leaderboard to extract the data for (Unranked=0,
                1v1 Deathmatch=1, Team Deathmatch=2, 1v1 Random Map=3, Team Random Map=4).
                Defaults to 3.
            language (str): language for the returned response ('en', 'de', 'el', 'es', 'es-MX',
                'fr', 'hi', 'it', 'ja', 'ko', 'ms', 'nl', 'pt', 'ru', 'tr', 'vi', 'zh', 'zh-TW').
                Defaults to 'en'.
            color (str): boolean to show player colors. Defaults to 'true'. Needs to be a string
                for now since requests transforms True boolean to 'True' and the API rejects that.
            flag (str): boolean to show the player flag. Defaults to 'true'. Needs to be a string
                for now since requests transforms True boolean to 'True' and the API rejects that.
            search (str): To perform the search for a specific player, from their name. Will
                return the highest rated player that matches the search.
            steam_id (int): To perform the search for a specific player, from their steamID64
                (ex: 76561199003184910).
            profile_id (int): To perform the search for a specific player, from their profile ID
                (ex: 459658).

        Raises:
            NightBotError: if the not one of 'search', 'steam_id' or 'profile_id' are provided.

        Returns:
            The text content of the response, as a decoded unicode string, with a quick sentence
            of information about the players in the match.
        """
        if not any((search, steam_id, profile_id)):
            logger.error("Missing one of 'search', 'steam_id', 'profile_id'.")
            msg = "Either 'search', 'steam_id' or 'profile_id' required, please provide one."
            raise NightBotError(msg)

        logger.debug("Preparing parameters for match details query")
        query_params = {
            "game": game,
            "leaderboard_id": leaderboard_id,
            "language": language,
            "color": color,
            "flag": flag,
            "search": search,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        return _get_request_text_response_decoded(
            session=self.session,
            url=self.CURRENT_MATCH_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def civs(
        self,
        game: str = "aoe2de",
        leaderboard_id: int = 3,
        language: str = "en",
        search: str | None = None,
        steam_id: int | None = None,
        profile_id: int | None = None,
    ) -> str:
        """
        Request civilisations from the current or last match. Either 'search', 'steam_id' or
        'profile_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            leaderboard_id (int): Leaderboard to extract the data for (Unranked=0,
                1v1 Deathmatch=1, Team Deathmatch=2, 1v1 Random Map=3, Team Random Map=4).
                Defaults to 3.
            language (str): language for the returned response ('en', 'de', 'el', 'es', 'es-MX',
                'fr', 'hi', 'it', 'ja', 'ko', 'ms', 'nl', 'pt', 'ru', 'tr', 'vi', 'zh', 'zh-TW').
                Defaults to 'en'.
            search (str): To perform the search for a specific player, from their name. Will
                return the highest rated player that matches the search.
            steam_id (int): To perform the search for a specific player, from their steamID64
                (ex: 76561199003184910).
            profile_id (int): To perform the search for a specific player, from their profile ID
                (ex: 459658).

        Raises:
            NightBotError: if the not one of 'search', 'steam_id' or 'profile_id' are provided.

        Returns:
            The text content of the response, as a decoded unicode string, with a quick sentence
            of information about the player's last opponent.
        """
        if not any((search, steam_id, profile_id)):
            logger.error("Missing one of 'search', 'steam_id', 'profile_id'.")
            msg = "Either 'search', 'steam_id' or 'profile_id' required, please provide one."
            raise NightBotError(msg)

        logger.debug("Preparing parameters for civilisations details query")
        query_params = {
            "game": game,
            "leaderboard_id": leaderboard_id,
            "language": language,
            "search": search,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        return _get_request_text_response_decoded(
            session=self.session,
            url=self.CURRENT_CIVS_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )

    def map(
        self,
        game: str = "aoe2de",
        leaderboard_id: int = 3,
        language: str = "en",
        search: str | None = None,
        steam_id: int | None = None,
        profile_id: int | None = None,
    ) -> str:
        """
        Request civilisations from the current or last match. Either 'search', 'steam_id' or
        'profile_id' required.

        Args:
            game (str): The game for which to extract the list of strings. Defaults to 'aoe2de'.
                Possibilities are 'aoe2hd' (Age of Empires 2: HD Edition) and 'aoe2de' (Age of
                Empires 2: Definitive Edition).
            leaderboard_id (int): Leaderboard to extract the data for (Unranked=0,
                1v1 Deathmatch=1, Team Deathmatch=2, 1v1 Random Map=3, Team Random Map=4).
                Defaults to 3.
            language (str): language for the returned response ('en', 'de', 'el', 'es', 'es-MX',
                'fr', 'hi', 'it', 'ja', 'ko', 'ms', 'nl', 'pt', 'ru', 'tr', 'vi', 'zh', 'zh-TW').
                Defaults to 'en'.
            search (str): To perform the search for a specific player, from their name. Will
                return the highest rated player that matches the search.
            steam_id (int): To perform the search for a specific player, from their steamID64
                (ex: 76561199003184910).
            profile_id (int): To perform the search for a specific player, from their profile ID
                (ex: 459658).

        Raises:
            NightBotError: if the not one of 'search', 'steam_id' or 'profile_id' are provided.

        Returns:
            The text content of the response, as a decoded unicode string, with a quick sentence
            of information about the player's last opponent.
        """
        if not any((search, steam_id, profile_id)):
            logger.error("Missing one of 'search', 'steam_id', 'profile_id'.")
            msg = "Either 'search', 'steam_id' or 'profile_id' required, please provide one."
            raise NightBotError(msg)

        logger.debug("Preparing parameters for civilisations details query")
        query_params = {
            "game": game,
            "leaderboard_id": leaderboard_id,
            "language": language,
            "search": search,
            "steam_id": steam_id,
            "profile_id": profile_id,
        }

        return _get_request_text_response_decoded(
            session=self.session,
            url=self.CURRENT_MAP_ENDPOINT,
            params=query_params,
            timeout=self.timeout,
        )


# ----- Helpers ----- #


def _get_request_text_response_decoded(
    session: requests.Session,
    url: str,
    params: dict[str, Any] | None = None,
    timeout: float | tuple[float, float] | None = None,
) -> str:
    """
    Helper function to handle a GET request to an endpoint and return the response JSON content
    as a dictionary.

    Args:
        session (requests.Session): Session object to use, for connection pooling and performance.
        url (str): API endpoint to send the request to.
        params (dict): A dictionary of parameters for the GET request.

    Raises:
        NightBotError: if the status code returned is not 200.

    Returns:
        The request's JSON response as a dictionary.
    """
    default_headers = {"content-type": "application/json;charset=UTF-8"}
    logger.debug(f"Sending GET request at '{url}'")
    logger.trace(f"Parameters are: {params!s}")

    response = session.get(url, params=params, headers=default_headers, timeout=timeout)
    if response.status_code != _OK_STATUS_CODE:
        logger.error(f"GET request at '{response.url}' returned a {response.status_code} status code")
        msg = f"Expected status code 200 - got {response.status_code} instead."
        raise NightBotError(msg)
    return response.text
