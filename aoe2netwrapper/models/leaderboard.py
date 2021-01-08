"""
aoe2netwrapper.models.leaderboard
---------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/leaderboard
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class LeaderBoardSpot(BaseModel):
    profile_id: Optional[int] = Field(...)
    rank: Optional[int] = Field(...)
    rating: Optional[int] = Field(...)
    steam_id: Optional[int] = Field(...)
    icon: Any = None
    name: Optional[str] = Field(...)
    clan: Optional[str] = Field(...)
    country: Optional[str] = Field(...)
    previous_rating: Optional[int] = Field(...)
    highest_rating: Optional[int] = Field(...)
    streak: Optional[int] = Field(...)
    lowest_streak: Optional[int] = Field(...)
    highest_streak: Optional[int] = Field(...)
    games: Optional[int] = Field(...)
    wins: Optional[int] = Field(...)
    losses: Optional[int] = Field(...)
    drops: Optional[int] = Field(...)
    last_match: Optional[int] = Field(...)
    last_match_time: Optional[int] = Field(...)


class LeaderBoardResponse(BaseModel):
    total: Optional[int] = Field(...)
    leaderboard_id: Optional[int] = Field(...)
    start: Optional[int] = Field(...)
    count: Optional[int] = Field(...)
    leaderboard: Optional[List[LeaderBoardSpot]] = Field(...)
