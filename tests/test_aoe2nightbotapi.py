import pathlib

import pytest
import responses

from aoe2netwrapper.exceptions import NightBotException
from aoe2netwrapper.nightbot import AoE2NightbotAPI, _get_request_text_response_decoded

CURRENT_DIR = pathlib.Path(__file__).parent
INPUTS_DIR = CURRENT_DIR / "inputs"

# ----- Expected Responses for Callbacks ----- #

RANKS = {
    "viper_flag": "🇳🇴 GL.TheViper (2501) Rank #1, has played 762 games with a 69% winrate, "
    "-1 streak, and 2 drops",
    "viper": "GL.TheViper (2501) Rank #1, has played 762 games with a 69% winrate, " "-1 streak, and 2 drops",
    "hoang_flag": "🇻🇳 DS_HOANG |AOEBuilds.com (2345) Rank #27, has played 2,975 games with a "
    "58% winrate, +7 streak, and 41 drops",
    "hoang": "DS_HOANG |AOEBuilds.com (2345) Rank #27, has played 2,975 games with a "
    "58% winrate, +7 streak, and 41 drops",
}

OPPONENTS = {
    "viper_flag": "Player not found",
    "viper": "Player not found",
    "hoang_flag": "Player not found",
    "hoang": "Player not found",
}

MATCH = {
    "viper_flag": "Player not found",
    "viper": "Player not found",
    "hoang_flag": "Player not found",
    "hoang": "Player not found",
}

CIVS = {
    "viper": "Player not found",
    "hoang": "Player not found",
}

MAP = {
    "viper": "Player not found",
    "hoang": "Player not found",
}


# ----- Test Classes ----- #


class TestExceptions:
    client = AoE2NightbotAPI()

    def test_rank_misses_required_param(self, caplog):
        with pytest.raises(NightBotException):
            self.client.rank()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'search', 'steam_id', 'profile_id'" in caplog.text

    def test_opponent_misses_required_param(self, caplog):
        with pytest.raises(NightBotException):
            self.client.opponent()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'search', 'steam_id', 'profile_id'" in caplog.text

    def test_match_misses_required_param(self, caplog):
        with pytest.raises(NightBotException):
            self.client.match()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'search', 'steam_id', 'profile_id'" in caplog.text

    def test_civs_misses_required_param(self, caplog):
        with pytest.raises(NightBotException):
            self.client.civs()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'search', 'steam_id', 'profile_id'" in caplog.text

    def test_ma_misses_required_param(self, caplog):
        with pytest.raises(NightBotException):
            self.client.map()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'search', 'steam_id', 'profile_id'" in caplog.text

    @responses.activate
    def test_raise_on_invalid_status_codes(self, caplog):
        responses.add(
            responses.GET,
            "https://local/test/endpoint",
            json={"error": "not found"},
            status=404,
        )

        with pytest.raises(NightBotException):
            _ = _get_request_text_response_decoded(self.client.session, url="https://local/test/endpoint")

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "GET request at 'https://local/test/endpoint' returned a 404 status code" in caplog.text


class TestClientInstantiation:
    def test_timeout_attribute(self):
        client = AoE2NightbotAPI(timeout=1)
        assert client.timeout == 1

    def test_repr(self):
        client = AoE2NightbotAPI()
        assert str(client) == "Client for <https://aoe2.net/api/nightbot>"
        assert repr(client) == "Client for <https://aoe2.net/api/nightbot>"


class TestMethods:
    client = AoE2NightbotAPI()

    @responses.activate
    @pytest.mark.parametrize(
        "flag, search, steam_id, profile_id, returned_text",
        [
            ("true", "GL.TheViper", None, None, RANKS["viper_flag"]),
            ("false", "GL.TheViper", None, None, RANKS["viper"]),
            ("true", None, 76561199003184910, None, RANKS["hoang_flag"]),
            ("false", None, None, 459658, RANKS["hoang"]),
        ],
    )
    def test_rank_endpoint(self, flag, search, steam_id, profile_id, returned_text):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/nightbot/rank",
            body=returned_text,
            status=200,
        )

        result = self.client.rank(
            flag=flag,
            search=search,
            steam_id=steam_id,
            profile_id=profile_id,
        )
        assert result == returned_text
        assert len(responses.calls) == 1

    @responses.activate
    @pytest.mark.parametrize(
        "flag, search, steam_id, profile_id, returned_text",
        [
            ("true", "GL.TheViper", None, None, OPPONENTS["viper_flag"]),
            ("false", "GL.TheViper", None, None, OPPONENTS["viper"]),
            ("true", None, 76561199003184910, None, OPPONENTS["hoang_flag"]),
            ("false", None, None, 459658, OPPONENTS["hoang"]),
        ],
    )
    def test_opponent_endpoint(self, flag, search, steam_id, profile_id, returned_text):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/nightbot/opponent",
            body=returned_text,
            status=200,
        )

        result = self.client.opponent(
            flag=flag,
            search=search,
            steam_id=steam_id,
            profile_id=profile_id,
        )
        assert result == returned_text
        assert len(responses.calls) == 1

    @responses.activate
    @pytest.mark.parametrize(
        "flag, search, steam_id, profile_id, returned_text",
        [
            ("true", "GL.TheViper", None, None, MATCH["viper_flag"]),
            ("false", "GL.TheViper", None, None, MATCH["viper"]),
            ("true", None, 76561199003184910, None, MATCH["hoang_flag"]),
            ("false", None, None, 459658, MATCH["hoang"]),
        ],
    )
    def test_match_endpoint(self, flag, search, steam_id, profile_id, returned_text):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/nightbot/match",
            body=returned_text,
            status=200,
        )

        result = self.client.match(
            flag=flag,
            search=search,
            steam_id=steam_id,
            profile_id=profile_id,
        )
        assert result == returned_text
        assert len(responses.calls) == 1

    @responses.activate
    @pytest.mark.parametrize(
        "search, steam_id, profile_id, returned_text",
        [
            ("GL.TheViper", None, None, CIVS["viper"]),
            (None, 76561199003184910, None, CIVS["hoang"]),
            (None, None, 459658, CIVS["hoang"]),
        ],
    )
    def test_civs_endpoint(self, search, steam_id, profile_id, returned_text):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/nightbot/civs",
            body=returned_text,
            status=200,
        )

        result = self.client.civs(
            search=search,
            steam_id=steam_id,
            profile_id=profile_id,
        )
        assert result == returned_text
        assert len(responses.calls) == 1

    @responses.activate
    @pytest.mark.parametrize(
        "search, steam_id, profile_id, returned_text",
        [
            ("GL.TheViper", None, None, MAP["viper"]),
            (None, 76561199003184910, None, MAP["hoang"]),
            (None, None, 459658, MAP["hoang"]),
        ],
    )
    def test_map_endpoint(self, search, steam_id, profile_id, returned_text):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/nightbot/map",
            body=returned_text,
            status=200,
        )

        result = self.client.map(
            search=search,
            steam_id=steam_id,
            profile_id=profile_id,
        )
        assert result == returned_text
        assert len(responses.calls) == 1
