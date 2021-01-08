"""
aoe2netwrapper.models.leaderboard
---------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/leaderboard
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class LeaderBoardSpot(BaseModel):
    profile_id: Optional[int] = Field(None)
    rank: Optional[int] = Field(None)
    rating: Optional[int] = Field(None)
    steam_id: Optional[int] = Field(None)
    icon: Any = None
    name: Optional[str] = Field(None)
    clan: Optional[str] = Field(None)
    country: Optional[str] = Field(None)
    previous_rating: Optional[int] = Field(None)
    highest_rating: Optional[int] = Field(None)
    streak: Optional[int] = Field(None)
    lowest_streak: Optional[int] = Field(None)
    highest_streak: Optional[int] = Field(None)
    games: Optional[int] = Field(None)
    wins: Optional[int] = Field(None)
    losses: Optional[int] = Field(None)
    drops: Optional[int] = Field(None)
    last_match: Optional[int] = Field(None)
    last_match_time: Optional[int] = Field(None)


class LeaderBoardResponse(BaseModel):
    total: Optional[int] = Field(None)
    leaderboard_id: Optional[int] = Field(None)
    start: Optional[int] = Field(None)
    count: Optional[int] = Field(None)
    leaderboard: Optional[List[LeaderBoardSpot]] = Field(None)
