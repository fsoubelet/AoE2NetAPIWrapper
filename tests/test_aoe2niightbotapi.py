import pathlib

import pytest
import responses

from aoe2netwrapper.exceptions import NightBotException
from aoe2netwrapper.nightbot import AoE2NightbotAPI, _get_request_text_response_decoded

CURRENT_DIR = pathlib.Path(__file__).parent
INPUTS_DIR = CURRENT_DIR / "inputs"


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
            _ = _get_request_text_response_decoded(
                self.client.session, url="https://local/test/endpoint"
            )

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert (
                "GET request at 'https://local/test/endpoint' returned a 404 status code"
                in caplog.text
            )


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
    pass
