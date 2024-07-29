"""
aoe2netwrapper.models.lobbies
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/lobbies
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class LobbyMember(BaseModel):
    """An object to encapsulate any entry in the leaderboard ranking."""

    profile_id: int | None = Field(None, description="The ID attributed to the member by AoE II")
    steam_id: int | None = Field(None, description="ID of the member on the Steam platform")
    name: str | None = Field(None, description="The member's in-game name")
    clan: str | None = Field(None, description="The member's clan / team")
    country: str | None = Field(None, description="Country the player connected from")
    slot: int | None = Field(None, description="Slot number of the member in the lobby")
    slot_type: int | None = Field(None, description="ID of the role of the member in the lobby")
    rating: int | None = Field(None, description="The member's rating in the ELO system")
    rating_change: Any | None = Field(None, description="The difference to the member's previous rating")
    games: int | None = Field(None, description="The total amount of games played by the member")
    wins: int | None = Field(None, description="Total amount of wins of the member")
    streak: int | None = Field(None, description="Current number of consecutive wins of the member")
    drops: int | None = Field(None, description="Number of games the member dropped out of")
    color: str | int | None = Field(None, description="The member's in-game color")
    team: int | None = Field(None, description="The member's team number for the game")
    civ: int | None = Field(None, description="The member's civilization pick for the game")
    won: int | None = Field(None, description="Unclear")


class MatchLobby(BaseModel):
    """An object to encapsulate any entry in the list of returned lobbies."""

    match_id: int | None = Field(None, description="ID attributed to the match this lobby is for")
    lobby_id: int | None = Field(None, description="ID attributed to the lobby itself")
    match_uuid: str | None = Field(None, description="UUID attributed to the match this lobby is for")
    version: int | None = Field(None, description="Version number of the game patch")
    name: str | None = Field(None, description="Name given to the lobby")
    num_players: int | None = Field(None, description="Number of players in the lobby")
    num_slots: int | None = Field(None, description="Number of player slots in the lobby")
    average_rating: int | None = Field(None, description="Average rating of the members in the lobby")
    cheats: bool | None = Field(None, description="Whether cheats are enabled")
    full_tech_tree: bool | None = Field(None, description="Whether the full tech tree is set unlocked")
    ending_age: int | None = Field(None, description="The last attainable age for the game")
    expansion: str | None = Field(None, description="The expansion patch enabled")
    game_type: int | None = Field(None, description="ID of the game type, same a leaderboard IDs")
    has_custom_content: bool | None = Field(None, description="Whether the game has custom content")
    has_password: bool | None = Field(None, description="Whether the lobby is password-protected")
    lock_speed: bool | None = Field(None, description="Whether the game speed setting is locked")
    lock_teams: bool | None = Field(None, description="Whether the player teams are locked")
    map_size: int | None = Field(None, description="The game's map size setting")
    map_type: int | None = Field(None, description="ID of the game's map type")
    pop: int | None = Field(None, description="The max population setting for the game")
    ranked: bool | None = Field(None, description="Whether the lobby is for a ranked game")
    leaderboard_id: int | None = Field(None, description="Leaderboard ID for the game type")
    rating_type: int | None = Field(None, description="The rating ID for the game")
    resources: int | None = Field(None, description="The setting for players' starting resources")
    rms: str | None = Field(None, description="Unclear")
    scenario: str | None = Field(None, description="The activated scenario for the game")
    server: str | None = Field(None, description="The server hosting the game")
    shared_exploration: bool | None = Field(None, description="Whether the map exploration is shared")
    speed: int | None = Field(None, description="The game speed")
    starting_age: int | None = Field(None, description="The starting age for the game")
    team_together: bool | None = Field(None, description="Whether players can team up")
    team_positions: bool | None = Field(None, description="Whether players start with team positions")
    treaty_length: int | None = Field(None, description="Duration of the 'no attack' treaty in minutes")
    turbo: bool | None = Field(None, description="Whether the game will be played in turbo mode")
    victory: int | None = Field(None, description="ID of the game's victory condition")
    victory_time: int | None = Field(None, description="Setting of the victory time limit")
    visibility: int | None = Field(None, description="ID of the visibility setting")
    opened: int | None = Field(None, description="Timestamp of the lobby's creation")
    started: Any | None = Field(None, description="Timestamp of the game's start")
    finished: Any | None = Field(None, description="Timestamp of the game's end")
    players: list[LobbyMember] | None = Field(None, description="List of members in the lobby")
