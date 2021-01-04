import json
import pathlib

import pytest
import responses

from aoe2netwrapper.api import AoE2NetAPI, _get_request_response_json
from aoe2netwrapper.exceptions import Aoe2NetException

CURRENT_DIR = pathlib.Path(__file__).parent
INPUTS_DIR = CURRENT_DIR / "inputs"


class TestExceptions:
    client = AoE2NetAPI()

    def test_leaderboard_invalid_count_parameter(self, caplog):
        with pytest.raises(Aoe2NetException):
            self.client.leaderboard(count=11_000)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "'count' has to be 10000 or less, but 11000 was provided" in caplog.text

    def test_last_match_misses_required_param(self, caplog):
        with pytest.raises(Aoe2NetException):
            self.client.last_match()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'steam_id', 'profile_id'" in caplog.text

    def test_match_history_invalid_count_parameter(self, caplog):
        with pytest.raises(Aoe2NetException):
            self.client.match_history(count=1500, steam_id=76561199003184910)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "'count' has to be 1000 or less, but 1500 was provided" in caplog.text

    def test_match_history_misses_required_param(self, caplog):
        with pytest.raises(Aoe2NetException):
            self.client.match_history()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'steam_id', 'profile_id'" in caplog.text

    def test_rating_history_invalid_count_parameter(self, caplog):
        with pytest.raises(Aoe2NetException):
            self.client.rating_history(count=12_000, steam_id=76561199003184910)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "'count' has to be 10 000 or less, but 12000 was provided" in caplog.text

    def test_rating_history_misses_required_param(self, caplog):
        with pytest.raises(Aoe2NetException):
            self.client.rating_history()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'steam_id', 'profile_id'" in caplog.text

    def test_matches_invalid_count_parameter(self, caplog):
        with pytest.raises(Aoe2NetException):
            self.client.match_history(count=2000)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "'count' has to be 1000 or less, but 2000 was provided." in caplog.text

    def test_match_misses_required_param(self, caplog):
        with pytest.raises(Aoe2NetException):
            self.client.match()

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Missing one of 'uuid', 'match_id'" in caplog.text

    @responses.activate
    def test_raise_on_invalid_status_codes(self, caplog):
        responses.add(
            responses.GET, "https://local/test/endpoint", json={"error": "not found"}, status=404
        )

        with pytest.raises(Aoe2NetException):
            result = _get_request_response_json(
                self.client.session, url="https://local/test/endpoint"
            )

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert (
                "GET request at 'https://local/test/endpoint' returned a 404 status code"
                in caplog.text
            )


class TestMethods:
    client = AoE2NetAPI()

    @responses.activate
    def test_strings_endpoint(self, strings_endpoint_json_payload):
        responses.add(
            responses.GET,
            "https://aoe2.net/api/strings",
            json=strings_endpoint_json_payload,
            status=200,
        )

        result = self.client.strings()
        assert result == strings_endpoint_json_payload

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == "https://aoe2.net/api/strings?game=aoe2de"


# ----- Fixtures ----- #


@pytest.fixture()
def strings_endpoint_json_payload() -> dict:
    strings_response_file = INPUTS_DIR / "strings_response.json"
    with strings_response_file.open("r") as fileobj:
        payload = json.load(fileobj)
    return payload
