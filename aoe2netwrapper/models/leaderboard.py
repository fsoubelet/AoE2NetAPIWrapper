"""
aoe2netwrapper.models.leaderboard
---------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/leaderboard
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class LeaderBoardSpot(BaseModel):
    profile_id: Optional[int] = Field(None, description="The ID attributed to the player by AoE II")
    rank: Optional[int] = Field(None, description="The player's rank on the ladder")
    rating: Optional[int] = Field(None, description="The player's rating in the ELO system")
    steam_id: Optional[int] = Field(None, description="ID of the player on the Steam platform")
    icon: Optional[Any] = Field(None, description="The player's icon")
    name: Optional[str] = Field(None, description="The player's in-game name")
    clan: Optional[str] = Field(None, description="The player's clan / team")
    country: Optional[str] = Field(None, description="Country the player connected from")
    previous_rating: Optional[int] = Field(None, description="Player's rating at their last match")
    highest_rating: Optional[int] = Field(None, description="Highest rating achieved by the player")
    streak: Optional[int] = Field(None, description="Current number of consecutive wins")
    lowest_streak: Optional[int] = Field(None, description="Lowest streak achieved by this player")
    highest_streak: Optional[int] = Field(None, description="Highest streak achieved by this player")
    games: Optional[int] = Field(None, description="The total amount of games played by the player")
    wins: Optional[int] = Field(None, description="Total amount of wins")
    losses: Optional[int] = Field(None, description="Total amount of losses")
    drops: Optional[int] = Field(None, description="Number of games the player dropped out of")
    last_match: Optional[int] = Field(None, description="Timestamp of the last game played")
    last_match_time: Optional[int] = Field(None, description="Timestamp of the last game played")


class LeaderBoardResponse(BaseModel):
    total: Optional[int] = Field(None, description="Total number of entries in the leaderboard")
    leaderboard_id: Optional[int] = Field(None, description="ID of the leaderboard queried, aka game type")
    start: Optional[int] = Field(None, description="Starting rank of the first entry in the response")
    count: Optional[int] = Field(None, description="Number of entries returned")
    leaderboard: Optional[List[LeaderBoardSpot]] = Field(None, description="List of LeaderBoardSport entries")
