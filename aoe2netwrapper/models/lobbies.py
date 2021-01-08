"""
aoe2netwrapper.models.lobbies
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/lobbies
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class LobbyMember(BaseModel):
    profile_id: Optional[int] = Field(None)
    steam_id: Optional[int] = Field(None)
    name: Optional[str] = Field(None)
    clan: Optional[str] = Field(None)
    country: Optional[str] = Field(None)
    slot: Optional[int] = Field(None)
    slot_type: Optional[int] = Field(None)
    rating: Optional[int] = Field(None)
    rating_change: Any = None
    games: Optional[int] = Field(None)
    wins: Optional[int] = Field(None)
    streak: Optional[int] = Field(None)
    drops: Optional[int] = Field(None)
    color: Optional[str] = Field(None)
    team: Optional[str] = Field(None)
    civ: Optional[int] = Field(None)
    won: Optional[int] = Field(None)


class MatchLobby(BaseModel):
    match_id: Optional[int] = Field(None)
    lobby_id: Optional[int] = Field(None)
    match_uuid: Optional[str] = Field(None)
    version: Optional[int] = Field(None)
    name: Optional[str] = Field(None)
    num_players: Optional[int] = Field(None)
    num_slots: Optional[int] = Field(None)
    average_rating: Optional[int] = Field(None)
    cheats: Optional[bool] = Field(None)
    full_tech_tree: Optional[bool] = Field(None)
    ending_age: Optional[int] = Field(None)
    expansion: Optional[str] = Field(None)
    game_type: Optional[int] = Field(None)
    has_custom_content: Optional[bool] = Field(None)
    has_password: Optional[bool] = Field(None)
    lock_speed: Optional[bool] = Field(None)
    lock_teams: Optional[bool] = Field(None)
    map_size: Optional[int] = Field(None)
    map_type: Optional[int] = Field(None)
    pop: Optional[int] = Field(None)
    ranked: Optional[bool] = Field(None)
    leaderboard_id: Optional[int] = Field(None)
    rating_type: Optional[int] = Field(None)
    resources: Optional[int] = Field(None)
    rms: Optional[str] = Field(None)
    scenario: Optional[str] = Field(None)
    server: Optional[str] = Field(None)
    shared_exploration: Optional[bool] = Field(None)
    speed: Optional[int] = Field(None)
    starting_age: Optional[int] = Field(None)
    team_together: Optional[bool] = Field(None)
    team_positions: Optional[bool] = Field(None)
    treaty_length: Optional[int] = Field(None)
    turbo: Optional[bool] = Field(None)
    victory: Optional[int] = Field(None)
    victory_time: Optional[int] = Field(None)
    visibility: Optional[int] = Field(None)
    opened: Optional[int] = Field(None)
    started: Any = None
    finished: Any = None
    players: Optional[List[LobbyMember]] = Field(None)
