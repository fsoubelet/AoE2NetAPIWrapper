import json
import pathlib

import pytest
import responses

from aoe2netwrapper.api import AoE2NetAPI, _get_request_response_json
from aoe2netwrapper.exceptions import Aoe2NetException
from aoe2netwrapper.models import (
    LastMatchResponse,
    LeaderBoardResponse,
    MatchLobby,
    NumOnlineResponse,
    RatingTimePoint,
    StringsResponse,
)

CURRENT_DIR = pathlib.Path(__file__).parent
INPUTS_DIR = CURRENT_DIR / "inputs"


class TestExceptions:
    pass


class TestConvert:
    pass


# ----- Fixtures ----- #


@pytest.fixture()
def strings_defaults_payload() -> dict:
    strings_response_file = INPUTS_DIR / "strings.json"
    with strings_response_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def leaderboard_defaults_payload() -> dict:
    leaderboard_defaults_file = INPUTS_DIR / "leaderboard_defaults.json"
    with leaderboard_defaults_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def leaderboard_search_payload() -> dict:
    leaderboard_search_file = INPUTS_DIR / "leaderboard_search.json"
    with leaderboard_search_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def leaderboard_steamid_payload() -> dict:
    leaderboard_steamid_file = INPUTS_DIR / "leaderboard_steamid.json"
    with leaderboard_steamid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def leaderboard_profileid_payload() -> dict:
    leaderboard_profileid_file = INPUTS_DIR / "leaderboard_profileid.json"
    with leaderboard_profileid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def lobbies_defaults_payload() -> dict:
    lobbies_defaults_file = INPUTS_DIR / "lobbies.json"
    with lobbies_defaults_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def last_match_steamid_payload() -> dict:
    last_match_steamid_file = INPUTS_DIR / "last_match_steamid.json"
    with last_match_steamid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def last_match_profileid_payload() -> dict:
    last_match_profileid_file = INPUTS_DIR / "last_match_profileid.json"
    with last_match_profileid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def match_history_steamid_payload() -> dict:
    match_history_steamid_file = INPUTS_DIR / "match_history_steamid.json"
    with match_history_steamid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def match_history_profileid_payload() -> dict:
    match_history_profileid_file = INPUTS_DIR / "match_history_profileid.json"
    with match_history_profileid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def rating_history_steamid_payload() -> dict:
    rating_history_steamid_file = INPUTS_DIR / "rating_history_steamid.json"
    with rating_history_steamid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def rating_history_profileid_payload() -> dict:
    rating_history_profileid_file = INPUTS_DIR / "rating_history_profileid.json"
    with rating_history_profileid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def matches_defaults_payload() -> dict:
    matches_defaults_file = INPUTS_DIR / "matches_defaults.json"
    with matches_defaults_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def matches_since_payload() -> dict:
    matches_since_file = INPUTS_DIR / "matches_since.json"
    with matches_since_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def match_uuid_payload() -> dict:
    match_uuid_file = INPUTS_DIR / "match_uuid.json"
    with match_uuid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def match_matchid_payload() -> dict:
    match_match_id_file = INPUTS_DIR / "match_matchid.json"
    with match_match_id_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def num_online_defaults_payload() -> dict:
    num_online_defaults_file = INPUTS_DIR / "num_online.json"
    with num_online_defaults_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload
