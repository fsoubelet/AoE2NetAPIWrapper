"""
aoe2netwrapper.models.num_online
--------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/stats/players
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class NumPlayers(BaseModel):
    steam: Optional[int] = Field(None, description="Number of players from Steam")
    multiplayer: Optional[int] = Field(None, description="Number of people playing multiplayer")
    looking: Optional[int] = Field(None, description="Number of players currently looking for a game")
    in_game: Optional[int] = Field(None, description="Number of players currently playing")
    multiplayer_1h: Optional[int] = Field(None, description="Number of multiplayer players the past hour")
    multiplayer_24h: Optional[int] = Field(None, description="Number of multiplayer players the past 24 hour")


class PlayerCountTimePoint(BaseModel):
    time: Optional[int] = Field(None, description="Timestamp of the metrics data point")
    num_players: Optional[NumPlayers] = Field(None, description="A NumPlayer object with the metrics")


class NumOnlineResponse(BaseModel):
    app_id: Optional[int] = Field(None, description="Unclear")
    player_stats: Optional[List[PlayerCountTimePoint]] = Field(
        None, description="List of metrics at different points in time"
    )
