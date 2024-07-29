"""
aoe2netwrapper.models.leaderboard
---------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/leaderboard
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class LeaderBoardSpot(BaseModel):
    """An object to encapsulate any entry in the leaderboard ranking."""

    profile_id: int | None = Field(None, description="The ID attributed to the player by AoE II")
    rank: int | None = Field(None, description="The player's rank on the ladder")
    rating: int | None = Field(None, description="The player's rating in the ELO system")
    steam_id: int | None = Field(None, description="ID of the player on the Steam platform")
    icon: Any | None = Field(None, description="The player's icon")
    name: str | None = Field(None, description="The player's in-game name")
    clan: str | None = Field(None, description="The player's clan / team")
    country: str | None = Field(None, description="Country the player connected from")
    previous_rating: int | None = Field(None, description="Player's rating at their last match")
    highest_rating: int | None = Field(None, description="Highest rating achieved by the player")
    streak: int | None = Field(None, description="Current number of consecutive wins")
    lowest_streak: int | None = Field(None, description="Lowest streak achieved by this player")
    highest_streak: int | None = Field(None, description="Highest streak achieved by this player")
    games: int | None = Field(None, description="The total amount of games played by the player")
    wins: int | None = Field(None, description="Total amount of wins")
    losses: int | None = Field(None, description="Total amount of losses")
    drops: int | None = Field(None, description="Number of games the player dropped out of")
    last_match: int | None = Field(None, description="Timestamp of the last game played")
    last_match_time: int | None = Field(None, description="Timestamp of the last game played")


class LeaderBoardResponse(BaseModel):
    """An object to encapsulate the response from the leaderboard API."""

    total: int | None = Field(None, description="Total number of entries in the leaderboard")
    leaderboard_id: int | None = Field(None, description="ID of the leaderboard queried, aka game type")
    start: int | None = Field(None, description="Starting rank of the first entry in the response")
    count: int | None = Field(None, description="Number of entries returned")
    leaderboard: list[LeaderBoardSpot] | None = Field(None, description="List of LeaderBoardSport entries")
