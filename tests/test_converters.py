import json
import pathlib

import pandas as pd
import pytest
import responses

from aoe2netwrapper import AoE2NetAPI
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
    client = AoE2NetAPI()

    @responses.activate
    def test_strings(self, strings_defaults_payload, strings_converted):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/strings",
            json=strings_defaults_payload,
            status=200,
        )

        result = self.client.strings()
        dframe = Convert.strings(result)

        assert isinstance(dframe, pd.DataFrame)
        assert dframe.size == 1331
        assert dframe.shape == (121, 11)
        pd.testing.assert_frame_equal(dframe, strings_converted)

    @responses.activate
    def test_leaderboard(self, leaderboard_defaults_payload, leaderboard_converted):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/leaderboard",
            json=leaderboard_defaults_payload,
            status=200,
        )

        result = self.client.leaderboard()
        dframe = Convert.leaderboard(result)

        assert isinstance(dframe, pd.DataFrame)
        assert dframe.size == 230
        assert dframe.shape == (10, 23)
        pd.testing.assert_frame_equal(dframe, leaderboard_converted)

    @responses.activate
    def test_lobbies(self, lobbies_defaults_payload, lobbies_converted):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/lobbies",
            json=lobbies_defaults_payload,
            status=200,
        )

        result = self.client.lobbies()
        dframe = Convert.lobbies(result)

        assert isinstance(dframe, pd.DataFrame)
        assert dframe.size == 34086
        assert dframe.shape == (598, 57)
        pd.testing.assert_frame_equal(dframe, lobbies_converted)

    @responses.activate
    def test_last_match_endpoint_with_steamid(self, last_match_steamid_payload, last_match_converted):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/player/lastmatch",
            json=last_match_steamid_payload,
            status=200,
        )

        result = self.client.last_match(steam_id=76561199003184910)
        dframe = Convert.last_match(result)

        assert isinstance(dframe, pd.DataFrame)
        assert dframe.size == 45
        assert dframe.shape == (1, 45)
        pd.testing.assert_frame_equal(dframe, last_match_converted)

    @responses.activate
    def test_match_history(self, match_history_steamid_payload, match_history_converted):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/player/matches",
            json=match_history_steamid_payload,
            status=200,
        )

        result = self.client.match_history(steam_id=76561199003184910)
        dframe = Convert.match_history(result)

        assert isinstance(dframe, pd.DataFrame)
        assert dframe.size == 1482
        assert dframe.shape == (26, 57)
        pd.testing.assert_frame_equal(dframe, match_history_converted)

    @responses.activate
    def test_rating_history(self, rating_history_profileid_payload, rating_history_converted):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/player/ratinghistory",
            json=rating_history_profileid_payload,
            status=200,
        )

        result = self.client.rating_history(profile_id=459658)
        dframe = Convert.rating_history(result)

        assert isinstance(dframe, pd.DataFrame)
        assert dframe.size == 600
        assert dframe.shape == (100, 6)
        pd.testing.assert_frame_equal(dframe, rating_history_converted)

    @responses.activate
    def test_matches(self, matches_defaults_payload, matches_converted):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/matches",
            json=matches_defaults_payload,
            status=200,
        )

        result = self.client.matches()
        dframe = Convert.matches(result)

        assert isinstance(dframe, pd.DataFrame)
        assert dframe.size == 2622
        assert dframe.shape == (46, 57)
        pd.testing.assert_frame_equal(dframe, matches_converted)

    @responses.activate
    def test_match(self, match_uuid_payload, match_converted):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/match",
            json=match_uuid_payload,
            status=200,
        )

        result = self.client.match(uuid="66ec2575-5ee4-d241-a1fc-d7ffeffb48b6")
        dframe = Convert.match(result)

        assert isinstance(dframe, pd.DataFrame)
        assert dframe.size == 456
        assert dframe.shape == (8, 57)
        pd.testing.assert_frame_equal(dframe, match_converted)

    @responses.activate
    def test_num_online(self, num_online_defaults_payload, num_online_converted):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/stats/players",
            json=num_online_defaults_payload,
            status=200,
        )

        result = self.client.num_online()
        dframe = Convert.num_online(result)

        assert isinstance(dframe, pd.DataFrame)
        assert dframe.size == 5752
        assert dframe.shape == (719, 8)
        pd.testing.assert_frame_equal(dframe, num_online_converted)


# ----- Fixtures ----- #


@pytest.fixture()
def strings_defaults_payload() -> dict:
    strings_response_file = INPUTS_DIR / "strings.json"
    with strings_response_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def strings_converted() -> pd.DataFrame:
    strings_converted_file = INPUTS_DIR / "convert_strings.pkl"
    return pd.read_pickle(strings_converted_file)


@pytest.fixture()
def leaderboard_defaults_payload() -> dict:
    leaderboard_defaults_file = INPUTS_DIR / "leaderboard_defaults.json"
    with leaderboard_defaults_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def leaderboard_converted() -> pd.DataFrame:
    leaderboard_converted_file = INPUTS_DIR / "convert_leaderboard.pkl"
    return pd.read_pickle(leaderboard_converted_file)


@pytest.fixture()
def lobbies_defaults_payload() -> dict:
    lobbies_defaults_file = INPUTS_DIR / "lobbies.json"
    with lobbies_defaults_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def lobbies_converted() -> pd.DataFrame:
    lobbies_converted_file = INPUTS_DIR / "convert_lobbies.pkl"
    return pd.read_pickle(lobbies_converted_file)


@pytest.fixture()
def last_match_steamid_payload() -> dict:
    last_match_steamid_file = INPUTS_DIR / "last_match_steamid.json"
    with last_match_steamid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def last_match_converted() -> pd.DataFrame:
    last_match_converted_file = INPUTS_DIR / "convert_last_match.pkl"
    return pd.read_pickle(last_match_converted_file)


@pytest.fixture()
def match_history_steamid_payload() -> dict:
    match_history_steamid_file = INPUTS_DIR / "match_history_steamid.json"
    with match_history_steamid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def match_history_converted() -> pd.DataFrame:
    match_history_converted_file = INPUTS_DIR / "convert_match_history.pkl"
    return pd.read_pickle(match_history_converted_file)


@pytest.fixture()
def rating_history_profileid_payload() -> dict:
    rating_history_profileid_file = INPUTS_DIR / "rating_history_profileid.json"
    with rating_history_profileid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def rating_history_converted() -> pd.DataFrame:
    rating_history_converted_file = INPUTS_DIR / "convert_rating_history.pkl"
    return pd.read_pickle(rating_history_converted_file)


@pytest.fixture()
def matches_defaults_payload() -> dict:
    matches_defaults_file = INPUTS_DIR / "matches_defaults.json"
    with matches_defaults_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def matches_converted() -> pd.DataFrame:
    matches_converted_file = INPUTS_DIR / "convert_matches.pkl"
    return pd.read_pickle(matches_converted_file)


@pytest.fixture()
def match_uuid_payload() -> dict:
    match_uuid_file = INPUTS_DIR / "match_uuid.json"
    with match_uuid_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def match_converted() -> pd.DataFrame:
    match_converted_file = INPUTS_DIR / "convert_match.pkl"
    return pd.read_pickle(match_converted_file)


@pytest.fixture()
def num_online_defaults_payload() -> dict:
    num_online_defaults_file = INPUTS_DIR / "num_online.json"
    with num_online_defaults_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload


@pytest.fixture()
def num_online_converted() -> pd.DataFrame:
    num_online_converted_file = INPUTS_DIR / "convert_num_online.pkl"
    return pd.read_pickle(num_online_converted_file)
