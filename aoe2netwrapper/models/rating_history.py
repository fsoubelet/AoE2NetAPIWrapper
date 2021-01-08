"""
aoe2netwrapper.models.rating_history
------------------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/player/ratinghistory
"""
from typing import Optional

from pydantic import BaseModel, Field


class RatingTimePoint(BaseModel):
    rating: Optional[int] = Field(None)
    num_wins: Optional[int] = Field(None)
    num_losses: Optional[int] = Field(None)
    streak: Optional[int] = Field(None)
    drops: Optional[int] = Field(None)
    timestamp: Optional[int] = Field(None)
