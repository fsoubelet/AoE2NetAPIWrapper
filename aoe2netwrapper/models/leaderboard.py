"""
aoe2netwrapper.models.leaderboard
---------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/leaderboard
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class LeaderBoardSpot(BaseModel):
    profile_id: int
    rank: int
    rating: int
    steam_id: int
    icon: Any = None
    name: str
    clan: Optional[str] = Field(...)
    country: str
    previous_rating: int
    highest_rating: int
    streak: int
    lowest_streak: int
    highest_streak: int
    games: int
    wins: int
    losses: int
    drops: int
    last_match: int
    last_match_time: int


class LeaderBoardResponse(BaseModel):
    total: int
    leaderboard_id: int
    start: int
    count: int
    leaderboard: List[LeaderBoardSpot]
