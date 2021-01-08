"""
aoe2netwrapper.models.rating_history
------------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/player/ratinghistory
"""
from typing import Optional

from pydantic import BaseModel, Field


class RatingTimePoint(BaseModel):
    """An object to encapsulate any entry in the list of returned ranking timestamped data points."""

    rating: Optional[int] = Field(None, description="The player's rating in the ELO system")
    num_wins: Optional[int] = Field(None, description="Total amount of wins")
    num_losses: Optional[int] = Field(None, description="Total amount of losses")
    streak: Optional[int] = Field(None, description="Current number of consecutive wins")
    drops: Optional[int] = Field(None, description="Number of games dropped out of")
    timestamp: Optional[int] = Field(None, description="Timestamp of the metrics")
