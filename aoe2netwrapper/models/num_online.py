"""
aoe2netwrapper.models.num_online
--------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/stats/players
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class NumPlayers(BaseModel):
    """A model to encapsulate the metrics from the num_online API."""

    steam: int | None = Field(None, description="Number of players from Steam")
    multiplayer: int | None = Field(None, description="Number of people playing multiplayer")
    looking: int | None = Field(None, description="Number of players currently looking for a game")
    in_game: int | None = Field(None, description="Number of players currently playing")
    multiplayer_1h: int | None = Field(None, description="Number of multiplayer players the past hour")
    multiplayer_24h: int | None = Field(None, description="Number of multiplayer players the past 24 hour")


class PlayerCountTimePoint(BaseModel):
    """A model to encapsulate a timestamp datapoint of the num_online API metrics."""

    time: int | None = Field(None, description="Timestamp of the metrics data point")
    num_players: NumPlayers | None = Field(None, description="A NumPlayer object with the metrics")


class NumOnlineResponse(BaseModel):
    """A model to encapsulate the response from the num_online API."""

    app_id: int | None = Field(None, description="Unclear")
    player_stats: list[PlayerCountTimePoint] | None = Field(
        None, description="List of metrics at different points in time"
    )
