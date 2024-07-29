import pandas as pd
import pytest
import responses

from aoe2netwrapper import AoE2NetAPI
from aoe2netwrapper.converters import Convert, _unfold_match_lobby_to_dataframe


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

    # def test_lobbies_fail_on_wrong_type(self, caplog):
    #     # No longer tested as endpoint and method have been removed
    #     with pytest.raises(TypeError):
    #         _ = Convert.lobbies(None)

    #     for record in caplog.records:
    #         assert record.levelname == "ERROR"
    #         assert "Tried to use method with a parameter of type != 'List[MatchLobby]'" in caplog.text

    # def test_last_match_fail_on_wrong_type(self, caplog):
    #     # No longer tested as endpoint and method have been removed
    #     with pytest.raises(TypeError):
    #         _ = Convert.last_match({"a": 1})

    #     for record in caplog.records:
    #         assert record.levelname == "ERROR"
    #         assert "Tried to use method with a parameter of type != 'LastMatchResponse'" in caplog.text

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

    # def test_matches_fail_on_wrong_type(self, caplog):
    #     # No longer tested as endpoint and method have been removed
    #     with pytest.raises(TypeError):
    #         _ = Convert.matches(TypeError)

    #     for record in caplog.records:
    #         assert record.levelname == "ERROR"
    #         assert "Tried to use method with a parameter of type != 'List[MatchLobby]'" in caplog.text

    # def test_match_fail_on_wrong_type(self, caplog):
    #     # No longer tested as endpoint and method have been removed
    #     with pytest.raises(TypeError):
    #         _ = Convert.match({"a": 1})

    #     for record in caplog.records:
    #         assert record.levelname == "ERROR"
    #         assert "Tried to use method with a parameter of type != 'MatchLobby'" in caplog.text

    # def test_num_online_fail_on_wrong_type(self, caplog):
    #     # No longer tested as endpoint and method have been removed
    #     with pytest.raises(TypeError):
    #         _ = Convert.num_online(self)

    #     for record in caplog.records:
    #         assert record.levelname == "ERROR"
    #         assert "Tried to use method with a parameter of type != 'NumOnlineResponse'" in caplog.text

    def test_match_lobby_unfolding_raises_on_wrong_type(self, caplog):
        with pytest.raises(TypeError):
            _ = _unfold_match_lobby_to_dataframe(10)

        for record in caplog.records:
            assert record.levelname == "ERROR"
            assert "Tried to use method with a parameter of type != 'MatchLobby'" in caplog.text

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

    # @responses.activate
    # def test_lobbies(self, lobbies_defaults_payload, lobbies_converted):
    #     # No longer tested as endpoint and method have been removed
    #     responses.add(
    #         responses.GET,
    #         "https://aoe2.net/api/lobbies",
    #         json=lobbies_defaults_payload,
    #         status=200,
    #     )

    #     result = self.client.lobbies()
    #     dframe = Convert.lobbies(result)

    #     assert isinstance(dframe, pd.DataFrame)
    #     assert dframe.size == 34086
    #     assert dframe.shape == (598, 57)
    #     pd.testing.assert_frame_equal(dframe, lobbies_converted)

    # @responses.activate
    # def test_last_match_endpoint_with_steamid(self, last_match_steamid_payload, last_match_converted):
    #     # No longer tested as endpoint and method have been removed
    #     responses.add(
    #         responses.GET,
    #         "https://aoe2.net/api/player/lastmatch",
    #         json=last_match_steamid_payload,
    #         status=200,
    #     )

    #     result = self.client.last_match(steam_id=76561199003184910)
    #     dframe = Convert.last_match(result)

    #     assert isinstance(dframe, pd.DataFrame)
    #     assert dframe.size == 45
    #     assert dframe.shape == (1, 45)
    #     pd.testing.assert_frame_equal(dframe, last_match_converted)

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

    # @responses.activate
    # def test_matches(self, matches_defaults_payload, matches_converted):
    #     # No longer tested as endpoint and method have been removed
    #     responses.add(
    #         responses.GET,
    #         "https://aoe2.net/api/matches",
    #         json=matches_defaults_payload,
    #         status=200,
    #     )

    #     result = self.client.matches()
    #     dframe = Convert.matches(result)

    #     assert isinstance(dframe, pd.DataFrame)
    #     assert dframe.size == 2622
    #     assert dframe.shape == (46, 57)
    #     pd.testing.assert_frame_equal(dframe, matches_converted)

    # @responses.activate
    # def test_match(self, match_uuid_payload, match_converted):
    #     # No longer tested as endpoint and method have been removed
    #     responses.add(
    #         responses.GET,
    #         "https://aoe2.net/api/match",
    #         json=match_uuid_payload,
    #         status=200,
    #     )

    #     result = self.client.match(uuid="66ec2575-5ee4-d241-a1fc-d7ffeffb48b6")
    #     dframe = Convert.match(result)

    #     assert isinstance(dframe, pd.DataFrame)
    #     assert dframe.size == 456
    #     assert dframe.shape == (8, 57)
    #     pd.testing.assert_frame_equal(dframe, match_converted)

    # @responses.activate
    # def test_num_online(self, num_online_defaults_payload, num_online_converted):
    #     # No longer tested as endpoint and method have been removed
    #     responses.add(
    #         responses.GET,
    #         "https://aoe2.net/api/stats/players",
    #         json=num_online_defaults_payload,
    #         status=200,
    #     )

    #     result = self.client.num_online()
    #     dframe = Convert.num_online(result)

    #     assert isinstance(dframe, pd.DataFrame)
    #     assert dframe.size == 5752
    #     assert dframe.shape == (719, 8)
    #     pd.testing.assert_frame_equal(dframe, num_online_converted)
