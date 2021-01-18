import json
import pathlib

import pytest

from aoe2netwrapper.converters import Convert

CURRENT_DIR = pathlib.Path(__file__).parent
INPUTS_DIR = CURRENT_DIR / "inputs"


class TestExceptions:
    def test_strings_fail_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = Convert.strings(10)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'StringsResponse'" in caplog.text

    def test_leaderboard_fail_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = Convert.leaderboard("not a LeaderBoardResponse")

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'LeaderBoardResponse'" in caplog.text

    def test_lobbies_fail_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = Convert.lobbies(None)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'List[MatchLobby]'" in caplog.text

    def test_last_match_fail_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = Convert.last_match(json)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'LastMatchResponse'" in caplog.text

    def test_match_history_fail_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = Convert.match_history(True)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'List[MatchLobby]'" in caplog.text

    def test_rating_history_fail_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = Convert.rating_history(4.5)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'List[RatingTimePoint]'" in caplog.text

    def test_matches_fail_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = Convert.matches(TypeError)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'List[MatchLobby]'" in caplog.text

    def test_match_fail_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = Convert.match(CURRENT_DIR)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'MatchLobby'" in caplog.text

    def test_num_online_fail_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = Convert.num_online(self)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'NumOnlineResponse'" in caplog.text


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
