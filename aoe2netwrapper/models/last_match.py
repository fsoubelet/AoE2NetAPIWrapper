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
    profile_id: Optional[int] = Field(None, description="The ID attributed to the player by AoE II")
    steam_id: Optional[int] = Field(None, description="ID of the player on the Steam platform")
    name: Optional[str] = Field(None, description="Name of the player the query was made for")
    country: Optional[str] = Field(None, description="Country the player connected from")
    last_match: Optional[MatchLobby] = Field(None, description="MatchLobby  of the last match")
