"""
aoe2netwrapper.models.num_online
--------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/stats/players
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class NumPlayers(BaseModel):
    steam: Optional[int] = Field(None)
    multiplayer: Optional[int] = Field(None)
    looking: Optional[int] = Field(None)
    in_game: Optional[int] = Field(None)
    multiplayer_1h: Optional[int] = Field(None)
    multiplayer_24h: Optional[int] = Field(None)


class PlayerCountTimePoint(BaseModel):
    time: Optional[int] = Field(None)
    num_players: Optional[NumPlayers] = Field(None)


class NumOnlineResponse(BaseModel):
    app_id: Optional[int] = Field(None)
    player_stats: Optional[List[PlayerCountTimePoint]] = Field(None)
