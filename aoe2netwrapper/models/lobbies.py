"""
aoe2netwrapper.models.lobbies
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/lobbies
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class LobbyMember(BaseModel):
    profile_id: Optional[int] = Field(None, description="The ID attributed to the member by AoE II")
    steam_id: Optional[int] = Field(None, description="ID of the member on the Steam platform")
    name: Optional[str] = Field(None, description="The member's in-game name")
    clan: Optional[str] = Field(None, description="The member's clan / team")
    country: Optional[str] = Field(None, description="Country the player connected from")
    slot: Optional[int] = Field(None, description="Slot number of the member in the lobby")
    slot_type: Optional[int] = Field(None, description="ID of the role of the member in the lobby")
    rating: Optional[int] = Field(None, description="The member's rating in the ELO system")
    rating_change: Optional[Any] = Field(None, description="The difference to the member's previous rating")
    games: Optional[int] = Field(None, description="The total amount of games played by the member")
    wins: Optional[int] = Field(None, description="Total amount of wins of the member")
    streak: Optional[int] = Field(None, description="Current number of consecutive wins of the member")
    drops: Optional[int] = Field(None, description="Number of games the member dropped out of")
    color: Optional[str] = Field(None, description="The member's in-game color")
    team: Optional[str] = Field(None, description="The member's team number for the game")
    civ: Optional[int] = Field(None, description="The member's civilization pick for the game")
    won: Optional[int] = Field(None, description="Unclear")


class MatchLobby(BaseModel):
    match_id: Optional[int] = Field(None, description="ID attributed to the match this lobby is for")
    lobby_id: Optional[int] = Field(None, description="ID attributed to the lobby itself")
    match_uuid: Optional[str] = Field(None, description="UUID attributed to the match this lobby is for")
    version: Optional[int] = Field(None, description="Version number of the game patch")
    name: Optional[str] = Field(None, description="Name given to the lobby")
    num_players: Optional[int] = Field(None, description="Number of players in the lobby")
    num_slots: Optional[int] = Field(None, description="Number of player slots in the lobby")
    average_rating: Optional[int] = Field(None, description="Average rating of the members in the lobby")
    cheats: Optional[bool] = Field(None, description="Whether cheats are enabled")
    full_tech_tree: Optional[bool] = Field(None, description="Whether the full tech tree is set unlocked")
    ending_age: Optional[int] = Field(None, description="The last attainable age for the game")
    expansion: Optional[str] = Field(None, description="The expansion patch enabled")
    game_type: Optional[int] = Field(None, description="ID of the game type, same a leaderboard IDs")
    has_custom_content: Optional[bool] = Field(None, description="Whether the game has custom content")
    has_password: Optional[bool] = Field(None, description="Whether the lobby is password-protected")
    lock_speed: Optional[bool] = Field(None, description="Whether the game speed setting is locked")
    lock_teams: Optional[bool] = Field(None, description="Whether the player teams are locked")
    map_size: Optional[int] = Field(None, description="The game's map size setting")
    map_type: Optional[int] = Field(None, description="ID of the game's map type")
    pop: Optional[int] = Field(None, description="The max population setting for the game")
    ranked: Optional[bool] = Field(None, description="Whether the lobby is for a ranked game")
    leaderboard_id: Optional[int] = Field(None, description="Leaderboard ID for the game type")
    rating_type: Optional[int] = Field(None, description="The rating ID for the game")
    resources: Optional[int] = Field(None, description="The setting for players' starting resources")
    rms: Optional[str] = Field(None, description="Unclear")
    scenario: Optional[str] = Field(None, description="The activated scenario for the game")
    server: Optional[str] = Field(None, description="The server hosting the game")
    shared_exploration: Optional[bool] = Field(None, description="Whether the map exploration is shared")
    speed: Optional[int] = Field(None, description="The game speed")
    starting_age: Optional[int] = Field(None, description="The starting age for the game")
    team_together: Optional[bool] = Field(None, description="Whether players can team up")
    team_positions: Optional[bool] = Field(None, description="Whether players start with team positions")
    treaty_length: Optional[int] = Field(None, description="Duration of the 'no attack' treaty in minutes")
    turbo: Optional[bool] = Field(None, description="Whether the game will be played in turbo mode")
    victory: Optional[int] = Field(None, description="ID of the game's victory condition")
    victory_time: Optional[int] = Field(None, description="Setting of the victory time limit")
    visibility: Optional[int] = Field(None, description="ID of the visibility setting")
    opened: Optional[int] = Field(None, description="Timestamp of the lobby's creation")
    started: Optional[Any] = Field(None, description="Timestamp of the game's start")
    finished: Optional[Any] = Field(None, description="Timestamp of the game's end")
    players: Optional[List[LobbyMember]] = Field(None, description="List of members in the lobby")
