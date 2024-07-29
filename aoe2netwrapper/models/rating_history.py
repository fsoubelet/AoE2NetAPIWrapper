"""
aoe2netwrapper.models.rating_history
------------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/player/ratinghistory
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class RatingTimePoint(BaseModel):
    """An object to encapsulate any entry in the list of returned ranking timestamped data points."""

    rating: int | None = Field(None, description="The player's rating in the ELO system")
    num_wins: int | None = Field(None, description="Total amount of wins")
    num_losses: int | None = Field(None, description="Total amount of losses")
    streak: int | None = Field(None, description="Current number of consecutive wins")
    drops: int | None = Field(None, description="Number of games dropped out of")
    timestamp: int | None = Field(None, description="Timestamp of the metrics")
