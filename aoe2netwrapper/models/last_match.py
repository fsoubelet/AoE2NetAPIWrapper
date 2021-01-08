"""
aoe2netwrapper.models.lobbies
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/lobbies
"""
from typing import Optional

from pydantic import BaseModel, Field

from aoe2netwrapper.models.lobbies import MatchLobby


class LastMatchResponse(BaseModel):
    profile_id: Optional[int] = Field(None)
    steam_id: Optional[int] = Field(None)
    name: Optional[str] = Field(None)
    country: Optional[str] = Field(None)
    last_match: Optional[MatchLobby] = Field(None)
