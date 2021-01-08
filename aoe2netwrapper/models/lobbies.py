"""
aoe2netwrapper.models.lobbies
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/lobbies
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class LobbyMember(BaseModel):
    profile_id: Optional[int] = Field(...)
    steam_id: Optional[int] = Field(...)
    name: Optional[str] = Field(...)
    clan: Optional[str] = Field(...)
    country: Optional[str] = Field(...)
    slot: Optional[int] = Field(...)
    slot_type: Optional[int] = Field(...)
    rating: Optional[int] = Field(...)
    rating_change: Any = None
    games: Optional[int] = Field(...)
    wins: Optional[int] = Field(...)
    streak: Optional[int] = Field(...)
    drops: Optional[int] = Field(...)
    color: Optional[str] = Field(...)
    team: Optional[str] = Field(...)
    civ: Optional[int] = Field(...)
    won: Optional[int] = Field(...)


class Lobby(BaseModel):
    match_id: Optional[int] = Field(...)
    lobby_id: Optional[int] = Field(...)
    match_uuid: Optional[str] = Field(...)
    version: Optional[int] = Field(...)
    name: Optional[str] = Field(...)
    num_players: Optional[int] = Field(...)
    num_slots: Optional[int] = Field(...)
    average_rating: Optional[int] = Field(...)
    cheats: Optional[bool] = Field(...)
    full_tech_tree: Optional[bool] = Field(...)
    ending_age: Optional[int] = Field(...)
    expansion: Optional[str] = Field(...)
    game_type: Optional[int] = Field(...)
    has_custom_content: Optional[bool] = Field(...)
    has_password: Optional[bool] = Field(...)
    lock_speed: Optional[bool] = Field(...)
    lock_teams: Optional[bool] = Field(...)
    map_size: Optional[int] = Field(...)
    map_type: Optional[int] = Field(...)
    pop: Optional[int] = Field(...)
    ranked: Optional[bool] = Field(...)
    leaderboard_id: Optional[int] = Field(...)
    rating_type: Optional[int] = Field(...)
    resources: Optional[int] = Field(...)
    rms: Optional[str] = Field(...)
    scenario: Optional[str] = Field(...)
    server: Optional[str] = Field(...)
    shared_exploration: Optional[bool] = Field(...)
    speed: Optional[int] = Field(...)
    starting_age: Optional[int] = Field(...)
    team_together: Optional[bool] = Field(...)
    team_positions: Optional[bool] = Field(...)
    treaty_length: Optional[int] = Field(...)
    turbo: Optional[bool] = Field(...)
    victory: Optional[int] = Field(...)
    victory_time: Optional[int] = Field(...)
    visibility: Optional[int] = Field(...)
    opened: Optional[int] = Field(...)
    started: Any = None
    finished: Any = None
    players: Optional[List[LobbyMember]] = Field(...)
