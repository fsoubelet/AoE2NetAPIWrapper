"""
Client to query the API at https://aoe2.net/#nightbot.
"""

import requests


class AoE2NightbotAPI:
    """
    The 'AoE2NightbotAPI' class is a client that encompasses the https://aoe2.net/#nightbot
    Nightbot API functions, which only return their requested data as plain text.
    """

    NIGHTBOT_BASE_URL: str = "https://aoe2.net/api/nightbot"
    RANK_DETAILS_ENDPOINT = NIGHTBOT_BASE_URL + "/rank"
    RECENT_OPPONENT_ENDPOINT = NIGHTBOT_BASE_URL + "/opponent"
    CURRENT_MATCH_ENDPOINT = NIGHTBOT_BASE_URL + "/match"
    CURRENT_CIVS_ENDPOINT = NIGHTBOT_BASE_URL + "/civs"
    CURRENT_MAP_ENDPOINT = NIGHTBOT_BASE_URL + "/map"

    def __init__(self):
        """Creating a Session for connection pooling since we're always querying the same host."""
        self.client = requests.Session()

    def __repr__(self) -> str:
        return f"Client for <{self.NIGHTBOT_BASE_URL}>"
