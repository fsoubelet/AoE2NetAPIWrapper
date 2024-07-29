"""
aoe2netwrapper.models.num_online
--------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/stats/players
"""
from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class NumPlayers(BaseModel):
    """A model to encapsulate the metrics from the num_online API."""

    steam: Optional[int] = Field(None, description="Number of players from Steam")
    multiplayer: Optional[int] = Field(None, description="Number of people playing multiplayer")
    looking: Optional[int] = Field(None, description="Number of players currently looking for a game")
    in_game: Optional[int] = Field(None, description="Number of players currently playing")
    multiplayer_1h: Optional[int] = Field(None, description="Number of multiplayer players the past hour")
    multiplayer_24h: Optional[int] = Field(None, description="Number of multiplayer players the past 24 hour")


class PlayerCountTimePoint(BaseModel):
    """A model to encapsulate a timestamp datapoint of the num_online API metrics."""

    time: Optional[int] = Field(None, description="Timestamp of the metrics data point")
    num_players: Optional[NumPlayers] = Field(None, description="A NumPlayer object with the metrics")


class NumOnlineResponse(BaseModel):
    """A model to encapsulate the response from the num_online API."""

    app_id: Optional[int] = Field(None, description="Unclear")
    player_stats: Optional[List[PlayerCountTimePoint]] = Field(
        None, description="List of metrics at different points in time"
    )
