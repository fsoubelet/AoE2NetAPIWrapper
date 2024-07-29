import json
import pathlib

import pandas as pd
import pytest

CURRENT_DIR = pathlib.Path(__file__).parent
INPUTS_DIR = CURRENT_DIR / "inputs"


# ----- Fixtures for AoE2NetAPI ----- #


@pytest.fixture(scope="session")
def strings_defaults_payload() -> dict:
    strings_response_file = INPUTS_DIR / "strings.json"
    with strings_response_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def leaderboard_defaults_payload() -> dict:
    leaderboard_defaults_file = INPUTS_DIR / "leaderboard_defaults.json"
    with leaderboard_defaults_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def leaderboard_search_payload() -> dict:
    leaderboard_search_file = INPUTS_DIR / "leaderboard_search.json"
    with leaderboard_search_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def leaderboard_steamid_payload() -> dict:
    leaderboard_steamid_file = INPUTS_DIR / "leaderboard_steamid.json"
    with leaderboard_steamid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def leaderboard_profileid_payload() -> dict:
    leaderboard_profileid_file = INPUTS_DIR / "leaderboard_profileid.json"
    with leaderboard_profileid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def lobbies_defaults_payload() -> dict:
    lobbies_defaults_file = INPUTS_DIR / "lobbies.json"
    with lobbies_defaults_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def last_match_steamid_payload() -> dict:
    last_match_steamid_file = INPUTS_DIR / "last_match_steamid.json"
    with last_match_steamid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def last_match_profileid_payload() -> dict:
    last_match_profileid_file = INPUTS_DIR / "last_match_profileid.json"
    with last_match_profileid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def match_history_steamid_payload() -> dict:
    match_history_steamid_file = INPUTS_DIR / "match_history_steamid.json"
    with match_history_steamid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def match_history_profileid_payload() -> dict:
    match_history_profileid_file = INPUTS_DIR / "match_history_profileid.json"
    with match_history_profileid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def rating_history_steamid_payload() -> dict:
    rating_history_steamid_file = INPUTS_DIR / "rating_history_steamid.json"
    with rating_history_steamid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def rating_history_profileid_payload() -> dict:
    rating_history_profileid_file = INPUTS_DIR / "rating_history_profileid.json"
    with rating_history_profileid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def matches_defaults_payload() -> dict:
    matches_defaults_file = INPUTS_DIR / "matches_defaults.json"
    with matches_defaults_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def matches_since_payload() -> dict:
    matches_since_file = INPUTS_DIR / "matches_since.json"
    with matches_since_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def match_uuid_payload() -> dict:
    match_uuid_file = INPUTS_DIR / "match_uuid.json"
    with match_uuid_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def match_matchid_payload() -> dict:
    match_match_id_file = INPUTS_DIR / "match_matchid.json"
    with match_match_id_file.open("r") as fileobj:
        return json.load(fileobj)


@pytest.fixture(scope="session")
def num_online_defaults_payload() -> dict:
    num_online_defaults_file = INPUTS_DIR / "num_online.json"
    with num_online_defaults_file.open("r") as fileobj:
        return json.load(fileobj)


# ----- Fixtures for Converters ----- #


@pytest.fixture(scope="session")
def strings_converted() -> pd.DataFrame:
    strings_converted_file = INPUTS_DIR / "convert_strings.pkl"
    return pd.read_pickle(strings_converted_file)


@pytest.fixture(scope="session")
def leaderboard_converted() -> pd.DataFrame:
    leaderboard_converted_file = INPUTS_DIR / "convert_leaderboard.pkl"
    return pd.read_pickle(leaderboard_converted_file)


@pytest.fixture(scope="session")
def lobbies_converted() -> pd.DataFrame:
    lobbies_converted_file = INPUTS_DIR / "convert_lobbies.pkl"
    return pd.read_pickle(lobbies_converted_file)


@pytest.fixture(scope="session")
def last_match_converted() -> pd.DataFrame:
    last_match_converted_file = INPUTS_DIR / "convert_last_match.pkl"
    return pd.read_pickle(last_match_converted_file)


@pytest.fixture(scope="session")
def match_history_converted() -> pd.DataFrame:
    match_history_converted_file = INPUTS_DIR / "convert_match_history.pkl"
    return pd.read_pickle(match_history_converted_file)


@pytest.fixture(scope="session")
def rating_history_converted() -> pd.DataFrame:
    rating_history_converted_file = INPUTS_DIR / "convert_rating_history.pkl"
    return pd.read_pickle(rating_history_converted_file)


@pytest.fixture(scope="session")
def matches_converted() -> pd.DataFrame:
    matches_converted_file = INPUTS_DIR / "convert_matches.pkl"
    return pd.read_pickle(matches_converted_file)


@pytest.fixture(scope="session")
def match_converted() -> pd.DataFrame:
    match_converted_file = INPUTS_DIR / "convert_match.pkl"
    return pd.read_pickle(match_converted_file)


@pytest.fixture(scope="session")
def num_online_converted() -> pd.DataFrame:
    num_online_converted_file = INPUTS_DIR / "convert_num_online.pkl"
    return pd.read_pickle(num_online_converted_file)
