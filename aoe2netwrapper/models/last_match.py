"""
aoe2netwrapper.models.lobbies
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/lobbies
"""
from typing import Any, List, Optional

from pydantic import BaseModel, Field

from aoe2netwrapper.models.lobbies import MatchLobby


class LastMatchResponse(BaseModel):
    profile_id: Optional[int] = Field(...)
    steam_id: Optional[int] = Field(...)
    name: Optional[str] = Field(...)
    country: Optional[str] = Field(...)
    last_match: Optional[MatchLobby] = Field(...)
