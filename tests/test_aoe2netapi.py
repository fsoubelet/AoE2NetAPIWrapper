import json
import pathlib

import pytest
import responses

from aoe2netwrapper.api import AoE2NetAPI, _get_request_response_json
from aoe2netwrapper.exceptions import Aoe2NetError
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
    client = AoE2NetAPI()

    def test_leaderboard_invalid_count_parameter(self, caplog):
        with pytest.raises(Aoe2NetError):
            self.client.leaderboard(count=11_000)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "'count' has to be 10000 or less, but 11000 was provided" in caplog.text

    def test_last_match_misses_required_param(self, caplog):
        with pytest.raises(Aoe2NetError):
            self.client.last_match()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'steam_id', 'profile_id'" in caplog.text

    def test_match_history_invalid_count_parameter(self, caplog):
        with pytest.raises(Aoe2NetError):
            self.client.match_history(count=1500, steam_id=76561199003184910)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "'count' has to be 1000 or less, but 1500 was provided" in caplog.text

    def test_match_history_misses_required_param(self, caplog):
        with pytest.raises(Aoe2NetError):
            self.client.match_history()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'steam_id', 'profile_id'" in caplog.text

    def test_rating_history_invalid_count_parameter(self, caplog):
        with pytest.raises(Aoe2NetError):
            self.client.rating_history(count=12_000, steam_id=76561199003184910)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "'count' has to be 10 000 or less, but 12000 was provided" in caplog.text

    def test_rating_history_misses_required_param(self, caplog):
        with pytest.raises(Aoe2NetError):
            self.client.rating_history()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'steam_id', 'profile_id'" in caplog.text

    def test_matches_invalid_count_parameter(self, caplog):
        with pytest.raises(Aoe2NetError):
            self.client.matches(count=2000)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "'count' has to be 1000 or less, but 2000 was provided." in caplog.text

    def test_match_misses_required_param(self, caplog):
        with pytest.raises(Aoe2NetError):
            self.client.match()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'uuid', 'match_id'" in caplog.text

    @responses.activate
    def test_raise_on_invalid_status_codes(self, caplog):
        responses.add(
            responses.GET,
            "https://local/test/endpoint",
            json={"error": "not found"},
            status=404,
        )

        with pytest.raises(Aoe2NetError):
            _ = _get_request_response_json(self.client.session, url="https://local/test/endpoint")

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "GET request at 'https://local/test/endpoint' returned a 404 status code" in caplog.text


class TestClientInstantiation:
    def test_timeout_attribute(self):
        client = AoE2NetAPI(timeout=1)
        assert client.timeout == 1

    def test_repr(self):
        client = AoE2NetAPI()
        assert str(client) == "Client for <https://aoe2.net/api>"
        assert repr(client) == "Client for <https://aoe2.net/api>"


class TestMethods:
    client = AoE2NetAPI()

    @responses.activate
    def test_strings_endpoint(self, strings_defaults_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/strings",
            json=strings_defaults_payload,
            status=200,
        )

        result = self.client.strings()
        assert isinstance(result, StringsResponse)
        assert result == StringsResponse(**strings_defaults_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {"game": "aoe2de"}
        assert responses.calls[0].request.url == "https://aoe2.net/api/strings?game=aoe2de"

    @responses.activate
    def test_leaderboard_endpoint_defaults(self, leaderboard_defaults_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/leaderboard",
            json=leaderboard_defaults_payload,
            status=200,
        )

        result = self.client.leaderboard()
        assert isinstance(result, LeaderBoardResponse)
        assert result == LeaderBoardResponse(**leaderboard_defaults_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "leaderboard_id": "3",
            "start": "1",
            "count": "10",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count=10"
        )

    @responses.activate
    def test_leaderboard_endpoint_with_search(self, leaderboard_search_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/leaderboard",
            json=leaderboard_search_payload,
            status=200,
        )

        assert isinstance(leaderboard_search_payload, dict)
        result = self.client.leaderboard(search="GL.TheViper")
        assert isinstance(result, LeaderBoardResponse)
        assert result == LeaderBoardResponse(**leaderboard_search_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "leaderboard_id": "3",
            "start": "1",
            "count": "10",
            "search": "GL.TheViper",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count=10&"
            "search=GL.TheViper"
        )

    @responses.activate
    def test_leaderboard_endpoint_with_steamid(self, leaderboard_steamid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/leaderboard",
            json=leaderboard_steamid_payload,
            status=200,
        )

        result = self.client.leaderboard(steam_id=76561199003184910)
        assert isinstance(result, LeaderBoardResponse)
        assert result == LeaderBoardResponse(**leaderboard_steamid_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "leaderboard_id": "3",
            "start": "1",
            "count": "10",
            "steam_id": "76561199003184910",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count=10"
            "&steam_id=76561199003184910"
        )

    @responses.activate
    def test_leaderboard_endpoint_with_profileid(self, leaderboard_profileid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/leaderboard",
            json=leaderboard_profileid_payload,
            status=200,
        )

        result = self.client.leaderboard(profile_id=459658)
        assert isinstance(result, LeaderBoardResponse)
        assert result == LeaderBoardResponse(**leaderboard_profileid_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "leaderboard_id": "3",
            "start": "1",
            "count": "10",
            "profile_id": "459658",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count=10&"
            "profile_id=459658"
        )

    @responses.activate
    def test_lobbies_endpoint(self, lobbies_defaults_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/lobbies",
            json=lobbies_defaults_payload,
            status=200,
        )

        result = self.client.lobbies()
        assert isinstance(result, list)
        assert isinstance(result[0], MatchLobby)
        assert result == [MatchLobby(**lobby) for lobby in lobbies_defaults_payload]

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {"game": "aoe2de"}
        assert responses.calls[0].request.url == "https://aoe2.net/api/lobbies?game=aoe2de"

    @responses.activate
    def test_last_match_endpoint_with_steamid(self, last_match_steamid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/player/lastmatch",
            json=last_match_steamid_payload,
            status=200,
        )

        result = self.client.last_match(steam_id=76561199003184910)
        assert isinstance(result, LastMatchResponse)
        assert result == LastMatchResponse(**last_match_steamid_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "steam_id": "76561199003184910",
        }
        assert (
            responses.calls[0].request.url == "https://aoe2.net/api/player/lastmatch?"
            "game=aoe2de&steam_id=76561199003184910"
        )

    @responses.activate
    def test_last_match_endpoint_with_profileid(self, last_match_profileid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/player/lastmatch",
            json=last_match_profileid_payload,
            status=200,
        )

        result = self.client.last_match(profile_id=459658)
        assert isinstance(result, LastMatchResponse)
        assert result == LastMatchResponse(**last_match_profileid_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "profile_id": "459658",
        }
        assert (
            responses.calls[0].request.url == "https://aoe2.net/api/player/lastmatch?"
            "game=aoe2de&profile_id=459658"
        )

    @responses.activate
    def test_match_history_endpoint_with_steamid(self, match_history_steamid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/player/matches",
            json=match_history_steamid_payload,
            status=200,
        )

        result = self.client.match_history(steam_id=76561199003184910)
        assert isinstance(result, list)
        assert isinstance(result[0], MatchLobby)
        assert result == [MatchLobby(**lobby) for lobby in match_history_steamid_payload]

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "start": "0",
            "count": "10",
            "steam_id": "76561199003184910",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/player/matches?game=aoe2de&start=0&count=10&"
            "steam_id=76561199003184910"
        )

    @responses.activate
    def test_match_history_endpoint_with_profileid(self, match_history_profileid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/player/matches",
            json=match_history_profileid_payload,
            status=200,
        )

        result = self.client.match_history(profile_id=459658)
        assert isinstance(result, list)
        assert isinstance(result[0], MatchLobby)
        assert result == [MatchLobby(**lobby) for lobby in match_history_profileid_payload]

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "start": "0",
            "count": "10",
            "profile_id": "459658",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/player/matches?game=aoe2de&start=0&count=10&profile_id=459658"
        )

    @responses.activate
    def test_rating_history_endpoint_with_steamid(self, rating_history_steamid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/player/ratinghistory",
            json=rating_history_steamid_payload,
            status=200,
        )

        result = self.client.rating_history(steam_id=76561199003184910)
        assert isinstance(result, list)
        assert isinstance(result[0], RatingTimePoint)
        assert result == [RatingTimePoint(**rating) for rating in rating_history_steamid_payload]

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "leaderboard_id": "3",
            "start": "0",
            "count": "20",
            "steam_id": "76561199003184910",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=3&start=0&"
            "count=20&steam_id=76561199003184910"
        )

    @responses.activate
    def test_rating_history_endpoint_with_profileid(self, rating_history_profileid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/player/ratinghistory",
            json=rating_history_profileid_payload,
            status=200,
        )

        result = self.client.rating_history(profile_id=459658)
        assert isinstance(result, list)
        assert isinstance(result[0], RatingTimePoint)
        assert result == [RatingTimePoint(**rating) for rating in rating_history_profileid_payload]

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "leaderboard_id": "3",
            "start": "0",
            "count": "20",
            "profile_id": "459658",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=3&start=0&"
            "count=20&profile_id=459658"
        )

    @responses.activate
    def test_matches_endpoint_defaults(self, matches_defaults_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/matches",
            json=matches_defaults_payload,
            status=200,
        )

        result = self.client.matches()
        assert isinstance(result, list)
        assert isinstance(result[0], MatchLobby)
        assert result == [MatchLobby(**lobby) for lobby in matches_defaults_payload]

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "count": "10",
        }
        assert responses.calls[0].request.url == "https://aoe2.net/api/matches?game=aoe2de&count=10"

    @responses.activate
    def test_matches_endpoint_with_since(self, matches_since_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/matches",
            json=matches_since_payload,
            status=200,
        )

        result = self.client.matches(since=1596775000)
        assert isinstance(result, list)
        assert isinstance(result[0], MatchLobby)
        assert result == [MatchLobby(**lobby) for lobby in matches_since_payload]

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "count": "10",
            "since": "1596775000",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/matches?game=aoe2de&count=10&since=1596775000"
        )

    @responses.activate
    def test_match_endpoint_with_uuid(self, match_uuid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/match",
            json=match_uuid_payload,
            status=200,
        )

        result = self.client.match(uuid="66ec2575-5ee4-d241-a1fc-d7ffeffb48b6")
        assert isinstance(result, MatchLobby)
        assert result == MatchLobby(**match_uuid_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "uuid": "66ec2575-5ee4-d241-a1fc-d7ffeffb48b6",
        }
        assert (
            responses.calls[0].request.url
            == "https://aoe2.net/api/match?game=aoe2de&uuid=66ec2575-5ee4-d241-a1fc-d7ffeffb48b6"
        )

    @responses.activate
    def test_match_endpoint_with_matchid(self, match_matchid_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/match",
            json=match_matchid_payload,
            status=200,
        )

        result = self.client.match(match_id=32435313)
        assert isinstance(result, MatchLobby)
        assert result == MatchLobby(**match_matchid_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {
            "game": "aoe2de",
            "match_id": "32435313",
        }
        assert responses.calls[0].request.url == "https://aoe2.net/api/match?game=aoe2de&match_id=32435313"

    @responses.activate
    def test_num_online_endpoint(self, num_online_defaults_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/stats/players",
            json=num_online_defaults_payload,
            status=200,
        )

        result = self.client.num_online()
        assert isinstance(result, NumOnlineResponse)
        assert result == NumOnlineResponse(**num_online_defaults_payload)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.params == {"game": "aoe2de"}
        assert responses.calls[0].request.url == "https://aoe2.net/api/stats/players?game=aoe2de"


# ----- Fixtures ----- #


@pytest.fixture
def strings_defaults_payload() -> dict:
    strings_response_file = INPUTS_DIR / "strings.json"
    with strings_response_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def leaderboard_defaults_payload() -> dict:
    leaderboard_defaults_file = INPUTS_DIR / "leaderboard_defaults.json"
    with leaderboard_defaults_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def leaderboard_search_payload() -> dict:
    leaderboard_search_file = INPUTS_DIR / "leaderboard_search.json"
    with leaderboard_search_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def leaderboard_steamid_payload() -> dict:
    leaderboard_steamid_file = INPUTS_DIR / "leaderboard_steamid.json"
    with leaderboard_steamid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def leaderboard_profileid_payload() -> dict:
    leaderboard_profileid_file = INPUTS_DIR / "leaderboard_profileid.json"
    with leaderboard_profileid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def lobbies_defaults_payload() -> dict:
    lobbies_defaults_file = INPUTS_DIR / "lobbies.json"
    with lobbies_defaults_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def last_match_steamid_payload() -> dict:
    last_match_steamid_file = INPUTS_DIR / "last_match_steamid.json"
    with last_match_steamid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def last_match_profileid_payload() -> dict:
    last_match_profileid_file = INPUTS_DIR / "last_match_profileid.json"
    with last_match_profileid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def match_history_steamid_payload() -> dict:
    match_history_steamid_file = INPUTS_DIR / "match_history_steamid.json"
    with match_history_steamid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def match_history_profileid_payload() -> dict:
    match_history_profileid_file = INPUTS_DIR / "match_history_profileid.json"
    with match_history_profileid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def rating_history_steamid_payload() -> dict:
    rating_history_steamid_file = INPUTS_DIR / "rating_history_steamid.json"
    with rating_history_steamid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def rating_history_profileid_payload() -> dict:
    rating_history_profileid_file = INPUTS_DIR / "rating_history_profileid.json"
    with rating_history_profileid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def matches_defaults_payload() -> dict:
    matches_defaults_file = INPUTS_DIR / "matches_defaults.json"
    with matches_defaults_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def matches_since_payload() -> dict:
    matches_since_file = INPUTS_DIR / "matches_since.json"
    with matches_since_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def match_uuid_payload() -> dict:
    match_uuid_file = INPUTS_DIR / "match_uuid.json"
    with match_uuid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def match_matchid_payload() -> dict:
    match_match_id_file = INPUTS_DIR / "match_matchid.json"
    with match_match_id_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture
def num_online_defaults_payload() -> dict:
    num_online_defaults_file = INPUTS_DIR / "num_online.json"
    with num_online_defaults_file.open("r") as fileobj:
        return json.load(fileobj)
